#!/usr/bin/env python3
"""sessionStart: inject WritingAccuracy + PolyglotHorizon + grammar×lexicon pairing."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "state.toon.md"
METHOD = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "method.toon.md"
PAIRING = ROOT / "pedagogy" / "_learn" / "polyglot" / "pairing.toon.md"
HORIZON = ROOT / "pedagogy" / "_learn" / "polyglot" / "horizon.toon.md"
SIGNAL = ROOT / "pedagogy" / "_learn" / "polyglot" / "last-signal.toon.md"
FRAMES = ROOT / "pedagogy" / "_learn" / "polyglot" / "frames" / "de.toon.md"


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def parse_focus(text: str) -> list[str]:
    lines = text.splitlines()
    out: list[str] = []
    in_block = False
    for line in lines:
        if line.startswith("todayFocus"):
            in_block = True
            continue
        if in_block:
            if not line.strip():
                break
            if re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
                break
            item = line.strip().lstrip("-").strip()
            if item and not item.startswith("#"):
                if re.match(r"^\d+,", item):
                    item = item.split(",", 1)[-1].strip()
                out.append(item)
    return out[:6]


def parse_field(text: str, key: str) -> str:
    for line in text.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return ""


def main() -> int:
    try:
        raw_in = sys.stdin.buffer.read().decode("utf-8")
        if raw_in.strip():
            json.loads(raw_in)
    except Exception:
        pass

    state = _read(STATE)
    if "status: active" not in state:
        print("{}")
        return 0

    focus = parse_focus(state)
    one = parse_field(state, "oneFocus") or (focus[0] if focus else "")
    reuse = parse_field(state, "reuseNextSession")
    target = parse_field(state, "targetLang") or "de"
    age_t = parse_field(_read(HORIZON), "age_target") or "35"
    count = parse_field(_read(HORIZON), "count") or "16"

    bullets = "\n".join(f"  - {f}" for f in focus) if focus else "  - (no todayFocus yet)"
    last_p = parse_field(_read(SIGNAL), "primaryLang")
    last_hit = parse_field(_read(SIGNAL), "methodHit")
    ctx = (
        "<writing_accuracy_arbitrage>\n"
        f"Method: writing-accuracy-base-arbitrage · targetLang={target}\n"
        f"Horizon: B2+ in {count} languages by age {age_t}. Do not invent unnamed language names.\n"
        f"last-signal: primaryLang={last_p or 'none'} methodHit={last_hit or 'unknown'} "
        f"({SIGNAL.as_posix()}). Empty tokenCount must not reset this to en.\n"
        "Hook flow: beforeSubmitPrompt runs polyglot_detect.analyze. If methodHit "
        "(DE/FR/ES markers ≥2), this turn is a writing sample even after a ZH stretch. "
        "Auto-writes GAP vertices into bridge.graph.md.\n"
        "After minimal rewrite: write sessions/*.toon.md then run "
        "python pedagogy/_learn/writing-accuracy/ingest_session.py --session <file> "
        "so Forms attach. Do not wait to be asked.\n"
        "Grammar×lexicon: Frame owns slots; Lemma/Form fills slots; Chunk = filled Frame; "
        f"oneFocus = one Frame. See {PAIRING.as_posix()} and {FRAMES.as_posix()}.\n"
        "Rule: project job first. Minimal rewrite + one Frame focus. Not a grammar teacher. "
        "Do not edit product code for language logging.\n"
        f"oneFocus: {one}\n"
        "todayFocus:\n"
        f"{bullets}\n"
    )
    if reuse:
        ctx += f"reuseNextSession scaffold: {reuse}\n"
    ctx += (
        f"Stores: {STATE.as_posix()} · {METHOD.as_posix()} · "
        "pedagogy/_learn/writing-accuracy/lexicon.graph.md · "
        "pedagogy/_learn/polyglot/bridge.graph.md\n"
        "</writing_accuracy_arbitrage>"
    )

    payload = {
        "env": {
            "WRITING_ACCURACY_TARGET": target,
            "WRITING_ACCURACY_ONE_FOCUS": one[:200],
            "POLYGLOT_HORIZON_AGE": age_t,
            "POLYGLOT_LANG_COUNT": count,
        },
        "additional_context": ctx,
    }
    print(json.dumps(payload, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        print("{}")
        raise SystemExit(0)
