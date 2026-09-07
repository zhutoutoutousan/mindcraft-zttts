#!/usr/bin/env python3
"""Recompute ontology attention weights + mirror mastery.

    python cron/ontology-weight.py
    python cron/ontology-weight.py --dry-run

Reads goals / PLAN / STUDY / harvest / learn grasp / graph kinds.
Writes pedagogy/_learn/weights.toon.md with per-vertex dims + reason.
Does not invent ANSWER. Does not add CLAIM to universe.graph.
Maintain organ may run this as the delta when rotating to ontology-weight.
"""
from __future__ import annotations

import argparse
import csv
import io
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "pedagogy" / "_learn" / "weights.toon.md"
GRAPH = ROOT / "pedagogy" / "universe.graph.md"
GOALS = ROOT / "self" / "goals.toon.md"
LEARN = ROOT / "self" / "learn.toon.md"
PED_CPU = ROOT / "pedagogy" / "pedagogy-cpu.fu.md"
HARVEST = ROOT / "schedule" / "harvest.toon.md"
INFLOW = ROOT / "inflow" / "inflow.fu.md"

V_RE = re.compile(r"^V\s+(\S+)\s+(.*)$")
KV_RE = re.compile(r"(\S+)=(\S+)")
STUDY_RE = re.compile(r"STUDY\s+\$id=(\S+)")
PLAN_RE = re.compile(r"PLAN\s+\$id=(\S+)")

# title/news keyword → vertex ids (zeitgeist / era tech)
ZEIT_KEYWORDS: list[tuple[re.Pattern[str], list[str], int]] = [
    (re.compile(r"agentcore|bedrock.?agent|cedar", re.I), ["AgentCore", "LambdaMicroVM", "AgentToolkit"], 3),
    (re.compile(r"\bmcp\b|model context protocol", re.I), ["MCP", "Agent"], 2),
    (re.compile(r"multi.?agent|subagent|agentic", re.I), ["MultiAgent", "AgentLoop", "AgenticEngineering"], 2),
    (re.compile(r"hook|plugin", re.I), ["AgentHook", "AgentPlugin"], 2),
    (re.compile(r"rag|vector|embedding", re.I), ["RAG", "VectorDatabase", "LargeLanguageModel"], 2),
    (re.compile(r"llmops|observab|sentry|reliab", re.I), ["LLMOps", "Sentry", "AgentLoop"], 2),
    (re.compile(r"reinforcement|rl\b|gym", re.I), ["SearchHarness", "Agent"], 2),
    (re.compile(r"language ai|nlp|subtitle|b2", re.I), ["NaturalLanguage", "DualSubtitle", "Wordschatz"], 2),
    (re.compile(r"health ai|fog|sickness|interocept|chill", re.I), ["SicknessBehavior", "Interoception", "AestheticChills", "Neuroscience"], 2),
    (re.compile(r"stripe|payment|ecommerce|pos", re.I), ["Payment", "Ecommerce", "Disposition"], 1),
    (re.compile(r"cursor|claude code|kiro", re.I), ["CursorSkill", "ClaudeCode", "Kiro"], 2),
]

MASLOW_KIND = {
    "natural": ("safety", 2),  # body/brain as safety base — not a diagnosis
    "techne": ("esteem", 1),
    "praxis": ("self_actualization", 2),
    "semiosis": ("belonging", 1),
    "formal": ("esteem", 1),
    "transcendental": ("self_actualization", 1),
}

MASLOW_ID = [
    (re.compile(r"^(Sickness|Caffeine|Binaural|Aphthous|Resistance|Scapula|Interocept|Aesthetic)"), ("physiological", 3)),
    (re.compile(r"^(Memory|Neuroscience|IntellectualLoad|LowDemand)"), ("safety", 2)),
    (re.compile(r"^(NaturalLanguage|DualSubtitle|Wordschatz|Language|Pedagogy|Study)"), ("belonging", 2)),
    (re.compile(r"^(AgentCore|Agent|MultiAgent|Agentic|ClaudeCode|CursorSkill)"), ("esteem", 3)),
    (re.compile(r"^(Being|Essence|Form|Mathematics|GraphTraversal)"), ("self_actualization", 2)),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def parse_graph(path: Path) -> dict[str, dict]:
    verts: dict[str, dict] = {}
    for raw in read(path).splitlines():
        m = V_RE.match(raw.strip())
        if not m:
            continue
        props = dict(KV_RE.findall(m.group(2)))
        verts[m.group(1)] = {"id": m.group(1), **props}
    return verts


def parse_goals_north(text: str) -> tuple[str, list[str]]:
    focus = ""
    north: list[str] = []
    nodes = []
    for line in text.splitlines():
        if line.startswith("focus:"):
            focus = line.split(":", 1)[1].strip()
        elif re.match(r"^\s+\S+,", line) and "nodes[" not in line:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) >= 7:
                nodes.append((parts[0], parts[6].split()))
    for nid, nlist in nodes:
        if nid == focus:
            north = nlist
            break
    if not north and nodes:
        north = nodes[0][1]
    return focus, north


