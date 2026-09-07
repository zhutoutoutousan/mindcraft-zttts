"""Promote named tmp knowledge caches into lasting stores before TTL delete.

Deliverables (html, media, build scripts) stay expire-only. Never invent CLAIM or STUDY ANSWER.
"""
from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "tmp"

# (relative tmp path, lasting dest, kind)
ROUTES: list[tuple[str, str, str]] = [
    (
        "tmp/pedagogy/inflow-takes.toon.md",
        "inflow/takes.toon.md",
        "inflow-take",
    ),
    (
        "tmp/pedagogy/learner-notes.toon.md",
        "pedagogy/_learn/learner-notes.toon.md",
        "learner-note",
    ),
    (
        "tmp/pedagogy/baseline-answers.toon.md",
        "pedagogy/_learn/baseline-answers.toon.md",
        "baseline-answers",
    ),
]


def _copy_file(src: Path, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return "copied"


def promote_all(*, dry_run: bool = False) -> list[tuple[Path, Path, str]]:
    """Copy known knowledge caches out of tmp. Returns (src_rel, dest_rel, action)."""
    done: list[tuple[Path, Path, str]] = []
    for src_rel, dest_rel, kind in ROUTES:
        src = ROOT / src_rel
        dest = ROOT / dest_rel
        if not src.is_file():
            continue
        action = "would-copy" if dry_run else _copy_file(src, dest)
        print(f"PROMOTE {kind} {src_rel} -> {dest_rel} {action}", flush=True)
        done.append((Path(src_rel), Path(dest_rel), action))
    return done


def classify_tmp_child(child: Path) -> str:
    """How TTL should treat this sibling: promote-then-expire vs expire."""
    try:
        rel = child.relative_to(ROOT).as_posix().replace("\\", "/")
    except ValueError:
        return "expire"
    for src_rel, _, _ in ROUTES:
        if rel == src_rel.replace("\\", "/"):
            return "promote"
        if child.is_dir() and src_rel.startswith(rel + "/"):
            return "promote-tree"
    return "expire"


def main() -> int:
    import argparse

    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    rows = promote_all(dry_run=args.dry_run)
    print(f"PROMOTE n={len(rows)} dry_run={args.dry_run}")
    print(f"stamp {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
