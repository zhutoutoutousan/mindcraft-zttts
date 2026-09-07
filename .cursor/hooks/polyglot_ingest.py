#!/usr/bin/env python3
"""Internalize writing-accuracy gaps/sessions into the language knowledge graph."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BRIDGE = ROOT / "pedagogy" / "_learn" / "polyglot" / "bridge.graph.md"
LEXICON = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "lexicon.graph.md"
PENDING = ROOT / "pedagogy" / "_learn" / "polyglot" / "pending-ingest.toon.md"


def slug(s: str, max_len: int = 40) -> str:
    """ASCII-safe graph id fragment; hash when any non-ASCII (CJK etc.)."""
    import hashlib

    raw = s.strip()
    ascii_part = re.sub(r"[^a-z0-9]+", "_", raw.lower())
    ascii_part = re.sub(r"_+", "_", ascii_part).strip("_")
    if any(ord(c) > 127 for c in raw):
        h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
        if ascii_part:
            return f"{ascii_part}_{h}"[:max_len]
        return f"u{h}"[:max_len]
    return (ascii_part or "x")[:max_len]


def graph_prop(s: str, max_len: int = 80) -> str:
    """Value for V/E property; quote when spaces so the viz parser keeps the words."""
    s = s.strip().replace("\n", " ").replace('"', "'")[:max_len]
    if not s:
        return "empty"
    if re.search(r"[\s=]", s):
        return '"' + s + '"'
    return s


def surface_prop(s: str, max_len: int = 80) -> str:
    return graph_prop(s, max_len)


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def _append(path: Path, block: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    cur = _read(path)
    first = next((ln for ln in block.splitlines() if ln.startswith("V ")), "")
    if first:
        vid = first.split()[1]
        if re.search(rf"^V\s+{re.escape(vid)}\s", cur, re.M):
            return False
    with path.open("a", encoding="utf-8") as f:
        if cur and not cur.endswith("\n"):
            f.write("\n")
        f.write("\n" + block.rstrip() + "\n")
    return True


def upsert_code_switch_gaps(
    gaps: list[dict],
    *,
    target: str,
    source: str,
    stamp: str | None = None,
) -> list[str]:
    """Write open GAP vertices into bridge.graph.md. Returns new ids."""
    stamp = stamp or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    added: list[str] = []
    for g in gaps:
        surface = str(g.get("surface") or "").strip()
        from_lang = str(g.get("fromLang") or "x")
        if not surface:
            continue
        sid = slug(f"{from_lang}_{surface}")
        gap_id = f"Gap_{sid}"
        concept_id = f"Concept_gap_{sid}"
        lemma_id = f"Lemma_{from_lang}_{sid}"
        surf = surface_prop(surface)
        block = "\n".join(
            [
                f"# auto-gap {stamp} surface={surf}",
                f"V {concept_id} kind=concept gloss=unknown-expression-in-{target} status=open",
                f"V {gap_id} kind=gap lang={from_lang} surface={surf} target={target} status=open",
                f"V {lemma_id} kind=lemma lang={from_lang} surface={surf}",
                f"E {concept_id} EXPRESSES {lemma_id} SOURCE={source}",
                f"E {lemma_id} GAP_IN {target} SOURCE={source}",
                f"E {concept_id} GAP_IN {target} SOURCE={source}",
            ]
        )
        if _append(BRIDGE, block):
            added.append(gap_id)
    if added:
        PENDING.write_text(
            "\n".join(
                [
                    "schema: learn/polyglot-pending-ingest",
                    f"updated: {stamp}",
                    f"targetLang: {target}",
                    "openGaps:",
                    *[f"  - {g}" for g in added],
                    "note: Hook auto-wrote GAP vertices. After minimal rewrite, ingest the session to attach target Forms.",
                ]
            )
            + "\n",
            encoding="utf-8",
        )
    return added


def ingest_session_file(session_path: Path) -> dict:
    """Append session + corrected forms into lexicon.graph.md and bridge.graph.md."""
    text = _read(session_path)
    if not text:
        return {"ok": False, "error": "empty session"}

    def field(key: str) -> str:
        for line in text.splitlines():
            if line.startswith(f"{key}:"):
                return line.split(":", 1)[1].strip()
        return ""

    date = field("date") or "unknown"
    sid = field("id") or session_path.stem
    corrected = field("corrected")
    one_focus = field("oneFocus")
    lang = field("lang") or "de"
    # allow meta: block style sourceLang via simple scan
    if lang == "de":
        for line in text.splitlines():
            if "sourceLang:" in line:
                lang = line.split("sourceLang:", 1)[1].strip().split()[0] or lang
                break
    lang = re.sub(r"[^a-z]", "", lang.lower())[:8] or "de"
    session_id = f"Session_{slug(sid)}"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rel = session_path.resolve().as_posix()
    if "/pedagogy/" in rel:
        rel = "pedagogy/" + rel.split("/pedagogy/", 1)[-1]
    rel_prop = rel.replace(" ", "_")

    _append(
        LEXICON,
        "\n".join(
            [
                f"# ingest-session {stamp} {sid} lang={lang}",
                f"V {session_id} kind=session date={date} lang={lang} body={rel_prop}",
                f"V Sent_{slug(sid)}_raw kind=sentence date={date} lang={lang} role=raw",
                f"V Sent_{slug(sid)}_fix kind=sentence date={date} lang={lang} role=corrected",
                f"E Sent_{slug(sid)}_fix FIXES Sent_{slug(sid)}_raw",
                f"E Sent_{slug(sid)}_raw FROM_SESSION {session_id}",
                f"E Sent_{slug(sid)}_fix FROM_SESSION {session_id}",
            ]
        ),
    )

    briefs: list[str] = []
    in_brief = False
    for line in text.splitlines():
        if line.startswith("errors_brief") or line.startswith("errors["):
            in_brief = True
            continue
        if in_brief:
            if not line.strip() or (
                re.match(r"^[a-zA-Z_]", line) and not line.startswith(" ")
            ):
                break
            item = line.strip().lstrip("-").strip()
            if re.match(r"^\d+,", item):
                item = item.split(",", 1)[-1].strip()
            if item:
                briefs.append(item)

    bridge_lines = [
        f"# ingest-session {stamp} {sid} lang={lang}",
        f"V {session_id} kind=session date={date} lang={lang} body={rel_prop}",
    ]
    if one_focus:
        bridge_lines.append(
            f"V Focus_{slug(sid)} kind=focus lang={lang} gloss={graph_prop(one_focus, 50)} status=active"
        )
        bridge_lines.append(f"E Focus_{slug(sid)} FROM_SESSION {session_id}")
    if corrected:
        bridge_lines.append(
            f"V Lemma_{lang}_fix_{slug(sid)} kind=lemma lang={lang} "
            f"surface={surface_prop(corrected, 50)} role=minimal-rewrite"
        )
        bridge_lines.append(
            f"E Lemma_{lang}_fix_{slug(sid)} FROM_SESSION {session_id} SOURCE={rel_prop}"
        )
    for i, b in enumerate(briefs[:8]):
        m = re.split(r"\s*→\s*|\s*->\s*", b, maxsplit=1)
        if len(m) != 2:
            continue
        wrong, right = m[0].strip(), m[1].strip()
        right_main = right.split("(")[0].strip()
        wid = slug(f"fix_{sid}_{i}_{right_main}")
        bridge_lines.append(
            f"V Form_{wid} kind=form lang={lang} surface={surface_prop(right_main, 40)} "
            f"fixes={surface_prop(wrong, 30)}"
        )
        bridge_lines.append(f"E Form_{wid} FROM_SESSION {session_id}")
    _append(BRIDGE, "\n".join(bridge_lines))

    if PENDING.exists():
        try:
            PENDING.unlink()
        except OSError:
            pass

    return {
        "ok": True,
        "session": session_id,
        "lang": lang,
        "briefs": len(briefs),
        "lexicon": str(LEXICON),
        "bridge": str(BRIDGE),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--session", type=Path, help="session .toon.md to ingest")
    p.add_argument("--gaps-json", type=str, default="", help="JSON list of gaps")
    p.add_argument("--target", default="de")
    p.add_argument("--source", default="hook/auto")
    args = p.parse_args()
    if args.gaps_json:
        gaps = json.loads(args.gaps_json)
        added = upsert_code_switch_gaps(gaps, target=args.target, source=args.source)
        print(json.dumps({"added": added}, ensure_ascii=True))
        return 0
    if args.session:
        print(json.dumps(ingest_session_file(args.session.resolve()), ensure_ascii=True))
        return 0
    p.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
