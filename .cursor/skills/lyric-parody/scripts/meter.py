#!/usr/bin/env python3
"""Check parody lines against skeleton 字/syllable counts.

  python .cursor/skills/lyric-parody/scripts/meter.py --job tmp/lyric-parody/slug/job.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CJK = re.compile(r"[\u4e00-\u9fff]")
KEEP_LATIN = re.compile(r"[0-9A-Za-zÄÖÜäöüß]")
SYL = re.compile(r"[aeiouyäöü]+", re.I)


def zh_n(text: str) -> int:
    return len(CJK.findall(text)) + len(KEEP_LATIN.findall(text))


def latin_n(text: str) -> int:
    words = re.split(r"[^A-Za-zÄÖÜäöüß']+", text)
    n = 0
    for w in words:
        w = w.strip("'")
        if not w:
            continue
        groups = SYL.findall(w)
        n += max(1, len(groups))
    return n


def units(text: str, lang: str) -> int:
    if lang == "zh":
        return zh_n(text)
    return latin_n(text)


def check(job: dict) -> list[str]:
    lang = job.get("lang") or "zh"
    errs: list[str] = []
    lines = job.get("lines") or []
    if not lines:
        return ["no lines"]
    for i, row in enumerate(lines):
        text = (row.get("text") or "").strip()
        want = int(row.get("n") or 0)
        got = units(text, lang)
        flex = 1 if row.get("flex") else 0
        if want <= 0:
            errs.append(f"line {i}: missing n")
        elif not text:
            errs.append(f"line {i}: empty text")
        elif abs(got - want) > flex:
            errs.append(f"line {i}: expected {want} got {got}  {text}")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True)
    args = ap.parse_args()
    job = json.loads(Path(args.job).read_text(encoding="utf-8"))
    errs = check(job)
    if errs:
        print("\n".join(errs))
        raise SystemExit(2)
    print("OK", len(job["lines"]), "lines", job.get("lang", "zh"))


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        print(exc, file=sys.stderr)
        raise SystemExit(1)
