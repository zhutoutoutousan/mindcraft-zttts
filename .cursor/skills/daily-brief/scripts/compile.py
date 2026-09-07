#!/usr/bin/env python3
"""Compile a daily-brief tex in tmp/ with XeLaTeX.

    python .cursor/skills/daily-brief/scripts/compile.py tmp/day-YYYY-MM-DD.tex
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

def repo_root() -> Path:
    here = Path(__file__).resolve()
    for p in here.parents:
        if (p / "CPU.md").is_file():
            return p
    sys.exit("ASK CPU.md not found")


def xelatex() -> str:
    found = shutil.which("xelatex")
    if found:
        return found
    win = Path.home() / "AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe"
    if win.is_file():
        return str(win)
    sys.exit("ASK xelatex not on PATH")


def main() -> int:
    if len(sys.argv) != 2:
        print("ASK python .cursor/skills/daily-brief/scripts/compile.py tmp/day-YYYY-MM-DD.tex")
        return 2
    tex = Path(sys.argv[1])
    root = repo_root()
    if not tex.is_absolute():
        tex = root / tex
    if not tex.is_file() or tex.suffix.lower() != ".tex":
        print(f"ASK missing tex {tex}")
        return 2
    cmd = [
        xelatex(),
        "-interaction=nonstopmode",
        "-halt-on-error",
        tex.name,
    ]
    for _ in range(2):
        r = subprocess.run(cmd, cwd=tex.parent, check=False)
        if r.returncode != 0:
            return r.returncode
    pdf = tex.with_suffix(".pdf")
    print(pdf.as_posix())
    return 0 if pdf.is_file() else 1


if __name__ == "__main__":
    raise SystemExit(main())
