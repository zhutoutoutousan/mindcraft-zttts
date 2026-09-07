#!/usr/bin/env python3
"""Dynamic project-state HTML from ROOT + live stores + universe.graph.

    python skills/project-state-viz.py
    python skills/project-state-viz.py --purpose hire
    python skills/project-state-viz.py --serve
    python skills/project-state-viz.py --serve --purpose study

Writes tmp/pedagogy/project-state.html and stamps TTL.
"""
from __future__ import annotations

import argparse
import http.server
import json
import re
import socketserver
import sys
import webbrowser
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "tmp" / "pedagogy" / "project-state.html"
NOTES = ROOT / "tmp" / "pedagogy" / "learner-notes.toon.md"
NOTES_STORE = ROOT / "pedagogy" / "_learn" / "learner-notes.toon.md"
INFLOW_TAKES = ROOT / "tmp" / "pedagogy" / "inflow-takes.toon.md"
INFLOW_TAKES_STORE = ROOT / "inflow" / "takes.toon.md"

KIND_FILL = {
    "transcendental": "#1a237e",
    "formal": "#004d40",
    "natural": "#1b3a4b",
    "techne": "#3e2723",
    "praxis": "#4a148c",
    "semiosis": "#0d47a1",
    # language-learn stores (lexicon / bridge / frames / skilltree)
    "lemma": "#0d47a1",
    "form": "#1565c0",
    "chunk": "#283593",
    "sentence": "#4527a0",
    "usage": "#00695c",
    "pattern": "#37474f",
    "session": "#455a64",
    "concept": "#4a148c",
    "gap": "#b71c1c",
    "frame": "#1b5e20",
    "slot": "#33691e",
    "focus": "#e65100",
    "band": "#263238",
    "lang": "#01579b",
    "horizon": "#004d40",
}
KIND_EDGE = {
    "transcendental": "#90caf9",
    "formal": "#69f0ae",
    "natural": "#80deea",
    "techne": "#ffcc80",
    "praxis": "#ce93d8",
    "semiosis": "#82b1ff",
    "lemma": "#82b1ff",
    "form": "#90caf9",
    "chunk": "#9fa8da",
    "sentence": "#b39ddb",
    "usage": "#80cbc4",
    "pattern": "#90a4ae",
    "session": "#b0bec5",
    "concept": "#ce93d8",
    "gap": "#ef9a9a",
    "frame": "#a5d6a7",
    "slot": "#c5e1a5",
    "focus": "#ffcc80",
    "band": "#b0bec5",
    "lang": "#4fc3f7",
    "horizon": "#69f0ae",
}
LABEL_COLOR = {
    "ISA": "#90caf9",
    "PARTICIPATES": "#ce93d8",
    "INFORMS": "#69f0ae",
    "RECEIVES": "#80cbc4",
    "STUDIES": "#ffcc80",
    "GROUNDS_IN": "#ffab91",
    "APPLIES": "#82b1ff",
    "ENACTS": "#f48fb1",
    "MEDIATES": "#b39ddb",
    "TRANSMITS": "#a5d6a7",
    "CONTRADICTS": "#ef5350",
    "EXPRESSES": "#ce93d8",
    "GAP_IN": "#ef9a9a",
    "FROM_SESSION": "#90a4ae",
    "NEEDS_FRAME": "#a5d6a7",
    "HAS_FORM": "#90caf9",
    "HAS_SLOT": "#c5e1a5",
    "FILLED_BY": "#82b1ff",
    "IN_BAND": "#4fc3f7",
    "TARGETS": "#69f0ae",
    "FIXES": "#ffab91",
}

V_RE = re.compile(r"^V\s+(\S+)\s+(.*)$")
E_RE = re.compile(r"^E\s+(\S+)\s+(\S+)\s+(\S+)(?:\s+(.*))?$")
KV_RE = re.compile(r'(\S+)=(?:"([^"]*)"|(\S+))')
KIND_READ = {
    "concept": "意思",
    "lemma": "词",
    "form": "词形",
    "chunk": "搭配",
    "sentence": "句子",
    "usage": "用法",
    "pattern": "偏误",
    "session": "会话",
    "focus": "焦点",
    "frame": "句法",
    "slot": "槽",
    "gap": "缺口",
    "lang": "语言",
    "band": "等级",
    "horizon": "目标",
}
_ID_PREFIXES = (
    "Form_fix_",
    "Form_",
    "Lemma_de_fix_",
    "Lemma_fr_fix_",
    "Lemma_en_",
    "Lemma_de_",
    "Lemma_zh_",
    "Lemma_fr_",
    "Lemma_",
    "Session_",
    "Focus_",
    "Concept_gap_",
    "Concept_",
    "Gap_",
    "Frame_de_",
    "Frame_fr_",
    "Frame_",
    "Chunk_",
    "Sent_",
    "Slot_",
    "Filler_",
    "Usage_",
    "Pat_",
    "Horizon_",
    "Band_",
    "Lang_",
)
_HOLE = (
    (re.compile(r"\bh tte\b", re.I), "hätte"),
    (re.compile(r"\bh tten\b", re.I), "hätten"),
    (re.compile(r"\bf r\b", re.I), "für"),
    (re.compile(r"\bf rs\b", re.I), "fürs"),
    (re.compile(r"\bg nzlich\b", re.I), "gänzlich"),
    (re.compile(r"\bs tze\b", re.I), "Sätze"),
    (re.compile(r"\bhaette\b", re.I), "hätte"),
    (re.compile(r"\baeussern\b", re.I), "äußern"),
    (re.compile(r"\bAenderung\b"), "Änderung"),
)
AGENT_RE = re.compile(r"AGENT\s+\$id=(\S+)")
STUDY_RE = re.compile(r"STUDY\s+\$id=(\S+)")
PLAN_RE = re.compile(r"PLAN\s+\$id=(\S+)")
CAPTURE_RE = re.compile(r"CAPTURE\s+\$id=(\S+)")


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def parse_kv(blob: str) -> dict:
    props: dict[str, str] = {}
    for m in KV_RE.finditer(blob or ""):
        props[m.group(1)] = m.group(2) if m.group(2) is not None else (m.group(3) or "")
    return props


def humanize_lang_text(s: str) -> str:
    """Turn graph-safe tokens into something a person can read on a node."""
    if not s:
        return ""
    t = str(s).replace("-", " ").replace("_", " ")
    t = re.sub(r"\s+", " ", t).strip()
    t = re.sub(r"\b[a-f0-9]{8,10}\b", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    for rx, rep in _HOLE:
        t = rx.sub(rep, t)
    return t


def strip_id_prefix(vid: str) -> str:
    s = vid or ""
    for p in _ID_PREFIXES:
        if s.startswith(p):
            return s[len(p) :]
    return s


def lang_node_label(v: dict) -> str:
    kind = (v.get("kind") or "").lower()
    surface = humanize_lang_text(v.get("surface") or "")
    gloss = humanize_lang_text(v.get("gloss") or "")
    vid = v.get("id") or ""
    if kind == "session":
        rest = humanize_lang_text(strip_id_prefix(vid))
        date = v.get("date") or ""
        if date:
            try:
                _y, m, d = date.split("-")
                stamp = f"{int(d)}.{int(m)}."
            except ValueError:
                stamp = date
            return f"{stamp} {rest}".strip()[:48]
        return (rest or vid)[:48]
    if kind == "frame":
        pat = humanize_lang_text(v.get("pattern") or "")
        return (pat or gloss or humanize_lang_text(strip_id_prefix(vid)))[:48]
    if kind == "gap":
        core = surface or gloss or humanize_lang_text(strip_id_prefix(vid))
        return ("缺口 · " + core)[:48]
    if kind == "lang":
        return " · ".join(x for x in ((v.get("surface") or ""), gloss) if x)[:48]
    if kind in {"lemma", "form"}:
        if surface:
            return surface[:42]
        if vid and "_" not in vid:
            return vid
        return (gloss or humanize_lang_text(strip_id_prefix(vid)))[:42]
    if kind == "concept":
        return (gloss or humanize_lang_text(strip_id_prefix(vid)))[:42]
    return (surface or gloss or humanize_lang_text(strip_id_prefix(vid)) or vid)[:42]


def decorate_lang_verts(verts: list[dict]) -> list[dict]:
    for v in verts:
        v["label"] = lang_node_label(v)
        v["kindRead"] = KIND_READ.get((v.get("kind") or "").lower(), v.get("kind") or "")
        v["surfaceRead"] = humanize_lang_text(v.get("surface") or "")
        v["glossRead"] = humanize_lang_text(v.get("gloss") or "")
        v["fixesRead"] = humanize_lang_text(v.get("fixes") or "")
    return verts


def parse_graph(path: Path) -> tuple[list[dict], list[dict]]:
    verts: list[dict] = []
    edges: list[dict] = []
    for raw in read(path).splitlines():
        line = raw.strip()
        if not line or line.startswith("graph:") or line.startswith("engine:"):
            continue
        m = V_RE.match(line)
        if m:
            verts.append({"id": m.group(1), **parse_kv(m.group(2))})
            continue
        m = E_RE.match(line)
        if m:
            edges.append(
                {
                    "src": m.group(1),
                    "label": m.group(2),
                    "dst": m.group(3),
                    **parse_kv(m.group(4) or ""),
                }
            )
    return verts, edges


def _graph_pack(
    verts: list[dict], edges: list[dict], *, default_branch: str
) -> dict:
    for v in verts:
        if not v.get("branch"):
            v["branch"] = v.get("lang") or default_branch
        if not v.get("kind"):
            v["kind"] = "lemma"
    decorate_lang_verts(verts)
    return {
        "verts": verts,
        "edges": edges,
        "v_count": len(verts),
        "e_count": len(edges),
        "source": default_branch,
    }


def parse_horizon_langs(text: str) -> list[dict]:
    """Parse langs[N]{{code,name,band,script}} rows from horizon.toon.md."""
    langs: list[dict] = []
    in_langs = False
    for line in text.splitlines():
        if line.startswith("langs["):
            in_langs = True
            continue
        if not in_langs:
            continue
        if not line.strip() or (
            re.match(r"^[a-zA-Z_]", line) and not line.startswith(" ")
        ):
            break
        parts = [p.strip() for p in line.strip().split(",")]
        if len(parts) >= 3 and re.match(r"^[a-z]{2,3}$", parts[0]):
            langs.append(
                {
                    "code": parts[0],
                    "name": parts[1],
                    "band": parts[2],
                    "script": parts[3] if len(parts) > 3 else "",
                }
            )
    return langs


def frames_to_graph(text: str, lang: str = "de") -> tuple[list[dict], list[dict]]:
    """Turn frames/*.toon.md into Frame/Slot/filler verts for Grammar view."""
    verts: list[dict] = []
    edges: list[dict] = []
    cur: dict | None = None

    def flush() -> None:
        nonlocal cur
        if not cur or not cur.get("id"):
            cur = None
            return
        fid = f"Frame_{lang}_{cur['id']}"
        verts.append(
            {
                "id": fid,
                "kind": "frame",
                "lang": lang,
                "branch": "grammar",
                "gloss": cur.get("gloss") or cur["id"],
                "surface": (cur.get("pattern") or "")[:80],
                "pattern": (cur.get("pattern") or "")[:80],
            }
        )
        slots = cur.get("slots") or []
        fillers = cur.get("fillers") or []
        for i, slot in enumerate(slots):
            sid = f"Slot_{lang}_{cur['id']}_{i}"
            verts.append(
                {
                    "id": sid,
                    "kind": "slot",
                    "lang": lang,
                    "branch": "grammar",
                    "gloss": slot,
                }
            )
            edges.append({"src": fid, "label": "HAS_SLOT", "dst": sid})
            if i < len(fillers):
                fill = fillers[i]
                lid = f"Filler_{lang}_{re.sub(r'[^a-zA-Z0-9]+', '_', fill)[:40]}"
                if not any(v["id"] == lid for v in verts):
                    verts.append(
                        {
                            "id": lid,
                            "kind": "form",
                            "lang": lang,
                            "branch": "grammar",
                            "surface": fill,
                            "gloss": fill,
                        }
                    )
                edges.append({"src": sid, "label": "FILLED_BY", "dst": lid})
        cur = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("frame:"):
            flush()
            cur = {"id": "", "gloss": "", "pattern": "", "slots": [], "fillers": []}
            continue
        if cur is None:
            continue
        if line.startswith("  id:"):
            cur["id"] = line.split(":", 1)[1].strip()
        elif line.startswith("  gloss:"):
            cur["gloss"] = line.split(":", 1)[1].strip()
        elif line.startswith("  pattern:"):
            cur["pattern"] = line.split(":", 1)[1].strip()
        elif re.match(r"^\s+slots\[\d+\]:", line):
            cur["slots"] = [x.strip() for x in line.split(":", 1)[1].split(",") if x.strip()]
        elif re.match(r"^\s+fillers\[\d+\]:", line):
            cur["fillers"] = [
                x.strip() for x in line.split(":", 1)[1].split(",") if x.strip()
            ]
    flush()
    return verts, edges


def skilltree_from_horizon(horizon_text: str) -> tuple[list[dict], list[dict], dict]:
    """16-lang skill tree: Horizon → Band → Lang."""
    langs = parse_horizon_langs(horizon_text)
    meta: dict = {"count": len(langs), "age_target": "", "want": ""}
    for line in horizon_text.splitlines():
        if line.startswith("age_target:"):
            meta["age_target"] = line.split(":", 1)[1].strip()
        elif line.startswith("want:"):
            meta["want"] = line.split(":", 1)[1].strip()
        elif line.startswith("count:"):
            try:
                meta["count"] = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass
    verts: list[dict] = [
        {
            "id": "Horizon_polyglot",
            "kind": "horizon",
            "branch": "skilltree",
            "gloss": f"B2+-by-age-{meta.get('age_target') or '?'}",
        }
    ]
    edges: list[dict] = []
    bands_seen: set[str] = set()
    for L in langs:
        band = L["band"]
        bid = f"Band_{band}"
        if band not in bands_seen:
            bands_seen.add(band)
            verts.append(
                {
                    "id": bid,
                    "kind": "band",
                    "branch": "skilltree",
                    "gloss": band.replace("_", "-"),
                }
            )
            edges.append({"src": "Horizon_polyglot", "label": "TARGETS", "dst": bid})
        lid = f"Lang_{L['code']}"
        verts.append(
            {
                "id": lid,
                "kind": "lang",
                "branch": "skilltree",
                "lang": L["code"],
                "gloss": L["name"].replace(" ", "-"),
                "surface": L["code"],
                "band": band,
                "script": L.get("script") or "",
            }
        )
        edges.append({"src": bid, "label": "IN_BAND", "dst": lid})
    return verts, edges, {"langs": langs, **meta}


def collect_language() -> dict:
    """Separate language-learn graphs (not pedagogy/universe.graph.md)."""
    base = ROOT / "pedagogy" / "_learn"
    bridge_v, bridge_e = parse_graph(base / "polyglot" / "bridge.graph.md")
    lex_v, lex_e = parse_graph(base / "writing-accuracy" / "lexicon.graph.md")
    frames_dir = base / "polyglot" / "frames"
    fr_v: list[dict] = []
    fr_e: list[dict] = []
    if frames_dir.is_dir():
        for fp in sorted(frames_dir.glob("*.toon.md")):
            code = fp.stem  # de, fr, …
            v, e = frames_to_graph(read(fp), code)
            fr_v.extend(v)
            fr_e.extend(e)
    horizon_text = read(base / "polyglot" / "horizon.toon.md")
    st_v, st_e, horizon_meta = skilltree_from_horizon(horizon_text)
    wa_state = read(base / "writing-accuracy" / "state.toon.md")
    target = "de"
    one_focus = ""
    for line in wa_state.splitlines():
        if line.startswith("targetLang:"):
            target = line.split(":", 1)[1].strip() or "de"
        elif line.startswith("oneFocus:"):
            one_focus = line.split(":", 1)[1].strip()
    return {
        "targetLang": target,
        "oneFocus": one_focus,
        "horizon": horizon_meta,
        "polyglot": _graph_pack(bridge_v, bridge_e, default_branch="polyglot"),
        "wortschatz": _graph_pack(lex_v, lex_e, default_branch="wortschatz"),
        "grammar": _graph_pack(fr_v, fr_e, default_branch="grammar"),
        "skilltree": _graph_pack(st_v, st_e, default_branch="skilltree"),
    }


def is_stack(v: dict) -> bool:
    return "/stack/" in v.get("body", "")


def vertex_branch(v: dict) -> str:
    """pedagogy/<branch>/… → being|math|physics|biology|computation|language|stack|other."""
    body = (v.get("body") or "").replace("\\", "/")
    if "/stack/" in body:
        return "stack"
    m = re.search(r"pedagogy/([^/]+)/", body)
    return m.group(1) if m else "other"


BRANCH_FILL = {
    "being": "#1a237e",
    "math": "#004d40",
    "physics": "#263238",
    "biology": "#1b3a4b",
    "computation": "#3e2723",
    "language": "#0d47a1",
    "stack": "#37474f",
    "other": "#212121",
    "polyglot": "#4a148c",
    "wortschatz": "#0d47a1",
    "grammar": "#1b5e20",
    "skilltree": "#01579b",
}
BRANCH_EDGE = {
    "being": "#90caf9",
    "math": "#69f0ae",
    "physics": "#b0bec5",
    "biology": "#80deea",
    "computation": "#ffcc80",
    "language": "#82b1ff",
    "stack": "#90a4ae",
    "other": "#757575",
    "polyglot": "#ce93d8",
    "wortschatz": "#82b1ff",
    "grammar": "#a5d6a7",
    "skilltree": "#4fc3f7",
}


def parse_root_organs(text: str) -> list[dict]:
    organs: list[dict] = []
    current: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if re.match(r"^- (DIR|FILE|TAG) ", line):
            if current:
                organs.append(current)
            kind, name = line[2:].split(None, 1)
            current = {"tag": kind, "name": name.strip(), "kind": "", "meaning": ""}
            continue
        if current is None:
            continue
        m = re.match(r"^\s+- KIND (.+)$", line)
        if m and not current["kind"]:
            current["kind"] = m.group(1).strip()
            continue
        m = re.match(r"^\s+- MEANING (.+)$", line)
        if m and not current["meaning"]:
            current["meaning"] = m.group(1).strip()
            continue
    if current:
        organs.append(current)
    return organs


def parse_goals(text: str) -> dict:
    out: dict = {
        "focus": "",
        "active": [],
        "nodes": [],
        "north": [],
        "as_of": "",
    }
    for line in text.splitlines():
        if line.startswith("focus:"):
            out["focus"] = line.split(":", 1)[1].strip()
        elif line.startswith("as_of:"):
            out["as_of"] = line.split(":", 1)[1].strip()
        elif line.startswith("active["):
            rest = line.split(":", 1)[1].strip()
            out["active"] = [x.strip() for x in rest.split(",") if x.strip()]
        elif re.match(r"^\s+\S+,", line) and "nodes[" not in line:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) >= 7:
                node = {
                    "id": parts[0],
                    "kind": parts[1],
                    "want": parts[2],
                    "status": parts[5],
                    "north": parts[6].split(),
                }
                out["nodes"].append(node)
                if node["id"] == out["focus"] or not out["north"]:
                    out["north"] = node["north"]
    for n in out["nodes"]:
        if n["id"] == out["focus"]:
            out["north"] = n["north"]
            break
    return out


def parse_plans(text: str) -> list[dict]:
    plans: list[dict] = []
    cur: dict | None = None
    for raw in text.splitlines():
        m = PLAN_RE.search(raw)
        if m:
            if cur:
                plans.append(cur)
            cur = {"id": m.group(1), "now": "", "next": [], "why": ""}
            continue
        if cur is None:
            continue
        if re.match(r"^\s+- NOW ", raw):
            cur["now"] = raw.split("NOW", 1)[1].strip()
        elif re.match(r"^\s+- NEXT ", raw):
            cur["next"] = raw.split("NEXT", 1)[1].strip().split()
        elif re.match(r"^\s+- WHY ", raw):
            cur["why"] = raw.split("WHY", 1)[1].strip()
        elif re.match(r"^- (STUDY|DAY|PROTOCOL|PLAN) ", raw) and "PLAN $" not in raw:
            if cur:
                plans.append(cur)
                cur = None
    if cur:
        plans.append(cur)
    return plans


def parse_studies(text: str) -> list[dict]:
    studies: list[dict] = []
    cur: dict | None = None
    mode = ""
    probe_lines: list[str] = []
    answer_lines: list[str] = []

    def flush():
        nonlocal cur, mode, probe_lines, answer_lines
        if not cur:
            return
        probe = " ".join(x.strip("- ").strip() for x in probe_lines if x.strip())
        answer = "\n".join(x for x in answer_lines if x.strip()).strip()
        cur["probe"] = probe
        cur["answered"] = bool(answer)
        cur["answer_preview"] = answer[:160]
        studies.append(cur)
        cur = None
        mode = ""
        probe_lines = []
        answer_lines = []

    for raw in text.splitlines():
        m = STUDY_RE.search(raw)
        if m:
            flush()
            cur = {"id": m.group(1), "why": "", "phase": ""}
            continue
        if cur is None:
            continue
        if re.match(r"^- (STUDY|PLAN|DAY|PROTOCOL) ", raw):
            flush()
            continue
        if re.match(r"^\s+- PHASE ", raw):
            cur["phase"] = raw.split("PHASE", 1)[1].strip()
        elif re.match(r"^\s+- WHY ", raw):
            cur["why"] = raw.split("WHY", 1)[1].strip()
        elif re.match(r"^\s+- PROBE\s*$", raw):
            mode = "probe"
        elif re.match(r"^\s+- ANSWER\s*$", raw):
            mode = "answer"
        elif re.match(r"^\s+- (ASSESS|RECALL|GAP|DRILL|STORE|DONE) ", raw) or re.match(
            r"^\s+- (ASSESS|RECALL|GAP)\s*$", raw
        ):
            mode = ""
        elif mode == "probe" and raw.strip().startswith("-"):
            probe_lines.append(raw.strip())
        elif mode == "answer" and raw.strip().startswith("-"):
            answer_lines.append(raw.strip()[1:].strip())
    flush()
    return studies