def parse_plans(text: str) -> list[dict]:
    plans = []
    cur = None
    for raw in text.splitlines():
        m = PLAN_RE.search(raw)
        if m:
            if cur:
                plans.append(cur)
            cur = {"id": m.group(1), "now": "", "next": []}
            continue
        if cur is None:
            continue
        if re.match(r"^\s+- NOW ", raw):
            cur["now"] = raw.split("NOW", 1)[1].strip().split()[0] if raw.split("NOW", 1)[1].strip() else ""
        elif re.match(r"^\s+- NEXT ", raw):
            cur["next"] = raw.split("NEXT", 1)[1].strip().split()
        elif re.match(r"^- (STUDY|DAY|PROTOCOL|PLAN) ", raw) and "PLAN $" not in raw:
            plans.append(cur)
            cur = None
    if cur:
        plans.append(cur)
    return plans


def parse_open_studies(text: str) -> set[str]:
    open_ids: set[str] = set()
    cur = None
    mode = ""
    answered = False
    for raw in text.splitlines():
        m = STUDY_RE.search(raw)
        if m:
            if cur and not answered:
                open_ids.add(cur)
            cur = m.group(1)
            mode = ""
            answered = False
            continue
        if cur is None:
            continue
        if re.match(r"^- (STUDY|PLAN|DAY|PROTOCOL) ", raw):
            if not answered:
                open_ids.add(cur)
            cur = None
            continue
        if re.match(r"^\s+- ANSWER\s*$", raw):
            mode = "answer"
            continue
        if mode == "answer" and raw.strip().startswith("-") and len(raw.strip()) > 2:
            answered = True
            mode = ""
        if re.match(r"^\s+- (ASSESS|RECALL|GAP|PROBE|STORE) ", raw) or re.match(
            r"^\s+- (ASSESS|RECALL|GAP|PROBE)\s*$", raw
        ):
            if not raw.strip().startswith("- ANSWER"):
                mode = ""
    if cur and not answered:
        open_ids.add(cur)
    return open_ids


