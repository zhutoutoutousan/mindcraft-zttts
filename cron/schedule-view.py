#!/usr/bin/env python3
"""Google-style week view + agenda cards into tmp/schedule/.

    python cron/schedule-view.py
    python cron/schedule-view.py --today 2026-09-02
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

from coarse import coarse_place

ROOT = Path(__file__).resolve().parent.parent
ENRICH = ROOT / "schedule" / "enrich.toon.md"
OUT = ROOT / "tmp" / "schedule"
TZ = ZoneInfo("Europe/Berlin")
WD = ("SO", "MO", "DI", "MI", "DO", "FR", "SA")
MONTH_DE = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember",
}

C_BG = "#0b0e12"
C_PANEL = "#14181f"
C_GRID = "#2a3140"
C_TEXT = "#e8eaed"
C_MUTED = "#9aa0a6"
C_TODAY = "#8ab4f8"
C_TODAY_BG = "#1a2838"
C_CONF = "#1a73e8"
C_CAND = "#5f6368"
C_CLASH = "#e37400"
C_ALLDAY = "#8ab4f8"
C_ALLDAY_CAND = "#80868b"


@dataclass
class Event:
    title: str
    what: str
    where: str
    why: str
    url: str
    start: datetime
    end: datetime
    allday: bool
    status: str
    clash: bool = False
    lane: int = 0


def parse_iso(raw: str) -> datetime:
    text = raw.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TZ)
    return dt.astimezone(TZ)


def parse_enrich(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    cur: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "record:":
            if cur.get("title"):
                records.append(cur)
            cur = {}
            continue
        m = re.match(r"^\s{2}([a-z]+):\s*(.*)$", line)
        if m:
            cur[m.group(1)] = m.group(2).strip()
    if cur.get("title"):
        records.append(cur)
    return records


def month_fu_path(day: date | None = None) -> Path:
    d = day or datetime.now(TZ).date()
    return ROOT / "schedule" / f"{d.year}-{d.month}.fu.md"


def parse_status(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    title = ""
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("- SCHEDULE "):
            payload = line[len("- SCHEDULE ") :].strip()
            payload = re.sub(r"^\d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}–\d{2}:\d{2})? ", "", payload)
            title = payload.strip()
            continue
        m = re.match(r"^  - STATUS (\S+)", line)
        if m and title:
            out[title] = m.group(1).lower()
    return out


def load_events(day: date | None = None) -> list[Event]:
    status_map = parse_status(month_fu_path(day))
    events: list[Event] = []
    for rec in parse_enrich(ENRICH):
        title = rec.get("title", "").strip()
        if not title or not rec.get("when"):
            continue
        start = parse_iso(rec["when"])
        end = parse_iso(rec["end"]) if rec.get("end") else start + timedelta(hours=1)
        allday = rec.get("allday", "false").lower() == "true"
        events.append(
            Event(
                title=title,
                what=rec.get("what", ""),
                where=rec.get("where", ""),
                why=rec.get("why", ""),
                url=rec.get("url", ""),
                start=start,
                end=end,
                allday=allday,
                status=status_map.get(title, "candidate"),
            )
        )
    mark_clashes(events)
    events.sort(key=lambda e: (e.start, e.end, e.title))
    return events


def mark_clashes(events: list[Event]) -> None:
    timed = [e for e in events if not e.allday]
    for i, a in enumerate(timed):
        for b in timed[i + 1 :]:
            if a.start.date() != b.start.date():
                continue
            if a.start < b.end and b.start < a.end:
                a.clash = True
                b.clash = True


def sunday_of(day: date) -> date:
    return day - timedelta(days=(day.weekday() + 1) % 7)


def weeks_covering(events: list[Event], today: date) -> list[date]:
    if not events:
        return [sunday_of(today)]
    last = max((e.end.date() - timedelta(days=1) if e.allday else e.end.date()) for e in events)
    last = max(last, today)
    weeks: list[date] = []
    cur = sunday_of(today)
    while cur <= last:
        weeks.append(cur)
        cur += timedelta(days=7)
    return weeks


def dates_of(ev: Event) -> list[date]:
    if ev.allday:
        d = ev.start.date()
        end = ev.end.date()
        out: list[date] = []
        while d < end:
            out.append(d)
            d += timedelta(days=1)
        return out
    return [ev.start.date()]


def intersects_week(ev: Event, week: date) -> bool:
    days = set(week + timedelta(days=i) for i in range(7))
    return any(d in days for d in dates_of(ev))


def short_title(title: str, n: int = 22) -> str:
    if len(title) <= n:
        return title
    return title[: n - 1] + "…"


def stamp_ttl() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "cron" / "janitor.py"), "--touch"],
        check=True,
    )


def splice_private_take() -> Path:
    """Public schedule stays clean. Private clocks go to tmp/take.html."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "cron" / "private-take.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    rel = (proc.stdout or "").strip().splitlines()[-1]
    return ROOT / rel


