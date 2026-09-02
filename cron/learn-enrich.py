#!/usr/bin/env python3
"""Pick a job-seeking study target, render a temp lesson, grade grasp.

    python cron/learn-enrich.py --pick
    python cron/learn-enrich.py --status
    python cron/learn-enrich.py --lesson
    python cron/learn-enrich.py --probe
    python cron/learn-enrich.py --answer --text "..."
    python cron/learn-enrich.py --assess
    python cron/learn-enrich.py --gui
    python cron/learn-enrich.py --baseline
    python cron/learn-enrich.py --baseline-serve
    python cron/learn-enrich.py --ingest-baseline
    python cron/learn-enrich.py --satisfy
    python cron/learn-enrich.py --satisfy
    python cron/learn-enrich.py --grade --id AgentCore --answers 0,1,2
"""
from __future__ import annotations

import argparse
import html
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import temp_ttl

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "pedagogy" / "universe.graph.md"
CPU = ROOT / "pedagogy" / "pedagogy-cpu.fu.md"
LEARN = ROOT / "self" / "learn.toon.md"
GOALS = ROOT / "self" / "goals.toon.md"
LESSON_DIR = ROOT / "pedagogy" / "_learn"
LESSON_PACK = LESSON_DIR / "lesson.toon.md"
STATE = LESSON_DIR / "state.toon.md"
MEZZANINE = ROOT / "mezzanine" / "learn-enrich.toon.md"
BASELINE_PROBES = LESSON_DIR / "baseline-probes.toon.md"
BASELINE_HTML = temp_ttl.TMP / "pedagogy" / "baseline.html"
BASELINE_ANSWERS = temp_ttl.TMP / "pedagogy" / "baseline-answers.toon.md"
BASELINE_DURABLE = LESSON_DIR / "baseline.toon.md"
BASELINE_PORT = 8765
BASELINE_LANGS = ("en", "zh", "fr", "de")
BASELINE_LANG_LABEL = {
    "en": "English",
    "zh": "中文",
    "fr": "Français",
    "de": "Deutsch",
}
BASELINE_LANG_BCP47 = {
    "en": "en-GB",
    "zh": "zh-CN",
    "fr": "fr-FR",
    "de": "de-DE",
}

