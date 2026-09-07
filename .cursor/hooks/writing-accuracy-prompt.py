#!/usr/bin/env python3
"""beforeSubmitPrompt: detect primary lang + code-switch gaps; INTERNALIZE gaps into bridge.graph.md."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from polyglot_detect import analyze  # noqa: E402
from polyglot_ingest import upsert_code_switch_gaps  # noqa: E402

STATE = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "state.toon.md"
SIGNAL = ROOT / "pedagogy" / "_learn" / "polyglot" / "last-signal.toon.md"


def parse_field(text: str, key: str) -> str:
    for line in text.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return ""


def main() -> int:
    try:
        raw_bytes = sys.stdin.buffer.read()
        raw = raw_bytes.decode("utf-8")
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}

    prompt = str(data.get("prompt") or "")
    try:
        state = STATE.read_text(encoding="utf-8")
    except OSError:
        state = ""
    target = parse_field(state, "targetLang") or "de"
    if "status: active" not in state:
        print(json.dumps({"continue": True}))
        return 0

    result = analyze(prompt, target=target)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if result["tokenCount"] == 0:
        # Empty stdin (image-only / control) must not clobber last-signal to en/0.
        print(json.dumps({"continue": True}))
        return 0

    added: list[str] = []
    if result["gaps"]:
        added = upsert_code_switch_gaps(
            result["gaps"],
            target=target,
            source="hook/beforeSubmitPrompt",
            stamp=now,
        )

    lines = [
        "schema: learn/polyglot-last-signal",
        f"updated: {now}",
        f"primaryLang: {result['primaryLang']}",
        f"targetLang: {result['targetLang']}",
        f"tokenCount: {result['tokenCount']}",
        f"mix: {str(result['mix']).lower()}",
        f"methodHit: {str(result.get('methodHit', False)).lower()}",
        f"scores: {json.dumps(result['scores'], ensure_ascii=True)}",
        f"graphUpserted: {json.dumps(added, ensure_ascii=True)}",
        "gaps:",
    ]
    if result["gaps"]:
        for g in result["gaps"]:
            lines.append(
                f"  - surface: {g['surface']} | from: {g['fromLang']} | "
                f"kind: {g['kind']} | treatAs: unknown-expression-in-{g['targetLang']} | internalized: gap-vertex"
            )
    else:
        lines.append("  - (none)")
    lines.append(
        "agentRule: Job first. Gaps are already in pedagogy/_learn/polyglot/bridge.graph.md. "
        "After minimal rewrite, write sessions/*.toon.md and run "
        "python pedagogy/_learn/writing-accuracy/ingest_session.py --session <file> "
        "so Forms attach to the language KG. Do not wait to be asked. "
        "If methodHit: this utterance IS a target-lang sample even after a ZH stretch."
    )
    lines.append("pairing: pedagogy/_learn/polyglot/pairing.toon.md")
    try:
        SIGNAL.parent.mkdir(parents=True, exist_ok=True)
        SIGNAL.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        pass

    out: dict = {"continue": True}
    if result.get("methodHit"):
        out["additional_context"] = (
            "<writing_accuracy_this_turn>\n"
            f"polyglot_detect methodHit=true primary={result['primaryLang']} "
            f"target={result['targetLang']} tokens={result['tokenCount']}\n"
            "This chatbox turn is a writing-accuracy sample. Job first, then minimal "
            "rewrite in the reply + ingest_session.py. A prior ZH stretch does not skip this.\n"
            "</writing_accuracy_this_turn>"
        )
    if result["mix"] and result["gaps"]:
        surfaces = ", ".join(g["surface"] for g in result["gaps"][:5])
        out["user_message"] = (
            f"Language KG: primary={result['primaryLang']} → gaps [{surfaces}] "
            f"written into bridge.graph.md ({len(added)} new). "
            "Forms attach after session ingest."
        )
    print(json.dumps(out, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({"continue": True}))
        raise SystemExit(0)