def parse_cpu_agents(text: str) -> list[dict]:
    agents: list[dict] = []
    for raw in text.splitlines():
        if "AGENT $id=" not in raw:
            continue
        m = AGENT_RE.search(raw)
        if not m:
            continue
        aid = m.group(1)
        when = ""
        wm = re.search(r"\$when=([^=]+?)(?:\s+\$|\s*$)", raw)
        if wm:
            when = wm.group(1).strip()
        prompt = ""
        pm = re.search(r"\$prompt=(.+)$", raw)
        if pm:
            prompt = pm.group(1).strip()[:180]
        agents.append({"id": aid, "when": when or "armed", "prompt": prompt})
    return agents


def parse_dump_pending(text: str) -> list[dict]:
    items: list[dict] = []
    cur: dict | None = None
    in_pending = False
    for raw in text.splitlines():
        if raw.startswith("- PENDING"):
            in_pending = True
            continue
        if raw.startswith("- HUMAN OPEN") or raw.startswith("- DRIPPED") or raw.startswith("- DONE"):
            in_pending = False
            if cur:
                items.append(cur)
                cur = None
            continue
        if not in_pending:
            continue
        m = CAPTURE_RE.search(raw)
        if m:
            if cur:
                items.append(cur)
            cur = {"id": m.group(1), "title": "", "status": "", "kind": ""}
            continue
        if cur is None:
            continue
        if re.match(r"^\s+- TITLE ", raw):
            cur["title"] = raw.split("TITLE", 1)[1].strip()
        elif re.match(r"^\s+- STATUS ", raw):
            cur["status"] = raw.split("STATUS", 1)[1].strip()
        elif re.match(r"^\s+- KIND ", raw):
            cur["kind"] = raw.split("KIND", 1)[1].strip()
    if cur:
        items.append(cur)
    return items


def parse_state_header(text: str) -> dict:
    lines = text.splitlines()
    first = lines[0] if lines else ""
    skip_n = sum(1 for ln in lines if ln.startswith("- "))
    loop = ""
    maintain = ""
    last_organ = ""
    last_delta = ""
    recent_skip: list[str] = []
    in_skip = False
    for ln in lines:
        if ln.startswith("Loop:"):
            loop = ln[:220]
        elif ln.startswith("Maintain:"):
            maintain = ln[:220]
        elif ln.startswith("Maintain last_organ:"):
            last_organ = ln.split(":", 1)[1].strip()[:80]
        elif ln.startswith("Maintain last_delta:"):
            last_delta = ln.split(":", 1)[1].strip()[:200]
        elif ln.strip() == "## Skip":
            in_skip = True
            continue
        elif in_skip and ln.startswith("- "):
            recent_skip.append(ln[2:].strip()[:80])
    return {
        "header": first[:240],
        "skip_count": skip_n,
        "loop": loop,
        "maintain": maintain,
        "last_organ": last_organ,
        "last_delta": last_delta,
        "recent_skip": recent_skip[-12:],
    }


def parse_dump_section(text: str, section: str) -> list[dict]:
    """section is PENDING or HUMAN OPEN."""
    items: list[dict] = []
    cur: dict | None = None
    in_sec = False
    marker = f"- {section}"

    def flush() -> None:
        nonlocal cur
        if cur:
            items.append(cur)
            cur = None

    for raw in text.splitlines():
        if raw.startswith(marker):
            in_sec = True
            continue
        if raw.startswith("- ") and not raw.startswith("  ") and in_sec:
            if not raw.startswith(marker) and re.match(r"^- [A-Z]", raw):
                in_sec = False
                flush()
                continue
        if not in_sec:
            continue
        m = CAPTURE_RE.search(raw)
        if m:
            flush()
            cur = {
                "id": m.group(1),
                "title": "",
                "status": "",
                "kind": "",
                "note": "",
                "why": "",
                "learn": "",
                "when": "",
                "drip": "",
                "urls": [],
                "sources": [],
                "bucket": section.lower().replace(" ", "-"),
            }
            continue
        if cur is None:
            continue
        if re.match(r"^\s+- TITLE ", raw):
            cur["title"] = raw.split("TITLE", 1)[1].strip()
        elif re.match(r"^\s+- STATUS ", raw):
            cur["status"] = raw.split("STATUS", 1)[1].strip()
        elif re.match(r"^\s+- KIND ", raw):
            cur["kind"] = raw.split("KIND", 1)[1].strip()
        elif re.match(r"^\s+- NOTE ", raw):
            cur["note"] = raw.split("NOTE", 1)[1].strip()[:600]
        elif re.match(r"^\s+- WHY ", raw):
            cur["why"] = raw.split("WHY", 1)[1].strip()[:400]
        elif re.match(r"^\s+- LEARN ", raw):
            cur["learn"] = raw.split("LEARN", 1)[1].strip()[:160]
        elif re.match(r"^\s+- WHEN ", raw):
            cur["when"] = raw.split("WHEN", 1)[1].strip()[:160]
        elif re.match(r"^\s+- DRIP ", raw):
            cur["drip"] = raw.split("DRIP", 1)[1].strip()[:280]
        elif re.match(r"^\s+- URL ", raw):
            cur["urls"].append(raw.split("URL", 1)[1].strip())
        elif re.match(r"^\s+- SOURCE ", raw):
            cur["sources"].append(raw.split("SOURCE", 1)[1].strip()[:200])
        elif re.match(r"^\s+- STORE PATH ", raw):
            cur["sources"].append("STORE " + raw.split("STORE PATH", 1)[1].strip()[:160])
    flush()
    return items


def parse_inflow_news(text: str, limit: int = 40) -> list[dict]:
    items: list[dict] = []
    cur: dict | None = None
    for raw in text.splitlines():
        m = re.search(r"NEWS\s+\$id=(\S+)", raw)
        if m:
            if cur:
                items.append(cur)
            cur = {
                "id": m.group(1),
                "title": "",
                "url": "",
                "urls": [],
                "why": "",
                "learn": "",
                "bucket": "news",
            }
            continue
        if cur is None:
            continue
        if re.match(r"^\s+- TITLE ", raw):
            cur["title"] = raw.split("TITLE", 1)[1].strip()
        elif re.match(r"^\s+- URL ", raw):
            u = raw.split("URL", 1)[1].strip()
            cur["url"] = cur["url"] or u
            cur["urls"].append(u)
        elif re.match(r"^\s+- WHY ", raw):
            cur["why"] = raw.split("WHY", 1)[1].strip()[:400]
        elif re.match(r"^\s+- LEARN ", raw):
            cur["learn"] = raw.split("LEARN", 1)[1].strip()
        elif re.match(r"^- TICK ", raw) or re.match(r"^- NEWS ", raw):
            if raw.startswith("- TICK") and cur:
                items.append(cur)
                cur = None
    if cur:
        items.append(cur)
    return items[-limit:]


def parse_cpu_blocks(text: str) -> dict:
    agents = parse_cpu_agents(text)
    schedules: list[dict] = []
    todos: list[dict] = []
    notes: list[str] = []
    note_today: dict = {
        "headline": "",
        "body": [],
        "clock": [],
        "learn": [],
        "loop": [],
        "other": [],
    }
    in_today = False
    for raw in text.splitlines():
        if raw.startswith("- SCHEDULE "):
            in_today = False
            schedules.append({"text": raw[len("- SCHEDULE ") :].strip()[:220]})
        elif raw.startswith("- TODO "):
            in_today = False
            todos.append({"text": raw[len("- TODO ") :].strip()[:180], "done": False})
        elif raw.startswith("- NOTE "):
            payload = raw[len("- NOTE ") :].strip()
            notes.append(payload[:220])
            if payload.upper().startswith("TODAY ") or " TODAY " in f" {payload.upper()}":
                in_today = True
                note_today["headline"] = payload[:280]
            else:
                in_today = False
        elif re.match(r"^\s+- DONE ", raw) and todos:
            todos[-1]["done"] = True
        elif in_today and re.match(r"^\s+- BODY ", raw):
            note_today["body"].append(raw.split("BODY", 1)[1].strip()[:220])
        elif in_today and re.match(r"^\s+- CLOCK ", raw):
            note_today["clock"].append(raw.split("CLOCK", 1)[1].strip()[:220])
        elif in_today and re.match(r"^\s+- LEARN ", raw):
            note_today["learn"].append(raw.split("LEARN", 1)[1].strip()[:220])
        elif in_today and re.match(r"^\s+- LOOP ", raw):
            note_today["loop"].append(raw.split("LOOP", 1)[1].strip()[:220])
        elif in_today and re.match(r"^\s+- ", raw) and not re.match(
            r"^\s+- (STORE|DONE) ", raw
        ):
            note_today["other"].append(raw.strip()[2:][:220])
        elif raw.startswith("- AGENT ") or raw.startswith("- SCHEDULE ") or raw.startswith(
            "- LEARNING_DUMP "
        ):
            in_today = False
    return {
        "agents": agents,
        "schedules": schedules,
        "todos": todos,
        "notes": notes,
        "note_today": note_today,
    }


def berlin_today() -> tuple[str, str]:
    try:
        from zoneinfo import ZoneInfo

        now = datetime.now(ZoneInfo("Europe/Berlin"))
    except Exception:
        now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%d"), now.strftime("%A")


def harvest_covers_day(row: dict, day: str) -> bool:
    start = (row.get("start") or "")[:10]
    end = (row.get("end") or start)[:10]
    if not start:
        return False
    # all-day multi-day: end exclusive in some rows (IFA ends 09-09 for 04-08)
    if end and end < start:
        end = start
    if not end or end == start:
        return start == day
    return start <= day <= end or start <= day < end


def build_today(
    *,
    cpu: dict,
    schedule: dict,
    plans: list[dict],
    studies: list[dict],
    goals: dict,
    self_pack: dict,
    inflow: dict,
    weights: dict,
) -> dict:
    day, weekday = berlin_today()
    nt = cpu.get("note_today") or {}
    harvest_today = [
        r for r in (schedule.get("harvest") or []) if harvest_covers_day(r, day)
    ]
    # CPU SCHEDULE text that mentions today's date or IFA range covering today
    cpu_sched_today = []
    for s in cpu.get("schedules") or []:
        t = s.get("text") or ""
        if day in t or day.replace("-", ".") in t:
            cpu_sched_today.append(t)
        elif re.search(r"2026-09-0[4-8]", t) and day >= "2026-09-04" and day <= "2026-09-08":
            if "IFA" in t.upper() or "ifa" in t:
                cpu_sched_today.append(t)

    focus = goals.get("focus") or ""
    plan_now = ""
    plan_next = []
    for pl in plans:
        if pl.get("id") == focus or (not plan_now and pl.get("now")):
            if pl.get("id") == focus:
                plan_now = pl.get("now") or ""
                plan_next = pl.get("next") or []
                break
    if not plan_now:
        for pl in plans:
            if pl.get("now"):
                plan_now = pl["now"]
                plan_next = pl.get("next") or []
                break

    probe = None
    for s in studies:
        if s.get("id") == plan_now:
            probe = s
            break

    endu = self_pack.get("endurance") or {}
    logs = endu.get("logs") or []
    last_log = {}
    for lg in logs:
        if lg.get("date") == day:
            last_log = lg
            break
    if not last_log and logs:
        last_log = sorted(logs, key=lambda x: x.get("date") or "")[-1]
    foggy = bool(
        last_log
        and (
            "fog" in (last_log.get("sore") or "").lower()
            or "fog" in (last_log.get("note") or "").lower()
        )
    )
    train = self_pack.get("training") or {}
    routine = self_pack.get("routine") or {}
    week_today = None
    for w in train.get("week") or []:
        if w.get("date") == day:
            week_today = w
            break
    sessions_today = [s for s in (train.get("sessions") or []) if s.get("date") == day]
    injury = train.get("injury") or {}
    pending = [
        d for d in (inflow.get("pending") or []) if (d.get("status") or "") == "pending"
    ]
    top_w = (weights.get("nodes") or [])[:5]

    actions: list[dict] = []

    def add(priority: int, kind: str, source: str, text: str) -> None:
        actions.append(
            {"priority": priority, "kind": kind, "source": source, "text": text[:280]}
        )

    # injury blockers first
    if injury.get("active"):
        for b in injury.get("blockers") or []:
            add(1, "injury", "training.flags", b)
        for n in (injury.get("notes") or [])[:3]:
            add(1, "injury", "training.injury", n)
        regs = ", ".join(injury.get("regions") or [])
        if regs:
            add(1, "injury", "training.injury", f"region: {regs}")

    # blockers / stops
    for b in nt.get("body") or []:
        low = b.lower()
        if any(x in low for x in ("no ", "skip", "stop", "not a ", "rest")):
            add(1, "stop", "CPU NOTE BODY", b)
        else:
            add(2, "body", "CPU NOTE BODY", b)
    for c in nt.get("clock") or []:
        if day in c or weekday[:3].lower() in c.lower():
            add(2, "clock", "CPU NOTE CLOCK", c)
        else:
            add(4, "ahead", "CPU NOTE CLOCK", c)
    for lp in nt.get("loop") or []:
        add(1, "stop", "CPU NOTE LOOP", lp)

    for r in harvest_today:
        st = r.get("status") or ""
        title = r.get("title") or r.get("id") or ""
        where = r.get("where") or ""
        if st == "confirmed":
            add(2, "calendar", "harvest confirmed", f"{title} · {where}")
        else:
            add(3, "calendar", "harvest candidate", f"{title} · {where}")

    for t in cpu_sched_today:
        add(2, "calendar", "CPU SCHEDULE", t)

    # training plan today
    if week_today:
        add(
            2,
            "train",
            f"week.{week_today.get('role')}",
            f"{week_today.get('do')} · blocker {week_today.get('blocker')}",
        )
    for sess in sessions_today:
        skip = ", ".join(sess.get("skip") or [])
        add(
            2,
            "train",
            f"session.{sess.get('status')}",
            f"{sess.get('label')} · skip [{skip}] · {sess.get('skipNote') or ''}",
        )
        for blk in (sess.get("blocks") or [])[:6]:
            add(
                2,
                "train",
                "session.block",
                f"{blk.get('min')}: {blk.get('do')} (RPE {blk.get('rpe')}) {blk.get('note') or ''}",
            )

    for fl in train.get("flags_true") or []:
        if fl not in (injury.get("blockers") or []):
            if "skip" in fl.lower() or "scapula" in fl.lower() or "pain" in fl.lower():
                add(1, "stop", "training.flags", fl)

    # daily routine + preventive due
    for d in routine.get("daily") or []:
        slot = d.get("slot") or ""
        pri = 2 if slot == "morning" else 3
        add(
            pri,
            "routine",
            f"routine.daily.{slot}",
            f"{d.get('label')} / {d.get('label_zh')} ({d.get('minutes')}m) — {d.get('protocol') or ''}",
        )
    for r in routine.get("due") or []:
        add(
            2 if r.get("due_state") == "due" else 3,
            "routine",
            f"routine.periodic.{r.get('due_state')}",
            f"{r.get('label')} / {r.get('label_zh')} — {r.get('due_state')} (every {r.get('interval_months')}mo). Log last visit; do not invent Termin.",
        )
    for o in (routine.get("optimize") or [])[:2]:
        add(4, "routine", "routine.optimize", f"{o.get('change')} — {o.get('why')}")

    if foggy:
        add(
            1,
            "stop",
            "endurance.log",
            f"{last_log.get('date')}: {last_log.get('sore')} — {last_log.get('note')}",
        )
        add(3, "rest", "endurance", "Fog/rest: do not pile DAY. Empty PROBE stays empty until asked.")
    else:
        for act in endu.get("activities") or []:
            add(
                3,
                "drill",
                "endurance.activity",
                f"{act.get('label') or act.get('id')} → {act.get('vertex')}",
            )

    if probe and not probe.get("answered"):
        pri = 4 if foggy else 3
        add(
            pri,
            "learn",
            f"STUDY {plan_now}",
            probe.get("probe")
            or f"Open PROBE on {plan_now} (ANSWER empty). Do not invent ANSWER.",
        )
    for ln in nt.get("learn") or []:
        add(3 if not foggy else 4, "learn", "CPU NOTE LEARN", ln)

    if pending:
        add(
            4,
            "inflow",
            "DUMP pending",
            f"{len(pending)} CAPTURE pending — drip when human is back (dump-drip).",
        )

    if top_w and not foggy:
        ids = ", ".join(f"{n['id']}★{n['total']}" for n in top_w[:3])
        add(5, "north", "weights", f"If quiet later: highest attention {ids}")

    # next session lookahead
    ns = train.get("next_session") or {}
    if ns.get("bench_when") or ns.get("bench_top"):
        add(
            4,
            "ahead",
            "nextSession.bench",
            f"earliest {ns.get('bench_when')} · {ns.get('bench_top')} · {ns.get('bench_condition')}",
        )

    actions.sort(key=lambda a: (a["priority"], a["kind"]))

    return {
        "date": day,
        "weekday": weekday,
        "tz": "Europe/Berlin",
        "headline": nt.get("headline") or f"TODAY {day}",
        "focus": focus,
        "plan_now": plan_now,
        "plan_next": plan_next,
        "probe": {
            "id": (probe or {}).get("id") or plan_now,
            "text": (probe or {}).get("probe") or "",
            "answered": bool((probe or {}).get("answered")),
        },
        "harvest_today": harvest_today,
        "cpu_sched_today": cpu_sched_today,
        "note_today": nt,
        "foggy": foggy,
        "budget_now": endu.get("budget_now") or "",
        "training_flags": train.get("flags_true") or [],
        "training_week": week_today,
        "training_sessions": sessions_today,
        "injury": injury,
        "periodization": train.get("periodization") or {},
        "routine": routine,
        "pending_dumps": len(pending),
        "actions": actions,
    }


def parse_toon_kv_prefix(text: str, keys: list[str]) -> dict:
    out: dict = {}
    for line in text.splitlines():
        if ":" not in line or line.startswith(" ") and not line.strip().startswith(tuple(keys)):
            pass
        for k in keys:
            if line.startswith(f"{k}:"):
                out[k] = line.split(":", 1)[1].strip()
            elif re.match(rf"^\s+{re.escape(k)}:", line):
                out[k] = line.split(":", 1)[1].strip()
    return out


