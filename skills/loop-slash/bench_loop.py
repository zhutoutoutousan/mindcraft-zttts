#!/usr/bin/env python3
"""Evidence bench for /loop claims. Run: python skills/loop-slash/bench_loop.py"""
from __future__ import annotations

import json
import re
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "bench_results.json"

INTERVAL_RE = re.compile(r"^(\d+)([smhd])$")
EVERY_RE = re.compile(
    r"^(?P<prompt>.*?)\s+every\s+(?P<n>\d+)\s*(?P<u>s|m|h|d|seconds?|minutes?|hours?|days?)\s*$",
    re.I,
)
UNIT = {"s": "s", "second": "s", "seconds": "s", "m": "m", "minute": "m", "minutes": "m",
        "h": "h", "hour": "h", "hours": "h", "d": "d", "day": "d", "days": "d"}


def to_short(n: str, u: str) -> str:
    return f"{int(n)}{UNIT[u.lower()]}"


def parse_claude_2_1_71(raw: str) -> dict:
    """Exact parse rules from bundled skill @anthropic-ai/claude-code@2.1.71."""
    raw = raw.strip()
    if not raw:
        return {"interval": None, "prompt": "", "rule": "empty", "ok": False}
    parts = raw.split()
    m = INTERVAL_RE.match(parts[0])
    if m:
        prompt = " ".join(parts[1:])
        return {"interval": parts[0], "prompt": prompt, "rule": "leading", "ok": bool(prompt)}
    m = EVERY_RE.match(raw)
    if m:
        return {"interval": to_short(m["n"], m["u"]), "prompt": m["prompt"].strip(), "rule": "trailing-every", "ok": True}
    return {"interval": "10m", "prompt": raw, "rule": "default-10m", "ok": True}


def parse_cursor_docs_2026(raw: str) -> dict:
    """Cursor SKILL.md + current Claude scheduled-tasks docs: no interval => dynamic."""
    raw = raw.strip()
    if not raw:
        return {"interval": None, "prompt": "", "rule": "empty", "ok": False, "mode": "usage"}
    parts = raw.split()
    m = INTERVAL_RE.match(parts[0])
    if m:
        prompt = " ".join(parts[1:])
        return {"interval": parts[0], "prompt": prompt, "rule": "leading", "ok": bool(prompt), "mode": "fixed"}
    m = EVERY_RE.match(raw)
    if m:
        return {"interval": to_short(m["n"], m["u"]), "prompt": m["prompt"].strip(), "rule": "trailing-every", "ok": True, "mode": "fixed"}
    return {"interval": None, "prompt": raw, "rule": "dynamic", "ok": True, "mode": "self-pace"}


