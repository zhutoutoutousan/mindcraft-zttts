"""On-demand deliverables live in tmp/. Only ttl.toon.md persists.

    python cron/janitor.py --touch   stamp last_run now
    python cron/janitor.py --ttl     delete tmp siblings if last_run is 5 days old
    python cron/janitor.py --purge   delete tmp siblings now. Keep ttl.toon.md. Human asked.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TMP = ROOT / "tmp"
TTL_FILE = TMP / "ttl.toon.md"
LAPSE_DAYS = 5
SCHEMA = "deliver/ttl"


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
        "note: only persistent file in tmp. ROOT reads this. After lapse_days janitor promotes named caches then deletes every other file in tmp.",
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


def sibling_paths() -> list[Path]:
    if not TMP.is_dir():
        return []
    found: list[Path] = []
    for child in TMP.iterdir():
        if child.resolve() == TTL_FILE.resolve():
            continue
        found.append(child)
    found.sort(key=lambda p: p.as_posix())
    return found


def due(now: datetime | None = None) -> bool:
    now = now or now_utc()
    siblings = sibling_paths()
    last = parse_iso(read_ttl().get("last_run", ""))
    if last is None:
        return bool(siblings)
    return now >= last + timedelta(days=LAPSE_DAYS) and bool(siblings)


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

    for child in sibling_paths():
        rel = child.relative_to(ROOT)
        if dry_run:
            gone.append(rel)
            continue
        try:
            if child.is_dir():
                shutil.rmtree(child)
            elif child.is_file():
                child.unlink()
            else:
                continue
        except OSError as exc:
            print(f"TTL FAIL {rel.as_posix()}: {exc}")
            continue
        gone.append(rel)
    if not dry_run:
        write_ttl(last_run="", last_expire=now_utc().strftime("%Y-%m-%dT%H:%M:%SZ"))
    return gone