def parse_endurance(text: str) -> dict:
    out = {
        "budget_now": "",
        "budget_default": "",
        "activities": [],
        "logs": [],
    }
    for line in text.splitlines():
        if line.startswith("budget.now:"):
            out["budget_now"] = line.split(":", 1)[1].strip()
        elif line.startswith("budget.default:"):
            out["budget_default"] = line.split(":", 1)[1].strip()
        elif line.startswith("  id:") and "activity" in text[: text.find(line) + 1] or False:
            pass
    # activities: blocks starting with activity:
    cur = None
    mode = ""
    for line in text.splitlines():
        if line.startswith("activity:"):
            if cur:
                out["activities"].append(cur)
            cur = {"id": "", "label": "", "vertex": ""}
            mode = "activity"
            continue
        if line.startswith("session[") or line.startswith("log["):
            if cur and mode == "activity":
                out["activities"].append(cur)
                cur = None
            mode = "log" if line.startswith("log[") else "session"
            continue
        if mode == "activity" and cur is not None:
            if line.strip().startswith("id:"):
                cur["id"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("label:"):
                cur["label"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("vertex:"):
                cur["vertex"] = line.split(":", 1)[1].strip()
        if mode == "log" and re.match(r"^\s+\d{4}-\d{2}-\d{2},", line):
            parts = [p.strip() for p in line.strip().split(",", 5)]
            out["logs"].append(
                {
                    "date": parts[0] if parts else "",
                    "sore": parts[3] if len(parts) > 3 else "",
                    "note": parts[5] if len(parts) > 5 else (parts[-1] if parts else ""),
                }
            )
    if cur and mode == "activity":
        out["activities"].append(cur)
    out["logs"] = out["logs"][-8:]
    return out


def parse_learn(text: str) -> dict:
    out = {"target": "", "updated": "", "nodes": []}
    for line in text.splitlines():
        if line.startswith("target:"):
            out["target"] = line.split(":", 1)[1].strip()
        elif line.startswith("updated:"):
            out["updated"] = line.split(":", 1)[1].strip()
        elif re.match(r"^\s+\S+,(unknown|weak|partial|firm)", line) or re.match(
            r"^\s+\S+,\w*,", line
        ):
            parts = [p.strip() for p in line.strip().split(",")]
            if parts:
                out["nodes"].append(
                    {
                        "id": parts[0],
                        "grasp": parts[1] if len(parts) > 1 else "",
                    }
                )
    return out


def parse_training_pulse(text: str) -> dict:
    """Full training store for train/injury views. Alias kept for collect_self."""
    out: dict = {
        "updated": "",
        "bodyweightKg": "",
        "bodyweightAsOf": "",
        "bodyweightPrev": "",
        "flags_true": [],
        "flags": {},
        "claimed_bench": "",
        "session_e1rm": "",
        "pullups_best": "",
        "periodization": {},
        "week": [],
        "sessions": [],
        "next_session": {},
        "logs": [],
        "rules": [],
        "injury": {
            "active": False,
            "regions": [],
            "blockers": [],
            "notes": [],
        },
    }
    m = re.search(r'^updated:\s*"?([^"\n]+)"?', text, re.M)
    if m:
        out["updated"] = m.group(1).strip()
    m = re.search(r"^\s+bodyweightKg:\s*([0-9.]+)", text, re.M)
    if m:
        out["bodyweightKg"] = m.group(1)
    m = re.search(r"^\s+bodyweightKg\.asOf:\s*\"?([^\n\"]+)", text, re.M)
    if m:
        out["bodyweightAsOf"] = m.group(1).strip()
    m = re.search(r"^\s+bodyweightKg\.prevKg:\s*([0-9.]+)", text, re.M)
    if m:
        out["bodyweightPrev"] = m.group(1)
    m = re.search(r"claimed1rmKg:\s*\n\s+benchPress:\s*([0-9.]+)", text)
    if m:
        out["claimed_bench"] = m.group(1)
    m = re.search(r"sessionEstimated1rmKg:\s*\n\s+benchPress:\s*([0-9.]+)", text)
    if m:
        out["session_e1rm"] = m.group(1)
    m = re.search(r"pullups:\s*\n(?:.*\n)*?\s+bestSetReps:\s*(\d+)", text)
    if m:
        out["pullups_best"] = m.group(1)

    # flags block
    in_flags = False
    for line in text.splitlines():
        if line.startswith("flags:"):
            in_flags = True
            continue
        if in_flags:
            if re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
                in_flags = False
            else:
                fm = re.match(r"^  ([A-Za-z0-9_.]+):\s*(.+)$", line)
                if fm:
                    key, val = fm.group(1), fm.group(2).strip().strip('"')
                    out["flags"][key] = val
                    if val.lower() == "true":
                        out["flags_true"].append(key)

    # periodization
    in_per = False
    for line in text.splitlines():
        if line.startswith("periodization:"):
            in_per = True
            continue
        if in_per:
            if re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
                in_per = False
            else:
                pm = re.match(r"^  ([A-Za-z0-9_.]+):\s*(.+)$", line)
                if pm and not pm.group(1).startswith("nextMeso"):
                    out["periodization"][pm.group(1)] = pm.group(2).strip()[:200]
                if line.strip().startswith("kind:"):
                    out["periodization"]["nextMeso.kind"] = line.split(":", 1)[1].strip()
                if line.strip().startswith("startAfter:"):
                    out["periodization"]["nextMeso.startAfter"] = line.split(":", 1)[1].strip()[
                        :160
                    ]
                if line.strip().startswith("e1rmKg:"):
                    out["periodization"]["nextMeso.e1rmKg"] = line.split(":", 1)[1].strip()

    # week rows
    week_key = None
    for line in text.splitlines():
        if re.match(r"^weekUntil", line):
            week_key = line.split("{", 1)[0].strip()
            continue
        if week_key and re.match(r"^\s+\d{4}-\d{2}-\d{2},", line):
            parts = [p.strip() for p in line.strip().split(",", 3)]
            if len(parts) >= 3:
                out["week"].append(
                    {
                        "date": parts[0],
                        "role": parts[1],
                        "do": parts[2],
                        "blocker": parts[3] if len(parts) > 3 else "",
                    }
                )
        elif week_key and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            week_key = None

    # sessions (may repeat)
    cur: dict | None = None
    mode = ""
    for line in text.splitlines():
        if line.startswith("session:"):
            if cur:
                out["sessions"].append(cur)
            cur = {
                "id": "",
                "date": "",
                "label": "",
                "status": "",
                "skip": [],
                "skipNote": "",
                "pain": {},
                "blocks": [],
            }
            mode = "session"
            continue
        if line.startswith("nextSession:"):
            if cur:
                out["sessions"].append(cur)
                cur = None
            mode = "next"
            out["next_session"] = {
                "bench_when": "",
                "bench_top": "",
                "bench_condition": "",
                "pull": "",
                "technique": "",
            }
            continue
        if line.startswith("log[") or line.startswith("agentHints") or line.startswith(
            "periodization:"
        ):
            if cur and mode == "session":
                out["sessions"].append(cur)
                cur = None
            mode = "log" if line.startswith("log[") else mode
            if line.startswith("log["):
                mode = "log"
            continue
        if mode == "session" and cur is not None:
            if re.match(r"^  id:", line):
                cur["id"] = line.split(":", 1)[1].strip()
            elif re.match(r'^  date:', line):
                cur["date"] = line.split(":", 1)[1].strip().strip('"')
            elif re.match(r"^  label:", line):
                cur["label"] = line.split(":", 1)[1].strip().strip('"')[:160]
            elif re.match(r"^  status:", line):
                cur["status"] = line.split(":", 1)[1].strip()
            elif re.match(r"^  skipNote:", line):
                cur["skipNote"] = line.split(":", 1)[1].strip()[:200]
            elif re.match(r"^  skip\[", line):
                cur["skip"] = [
                    x.strip() for x in line.split(":", 1)[1].split(",") if x.strip()
                ]
            elif re.match(r"^    region:", line):
                cur["pain"]["region"] = line.split(":", 1)[1].strip()
            elif re.match(r"^    regionZh:", line):
                cur["pain"]["regionZh"] = line.split(":", 1)[1].strip()
            elif re.match(r"^    quality:", line):
                cur["pain"]["quality"] = line.split(":", 1)[1].strip()
            elif re.match(r"^    reliefPct:", line):
                cur["pain"]["reliefPct"] = line.split(":", 1)[1].strip()
            elif re.match(r"^    action:", line):
                cur["pain"]["action"] = line.split(":", 1)[1].strip()[:120]
            elif re.match(r"^\s+\d|^\s+open,|^\s+then,", line) and "block" in text[
                max(0, text.find(line) - 200) : text.find(line)
            ]:
                pass
            # block rows like `    0-4,easy bike,3,...`
            if re.match(r"^\s{4}[\dopen]", line) or re.match(r"^\s{4}then,", line):
                parts = [p.strip() for p in line.strip().split(",", 3)]
                if len(parts) >= 2:
                    cur["blocks"].append(
                        {
                            "min": parts[0],
                            "do": parts[1],
                            "rpe": parts[2] if len(parts) > 2 else "",
                            "note": parts[3] if len(parts) > 3 else "",
                        }
                    )
        if mode == "next":
            if "whenEarliest:" in line:
                out["next_session"]["bench_when"] = line.split(":", 1)[1].strip().strip('"')
            elif "targetTop:" in line:
                out["next_session"]["bench_top"] = line.split(":", 1)[1].strip().strip('"')
            elif re.match(r"^    condition:", line):
                out["next_session"]["bench_condition"] = line.split(":", 1)[1].strip()[:160]
            elif re.match(r"^    then:", line):
                out["next_session"]["pull"] = line.split(":", 1)[1].strip()[:120]
            elif re.match(r"^    cue:", line):
                out["next_session"]["technique"] = line.split(":", 1)[1].strip()[:120]
        if mode == "log" and re.match(r"^\s+\d{4}-\d{2}-\d{2},", line):
            parts = [p.strip() for p in line.strip().split(",", 2)]
            if len(parts) >= 3:
                out["logs"].append({"date": parts[0], "kind": parts[1], "note": parts[2][:200]})

    if cur:
        out["sessions"].append(cur)

    # rules
    in_rules = False
    for line in text.splitlines():
        if line.startswith("rules["):
            in_rules = True
            continue
        if in_rules:
            if line.startswith("session:") or (
                re.match(r"^[a-zA-Z]", line) and not line.startswith(" ")
            ):
                in_rules = False
            elif line.strip().startswith("- "):
                out["rules"].append(line.strip()[2:][:160])

    # injury synthesis
    blockers = []
    regions = []
    notes = []
    if out["flags"].get("leftScapulaPain", "").lower() == "true":
        out["injury"]["active"] = True
        regions.append("left scapula / 左肩胛")
        blockers.append("leftScapulaPain")
        relief = out["flags"].get("leftScapulaReliefPct", "")
        if relief:
            notes.append(f"reliefPct {relief}% asOf {out['flags'].get('leftScapulaReliefAsOf', '')}")
    if out["flags"].get("skipHeavyPressUntilClear", "").lower() == "true":
        out["injury"]["active"] = True
        blockers.append("skipHeavyPressUntilClear")
        notes.append(out["flags"].get("nextHeavyBenchNote", "")[:160])
    if out["flags"].get("rotationTorsoInvokesScapula", "").lower() == "true":
        out["injury"]["active"] = True
        blockers.append("rotationTorsoInvokesScapula")
        notes.append(out["flags"].get("rotationTorsoInvokesScapula.note", "")[:120])
    if out["flags"].get("nextHeavyBenchEarliest"):
        notes.append(f"next heavy bench earliest {out['flags']['nextHeavyBenchEarliest']}")
    for s in out["sessions"]:
        if s.get("pain"):
            out["injury"]["active"] = True
            if s["pain"].get("region"):
                regions.append(s["pain"]["region"])
            if s["pain"].get("regionZh"):
                regions.append(s["pain"]["regionZh"])
    # recent pain/doms logs
    for lg in out["logs"][-12:]:
        if lg["kind"] in ("pain", "doms"):
            notes.append(f"{lg['date']} {lg['kind']}: {lg['note'][:100]}")
    # uniq
    seen = set()
    out["injury"]["regions"] = []
    for r in regions:
        if r and r not in seen:
            seen.add(r)
            out["injury"]["regions"].append(r)
    out["injury"]["blockers"] = blockers
    seen_n = set()
    out["injury"]["notes"] = []
    for n in notes:
        if n and n not in seen_n:
            seen_n.add(n)
            out["injury"]["notes"].append(n)
    out["logs"] = out["logs"][-15:]
    return out


def parse_harvest_rows(text: str) -> list[dict]:
    import csv
    import io

    rows: list[dict] = []
    started = False
    for line in text.splitlines():
        if line.startswith("nodes["):
            started = True
            continue
        if not started or not line.strip() or line.startswith("schema:"):
            continue
        if not line.startswith("  "):
            continue
        try:
            parts = next(csv.reader(io.StringIO(line.strip())))
        except Exception:
            continue
        if len(parts) < 6:
            continue
        rows.append(
            {
                "id": parts[0],
                "start": parts[1],
                "end": parts[2],
                "title": parts[3],
                "where": parts[4][:80],
                "status": parts[5],
                "gap": parts[11] if len(parts) > 11 else "",
            }
        )
    return rows


def parse_enrich_records(text: str) -> list[dict]:
    rows: list[dict] = []
    cur: dict | None = None
    for line in text.splitlines():
        if line.startswith("record:"):
            if cur:
                rows.append(cur)
            cur = {"title": "", "when": "", "where": "", "why": "", "match": ""}
            continue
        if cur is None:
            continue
        for key in ("title", "when", "where", "why", "match", "what"):
            if line.startswith(f"  {key}:"):
                cur[key] = line.split(":", 1)[1].strip()[:180]
    if cur:
        rows.append(cur)
    return rows


def parse_schedule_month(text: str) -> list[dict]:
    rows: list[dict] = []
    cur: dict | None = None
    for raw in text.splitlines():
        if re.match(r"^- SCHEDULE ", raw):
            if cur:
                rows.append(cur)
            cur = {"when": raw.split("SCHEDULE", 1)[1].strip()[:120], "what": "", "where": "", "why": ""}
            continue
        if cur is None:
            continue
        if re.match(r"^\s+- WHAT ", raw):
            cur["what"] = raw.split("WHAT", 1)[1].strip()[:160]
        elif re.match(r"^\s+- WHERE ", raw):
            cur["where"] = raw.split("WHERE", 1)[1].strip()[:120]
        elif re.match(r"^\s+- WHY ", raw):
            cur["why"] = raw.split("WHY", 1)[1].strip()[:160]
        elif raw.startswith("- SCHEDULE ") or (raw.startswith("- ") and not raw.startswith("  ")):
            if not raw.startswith("- SCHEDULE"):
                rows.append(cur)
                cur = None
    if cur:
        rows.append(cur)
    return rows


def list_dir_files(rel: str, patterns: tuple[str, ...]) -> list[dict]:
    base = ROOT / rel
    if not base.exists():
        return []
    out: list[dict] = []
    for pat in patterns:
        for p in sorted(base.glob(pat)):
            if p.name.startswith("."):
                continue
            if p.is_dir():
                continue
            schema = ""
            kind = ""
            try:
                head = p.read_text(encoding="utf-8", errors="replace").splitlines()[:8]
                for ln in head:
                    if ln.startswith("schema:"):
                        schema = ln.split(":", 1)[1].strip()
                    if re.match(r"^- KIND ", ln):
                        kind = ln.split("KIND", 1)[1].strip()[:100]
                    if ln.startswith("- NOTE ") and not kind:
                        kind = ln.split("NOTE", 1)[1].strip()[:100]
            except Exception:
                pass
            out.append(
                {
                    "path": f"{rel}/{p.name}".replace("\\", "/"),
                    "name": p.name,
                    "bytes": p.stat().st_size,
                    "mtime": datetime.fromtimestamp(p.stat().st_mtime, timezone.utc).strftime(
                        "%Y-%m-%d"
                    ),
                    "schema": schema,
                    "kind": kind,
                }
            )
    # de-dupe by path
    seen = set()
    uniq = []
    for x in out:
        if x["path"] in seen:
            continue
        seen.add(x["path"])
        uniq.append(x)
    return uniq


def collect_cron() -> dict:
    jobs = []
    for p in sorted((ROOT / "cron").glob("*.fu.md")):
        text = read(p)
        agents = AGENT_RE.findall(text)
        kind = ""
        m = re.search(r"^- KIND (.+)$", text, re.M)
        if m:
            kind = m.group(1).strip()[:120]
        recurring = bool(re.search(r"RECURRING", text))
        jobs.append(
            {
                "file": f"cron/{p.name}",
                "kind": kind,
                "agents": agents,
                "recurring": recurring,
                "has_py": (ROOT / "cron" / (p.stem + ".py")).exists(),
            }
        )
    scripts = []
    for p in sorted((ROOT / "cron").glob("*.py")):
        scripts.append({"file": f"cron/{p.name}", "bytes": p.stat().st_size})
    return {"jobs": jobs, "scripts": scripts}


def parse_routine(text: str) -> dict:
    """self/routine.toon.md → daily / periodic due / tips / optimize for Today."""

    def split_csvish(line: str) -> list[str]:
        out: list[str] = []
        cur: list[str] = []
        in_q = False
        for ch in line:
            if ch == '"':
                in_q = not in_q
                cur.append(ch)
            elif ch == "," and not in_q:
                out.append("".join(cur).strip().strip('"'))
                cur = []
            else:
                cur.append(ch)
        out.append("".join(cur).strip().strip('"'))
        return out

    def section_rows(header: str) -> list[list[str]]:
        rows = []
        started = False
        for line in text.splitlines():
            if line.startswith(header):
                started = True
                continue
            if started and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
                break
            if started and re.match(r"^\s+\S+,", line):
                rows.append(split_csvish(line.strip()))
        return rows

    def add_months(d, months: int):
        from datetime import date as date_cls

        m = d.month - 1 + months
        y = d.year + m // 12
        m = m % 12 + 1
        dim = [
            31,
            29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31,
        ][m - 1]
        return date_cls(y, m, min(d.day, dim))

    day, _ = berlin_today()
    from datetime import date as date_cls

    today = date_cls.fromisoformat(day)
    daily = []
    for p in section_rows("daily["):
        if len(p) < 5:
            continue
        if (p[4] or "true").lower() != "true":
            continue
        daily.append(
            {
                "id": p[0],
                "slot": p[1],
                "label": p[2],
                "label_zh": p[3] if len(p) > 3 else "",
                "minutes": p[5] if len(p) > 5 else "",
                "protocol": p[6] if len(p) > 6 else "",
                "source": p[7] if len(p) > 7 else "",
            }
        )
    periodic = []
    for p in section_rows("periodic["):
        if len(p) < 4:
            continue
        last = p[4] if len(p) > 4 else ""
        nxt = p[5] if len(p) > 5 else ""
        interval = int(p[3] or 0)
        due_state = "ask-human-log-last"
        if last and interval:
            try:
                ld = date_cls.fromisoformat(last[:10])
                nxt = add_months(ld, interval).isoformat()
            except ValueError:
                pass
        if not last:
            due_state = "ask-human-log-last"
        elif nxt:
            try:
                nd = date_cls.fromisoformat(nxt[:10])
                if nd <= today:
                    due_state = "due"
                elif (nd - today).days <= 30:
                    due_state = "soon"
                else:
                    due_state = "ok"
            except ValueError:
                due_state = "ask-human"
        periodic.append(
            {
                "id": p[0],
                "label": p[1],
                "label_zh": p[2],
                "interval_months": interval,
                "last_done": last,
                "next_due": nxt,
                "status": p[6] if len(p) > 6 else "open",
                "due_state": due_state,
                "note": p[8] if len(p) > 8 else "",
            }
        )
    tips = []
    for p in section_rows("tip["):
        if len(p) >= 4:
            tips.append({"id": p[0], "topic": p[1], "text": p[2], "source": p[3]})
    optimize = []
    for p in section_rows("optimize["):
        if len(p) >= 5 and p[4] == "open":
            optimize.append(
                {
                    "id": p[0],
                    "habit": p[1],
                    "change": p[2],
                    "why": p[3],
                    "status": p[4],
                }
            )
    return {
        "daily": daily,
        "periodic": periodic,
        "tips": tips[-5:],
        "optimize": optimize,
        "due": [x for x in periodic if x["due_state"] in ("due", "soon", "ask-human-log-last")],
    }


def collect_self() -> dict:
    files = list_dir_files("self", ("*.toon.md", "*.fu.md"))
    # drop lebenslauf / identity-ish from display of contents but keep file name only
    public_files = []
    for f in files:
        if "lebenslauf" in f["name"] or f["name"].startswith("identity"):
            public_files.append({**f, "kind": "gitignored-particulars (name only)", "schema": "private-ish"})
        else:
            public_files.append(f)
    return {
        "files": public_files,
        "goals": parse_goals(read(ROOT / "self" / "goals.toon.md")),
        "endurance": parse_endurance(read(ROOT / "self" / "endurance.toon.md")),
        "learn": parse_learn(read(ROOT / "self" / "learn.toon.md")),
        "training": parse_training_pulse(read(ROOT / "self" / "training.toon.md")),
        "routine": parse_routine(read(ROOT / "self" / "routine.toon.md")),
    }


def collect_schedule() -> dict:
    harvest = parse_harvest_rows(read(ROOT / "schedule" / "harvest.toon.md"))
    enrich = parse_enrich_records(read(ROOT / "schedule" / "enrich.toon.md"))
    months = []
    for p in sorted((ROOT / "schedule").glob("*.fu.md")):
        months.append(
            {
                "file": f"schedule/{p.name}",
                "rows": parse_schedule_month(read(p)),
            }
        )
    return {
        "files": list_dir_files("schedule", ("*.toon.md", "*.fu.md", "*.ics")),
        "harvest": harvest,
        "enrich": enrich,
        "months": months,
        "cpu_schedules": parse_cpu_blocks(read(ROOT / "CPU.md"))["schedules"],
    }


def collect_inflow() -> dict:
    dump_text = read(ROOT / "inflow" / "DUMP.md")
    pending = parse_dump_section(dump_text, "PENDING")
    human_open = parse_dump_section(dump_text, "HUMAN OPEN")
    news = parse_inflow_news(read(ROOT / "inflow" / "inflow.fu.md"))
    takes = _load_inflow_takes()
    files = list_dir_files("inflow", ("*.md", "*.fu.md"))
    # digest: human-open needing attention + pending not dripped
    digest = []
    for d in human_open:
        if (d.get("status") or "").lower() in ("open", "researched", "answered", ""):
            digest.append({**d, "lane": "human-open"})
    for d in pending:
        st = (d.get("status") or "").lower()
        if st != "dripped":
            digest.append({**d, "lane": "pending"})
    by_id: dict[str, dict] = {}
    for d in pending + human_open + news:
        by_id[d["id"]] = d
    return {
        "files": files,
        "pending": pending,
        "human_open": human_open,
        "state": parse_state_header(read(ROOT / "inflow" / "STATE.md")),
        "news": news,
        "digest": digest,
        "takes": takes,
        "by_id": by_id,
    }


def collect_mezzanine() -> dict:
    return {"files": list_dir_files("mezzanine", ("*.toon.md", "*.md"))}


def collect_skills() -> dict:
    lib = list_dir_files("skills", ("*.fu.md", "*.py"))
    cursor = []
    skill_root = ROOT / ".cursor" / "skills"
    if skill_root.exists():
        for d in sorted(skill_root.iterdir()):
            if d.is_dir() and (d / "SKILL.md").exists():
                desc = ""
                try:
                    for ln in (d / "SKILL.md").read_text(encoding="utf-8").splitlines()[:30]:
                        if ln.startswith("description:"):
                            desc = ln.split(":", 1)[1].strip().strip(">").strip()
                            break
                        if ln.strip().startswith("- ") and desc == "" and "description" in (
                            d / "SKILL.md"
                        ).read_text(encoding="utf-8")[:400]:
                            pass
                except Exception:
                    pass
                # better: YAML block description multiline — take first non-empty after description
                try:
                    raw = (d / "SKILL.md").read_text(encoding="utf-8")
                    m = re.search(r"^description:\s*>?-?\s*\n((?:  .*\n)+)", raw, re.M)
                    if m:
                        desc = " ".join(x.strip() for x in m.group(1).splitlines())[:160]
                    else:
                        m = re.search(r"^description:\s*(.+)$", raw, re.M)
                        if m:
                            desc = m.group(1).strip()[:160]
                except Exception:
                    pass
                cursor.append({"name": d.name, "path": f".cursor/skills/{d.name}", "description": desc})
    return {"library": lib, "cursor_skills": cursor}


def collect_tmp() -> dict:
    ttl = parse_toon_kv_prefix(
        read(ROOT / "tmp" / "ttl.toon.md"),
        ["last_run", "lapse_days", "last_expire", "schema"],
    )
    siblings = []
    tmp = ROOT / "tmp"
    if tmp.exists():
        for p in sorted(tmp.iterdir()):
            if p.name == "ttl.toon.md":
                continue
            siblings.append(
                {
                    "name": p.name,
                    "kind": "dir" if p.is_dir() else "file",
                }
            )
    return {"ttl": ttl, "siblings": siblings[:80], "sibling_count": len(siblings)}


def collect_pedagogy_dirs() -> dict:
    base = ROOT / "pedagogy"
    branches = []
    if base.exists():
        for p in sorted(base.iterdir()):
            if not p.is_dir() or p.name.startswith("_") or p.name.startswith("."):
                continue
            n_fu = len(list(p.rglob("*.fu.md")))
            branches.append({"name": p.name, "fu_count": n_fu})
    return {
        "branches": branches,
        "graph": "pedagogy/universe.graph.md",
        "cpu": "pedagogy/pedagogy-cpu.fu.md",
    }


def parse_weights(text: str) -> dict:
    out: dict = {"updated": "", "focus": "", "nodes": [], "by_id": {}}
    for line in text.splitlines():
        if line.startswith("updated:"):
            out["updated"] = line.split(":", 1)[1].strip()
        elif line.startswith("focus:"):
            out["focus"] = line.split(":", 1)[1].strip()
        elif re.match(r"^\s+\S+,\d+", line):
            # id,hire,plan,study,zeit,maslow,maslow_layer,total,mastery,reason
            parts = line.strip().split(",", 9)
            if len(parts) < 9:
                continue
            node = {
                "id": parts[0],
                "hire": int(parts[1] or 0),
                "plan": int(parts[2] or 0),
                "study": int(parts[3] or 0),
                "zeit": int(parts[4] or 0),
                "maslow": int(parts[5] or 0),
                "maslow_layer": parts[6],
                "total": int(parts[7] or 0),
                "mastery": parts[8],
                "reason": parts[9] if len(parts) > 9 else "",
            }
            out["nodes"].append(node)
            out["by_id"][node["id"]] = node
    return out


def collect_recycle() -> dict:
    base = ROOT / "recycle"
    n = 0
    journal = ""
    if base.exists():
        for p in base.rglob("*"):
            if p.is_file():
                n += 1
        jp = base / "JOURNAL.md"
        if jp.exists():
            journal = read(jp).splitlines()[0][:160] if read(jp) else ""
    return {"file_count": n, "journal_head": journal}


def collect_state() -> dict:
    verts, edges = parse_graph(ROOT / "pedagogy" / "universe.graph.md")
    pedagogy_cpu = read(ROOT / "pedagogy" / "pedagogy-cpu.fu.md")
    goals = parse_goals(read(ROOT / "self" / "goals.toon.md"))
    plans = parse_plans(pedagogy_cpu)
    studies = parse_studies(pedagogy_cpu)
    organs = parse_root_organs(read(ROOT / "ROOT.md"))
    cpu = parse_cpu_blocks(read(ROOT / "CPU.md"))
    self_pack = collect_self()
    schedule = collect_schedule()
    cron = collect_cron()
    inflow = collect_inflow()
    mezz = collect_mezzanine()
    skills = collect_skills()
    tmp = collect_tmp()
    ped_dirs = collect_pedagogy_dirs()
    recycle = collect_recycle()
    weights = parse_weights(read(ROOT / "pedagogy" / "_learn" / "weights.toon.md"))
    language = collect_language()
    north = set(goals.get("north") or [])
    study_ids = {s["id"] for s in studies}
    for v in verts:
        v["branch"] = vertex_branch(v)
    kind_counts: dict[str, int] = defaultdict(int)
    branch_counts: dict[str, int] = defaultdict(int)
    for v in verts:
        kind_counts[v.get("kind", "?")] += 1
        branch_counts[v["branch"]] += 1
    today = build_today(
        cpu=cpu,
        schedule=schedule,
        plans=plans,
        studies=studies,
        goals=goals,
        self_pack=self_pack,
        inflow=inflow,
        weights=weights,
    )
    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "repo": str(ROOT),
        "organs": organs,
        "goals": goals,
        "plans": plans,
        "studies": studies,
        "agents": cpu["agents"],
        "cpu": cpu,
        "dumps": inflow["pending"],
        "inflow_state": inflow["state"],
        "self": self_pack,
        "schedule": schedule,
        "cron": cron,
        "inflow": inflow,
        "mezzanine": mezz,
        "skills": skills,
        "tmp": tmp,
        "pedagogy_dirs": ped_dirs,
        "recycle": recycle,
        "weights": weights,
        "language": language,
        "today": today,
        "graph": {
            "verts": verts,
            "edges": edges,
            "v_count": len(verts),
            "e_count": len(edges),
            "kind_counts": dict(kind_counts),
            "branch_counts": dict(branch_counts),
            "north": sorted(north),
            "study_ids": sorted(study_ids),
            "stack_ids": sorted(v["id"] for v in verts if is_stack(v)),
            "core_ids": sorted(v["id"] for v in verts if not is_stack(v)),
        },
    }


def write_html(state: dict, path: Path, default_purpose: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(state, ensure_ascii=False)
    purposes = json.dumps(
        [
            {"id": "today", "label": "Today", "hint": "综合今天干什么 · all organs"},
            {"id": "train", "label": "Train / Injury", "hint": "肌肉 · 计划 · 伤病 flags"},
            {"id": "routine", "label": "Routine", "hint": "刷牙洗脸 · 洗牙体检 · tips"},
            {"id": "project", "label": "Project", "hint": "ROOT map · all organs"},
            {"id": "self", "label": "Self", "hint": "goals · endurance · train · learn"},
            {"id": "schedule", "label": "Schedule", "hint": "table · calendar · gantt"},
            {"id": "cron", "label": "Cron", "hint": "gatherer jobs ≠ life queue"},
            {"id": "inflow", "label": "Inflow", "hint": "可读消化 · 点开详情 · 写意见"},
            {"id": "runtime", "label": "CPU runtime", "hint": "AGENT · TODO · SCHEDULE"},
            {"id": "study", "label": "Study", "hint": "pedagogy-cpu PROBE surface"},
            {"id": "weights", "label": "Weights", "hint": "hire·plan·study·zeit·maslow + mastery"},
            {"id": "hire", "label": "Hire north", "hint": "goals.north + 1-hop graph"},
            {"id": "ontology", "label": "Ontology", "hint": "branch/kind clusters · size=weight · glow=mastery"},
            {"id": "core", "label": "Core graph", "hint": "non-stack · same grouping tools"},
            {"id": "stack", "label": "Stack graph", "hint": "stack tools · same grouping tools"},
            {"id": "lang-polyglot", "label": "Polyglot KG", "hint": "可读词面 · 意思/词/句法 · 检查结构"},
            {"id": "lang-wortschatz", "label": "Wortschatz", "hint": "词 / 词形 / 搭配 · 可读词面"},
            {"id": "lang-grammar", "label": "Grammatik", "hint": "句法框 · 槽 · 填充词"},
            {"id": "lang-skilltree", "label": "Skill tree", "hint": "Horizon → 等级 → 16 种语言"},
            {"id": "skills", "label": "Skills", "hint": "skills/ + .cursor/skills"},
            {"id": "mezzanine", "label": "Mezzanine", "hint": "ingest notes · not ontology"},
            {"id": "tmp", "label": "Tmp", "hint": "TTL deliverables"},
        ]
    )
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>project-state · mindcraft</title>
  <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
  <style>
    :root {{
      --bg: #0a0e14; --panel: #121a24; --line: #2a3544; --text: #e8eef5;
      --muted: #8b9bb4; --acc: #69f0ae; --warn: #ffcc80; --bad: #ef5350;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; height: 100%; background: var(--bg); color: var(--muted); font: 14px/1.45 ui-sans-serif, system-ui, sans-serif; }}
    #app {{ display: grid; grid-template-columns: 250px 1fr; height: 100%; }}
    aside {{ border-right: 1px solid var(--line); padding: 14px 12px; overflow: auto; background: #0d141c; }}
    aside h1 {{ margin: 0 0 4px; color: var(--acc); font-size: 15px; }}
    aside .meta {{ font-size: 11px; margin-bottom: 10px; }}
    aside .group {{ font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em; color: #5c6b82; margin: 12px 0 6px; }}
    .purpose {{ display: block; width: 100%; text-align: left; margin: 0 0 6px; padding: 8px 10px; border: 1px solid var(--line); background: var(--panel); color: var(--text); border-radius: 8px; cursor: pointer; }}
    .purpose:hover {{ border-color: var(--acc); }}
    .purpose.active {{ border-color: var(--acc); box-shadow: inset 0 0 0 1px var(--acc); }}
    .purpose strong {{ display: block; font-size: 12px; }}
    .purpose span {{ display: block; color: var(--muted); font-size: 10px; margin-top: 2px; }}
    main {{ display: grid; grid-template-rows: auto 1fr; min-width: 0; }}
    #bar {{ padding: 12px 18px; border-bottom: 1px solid var(--line); display: flex; gap: 16px; flex-wrap: wrap; align-items: baseline; }}
    #bar strong {{ color: var(--acc); }}
    #view {{ position: relative; min-height: 0; }}
    #net {{ position: absolute; inset: 0; }}
    #panel {{ position: absolute; inset: 0; overflow: auto; padding: 18px; display: none; }}
    #panel.show {{ display: block; }}
    #net.hide {{ display: none; }}
    #graph-tools {{
      position: absolute; left: 12px; top: 12px; z-index: 6; max-width: min(320px, 46vw);
      background: rgba(13,20,28,.92); border: 1px solid var(--line); border-radius: 10px;
      padding: 10px 12px; backdrop-filter: blur(6px); box-shadow: 0 8px 24px rgba(0,0,0,.35);
    }}
    #graph-tools.hide {{ display: none; }}
    #graph-tools .gt-row {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 8px; align-items: center; }}
    #graph-tools .gt-label {{ font-size: 10px; text-transform: uppercase; letter-spacing: .06em; color: #5c6b82; width: 100%; margin-bottom: 2px; }}
    #graph-tools button {{
      background: var(--panel); border: 1px solid var(--line); color: var(--text);
      padding: 4px 9px; border-radius: 6px; cursor: pointer; font-size: 11px;
    }}
    #graph-tools button.on {{ border-color: var(--acc); color: var(--acc); }}
    #graph-tools .chip {{
      font-size: 10px; border: 1px solid var(--line); border-radius: 999px; padding: 2px 8px;
      cursor: pointer; color: var(--muted); background: transparent;
    }}
    #graph-tools .chip.on {{ color: var(--text); border-color: var(--acc); background: #122018; }}
    #graph-tools .chip.off {{ opacity: 0.35; }}
    #graph-tools .gt-hint {{ font-size: 10px; color: var(--muted); margin: 4px 0 0; line-height: 1.35; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px; }}
    .card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; }}
    .card.click {{ cursor: pointer; }}
    .card.click:hover {{ border-color: var(--acc); }}
    .card h3 {{ margin: 0 0 6px; color: var(--text); font-size: 13px; }}
    .card .tag {{ display: inline-block; font-size: 10px; color: var(--acc); border: 1px solid #2d4a3a; padding: 1px 6px; border-radius: 999px; margin-bottom: 6px; }}
    .card p {{ margin: 0; font-size: 12px; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 8px; }}
    th, td {{ text-align: left; padding: 7px 8px; border-bottom: 1px solid var(--line); font-size: 12px; vertical-align: top; }}
    th {{ color: var(--acc); font-weight: 600; }}
    .ok {{ color: var(--acc); }} .wait {{ color: var(--warn); }} .bad {{ color: var(--bad); }}
    .section {{ margin-bottom: 22px; }}
    .section h2 {{ margin: 0 0 10px; color: var(--text); font-size: 16px; }}
    #detail {{ position: absolute; right: 14px; bottom: 14px; max-width: 320px; background: #0d141c; border: 1px solid var(--line); border-radius: 10px; padding: 10px 12px; display: none; z-index: 5; }}
    #detail.show {{ display: none; }}
    #drawer {{
      position: absolute; top: 0; right: 0; width: min(520px, 100%); height: 100%;
      background: #0d141c; border-left: 1px solid var(--line); z-index: 20;
      transform: translateX(105%); transition: transform .2s ease; display: flex; flex-direction: column;
    }}
    #drawer.open {{ transform: translateX(0); }}
    #drawer-backdrop {{
      position: absolute; inset: 0; background: rgba(0,0,0,.45); z-index: 15; display: none;
    }}
    #drawer-backdrop.show {{ display: block; }}
    #drawer-head {{ display: flex; justify-content: space-between; gap: 12px; padding: 14px 16px; border-bottom: 1px solid var(--line); }}
    #drawer-head h2 {{ margin: 0; color: var(--acc); font-size: 16px; overflow-wrap: anywhere; }}
    #drawer-head p {{ margin: 4px 0 0; font-size: 12px; color: var(--muted); }}
    #drawer-close {{ background: transparent; border: 1px solid var(--line); color: var(--text); border-radius: 6px; cursor: pointer; padding: 4px 10px; }}
    #drawer-meta {{ padding: 10px 16px; font-size: 12px; border-bottom: 1px solid var(--line); color: var(--muted); }}
    #drawer-body {{ flex: 1; overflow: auto; padding: 12px 16px; }}
    #drawer-learn {{ border-top: 1px solid var(--line); padding: 12px 16px; background: #0a1018; }}
    #drawer-learn h3 {{ margin: 0 0 8px; color: var(--text); font-size: 13px; }}
    #drawer-learn textarea, #drawer-learn select {{
      width: 100%; background: var(--panel); color: var(--text); border: 1px solid var(--line);
      border-radius: 6px; padding: 8px; margin: 6px 0 10px; font: inherit;
    }}
    #learn-status {{ font-size: 11px; color: var(--acc); }}
    __FU_CSS__
    .action {{ display: grid; grid-template-columns: 56px 88px 1fr; gap: 10px; align-items: start; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 12px 14px; margin-bottom: 8px; }}
    .action .pri {{ font-size: 11px; color: var(--acc); }}
    .action .kind {{ font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; }}
    .action .kind.routine {{ color: #a5d6a7; }}
    .action .kind.injury {{ color: var(--bad); }}
    .action .kind.train {{ color: #80deea; }}
    .action .kind.stop {{ color: var(--bad); }}
    .action .kind.body, .action .kind.calendar {{ color: var(--acc); }}
    .action .kind.learn {{ color: #82b1ff; }}
    .action .kind.rest, .action .kind.drill {{ color: var(--warn); }}
    .action .txt {{ color: var(--text); font-size: 13px; }}
    .action .src {{ display: block; color: var(--muted); font-size: 10px; margin-top: 4px; }}
    .today-hero {{ background: linear-gradient(135deg, #121a24, #0d1f18); border: 1px solid #2d4a3a; border-radius: 12px; padding: 16px 18px; margin-bottom: 18px; }}
    .today-hero h2 {{ margin: 0 0 6px; color: var(--acc); font-size: 18px; }}
    .today-hero p {{ margin: 4px 0; font-size: 13px; color: var(--text); }}
    .pillrow {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }}
    .pill {{ font-size: 11px; border: 1px solid var(--line); border-radius: 999px; padding: 3px 10px; color: var(--muted); }}
    .pill.bad {{ border-color: #5a3030; color: var(--bad); }}
    .pill.warn {{ border-color: #5a4a30; color: var(--warn); }}
    .pill.ok {{ border-color: #2d4a3a; color: var(--acc); }}
    .cal {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; }}
    .cal .hd {{ font-size: 10px; color: var(--acc); text-align: center; padding: 4px; }}
    .cal .day {{ min-height: 72px; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 4px; font-size: 10px; }}
    .cal .day .n {{ color: var(--muted); margin-bottom: 2px; }}
    .cal .day .ev {{ display: block; margin: 2px 0; padding: 2px 4px; border-radius: 3px; background: #1a2a22; color: var(--text); overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }}
    .cal .day .ev.cand {{ background: #2a2418; color: var(--warn); }}
    .cal .day.mute {{ opacity: 0.35; }}
    .viewbar {{ display: flex; gap: 8px; margin-bottom: 14px; flex-wrap: wrap; }}
    .viewbar button {{ background: var(--panel); border: 1px solid var(--line); color: var(--text); padding: 6px 12px; border-radius: 6px; cursor: pointer; }}
    .viewbar button.on {{ border-color: var(--acc); color: var(--acc); }}
    .gantt {{ position: relative; overflow-x: auto; }}
    .gantt .row {{ display: grid; grid-template-columns: 180px 1fr; gap: 8px; align-items: center; margin-bottom: 6px; }}
    .gantt .label {{ font-size: 11px; color: var(--text); }}
    .gantt .track {{ position: relative; height: 22px; background: #0d141c; border: 1px solid var(--line); border-radius: 4px; }}
    .gantt .bar {{ position: absolute; top: 2px; bottom: 2px; border-radius: 3px; font-size: 9px; padding: 0 4px; color: #0a0e14; overflow: hidden; white-space: nowrap; }}
    .gantt .bar.ok {{ background: var(--acc); }}
    .gantt .bar.cand {{ background: var(--warn); }}
    .legend {{ font-size: 11px; margin-bottom: 10px; }}
    code {{ color: var(--acc); }}
    .in-card {{ cursor: pointer; transition: border-color .12s; }}
    .in-card:hover {{ border-color: var(--acc); }}
    .in-card .why {{ margin-top: 8px; font-size: 13px; color: var(--text); line-height: 1.45; }}
    .in-card .meta {{ margin-top: 8px; font-size: 11px; color: var(--muted); }}
    .in-card .take-badge {{ color: var(--acc); }}
    .in-body h4 {{ margin: 14px 0 6px; color: var(--acc); font-size: 12px; text-transform: uppercase; letter-spacing: .04em; }}
    .in-body p {{ margin: 0 0 8px; font-size: 13px; line-height: 1.5; }}
    .in-body a {{ color: var(--acc); }}
  </style>
</head>
<body>
  <div id="app">
    <aside>
      <h1>project-state</h1>
      <div class="meta" id="stamp"></div>
      <div id="purposes"></div>
    </aside>
    <main>
      <div id="bar"><strong id="title">…</strong><span id="hint"></span><span id="stats"></span></div>
      <div id="view"><div id="graph-tools" class="hide"></div><div id="net"></div><div id="panel"></div><div id="detail"></div>
        <aside id="drawer" aria-hidden="true">
          <header id="drawer-head">
            <div>
              <h2 id="drawer-title">…</h2>
              <p id="drawer-sub"></p>
            </div>
            <button type="button" id="drawer-close">✕</button>
          </header>
          <div id="drawer-meta"></div>
          <div id="drawer-body" class="fu-scroll">Loading…</div>
          <section id="drawer-learn">
            <h3>Learner</h3>
            <p class="legend">Notes write to <code>pedagogy/_learn/learner-notes.toon.md</code>. tmp cache. Does not invent STUDY ANSWER. Needs <code>--serve</code>.</p>
            <label>grasp / stance
              <select id="learn-grasp">
                <option value="unknown">unknown / 未定</option>
                <option value="weak">weak / 略看</option>
                <option value="partial">partial / 有用</option>
                <option value="firm">firm / 要行动</option>
              </select>
            </label>
            <textarea id="learn-note" rows="4" placeholder="RECALL / 你的意见…"></textarea>
            <div class="viewbar">
              <button type="button" id="learn-save">Save note</button>
              <span id="learn-status"></span>
            </div>
          </section>
        </aside>
        <div id="drawer-backdrop"></div>
      </div>
    </main>
  </div>
  <script>
    const STATE = {payload};
    const PURPOSES = {purposes};
    const GROUPS = [
      {{ title: 'now', ids: ['today', 'train', 'routine'] }},
      {{ title: 'map', ids: ['project'] }},
      {{ title: 'life', ids: ['self', 'schedule', 'runtime'] }},
      {{ title: 'ingest', ids: ['inflow', 'cron', 'mezzanine'] }},
      {{ title: 'know', ids: ['study', 'weights', 'hire', 'ontology', 'core', 'stack'] }},
      {{ title: 'language', ids: ['lang-polyglot', 'lang-wortschatz', 'lang-grammar', 'lang-skilltree'] }},
      {{ title: 'kits', ids: ['skills', 'tmp'] }},
    ];
    const KIND_FILL = {json.dumps(KIND_FILL)};
    const KIND_EDGE = {json.dumps(KIND_EDGE)};
    const BRANCH_FILL = {json.dumps(BRANCH_FILL)};
    const BRANCH_EDGE = {json.dumps(BRANCH_EDGE)};
    const LABEL_COLOR = {json.dumps(LABEL_COLOR)};
    const KIND_READ = {json.dumps(KIND_READ)};
    const LANG_EDGE = {{
      FROM_SESSION: '',
      EXPRESSES: '表达',
      NEEDS_FRAME: '句法',
      GAP_IN: '缺口',
      HAS_FORM: '词形',
      HAS_SLOT: '槽',
      FILLED_BY: '填',
      FIXES: '改',
      IN_BAND: '在',
      TARGETS: '目标',
      COLLOCATES: '搭配',
      IN_SENTENCE: '句中',
      APPLIES: '用',
      USES: '用'
    }};
    let purpose = {json.dumps(default_purpose)};
    let net = null;
    const GRAPH_UI = {{
      groupBy: 'branch',   // branch | kind | none
      clustered: true,
      filters: null        // null = all keys; Set of active keys when filtering
    }};

    document.getElementById('stamp').textContent =
      STATE.generated_at + ' · V' + STATE.graph.v_count + ' E' + STATE.graph.e_count;

    const box = document.getElementById('purposes');
    GROUPS.forEach(g => {{
      const h = document.createElement('div');
      h.className = 'group';
      h.textContent = g.title;
      box.appendChild(h);
      g.ids.forEach(id => {{
        const p = PURPOSES.find(x => x.id === id);
        if (!p) return;
        const b = document.createElement('button');
        b.className = 'purpose' + (p.id === purpose ? ' active' : '');
        b.dataset.id = p.id;
        b.innerHTML = '<strong>' + p.label + '</strong><span>' + p.hint + '</span>';
        b.onclick = () => setPurpose(p.id);
        box.appendChild(b);
      }});
    }});

    function setPurpose(id) {{
      purpose = id;
      box.querySelectorAll('.purpose').forEach(el => el.classList.toggle('active', el.dataset.id === id));
      if (String(id).startsWith('lang-')) {{
        GRAPH_UI.groupBy = 'kind';
        GRAPH_UI.clustered = false;
        GRAPH_UI.filters = (id === 'lang-polyglot' || id === 'lang-wortschatz')
          ? 'structure' : null;
      }}
      render();
    }}

    function hop1(seed) {{
      const keep = new Set(seed);
      const g = graphBundle();
      g.edges.forEach(e => {{
        if (seed.has(e.src) || seed.has(e.dst)) {{ keep.add(e.src); keep.add(e.dst); }}
      }});
      return keep;
    }}

    function graphBundle() {{
      const L = STATE.language || {{}};
      if (purpose === 'lang-polyglot') return L.polyglot || {{ verts: [], edges: [] }};
      if (purpose === 'lang-wortschatz') return L.wortschatz || {{ verts: [], edges: [] }};
      if (purpose === 'lang-grammar') return L.grammar || {{ verts: [], edges: [] }};
      if (purpose === 'lang-skilltree') return L.skilltree || {{ verts: [], edges: [] }};
      return STATE.graph;
    }}

    function filterGraph() {{
      const g = graphBundle();
      let ids;
      if (purpose === 'hire') ids = hop1(new Set(g.north || []));
      else if (purpose === 'study') ids = hop1(new Set(g.study_ids || []));
      else if (purpose === 'core') ids = new Set(g.core_ids || []);
      else if (purpose === 'stack') ids = new Set(g.stack_ids || []);
      else ids = new Set((g.verts || []).map(v => v.id));
      return {{
        verts: (g.verts || []).filter(v => ids.has(v.id)),
        edges: (g.edges || []).filter(e => ids.has(e.src) && ids.has(e.dst))
      }};
    }}

    function groupKeyOf(v) {{
      if (GRAPH_UI.groupBy === 'kind') return v.kind || '?';
      if (GRAPH_UI.groupBy === 'branch') return v.branch || 'other';
      return null;
    }}
    function groupFill(key) {{
      if (GRAPH_UI.groupBy === 'kind') return KIND_FILL[key] || '#121a24';
      return BRANCH_FILL[key] || '#212121';
    }}
    function groupEdge(key) {{
      if (GRAPH_UI.groupBy === 'kind') return KIND_EDGE[key] || '#69f0ae';
      return BRANCH_EDGE[key] || '#757575';
    }}
    function hideGraphTools() {{
      const el = document.getElementById('graph-tools');
      if (el) el.classList.add('hide');
    }}
    function paintGraphTools(visibleVerts) {{
      const el = document.getElementById('graph-tools');
      if (!el) return;
      el.classList.remove('hide');
      const counts = {{}};
      visibleVerts.forEach(v => {{
        const k = groupKeyOf(v);
        if (!k) return;
        counts[k] = (counts[k] || 0) + 1;
      }});
      const keys = Object.keys(counts).sort();
      const filters = GRAPH_UI.filters;
      let html = '<div class="gt-row"><span class="gt-label">Group by</span>';
      [['branch','Branch'],['kind','Kind'],['none','Flat']].forEach(([id, lab]) => {{
        html += '<button type="button" data-act="groupby" data-v="' + id + '"' +
          (GRAPH_UI.groupBy === id ? ' class="on"' : '') + '>' + lab + '</button>';
      }});
      html += '</div><div class="gt-row"><span class="gt-label">Clusters</span>';
      html += '<button type="button" data-act="cluster" data-v="on"' +
        (GRAPH_UI.clustered ? ' class="on"' : '') + '>Collapsed</button>';
      html += '<button type="button" data-act="cluster" data-v="off"' +
        (!GRAPH_UI.clustered ? ' class="on"' : '') + '>Expanded</button>';
      html += '</div>';
      if (GRAPH_UI.groupBy !== 'none' && keys.length) {{
        html += '<div class="gt-row"><span class="gt-label">Filter · click to toggle</span>';
        keys.forEach(k => {{
          const on = !filters || filters.has(k);
          html += '<button type="button" class="chip ' + (on ? 'on' : 'off') +
            '" data-act="filter" data-v="' + esc(k) + '" style="border-color:' +
            groupEdge(k) + '">' + esc(KIND_READ[k] || k) + ' · ' + counts[k] + '</button>';
        }});
        html += '<button type="button" data-act="filter-all">All</button>';
        html += '</div>';
      }}
      html += '<p class="gt-hint">' +
        (String(purpose).startsWith('lang-')
          ? '节点是词面/意思，不是机器 ID。默认展开；会话星形先关掉，点「会话」可打开。'
          : ('双击簇圆展开；Collapsed 时按 ' +
            (GRAPH_UI.groupBy === 'none' ? 'flat' : GRAPH_UI.groupBy) + ' 圈定。')) +
        '</p>';
      el.innerHTML = html;
      el.querySelectorAll('[data-act]').forEach(btn => {{
        btn.onclick = () => {{
          const act = btn.getAttribute('data-act');
          const v = btn.getAttribute('data-v');
          if (act === 'groupby') {{
            GRAPH_UI.groupBy = v;
            GRAPH_UI.filters = null;
            if (v === 'none') GRAPH_UI.clustered = false;
            else if (!GRAPH_UI.clustered && visibleVerts.length > 36) GRAPH_UI.clustered = true;
          }} else if (act === 'cluster') {{
            GRAPH_UI.clustered = (v === 'on');
          }} else if (act === 'filter-all') {{
            GRAPH_UI.filters = null;
          }} else if (act === 'filter') {{
            const all = new Set(keys);
            let next = GRAPH_UI.filters ? new Set(GRAPH_UI.filters) : new Set(all);
            if (next.has(v)) next.delete(v); else next.add(v);
            if (!next.size || next.size === all.size) GRAPH_UI.filters = null;
            else GRAPH_UI.filters = next;
          }}
          renderGraph({{ keepPanel: purpose === 'study' }});
        }};
      }});
    }}

    function weightOf(id) {{
      const w = (STATE.weights && STATE.weights.by_id) ? STATE.weights.by_id[id] : null;
      return w || null;
    }}
    function masteryRank(m) {{
      return ({{ unknown: 0, weak: 1, partial: 2, firm: 3 }})[m || 'unknown'] || 0;
    }}
    function nodeColor(v) {{
      const kind = v.kind || 'praxis';
      const north = new Set(STATE.graph.north);
      const nowIds = new Set(STATE.plans.map(p => p.now).filter(Boolean));
      const w = weightOf(v.id);
      let border = KIND_EDGE[kind] || '#69f0ae';
      if (nowIds.has(v.id)) border = '#ef5350';
      else if (north.has(v.id)) border = '#ffcc80';
      const mr = masteryRank(w && w.mastery);
      const borderWidth = 1 + mr;
      // soft branch tint on fill when grouping by branch
      let background = KIND_FILL[kind] || '#121a24';
      if (GRAPH_UI.groupBy === 'branch' && v.branch && BRANCH_FILL[v.branch]) {{
        background = BRANCH_FILL[v.branch];
      }}
      return {{ background, border, borderWidth }};
    }}

    function renderGraph(opts) {{
      opts = opts || {{}};
      let {{ verts, edges }} = filterGraph();
      document.getElementById('net').classList.remove('hide');
      if (!opts.keepPanel) document.getElementById('panel').classList.remove('show');

      // default: cluster large ontology-ish graphs
      if (opts.resetDefaults) {{
        GRAPH_UI.groupBy = 'branch';
        GRAPH_UI.clustered = verts.length > 28;
        GRAPH_UI.filters = null;
      }}

      if (GRAPH_UI.filters === 'structure') {{
        const kinds = new Set(verts.map(v => v.kind).filter(Boolean));
        GRAPH_UI.filters = new Set([...kinds].filter(k => k !== 'session' && k !== 'focus'));
      }}

      if (GRAPH_UI.groupBy !== 'none' && GRAPH_UI.filters && GRAPH_UI.filters.size) {{
        verts = verts.filter(v => GRAPH_UI.filters.has(groupKeyOf(v)));
        const keep = new Set(verts.map(v => v.id));
        edges = edges.filter(e => keep.has(e.src) && keep.has(e.dst));
      }}

      paintGraphTools(filterGraph().verts);

      const maxW = Math.max(1, ...verts.map(v => (weightOf(v.id) || {{}}).total || 0));
      const nodes = verts.map(v => {{
        const w = weightOf(v.id);
        const total = w ? w.total : 0;
        const fontSize = 11 + Math.round(10 * (total / maxW));
        const langMode = String(purpose).startsWith('lang-');
        let lab = v.label || v.id;
        if (langMode) {{
          lab = v.label || v.surfaceRead || v.glossRead || v.id;
          if (lab.length > 36) lab = lab.slice(0, 34) + '…';
        }} else if (w && w.total) {{
          lab = v.id + '\\n★' + w.total;
        }}
        const titleBits = langMode
          ? [lab, (v.kindRead || v.kind || ''), v.glossRead || '', v.fixesRead ? ('改自 ' + v.fixesRead) : ''].filter(Boolean)
          : [(v.gloss || '').replace(/-/g, ' '), 'branch ' + (v.branch || '?'), 'kind ' + (v.kind || '?')];
        if (w && !langMode) titleBits.push('weight ' + w.total + ' · mastery ' + w.mastery, w.reason);
        const c = nodeColor(v);
        return {{
          id: v.id,
          label: lab,
          title: titleBits.join('\\n'),
          shape: 'box',
          color: c,
          font: {{ color: '#e8eef5', size: langMode ? 13 : fontSize }},
          borderWidth: c.borderWidth || 1,
          value: 1 + total,
          branch: v.branch || 'other',
          kind: v.kind || '?',
          group: groupKeyOf(v) || undefined
        }};
      }});
      const visEdges = edges.map(e => {{
        const langMode = String(purpose).startsWith('lang-');
        const elab = langMode
          ? (LANG_EDGE.hasOwnProperty(e.label) ? LANG_EDGE[e.label] : e.label)
          : e.label;
        return {{
          from: e.src, to: e.dst, label: elab, arrows: 'to',
          color: {{ color: LABEL_COLOR[e.label] || '#69f0ae' }},
          font: {{ color: LABEL_COLOR[e.label] || '#69f0ae', size: 9, strokeWidth: 0 }}
        }};
      }});
      if (net) net.destroy();
      net = new vis.Network(document.getElementById('net'), {{
        nodes: new vis.DataSet(nodes), edges: new vis.DataSet(visEdges)
      }}, {{
        physics: {{
          enabled: true, solver: 'forceAtlas2Based',
          forceAtlas2Based: {{ gravitationalConstant: -70, springLength: 95, avoidOverlap: 1 }},
          stabilization: {{ iterations: Math.min(320, 80 + nodes.length) }}
        }},
        interaction: {{ hover: true, navigationButtons: true, keyboard: true }},
        nodes: {{ margin: 8, widthConstraint: {{ maximum: String(purpose).startsWith('lang-') ? 240 : 170 }}, scaling: {{ min: 10, max: 40 }} }},
        edges: {{ smooth: {{ type: 'cubicBezier', forceDirection: 'vertical', roundness: 0.4 }} }}
      }});

      if (GRAPH_UI.clustered && GRAPH_UI.groupBy !== 'none') {{
        const keys = [...new Set(verts.map(v => groupKeyOf(v)).filter(Boolean))];
        keys.forEach(key => {{
          const n = verts.filter(v => groupKeyOf(v) === key).length;
          if (n < 2) return;
          const cid = 'cluster:' + GRAPH_UI.groupBy + ':' + key;
          net.cluster({{
            joinCondition: function(nodeOptions) {{
              return (GRAPH_UI.groupBy === 'kind' ? nodeOptions.kind : nodeOptions.branch) === key;
            }},
            allowSingleNodeCluster: false,
            processProperties: function(clusterOptions, childNodes) {{
              clusterOptions.id = cid;
              clusterOptions.label = (KIND_READ[key] || key) + '\\n(' + childNodes.length + ')';
              clusterOptions.title = GRAPH_UI.groupBy + ' · ' + key + ' · ' + childNodes.length + ' nodes\\n双击展开';
              clusterOptions.shape = 'ellipse';
              clusterOptions.color = {{
                background: groupFill(key),
                border: groupEdge(key),
                highlight: {{ background: groupFill(key), border: '#e8eef5' }}
              }};
              clusterOptions.font = {{ color: '#e8eef5', size: 15, face: 'ui-sans-serif' }};
              clusterOptions.borderWidth = 3;
              clusterOptions.margin = 18;
              clusterOptions.value = 8 + childNodes.length;
              return clusterOptions;
            }},
            clusterEdgeProperties: {{
              dashes: [4, 4],
              color: {{ color: '#5c6b82', opacity: 0.55 }},
              font: {{ size: 0 }}
            }}
          }});
        }});
      }}

      net.once('stabilized', () => net.setOptions({{ physics: false }}));
      net.on('click', params => {{
        if (!params.nodes.length) return;
        const id = params.nodes[0];
        if (net.isCluster(id)) return; // 单击簇：不打开 drawer；双击展开
        openVertex(id);
      }});
      net.on('doubleClick', params => {{
        if (!params.nodes.length) return;
        const id = params.nodes[0];
        if (net.isCluster(id)) {{
          net.openCluster(id);
          net.setOptions({{ physics: {{ enabled: true }} }});
          setTimeout(() => {{
            try {{ net.setOptions({{ physics: false }}); }} catch (e) {{}}
          }}, 900);
        }}
      }});
      document.getElementById('stats').textContent = 'nodes ' + nodes.length + ' · edges ' + visEdges.length +
        (GRAPH_UI.clustered && GRAPH_UI.groupBy !== 'none' ? ' · clustered by ' + GRAPH_UI.groupBy : '') +
        (String(purpose).startsWith('lang-')
          ? ' · lang store ' + purpose.replace('lang-', '')
          : ' · weights ' + ((STATE.weights && STATE.weights.nodes) || []).length);
    }}

    let currentVertex = null;
    let drawerMode = 'vertex'; // vertex | inflow | file
    let currentInflowId = null;
    let drawerSeq = 0;
    function resetLearnFields(grasp, note) {{
      const ta = document.getElementById('learn-note');
      const sel = document.getElementById('learn-grasp');
      if (ta && ta.parentNode) {{
        const fresh = ta.cloneNode(false);
        fresh.id = 'learn-note';
        fresh.rows = ta.rows;
        fresh.placeholder = ta.placeholder;
        fresh.value = note || '';
        fresh.setAttribute('data-seq', String(drawerSeq));
        ta.parentNode.replaceChild(fresh, ta);
      }} else if (ta) {{
        ta.value = note || '';
      }}
      if (sel) sel.value = grasp || 'unknown';
      const st = document.getElementById('learn-status');
      if (st) st.textContent = '';
    }}
    function applyLearnIfCurrent(seq, grasp, note) {{
      if (seq !== drawerSeq) return false;
      resetLearnFields(grasp, note);
      return true;
    }}
    function closeDrawer() {{
      document.getElementById('drawer').classList.remove('open');
      document.getElementById('drawer-backdrop').classList.remove('show');
      document.getElementById('drawer').setAttribute('aria-hidden', 'true');
    }}
    function setDrawerLearnLabel(mode) {{
      const h = document.querySelector('#drawer-learn h3');
      const legend = document.querySelector('#drawer-learn .legend');
      if (mode === 'inflow') {{
        if (h) h.textContent = 'Your take';
        if (legend) legend.innerHTML = '意见写入 <code>inflow/takes.toon.md</code>（lasting）。tmp 是缓存，janitor 可删。不发明 drip / ANSWER。需要 <code>--serve</code>。';
      }} else if (mode === 'file') {{
        if (h) h.textContent = 'File note';
        if (legend) legend.innerHTML = 'Optional note keyed by filename. Needs <code>--serve</code>.';
      }} else {{
        if (h) h.textContent = 'Learner';
        if (legend) legend.innerHTML = 'Notes write to <code>pedagogy/_learn/learner-notes.toon.md</code> (lasting). tmp is cache. Does not invent STUDY ANSWER. Needs <code>--serve</code>.';
      }}
    }}
    function inflowItemHtml(it) {{
      if (!it) return '<p class="bad">Item not found</p>';
      let html = '<div class="in-body">';
      html += '<p><span class="pill ' +
        ((it.status==='pending'||it.status==='open')?'warn':(it.status==='dripped'?'ok':'')) +
        '">' + esc(it.status || it.bucket || '') + '</span> ' +
        (it.kind ? '<span class="pill">' + esc(it.kind) + '</span> ' : '') +
        (it.learn ? '<span class="pill">LEARN ' + esc(it.learn) + '</span>' : '') + '</p>';
      if (it.when) html += '<h4>When</h4><p>' + esc(it.when) + '</p>';
      if (it.why) html += '<h4>Why it matters</h4><p>' + esc(it.why) + '</p>';
      if (it.note) html += '<h4>Note</h4><p>' + esc(it.note) + '</p>';
      if (it.drip) html += '<h4>Drip</h4><p>' + esc(it.drip) + '</p>';
      const urls = it.urls && it.urls.length ? it.urls : (it.url ? [it.url] : []);
      if (urls.length) {{
        html += '<h4>Links</h4>';
        urls.forEach(u => {{
          html += '<p><a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u) + '</a></p>';
        }});
      }}
      if ((it.sources||[]).length) {{
        html += '<h4>Sources</h4>';
        it.sources.forEach(s => {{ html += '<p><code>' + esc(s) + '</code></p>'; }});
      }}
      html += '<p class="legend"><code>' + esc(it.id) + '</code> · bucket ' + esc(it.bucket||'') + '</p>';
      html += '</div>';
      return html;
    }}
    async function openInflowItem(id) {{
      const seq = ++drawerSeq;
      drawerMode = 'inflow';
      currentInflowId = id;
      currentVertex = null;
      setDrawerLearnLabel('inflow');
      const it = (STATE.inflow.by_id && STATE.inflow.by_id[id]) ||
        (STATE.inflow.pending||[]).concat(STATE.inflow.human_open||[]).concat(STATE.inflow.news||[]).find(x => x.id === id);
      document.getElementById('drawer-title').textContent = (it && it.title) || id;
      document.getElementById('drawer-sub').textContent = 'inflow · ' + ((it && it.bucket) || 'capture');
      document.getElementById('drawer-meta').innerHTML =
        '<code>' + esc(id) + '</code>' +
        (it && it.status ? ' · <span class="pill">' + esc(it.status) + '</span>' : '');
      document.getElementById('drawer-body').innerHTML = inflowItemHtml(it);
      const take = (STATE.inflow.takes && STATE.inflow.takes[id]) || null;
      resetLearnFields(take ? (take.stance || 'unknown') : 'unknown', take ? (take.note || '') : '');
      document.getElementById('drawer').classList.add('open');
      document.getElementById('drawer-backdrop').classList.add('show');
      document.getElementById('drawer').setAttribute('aria-hidden', 'false');
      try {{
        const res = await fetch('/api/inflow/item/' + encodeURIComponent(id));
        const data = await res.json();
        if (seq !== drawerSeq) return;
        if (res.ok && data.ok) {{
          if (data.item) document.getElementById('drawer-body').innerHTML = inflowItemHtml(data.item);
          if (data.take) {{
            applyLearnIfCurrent(seq, data.take.stance || 'unknown', data.take.note || '');
          }}
        }}
      }} catch (e) {{ /* cards still work offline; save needs serve */ }}
    }}
    async function openInflowFile(name) {{
      const seq = ++drawerSeq;
      drawerMode = 'file';
      currentInflowId = 'file:' + name;
      currentVertex = null;
      setDrawerLearnLabel('file');
      document.getElementById('drawer-title').textContent = name;
      document.getElementById('drawer-sub').textContent = 'inflow/' + name;
      document.getElementById('drawer-meta').innerHTML = '<code>inflow/' + esc(name) + '</code>';
      document.getElementById('drawer-body').innerHTML = '<p class="wait">Loading file…</p>';
      resetLearnFields('unknown', '');
      document.getElementById('drawer').classList.add('open');
      document.getElementById('drawer-backdrop').classList.add('show');
      document.getElementById('drawer').setAttribute('aria-hidden', 'false');
      try {{
        const res = await fetch('/api/inflow/file?name=' + encodeURIComponent(name));
        const data = await res.json();
        if (seq !== drawerSeq) return;
        if (seq !== drawerSeq) return;
        if (!res.ok || !data.ok) {{
          document.getElementById('drawer-body').innerHTML =
            '<p class="bad">Need <code>--serve</code> to open inflow files.</p>';
          return;
        }}
        document.getElementById('drawer-body').innerHTML =
          '<pre style="white-space:pre-wrap;font-size:12px;line-height:1.45;margin:0">' +
          esc(data.text || '') + '</pre>';
        if (data.take) {{
          applyLearnIfCurrent(seq, data.take.stance || 'unknown', data.take.note || '');
        }}
      }} catch (e) {{
        document.getElementById('drawer-body').innerHTML =
          '<p class="bad">Fetch failed — open via <code>--serve</code>.</p>';
      }}
    }}
    function vertById(id) {{
      return (graphBundle().verts || []).find(x => x.id === id)
        || (STATE.graph.verts || []).find(x => x.id === id) || null;
    }}
    function langVertexHtml(v) {{
      if (!v) return '<p class="bad">节点不在语言图里</p>';
      const g = graphBundle();
      const neigh = [];
      (g.edges || []).forEach(e => {{
        if (e.src === v.id) {{
          const t = vertById(e.dst);
          neigh.push({{ dir: '→', rel: LANG_EDGE[e.label] || e.label, other: t }});
        }} else if (e.dst === v.id) {{
          const t = vertById(e.src);
          neigh.push({{ dir: '←', rel: LANG_EDGE[e.label] || e.label, other: t }});
        }}
      }});
      let html = '<p><span class="pill">' + esc(v.kindRead || v.kind || '') + '</span> ' +
        (v.lang ? '<span class="pill">' + esc(v.lang) + '</span>' : '') + '</p>';
      if (v.surfaceRead) html += '<h4>词面</h4><p style="font-size:16px;color:var(--text)">' + esc(v.surfaceRead) + '</p>';
      if (v.glossRead) html += '<h4>意思</h4><p>' + esc(v.glossRead) + '</p>';
      if (v.fixesRead) html += '<h4>改自</h4><p>' + esc(v.fixesRead) + ' → ' + esc(v.surfaceRead || v.label) + '</p>';
      if (v.date) html += '<h4>日期</h4><p>' + esc(v.date) + '</p>';
      if (neigh.length) {{
        html += '<h4>相连</h4><ul style="margin:6px 0 0 16px;padding:0;font-size:13px">';
        neigh.slice(0, 12).forEach(n => {{
          const lab = (n.other && (n.other.label || n.other.surfaceRead)) || (n.other && n.other.id) || '?';
          html += '<li>' + esc(n.dir + ' ' + (n.rel || '') + ' · ' + lab) + '</li>';
        }});
        html += '</ul>';
      }}
      html += '<p class="legend">语言知识图节点，不是 ontology .fu</p>';
      return html;
    }}
    async function openVertex(id) {{
      const seq = ++drawerSeq;
      drawerMode = 'vertex';
      currentVertex = id;
      currentInflowId = null;
      resetLearnFields('unknown', '');
      setDrawerLearnLabel('vertex');
      const v = vertById(id) || {{ id }};
      const w = weightOf(id);
      const langMode = String(purpose).startsWith('lang-');
      document.getElementById('drawer-title').textContent = langMode ? (v.label || id) : id;
      document.getElementById('drawer-sub').textContent = langMode
        ? ((v.kindRead || v.kind || '') + (v.lang ? ' · ' + v.lang : ''))
        : (v.gloss || v.surface || '').replace(/-/g, ' ');
      document.getElementById('drawer-meta').innerHTML = langMode
        ? '<span class="pill">' + esc(v.kindRead || v.kind || '') + '</span>'
        : ('<code>' + esc(v.kind || '') + '</code> · <code>' + esc(v.lang || v.branch || v.body || '') + '</code>' +
          (w ? ' · weight <strong style="color:var(--acc)">' + w.total + '</strong> · mastery ' + esc(w.mastery) : '') +
          (v.band ? ' · band ' + esc(v.band) : '') +
          (w && w.reason ? '<div style="margin-top:6px;font-size:11px">' + esc(w.reason) + '</div>' : ''));
      document.getElementById('drawer-body').innerHTML = langMode
        ? langVertexHtml(v)
        : '<p class="wait">Loading fu body…</p>';
      if (!langMode) resetLearnFields((w && w.mastery) || 'unknown', '');
      document.getElementById('drawer').classList.add('open');
      document.getElementById('drawer-backdrop').classList.add('show');
      document.getElementById('drawer').setAttribute('aria-hidden', 'false');
      if (langMode) return;
      try {{
        const res = await fetch('/api/vertex/' + encodeURIComponent(id));
        const data = await res.json();
        if (seq !== drawerSeq) return;
        if (!res.ok || !data.ok) {{
          const err = (data && data.error) ? data.error : ('HTTP ' + res.status);
          document.getElementById('drawer-body').innerHTML =
            '<p class="bad">Vertex load failed: <code>' + esc(err) + '</code></p>' +
            '<p class="legend">If this is a network error, open via <code>python skills/project-state-viz.py --serve</code>.</p>' +
            '<p>body path: <code>' + esc(v.body || '') + '</code></p>' +
            (data && data.html ? data.html : '');
        }} else {{
          document.getElementById('drawer-body').innerHTML =
            data.html +
            ((data.tags && data.tags.length)
              ? '<p class="legend">tags: ' + esc(data.tags.join(' ')) + '</p>'
              : '');
          if (data.note) {{
            applyLearnIfCurrent(seq, data.note.grasp || 'unknown', data.note.note || '');
          }} else {{
            applyLearnIfCurrent(seq, (w && w.mastery) || 'unknown', '');
          }}
        }}
      }} catch (err) {{
        if (seq !== drawerSeq) return;
        document.getElementById('drawer-body').innerHTML =
          '<p class="bad">Fetch failed — open via <code>--serve</code> so fu bodies can render and notes save.</p>' +
          '<p><code>' + esc(v.body || '') + '</code></p>';
      }}
    }}
    async function saveLearnerNote() {{
      if (drawerMode === 'inflow' || drawerMode === 'file') {{
        if (!currentInflowId) return;
        const payload = {{
          id: currentInflowId,
          stance: document.getElementById('learn-grasp').value,
          note: document.getElementById('learn-note').value
        }};
        try {{
          const res = await fetch('/api/inflow/take', {{
            method: 'POST',
            headers: {{ 'content-type': 'application/json' }},
            body: JSON.stringify(payload)
          }});
          const data = await res.json();
          document.getElementById('learn-status').textContent = data.ok
            ? ('saved ' + (data.updated || ''))
            : ('fail: ' + (data.error || res.status));
          if (data.ok && STATE.inflow) {{
            STATE.inflow.takes = STATE.inflow.takes || {{}};
            STATE.inflow.takes[currentInflowId] = {{
              id: currentInflowId, stance: payload.stance, note: payload.note, updated: data.updated
            }};
          }}
        }} catch (e) {{
          document.getElementById('learn-status').textContent = 'save needs --serve';
        }}
        return;
      }}
      if (!currentVertex) return;
      const payload = {{
        id: currentVertex,
        grasp: document.getElementById('learn-grasp').value,
        note: document.getElementById('learn-note').value
      }};
      try {{
        const res = await fetch('/api/note', {{
          method: 'POST',
          headers: {{ 'content-type': 'application/json' }},
          body: JSON.stringify(payload)
        }});
        const data = await res.json();
        document.getElementById('learn-status').textContent = data.ok
          ? ('saved ' + (data.updated || ''))
          : ('fail: ' + (data.error || res.status));
      }} catch (e) {{
        document.getElementById('learn-status').textContent = 'save needs --serve';
      }}
    }}
    document.getElementById('drawer-close').onclick = closeDrawer;
    document.getElementById('drawer-backdrop').onclick = closeDrawer;
    document.getElementById('learn-save').onclick = saveLearnerNote;

    function esc(s) {{
      return String(s || '').replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
    }}
    function showPanel() {{
      document.getElementById('net').classList.add('hide');
      document.getElementById('panel').classList.add('show');
      document.getElementById('detail').classList.remove('show');
      hideGraphTools();
    }}
    function clearStudyLayout() {{
      document.getElementById('panel').style.cssText = '';
      document.getElementById('net').style.left = '';
    }}

    function renderToday() {{
      showPanel();
      const t = STATE.today || {{}};
      const actions = t.actions || [];
      let html = '<div class="today-hero"><h2>' + esc(t.weekday) + ' · ' + esc(t.date) +
        '</h2><p>' + esc(t.headline) + '</p><div class="pillrow">' +
        '<span class="pill ok">focus ' + esc(t.focus) + '</span>' +
        '<span class="pill">PLAN NOW <code>' + esc(t.plan_now) + '</code></span>' +
        '<span class="pill">budget ' + esc(t.budget_now) + '</span>' +
        (t.foggy ? '<span class="pill bad">fog/rest</span>' : '<span class="pill ok">head not fog-logged</span>') +
        ((t.injury && t.injury.active) ? '<span class="pill bad">injury active</span>' : '<span class="pill ok">no injury flags</span>') +
        '<span class="pill' + ((t.probe && t.probe.answered) ? ' ok' : ' warn') + '">PROBE ' +
        ((t.probe && t.probe.answered) ? 'filled' : 'empty') + '</span>' +
        '<span class="pill">DUMP pending ' + (t.pending_dumps || 0) + '</span></div></div>';

      if (t.injury && t.injury.active) {{
        html += '<div class="section"><h2>Injury / blockers</h2><div class="card">';
        html += '<p><strong style="color:var(--bad)">' + esc((t.injury.regions||[]).join(' · ')) +
          '</strong></p><p>blockers: <code>' + esc((t.injury.blockers||[]).join(' · ')) +
          '</code></p>';
        (t.injury.notes||[]).slice(0,5).forEach(n => {{
          html += '<p style="font-size:12px;margin-top:6px">' + esc(n) + '</p>';
        }});
        html += '<p style="margin-top:8px"><span class="card click" data-go="train" style="display:inline-block">Open Train / Injury →</span></p></div></div>';
      }}

      if (t.training_week || (t.training_sessions||[]).length) {{
        html += '<div class="section"><h2>Train today</h2>';
        if (t.training_week) {{
          html += '<div class="card"><span class="tag">' + esc(t.training_week.role) +
            '</span><h3>' + esc(t.training_week.date) + '</h3><p>' + esc(t.training_week.do) +
            '</p><p style="margin-top:6px;color:var(--bad)">blocker ' +
            esc(t.training_week.blocker) + '</p></div>';
        }}
        (t.training_sessions||[]).forEach(s => {{
          html += '<div class="card" style="margin-top:8px"><span class="tag">' +
            esc(s.status) + '</span><h3>' + esc(s.label) + '</h3><p>skip: ' +
            esc((s.skip||[]).join(', ')) + '</p><p>' + esc(s.skipNote||'') + '</p></div>';
        }});
        html += '</div>';
      }}

      const rt = t.routine || {{}};
      if ((rt.daily||[]).length || (rt.due||[]).length || (rt.optimize||[]).length) {{
        html += '<div class="section"><h2>Routine today</h2>';
        if ((rt.due||[]).length) {{
          html += '<div class="card" style="margin-bottom:8px"><h3>Preventive recall</h3>';
          (rt.due||[]).forEach(r => {{
            const cls = r.due_state === 'due' ? 'bad' : (r.due_state === 'soon' ? 'wait' : 'wait');
            html += '<p style="margin-top:6px"><span class="' + cls + '">' + esc(r.due_state) +
              '</span> · ' + esc(r.label) + ' / ' + esc(r.label_zh) +
              ' · every ' + esc(r.interval_months) + 'mo' +
              (r.last_done ? ' · last ' + esc(r.last_done) : ' · last_done empty — ask human') +
              '</p>';
          }});
          html += '</div>';
        }}
        const bySlot = {{}};
        (rt.daily||[]).forEach(d => {{
          const s = d.slot || 'other';
          (bySlot[s] = bySlot[s] || []).push(d);
        }});
        Object.keys(bySlot).forEach(slot => {{
          html += '<div class="card" style="margin-bottom:8px"><span class="tag">' + esc(slot) +
            '</span>';
          bySlot[slot].forEach(d => {{
            html += '<p style="margin-top:6px"><strong>' + esc(d.label) + '</strong> / ' +
              esc(d.label_zh) + ' · ' + esc(d.minutes) + 'm<br><span style="font-size:12px">' +
              esc(d.protocol||'') + '</span></p>';
          }});
          html += '</div>';
        }});
        if ((rt.optimize||[]).length) {{
          html += '<div class="card"><h3>Optimize open</h3>';
          (rt.optimize||[]).slice(0,3).forEach(o => {{
            html += '<p style="margin-top:6px">' + esc(o.change) + ' — ' + esc(o.why) + '</p>';
          }});
          html += '</div>';
        }}
        html += '<p style="margin-top:8px"><span class="card click" data-go="routine" style="display:inline-block">Open Routine →</span></p></div>';
      }}

      html += '<div class="section"><h2>Do / Dont (merged)</h2>';
      if (!actions.length) html += '<p>No synthesized rows. Check CPU NOTE TODAY.</p>';
      actions.forEach(a => {{
        html += '<div class="action"><div class="pri">P' + a.priority +
          '</div><div class="kind ' + esc(a.kind) + '">' + esc(a.kind) +
          '</div><div class="txt">' + esc(a.text) +
          '<span class="src">' + esc(a.source) + '</span></div></div>';
      }});
      html += '</div>';

      html += '<div class="section"><h2>Calendar today</h2>';
      if (!(t.harvest_today || []).length && !(t.cpu_sched_today || []).length) {{
        html += '<p class="wait">No harvest/CPU schedule row covering ' + esc(t.date) + '</p>';
      }} else {{
        html += '<table><tr><th>status</th><th>title</th><th>where</th></tr>';
        (t.harvest_today || []).forEach(r => {{
          html += '<tr><td class="' + (r.status==='confirmed'?'ok':'wait') + '">' +
            esc(r.status) + '</td><td>' + esc(r.title) + '</td><td>' + esc(r.where) + '</td></tr>';
        }});
        html += '</table>';
        (t.cpu_sched_today || []).forEach(s => {{
          html += '<div class="card" style="margin-top:8px"><p>' + esc(s) + '</p></div>';
        }});
      }}
      html += '</div>';

      html += '<div class="section"><h2>Learn surface</h2><div class="card"><h3>NOW · ' +
        esc(t.plan_now) + '</h3><p>' +
        (t.probe && t.probe.answered
          ? '<span class="ok">ANSWER present</span>'
          : '<span class="wait">ANSWER empty — do not invent</span>') +
        '</p><p style="margin-top:8px">' + esc((t.probe && t.probe.text) || '') +
        '</p><p style="margin-top:8px;font-size:11px">NEXT ' +
        esc((t.plan_next || []).join(' ')) + '</p></div></div>';

      if ((t.training_flags || []).length) {{
        html += '<div class="section"><h2>Training stops</h2><div class="card"><code>' +
          esc((t.training_flags || []).join(' · ')) + '</code></div></div>';
      }}

      html += '<p class="legend">Sources: CPU NOTE TODAY · training · routine · harvest · PLAN/STUDY · endurance · DUMP · weights. Re-run viz to refresh.</p>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('panel').querySelectorAll('[data-go]').forEach(el => {{
        el.onclick = () => setPurpose(el.dataset.go);
      }});
      document.getElementById('stats').textContent =
        'actions ' + actions.length + ' · ' + esc(t.date);
    }}

    function renderRoutine() {{
      showPanel();
      const rt = ((STATE.self && STATE.self.routine) || (STATE.today && STATE.today.routine) || {{}});
      let html = '<div class="today-hero"><h2>Routine</h2><p>Store <code>self/routine.toon.md</code> · ' +
        'cron <code>routine-enrich.py --due</code> · mark via <code>--mark-done</code> / <code>--mark-periodic</code></p>' +
        '<div class="pillrow">' +
        '<span class="pill ok">daily ' + ((rt.daily||[]).length) + '</span>' +
        '<span class="pill warn">due/soon/ask ' + ((rt.due||[]).length) + '</span>' +
        '<span class="pill">tips ' + ((rt.tips||[]).length) + '</span>' +
        '<span class="pill">optimize open ' + ((rt.optimize||[]).length) + '</span></div></div>';

      html += '<div class="section"><h2>Daily protocol</h2>';
      (rt.daily||[]).forEach(d => {{
        html += '<div class="card" style="margin-bottom:8px"><span class="tag">' + esc(d.slot) +
          '</span><h3>' + esc(d.label) + ' / ' + esc(d.label_zh) + '</h3><p>' + esc(d.minutes) +
          'm · <code>' + esc(d.id) + '</code></p><p style="margin-top:6px">' + esc(d.protocol||'') +
          '</p>' + (d.source ? '<p class="legend"><a href="' + esc(d.source) +
          '" target="_blank" rel="noopener">SOURCE</a></p>' : '') + '</div>';
      }});
      html += '</div>';

      html += '<div class="section"><h2>Periodic preventive</h2><table><tr><th>state</th><th>item</th><th>interval</th><th>last</th><th>next</th></tr>';
      (rt.periodic||[]).forEach(r => {{
        const cls = r.due_state === 'due' ? 'bad' : (r.due_state === 'ok' ? 'ok' : 'wait');
        html += '<tr><td class="' + cls + '">' + esc(r.due_state) + '</td><td>' +
          esc(r.label) + ' / ' + esc(r.label_zh) + '</td><td>' + esc(r.interval_months) +
          ' mo</td><td>' + esc(r.last_done || '—') + '</td><td>' + esc(r.next_due || '—') +
          '</td></tr>';
      }});
      html += '</table><p class="legend">Empty last_done → ask human. Do not invent Termin.</p></div>';

      html += '<div class="section"><h2>Tips (sourced)</h2>';
      (rt.tips||[]).forEach(tip => {{
        html += '<div class="card" style="margin-bottom:8px"><span class="tag">' + esc(tip.topic) +
          '</span><p>' + esc(tip.text) + '</p>' +
          (tip.source ? '<p class="legend"><a href="' + esc(tip.source) +
          '" target="_blank" rel="noopener">SOURCE</a></p>' : '') + '</div>';
      }});
      html += '</div>';

      html += '<div class="section"><h2>Optimize open</h2>';
      if (!(rt.optimize||[]).length) html += '<p class="wait">No open optimize rows.</p>';
      (rt.optimize||[]).forEach(o => {{
        html += '<div class="card" style="margin-bottom:8px"><h3>' + esc(o.change) +
          '</h3><p>habit <code>' + esc(o.habit) + '</code> — ' + esc(o.why) + '</p></div>';
      }});
      html += '</div>';

      html += '<p class="legend">Reminders only — not prescriptions. Mouth particulars stay in .private/health.fu.md</p>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent =
        'daily ' + ((rt.daily||[]).length) + ' · due ' + ((rt.due||[]).length);
    }}

    function renderTrain() {{
      showPanel();
      const tr = (STATE.self && STATE.self.training) || {{}};
      const inj = tr.injury || {{}};
      let html = '<div class="today-hero"><h2>Train / Injury</h2><p>Store <code>self/training.toon.md</code> · updated ' +
        esc(tr.updated) + '</p><div class="pillrow">' +
        '<span class="pill ok">bw ' + esc(tr.bodyweightKg) + ' kg</span>' +
        (tr.bodyweightPrev ? '<span class="pill">prev ' + esc(tr.bodyweightPrev) + '</span>' : '') +
        '<span class="pill">claimed 1RM ' + esc(tr.claimed_bench) + '</span>' +
        '<span class="pill">session e1RM ' + esc(tr.session_e1rm) + '</span>' +
        '<span class="pill">pullups best ' + esc(tr.pullups_best) + '</span>' +
        (inj.active ? '<span class="pill bad">injury ACTIVE</span>' : '<span class="pill ok">injury clear</span>') +
        '</div></div>';

      html += '<div class="section"><h2>Injury status</h2><div class="card">';
      if (!inj.active) {{
        html += '<p class="ok">No active injury flags in store.</p>';
      }} else {{
        html += '<p><strong style="color:var(--bad)">Regions: ' + esc((inj.regions||[]).join(' · ')) +
          '</strong></p><p>Blockers: <code>' + esc((inj.blockers||[]).join(' · ')) + '</code></p>';
        (inj.notes||[]).forEach(n => {{ html += '<p style="margin-top:6px;font-size:12px">' + esc(n) + '</p>'; }});
      }}
      html += '<table style="margin-top:10px"><tr><th>flag</th><th>value</th></tr>';
      Object.entries(tr.flags || {{}}).forEach(([k,v]) => {{
        const bad = String(v).toLowerCase() === 'true' || /pain|skip/i.test(k);
        html += '<tr><td><code>' + esc(k) + '</code></td><td class="' + (bad?'bad':'') + '">' + esc(v) + '</td></tr>';
      }});
      html += '</table></div></div>';

      const per = tr.periodization || {{}};
      html += '<div class="section"><h2>Periodization</h2><div class="card"><p><strong>' +
        esc(per.thisMicrocycle || '') + '</strong></p><p>' + esc(per.thisMicrocycleNote || '') +
        '</p><p style="margin-top:8px">framework: ' + esc(per.framework || '') +
        '</p><p>next meso: ' + esc(per['nextMeso.kind'] || '') + ' after ' +
        esc(per['nextMeso.startAfter'] || '') + ' · e1RM ' + esc(per['nextMeso.e1rmKg'] || '') +
        '</p></div></div>';

      html += '<div class="section"><h2>Week plan</h2><table><tr><th>date</th><th>role</th><th>do</th><th>blocker</th></tr>';
      (tr.week || []).forEach(w => {{
        const isToday = STATE.today && STATE.today.date === w.date;
        html += '<tr' + (isToday ? ' style="background:#1a2a22"' : '') + '><td>' + esc(w.date) +
          (isToday ? ' ←' : '') + '</td><td class="wait">' + esc(w.role) + '</td><td>' +
          esc(w.do) + '</td><td class="bad">' + esc(w.blocker) + '</td></tr>';
      }});
      html += '</table></div>';

      html += '<div class="section"><h2>Sessions</h2>';
      (tr.sessions || []).forEach(s => {{
        html += '<div class="card" style="margin-bottom:10px"><span class="tag">' + esc(s.status) +
          '</span><h3>' + esc(s.date) + ' · ' + esc(s.label) + '</h3>';
        if ((s.skip||[]).length) html += '<p>skip: <code>' + esc(s.skip.join(', ')) + '</code></p>';
        if (s.skipNote) html += '<p>' + esc(s.skipNote) + '</p>';
        if (s.pain && s.pain.region) {{
          html += '<p class="bad">pain ' + esc(s.pain.region) +
            (s.pain.regionZh ? ' / ' + esc(s.pain.regionZh) : '') +
            ' · ' + esc(s.pain.quality || '') + ' · relief ' + esc(s.pain.reliefPct || '') + '%</p>';
        }}
        if ((s.blocks||[]).length) {{
          html += '<table><tr><th>block</th><th>do</th><th>RPE</th><th>note</th></tr>';
          s.blocks.forEach(b => {{
            html += '<tr><td>' + esc(b.min) + '</td><td>' + esc(b.do) + '</td><td>' +
              esc(b.rpe) + '</td><td>' + esc(b.note) + '</td></tr>';
          }});
          html += '</table>';
        }}
        html += '</div>';
      }});
      html += '</div>';

      const ns = tr.next_session || {{}};
      html += '<div class="section"><h2>Next session (when clear)</h2><div class="card"><p>condition: ' +
        esc(ns.bench_condition || '') + '</p><p>earliest: <code>' + esc(ns.bench_when || '') +
        '</code></p><p>top: ' + esc(ns.bench_top || '') + '</p><p>pull: ' + esc(ns.pull || '') +
        '</p><p>technique if not quiet: ' + esc(ns.technique || '') + '</p></div></div>';

      html += '<div class="section"><h2>Recent log</h2><table><tr><th>date</th><th>kind</th><th>note</th></tr>';
      (tr.logs || []).slice().reverse().forEach(l => {{
        const cls = l.kind === 'pain' ? 'bad' : (l.kind === 'doms' ? 'wait' : '');
        html += '<tr><td>' + esc(l.date) + '</td><td class="' + cls + '">' + esc(l.kind) +
          '</td><td>' + esc(l.note) + '</td></tr>';
      }});
      html += '</table></div>';

      if ((tr.rules || []).length) {{
        html += '<div class="section"><h2>Rules</h2><ul style="margin:0;padding-left:18px;font-size:12px">';
        tr.rules.forEach(r => {{ html += '<li style="margin-bottom:4px">' + esc(r) + '</li>'; }});
        html += '</ul></div>';
      }}

      html += '<p class="legend">Do not invent quiet scapula. Do not invent completed sets. Store: self/training.toon.md</p>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent =
        'sessions ' + (tr.sessions||[]).length + ' · injury ' + (inj.active ? 'ACTIVE' : 'clear');
    }}

    function renderProject() {{
      showPanel();
      const pulse = [
        ['today', 'Today', (STATE.today&&STATE.today.date) + ' · ' + ((STATE.today&&STATE.today.actions)||[]).length + ' actions'],
        ['train', 'Train / Injury', ((STATE.self.training&&STATE.self.training.injury&&STATE.self.training.injury.active)?'ACTIVE':'clear') + ' · ' + ((STATE.self.training&&STATE.self.training.sessions)||[]).length + ' sessions'],
        ['routine', 'Routine', (((STATE.self.routine&&STATE.self.routine.daily)||[]).length) + ' daily · ' + (((STATE.self.routine&&STATE.self.routine.due)||[]).length) + ' due/ask'],
        ['self', 'Self', (STATE.self.files||[]).length + ' files · focus ' + (STATE.goals.focus||'')],
        ['schedule', 'Schedule', (STATE.schedule.harvest||[]).length + ' harvest · ' + (STATE.schedule.enrich||[]).length + ' enrich'],
        ['cron', 'Cron', (STATE.cron.jobs||[]).length + ' jobs · ' + (STATE.cron.scripts||[]).length + ' py'],
        ['inflow', 'Inflow', (STATE.inflow.pending||[]).length + ' pending · skip ' + (STATE.inflow.state.skip_count||0)],
        ['runtime', 'CPU', (STATE.cpu.agents||[]).length + ' agent · ' + (STATE.cpu.todos||[]).length + ' todo'],
        ['study', 'Study', (STATE.studies||[]).length + ' STUDY'],
        ['weights', 'Weights', ((STATE.weights&&STATE.weights.nodes)||[]).length + ' scored · ' + esc((STATE.weights&&STATE.weights.updated)||'')],
        ['ontology', 'Ontology', 'V' + STATE.graph.v_count + ' E' + STATE.graph.e_count],
        ['skills', 'Skills', (STATE.skills.cursor_skills||[]).length + ' cursor · ' + (STATE.skills.library||[]).length + ' lib'],
        ['mezzanine', 'Mezzanine', (STATE.mezzanine.files||[]).length + ' notes'],
        ['tmp', 'Tmp', (STATE.tmp.sibling_count||0) + ' siblings · ttl ' + ((STATE.tmp.ttl||{{}}).last_run||'')],
      ];
      let html = '<div class="section"><h2>Organs (distinct stores)</h2><div class="grid">';
      pulse.forEach(([id, label, meta]) => {{
        html += '<div class="card click" data-go="' + id + '"><span class="tag">' + esc(id) +
          '</span><h3>' + esc(label) + '</h3><p>' + esc(meta) + '</p></div>';
      }});
      html += '</div></div><div class="section"><h2>ROOT constitution</h2><div class="grid">';
      STATE.organs.forEach(o => {{
        html += '<div class="card"><span class="tag">' + esc(o.tag) + '</span><h3>' + esc(o.name) +
          '</h3><p>' + esc(o.kind) + '</p><p style="margin-top:6px">' + esc(o.meaning) + '</p></div>';
      }});
      html += '</div></div><div class="section"><h2>Pedagogy branches</h2><div class="grid">';
      (STATE.pedagogy_dirs.branches||[]).forEach(b => {{
        html += '<div class="card"><h3>' + esc(b.name) + '</h3><p>' + b.fu_count + ' .fu.md</p></div>';
      }});
      html += '</div></div><div class="section"><h2>Recycle</h2><div class="card"><p>files ' +
        (STATE.recycle.file_count||0) + '</p><p>' + esc(STATE.recycle.journal_head||'') + '</p></div></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('panel').querySelectorAll('[data-go]').forEach(el => {{
        el.onclick = () => setPurpose(el.dataset.go);
      }});
      document.getElementById('stats').textContent = 'organs ' + STATE.organs.length;
    }}

    function renderSelf() {{
      showPanel();
      const s = STATE.self;
      let html = '<div class="section"><h2>Goals</h2><div class="card"><h3>focus · ' + esc(s.goals.focus) +
        '</h3><p>north <code>' + esc((s.goals.north||[]).join(' ')) + '</code></p><table><tr><th>id</th><th>want</th><th>status</th></tr>';
      (s.goals.nodes||[]).forEach(n => {{
        html += '<tr><td>' + esc(n.id) + '</td><td>' + esc(n.want) + '</td><td>' + esc(n.status) + '</td></tr>';
      }});
      html += '</table></div></div>';
      html += '<div class="section"><h2>Endurance</h2><div class="card"><p>budget now ' +
        esc(s.endurance.budget_now) + ' / default ' + esc(s.endurance.budget_default) + '</p><table><tr><th>activity</th><th>vertex</th></tr>';
      (s.endurance.activities||[]).forEach(a => {{
        html += '<tr><td>' + esc(a.label||a.id) + '</td><td><code>' + esc(a.vertex) + '</code></td></tr>';
      }});
      html += '</table><table><tr><th>date</th><th>sore</th><th>note</th></tr>';
      (s.endurance.logs||[]).forEach(l => {{
        html += '<tr><td>' + esc(l.date) + '</td><td class="wait">' + esc(l.sore) + '</td><td>' + esc(l.note) + '</td></tr>';
      }});
      html += '</table></div></div>';
      html += '<div class="section"><h2>Training pulse</h2><div class="card"><p>bw ' +
        esc(s.training.bodyweightKg) + ' kg · updated ' + esc(s.training.updated) +
        '</p><p>flags true: <code>' + esc((s.training.flags_true||[]).join(' ')) +
        '</code></p><p>claimed bench 1RM ' + esc(s.training.claimed_bench) +
        ' · session e1RM ' + esc(s.training.session_e1rm) +
        '</p><p style="margin-top:8px"><span class="card click" data-go="train" style="display:inline-block">Open Train / Injury →</span></p></div></div>';
      html += '<div class="section"><h2>Learn grasp</h2><div class="card"><p>target ' +
        esc(s.learn.target) + '</p><table><tr><th>id</th><th>grasp</th></tr>';
      (s.learn.nodes||[]).forEach(n => {{
        html += '<tr><td><code>' + esc(n.id) + '</code></td><td class="wait">' + esc(n.grasp) + '</td></tr>';
      }});
      html += '</table></div></div><div class="section"><h2>self/ files</h2><table><tr><th>path</th><th>schema</th><th>mtime</th></tr>';
      (s.files||[]).forEach(f => {{
        html += '<tr><td><code>' + esc(f.path) + '</code></td><td>' + esc(f.schema||f.kind) +
          '</td><td>' + esc(f.mtime) + '</td></tr>';
      }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('panel').querySelectorAll('[data-go]').forEach(el => {{
        el.onclick = () => setPurpose(el.dataset.go);
      }});
      document.getElementById('stats').textContent = 'self files ' + (s.files||[]).length;
    }}

    function renderSchedule() {{
      showPanel();
      const s = STATE.schedule;
      const harvest = s.harvest || [];
      let mode = window.__schedMode || 'calendar';
      function paint() {{
        mode = window.__schedMode || mode;
        let html = '<div class="viewbar">' +
          '<button data-m="table"' + (mode==='table'?' class="on"':'') + '>Table</button>' +
          '<button data-m="calendar"' + (mode==='calendar'?' class="on"':'') + '>Calendar</button>' +
          '<button data-m="gantt"' + (mode==='gantt'?' class="on"':'') + '>Gantt</button></div>';
        html += '<p class="legend">confirmed=<span class="ok">green</span> · candidate=<span class="wait">amber</span> · source harvest.toon + CPU SCHEDULE</p>';
        if (mode === 'table') {{
          html += '<div class="section"><h2>CPU SCHEDULE</h2><table><tr><th>row</th></tr>';
          (s.cpu_schedules||[]).forEach(r => {{ html += '<tr><td>' + esc(r.text) + '</td></tr>'; }});
          html += '</table></div><div class="section"><h2>harvest</h2><table><tr><th>start</th><th>status</th><th>title</th><th>where</th></tr>';
          harvest.forEach(r => {{
            const st = r.status === 'confirmed' ? 'ok' : 'wait';
            html += '<tr><td>' + esc(r.start) + '</td><td class="' + st + '">' + esc(r.status) +
              '</td><td>' + esc(r.title) + '</td><td>' + esc(r.where) + '</td></tr>';
          }});
          html += '</table></div>';
        }} else if (mode === 'calendar') {{
          const byDay = {{}};
          harvest.forEach(r => {{
            const d = (r.start || '').slice(0, 10);
            if (!d) return;
            (byDay[d] = byDay[d] || []).push(r);
          }});
          const days = Object.keys(byDay).sort();
          if (!days.length) {{
            html += '<p>no harvest dates</p>';
          }} else {{
            const start = new Date(days[0] + 'T12:00:00');
            const end = new Date(days[days.length-1] + 'T12:00:00');
            const cursor = new Date(start.getFullYear(), start.getMonth(), 1);
            const last = new Date(end.getFullYear(), end.getMonth() + 1, 0);
            while (cursor <= last) {{
              const y = cursor.getFullYear(), m = cursor.getMonth();
              html += '<div class="section"><h2>' + y + '-' + String(m+1).padStart(2,'0') + '</h2><div class="cal">';
              ['Mo','Tu','We','Th','Fr','Sa','Su'].forEach(h => {{ html += '<div class="hd">' + h + '</div>'; }});
              let dow = (new Date(y, m, 1).getDay() + 6) % 7;
              for (let i = 0; i < dow; i++) html += '<div class="day mute"></div>';
              const dim = new Date(y, m + 1, 0).getDate();
              for (let day = 1; day <= dim; day++) {{
                const key = y + '-' + String(m+1).padStart(2,'0') + '-' + String(day).padStart(2,'0');
                const evs = byDay[key] || [];
                html += '<div class="day"><div class="n">' + day + '</div>';
                evs.forEach(e => {{
                  html += '<span class="ev' + (e.status==='confirmed'?'':' cand') + '" title="' +
                    esc(e.title + ' · ' + e.where) + '">' + esc(e.title) + '</span>';
                }});
                html += '</div>';
              }}
              html += '</div></div>';
              cursor.setMonth(cursor.getMonth() + 1);
            }}
          }}
        }} else {{
          // gantt
          const parsed = harvest.map(r => {{
            const a = Date.parse(r.start);
            const b = Date.parse(r.end || r.start);
            return {{ ...r, a: isNaN(a)?null:a, b: isNaN(b)?a:b }};
          }}).filter(r => r.a != null).sort((x,y) => x.a - y.a);
          if (!parsed.length) {{
            html += '<p>no parseable dates</p>';
          }} else {{
            const minT = Math.min(...parsed.map(r => r.a));
            const maxT = Math.max(...parsed.map(r => r.b));
            const span = Math.max(1, maxT - minT);
            html += '<div class="section"><h2>Gantt</h2><div class="gantt">';
            parsed.forEach(r => {{
              const left = ((r.a - minT) / span) * 100;
              const width = Math.max(1.2, ((r.b - r.a) / span) * 100);
              html += '<div class="row"><div class="label">' + esc(r.title) +
                '</div><div class="track"><div class="bar ' + (r.status==='confirmed'?'ok':'cand') +
                '" style="left:' + left + '%;width:' + width + '%" title="' +
                esc(r.start + ' → ' + (r.end||'') + ' · ' + r.status) + '">' +
                esc((r.start||'').slice(0,10)) + '</div></div></div>';
            }});
            html += '</div></div>';
          }}
        }}
        document.getElementById('panel').innerHTML = html;
        document.getElementById('panel').querySelectorAll('.viewbar button').forEach(btn => {{
          btn.onclick = () => {{ window.__schedMode = btn.dataset.m; paint(); }};
        }});
        document.getElementById('stats').textContent =
          'harvest ' + harvest.length + ' · view ' + mode;
      }}
      paint();
    }}

    function renderWeights() {{
      showPanel();
      const w = STATE.weights || {{ nodes: [] }};
      let html = '<div class="section"><h2>Attention weights</h2><p class="legend">Updated ' +
        esc(w.updated) + ' · focus ' + esc(w.focus) +
        ' · run <code>python cron/ontology-weight.py</code> (maintain organ). Size on Ontology graph = total. Mastery from learn grasp.</p>';
      html += '<table><tr><th>total</th><th>id</th><th>mastery</th><th>hire</th><th>plan</th><th>study</th><th>zeit</th><th>maslow</th><th>reason</th></tr>';
      (w.nodes||[]).forEach(n => {{
        const mc = n.mastery === 'firm' ? 'ok' : (n.mastery === 'unknown' ? 'wait' : 'wait');
        html += '<tr><td><strong style="color:var(--acc)">' + n.total +
          '</strong></td><td><code>' + esc(n.id) + '</code></td><td class="' + mc + '">' +
          esc(n.mastery) + '</td><td>' + n.hire + '</td><td>' + n.plan + '</td><td>' +
          n.study + '</td><td>' + n.zeit + '</td><td>' + n.maslow + ' <span style="color:var(--muted)">' +
          esc(n.maslow_layer) + '</span></td><td style="font-size:11px">' + esc(n.reason) + '</td></tr>';
      }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent = 'weighted ' + (w.nodes||[]).length;
    }}

    function renderCron() {{
      showPanel();
      let html = '<div class="section"><h2>cron jobs (.fu.md)</h2><p style="font-size:12px">Scheduled gatherers — not CPU life queue, not ontology claims.</p><table><tr><th>file</th><th>kind</th><th>agents</th><th>py</th></tr>';
      (STATE.cron.jobs||[]).forEach(j => {{
        html += '<tr><td><code>' + esc(j.file) + '</code></td><td>' + esc(j.kind) +
          '</td><td>' + esc((j.agents||[]).join(' ')) + '</td><td>' +
          (j.has_py ? '<span class="ok">yes</span>' : '—') + '</td></tr>';
      }});
      html += '</table></div><div class="section"><h2>scripts</h2><table><tr><th>file</th><th>bytes</th></tr>';
      (STATE.cron.scripts||[]).forEach(s => {{
        html += '<tr><td><code>' + esc(s.file) + '</code></td><td>' + s.bytes + '</td></tr>';
      }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent = 'jobs ' + (STATE.cron.jobs||[]).length;
    }}

    function renderInflow() {{
      showPanel();
      const i = STATE.inflow || {{}};
      const takes = i.takes || {{}};
      let tab = 'digest';
      const pendingLive = (i.pending||[]).filter(d => (d.status||'').toLowerCase() !== 'dripped');
      const openLive = (i.human_open||[]).filter(d => (d.status||'').toLowerCase() !== 'closed');

      function card(it, lane) {{
        const take = takes[it.id];
        const st = it.status || lane || '';
        const stCls = st === 'pending' || st === 'open' ? 'warn' : (st === 'dripped' ? 'ok' : '');
        let h = '<div class="card in-card" data-inid="' + esc(it.id) + '">' +
          '<div class="pillrow"><span class="pill ' + stCls + '">' + esc(st) + '</span>' +
          (it.kind ? '<span class="pill">' + esc(it.kind) + '</span>' : '') +
          (lane ? '<span class="pill">' + esc(lane) + '</span>' : '') +
          (take && take.note ? '<span class="pill take-badge">your take</span>' : '') +
          '</div><h3 style="margin:10px 0 0">' + esc(it.title || it.id) + '</h3>';
        if (it.why) h += '<p class="why">' + esc(it.why) + '</p>';
        else if (it.note) h += '<p class="why">' + esc(it.note.slice(0, 220)) + (it.note.length>220?'…':'') + '</p>';
        h += '<p class="meta"><code>' + esc(it.id) + '</code>' +
          (it.learn ? ' · LEARN ' + esc(it.learn) : '') +
          ((it.urls&&it.urls[0]) || it.url ? ' · link' : '') +
          ' · click to open</p></div>';
        return h;
      }}

      function paint() {{
        let html = '<div class="today-hero"><h2>Inflow digest</h2><p>Away captures for a human to read — not ontology claims. Write your take in the drawer.</p>' +
          '<div class="pillrow">' +
          '<span class="pill warn">digest ' + ((i.digest||[]).length) + '</span>' +
          '<span class="pill">pending live ' + pendingLive.length + '</span>' +
          '<span class="pill">human open ' + openLive.length + '</span>' +
          '<span class="pill">news ' + ((i.news||[]).length) + '</span>' +
          '<span class="pill">skip ' + ((i.state&&i.state.skip_count)||0) + '</span></div></div>';

        html += '<div class="viewbar">' +
          [['digest','Digest'],['pending','Pending'],['open','Human open'],['news','NEWS'],['files','Files'],['state','STATE']].map(([id,lab]) =>
            '<button type="button" data-intab="' + id + '" class="' + (tab===id?'on':'') + '">' + lab + '</button>'
          ).join('') + '</div>';

        if (tab === 'digest') {{
          html += '<div class="section"><h2>Read these</h2><p class="legend">Open / researched / pending — skip dripped noise. Click a card.</p>';
          if (!(i.digest||[]).length) html += '<p class="wait">Digest empty.</p>';
          (i.digest||[]).forEach(d => {{ html += card(d, d.lane); }});
          html += '</div>';
        }} else if (tab === 'pending') {{
          html += '<div class="section"><h2>DUMP pending</h2>';
          (i.pending||[]).forEach(d => {{ html += card(d, 'pending'); }});
          html += '</div>';
        }} else if (tab === 'open') {{
          html += '<div class="section"><h2>HUMAN OPEN</h2>';
          (i.human_open||[]).forEach(d => {{ html += card(d, 'human-open'); }});
          html += '</div>';
        }} else if (tab === 'news') {{
          html += '<div class="section"><h2>inflow.fu NEWS (newest first)</h2>';
          (i.news||[]).slice().reverse().forEach(n => {{ html += card(n, 'news'); }});
          html += '</div>';
        }} else if (tab === 'files') {{
          html += '<div class="section"><h2>inflow files</h2><p class="legend">Click to read full text via --serve.</p>';
          (i.files||[]).forEach(f => {{
            const name = (f.name || (f.path||'').split('/').pop());
            html += '<div class="card in-card" data-infile="' + esc(name) + '"><h3>' +
              esc(name) + '</h3><p class="meta">' + esc(f.path) + ' · ' + esc(f.mtime||'') +
              (takes['file:'+name] && takes['file:'+name].note ? ' · <span class="take-badge">your take</span>' : '') +
              '</p></div>';
          }});
          html += '</div>';
        }} else {{
          const st = i.state || {{}};
          html += '<div class="section"><h2>STATE</h2><div class="card"><p>' + esc(st.header) +
            '</p><p style="margin-top:8px">' + esc(st.loop) + '</p><p>' + esc(st.maintain) +
            '</p><p class="meta">last_organ ' + esc(st.last_organ) + ' · skip ' + (st.skip_count||0) +
            '</p><p style="margin-top:8px">' + esc(st.last_delta) + '</p></div>';
          html += '<h2 style="margin-top:16px">Recent skip (tail)</h2><table><tr><th>id</th></tr>';
          (st.recent_skip||[]).forEach(s => {{ html += '<tr><td><code>' + esc(s) + '</code></td></tr>'; }});
          html += '</table></div>';
        }}

        html += '<p class="legend">Stores: inflow/DUMP.md · inflow.fu.md · STATE.md · takes → inflow/takes.toon.md (tmp cache)</p>';
        document.getElementById('panel').innerHTML = html;
        document.getElementById('panel').querySelectorAll('[data-intab]').forEach(btn => {{
          btn.onclick = () => {{ tab = btn.dataset.intab; paint(); }};
        }});
        document.getElementById('panel').querySelectorAll('[data-inid]').forEach(el => {{
          el.onclick = () => openInflowItem(el.dataset.inid);
        }});
        document.getElementById('panel').querySelectorAll('[data-infile]').forEach(el => {{
          el.onclick = () => openInflowFile(el.dataset.infile);
        }});
        document.getElementById('stats').textContent =
          'digest ' + ((i.digest||[]).length) + ' · pending ' + pendingLive.length +
          ' · news ' + ((i.news||[]).length);
      }}
      paint();
    }}

    function renderRuntime() {{
      showPanel();
      const c = STATE.cpu;
      let html = '<div class="section"><h2>NOTE</h2>';
      (c.notes||[]).forEach(n => {{ html += '<div class="card" style="margin-bottom:8px"><p>' + esc(n) + '</p></div>'; }});
      html += '</div><div class="section"><h2>AGENT</h2><table><tr><th>id</th><th>when</th><th>prompt</th></tr>';
      (c.agents||[]).forEach(a => {{
        html += '<tr><td><code>' + esc(a.id) + '</code></td><td>' + esc(a.when) +
          '</td><td>' + esc(a.prompt) + '</td></tr>';
      }});
      html += '</table></div><div class="section"><h2>TODO</h2><table><tr><th>done</th><th>text</th></tr>';
      (c.todos||[]).forEach(t => {{
        html += '<tr><td>' + (t.done ? '<span class="ok">DONE</span>' : '<span class="wait">open</span>') +
          '</td><td>' + esc(t.text) + '</td></tr>';
      }});
      html += '</table></div><div class="section"><h2>SCHEDULE</h2><table><tr><th>row</th></tr>';
      (c.schedules||[]).forEach(s => {{ html += '<tr><td>' + esc(s.text) + '</td></tr>'; }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent =
        'agents ' + (c.agents||[]).length + ' · todos ' + (c.todos||[]).length;
    }}

    function renderSkills() {{
      showPanel();
      let html = '<div class="section"><h2>.cursor/skills</h2><table><tr><th>name</th><th>description</th></tr>';
      (STATE.skills.cursor_skills||[]).forEach(s => {{
        html += '<tr><td><code>' + esc(s.name) + '</code></td><td>' + esc(s.description) + '</td></tr>';
      }});
      html += '</table></div><div class="section"><h2>skills/ library</h2><table><tr><th>path</th><th>kind/schema</th></tr>';
      (STATE.skills.library||[]).forEach(f => {{
        html += '<tr><td><code>' + esc(f.path) + '</code></td><td>' + esc(f.kind||f.schema) + '</td></tr>';
      }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent =
        'cursor ' + (STATE.skills.cursor_skills||[]).length;
    }}

    function renderMezzanine() {{
      showPanel();
      let html = '<div class="section"><h2>mezzanine (ingest · not claims)</h2><table><tr><th>path</th><th>schema</th><th>mtime</th></tr>';
      (STATE.mezzanine.files||[]).forEach(f => {{
        html += '<tr><td><code>' + esc(f.path) + '</code></td><td>' + esc(f.schema) +
          '</td><td>' + esc(f.mtime) + '</td></tr>';
      }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent = 'files ' + (STATE.mezzanine.files||[]).length;
    }}

    function renderTmp() {{
      showPanel();
      const t = STATE.tmp;
      let html = '<div class="section"><h2>ttl.toon.md</h2><div class="card"><p>last_run ' +
        esc((t.ttl||{{}}).last_run) + '</p><p>lapse_days ' + esc((t.ttl||{{}}).lapse_days) +
        '</p><p>last_expire ' + esc((t.ttl||{{}}).last_expire) + '</p></div></div>';
      html += '<div class="section"><h2>siblings (' + (t.sibling_count||0) + ')</h2><div class="grid">';
      (t.siblings||[]).forEach(s => {{
        html += '<div class="card"><span class="tag">' + esc(s.kind) + '</span><h3>' + esc(s.name) + '</h3></div>';
      }});
      html += '</div></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('stats').textContent = 'siblings ' + (t.sibling_count||0);
    }}

    function renderStudySplit() {{
      document.getElementById('net').classList.remove('hide');
      document.getElementById('panel').classList.add('show');
      document.getElementById('panel').style.cssText =
        'position:absolute;left:0;top:0;width:360px;bottom:0;overflow:auto;padding:14px;background:#0d141c;border-right:1px solid var(--line);z-index:3;';
      document.getElementById('net').style.left = '360px';
      let html = '<div class="section"><h2>STUDY</h2><table><tr><th>id</th><th>ANSWER</th></tr>';
      STATE.studies.forEach(s => {{
        const ans = s.answered ? '<span class="ok">filled</span>' : '<span class="wait">empty</span>';
        html += '<tr><td><code>' + esc(s.id) + '</code></td><td>' + ans + '</td></tr>';
        if (s.probe) html += '<tr><td colspan="2" style="color:var(--muted);font-size:11px">' + esc(s.probe) + '</td></tr>';
      }});
      html += '</table></div>';
      document.getElementById('panel').innerHTML = html;
      renderGraph({{ keepPanel: true }});
      document.getElementById('stats').textContent =
        'empty ANSWER ' + STATE.studies.filter(s => !s.answered).length +
        ' / ' + STATE.studies.length + ' · ' + document.getElementById('stats').textContent;
    }}

    function render() {{
      const meta = PURPOSES.find(p => p.id === purpose) || PURPOSES[0];
      document.getElementById('title').textContent = meta.label;
      document.getElementById('hint').textContent = meta.hint;
      clearStudyLayout();
      const panels = {{
        today: renderToday, train: renderTrain, routine: renderRoutine,
        project: renderProject, self: renderSelf, schedule: renderSchedule, cron: renderCron,
        inflow: renderInflow, runtime: renderRuntime, skills: renderSkills,
        mezzanine: renderMezzanine, tmp: renderTmp, study: renderStudySplit, weights: renderWeights,
        'lang-skilltree': renderLangSkilltree
      }};
      if (panels[purpose]) panels[purpose]();
      else {{
        document.getElementById('panel').classList.remove('show');
        document.getElementById('net').classList.remove('hide');
        // first paint of a graph purpose: prefer branch clusters when large
        const n = filterGraph().verts.length;
        if (String(purpose).startsWith('lang-')) {{
          GRAPH_UI.groupBy = 'kind';
          GRAPH_UI.clustered = false;
          if (purpose === 'lang-polyglot' || purpose === 'lang-wortschatz') {{
            GRAPH_UI.filters = 'structure';
          }}
        }} else if (GRAPH_UI.groupBy === 'branch' && GRAPH_UI.filters === null) {{
          GRAPH_UI.clustered = n > 28;
        }}
        renderGraph();
      }}
    }}

    function renderLangSkilltree() {{
      const H = (STATE.language && STATE.language.horizon) || {{ langs: [] }};
      const bands = {{}};
      (H.langs || []).forEach(L => {{
        const b = L.band || 'unknown';
        if (!bands[b]) bands[b] = [];
        bands[b].push(L);
      }});
      let html = '<div class="section"><h2>Polyglot skill tree</h2>' +
        '<p class="legend">Horizon: ' + esc(H.want || 'B2+') +
        ' · age target ' + esc(String(H.age_target || '')) +
        ' · ' + esc(String(H.count || (H.langs||[]).length)) + ' langs · graph below = Band → Lang</p>';
      Object.keys(bands).sort().forEach(b => {{
        html += '<div class="card" style="margin-bottom:10px"><h3>' + esc(b) +
          '</h3><p>' + bands[b].map(L => '<code>' + esc(L.code) + '</code> ' + esc(L.name)).join(' · ') +
          '</p></div>';
      }});
      html += '<p class="legend">Stores: bridge.graph · lexicon.graph · frames/de · horizon.toon — not universe.graph</p></div>';
      document.getElementById('panel').innerHTML = html;
      document.getElementById('panel').classList.add('show');
      document.getElementById('net').classList.remove('hide');
      document.getElementById('stats').textContent =
        'skilltree ' + ((H.langs||[]).length) + ' langs · targetLang ' +
        esc((STATE.language && STATE.language.targetLang) || 'de');
      // split: keep a short panel strip; graph still visible underneath via absolute net
      // panel overlays — shrink panel to top strip via inline style
      document.getElementById('panel').style.maxHeight = '42%';
      document.getElementById('panel').style.background = 'rgba(10,14,20,.92)';
      document.getElementById('panel').style.zIndex = '4';
      renderGraph({{ keepPanel: true }});
    }}

    function clearLangPanelChrome() {{
      const p = document.getElementById('panel');
      if (!p) return;
      p.style.maxHeight = '';
      p.style.background = '';
      p.style.zIndex = '';
    }}

    render();
  </script>
</body>
</html>
"""
    import importlib.util

    _fr = Path(__file__).resolve().parent / "fu_render.py"
    _spec = importlib.util.spec_from_file_location("fu_render", _fr)
    fu_render = importlib.util.module_from_spec(_spec)
    assert _spec and _spec.loader
    _spec.loader.exec_module(fu_render)
    html = html.replace("__FU_CSS__", fu_render.FU_CSS)
    path.write_text(html, encoding="utf-8")


def stamp_ttl() -> None:
    import subprocess

    subprocess.run(
        [sys.executable, str(ROOT / "cron" / "janitor.py"), "--touch"],
        check=False,
    )


def _safe_body_path(rel: str) -> Path | None:
    if not rel or ".." in rel.replace("\\", "/"):
        return None
    rel = rel.replace("\\", "/").lstrip("/")
    if not rel.startswith("pedagogy/"):
        return None
    path = (ROOT / rel).resolve()
    try:
        path.relative_to((ROOT / "pedagogy").resolve())
    except ValueError:
        return None
    return path if path.suffix == ".md" else None


def _safe_inflow_file(name: str) -> Path | None:
    name = (name or "").replace("\\", "/").strip().lstrip("/")
    if not name or "/" in name or ".." in name:
        return None
    if not (name.endswith(".md") or name.endswith(".fu.md")):
        return None
    path = (ROOT / "inflow" / name).resolve()
    try:
        path.relative_to((ROOT / "inflow").resolve())
    except ValueError:
        return None
    return path if path.is_file() else None


def _parse_notes_text(text: str) -> dict[str, dict]:
    nodes: dict[str, dict] = {}
    cur = None
    for line in text.splitlines():
        if line.startswith("node:"):
            cur = {}
            continue
        if cur is None:
            continue
        if re.match(r"^  id:", line):
            cur["id"] = line.split(":", 1)[1].strip()
            nodes[cur["id"]] = cur
        elif re.match(r"^  grasp:", line):
            cur["grasp"] = line.split(":", 1)[1].strip()
        elif re.match(r"^  note:", line):
            cur["note"] = line.split(":", 1)[1].strip()
        elif re.match(r"^  updated:", line):
            cur["updated"] = line.split(":", 1)[1].strip()
        elif re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            cur = None
    return nodes


def _load_notes() -> dict[str, dict]:
    durable = _parse_notes_text(read(NOTES_STORE))
    cache = _parse_notes_text(read(NOTES))
    nodes = dict(durable)
    for nid, row in cache.items():
        old = nodes.get(nid) or {}
        if (row.get("updated") or "") >= (old.get("updated") or ""):
            nodes[nid] = row
    return nodes


def _save_notes(nodes: dict[str, dict]) -> None:
    NOTES.parent.mkdir(parents=True, exist_ok=True)
    NOTES_STORE.parent.mkdir(parents=True, exist_ok=True)
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "schema: learn/vertex-notes",
        "note: Learner RECALL drafts. Lasting copy is pedagogy/_learn/learner-notes.toon.md. tmp is cache. Not STUDY ANSWER. Not CLAIM. Do not invent.",
        f"updated: {updated}",
    ]
    for nid in sorted(nodes):
        n = nodes[nid]
        note = (n.get("note") or "").replace("\n", " ").strip()
        lines.append("node:")
        lines.append(f"  id: {nid}")
        lines.append(f"  grasp: {n.get('grasp') or 'unknown'}")
        lines.append(f"  note: {note}")
        lines.append(f"  updated: {n.get('updated') or updated}")
    body = "\n".join(lines) + "\n"
    NOTES.write_text(body, encoding="utf-8")
    NOTES_STORE.write_text(body, encoding="utf-8")


def _parse_inflow_takes_text(text: str) -> dict[str, dict]:
    nodes: dict[str, dict] = {}
    cur = None
    for line in text.splitlines():
        if line.startswith("take:"):
            cur = {}
            continue
        if cur is None:
            continue
        if re.match(r"^  id:", line):
            cur["id"] = line.split(":", 1)[1].strip()
            nodes[cur["id"]] = cur
        elif re.match(r"^  stance:", line):
            cur["stance"] = line.split(":", 1)[1].strip()
        elif re.match(r"^  note:", line):
            cur["note"] = line.split(":", 1)[1].strip()
        elif re.match(r"^  updated:", line):
            cur["updated"] = line.split(":", 1)[1].strip()
        elif re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            cur = None
    return nodes


def _load_inflow_takes() -> dict[str, dict]:
    """Durable store wins the id; tmp overlay if its updated stamp is newer."""
    durable = _parse_inflow_takes_text(read(INFLOW_TAKES_STORE))
    cache = _parse_inflow_takes_text(read(INFLOW_TAKES))
    nodes = dict(durable)
    for nid, row in cache.items():
        old = nodes.get(nid) or {}
        if (row.get("updated") or "") >= (old.get("updated") or ""):
            nodes[nid] = row
    return nodes


def _inflow_takes_lines(nodes: dict[str, dict], updated: str) -> list[str]:
    lines = [
        "schema: inflow/human-takes",
        "note: Human opinions on DUMP/NEWS items. Lasting copy is inflow/takes.toon.md. tmp is cache. Not drip. Not CLAIM. Not STUDY ANSWER.",
        f"updated: {updated}",
    ]
    for nid in sorted(nodes):
        n = nodes[nid]
        note = (n.get("note") or "").replace("\n", " ").strip()
        lines.append("take:")
        lines.append(f"  id: {nid}")
        lines.append(f"  stance: {n.get('stance') or 'unknown'}")
        lines.append(f"  note: {note}")
        lines.append(f"  updated: {n.get('updated') or updated}")
    return lines


def _save_inflow_takes(nodes: dict[str, dict]) -> None:
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    body = "\n".join(_inflow_takes_lines(nodes, updated)) + "\n"
    INFLOW_TAKES.parent.mkdir(parents=True, exist_ok=True)
    INFLOW_TAKES_STORE.parent.mkdir(parents=True, exist_ok=True)
    INFLOW_TAKES.write_text(body, encoding="utf-8")
    INFLOW_TAKES_STORE.write_text(body, encoding="utf-8")


def _inflow_index() -> dict[str, dict]:
    dump_text = read(ROOT / "inflow" / "DUMP.md")
    by_id: dict[str, dict] = {}
    for d in parse_dump_section(dump_text, "PENDING") + parse_dump_section(
        dump_text, "HUMAN OPEN"
    ):
        by_id[d["id"]] = d
    for n in parse_inflow_news(read(ROOT / "inflow" / "inflow.fu.md"), limit=200):
        by_id[n["id"]] = n
    return by_id


def _vertex_index() -> dict[str, dict]:
    """Fresh parse so --serve stays in sync after graph/HTML regenerates."""
    verts, _ = parse_graph(ROOT / "pedagogy" / "universe.graph.md")
    return {v["id"]: v for v in verts}


def serve(path: Path, open_browser: bool, host: str = "127.0.0.1", rebuild=None) -> int:
    import importlib.util

    _fr = Path(__file__).resolve().parent / "fu_render.py"
    _spec = importlib.util.spec_from_file_location("fu_render", _fr)
    fu_render = importlib.util.module_from_spec(_spec)
    assert _spec and _spec.loader
    _spec.loader.exec_module(fu_render)
    render_fu_file = fu_render.render_fu_file

    class Handler(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"

        def log_message(self, fmt, *args):
            sys.stderr.write("STATE " + (fmt % args) + "\n")

        def _json(self, code: int, payload: dict) -> None:
            raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("content-type", "application/json; charset=utf-8")
            self.send_header("cache-control", "no-store")
            self.send_header("content-length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def _bytes(self, code: int, raw: bytes, ctype: str) -> None:
            self.send_response(code)
            self.send_header("content-type", ctype)
            self.send_header("cache-control", "no-store")
            self.send_header("content-length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self) -> None:
            from urllib.parse import parse_qs, unquote, urlparse

            u = urlparse(self.path)
            pth = unquote(u.path)
            if pth in {"/", "/index.html", "/project-state.html"}:
                if rebuild:
                    try:
                        rebuild()
                    except Exception as exc:
                        sys.stderr.write(f"STATE rebuild failed: {exc}\n")
                self._bytes(200, path.read_bytes(), "text/html; charset=utf-8")
                return
            if pth.startswith("/api/vertex/"):
                vid = pth[len("/api/vertex/") :]
                v = _vertex_index().get(vid)
                if not v:
                    self._json(404, {"ok": False, "error": "unknown vertex"})
                    return
                body = v.get("body") or ""
                bp = _safe_body_path(body)
                if not bp or not bp.is_file():
                    self._json(
                        404,
                        {
                            "ok": False,
                            "error": "body missing" if bp else "no body path",
                            "body": body,
                        },
                    )
                    return
                rendered = render_fu_file(bp)
                notes = _load_notes()
                rendered["note"] = notes.get(vid)
                rendered["id"] = vid
                rendered["gloss"] = v.get("gloss", "")
                rendered["kind"] = v.get("kind", "")
                self._json(200, rendered)
                return
            if pth.startswith("/api/inflow/item/"):
                iid = pth[len("/api/inflow/item/") :]
                item = _inflow_index().get(iid)
                if not item:
                    self._json(404, {"ok": False, "error": "unknown inflow id"})
                    return
                takes = _load_inflow_takes()
                self._json(200, {"ok": True, "item": item, "take": takes.get(iid)})
                return
            if pth == "/api/inflow/file":
                qs = parse_qs(u.query or "")
                name = (qs.get("name") or [""])[0]
                fp = _safe_inflow_file(name)
                if not fp:
                    self._json(404, {"ok": False, "error": "bad inflow file"})
                    return
                try:
                    text = fp.read_text(encoding="utf-8")
                except OSError as exc:
                    self._json(500, {"ok": False, "error": str(exc)})
                    return
                if len(text) > 200_000:
                    text = text[:200_000] + "\n… truncated …\n"
                takes = _load_inflow_takes()
                self._json(
                    200,
                    {
                        "ok": True,
                        "name": name,
                        "path": f"inflow/{name}",
                        "text": text,
                        "take": takes.get(f"file:{name}"),
                    },
                )
                return
            if pth == "/api/notes":
                self._json(200, {"ok": True, "nodes": _load_notes()})
                return
            self.send_error(404)

        def do_POST(self) -> None:
            from urllib.parse import urlparse

            pth = urlparse(self.path).path
            n = int(self.headers.get("content-length") or "0")
            raw = self.rfile.read(n) if n else b"{}"
            try:
                body = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                self._json(400, {"ok": False, "error": "bad json"})
                return
            if pth == "/api/inflow/take":
                iid = str(body.get("id") or "").strip()
                if not iid or len(iid) > 160:
                    self._json(400, {"ok": False, "error": "bad id"})
                    return
                # allow capture ids or file:Name.md
                if iid.startswith("file:"):
                    if not _safe_inflow_file(iid[5:]):
                        self._json(400, {"ok": False, "error": "unknown file"})
                        return
                elif iid not in _inflow_index():
                    self._json(400, {"ok": False, "error": "unknown inflow id"})
                    return
                stance = str(body.get("stance") or "unknown").strip()
                if stance not in {"unknown", "weak", "partial", "firm"}:
                    stance = "unknown"
                note = str(body.get("note") or "").strip()[:2000]
                nodes = _load_inflow_takes()
                updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                nodes[iid] = {
                    "id": iid,
                    "stance": stance,
                    "note": note,
                    "updated": updated,
                }
                _save_inflow_takes(nodes)
                stamp_ttl()
                self._json(
                    200,
                    {
                        "ok": True,
                        "id": iid,
                        "updated": updated,
                        "path": INFLOW_TAKES_STORE.as_posix(),
                        "cache": INFLOW_TAKES.as_posix(),
                    },
                )
                return
            if pth != "/api/note":
                self.send_error(404)
                return
            vid = str(body.get("id") or "").strip()
            if vid not in _vertex_index():
                self._json(400, {"ok": False, "error": "unknown vertex"})
                return
            grasp = str(body.get("grasp") or "unknown").strip()
            if grasp not in {"unknown", "weak", "partial", "firm"}:
                grasp = "unknown"
            note = str(body.get("note") or "").strip()[:2000]
            nodes = _load_notes()
            updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            nodes[vid] = {"id": vid, "grasp": grasp, "note": note, "updated": updated}
            _save_notes(nodes)
            stamp_ttl()
            self._json(
                200,
                {
                    "ok": True,
                    "id": vid,
                    "updated": updated,
                    "path": NOTES_STORE.as_posix(),
                    "cache": NOTES.as_posix(),
                },
            )

    class Server(socketserver.TCPServer):
        allow_reuse_address = True

    last_err = None
    httpd = None
    port = 8780
    for try_port in (8780, 8781, 8782, 8790):
        try:
            httpd = Server((host, try_port), Handler)
            port = try_port
            break
        except OSError as exc:
            last_err = exc
            httpd = None
    if httpd is None:
        print(f"No free port: {last_err}", file=sys.stderr)
        return 1
    url = f"http://{host}:{port}/project-state.html"
    print(f"SERVE {url}", flush=True)
    print(f"SERVE notes {NOTES}", flush=True)
    print(f"SERVE inflow-takes {INFLOW_TAKES_STORE} cache {INFLOW_TAKES}", flush=True)
    print(
        "SERVE ontology drawer + inflow digest · POST /api/note · POST /api/inflow/take",
        flush=True,
    )
    if open_browser:
        webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nSTOP")
        return 0
    return 0


PURPOSE_CHOICES = [
    "today",
    "train",
    "routine",
    "project",
    "self",
    "schedule",
    "cron",
    "inflow",
    "runtime",
    "study",
    "weights",
    "hire",
    "ontology",
    "core",
    "stack",
    "lang-polyglot",
    "lang-wortschatz",
    "lang-grammar",
    "lang-skilltree",
    "skills",
    "mezzanine",
    "tmp",
]


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--purpose", default="today", choices=PURPOSE_CHOICES)
    p.add_argument("--serve", action="store_true")
    p.add_argument("--host", default="127.0.0.1", help="bind for --serve (0.0.0.0 for LAN/phone)")
    p.add_argument("--no-open", action="store_true")
    p.add_argument("--out", type=Path, default=OUT)
    args = p.parse_args()
    state = collect_state()
    write_html(state, args.out, args.purpose)
    stamp_ttl()
    print(f"DELIVERED {args.out}")
    print(
        f"V{state['graph']['v_count']} E{state['graph']['e_count']} "
        f"self={len(state['self']['files'])} cron={len(state['cron']['jobs'])} "
        f"harvest={len(state['schedule']['harvest'])} inflow_news={len(state['inflow']['news'])} "
        f"purpose={args.purpose}"
    )
    if args.serve:
        def _rebuild() -> None:
            st = collect_state()
            write_html(st, args.out, args.purpose)

        return serve(
            args.out,
            open_browser=not args.no_open,
            host=args.host,
            rebuild=_rebuild,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