def assign_lanes(day_events: list[Event]) -> int:
    ordered = sorted(day_events, key=lambda e: (e.start, e.end))
    ends: list[datetime] = []
    for ev in ordered:
        placed = False
        for i, fin in enumerate(ends):
            if ev.start >= fin:
                ends[i] = ev.end
                ev.lane = i
                placed = True
                break
        if not placed:
            ev.lane = len(ends)
            ends.append(ev.end)
    return max((e.lane for e in ordered), default=0) + 1


def draw_week(events: list[Event], week: date, today: date, path: Path) -> None:
    days = [week + timedelta(days=i) for i in range(7)]
    timed_by: dict[date, list[Event]] = {d: [] for d in days}
    allday_by: dict[date, list[Event]] = {d: [] for d in days}
    hour0, hour1 = 8, 21
    for ev in events:
        if not intersects_week(ev, week):
            continue
        if ev.allday:
            for d in dates_of(ev):
                if d in allday_by:
                    allday_by[d].append(ev)
        else:
            d = ev.start.date()
            if d in timed_by:
                timed_by[d].append(ev)
                hour0 = min(hour0, ev.start.hour)
                hour1 = max(hour1, ev.end.hour if ev.end.minute == 0 else ev.end.hour + 1)
    hour0 = max(7, hour0)
    hour1 = min(22, max(hour1, 21))
    hours = hour1 - hour0
    lanes = {d: assign_lanes(timed_by[d]) for d in days}

    fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor=C_BG)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.invert_yaxis()
    ax.axis("off")
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)

    last = week + timedelta(days=6)
    head = f"{week.day}. {MONTH_DE[week.month]} – {last.day}. {MONTH_DE[last.month]} 2026"
    ax.text(0.02, 0.025, head, color=C_TEXT, fontsize=18, fontweight="bold", va="top")
    ax.text(0.98, 0.025, "Europe/Berlin  ·  7-Tage-Ansicht", color=C_MUTED, fontsize=11, ha="right", va="top")

    gx0 = 0.07
    gy0 = 0.16
    gw = 0.91
    gh = 0.80
    col_w = gw / 7
    all_h = 0.07
    grid_y = gy0 + all_h
    grid_h = gh - all_h

    for i, d in enumerate(days):
        x = gx0 + i * col_w
        today_here = d == today
        if today_here:
            ax.add_patch(Rectangle((x, gy0), col_w, gh, facecolor=C_TODAY_BG, edgecolor="none"))
        ax.add_patch(Rectangle((x, gy0), col_w, gh, facecolor="none", edgecolor=C_GRID, linewidth=0.8))
        wd = WD[i]
        color = C_TODAY if today_here else C_MUTED
        ax.text(x + col_w / 2, 0.08, wd, color=color, fontsize=10, ha="center", va="center")
        ax.text(x + col_w / 2, 0.115, str(d.day), color=C_TODAY if today_here else C_TEXT, fontsize=16, ha="center", va="center", fontweight="bold")

    ax.add_patch(Rectangle((gx0, gy0), gw, all_h, facecolor=C_PANEL, edgecolor=C_GRID, linewidth=0.8))
    ax.text(0.012, gy0 + all_h / 2, "ganztags", color=C_MUTED, fontsize=7, va="center", rotation=90)

    drawn_all: set[tuple[str, date]] = set()
    for ev in events:
        if not ev.allday or not intersects_week(ev, week):
            continue
        span = [d for d in dates_of(ev) if d in allday_by]
        if not span:
            continue
        key = (ev.title, span[0])
        if key in drawn_all:
            continue
        drawn_all.add(key)
        i0 = (span[0] - week).days
        i1 = (span[-1] - week).days
        x = gx0 + i0 * col_w + 0.004
        w = (i1 - i0 + 1) * col_w - 0.008
        y = gy0 + 0.012
        fill = C_ALLDAY if ev.status == "confirmed" else C_ALLDAY_CAND
        ax.add_patch(FancyBboxPatch((x, y), w, all_h - 0.024, boxstyle="round,pad=0.004,rounding_size=0.008", facecolor=fill, edgecolor="none", alpha=0.92))
        more = " →" if span[-1] == days[-1] and dates_of(ev)[-1] > span[-1] else ""
        ax.text(x + 0.008, y + (all_h - 0.024) / 2, short_title(ev.title, 28) + more, color="#0b0e12", fontsize=8, va="center", fontweight="bold")

    for h in range(hours + 1):
        y = grid_y + (h / hours) * grid_h
        ax.plot([gx0, gx0 + gw], [y, y], color=C_GRID, linewidth=0.6)
        label = f"{hour0 + h:02d}:00"
        ax.text(gx0 - 0.008, y, label, color=C_MUTED, fontsize=7, ha="right", va="center")

    def y_for(dt: datetime) -> float:
        minutes = (dt.hour - hour0) * 60 + dt.minute
        minutes = max(0, min(hours * 60, minutes))
        return grid_y + (minutes / (hours * 60)) * grid_h

    for i, d in enumerate(days):
        n = max(lanes[d], 1)
        for ev in timed_by[d]:
            x0 = gx0 + i * col_w + 0.004 + ev.lane * ((col_w - 0.008) / n)
            w = (col_w - 0.008) / n - 0.006
            y0 = y_for(ev.start)
            y1 = y_for(ev.end)
            h = max(y1 - y0, 0.028)
            fill = C_CLASH if ev.clash else (C_CONF if ev.status == "confirmed" else C_CAND)
            ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0.003,rounding_size=0.006", facecolor=fill, edgecolor="none", alpha=0.95))
            t0 = ev.start.strftime("%H:%M")
            t1 = ev.end.strftime("%H:%M")
            ax.text(x0 + 0.006, y0 + 0.008, f"{t0}–{t1}", color="#f8fbff", fontsize=6.5, va="top")
            ax.text(x0 + 0.006, y0 + 0.022, short_title(ev.title, 18 if n > 1 else 24), color="#f8fbff", fontsize=7.5, va="top", fontweight="bold")

    ax.text(0.02, 0.97, "Blau = bestätigt  ·  gedämpft = Kandidat  ·  orange = Zeitkonflikt", color=C_MUTED, fontsize=8, va="top")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor=C_BG)
    plt.close(fig)


