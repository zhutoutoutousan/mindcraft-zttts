#!/usr/bin/env python3
"""Move non-markdown files into recycle/, preserving relative paths.

Bytecode caches (__pycache__, *.pyc) are trash. Delete them. Do not recycle.

    python cron/janitor.py --dry-run
    python cron/janitor.py --trash
    python cron/janitor.py --apply
    python cron/janitor.py --ttl
    python cron/janitor.py --touch
"""
from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from pathlib import Path

import temp_ttl

ROOT = Path(__file__).resolve().parent.parent
RECYCLE = ROOT / "recycle"
JOURNAL = RECYCLE / "JOURNAL.md"
KEEP_FILES = {
    Path("cron") / "janitor.py",
    Path("skills") / "ontology-showcase.py",
}
NEVER_DIR = {".git", "recycle", ".cursor", "tmp"}
TRASH_DIR_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
TRASH_SUFFIXES = {".pyc", ".pyo"}
KEEP_DIR_EMPTY = {
    Path("pedagogy"),
    Path("pedagogy") / "being",
    Path("pedagogy") / "math",
    Path("pedagogy") / "physics",
    Path("pedagogy") / "biology",
    Path("pedagogy") / "computation",
    Path("pedagogy") / "language",
    Path("cron"),
    Path("skills"),
    Path("self"),
    Path("self") / "identity",
    Path("mezzanine"),
    Path("schedule"),
    Path("inflow"),
    Path("tmp"),
}


def is_markdown(path: Path) -> bool:
    return path.suffix.lower() == ".md"


def never_dir(rel: Path) -> bool:
    return bool(rel.parts) and rel.parts[0] in NEVER_DIR


def is_trash_dir_name(name: str) -> bool:
    return name in TRASH_DIR_NAMES


def is_trash_rel(rel: Path) -> bool:
    if any(is_trash_dir_name(part) for part in rel.parts):
        return True
    return rel.suffix.lower() in TRASH_SUFFIXES


def walk_tree() -> tuple[list[Path], list[Path], list[Path]]:
    recycle: list[Path] = []
    trash_dirs: list[Path] = []
    trash_files: list[Path] = []
    stack = [ROOT]
    while stack:
        current = stack.pop()
        try:
            children = list(current.iterdir())
        except OSError:
            continue
        for child in children:
            try:
                rel = child.relative_to(ROOT)
            except ValueError:
                continue
            if never_dir(rel):
                continue
            if child.is_dir():
                if is_trash_dir_name(child.name):
                    trash_dirs.append(rel)
                    continue
                stack.append(child)
                continue
            if not child.is_file():
                continue
            if is_trash_rel(rel):
                trash_files.append(rel)
                continue
            if is_markdown(rel) or should_keep(rel):
                continue
            recycle.append(rel)
    recycle.sort(key=lambda p: p.as_posix())
    trash_dirs.sort(key=lambda p: p.as_posix())
    trash_files.sort(key=lambda p: p.as_posix())
    return recycle, trash_dirs, trash_files


def should_keep(rel: Path) -> bool:
    if rel in KEEP_FILES:
        return True
    if rel.name == "LICENSE" and len(rel.parts) == 1:
        return True
    if rel.name == ".gitignore" and len(rel.parts) == 1:
        return True
    if rel.name.lower() == "submit.ps1" and len(rel.parts) == 1:
        return True
    if rel.parts[:1] == ("schedule",) and rel.suffix.lower() == ".ics":
        return True
    if rel.suffix.lower() == ".py" and rel.parts and rel.parts[0] in {"cron", "skills"}:
        return True
    if rel.parts[:1] == ("skills",) and rel.suffix.lower() in {".puml", ".json"}:
        return True
    return False


def dest_for(rel: Path) -> Path:
    dest = RECYCLE / rel
    if not dest.exists():
        return dest
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return dest.with_name(f"{dest.stem}.{stamp}{dest.suffix}")