def parse_grasp(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        if re.match(r"^\s+\S+,\w*", line) and "nodes[" not in line:
            parts = [p.strip() for p in line.strip().split(",")]
            if parts:
                out[parts[0]] = parts[1] if len(parts) > 1 else "unknown"
    return out


def parse_harvest_blobs(text: str) -> list[tuple[str, str]]:
    """Return (status, title) rows."""
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("nodes["):
            started = True
            continue
        if not started or not line.startswith("  "):
            continue
        try:
            parts = next(csv.reader(io.StringIO(line.strip())))
        except Exception:
            continue
        if len(parts) >= 4:
            rows.append((parts[5] if len(parts) > 5 else "", parts[3]))
    return rows


def maslow_for(vid: str, kind: str) -> tuple[str, int, str]:
    for rx, (layer, score) in MASLOW_ID:
        if rx.search(vid):
            return layer, score, f"maslow:{layer} via id"
    layer, score = MASLOW_KIND.get(kind, ("esteem", 1))
    return layer, score, f"maslow:{layer} via kind={kind}"


def recompute() -> dict:
    verts = parse_graph(GRAPH)
    focus, north = parse_goals_north(read(GOALS))
    plans = parse_plans(read(PED_CPU))
    open_studies = parse_open_studies(read(PED_CPU))
    grasp = parse_grasp(read(LEARN))
    harvest = parse_harvest_blobs(read(HARVEST))
    news_text = read(INFLOW)

    dims: dict[str, dict] = defaultdict(
        lambda: {
            "hire": 0,
            "plan": 0,
            "study": 0,
            "zeit": 0,
            "maslow": 0,
            "maslow_layer": "",
            "reasons": [],
            "mastery": "unknown",
        }
    )

    for vid in north:
        if vid not in verts:
            continue
        dims[vid]["hire"] += 5
        dims[vid]["reasons"].append(f"goals.north[{focus}]")

    for pl in plans:
        now = pl.get("now") or ""
        if now in verts:
            dims[now]["plan"] += 4
            dims[now]["reasons"].append(f"PLAN[{pl['id']}].NOW")
        for nid in pl.get("next") or []:
            if nid in verts:
                dims[nid]["plan"] += 3
                dims[nid]["reasons"].append(f"PLAN[{pl['id']}].NEXT")

    for sid in open_studies:
        if sid in verts:
            dims[sid]["study"] += 2
            dims[sid]["reasons"].append("STUDY empty ANSWER")

    for status, title in harvest:
        bump = 2 if status == "confirmed" else 1
        blob = title
        for rx, vids, base in ZEIT_KEYWORDS:
            if rx.search(blob):
                for vid in vids:
                    if vid in verts:
                        dims[vid]["zeit"] += base * bump
                        dims[vid]["reasons"].append(
                            f"zeitgeist harvest:{status}:{title[:40]}"
                        )

    for rx, vids, base in ZEIT_KEYWORDS:
        if rx.search(news_text[-12000:]):
            for vid in vids:
                if vid in verts:
                    dims[vid]["zeit"] += 1
                    dims[vid]["reasons"].append("zeitgeist inflow NEWS keyword")

    # maslow only for nodes already touched OR all north/study — keep file small
    touched = set(dims.keys())
    for vid in list(touched):
        kind = verts.get(vid, {}).get("kind", "praxis")
        layer, score, why = maslow_for(vid, kind)
        dims[vid]["maslow"] = score
        dims[vid]["maslow_layer"] = layer
        dims[vid]["reasons"].append(why)

    for vid, g in grasp.items():
        if vid in verts:
            dims[vid]["mastery"] = g or "unknown"
            if vid not in touched:
                # still emit mastery-only rows
                dims[vid]["reasons"].append("mastery from self/learn.toon.md")

    nodes = []
    for vid, d in dims.items():
        if vid not in verts and vid not in grasp:
            continue
        total = d["hire"] + d["plan"] + d["study"] + d["zeit"] + d["maslow"]
        # uniq reasons preserve order
        seen = set()
        reasons = []
        for r in d["reasons"]:
            if r in seen:
                continue
            seen.add(r)
            reasons.append(r)
        nodes.append(
            {
                "id": vid,
                "hire": d["hire"],
                "plan": d["plan"],
                "study": d["study"],
                "zeit": d["zeit"],
                "maslow": d["maslow"],
                "maslow_layer": d["maslow_layer"],
                "total": total,
                "mastery": d["mastery"] if d["mastery"] != "unknown" else grasp.get(vid, "unknown"),
                "reason": " | ".join(reasons)[:240],
            }
        )
    nodes.sort(key=lambda x: (-x["total"], x["id"]))
    return {
        "focus": focus,
        "north": north,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "nodes": nodes,
    }


def write_weights(data: dict) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "schema: pedagogy/vertex-weight",
        "note: Attention priority particulars. Not Essence. Not a Person. Cron refreshes. Do not invent ANSWER. Do not write these numbers as CLAIM on universe.graph.",
        f"updated: {data['updated']}",
        f"focus: {data['focus']}",
        f"north: {' '.join(data['north'])}",
        "dims: hire plan study zeit maslow total",
        "maslow.note: physiological|safety|belonging|esteem|self_actualization heuristic from id/kind. Not a clinical claim.",
        "mastery.source: self/learn.toon.md grasp unknown|weak|partial|firm",
        "nodes[]{id,hire,plan,study,zeit,maslow,maslow_layer,total,mastery,reason}:",
    ]
    for n in data["nodes"]:
        reason = n["reason"].replace(",", ";").replace("\n", " ")
        lines.append(
            f"  {n['id']},{n['hire']},{n['plan']},{n['study']},{n['zeit']},{n['maslow']},{n['maslow_layer']},{n['total']},{n['mastery']},{reason}"
        )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    data = recompute()
    if args.dry_run:
        print(f"nodes={len(data['nodes'])} focus={data['focus']}")
        for n in data["nodes"][:15]:
            print(f"  {n['total']:3d} {n['id']:24s} mast={n['mastery']:8s} {n['reason'][:80]}")
        return 0
    write_weights(data)
    print(f"WROTE {OUT} nodes={len(data['nodes'])} focus={data['focus']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