def wrap(text: str, width: int) -> list[str]:
    return textwrap.wrap(text, width=width) or [""]


def draw_agenda(events: list[Event], week: date, today: date, path: Path) -> None:
    rows = [e for e in events if intersects_week(e, week)]
    last = week + timedelta(days=6)
    fig_h = max(12.0, 2.2 + 2.35 * max(len(rows), 1))
    fig = plt.figure(figsize=(12.0, fig_h), dpi=120, facecolor=C_BG)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.invert_yaxis()
    ax.axis("off")
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)

    ax.text(0.04, 0.02, f"Agenda  {week.day}. {MONTH_DE[week.month]} – {last.day}. {MONTH_DE[last.month]}", color=C_TEXT, fontsize=20, fontweight="bold", va="top")
    ax.text(0.04, 0.048, "WHAT · WHERE · WHEN · WHY  ·  sourced, no invented clocks", color=C_MUTED, fontsize=10, va="top")

    if not rows:
        ax.text(0.04, 0.12, "Keine Termine in dieser Woche.", color=C_MUTED, fontsize=14, va="top")
        path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, facecolor=C_BG)
        plt.close(fig)
        return

    top = 0.08
    gap = 0.012
    usable = 0.90
    card_h = min(0.22, (usable - gap * (len(rows) - 1)) / len(rows))
    for i, ev in enumerate(rows):
        y = top + i * (card_h + gap)
        fill = "#1c2430"
        edge = C_CLASH if ev.clash else (C_CONF if ev.status == "confirmed" else C_CAND)
        ax.add_patch(FancyBboxPatch((0.04, y), 0.92, card_h, boxstyle="round,pad=0.008,rounding_size=0.012", facecolor=fill, edgecolor=edge, linewidth=1.6))
        badge = "CONFIRMED" if ev.status == "confirmed" else "CANDIDATE"
        if ev.clash:
            badge += "  ·  CLASH"
        if ev.allday:
            when = f"{ev.start.date().isoformat()} – {(ev.end.date() - timedelta(days=1)).isoformat()}  ganztags"
        else:
            when = f"{ev.start.strftime('%Y-%m-%d  %H:%M')}–{ev.end.strftime('%H:%M')}  Europe/Berlin"
        ax.text(0.06, y + 0.012, ev.title, color=C_TEXT, fontsize=13, fontweight="bold", va="top")
        ax.text(0.94, y + 0.014, badge, color=edge, fontsize=8, ha="right", va="top")
        ax.text(0.06, y + 0.042, when, color=C_TODAY, fontsize=9, va="top")
        body_y = y + 0.062
        lines: list[str] = []
        lines.extend(wrap("WHERE  " + coarse_place(ev.where), 92)[:2])
        lines.extend(wrap("WHAT   " + ev.what, 92)[:3])
        lines.extend(wrap("WHY    " + coarse_place(ev.why), 92)[:3])
        if ev.url:
            lines.append(ev.url)
        for j, line in enumerate(lines[:9]):
            ax.text(0.06, body_y + j * 0.018, line, color=C_TEXT if j == 0 else C_MUTED, fontsize=8, va="top", family="DejaVu Sans")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor=C_BG)
    plt.close(fig)