def prune_empty(start: Path) -> None:
    if not start.exists() or not start.is_dir():
        return
    try:
        rel = start.relative_to(ROOT)
    except ValueError:
        return
    if start != ROOT and never_dir(rel):
        return
    for child in list(start.iterdir()):
        if child.is_dir():
            prune_empty(child)
    if rel in KEEP_DIR_EMPTY or start == ROOT:
        return
    try:
        next(start.iterdir())
    except StopIteration:
        start.rmdir()


def append_journal(moved: list[tuple[Path, Path]], trashed: list[Path]) -> None:
    RECYCLE.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [f"- SWEEP {stamp} moved={len(moved)} trash={len(trashed)}"]
    for src, dest in moved:
        lines.append(f"  - {src.as_posix()} -> {dest.relative_to(ROOT).as_posix()}")
    for rel in trashed:
        lines.append(f"  - TRASH {rel.as_posix()}")
    prev = JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else "- KIND recycle journal. Markdown so the janitor will not move this file.\n"
    if not prev.endswith("\n"):
        prev += "\n"
    JOURNAL.write_text(prev + "\n".join(lines) + "\n", encoding="utf-8")


def trash_now(trash_dirs: list[Path], trash_files: list[Path]) -> list[Path]:
    gone: list[Path] = []
    for rel in trash_files:
        src = ROOT / rel
        if not src.is_file():
            continue
        try:
            src.unlink()
        except OSError as exc:
            print(f"TRASH FAIL {rel.as_posix()}: {exc}")
            continue
        gone.append(rel)
    for rel in trash_dirs:
        src = ROOT / rel
        if not src.is_dir():
            continue
        try:
            shutil.rmtree(src)
        except OSError as exc:
            print(f"TRASH FAIL {rel.as_posix()}: {exc}")
            continue
        gone.append(rel)
    return gone


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--trash", action="store_true")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--ttl", action="store_true")
    p.add_argument("--touch", action="store_true")
    args = p.parse_args()
    n = sum(bool(x) for x in [args.dry_run, args.trash, args.apply, args.ttl, args.touch])
    if n != 1:
        print("ASK --dry-run or --trash or --apply or --ttl or --touch. Default is refuse.")
        return 2
    if args.touch:
        path = temp_ttl.touch()
        print(f"TOUCH {path.relative_to(ROOT).as_posix()} last_run={temp_ttl.read_ttl().get('last_run', '')}")
        return 0
    recycle, trash_dirs, trash_files = walk_tree()
    ttl_due = temp_ttl.due()
    ttl_preview = temp_ttl.expire(dry_run=True) if ttl_due else []
    if args.dry_run:
        print(f"DRY recycle={len(recycle)} trash_dirs={len(trash_dirs)} trash_files={len(trash_files)} ttl={len(ttl_preview)}")
        for rel in trash_dirs:
            print(f"TRASH DIR {rel.as_posix()}")
        for rel in trash_files:
            print(f"TRASH {rel.as_posix()}")
        for rel in ttl_preview:
            print(f"TTL {rel.as_posix()}")
        for rel in recycle:
            print(rel.as_posix())
        return 0
    if args.ttl:
        gone = temp_ttl.expire(dry_run=False)
        if gone:
            append_journal([], gone)
        print(f"TTL n={len(gone)} keep {temp_ttl.TTL_FILE.relative_to(ROOT).as_posix()}")
        return 0
    trashed = trash_now(trash_dirs, trash_files)
    if args.trash or args.apply:
        gone = temp_ttl.expire(dry_run=False)
        trashed.extend(gone)
    moved: list[tuple[Path, Path]] = []
    if args.apply:
        for rel in recycle:
            src = ROOT / rel
            dest = dest_for(rel)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            moved.append((rel, dest))
    append_journal(moved, trashed)
    prune_empty(ROOT)
    print(f"MOVED n={len(moved)} TRASH n={len(trashed)} -> {RECYCLE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
