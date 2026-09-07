#!/usr/bin/env python3
"""Splice gitignored .private calendar notes into tmp/take.html.

Public schedule stays clean. Grab the take file on the phone.

    python cron/private-take.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
PRIVATE = ROOT / ".private"
OUT = ROOT / "tmp" / "take.html"
TZ = ZoneInfo("Europe/Berlin")
WHEN_RE = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})(?:\s+(?P<start>\d{2}:\d{2})[–-](?P<end>\d{2}:\d{2}))?"
)


def parse_fu(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {"path": path.name}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- ") or line.startswith("  - "):
            continue
        rest = line[2:]
        key, _, val = rest.partition(" ")
        if key.isupper() or key in {"TZ"}:
            fields[key] = val.strip()
    return fields


def sort_key(fields: dict[str, str]) -> tuple[str, str]:
    m = WHEN_RE.search(fields.get("WHEN", ""))
    if not m:
        return ("9999-99-99", "99:99")
    return (m.group("date"), m.group("start") or "00:00")


def html_esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def card(fields: dict[str, str], today: date) -> str:
    title = fields.get("TITLE") or fields.get("KIND", fields["path"])
    when = fields.get("WHEN", "")
    m = WHEN_RE.search(when)
    day = date.fromisoformat(m.group("date")) if m else None
    past = day is not None and day < today
    klass = "past" if past else "soon"
    rows = []
    for key in ("WHEN", "WHERE", "FROM", "WHO", "URL", "STATUS", "RSVP", "NOTE", "CLOCK"):
        val = fields.get(key)
        if val:
            if key == "URL":
                rows.append(
                    f"<p><b>URL</b> <a href='{html_esc(val)}'>{html_esc(val)}</a></p>"
                )
            else:
                rows.append(f"<p><b>{html_esc(key)}</b> {html_esc(val)}</p>")
    return (
        f"<article class='{klass}'>"
        f"<h2>{html_esc(title)}</h2>"
        f"<p class='muted'>{html_esc(fields['path'])}</p>"
        + "".join(rows)
        + "</article>"
    )


def write_take(today: date | None = None) -> Path:
    today = today or datetime.now(TZ).date()
    cards = []
    for path in sorted(PRIVATE.glob("*.fu.md")):
        fields = parse_fu(path)
        if "WHEN" not in fields:
            continue
        cards.append(fields)
    cards.sort(key=sort_key)
    parts = [
        "<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'>",
        "<meta name='viewport' content='width=device-width, initial-scale=1'>",
        "<title>Private take</title>",
        "<style>",
        "body{background:#0b0e12;color:#e8eaed;font:18px/1.45 system-ui,Segoe UI,sans-serif;margin:20px}",
        "h1{font-size:22px} h2{font-size:20px;margin:0 0 6px}",
        ".muted{color:#9aa0a6;font-size:14px}",
        "article{border:1px solid #2a3140;border-radius:12px;padding:16px;margin:0 0 14px;background:#14181f}",
        "article.soon{border-color:#1a73e8} article.past{opacity:.55}",
        "b{color:#8ab4f8} a{color:#8ab4f8}",
        "</style></head><body>",
        f"<h1>Private take</h1><p class='muted'>Heute {today.isoformat()} Europe/Berlin. Not schedule. tmp/ expires in 5 days.</p>",
    ]
    for fields in cards:
        parts.append(card(fields, today))
    parts.append("</body></html>")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(parts), encoding="utf-8")
    subprocess.run(
        [sys.executable, str(ROOT / "cron" / "janitor.py"), "--touch"],
        check=True,
    )
    return OUT


def main() -> int:
    path = write_take()
    print(path.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