def write_html(events: list[Event], weeks: list[date], today: date, path: Path) -> None:
    parts = [
        "<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'>",
        "<title>Schedule 7-day</title>",
        "<style>",
        "body{background:#0b0e12;color:#e8eaed;font:15px/1.45 system-ui,Segoe UI,sans-serif;margin:24px}",
        "h1,h2{font-weight:650} .muted{color:#9aa0a6}",
        "table{width:100%;border-collapse:collapse;table-layout:fixed;margin:12px 0 32px}",
        "th,td{border:1px solid #2a3140;vertical-align:top;padding:8px;background:#14181f}",
        "th.today{color:#8ab4f8} td.today{background:#1a2838}",
        ".chip{display:block;border-radius:6px;padding:4px 6px;margin:0 0 6px;color:#0b0e12;font-size:12px}",
        ".conf{background:#8ab4f8}.cand{background:#aecbfa}.clash{background:#fdc69c}",
        "article{border:1px solid #2a3140;border-radius:12px;padding:14px 16px;margin:0 0 12px;background:#14181f}",
        "article.conf{border-color:#1a73e8} article.clash{border-color:#e37400}",
        "</style></head><body>",
        f"<h1>Termine Europe/Berlin</h1><p class='muted'>Heute {today.isoformat()}. Bilder liegen daneben als PNG. tmp/ läuft nach 5 Tagen ab.</p>",
    ]
    upcoming = [e for e in events if (e.end.date() if e.allday else e.start.date()) >= today]
    for week in weeks:
        days = [week + timedelta(days=i) for i in range(7)]
        last = days[-1]
        parts.append(f"<h2>{week.day}. {MONTH_DE[week.month]} – {last.day}. {MONTH_DE[last.month]}</h2>")
        parts.append("<table><tr>")
        for d in days:
            cls = "today" if d == today else ""
            parts.append(f"<th class='{cls}'>{WD[(d - week).days]} {d.day}</th>")
        parts.append("</tr><tr>")
        for d in days:
            cls = "today" if d == today else ""
            parts.append(f"<td class='{cls}'>")
            for ev in events:
                if d not in dates_of(ev):
                    continue
                klass = "clash" if ev.clash else ("conf" if ev.status == "confirmed" else "cand")
                if ev.allday:
                    label = f"ganztags · {ev.title}"
                else:
                    label = f"{ev.start.strftime('%H:%M')}–{ev.end.strftime('%H:%M')} · {ev.title}"
                parts.append(f"<span class='chip {klass}'>{html_esc(label)}</span>")
            parts.append("</td>")
        parts.append("</tr></table>")
    parts.append("<h2>Liste mit Details</h2>")
    for ev in upcoming:
        klass = "clash" if ev.clash else ("conf" if ev.status == "confirmed" else "")
        if ev.allday:
            when = f"{ev.start.date()} – {ev.end.date() - timedelta(days=1)} ganztags"
        else:
            when = f"{ev.start.strftime('%Y-%m-%d %H:%M')}–{ev.end.strftime('%H:%M')}"
        badge = "confirmed" if ev.status == "confirmed" else "candidate"
        if ev.clash:
            badge += " · clash"
        parts.append(f"<article class='{klass}'>")
        parts.append(f"<h3>{html_esc(ev.title)}</h3>")
        parts.append(f"<p class='muted'>{html_esc(badge)} · {html_esc(when)}</p>")
        parts.append(f"<p><b>WHERE</b> {html_esc(coarse_place(ev.where))}</p>")
        parts.append(f"<p><b>WHAT</b> {html_esc(ev.what)}</p>")
        parts.append(f"<p><b>WHY</b> {html_esc(coarse_place(ev.why))}</p>")
        if ev.url:
            parts.append(f"<p><a href='{html_esc(ev.url)}'>{html_esc(ev.url)}</a></p>")
        parts.append("</article>")
    parts.append("</body></html>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(parts), encoding="utf-8")


def html_esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def cjk_font():
    from matplotlib import font_manager

    for name in ("Microsoft YaHei", "Microsoft JhengHei", "SimHei", "Segoe UI"):
        try:
            path = font_manager.findfont(font_manager.FontProperties(family=name), fallback_to_default=False)
            if path and "DejaVu" not in path:
                return font_manager.FontProperties(fname=path)
        except (ValueError, OSError):
            continue
    return font_manager.FontProperties()


def events_on(events: list[Event], day: date) -> list[Event]:
    return [e for e in events if day in dates_of(e)]


def event_row(ev: Event) -> tuple[str, str, str, str]:
    when = "ganztags" if ev.allday else ev.start.strftime("%H:%M")
    fill = C_CLASH if ev.clash else (C_CONF if ev.status == "confirmed" else C_CAND)
    body = coarse_place(ev.where or ev.what) or ev.status
    return (when, short_title(ev.title, 42), body[:90], fill)


def draw_plate(today: date, path: Path) -> None:
    """Share card for today's plate. Friend-facing. No streets, halls, or ID."""
    fp = cjk_font()
    fig = plt.figure(figsize=(9.0, 12.0), dpi=140, facecolor=C_BG)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.invert_yaxis()
    ax.axis("off")
    ax.set_facecolor(C_BG)
    fig.patch.set_facecolor(C_BG)

    wd = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")[today.weekday()]
    ax.text(0.07, 0.04, "HEUTIGER TELLER", color=C_TODAY, fontsize=11, fontproperties=fp, fontweight="bold", va="top")
    ax.text(0.07, 0.075, f"{wd}  {today.day}. {MONTH_DE[today.month]} {today.year}", color=C_TEXT, fontsize=22, fontproperties=fp, fontweight="bold", va="top")
    ax.text(0.07, 0.125, "TZ Europe/Berlin  ·  sourced schedule", color=C_MUTED, fontsize=11, fontproperties=fp, va="top")

    day_events = events_on(load_events(today), today)
    cards = [event_row(ev) for ev in day_events[:6]]
    if not cards:
        cards = [("—", "Keine Termine", "Nichts in der Store für heute.", C_CAND)]
    top = 0.17
    h = 0.12
    gap = 0.018
    for i, (when, title, body, fill) in enumerate(cards):
        y = top + i * (h + gap)
        ax.add_patch(
            FancyBboxPatch(
                (0.07, y),
                0.86,
                h,
                boxstyle="round,pad=0.008,rounding_size=0.02",
                facecolor=C_PANEL,
                edgecolor=C_GRID,
                linewidth=1.0,
            )
        )
        ax.add_patch(Rectangle((0.07, y), 0.012, h, facecolor=fill, edgecolor="none"))
        ax.text(0.11, y + 0.018, when, color=fill, fontsize=11, fontproperties=fp, fontweight="bold", va="top")
        ax.text(0.28, y + 0.018, title, color=C_TEXT, fontsize=15, fontproperties=fp, fontweight="bold", va="top")
        ax.text(0.11, y + 0.052, body, color=C_MUTED, fontsize=11, fontproperties=fp, va="top", linespacing=1.45)

    ax.text(0.07, 0.96, "keine Straße  ·  keine Hallen-ID  ·  keine Ausweiszeile", color=C_MUTED, fontsize=9, fontproperties=fp, va="top")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor=C_BG)
    plt.close(fig)


