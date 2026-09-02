#!/usr/bin/env python3
"""Skip-list for inflow news. The agent writes inflow/inflow.fu.md.

    python cron/inflow-news.py --status
    python cron/inflow-news.py --stamp --ids a,b,c
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "inflow" / "STATE.md"
NEWS = ROOT / "inflow" / "inflow.fu.md"


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_skip(text: str) -> list[str]:
    ids: list[str] = []
    in_skip = False
    for line in text.splitlines():
        if line.startswith("## Skip") or line.startswith("## Delivered"):
            in_skip = True
            continue
        if line.startswith("#") and not line.startswith("## Skip") and not line.startswith("## Delivered"):
            in_skip = False
            continue
        if in_skip and line.startswith("- "):
            payload = line[2:].strip()
            if payload:
                ids.append(payload)
    return ids


def load_skip() -> list[str]:
    if not STATE.exists():
        return []
    return parse_skip(STATE.read_text(encoding="utf-8"))


def stamp(ids: list[str]) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    prev = STATE.read_text(encoding="utf-8") if STATE.exists() else "# inflow STATE\n"
    have = set(load_skip())
    fresh = [i for i in ids if i and i not in have]
    loop_line = f"Loop: RUNNING 20m last_stamp {now_iso()}. Read inflow/inflow.fu.md. Skip ids below."
    seen_loop = False
    out: list[str] = []
    for line in prev.splitlines():
        if line.startswith("Loop:"):
            if seen_loop:
                continue
            out.append(loop_line)
            seen_loop = True
            continue
        out.append(line)
    if not seen_loop:
        if out and out[0].startswith("#"):
            out.insert(1, loop_line)
        else:
            out.insert(0, loop_line)
    body = "\n".join(out)
    if fresh:
        if not body.endswith("\n"):
            body += "\n"
        body += "\n".join(f"- {i}" for i in fresh) + "\n"
    elif not body.endswith("\n"):
        body += "\n"
    STATE.write_text(body, encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--status", action="store_true")
    p.add_argument("--stamp", action="store_true")
    p.add_argument("--ids", default="")
    args = p.parse_args()
    if args.status:
        ids = load_skip()
        print(
            json.dumps(
                {
                    "state": STATE.as_posix(),
                    "news": NEWS.as_posix(),
                    "n_skip": len(ids),
                    "exists_news": NEWS.exists(),
                },
                indent=2,
            )
        )
        return 0
    if args.stamp:
        stamp([x.strip() for x in args.ids.split(",") if x.strip()])
        print(json.dumps({"stamped": load_skip()[-8:], "n_skip": len(load_skip())}, indent=2))
        return 0
    print("ASK --status or --stamp --ids a,b")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
