#!/usr/bin/env python3
"""Show or update the later block: drills plus retake of the previous model test.

  python .cursor/skills/goethe-b2-sprechen/scripts/due.py --date 2026-10-04
  python .cursor/skills/goethe-b2-sprechen/scripts/due.py --close 2026-10-03 --add --due 2026-10-05 --from 2026-10-04 --teil1 ID --teil2 ID --drills drills/2026-10-04.toon.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def queue_path() -> Path:
    return Path(__file__).resolve().parents[1] / "queue.toon.md"


def rows(text: str) -> list[list[str]]:
    found: list[list[str]] = []
    inside = False
    for line in text.splitlines():
        if line.startswith("item[]"):
            inside = True
            continue
        if inside and line.startswith("  ") and line.strip():
            found.append([part.strip() for part in line.strip().split(",", 5)])
        elif inside and line.strip() and not line.startswith(" "):
            break
    return found


def show(day: str) -> int:
    text = queue_path().read_text(encoding="utf-8")
    open_rows = [row for row in rows(text) if len(row) >= 6 and row[2] == "open" and row[0] <= day]
    if not open_rows:
        print("NONE")
        return 0
    for row in open_rows:
        due, src, status, teil1, teil2, drills = row[:6]
        print(f"due\t{due}\tfrom\t{src}\tstatus\t{status}")
        print(f"retake_teil1\t{teil1}")
        print(f"retake_teil2\t{teil2}")
        print(f"drills\t{drills}")
    return 0


def close_and_add(close_from: str, due: str, src: str, teil1: str, teil2: str, drills: str) -> int:
    path = queue_path()
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = 0
    out = []
    for line in lines:
        if line.startswith("  ") and close_from in line and ",open," in line:
            out.append(line.replace(",open,", ",done,", 1))
            changed += 1
        else:
            out.append(line)
    if changed == 0:
        print(f"NO_OPEN_FROM {close_from}", file=sys.stderr)
        return 2
    if not out[-1].endswith("\n"):
        pass
    out.append(f"  {due},{src},open,{teil1},{teil2},{drills}")
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"closed {changed} added {due}")
    return 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default="")
    parser.add_argument("--close", default="")
    parser.add_argument("--add", action="store_true")
    parser.add_argument("--due", default="")
    parser.add_argument("--from", dest="src", default="")
    parser.add_argument("--teil1", default="")
    parser.add_argument("--teil2", default="")
    parser.add_argument("--drills", default="")
    args = parser.parse_args()
    if args.add:
        if not all([args.close, args.due, args.src, args.teil1, args.teil2, args.drills]):
            print("NEED --close --due --from --teil1 --teil2 --drills", file=sys.stderr)
            return 2
        return close_and_add(args.close, args.due, args.src, args.teil1, args.teil2, args.drills)
    if not args.date:
        print("NEED --date YYYY-MM-DD", file=sys.stderr)
        return 2
    return show(args.date)


if __name__ == "__main__":
    raise SystemExit(main())