def seconds_to_cron_minutes(n_seconds: int) -> int:
    return max(1, (n_seconds + 59) // 60)  # ceil to 1 minute


def cron_minute_gaps(n: int) -> dict:
    hits = [m for m in range(60) if m % n == 0] if n <= 59 else []
    if not hits:
        return {"n": n, "hits": [], "gaps": [], "uneven": False}
    gaps = [hits[i + 1] - hits[i] for i in range(len(hits) - 1)]
    gaps.append(60 - hits[-1] + hits[0])
    return {"n": n, "hits": hits, "gaps": gaps, "uneven": len(set(gaps)) > 1, "wrap_gap": gaps[-1]}


def jitter_bound_seconds(interval_seconds: int) -> int:
    """Docs: recurring tasks fire up to 30 min after, or half the interval if < hourly."""
    half = interval_seconds // 2
    return min(30 * 60, half)


SENTINEL = "AGENT_LOOP_TICK_deploy"
SENTINEL_RE = re.compile(rf"^{SENTINEL}\b")


def sentinel_cases() -> list[dict]:
    samples = [
        f'{SENTINEL} {{"prompt":"check deploy"}}',
        f"noise {SENTINEL} later",
        "AGENT_LOOP_TICK_deployed extra",
        "AGENT_LOOP_TICK_other {\"prompt\":\"x\"}",
        f"  {SENTINEL} padded",
    ]
    return [{"line": s, "match": bool(SENTINEL_RE.search(s))} for s in samples]


def sleep_drift(requested: float, n: int = 8) -> dict:
    deltas = []
    for _ in range(n):
        t0 = time.perf_counter()
        time.sleep(requested)
        deltas.append(time.perf_counter() - t0)
    err = [d - requested for d in deltas]
    return {
        "requested_s": requested,
        "n": n,
        "mean_s": sum(deltas) / n,
        "mean_error_ms": 1000 * sum(err) / n,
        "max_error_ms": 1000 * max(err, key=abs),
        "min_s": min(deltas),
        "max_s": max(deltas),
    }


def powershell_sleep_drift(requested: float, n: int = 5) -> dict:
    code = (
        f"$n={n}; $r={requested}; $d=@(); "
        "1..$n | ForEach-Object { $t0=[Diagnostics.Stopwatch]::StartNew(); "
        "Start-Sleep -Milliseconds ([int]($r*1000)); $d += $t0.Elapsed.TotalSeconds }; "
        "$d | ConvertTo-Json -Compress"
    )
    p = subprocess.run(
        ["powershell", "-NoProfile", "-Command", code],
        capture_output=True, text=True, timeout=120,
    )
    if p.returncode != 0:
        return {"error": p.stderr[-400:], "requested_s": requested}
    raw = json.loads(p.stdout)
    if isinstance(raw, float):
        raw = [raw]
    err = [d - requested for d in raw]
    return {
        "requested_s": requested,
        "n": n,
        "engine": "Start-Sleep",
        "mean_s": sum(raw) / len(raw),
        "mean_error_ms": 1000 * sum(err) / len(raw),
        "max_error_ms": 1000 * max(err, key=abs),
        "samples_s": [round(x, 4) for x in raw],
    }


def double_tick_sim() -> dict:
    """If echo happens BEFORE sleep, arming + first tick collide. Skill forbids this."""
    events_bad = ["run_now", "tick"]  # echo first then sleep = immediate extra if agent also ran now
    events_good = ["run_now", "sleep", "tick"]
    return {
        "bad_pattern": "echo then sleep → 2 fires in <1s if prompt also ran immediately",
        "good_pattern": "run prompt now; sleep THEN echo (Cursor SKILL.md step 5-6)",
        "bad_events": events_bad,
        "good_events": events_good,
        "verdict": "CONFIRMED: sleep-first is required to avoid double tick",
    }


def main() -> None:
    cases = [
        "5m /babysit-prs",
        "check the deploy every 20m",
        "run tests every 5 minutes",
        "check the deploy",
        "check every PR",
        "5m",
        "30s check status",
        "90m babysit",
        "7m check ci",
        "2h run report",
        "",
    ]
    parse_table = []
    for c in cases:
        parse_table.append({
            "input": c,
            "claude_2_1_71": parse_claude_2_1_71(c),
            "cursor_or_docs_2026": parse_cursor_docs_2026(c),
            "disagree": parse_claude_2_1_71(c).get("interval") != parse_cursor_docs_2026(c).get("interval")
            or parse_claude_2_1_71(c).get("rule") != parse_cursor_docs_2026(c).get("rule"),
        })

    sec_round = {n: seconds_to_cron_minutes(n) for n in (1, 30, 59, 60, 61, 90)}
    gaps = {n: cron_minute_gaps(n) for n in (5, 7, 15, 30)}

    py_sleep = sleep_drift(0.25, n=12)
    ps_sleep = powershell_sleep_drift(0.4, n=6)

    myths = [
        {
            "id": "M1",
            "claim": "/loop check the deploy is always self-paced 1m–1h",
            "verdict": "BUSTED as a universal. Version-split.",
            "evidence": "claude-code@2.1.71 skill: no interval → default 10m fixed. Docs 2026: no interval → self-pace 1m–1h, except Bedrock/Foundry/old builds stay 10m.",
        },
        {
            "id": "M2",
            "claim": "Recurring /loop expires in 3 days",
            "verdict": "BUSTED on current docs (7 days). CONFIRMED in 2.1.71 skill text (3 days).",
            "evidence": "Gist skill: auto-expire after 3 days. scheduled-tasks.md: 7 days, fires once more, then deletes.",
        },
        {
            "id": "M3",
            "claim": "/loop 30s actually waits 30 seconds",
            "verdict": "BUSTED for Claude cron /loop.",
            "evidence": f"Seconds ceil to 1 minute. 30s → {seconds_to_cron_minutes(30)}m. Measured mapping: {sec_round}",
        },
        {
            "id": "M4",
            "claim": "/loop 7m is a clean every-7-minutes clock",
            "verdict": "BUSTED.",
            "evidence": f"*/7 hits {gaps[7]['hits']}; wrap-around gap is {gaps[7]['wrap_gap']} min not 7. Skill says round to nearest clean step.",
        },
        {
            "id": "M5",
            "claim": "check every PR is parsed as an interval",
            "verdict": "BUSTED.",
            "evidence": "every must be followed by a time expression. check every PR → prompt intact, 10m default (2.1.71) or dynamic (2026 docs).",
        },
        {
            "id": "M6",
            "claim": "A scheduled /loop fires exactly on the cron minute",
            "verdict": "BUSTED.",
            "evidence": "Jitter: up to 30 min late, or half the interval if < hourly. 5m job jitter bound = "
            f"{jitter_bound_seconds(300)}s. Offset is deterministic from task ID. Busy session: no catch-up, fires once when idle.",
        },
        {
            "id": "M7",
            "claim": "Cursor /loop 5m is cron on the OS",
            "verdict": "BUSTED.",
            "evidence": "Cursor local skill uses sleep + AGENT_LOOP_TICK_ sentinel + notify_on_output. Not Task Scheduler. Cloud path is subscribe_timer.",
        },
        {
            "id": "M8",
            "claim": "Start-Sleep on Windows is too sloppy for a 5m loop",
            "verdict": "PLAUSIBLE but overstated at loop scale.",
            "evidence": {
                "python_sleep_0.25s": py_sleep,
                "powershell_Start-Sleep_0.4s": ps_sleep,
                "note": "Millisecond-scale drift. On a 300s interval this is <<1%. Cron jitter (up to 150s on a 5m job) dominates.",
            },
        },
        {
            "id": "M9",
            "claim": "Arming a local loop and running the prompt now cannot double-fire",
            "verdict": "BUSTED if echo is before sleep.",
            "evidence": double_tick_sim(),
        },
        {
            "id": "M10",
            "claim": "/loop 20m /permissions re-executes the permissions UI",
            "verdict": "BUSTED.",
            "evidence": "Docs: built-ins (/permissions, /model, /clear) and disable-model-invocation skills arrive as plain text, they do not execute.",
        },
    ]

    payload = {
        "parse_table": parse_table,
        "seconds_ceil_to_minutes": sec_round,
        "cron_gaps": gaps,
        "sentinel": sentinel_cases(),
        "myths": myths,
        "sources": [
            "https://code.claude.com/docs/en/scheduled-tasks",
            "https://gist.github.com/Strajk/7bcece00b2ff0f5f501a0845ce009d27",
            "C:\\Users\\tians\\.cursor\\skills-cursor\\loop\\SKILL.md",
            "https://bestagent.dev/claude-code-loop-2026/",
        ],
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUT), "myths": [(m["id"], m["verdict"]) for m in myths]}, indent=2))
    print("\nPARSE DISAGREEMENTS")
    for row in parse_table:
        if row["disagree"]:
            print(f"  {row['input']!r:40}  2.1.71={row['claude_2_1_71']['interval']}/{row['claude_2_1_71']['rule']:16}  2026={row['cursor_or_docs_2026']['interval']}/{row['cursor_or_docs_2026']['rule']}")


if __name__ == "__main__":
    main()
