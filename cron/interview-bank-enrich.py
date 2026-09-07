#!/usr/bin/env python3
"""Interview bank theme enrich — titles/themes only, no answer paste.

    python cron/interview-bank-enrich.py --status
    python cron/interview-bank-enrich.py --gap
    python cron/interview-bank-enrich.py --zeitgeist
    python cron/interview-bank-enrich.py --stamp

Does not invent ANSWER. Does not write STUDY ANSWER. Does not scrape essays into pedagogy.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError, HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "pedagogy" / "_learn" / "mianling-agent-2026.toon.md"
STRATEGY = ROOT / "pedagogy" / "_learn" / "interview-prep-strategy.toon.md"
GRAPH = ROOT / "pedagogy" / "universe.graph.md"
MEZZ = ROOT / "mezzanine" / "interview-bank-enrich.toon.md"
MIANLING = "https://www.mianlingai.com/topics/ai-agent-interview-questions-2026/"
AMIT = "https://github.com/amitshekhariitbhu/ai-engineering-interview-questions"

EXPECTED_V = [
    "Agent",
    "AgentLoop",
    "AgentHarness",
    "ContextEngineering",
    "MCP",
    "CursorSkill",
    "MultiAgent",
    "ExperienceStore",
    "RAG",
    "AISafety",
    "InterviewPrep",
    "AutobiographicalMemory",
    "History",
    "AgentCore",
    "AgentHook",
    "AgentPlugin",
    "PromptEngineering",
    "Evaluation",
    "LLMOps",
]


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def graph_ids(text: str) -> set[str]:
    return set(re.findall(r"^V\s+(\S+)", text, re.M))


def parse_themes(text: str) -> list[dict]:
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("theme["):
            started = True
            continue
        if started and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            break
        if started and re.match(r"^\s+\S+,", line):
            parts = [p.strip() for p in line.strip().split(",", 4)]
            if len(parts) >= 4:
                rows.append(
                    {
                        "id": parts[0],
                        "label": parts[1],
                        "vertices": parts[2].split(),
                        "heat": parts[3],
                        "note": parts[4] if len(parts) > 4 else "",
                    }
                )
    return rows


def cmd_status() -> int:
    themes = parse_themes(read(THEME))
    ids = graph_ids(read(GRAPH))
    print(f"SOURCE {MIANLING}")
    print(f"SOURCE {AMIT}")
    print(f"themes {len(themes)} strategy={'yes' if STRATEGY.exists() else 'NO'}")
    for t in themes:
        missing = [v for v in t["vertices"] if v not in ids]
        flag = f" MISSING[{','.join(missing)}]" if missing else ""
        print(f"  [{t['heat']}] {t['id']}: {t['label']} → {t['vertices']}{flag}")
    return 0


def cmd_gap() -> int:
    ids = graph_ids(read(GRAPH))
    missing = [v for v in EXPECTED_V if v not in ids]
    print("expected_for_mianling_map")
    for v in EXPECTED_V:
        print(f"  {'OK' if v in ids else 'GAP'} {v}")
    if missing:
        print("ACTION add V/body+SOURCE or accept gap; do not invent CLAIM")
        return 1
    print("no vertex gaps vs EXPECTED_V")
    return 0


def fetch_head(url: str) -> tuple[int, str]:
    req = Request(url, headers={"User-Agent": "mindcraft-interview-bank-enrich/0.1"})
    try:
        with urlopen(req, timeout=25) as resp:
            raw = resp.read(120_000)
            code = getattr(resp, "status", 200) or 200
    except (URLError, HTTPError, TimeoutError) as exc:
        return 0, f"fetch_fail {exc}"
    try:
        text = raw.decode("utf-8", errors="replace")
    except Exception:
        text = ""
    # light signals only — no answer harvesting
    signals = []
    for pat, label in [
        (r"155", "mentions_155"),
        (r"Harness", "mentions_Harness"),
        (r"MCP", "mentions_MCP"),
        (r"Skill", "mentions_Skill"),
        (r"上下文", "mentions_context_zh"),
        (r"多智能体", "mentions_multiagent_zh"),
    ]:
        if re.search(pat, text):
            signals.append(label)
    return code, " ".join(signals) if signals else "fetched_no_signal"


def cmd_zeitgeist() -> int:
    code, sig = fetch_head(MIANLING)
    print(f"GET {MIANLING}")
    print(f"http {code} signals {sig}")
    print("NOTE themes stay in mianling-agent-2026.toon.md; answers stay on the site.")
    return 0 if code else 2


def cmd_stamp() -> int:
    code, sig = fetch_head(MIANLING)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    MEZZ.parent.mkdir(parents=True, exist_ok=True)
    body = (
        f"schema: mezzanine/interview-bank-enrich\n"
        f"as_of: {now}\n"
        f"SOURCE: {MIANLING}\n"
        f"SOURCE: {AMIT}\n"
        f"http: {code}\n"
        f"signals: {sig}\n"
        f"note: Theme map pedagogy/_learn/mianling-agent-2026.toon.md. "
        f"Strategy pedagogy/_learn/interview-prep-strategy.toon.md. "
        f"Do not invent ANSWER. Do not paste essays.\n"
    )
    MEZZ.write_text(body, encoding="utf-8")
    print(f"WROTE {MEZZ}")
    return 0 if code else 2


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--status", action="store_true")
    p.add_argument("--gap", action="store_true")
    p.add_argument("--zeitgeist", action="store_true")
    p.add_argument("--stamp", action="store_true")
    args = p.parse_args()
    if not any([args.status, args.gap, args.zeitgeist, args.stamp]):
        args.status = True
    rc = 0
    if args.status:
        rc = max(rc, cmd_status())
    if args.gap:
        rc = max(rc, cmd_gap())
    if args.zeitgeist:
        rc = max(rc, cmd_zeitgeist())
    if args.stamp:
        rc = max(rc, cmd_stamp())
    return rc


if __name__ == "__main__":
    sys.exit(main())
