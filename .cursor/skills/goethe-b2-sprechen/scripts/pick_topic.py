#!/usr/bin/env python3
"""Pick or mark Goethe-B2 Sprechen themes. Refuses a repeated id or title.

  python .cursor/skills/goethe-b2-sprechen/scripts/pick_topic.py
  python .cursor/skills/goethe-b2-sprechen/scripts/pick_topic.py --mark --date 2026-10-04 --teil1 ID --teil1 ID --teil2 ID
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def skill_dir() -> Path:
    return Path(__file__).resolve().parents[1]


def norm(title: str) -> str:
    text = title.casefold().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def parse_rows(path: Path, key: str) -> list[list[str]]:
    rows: list[list[str]] = []
    inside = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(key + "[]"):
            inside = True
            continue
        if inside and line.startswith("  ") and line.strip():
            rows.append([part.strip() for part in line.strip().split(",", 3 if key == "used" else 2)])
            continue
        if inside and line.strip() and not line.startswith(" "):
            break
    return rows


def load() -> tuple[list[list[str]], list[list[str]], list[list[str]]]:
    root = skill_dir()
    topics = root / "topics.toon.md"
    used = root / "used.toon.md"
    return parse_rows(topics, "teil1"), parse_rows(topics, "teil2"), parse_rows(used, "used")


def used_block(used: list[list[str]]) -> tuple[set[str], set[str]]:
    ids = {row[2] for row in used if len(row) >= 3}
    titles = {norm(row[3]) for row in used if len(row) >= 4}
    return ids, titles


def fresh(rows: list[list[str]], ids: set[str], titles: set[str]) -> list[list[str]]:
    out = []
    for row in rows:
        if len(row) < 2:
            continue
        if row[0] in ids or norm(row[1]) in titles:
            continue
        out.append(row)
    return out


def pick() -> int:
    teil1, teil2, used = load()
    ids, titles = used_block(used)
    a = fresh(teil1, ids, titles)
    b = fresh(teil2, ids, titles)
    if len(a) < 2 or len(b) < 1:
        print(f"POOL_EMPTY teil1={len(a)} teil2={len(b)}", file=sys.stderr)
        return 3
    print(f"teil1_a\t{a[0][0]}\t{a[0][1]}\t{a[0][2]}")
    print(f"teil1_b\t{a[1][0]}\t{a[1][1]}\t{a[1][2]}")
    print(f"teil2\t{b[0][0]}\t{b[0][1]}\t{b[0][2]}")
    return 0


def mark(date: str, teil1_ids: list[str], teil2_ids: list[str]) -> int:
    teil1, teil2, used = load()
    ids, titles = used_block(used)
    catalog = {row[0]: row for row in teil1 + teil2}
    lines = []
    for part, chosen in (("teil1", teil1_ids), ("teil2", teil2_ids)):
        for item in chosen:
            row = catalog.get(item)
            if row is None:
                print(f"UNKNOWN {item}", file=sys.stderr)
                return 2
            if item in ids or norm(row[1]) in titles:
                print(f"DUPLICATE {item} {row[1]}", file=sys.stderr)
                return 2
            ids.add(item)
            titles.add(norm(row[1]))
            lines.append(f"  {date},{part},{item},{row[1]}")
    path = skill_dir() / "used.toon.md"
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"marked {len(lines)}")
    return 0


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--mark", action="store_true")
    parser.add_argument("--date", default="")
    parser.add_argument("--teil1", action="append", default=[])
    parser.add_argument("--teil2", action="append", default=[])
    args = parser.parse_args()
    if not args.mark:
        return pick()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        print("NEED --date YYYY-MM-DD", file=sys.stderr)
        return 2
    if len(args.teil1) < 1 and len(args.teil2) < 1:
        print("NEED --teil1 or --teil2", file=sys.stderr)
        return 2
    return mark(args.date, args.teil1, args.teil2)


if __name__ == "__main__":
    raise SystemExit(main())
