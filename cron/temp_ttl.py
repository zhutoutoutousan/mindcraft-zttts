"""On-demand deliverables live in tmp/. Persist ttl.toon.md + mindcraft-hall.

    python cron/janitor.py --touch   stamp last_run now
    python cron/janitor.py --ttl     delete tmp siblings if last_run is 5 days old
    python cron/janitor.py --purge   delete tmp siblings now. Keep ttl + hall. Human asked.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "tmp"
TTL_FILE = TMP / "ttl.toon.md"
HALL_FILE = TMP / "pedagogy" / "mindcraft-hall.html"
LAPSE_DAYS = 5
SCHEMA = "deliver/ttl"
KEEP_REL = (
    Path("tmp") / "ttl.toon.md",
    Path("tmp") / "pedagogy" / "mindcraft-hall.html",
)
TTL_NOTE = (
    "persistent: ttl.toon.md + pedagogy/mindcraft-hall.html. "
    "ROOT reads this. After lapse_days janitor promotes named caches then "
    "deletes every other file in tmp. Keep hall."
)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_ttl(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip()
    return out


def read_ttl() -> dict[str, str]:
    if not TTL_FILE.is_file():
        return {}
    return parse_ttl(TTL_FILE.read_text(encoding="utf-8"))


def write_ttl(*, last_run: str | None = None, last_expire: str | None = None) -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    prev = read_ttl()
    run = prev.get("last_run", "") if last_run is None else last_run
    expire = prev.get("last_expire", "") if last_expire is None else last_expire
    lines = [
        f"schema: {SCHEMA}",
        f"dir: {TMP.name}",
        f"lapse_days: {LAPSE_DAYS}",
        f"last_run: {run}",
        f"last_expire: {expire}",
        f"note: {TTL_NOTE}",
        "",
    ]
    TTL_FILE.write_text("\n".join(lines), encoding="utf-8")


def parse_iso(value: str) -> datetime | None:
    raw = (value or "").strip()
    if not raw:
        return None
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def keep_resolved() -> set[Path]:
    keeps: set[Path] = set()
    for rel in KEEP_REL:
        keeps.add((ROOT / rel).resolve())
    return keeps


def _is_keep_file(path: Path, keeps: set[Path]) -> bool:
    try:
        return path.resolve() in keeps
    except OSError:
        return False


def _is_keep_ancestor(path: Path, keeps: set[Path]) -> bool:
    try:
        resolved = path.resolve()
    except OSError:
        return False
    for keep in keeps:
        try:
            keep.relative_to(resolved)
            return True
        except ValueError:
            continue
    return False


def sibling_paths() -> list[Path]:
    """Top-level tmp children that are not themselves keep files."""
    if not TMP.is_dir():
        return []
    keeps = keep_resolved()
    found: list[Path] = []
    for child in TMP.iterdir():
        if _is_keep_file(child, keeps):
            continue
        found.append(child)
    found.sort(key=lambda p: p.as_posix())
    return found


def has_expirable() -> bool:
    """True if tmp still has files other than KEEP_REL."""
    keeps = keep_resolved()
    if not TMP.is_dir():
        return False
    for path in TMP.rglob("*"):
        if path.is_dir():
            continue
        if _is_keep_file(path, keeps):
            continue
        return True
    return False


def due(now: datetime | None = None) -> bool:
    now = now or now_utc()
    last = parse_iso(read_ttl().get("last_run", ""))
    if last is None:
        return has_expirable()
    return now >= last + timedelta(days=LAPSE_DAYS) and has_expirable()


def touch() -> Path:
    write_ttl(last_run=now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"))
    return TTL_FILE


def expire(*, dry_run: bool = False, force: bool = False) -> list[Path]:
    gone: list[Path] = []
    if not force and not due():
        return gone
    import shutil

    import tmp_promote

    tmp_promote.promote_all(dry_run=dry_run)

    keeps = keep_resolved()

    def expire_node(node: Path) -> None:
        if _is_keep_file(node, keeps):
            return
        if node.is_dir() and _is_keep_ancestor(node, keeps):
            try:
                children = sorted(node.iterdir(), key=lambda p: p.as_posix())
            except OSError as exc:
                print(f"TTL FAIL {node.relative_to(ROOT).as_posix()}: {exc}")
                return
            for nested in children:
                expire_node(nested)
            return
        rel = node.relative_to(ROOT)
        if dry_run:
            gone.append(rel)
            return
        try:
            if node.is_dir():
                shutil.rmtree(node)
            elif node.is_file() or node.is_symlink():
                node.unlink()
            else:
                return
        except OSError as exc:
            print(f"TTL FAIL {rel.as_posix()}: {exc}")
            return
        gone.append(rel)

    if TMP.is_dir():
        for child in sorted(TMP.iterdir(), key=lambda p: p.as_posix()):
            expire_node(child)
    if not dry_run:
        write_ttl(last_run="", last_expire=now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"))
    return gone
