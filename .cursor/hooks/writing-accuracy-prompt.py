#!/usr/bin/env python3
"""beforeSubmitPrompt: detect primary lang + code-switch gaps; INTERNALIZE gaps into bridge.graph.md.

Cursor docs: this event's stdout only supports continue + user_message (shown when blocked).
It cannot print a Korrektur. last-signal is the agent-visible store. additional_context
on this event is not in the documented schema and must not be the only channel.
Qoder's UserPromptSubmit reads hookSpecificOutput.additionalContext.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from polyglot_detect import analyze, extract_prompt  # noqa: E402
from polyglot_ingest import upsert_code_switch_gaps  # noqa: E402

STATE = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "state.toon.md"
SIGNAL = ROOT / "pedagogy" / "_learn" / "polyglot" / "last-signal.toon.md"
TRACE = ROOT / "pedagogy" / "_learn" / "polyglot" / "hook-trace.toon.md"


def parse_field(text: str, key: str) -> str:
    for line in text.splitlines():
        if line.startswith(f"{key}:"):
            return line.split(":", 1)[1].strip()
    return ""


def write_trace(
    *,
    keys: list[str],
    prompt_chars: int,
    error: str,
    skipped: str,
    stdin_bytes: int = 0,
    decode: str = "",
    json_mode: str = "",
) -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "schema: learn/polyglot-hook-trace",
        f"updated: {now}",
        "event: beforeSubmitPrompt",
        f"stdinBytes: {stdin_bytes}",
        f"decode: {decode or 'n/a'}",
        f"jsonMode: {json_mode or 'n/a'}",
        f"stdinKeys: {','.join(keys) if keys else '(none)'}",
        f"promptChars: {prompt_chars}",
        f"skipped: {skipped or 'no'}",
        f"error: {error or 'none'}",
        "note: No prompt body stored. json-parse used to skip last-signal; raw stdin is now the prompt fallback.",
    ]
    try:
        TRACE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except OSError:
        pass


def write_signal(result: dict, added: list[str], now: str) -> None:
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
        "If methodHit: this utterance IS a target-lang sample even after a ZH stretch. "
        "beforeSubmitPrompt cannot show a Korrektur in the UI (user_message only when blocked)."
    )
    lines.append("pairing: pedagogy/_learn/polyglot/pairing.toon.md")
    SIGNAL.parent.mkdir(parents=True, exist_ok=True)
    SIGNAL.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _win_pipe_available(fd: int) -> int:
    """Bytes waiting on a Windows pipe, or -1 if PeekNamedPipe fails."""
    import ctypes
    import msvcrt

    avail = ctypes.c_ulong(0)
    ok = ctypes.windll.kernel32.PeekNamedPipe(
        msvcrt.get_osfhandle(fd),
        None,
        0,
        None,
        ctypes.byref(avail),
        None,
    )
    return int(avail.value) if ok else -1


def read_hook_stdin(*, max_wait: float = 1.5) -> bytes:
    """Cursor may keep stdin open after the JSON. Do not wait for EOF."""
    import os

    fd = sys.stdin.fileno()
    buf = bytearray()

    def try_parse() -> bool:
        if not buf:
            return False
        try:
            json.loads(bytes(buf).decode("utf-8-sig", errors="replace").strip() or "{}")
            return True
        except json.JSONDecodeError:
            return False

    if os.name == "nt":
        peeked = _win_pipe_available(fd)
        if peeked < 0:
            return sys.stdin.buffer.read()
        deadline = time.monotonic() + max_wait
        idle = 0
        while time.monotonic() < deadline:
            avail = _win_pipe_available(fd)
            if avail > 0:
                idle = 0
                buf.extend(os.read(fd, avail))
                if try_parse():
                    return bytes(buf)
                continue
            if buf:
                idle += 1
                if idle >= 4:
                    break
            time.sleep(0.05)
        return bytes(buf)

    import select

    deadline = time.monotonic() + max_wait
    idle = 0
    while time.monotonic() < deadline:
        ready, _, _ = select.select([sys.stdin], [], [], 0.05)
        if ready:
            idle = 0
            chunk = os.read(fd, 65536)
            if not chunk:
                break
            buf.extend(chunk)
            if try_parse():
                return bytes(buf)
            continue
        if buf:
            idle += 1
            if idle >= 4:
                break
    return bytes(buf)


def decode_stdin(raw_bytes: bytes) -> tuple[str, str]:
    if not raw_bytes:
        return "", "empty"
    if raw_bytes.startswith(b"\xff\xfe") or raw_bytes.startswith(b"\xfe\xff"):
        return raw_bytes.decode("utf-16", errors="replace"), "utf-16"
    return raw_bytes.decode("utf-8-sig", errors="replace"), "utf-8"


def parse_payload(raw: str) -> tuple[dict, str]:
    """Cursor docs send {prompt, attachments}. Windows sometimes sends BOM, a wrapper, or raw text."""
    s = (raw or "").strip()
    if not s:
        return {}, "empty"
    try:
        obj = json.loads(s)
        if isinstance(obj, dict):
            return obj, "json"
        if isinstance(obj, str):
            return {"prompt": obj}, "json-string"
        return {"prompt": str(obj)}, "json-other"
    except json.JSONDecodeError:
        pass
    start = s.find("{")
    end = s.rfind("}")
    if start >= 0 and end > start:
        try:
            obj = json.loads(s[start : end + 1])
            if isinstance(obj, dict):
                return obj, "json-slice"
        except json.JSONDecodeError:
            pass
    return {"prompt": s}, "raw-text"


def main() -> int:
    keys: list[str] = []
    stdin_bytes = 0
    decode = "n/a"
    json_mode = "n/a"
    try:
        raw_bytes = read_hook_stdin()
        stdin_bytes = len(raw_bytes)
        raw, decode = decode_stdin(raw_bytes)
        data, json_mode = parse_payload(raw)
    except Exception as exc:
        write_trace(
            keys=[],
            prompt_chars=0,
            error=type(exc).__name__,
            skipped="stdin-read",
            stdin_bytes=stdin_bytes,
            decode=decode,
            json_mode=json_mode,
        )
        print(json.dumps({"continue": True}))
        return 0

    if isinstance(data, dict):
        keys = sorted(str(k) for k in data.keys())

    prompt = extract_prompt(data)
    try:
        state = STATE.read_text(encoding="utf-8")
    except OSError:
        state = ""
    target = parse_field(state, "targetLang") or "de"
    if "status: active" not in state:
        write_trace(
            keys=keys,
            prompt_chars=len(prompt),
            error="none",
            skipped="method-inactive",
            stdin_bytes=stdin_bytes,
            decode=decode,
            json_mode=json_mode,
        )
        print(json.dumps({"continue": True}))
        return 0

    result = analyze(prompt, target=target)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if result["tokenCount"] == 0:
        write_trace(
            keys=keys,
            prompt_chars=len(prompt),
            error="none",
            skipped="empty-prompt",
            stdin_bytes=stdin_bytes,
            decode=decode,
            json_mode=json_mode,
        )
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

    try:
        write_signal(result, added, now)
    except OSError as exc:
        write_trace(
            keys=keys,
            prompt_chars=len(prompt),
            error=type(exc).__name__,
            skipped="signal-write",
            stdin_bytes=stdin_bytes,
            decode=decode,
            json_mode=json_mode,
        )
        print(json.dumps({"continue": True}))
        return 0

    write_trace(
        keys=keys,
        prompt_chars=len(prompt),
        error="none",
        skipped="no",
        stdin_bytes=stdin_bytes,
        decode=decode,
        json_mode=json_mode,
    )

    out: dict = {"continue": True}
    if result.get("methodHit"):
        this_turn = (
            "<writing_accuracy_this_turn>\n"
            f"polyglot_detect methodHit=true primary={result['primaryLang']} "
            f"target={result['targetLang']} tokens={result['tokenCount']}\n"
            "This chatbox turn is a writing-accuracy sample. Job first, then minimal "
            "rewrite in the reply + ingest_session.py. A prior ZH stretch does not skip this. "
            "Do not wait for a hook toast. beforeSubmitPrompt cannot display a Korrektur.\n"
            "</writing_accuracy_this_turn>"
        )
        out["additional_context"] = this_turn
        # Qoder injects hookSpecificOutput.additionalContext; Cursor uses additional_context.
        out["hookSpecificOutput"] = {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": this_turn,
        }
    print(json.dumps(out, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        write_trace(
            keys=[],
            prompt_chars=0,
            error=type(exc).__name__,
            skipped="uncaught",
        )
        print(json.dumps({"continue": True}))
        raise SystemExit(0)