NORTH = [
    "AgentCore",
    "AgentToolkit",
    "LambdaMicroVM",
    "AgenticEngineering",
    "AgentLoop",
    "MCP",
    "MultiAgent",
    "SearchHarness",
    "Bedrock",
    "AWS",
    "CursorSkill",
    "KVCache",
    "SemanticKernel",
    "LargeLanguageModel",
    "ExperienceStore",
    "CloudRuntime",
    "Agent",
    "GitHubCI",
]
GRASP_RANK = {"unknown": 0, "weak": 1, "partial": 2, "firm": 3}
PROPAGATE = {"firm": "weak", "partial": "weak", "weak": "unknown", "unknown": "unknown"}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_vertices(text: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for line in text.splitlines():
        if not line.startswith("V "):
            continue
        parts = line.split()
        vid = parts[1]
        props = {}
        for token in parts[2:]:
            if "=" in token:
                k, v = token.split("=", 1)
                props[k] = v
        out[vid] = props
    return out


def parse_edges(text: str) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for line in text.splitlines():
        if not line.startswith("E "):
            continue
        parts = line.split()
        if len(parts) < 4:
            continue
        out.append((parts[1], parts[2], parts[3]))
    return out


def neighbors_of(vid: str, edges: list[tuple[str, str, str]]) -> list[str]:
    seen: list[str] = []
    for frm, _lab, to in edges:
        other = to if frm == vid else frm if to == vid else None
        if other and other not in seen:
            seen.append(other)
    return seen


def parse_study_gaps(text: str) -> dict[str, dict[str, bool]]:
    """id -> {has_recall_body, has_gap_body, present}."""
    studies: dict[str, dict[str, bool]] = {}
    current = None
    pending = None
    for raw in text.splitlines():
        line = raw.rstrip()
        m = re.match(r"^-\s+STUDY\s+\$id=(\S+)", line)
        if m:
            current = m.group(1)
            studies[current] = {"present": True, "recall": False, "gap": False}
            pending = None
            continue
        if current is None:
            continue
        if re.match(r"^-\s+STUDY\s+", line) or (
            line.startswith("- ") and not line.startswith("  ") and not line.startswith("- STUDY")
        ):
            if not line.startswith("  ") and not line.startswith("- STUDY") and re.match(r"^-\s+(REVIEW|ASK|AGENT|EXECUTED|NOTE|KIND|STORE)", line):
                current = None
                pending = None
                continue
        stripped = line.strip()
        if stripped == "- RECALL":
            pending = "recall"
            continue
        if stripped == "- GAP":
            pending = "gap"
            continue
        if pending and stripped.startswith("- ") and stripped not in {"- RECALL", "- GAP", "- DRILL"} and not stripped.startswith("- DRILL"):
            studies[current][pending] = True
            pending = None
        if stripped.startswith("- DRILL") or stripped.startswith("- WHY") or stripped.startswith("- STORE"):
            pending = None
    return studies


def parse_kv_block(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def load_grasp() -> dict[str, dict[str, str]]:
    if not LEARN.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    for line in LEARN.read_text(encoding="utf-8").splitlines():
        if not line.startswith("  ") or line.strip().startswith("nodes["):
            continue
        if ":" in line[:8]:
            continue
        parts = [p.strip() for p in line.strip().split(",")]
        if len(parts) >= 2 and parts[0] and parts[0] != "id":
            rows[parts[0]] = {
                "grasp": parts[1] if len(parts) > 1 else "unknown",
                "score": parts[2] if len(parts) > 2 else "",
                "n": parts[3] if len(parts) > 3 else "",
                "at": parts[4] if len(parts) > 4 else "",
            }
    return rows


def write_grasp(rows: dict[str, dict[str, str]], target: str) -> None:
    LEARN.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "schema: learner/grasp",
        "note: particulars of internalization. Not a Person vertex. Graph mirrors as E Study STUDIES id grasp=",
        f"target: {target}",
        f"updated: {now_iso()}",
        "nodes[]{id,grasp,score,n,at}:",
    ]
    for vid in sorted(rows, key=lambda k: (-GRASP_RANK.get(rows[k].get("grasp", "unknown"), 0), k)):
        r = rows[vid]
        lines.append(
            f"  {vid},{r.get('grasp','unknown')},{r.get('score','')},{r.get('n','')},{r.get('at','')}"
        )
    LEARN.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_goals() -> dict:
    out: dict = {"focus": "", "age": "", "as_of": "", "active": [], "nodes": {}}
    if not GOALS.exists():
        return out
    for line in GOALS.read_text(encoding="utf-8").splitlines():
        raw = line.strip()
        if raw.startswith("focus:"):
            out["focus"] = raw.split(":", 1)[1].strip()
        elif raw.startswith("age:") and "note" not in raw:
            out["age"] = raw.split(":", 1)[1].strip()
        elif raw.startswith("as_of:"):
            out["as_of"] = raw.split(":", 1)[1].strip()
        elif raw.startswith("active["):
            out["active"] = [x.strip() for x in raw.split(":", 1)[1].split(",") if x.strip()]
        elif line.startswith("  ") and not raw.startswith("nodes["):
            parts = [p.strip() for p in raw.split(",")]
            if len(parts) >= 7 and parts[0] and parts[0] != "id":
                out["nodes"][parts[0]] = {
                    "kind": parts[1],
                    "want": parts[2],
                    "count": parts[3],
                    "level": parts[4],
                    "status": parts[5],
                    "north": parts[6] if len(parts) > 6 else "",
                }
    return out


def north_list() -> list[str]:
    goals = load_goals()
    ordered: list[str] = []
    focus = goals.get("focus") or ""
    if focus and focus in goals.get("nodes", {}):
        ordered.extend(goals["nodes"][focus].get("north", "").split())
    for gid in goals.get("active", []):
        if gid == focus:
            continue
        row = goals.get("nodes", {}).get(gid, {})
        ordered.extend(row.get("north", "").split())
    seen: list[str] = []
    for vid in ordered + NORTH:
        if vid and vid not in seen:
            seen.append(vid)
    return seen or list(NORTH)


def upsert_study_edge(graph_text: str, vid: str, grasp: str) -> str:
    pattern = re.compile(rf"^E Study\s+STUDIES\s+{re.escape(vid)}\b.*$", re.M)
    line = f"E Study                STUDIES      {vid} grasp={grasp} SOURCE=self/learn.toon.md"
    if pattern.search(graph_text):
        return pattern.sub(line, graph_text)
    if not graph_text.endswith("\n"):
        graph_text += "\n"
    return graph_text + line + "\n"


def empty_gap(studies: dict[str, dict[str, bool]], vid: str) -> bool:
    row = studies.get(vid)
    if row is None:
        return True
    return not row.get("gap")


def pick() -> dict:
    graph_text = GRAPH.read_text(encoding="utf-8")
    verts = parse_vertices(graph_text)
    studies = parse_study_gaps(CPU.read_text(encoding="utf-8")) if CPU.exists() else {}
    grasp = load_grasp()
    state = parse_kv_block(STATE)
    current = state.get("target", "")
    current_grasp = grasp.get(current, {}).get("grasp", "unknown") if current else ""
    if current and current_grasp in {"unknown", "weak", ""}:
        reason = "hold current until grasp is partial or firm"
        return {
            "id": current,
            "reason": reason,
            "on_graph": current in verts,
            "empty_gap": empty_gap(studies, current),
            "grasp": current_grasp or "unknown",
            "neighbors": neighbors_of(current, parse_edges(graph_text)),
        }
    chosen = None
    reason = ""
    for vid in north_list():
        g = grasp.get(vid, {}).get("grasp", "unknown")
        if g == "firm":
            continue
        on = vid in verts
        gap = empty_gap(studies, vid)
        if not on:
            chosen = vid
            reason = "NORTH vertex missing from graph. Ingest this tick."
            break
        if gap:
            chosen = vid
            reason = "empty GAP on pedagogy-cpu. Internalize this tick."
            break
        if GRASP_RANK.get(g, 0) < 2:
            chosen = vid
            reason = f"grasp={g}. Drill again."
            break
    if chosen is None:
        chosen = north_list()[0]
        reason = "all NORTH firm or missing study. Repeat focus north."
    return {
        "id": chosen,
        "reason": reason,
        "on_graph": chosen in verts,
        "empty_gap": empty_gap(studies, chosen),
        "grasp": grasp.get(chosen, {}).get("grasp", "unknown"),
        "neighbors": neighbors_of(chosen, parse_edges(graph_text)) if chosen in verts else [],
    }


def write_state(picked: dict) -> None:
    LESSON_DIR.mkdir(parents=True, exist_ok=True)
    STATE.write_text(
        "\n".join(
            [
                f"target: {picked['id']}",
                f"reason: {picked['reason']}",
                f"on_graph: {str(picked['on_graph']).lower()}",
                f"grasp: {picked['grasp']}",
                f"picked: {now_iso()}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def parse_lesson_pack(text: str) -> dict:
    pack: dict = {
        "id": "",
        "gloss": "",
        "why": "",
        "claims": [],
        "neighbors": [],
        "sources": [],
        "drills": [],
        "probe": "",
        "expect": "",
    }
    for line in text.splitlines():
        if line.startswith("id:"):
            pack["id"] = line.split(":", 1)[1].strip()
        elif line.startswith("gloss:"):
            pack["gloss"] = line.split(":", 1)[1].strip()
        elif line.startswith("why:"):
            pack["why"] = line.split(":", 1)[1].strip()
        elif line.startswith("probe:"):
            pack["probe"] = line.split(":", 1)[1].strip()
        elif line.startswith("expect:"):
            pack["expect"] = line.split(":", 1)[1].strip()
        elif line.startswith("claim:"):
            pack["claims"].append(line.split(":", 1)[1].strip())
        elif line.startswith("neighbor:"):
            pack["neighbors"].append(line.split(":", 1)[1].strip())
        elif line.startswith("source:"):
            pack["sources"].append(line.split(":", 1)[1].strip())
        elif line.startswith("drill:"):
            rest = line.split(":", 1)[1]
            bits = [b.strip() for b in rest.split("|")]
            q = bits[0] if bits else ""
            expected = bits[1] if len(bits) > 1 else ""
            kind = bits[2] if len(bits) > 2 else "short"
            choices = bits[3:] if len(bits) > 3 else []
            pack["drills"].append(
                {"q": q, "expected": expected, "kind": kind, "choices": choices}
            )
    return pack


def render_html(pack: dict) -> str:
    drills_js = json.dumps(pack["drills"])
    claims = "".join(f"<li>{html.escape(c)}</li>" for c in pack["claims"])
    neigh = " · ".join(html.escape(n) for n in pack["neighbors"])
    sources = "".join(
        f'<li><a href="{html.escape(s)}">{html.escape(s)}</a></li>' for s in pack["sources"]
    )
    items = []
    for i, d in enumerate(pack["drills"]):
        if d["kind"] == "mc" and d["choices"]:
            opts = "".join(
                f'<label><input type="radio" name="q{i}" value="{html.escape(c)}"/> {html.escape(c)}</label>'
                for c in d["choices"]
            )
            items.append(f'<fieldset data-i="{i}"><legend>{html.escape(d["q"])}</legend>{opts}</fieldset>')
        else:
            items.append(
                f'<fieldset data-i="{i}"><legend>{html.escape(d["q"])}</legend>'
                f'<input name="q{i}" type="text" autocomplete="off"/></fieldset>'
            )
    body = "\n".join(items)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>learn {html.escape(pack['id'])}</title>
  <style>
    html, body {{ margin: 0; background: #0a0e14; color: #e8eef5; font-family: ui-sans-serif, system-ui; }}
    main {{ max-width: 760px; margin: 0 auto; padding: 24px 20px 64px; }}
    h1 {{ font-size: 22px; color: #69f0ae; margin: 0 0 8px; }}
    .meta {{ color: #8b9bb4; margin-bottom: 20px; }}
    fieldset {{ border: 1px solid #2a3544; margin: 0 0 14px; padding: 12px; }}
    legend {{ color: #80deea; padding: 0 6px; }}
    label {{ display: block; margin: 8px 0; }}
    input[type=text] {{ width: 100%; background: #11161d; color: #e8eef5; border: 1px solid #2a3544; padding: 8px; }}
    button {{ background: #1a237e; color: #e8eef5; border: 1px solid #90caf9; padding: 10px 16px; cursor: pointer; }}
    #out {{ white-space: pre-wrap; background: #11161d; border: 1px solid #2a3544; padding: 12px; margin-top: 16px; color: #ce93d8; }}
    a {{ color: #82b1ff; }}
  </style>
</head>
<body>
  <main>
    <h1>{html.escape(pack['id'])}</h1>
    <p class="meta">{html.escape(pack['gloss'])}<br/>{html.escape(pack['why'])}<br/>neighbors: {neigh}</p>
    <ol>{claims}</ol>
    <form id="drill">{body}
      <button type="submit">grade this loop</button>
    </form>
    <pre id="out">answer then grade. paste the blob into pedagogy/_learn/answers.toon.md or into chat RECALL.</pre>
    <h2>SOURCE</h2>
    <ul>{sources}</ul>
  </main>
  <script>
    const drills = {drills_js};
    const vid = {json.dumps(pack['id'])};
    function norm(s) {{ return (s || '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); }}
    document.getElementById('drill').addEventListener('submit', (e) => {{
      e.preventDefault();
      const fd = new FormData(e.target);
      let ok = 0;
      const given = [];
      drills.forEach((d, i) => {{
        const g = (fd.get('q' + i) || '').toString();
        given.push(g);
        const n = norm(g);
        const exp = norm(d.expected);
        let hit = false;
        if (d.kind === 'mc') hit = n === exp;
        else hit = exp && (n.includes(exp) || exp.split(' ').every(w => !w || n.includes(w)));
        if (hit) ok += 1;
      }});
      const n = drills.length;
      const ratio = n ? ok / n : 0;
      let grasp = 'unknown';
      if (ratio >= 0.84) grasp = 'firm';
      else if (ratio >= 0.5) grasp = 'partial';
      else if (ok > 0) grasp = 'weak';
      const blob = [
        'id: ' + vid,
        'grasp: ' + grasp,
        'score: ' + ok,
        'n: ' + n,
        'answers: ' + given.join(' || '),
      ].join('\\n');
      document.getElementById('out').textContent = blob;
    }});
  </script>
</body>
</html>
"""


def render_fu(pack: dict) -> str:
    claims = "\n".join(f"- CLAIM {c}" for c in pack["claims"])
    drills = "\n".join(f"- DRILL {d['q']}" for d in pack["drills"])
    sources = "\n".join(f"- SOURCE {s}" for s in pack["sources"])
    neigh = " ".join(pack["neighbors"])
    return "\n".join(
        [
            f"- VERTEX {pack['id']}",
            "- KIND temp-lesson. Not the graph. pedagogy-cpu is the durable interface.",
            f"- GLOSS {pack['gloss']}",
            f"- WHY {pack['why']}",
            f"- NEIGHBOR {neigh}",
            claims,
            drills,
            sources,
            "- NOTE pedagogy-cpu PROBE is the interface. ANSWER there. HTML is optional.",
            "",
        ]
    )


def sweep_learn_html() -> list[str]:
    gone: list[str] = []
    if not LESSON_DIR.exists():
        return gone
    for path in LESSON_DIR.glob("*.html"):
        path.unlink()
        gone.append(path.as_posix())
    return gone


def cmd_lesson() -> None:
    if not LESSON_PACK.exists():
        raise SystemExit(f"missing {LESSON_PACK}")
    pack = parse_lesson_pack(LESSON_PACK.read_text(encoding="utf-8"))
    if not pack["id"]:
        raise SystemExit("lesson pack needs id:")
    LESSON_DIR.mkdir(parents=True, exist_ok=True)
    swept = sweep_learn_html()
    write_state(
        {
            "id": pack["id"],
            "reason": "lesson pack ready. GUI is ephemeral. PROBE on pedagogy-cpu.",
            "on_graph": True,
            "grasp": load_grasp().get(pack["id"], {}).get("grasp", "unknown"),
            "neighbors": pack["neighbors"],
        }
    )
    text = CPU.read_text(encoding="utf-8") if CPU.exists() else ""
    if text and pack.get("probe"):
        text = set_study_tag(text, pack["id"], "PROBE", pack["probe"])
        text = set_plan_field(text, "NOW", pack["id"])
        CPU.write_text(text, encoding="utf-8")
    print(json.dumps({"id": pack["id"], "probe": pack.get("probe", ""), "swept_html": swept, "store": LESSON_PACK.as_posix()}))


def cmd_gui() -> None:
    if not LESSON_PACK.exists():
        raise SystemExit(f"missing {LESSON_PACK}")
    pack = parse_lesson_pack(LESSON_PACK.read_text(encoding="utf-8"))
    dest = temp_ttl.TMP / "pedagogy" / "learn-gui.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(render_html(pack), encoding="utf-8")
    temp_ttl.touch()
    print(
        json.dumps(
            {
                "gui": dest.as_posix(),
                "keep": False,
                "note": "on-demand gather UI in tmp/. janitor --ttl deletes siblings 5 days after last_run. do not copy into pedagogy/.",
            }
        )
    )


def cmd_satisfy() -> None:
    pack = parse_lesson_pack(LESSON_PACK.read_text(encoding="utf-8")) if LESSON_PACK.exists() else {}
    grasp = load_grasp()
    plan = parse_plan(CPU.read_text(encoding="utf-8")) if CPU.exists() else {}
    swept = sweep_learn_html()
    MEZZANINE.parent.mkdir(parents=True, exist_ok=True)
    MEZZANINE.write_text(
        "\n".join(
            [
                "schema: process/learn-enrich",
                "works: probe then answer then assess then plan. GUI is ephemeral tempfile. Store is fu and toon.",
                f"at: {now_iso()}",
                f"plan: {plan.get('id', '')}",
                f"now: {plan.get('NOW', pack.get('id', ''))}",
                f"adjust: {plan.get('ADJUST', '')}",
                f"target_grasp: {grasp.get(plan.get('NOW', ''), {}).get('grasp', 'unknown')}",
                "store: pedagogy/pedagogy-cpu.fu.md",
                "store: pedagogy/_learn/lesson.toon.md",
                "store: self/learn.toon.md",
                "store: cron/learn-enrich.fu.md",
                f"swept_html: {' '.join(swept) if swept else 'none'}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"satisfied": True, "mezzanine": MEZZANINE.as_posix(), "swept_html": swept}))


def grade_values(vid: str, score: int, n: int) -> str:
    ratio = score / n if n else 0
    if ratio >= 0.84:
        grasp = "firm"
    elif ratio >= 0.5:
        grasp = "partial"
    elif score > 0:
        grasp = "weak"
    else:
        grasp = "unknown"
    rows = load_grasp()
    rows[vid] = {"grasp": grasp, "score": str(score), "n": str(n), "at": now_iso()}
    graph_text = GRAPH.read_text(encoding="utf-8")
    edges = parse_edges(graph_text)
    graph_text = upsert_study_edge(graph_text, vid, grasp)
    weaker = PROPAGATE[grasp]
    if weaker != "unknown":
        for nb in neighbors_of(vid, edges):
            old = rows.get(nb, {}).get("grasp", "unknown")
            if GRASP_RANK.get(old, 0) < GRASP_RANK[weaker]:
                rows[nb] = {
                    "grasp": weaker,
                    "score": rows.get(nb, {}).get("score", ""),
                    "n": rows.get(nb, {}).get("n", ""),
                    "at": now_iso(),
                }
                graph_text = upsert_study_edge(graph_text, nb, weaker)
    GRAPH.write_text(graph_text, encoding="utf-8")
    write_grasp(rows, vid)
    sweep_learn_html()
    print(json.dumps({"id": vid, "grasp": grasp, "score": score, "n": n}))
    return grasp


def cmd_grade(vid: str, answers: list[str]) -> None:
    pack = parse_lesson_pack(LESSON_PACK.read_text(encoding="utf-8")) if LESSON_PACK.exists() else {"id": vid, "drills": []}
    drills = pack.get("drills") or []
    ok = 0
    for i, d in enumerate(drills):
        given = answers[i] if i < len(answers) else ""
        n = re.sub(r"[^a-z0-9]+", " ", given.lower()).strip()
        exp = re.sub(r"[^a-z0-9]+", " ", d.get("expected", "").lower()).strip()
        if d.get("kind") == "mc":
            hit = n == exp
        else:
            hit = bool(exp) and all(w in n for w in exp.split() if w)
        if hit:
            ok += 1
    n = len(drills) if drills else len(answers)
    grade_values(vid, ok, n or 1)


def cmd_grade_file(path: Path) -> None:
    data = parse_kv_block(path)
    vid = data.get("id", "")
    if not vid:
        raise SystemExit("answers file needs id:")
    if "score" in data and "n" in data:
        grade_values(vid, int(data["score"]), int(data["n"]))
        return
    answers = [a.strip() for a in data.get("answers", "").split("||")]
    cmd_grade(vid, answers)


def parse_plans(text: str) -> list[dict[str, str]]:
    plans: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line in text.splitlines():
        if re.match(r"^-\s+PLAN\s+", line):
            if current:
                plans.append(current)
            current = {}
            m = re.search(r"\$id=(\S+)", line)
            if m:
                current["id"] = m.group(1)
            continue
        if current is not None and re.match(r"^-\s+(STUDY|REVIEW|ASK|AGENT|PROTOCOL|KIND|STORE|NOTE|EXECUTED|PLAN)", line):
            plans.append(current)
            current = None
            if re.match(r"^-\s+PLAN\s+", line):
                current = {}
                m = re.search(r"\$id=(\S+)", line)
                if m:
                    current["id"] = m.group(1)
            continue
        if current is None:
            continue
        m = re.match(r"^\s+-\s+(NOW|NEXT|DONE|ADJUST|WHY)\s+(.*)$", line)
        if m:
            current[m.group(1)] = m.group(2).strip()
    if current:
        plans.append(current)
    return plans


def parse_plan(text: str) -> dict[str, str]:
    plans = parse_plans(text)
    focus = load_goals().get("focus")
    for plan in plans:
        if focus and plan.get("id") == focus:
            return plan
    return plans[0] if plans else {}


def study_block_span(text: str, vid: str) -> tuple[int, int] | None:
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^-\s+STUDY\s+\$id={re.escape(vid)}\b", line):
            start = i
            continue
        if start is not None and re.match(r"^-\s+(STUDY|REVIEW|ASK|AGENT|PLAN|KIND|EXECUTED|PROTOCOL)", line):
            return start, i
    if start is not None:
        return start, len(lines)
    return None


def read_answer(text: str, vid: str) -> str:
    span = study_block_span(text, vid)
    if span is None:
        return ""
    lines = text.splitlines()
    body = lines[span[0] : span[1]]
    collecting = False
    bits: list[str] = []
    for line in body:
        if line.strip() == "- ANSWER":
            collecting = True
            continue
        if collecting:
            if re.match(r"^\s+-\s+(ASSESS|RECALL|GAP|DRILL|PROBE|PHASE|WHY|STORE|EXPECT)", line.strip() if False else line):
                if line.startswith("  - ") and not line.startswith("    "):
                    break
            if line.startswith("    - "):
                bits.append(line[6:].strip())
            elif line.startswith("  - "):
                break
    return " ".join(bits).strip()


def read_probe(text: str, vid: str) -> str:
    span = study_block_span(text, vid)
    if span is None:
        return ""
    body = text.splitlines()[span[0] : span[1]]
    for i, line in enumerate(body):
        stripped = line.strip()
        if stripped.startswith("- PROBE ") and stripped != "- PROBE":
            return stripped[8:].strip()
        if stripped == "- PROBE":
            bits: list[str] = []
            for nxt in body[i + 1 :]:
                if nxt.startswith("    - "):
                    bits.append(nxt[6:].strip())
                elif nxt.startswith("  - "):
                    break
            return " ".join(bits).strip()
    return ""


def set_study_tag(text: str, vid: str, tag: str, payload: str) -> str:
    span = study_block_span(text, vid)
    if span is None:
        return text
    lines = text.splitlines(keepends=True)
    body = lines[span[0] : span[1]]
    out: list[str] = []
    i = 0
    found = False
    while i < len(body):
        line = body[i]
        if re.match(rf"^\s+-\s+{tag}\b", line):
            found = True
            out.append(f"  - {tag}\n")
            if payload:
                out.append(f"    - {payload}\n")
            i += 1
            while i < len(body) and body[i].startswith("    "):
                i += 1
            continue
        out.append(line)
        i += 1
    if not found:
        out.append(f"  - {tag}\n")
        if payload:
            out.append(f"    - {payload}\n")
    return "".join(lines[: span[0]] + out + lines[span[1] :])


def plan_block_span(text: str, plan_id: str) -> tuple[int, int] | None:
    lines = text.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^-\s+PLAN\s+\$id={re.escape(plan_id)}\b", line):
            start = i
            continue
        if start is not None and re.match(r"^-\s+(PLAN|STUDY|REVIEW|ASK|AGENT|KIND|EXECUTED|PROTOCOL)", line):
            return start, i
    if start is not None:
        return start, len(lines)
    return None


def set_plan_field(text: str, field: str, value: str, plan_id: str = "") -> str:
    if plan_id:
        span = plan_block_span(text, plan_id)
        if span is None:
            return text
        lines = text.splitlines(keepends=True)
        body = lines[span[0] : span[1]]
        pat = re.compile(rf"^(\s+-\s+{field}\s+).*$")
        new_body: list[str] = []
        hit = False
        for line in body:
            if not hit and pat.match(line.rstrip("\n")):
                new_body.append(pat.sub(rf"\g<1>{value}", line.rstrip("\n")) + ("\n" if line.endswith("\n") else ""))
                hit = True
            else:
                new_body.append(line)
        return "".join(lines[: span[0]] + new_body + lines[span[1] :])
    pat = re.compile(rf"^(\s+-\s+{field}\s+).*$", re.M)
    if pat.search(text):
        return pat.sub(rf"\g<1>{value}", text, count=1)
    return text


def score_expect(answer: str, expect: str) -> tuple[int, int, str]:
    tokens = [t for t in re.split(r"[^a-z0-9]+", expect.lower()) if t]
    blob = re.sub(r"[^a-z0-9]+", " ", answer.lower())
    hit = [t for t in tokens if t in blob]
    n = len(tokens) or 1
    ok = len(hit)
    return ok, n, " ".join(hit)


def next_from_plan(plan: dict[str, str], grasp: str) -> dict[str, str]:
    now = plan.get("NOW") or north_list()[0]
    nxt = [x for x in plan.get("NEXT", "").split() if x]
    done = [x for x in plan.get("DONE", "").split() if x]
    if grasp == "firm" and nxt:
        done = done + [now]
        now = nxt.pop(0)
        adjust = f"promoted {done[-1]} grasp=firm. NOW {now}"
    elif grasp == "partial":
        adjust = f"stay {now} grasp=partial. deepen then neighbors {(' '.join(nxt[:2]) if nxt else '')}"
    else:
        adjust = f"stay {now} grasp={grasp}. follow-up PROBE. do not rotate"
    return {
        "NOW": now,
        "NEXT": " ".join(nxt) if nxt else "",
        "DONE": " ".join(done) if done else "",
        "ADJUST": adjust,
    }


def cmd_probe() -> None:
    text = CPU.read_text(encoding="utf-8")
    plan = parse_plan(text)
    vid = plan.get("NOW") or parse_kv_block(STATE).get("target") or north_list()[0]
    probe = read_probe(text, vid)
    pack = parse_lesson_pack(LESSON_PACK.read_text(encoding="utf-8")) if LESSON_PACK.exists() else {}
    if not probe:
        probe = pack.get("probe") or f"What is {vid}, in your own words?"
    answer = read_answer(text, vid)
    print(
        json.dumps(
            {
                "action": "wait" if not answer else "assess",
                "id": vid,
                "probe": probe,
                "answer": answer,
                "plan": plan,
                "goals": {
                    "focus": load_goals().get("focus"),
                    "age": load_goals().get("age"),
                    "active": load_goals().get("active"),
                },
            },
            indent=2,
        )
    )


def cmd_write_answer(vid: str, payload: str) -> None:
    text = CPU.read_text(encoding="utf-8")
    one = " ".join(payload.strip().split())
    CPU.write_text(set_study_tag(text, vid, "ANSWER", one), encoding="utf-8")


def cmd_assess() -> None:
    text = CPU.read_text(encoding="utf-8")
    plan = parse_plan(text)
    vid = plan.get("NOW") or north_list()[0]
    answer = read_answer(text, vid)
    pack = parse_lesson_pack(LESSON_PACK.read_text(encoding="utf-8")) if LESSON_PACK.exists() else {}
    if not answer:
        print(json.dumps({"action": "wait", "id": vid, "probe": read_probe(text, vid)}))
        return
    expect = pack.get("expect") or ""
    ok, n, hits = score_expect(answer, expect)
    grasp = grade_values(vid, ok, n)
    reason = f"hits {hits or 'none'} ({ok}/{n})"
    text = CPU.read_text(encoding="utf-8")
    text = set_study_tag(text, vid, "ASSESS", f"grasp={grasp} {reason}")
    moved = next_from_plan(plan, grasp)
    for field in ("NOW", "NEXT", "DONE", "ADJUST"):
        text = set_plan_field(text, field, moved[field], plan.get("id", ""))
    if grasp in {"unknown", "weak"}:
        follow = pack.get("drills") or []
        q = follow[0]["q"] if follow else f"Name one neighbor of {vid} and how it attaches."
        text = set_study_tag(text, vid, "PROBE", q)
        text = set_study_tag(text, vid, "ANSWER", "")
        text = set_study_tag(text, vid, "PHASE", "probe")
    elif grasp == "firm":
        text = set_study_tag(text, vid, "GAP", f"internalized enough to leave NOW. hits {hits}")
        text = set_study_tag(text, vid, "PHASE", "internalized")
    CPU.write_text(text, encoding="utf-8")
    print(json.dumps({"action": "assessed", "id": vid, "grasp": grasp, "plan": moved, "hits": hits}))


def parse_baseline_probes(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    rows: list[dict[str, str]] = []
    cur: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "probe:":
            if cur.get("id") and cur.get("q"):
                rows.append(cur)
            cur = {}
            continue
        m = re.match(r"^\s{2}(id|q):\s*(.*)$", line)
        if m:
            cur[m.group(1)] = m.group(2).strip()
    if cur.get("id") and cur.get("q"):
        rows.append(cur)
    return rows


def empty_lang_map() -> dict[str, str]:
    return {k: "" for k in BASELINE_LANGS}


def normalize_lang_map(raw) -> dict[str, str]:
    out = empty_lang_map()
    if isinstance(raw, str):
        out["en"] = raw.strip()
        return out
    if not isinstance(raw, dict):
        return out
    for key in BASELINE_LANGS:
        val = raw.get(key, raw.get(f"answer.{key}", ""))
        out[key] = str(val).strip() if val is not None else ""
    if not any(out.values()) and raw.get("answer"):
        out["en"] = str(raw.get("answer") or "").strip()
    return out


def filled_boxes(answers: dict[str, dict[str, str]]) -> int:
    n = 0
    for langs in answers.values():
        for key in BASELINE_LANGS:
            if langs.get(key, "").strip():
                n += 1
    return n


def content_text(langs: dict[str, str]) -> tuple[str, str]:
    for key in ("en", "de", "zh", "fr"):
        text = (langs.get(key) or "").strip()
        if text:
            return text, key
    return "", ""


def _is_field_name(text: str) -> bool:
    return bool(re.match(r"^answer\.(en|zh|fr|de):$", (text or "").strip()))


def extract_lang_field(chunk: str, key: str) -> str:
    header = re.compile(rf"^  answer\.{re.escape(key)}:[ \t]*(.*)$")
    lines = chunk.splitlines()
    for i, line in enumerate(lines):
        m = header.match(line)
        if not m:
            continue
        rest = m.group(1).strip()
        if rest == "|":
            body: list[str] = []
            for cont in lines[i + 1 :]:
                if cont.startswith("    "):
                    body.append(cont[4:])
                elif cont.strip() == "":
                    body.append("")
                else:
                    break
            text = "\n".join(body).strip()
        else:
            text = rest
        return "" if _is_field_name(text) else text
    return ""


def parse_baseline_answers(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}
    out: dict[str, dict[str, str]] = {}
    chunks = re.split(r"^node:\s*$", path.read_text(encoding="utf-8"), flags=re.M)
    for chunk in chunks[1:]:
        id_m = re.search(r"^  id:[ \t]*(.+)$", chunk, re.M)
        if not id_m:
            continue
        vid = id_m.group(1).strip()
        langs = empty_lang_map()
        for key in BASELINE_LANGS:
            langs[key] = extract_lang_field(chunk, key)
        if not any(langs.values()):
            lines = chunk.splitlines()
            for i, line in enumerate(lines):
                if re.match(r"^  answer\.(en|zh|fr|de):", line):
                    continue
                m = re.match(r"^  answer:[ \t]*(.*)$", line)
                if not m:
                    continue
                rest = m.group(1).strip()
                if rest == "|":
                    body: list[str] = []
                    for cont in lines[i + 1 :]:
                        if cont.startswith("    "):
                            body.append(cont[4:])
                        else:
                            break
                    langs["en"] = "\n".join(body).strip()
                else:
                    langs["en"] = rest
                break
        out[vid] = langs
    return out


def write_lang_field(lines: list[str], key: str, text: str) -> None:
    text = text or ""
    if "\n" in text:
        lines.append(f"  answer.{key}: |")
        for part in text.splitlines() or [""]:
            lines.append(f"    {part}")
        return
    lines.append(f"  answer.{key}: {text}")


def write_baseline_answers(path: Path, answers: dict, *, status: str = "open") -> None:
    probes = parse_baseline_probes(BASELINE_PROBES)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "schema: learn/baseline-answers",
        "kind: 摸底",
        f"saved: {now_iso()}",
        f"status: {status}",
        "langs: en zh fr de",
        "note: expression samples per language. Empty skip. Do not invent. en and de are attested SPRACHEN. zh and fr are samples, not SPRACHEN lines. Do not add Chinese as native.",
        "",
    ]
    for row in probes:
        vid = row["id"]
        langs = normalize_lang_map(answers.get(vid, {}))
        lines.append("node:")
        lines.append(f"  id: {vid}")
        for key in BASELINE_LANGS:
            write_lang_field(lines, key, langs[key])
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def render_baseline_html(probes: list[dict[str, str]], answers: dict[str, dict[str, str]]) -> str:
    cards = []
    for i, row in enumerate(probes, start=1):
        vid = html.escape(row["id"])
        q = html.escape(row["q"])
        langs = normalize_lang_map(answers.get(row["id"], {}))
        boxes = []
        for key in BASELINE_LANGS:
            label = html.escape(BASELINE_LANG_LABEL[key])
            val = html.escape(langs.get(key, ""))
            bcp = html.escape(BASELINE_LANG_BCP47[key])
            boxes.append(
                f'<div class="lang">'
                f'<div class="lang-head"><span>{label}</span>'
                f'<button type="button" class="mic" data-lang="{key}" aria-label="Speak {label}">Speak</button></div>'
                f'<textarea data-lang="{key}" lang="{bcp}" rows="4" placeholder="{label}. skip if empty. Speak or type.">{val}</textarea>'
                f"</div>"
            )
        cards.append(
            f'<article data-id="{vid}">'
            f"<header><span>{i}/{len(probes)}</span><strong>{vid}</strong></header>"
            f"<p>{q}</p>"
            f'<div class="langs">{"".join(boxes)}</div>'
            f"</article>"
        )
    body = "\n".join(cards)
    payload = json.dumps([{"id": r["id"], "q": r["q"]} for r in probes], ensure_ascii=False)
    langs_js = json.dumps(list(BASELINE_LANGS))
    bcp_js = json.dumps(BASELINE_LANG_BCP47)
    return f"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8"/>
  <title>摸底 · ai-agent-engineer</title>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <style>
    html, body {{ margin: 0; background: #0a0e14; color: #e8eef5; font-family: ui-sans-serif, system-ui; }}
    main {{ max-width: 960px; margin: 0 auto; padding: 24px 20px 80px; }}
    h1 {{ font-size: 22px; color: #69f0ae; margin: 0 0 8px; }}
    .meta {{ color: #8b9bb4; margin: 0 0 20px; line-height: 1.45; }}
    article {{ border: 1px solid #2a3544; border-radius: 12px; padding: 14px 16px; margin: 0 0 14px; background: #11161d; }}
    article header {{ display: flex; gap: 10px; align-items: baseline; color: #80deea; margin-bottom: 8px; }}
    article header span {{ color: #8b9bb4; font-size: 12px; }}
    .langs {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
    @media (max-width: 720px) {{ .langs {{ grid-template-columns: 1fr; }} }}
    .lang {{ display: flex; flex-direction: column; gap: 6px; color: #90caf9; font-size: 12px; }}
    .lang-head {{ display: flex; align-items: center; justify-content: space-between; gap: 8px; }}
    button.mic {{ background: #1a237e; color: #e8eef5; border: 1px solid #90caf9; padding: 4px 10px; cursor: pointer; border-radius: 8px; font-size: 12px; }}
    button.mic.live {{ background: #b71c1c; border-color: #ef9a9a; }}
    textarea {{ width: 100%; box-sizing: border-box; background: #0a0e14; color: #e8eef5; border: 1px solid #2a3544; border-radius: 8px; padding: 10px; font: 15px/1.4 ui-sans-serif, system-ui; }}
    textarea.listening {{ border-color: #ef9a9a; }}
    .bar {{ position: sticky; bottom: 0; background: #0a0e14; border-top: 1px solid #2a3544; padding: 12px 20px; display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }}
    button {{ background: #1a237e; color: #e8eef5; border: 1px solid #90caf9; padding: 10px 16px; cursor: pointer; border-radius: 8px; }}
    button.done {{ background: #004d40; border-color: #69f0ae; }}
    #status {{ color: #ce93d8; font-size: 13px; }}
  </style>
</head>
<body>
  <main>
    <h1>摸底 · first probe · four languages</h1>
    <p class="meta">Async. Same question, four boxes: English, 中文, Français, Deutsch. Skip any language. Stop if sore. Not today's DAY LOAD of 3.<br/>
    Speak in Chrome or Edge on this page: each Speak button listens in that language and writes into that box. Grant the microphone. Edit the transcript if it errs. Type if you prefer.<br/>
    Content grasp uses English if you filled it. Expression in each box stays separate for language assessment.<br/>
    en C1 and de B2+ are attested SPRACHEN. 中文 and Français are samples, not new SPRACHEN lines. Do not add Chinese as native.<br/>
    Answers: <code>tmp/pedagogy/baseline-answers.toon.md</code>. Empty is wait. Nothing is invented.</p>
    {body}
  </main>
  <div class="bar">
    <button type="button" id="save">Save now</button>
    <button type="button" id="dl">Download backup</button>
    <button type="button" id="done" class="done">I'm done</button>
    <span id="status">idle</span>
  </div>
  <script>
    const PROBES = {payload};
    const LANGS = {langs_js};
    const BCP47 = {bcp_js};
    const KEY = "baseline-lang4-voice-2026-09-02";
    const total = PROBES.length * LANGS.length;
    const areas = [...document.querySelectorAll("article[data-id]")];
    function collect() {{
      const out = {{}};
      areas.forEach((el) => {{
        const id = el.getAttribute("data-id");
        const row = {{}};
        LANGS.forEach((lang) => {{
          const box = el.querySelector('textarea[data-lang="' + lang + '"]');
          row[lang] = (box && box.value || "").trim();
        }});
        out[id] = row;
      }});
      return out;
    }}
    function restore(data) {{
      areas.forEach((el) => {{
        const id = el.getAttribute("data-id");
        let row = data[id];
        if (typeof row === "string") row = {{ en: row, zh: "", fr: "", de: "" }};
        if (!row) return;
        LANGS.forEach((lang) => {{
          const box = el.querySelector('textarea[data-lang="' + lang + '"]');
          if (box && row[lang]) box.value = row[lang];
        }});
      }});
    }}
    try {{
      const cached = JSON.parse(localStorage.getItem(KEY) || "{{}}");
      restore(cached);
      const old = JSON.parse(localStorage.getItem("baseline-2026-09-02") || "{{}}");
      areas.forEach((el) => {{
        const id = el.getAttribute("data-id");
        const box = el.querySelector('textarea[data-lang="en"]');
        if (box && !box.value && typeof old[id] === "string") box.value = old[id];
      }});
    }} catch (e) {{}}
    function filledCount(data) {{
      let n = 0;
      Object.values(data).forEach((row) => {{
        LANGS.forEach((lang) => {{ if ((row[lang] || "").trim()) n += 1; }});
      }});
      return n;
    }}
    async function save(status) {{
      const data = collect();
      localStorage.setItem(KEY, JSON.stringify(data));
      const n = filledCount(data);
      document.getElementById("status").textContent = "saving " + n + "/" + total;
      try {{
        const res = await fetch(status === "done" ? "/done" : "/save", {{
          method: "POST",
          headers: {{ "content-type": "application/json" }},
          body: JSON.stringify({{ status: status || "open", answers: data }}),
        }});
        if (!res.ok) throw new Error("http " + res.status);
        document.getElementById("status").textContent = (status === "done" ? "done · " : "saved · ") + n + "/" + total + " boxes · " + new Date().toLocaleTimeString();
      }} catch (e) {{
        document.getElementById("status").textContent = "local only · " + n + "/" + total + " · use Download backup";
      }}
    }}
    let t = null;
    areas.forEach((el) => {{
      el.querySelectorAll("textarea").forEach((box) => {{
        box.addEventListener("input", () => {{
          clearTimeout(t);
          t = setTimeout(() => save("open"), 1200);
        }});
      }});
    }});
    document.getElementById("save").onclick = () => save("open");
    document.getElementById("done").onclick = () => save("done");
    document.getElementById("dl").onclick = () => {{
      const data = collect();
      localStorage.setItem(KEY, JSON.stringify(data));
      const blob = new Blob([JSON.stringify({{ schema: "learn/baseline-answers", langs: LANGS, answers: data }}, null, 2)], {{ type: "application/json" }});
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "baseline-answers.json";
      a.click();
    }};
    const SpeechAPI = window.SpeechRecognition || window.webkitSpeechRecognition;
    let live = null;
    function clearLiveUi() {{
      document.querySelectorAll("button.mic").forEach((b) => {{
        b.classList.remove("live");
        b.textContent = "Speak";
      }});
      document.querySelectorAll("textarea.listening").forEach((el) => el.classList.remove("listening"));
    }}
    function stopLive() {{
      if (!live) return;
      live.keep = false;
      try {{ live.rec.stop(); }} catch (e) {{}}
      live = null;
      clearLiveUi();
    }}
    function startLive(btn) {{
      const lang = btn.getAttribute("data-lang");
      const box = btn.closest(".lang").querySelector("textarea");
      if (!SpeechAPI) {{
        document.getElementById("status").textContent = "voice needs Chrome or Edge at http://127.0.0.1:8765/";
        return;
      }}
      if (live && live.btn === btn) {{
        stopLive();
        save("open");
        return;
      }}
      stopLive();
      const rec = new SpeechAPI();
      rec.lang = BCP47[lang] || "en-GB";
      rec.continuous = true;
      rec.interimResults = true;
      rec.maxAlternatives = 1;
      let base = (box.value || "").replace(/\\s+$/, "");
      if (base) base += " ";
      live = {{ rec: rec, btn: btn, box: box, keep: true }};
      rec.onresult = (ev) => {{
        let acc = "";
        let tmp = "";
        for (let i = 0; i < ev.results.length; i++) {{
          const t = ev.results[i][0].transcript;
          if (ev.results[i].isFinal) acc += t;
          else tmp += t;
        }}
        box.value = (base + acc + tmp).replace(/ +/g, " ").replace(/^ /, "");
        box.dispatchEvent(new Event("input"));
      }};
      rec.onerror = (ev) => {{
        document.getElementById("status").textContent = "voice: " + ev.error + " · " + (BCP47[lang] || lang);
        if (ev.error === "not-allowed") stopLive();
      }};
      rec.onend = () => {{
        if (live && live.rec === rec && live.keep) {{
          base = (box.value || "").replace(/\\s+$/, "");
          if (base) base += " ";
          try {{ rec.start(); return; }} catch (e) {{}}
        }}
        if (live && live.rec === rec) {{
          live = null;
          clearLiveUi();
          save("open");
        }}
      }};
      try {{
        rec.start();
      }} catch (e) {{
        document.getElementById("status").textContent = "voice failed to start";
        live = null;
        return;
      }}
      clearLiveUi();
      btn.classList.add("live");
      btn.textContent = "Stop";
      box.classList.add("listening");
      document.getElementById("status").textContent = "listening " + lang + " · " + rec.lang + " · speak, then Stop";
    }}
    document.querySelectorAll("button.mic").forEach((btn) => {{
      btn.addEventListener("click", () => startLive(btn));
    }});
    if (!SpeechAPI) {{
      document.querySelectorAll("button.mic").forEach((b) => {{ b.hidden = true; }});
      document.getElementById("status").textContent = "type, or open in Chrome/Edge for Speak";
    }}
  </script>
</body>
</html>
"""


def cmd_baseline() -> dict:
    probes = parse_baseline_probes(BASELINE_PROBES)
    if not probes:
        raise SystemExit(f"missing probes {BASELINE_PROBES}")
    prev = parse_baseline_answers(BASELINE_ANSWERS)
    status = "open"
    if BASELINE_ANSWERS.exists():
        sm = re.search(r"^status:\s*(.+)$", BASELINE_ANSWERS.read_text(encoding="utf-8"), re.M)
        if sm:
            status = sm.group(1).strip() or "open"
    BASELINE_HTML.parent.mkdir(parents=True, exist_ok=True)
    BASELINE_HTML.write_text(render_baseline_html(probes, prev), encoding="utf-8")
    write_baseline_answers(BASELINE_ANSWERS, prev, status=status)
    temp_ttl.touch()
    info = {
        "html": BASELINE_HTML.as_posix(),
        "answers": BASELINE_ANSWERS.as_posix(),
        "n": len(probes),
        "langs": list(BASELINE_LANGS),
        "boxes": len(probes) * len(BASELINE_LANGS),
        "ids": [r["id"] for r in probes],
        "note": "async 摸底. four expression boxes en zh fr de. skip any language. stop if sore. do not invent answers. do not add Chinese as native.",
    }
    print(json.dumps(info, indent=2))
    return info


def cmd_baseline_serve(host: str = "127.0.0.1", port: int = BASELINE_PORT) -> None:
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    cmd_baseline()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args) -> None:
            sys_stdout = __import__("sys").stderr
            sys_stdout.write("BASELINE " + (fmt % args) + "\n")

        def _json(self, code: int, payload: dict) -> None:
            raw = json.dumps(payload).encode("utf-8")
            self.send_response(code)
            self.send_header("content-type", "application/json; charset=utf-8")
            self.send_header("content-length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def _html(self) -> None:
            raw = BASELINE_HTML.read_bytes()
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.send_header("cache-control", "no-store")
            self.send_header("content-length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self) -> None:
            if self.path in {"/", "/index.html", "/baseline.html"}:
                self._html()
                return
            if self.path == "/health":
                self._json(200, {"ok": True, "html": BASELINE_HTML.as_posix()})
                return
            if self.path == "/answers":
                self._json(200, parse_baseline_answers(BASELINE_ANSWERS))
                return
            self.send_error(404)

        def do_POST(self) -> None:
            if self.path not in {"/save", "/done"}:
                self.send_error(404)
                return
            n = int(self.headers.get("content-length") or "0")
            raw = self.rfile.read(n) if n else b"{}"
            try:
                body = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                self._json(400, {"ok": False})
                return
            answers = body.get("answers") or {}
            if not isinstance(answers, dict):
                self._json(400, {"ok": False})
                return
            clean = {str(k): normalize_lang_map(v) for k, v in answers.items()}
            status = "done" if self.path == "/done" else str(body.get("status") or "open")
            write_baseline_answers(BASELINE_ANSWERS, clean, status=status)
            temp_ttl.touch()
            filled = filled_boxes(clean)
            self._json(200, {"ok": True, "status": status, "filled": filled, "total": len(parse_baseline_probes(BASELINE_PROBES)) * len(BASELINE_LANGS)})

    httpd = ThreadingHTTPServer((host, port), Handler)
    print(f"BASELINE http://{host}:{port}/", flush=True)
    print(f"BASELINE answers {BASELINE_ANSWERS.as_posix()}", flush=True)
    httpd.serve_forever()


def cmd_ingest_baseline(*, apply_study: bool = False) -> None:
    answers = parse_baseline_answers(BASELINE_ANSWERS)
    if BASELINE_ANSWERS.exists():
        BASELINE_DURABLE.write_text(BASELINE_ANSWERS.read_text(encoding="utf-8"), encoding="utf-8")
    applied: list[str] = []
    skipped: list[str] = []
    empty: list[str] = []
    if apply_study and CPU.exists():
        text = CPU.read_text(encoding="utf-8")
        for vid, langs in answers.items():
            langs = normalize_lang_map(langs)
            one, src = content_text(langs)
            if not one:
                empty.append(vid)
                continue
            if study_block_span(text, vid) is None:
                skipped.append(vid)
                continue
            if read_answer(text, vid):
                skipped.append(vid)
                continue
            text = set_study_tag(text, vid, "ANSWER", one)
            applied.append(f"{vid}:{src}")
        CPU.write_text(text, encoding="utf-8")
    else:
        for vid, langs in answers.items():
            langs = normalize_lang_map(langs)
            if any((langs.get(k) or "").strip() for k in BASELINE_LANGS):
                skipped.append(vid)
            else:
                empty.append(vid)
    print(
        json.dumps(
            {
                "durable": BASELINE_DURABLE.as_posix(),
                "study": applied if apply_study else [],
                "kept_in_file": skipped,
                "empty": empty,
                "note": "no assess. no invented ANSWER. expression samples stay in the answers file. --apply-study uses English if present else first filled language.",
            },
            indent=2,
        )
    )


def cmd_status() -> None:
    picked = pick()
    print(json.dumps({"pick": picked, "grasp": load_grasp(), "state": parse_kv_block(STATE), "goals": load_goals()}, indent=2))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--pick", action="store_true")
    p.add_argument("--status", action="store_true")
    p.add_argument("--lesson", action="store_true")
    p.add_argument("--probe", action="store_true")
    p.add_argument("--assess", action="store_true")
    p.add_argument("--answer", action="store_true")
    p.add_argument("--gui", action="store_true")
    p.add_argument("--baseline", action="store_true")
    p.add_argument("--baseline-serve", action="store_true")
    p.add_argument("--ingest-baseline", action="store_true")
    p.add_argument("--apply-study", action="store_true")
    p.add_argument("--satisfy", action="store_true")
    p.add_argument("--grade", action="store_true")
    p.add_argument("--grade-file", type=Path)
    p.add_argument("--id")
    p.add_argument("--text", default="")
    p.add_argument("--answers", default="")
    args = p.parse_args()
    n = sum(
        bool(x)
        for x in [
            args.pick,
            args.status,
            args.lesson,
            args.probe,
            args.assess,
            args.answer,
            args.gui,
            args.baseline,
            args.baseline_serve,
            args.ingest_baseline,
            args.satisfy,
            args.grade,
            args.grade_file,
        ]
    )
    if n != 1:
        raise SystemExit(
            "choose exactly one of --pick --status --lesson --probe --assess --answer --gui --baseline --baseline-serve --ingest-baseline --satisfy --grade --grade-file"
        )
    if args.pick:
        picked = pick()
        write_state(picked)
        print(json.dumps(picked, indent=2))
        return
    if args.status:
        cmd_status()
        return
    if args.lesson:
        cmd_lesson()
        return
    if args.probe:
        cmd_probe()
        return
    if args.assess:
        cmd_assess()
        return
    if args.gui:
        cmd_gui()
        return
    if args.baseline:
        cmd_baseline()
        return
    if args.baseline_serve:
        cmd_baseline_serve()
        return
    if args.ingest_baseline:
        cmd_ingest_baseline(apply_study=args.apply_study)
        return
    if args.satisfy:
        cmd_satisfy()
        return
    if args.answer:
        vid = args.id or parse_plan(CPU.read_text(encoding="utf-8")).get("NOW") or north_list()[0]
        if not args.text:
            raise SystemExit("--answer needs --text")
        cmd_write_answer(vid, args.text)
        cmd_assess()
        return
    if args.grade_file:
        cmd_grade_file(args.grade_file)
        return
    if not args.id:
        raise SystemExit("--grade needs --id")
    cmd_grade(args.id, [a.strip() for a in args.answers.split(",")])


if __name__ == "__main__":
    main()