def draw_next_board(path: Path, kicker: str, title: str, sub: str, rows: list[tuple[str, str, str, str]], chips: list[str], foot: str) -> None:
    fp = cjk_font()
    fig = plt.figure(figsize=(8.5, 11.0), dpi=140, facecolor=C_BG)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.invert_yaxis()
    ax.axis("off")
    ax.set_facecolor(C_PANEL)
    fig.patch.set_facecolor(C_BG)
    ax.add_patch(FancyBboxPatch((0.04, 0.03), 0.92, 0.94, boxstyle="round,pad=0.01,rounding_size=0.03", facecolor=C_PANEL, edgecolor=C_GRID, linewidth=1.0))
    ax.text(0.08, 0.06, kicker, color=C_TODAY, fontsize=11, fontproperties=fp, fontweight="bold", va="top")
    ax.text(0.08, 0.10, title, color=C_TEXT, fontsize=26, fontproperties=fp, fontweight="bold", va="top")
    ax.text(0.08, 0.16, sub, color=C_MUTED, fontsize=12, fontproperties=fp, va="top")
    top = 0.22
    h = 0.13
    gap = 0.018
    for i, (when, head, body, fill) in enumerate(rows):
        y = top + i * (h + gap)
        ax.add_patch(FancyBboxPatch((0.08, y), 0.84, h, boxstyle="round,pad=0.008,rounding_size=0.02", facecolor=C_BG, edgecolor=C_GRID, linewidth=1.0))
        ax.add_patch(Rectangle((0.08, y), 0.012, h, facecolor=fill, edgecolor="none"))
        ax.text(0.12, y + 0.018, when, color=fill, fontsize=12, fontproperties=fp, fontweight="bold", va="top")
        ax.text(0.12, y + 0.048, head, color=C_TEXT, fontsize=16, fontproperties=fp, fontweight="bold", va="top")
        ax.text(0.12, y + 0.078, body, color=C_MUTED, fontsize=11, fontproperties=fp, va="top", linespacing=1.4)
    ax.text(0.08, 0.88, "   ·   ".join(chips), color=C_MUTED, fontsize=10, fontproperties=fp, va="top")
    ax.text(0.08, 0.93, foot, color=C_MUTED, fontsize=10, fontproperties=fp, va="top")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, facecolor=C_BG)
    plt.close(fig)


def draw_next_pack(out: Path, today: date) -> list[Path]:
    written: list[Path] = []
    events = load_events(today)
    wd = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")
    boards: list[tuple] = []
    for offset, name in ((0, "next-01-today.png"), (1, "next-02-plus1.png"), (2, "next-03-plus2.png")):
        day = today + timedelta(days=offset)
        rows = [event_row(ev) for ev in events_on(events, day)[:4]]
        if not rows:
            rows = [("—", "Keine Termine", "Nichts in der Store.", C_CAND)]
        boards.append(
            (
                out / name,
                f"TAG  ·  {wd[day.weekday()].upper()}",
                f"{day.day}. {MONTH_DE[day.month]} {day.year}",
                "Titel und Uhr. Keine Straße, keine Hallen-ID.",
                rows,
                ["sourced", "coarse place"],
                "schedule/  ·  tmp/schedule/",
            )
        )
    for item in boards:
        draw_next_board(*item)
        written.append(item[0])
    return written


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--today", default="")
    p.add_argument("--plate", action="store_true")
    p.add_argument("--next", action="store_true")
    args = p.parse_args()
    today = date.fromisoformat(args.today) if args.today else datetime.now(TZ).date()
    if args.next:
        OUT.mkdir(parents=True, exist_ok=True)
        written = draw_next_pack(OUT, today)
        take = splice_private_take()
        stamp_ttl()
        for path in written:
            print(path.relative_to(ROOT).as_posix())
        print(take.relative_to(ROOT).as_posix())
        return 0
    if args.plate:
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / f"plate-{today.isoformat()}.png"
        draw_plate(today, path)
        take = splice_private_take()
        stamp_ttl()
        print(path.relative_to(ROOT).as_posix())
        print(take.relative_to(ROOT).as_posix())
        return 0
    events = load_events()
    weeks = weeks_covering(events, today)
    OUT.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for week in weeks:
        week_path = OUT / f"week-{week.isoformat()}.png"
        agenda_path = OUT / f"agenda-{week.isoformat()}.png"
        draw_week(events, week, today, week_path)
        draw_agenda(events, week, today, agenda_path)
        written.extend([week_path, agenda_path])
    html_path = OUT / "upcoming.html"
    write_html(events, weeks, today, html_path)
    written.append(html_path)
    now_week = sunday_of(today)
    alias = OUT / "week-now.png"
    src = OUT / f"week-{now_week.isoformat()}.png"
    if src.exists():
        alias.write_bytes(src.read_bytes())
        written.append(alias)
    take = splice_private_take()
    written.append(take)
    stamp_ttl()
    for path in written:
        print(path.relative_to(ROOT).as_posix())
    print(f"n={len(written)} today={today.isoformat()} weeks={len(weeks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
