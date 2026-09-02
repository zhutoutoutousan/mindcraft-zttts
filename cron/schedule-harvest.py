#!/usr/bin/env python3
"""Harvest dated events from CPU, inflow, dumps into schedule/.

    python cron/schedule-harvest.py --dry-run
    python cron/schedule-harvest.py --apply
    python cron/schedule-harvest.py --ics
"""
from __future__ import annotations

import argparse
import hashlib
import re
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
CPU = ROOT / "CPU.md"
INFLOW_STATE = ROOT / "inflow" / "STATE.md"
INFLOW_FU = ROOT / "inflow" / "inflow.fu.md"
INFLOW_TEX = ROOT / "inflow" / "briefing.tex"
PRIVATE = ROOT / ".private"
SCHEDULE = ROOT / "schedule"
TOON = SCHEDULE / "harvest.toon.md"
ENRICH = SCHEDULE / "enrich.toon.md"
TZ = ZoneInfo("Europe/Berlin")
YEAR = 2026
MONTH_NAMES = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}
SKIP_SLUG = (
    "aws-sandbox",
    "ifa-post-human",
    "goethe-b2",
    "arxiv",
    "kvcached",
    "nature-",
    "stripe-",
    "namelos",
    "forbes",
    "ng-three",
    "evoclaw",
    "pythia",
    "nibblepos",
    "kassensichv",
    "fiskaly",
    "cursor-agent",
    "gastro-",
    "agentcore-cedar",
    "metr-hf",
    "jugend-debattiert",
    "b2-",
)


def say(text: str) -> None:
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", "replace").decode("ascii"))


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:60] or hashlib.sha1(text.encode()).hexdigest()[:12]


def parse_hhmm(raw: str) -> tuple[int, int]:
    h, m = raw.split(":")
    return int(h), int(m)


def dt_at(year: int, month: int, day: int, hh: int = 0, mm: int = 0) -> datetime:
    return datetime(year, month, day, hh, mm, tzinfo=TZ)


def ev(
    eid: str,
    start: datetime,
    end: datetime | None,
    title: str,
    where: str,
    status: str,
    source: str,
    url: str = "",
    allday: bool = False,
    what: str = "",
    why: str = "",
) -> dict:
    if end is None:
        end = start + timedelta(hours=1)
    return {
        "id": eid,
        "start": start.isoformat(timespec="minutes"),
        "end": end.isoformat(timespec="minutes"),
        "title": " ".join(title.split()),
        "where": where.strip(),
        "status": status,
        "source": source,
        "url": url,
        "allday": "true" if allday else "false",
        "what": what.strip(),
        "why": why.strip(),
        "gap": "true",
    }


def extract_url(text: str) -> str:
    m = re.search(r"https?://\S+", text)
    return m.group(0).rstrip(").,;") if m else ""


def parse_schedule_lines(text: str, source: str, status: str) -> list[dict]:
    out: list[dict] = []
    for line in text.splitlines():
        m = re.match(r"^-\s+SCHEDULE\s+(.+)$", line.strip())
        if not m:
            continue
        payload = m.group(1).strip()
        url = extract_url(payload)
        range_m = re.match(
            r"^(\d{4})-(\d{2})-(\d{2})[–-](\d{2})\s+(.*)$",
            payload,
        )
        if range_m:
            y, mo, d1, d2, rest = range_m.groups()
            start = dt_at(int(y), int(mo), int(d1))
            end = dt_at(int(y), int(mo), int(d2)) + timedelta(days=1)
            out.append(ev(slug(rest)[:40], start, end, rest, "", status, source, url, True))
            continue
        day_m = re.match(
            r"^(\d{4})-(\d{2})-(\d{2})(?:\s+(\d{1,2}:\d{2})(?:[–-](\d{1,2}:\d{2}))?)?\s+(.*)$",
            payload,
        )
        if not day_m:
            continue
        y, mo, d, t1, t2, rest = day_m.groups()
        dur = re.search(r"~(\d+)\s*min", rest)
        if t1:
            hh, mm = parse_hhmm(t1)
            start = dt_at(int(y), int(mo), int(d), hh, mm)
            if t2:
                h2, m2 = parse_hhmm(t2)
                end = dt_at(int(y), int(mo), int(d), h2, m2)
            elif dur:
                end = start + timedelta(minutes=int(dur.group(1)))
            else:
                end = start + timedelta(hours=2)
            out.append(ev(slug(rest)[:40], start, end, rest, "", status, source, url))
        else:
            start = dt_at(int(y), int(mo), int(d))
            out.append(
                ev(slug(rest)[:40], start, start + timedelta(days=1), rest, "", status, source, url, True)
            )
    return out


def parse_state_slugs(text: str, source: str) -> list[dict]:
    out: list[dict] = []
    for line in text.splitlines():
        m = re.match(r"^-\s+\d{4}-\d{2}-\d{2}-\d{4}\s+(\S+)$", line.strip())
        if not m:
            continue
        sid = m.group(1)
        if sid.endswith("-reminder") or "-reminder-" in sid:
            continue
        if any(sid.startswith(p) or p in sid for p in SKIP_SLUG):
            continue
        dm = re.search(r"(20\d{2})-(\d{2})-(\d{2})(?:-(\d{2}))?$", sid)
        if not dm:
            continue
        y, mo, d1, d2 = dm.group(1), dm.group(2), dm.group(3), dm.group(4)
        title = re.sub(r"-20\d{2}-\d{2}-\d{2}(?:-\d{2})?$", "", sid).replace("-", " ")
        start = dt_at(int(y), int(mo), int(d1))
        if d2:
            end = dt_at(int(y), int(mo), int(d2)) + timedelta(days=1)
        else:
            end = start + timedelta(days=1)
        out.append(ev(sid, start, end, title, "", "candidate", source, "", True))
    return out


def parse_briefing(text: str, source: str) -> list[dict]:
    cut = re.search(r"\\selectlanguage\{ngerman\}", text)
    if cut:
        text = text[: cut.start()]
    out: list[dict] = []
    year = YEAR
    dm = re.search(r"(\d{1,2})\s+September\s+(20\d{2})", text)
    if dm:
        year = int(dm.group(2))
    plain = text.replace("~", " ").replace("\\emph{", "").replace("\\textbf{", "")
    plain = re.sub(r"\\url\{([^}]+)\}", r" \1 ", plain)
    plain = re.sub(r"[{}]", "", plain)
    for m in re.finditer(
        r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+(\d{1,2})\s+Sep(?:tember)?\s+(\d{1,2}:\d{2})(?:--(\d{1,2}:\d{2}))?[,\s]+([^\n]+)",
        plain,
    ):
        day = int(m.group(2))
        hh, mm = parse_hhmm(m.group(3))
        start = dt_at(year, 9, day, hh, mm)
        if m.group(4):
            h2, m2 = parse_hhmm(m.group(4))
            end = dt_at(year, 9, day, h2, m2)
        else:
            end = start + timedelta(hours=2)
        rest = re.sub(r"\s+", " ", m.group(5))[:180]
        out.append(ev(slug(rest)[:40], start, end, rest, "", "candidate", source, extract_url(m.group(0))))
    for m in re.finditer(
        r"(\d{1,2})\.(\d{2})(?:\.(20\d{2}))?\s+(\d{1,2}:\d{2})(?:--(\d{1,2}:\d{2}))?\s+([^\n]+)",
        plain,
    ):
        day, month = int(m.group(1)), int(m.group(2))
        y = int(m.group(3)) if m.group(3) else year
        hh, mm = parse_hhmm(m.group(4))
        start = dt_at(y, month, day, hh, mm)
        if m.group(5):
            h2, m2 = parse_hhmm(m.group(5))
            end = dt_at(y, month, day, h2, m2)
        else:
            end = start + timedelta(hours=1)
        rest = re.split(r"\s+Then\s+|\s+\d{1,2}:\d{2}", re.sub(r"\s+", " ", m.group(6)), maxsplit=1)[0][:180]
        if "cannot go" in rest.lower() or "invite-only" in rest.lower():
            continue
        if len(rest.strip()) < 8:
            continue
        out.append(ev(slug(rest)[:40], start, end, rest, "", "candidate", source, extract_url(m.group(0))))
    for m in re.finditer(
        r"IFA\s+(\d{1,2})--(\d{1,2})\s+Sep",
        plain,
        re.I,
    ):
        d1, d2 = int(m.group(1)), int(m.group(2))
        start = dt_at(year, 9, d1)
        end = dt_at(year, 9, d2) + timedelta(days=1)
        out.append(
            ev(
                "ifa-berlin",
                start,
                end,
                "IFA Berlin",
                "Messe Berlin",
                "candidate",
                source,
                "https://www.ifa-berlin.com/de/",
                True,
            )
        )
    for m in re.finditer(
        r"(\d{1,2})--(\d{1,2})\s+Sep:?\s*([^.\n]+)",
        plain,
    ):
        d1, d2 = int(m.group(1)), int(m.group(2))
        rest = re.sub(r"\s+", " ", m.group(3)).strip()
        if rest.lower().startswith("ifa"):
            continue
        start = dt_at(year, 9, d1)
        end = dt_at(year, 9, d2) + timedelta(days=1)
        out.append(ev(slug(rest)[:40], start, end, rest, "", "candidate", source, "", True))
    return out


def collect() -> list[dict]:
    rows: list[dict] = []
    if CPU.exists():
        rows.extend(parse_schedule_lines(CPU.read_text(encoding="utf-8"), "CPU.md", "confirmed"))
    if PRIVATE.exists():
        for path in PRIVATE.glob("*.fu.md"):
            rows.extend(parse_schedule_lines(path.read_text(encoding="utf-8"), path.as_posix(), "confirmed"))
    if INFLOW_STATE.exists():
        rows.extend(parse_state_slugs(INFLOW_STATE.read_text(encoding="utf-8"), "inflow/STATE.md"))
    if INFLOW_FU.exists():
        rows.extend(parse_schedule_lines(INFLOW_FU.read_text(encoding="utf-8"), "inflow/inflow.fu.md", "candidate"))
    if INFLOW_TEX.exists():
        rows.extend(parse_briefing(INFLOW_TEX.read_text(encoding="utf-8"), "inflow/briefing.tex"))
    for dump in (ROOT / "raw").glob("*.fu.md") if (ROOT / "raw").exists() else []:
        rows.extend(parse_schedule_lines(dump.read_text(encoding="utf-8"), dump.as_posix(), "candidate"))
    return merge_enrich(dedup(rows))


def rank(row: dict) -> tuple:
    st = 0 if row["status"] == "confirmed" else 1
    timed = 0 if row["allday"] == "false" else 1
    return (st, timed, row["start"], row["id"])


def junk(row: dict) -> bool:
    t = row["title"].strip().lower()
    if len(t) < 8 or t.startswith(","):
        return True
    if any(x in t for x in ("forumsbeitrag", "morgen agentur", "post human", "invite-only", "cannot go")):
        return True
    if "\\" in row["title"] or "$" in row["title"]:
        return True
    return False


def norm_title(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())[:20]


def dedup(rows: list[dict]) -> list[dict]:
    rows = [r for r in rows if not junk(r)]
    rows = sorted(rows, key=rank)
    kept: list[dict] = []
    for row in rows:
        n = norm_title(row["title"])
        day = row["start"][:10]
        dup = False
        for k in kept:
            if k["start"][:10] != day:
                continue
            kn = norm_title(k["title"])
            if n[:8] and kn[:8] and (n[:8] in kn or kn[:8] in n):
                dup = True
                break
            if n[:3] and kn[:3] == n[:3] and (
                (row["allday"] == "true" and k["allday"] == "false")
                or (row["allday"] == "false" and k["allday"] == "false" and row["start"][:16] == k["start"][:16])
            ):
                dup = True
                break
        if not dup:
            kept.append(row)
    kept.sort(key=lambda r: (r["start"], r["id"]))
    return kept


def parse_enrich(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    cur: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip() == "record:":
            if cur.get("match"):
                records.append(cur)
            cur = {}
            continue
        m = re.match(r"^\s{2}([a-z]+):\s*(.*)$", line)
        if m:
            cur[m.group(1)] = m.group(2).strip()
    if cur.get("match"):
        records.append(cur)
    return records


def find_enrich(row: dict, records: list[dict]) -> dict | None:
    hay_id = row["id"].lower().replace("-", " ")
    hay_title = row["title"].lower()
    id_hits = [rec for rec in records if rec["match"].lower() in hay_id]
    if id_hits:
        return max(id_hits, key=lambda rec: len(rec["match"]))
    title_hits = [rec for rec in records if rec["match"].lower() in hay_title]
    if title_hits:
        return max(title_hits, key=lambda rec: len(rec["match"]))
    return None


def merge_enrich(rows: list[dict]) -> list[dict]:
    records = parse_enrich(ENRICH)
    used: set[str] = set()
    for row in rows:
        hit = find_enrich(row, records)
        row.setdefault("what", "")
        row.setdefault("why", "")
        if not hit:
            row["gap"] = "true"
            continue
        used.add(hit["match"])
        if hit.get("title"):
            row["title"] = hit["title"]
        if hit.get("where"):
            row["where"] = hit["where"]
        if hit.get("url"):
            row["url"] = hit["url"]
        if hit.get("what"):
            row["what"] = hit["what"]
        if hit.get("why"):
            row["why"] = hit["why"]
        extra = hit.get("source", "")
        if extra and extra not in row["source"]:
            row["source"] = f"{row['source']}; {extra}"
        if hit.get("when"):
            row["start"] = hit["when"]
        if hit.get("end"):
            row["end"] = hit["end"]
        if hit.get("allday"):
            row["allday"] = hit["allday"]
        missing = not (row["what"] and row["where"] and row["why"] and row["title"])
        row["gap"] = "true" if missing else "false"
    leftover = [rec["match"] for rec in records if rec["match"] not in used]
    if leftover:
        say("enrich unused: " + "; ".join(leftover))
    rows.sort(key=lambda r: (r["start"], r["id"]))
    return rows


def csv_cell(text: str) -> str:
    return " ".join(text.replace(",", ";").split())


def write_toon(rows: list[dict]) -> None:
    SCHEDULE.mkdir(parents=True, exist_ok=True)
    lines = [
        "schema: schedule/harvest",
        "tz: Europe/Berlin",
        "note: merge schedule/enrich.toon.md. Slug titles are gaps. ICS only when the human asks --ics.",
        f"updated: {datetime.now(TZ).isoformat(timespec='minutes')}",
        f"n: {len(rows)}",
        "nodes[]{id,start,end,title,where,status,source,url,allday,what,why,gap}:",
    ]
    for r in rows:
        lines.append(
            "  "
            + ",".join(
                [
                    r["id"],
                    r["start"],
                    r["end"],
                    csv_cell(r["title"]),
                    csv_cell(r["where"]),
                    r["status"],
                    csv_cell(r["source"]),
                    r["url"],
                    r["allday"],
                    csv_cell(r.get("what", "")),
                    csv_cell(r.get("why", "")),
                    r.get("gap", "true"),
                ]
            )
        )
    TOON.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_month_fu(rows: list[dict]) -> None:
    by_month: dict[str, list[dict]] = {}
    for r in rows:
        key = r["start"][:7]
        by_month.setdefault(key, []).append(r)
    for key, group in by_month.items():
        y, m = key.split("-")
        path = SCHEDULE / f"{y}-{int(m)}.fu.md"
        lines = [
            f"- KIND month schedule store. Harvested then web-enriched. ICS is not this file. Ask for python cron/schedule-harvest.py --ics.",
            f"- TZ Europe/Berlin",
            f"- STORE PATH schedule/harvest.toon.md",
            f"- STORE PATH schedule/enrich.toon.md",
            f"- MONTH {key}",
        ]
        for r in group:
            start = r["start"]
            day = start[:10]
            timebit = "" if r["allday"] == "true" else start[11:16]
            endbit = "" if r["allday"] == "true" else r["end"][11:16]
            when = day if not timebit else f"{day} {timebit}" + (f"–{endbit}" if endbit else "")
            lines.append(f"- SCHEDULE {when} {r['title']}")
            if r.get("what"):
                lines.append(f"  - WHAT {r['what']}")
            if r.get("where"):
                lines.append(f"  - WHERE {r['where']}")
            lines.append(f"  - WHEN {when} Europe/Berlin")
            if r.get("why"):
                lines.append(f"  - WHY {r['why']}")
            if r.get("url"):
                lines.append(f"  - URL {r['url']}")
            lines.append(f"  - STATUS {r['status']}")
            lines.append(f"  - SOURCE {r['source']}")
            if r.get("gap") == "true":
                lines.append("  - GAP browse the open web until WHAT WHERE WHEN WHY and a human name exist. Do not invent.")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def fold(line: str) -> str:
    if len(line) <= 74:
        return line
    parts = [line[:74]]
    rest = line[74:]
    while rest:
        parts.append(" " + rest[:73])
        rest = rest[73:]
    return "\r\n".join(parts)


def ics_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def when_text(row: dict) -> str:
    start = row["start"]
    if row["allday"] == "true":
        end_incl = (datetime.fromisoformat(row["end"]) - timedelta(days=1)).strftime("%Y-%m-%d")
        start_d = start[:10]
        if start_d == end_incl:
            return f"{start_d} all day, Europe/Berlin"
        return f"{start_d} – {end_incl}, Europe/Berlin"
    return f"{start[:10]} {start[11:16]}–{row['end'][11:16]} Europe/Berlin"


def ics_description(row: dict) -> str:
    chunks: list[str] = []
    if row.get("what"):
        chunks.append(row["what"])
    meta = []
    if row.get("where"):
        meta.append(f"Where: {row['where']}")
    meta.append(f"When: {when_text(row)}")
    chunks.append("\n".join(meta))
    if row.get("why"):
        chunks.append(row["why"])
    if row.get("url"):
        chunks.append(row["url"])
    return ics_escape("\n\n".join(chunks))


def ics_stamp(iso: str, allday: bool) -> str:
    if allday:
        return iso[:10].replace("-", "")
    local = iso.split("+", 1)[0].split("Z", 1)[0]
    digits = re.sub(r"[^0-9T]", "", local)
    if "T" in digits and len(digits) == 13:
        digits += "00"
    return digits[:15]


def write_ics(rows: list[dict]) -> Path:
    out = SCHEDULE / "calendar.ics"
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//mindcraft-zttts//schedule-harvest//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:mindcraft schedule",
        "X-WR-TIMEZONE:Europe/Berlin",
    ]
    for r in rows:
        allday = r["allday"] == "true"
        stamp = datetime.now(TZ).strftime("%Y%m%dT%H%M%S")
        lines.append("BEGIN:VEVENT")
        lines.append(fold(f"UID:{r['id']}@mindcraft-zttts"))
        lines.append(f"DTSTAMP:{stamp}")
        lines.append(f"LAST-MODIFIED:{stamp}")
        lines.append("SEQUENCE:2")
        if allday:
            lines.append(f"DTSTART;VALUE=DATE:{ics_stamp(r['start'], True)}")
            lines.append(f"DTEND;VALUE=DATE:{ics_stamp(r['end'], True)}")
        else:
            lines.append(f"DTSTART;TZID=Europe/Berlin:{ics_stamp(r['start'], False)}")
            lines.append(f"DTEND;TZID=Europe/Berlin:{ics_stamp(r['end'], False)}")
        lines.append(fold(f"SUMMARY:{ics_escape(r['title'])}"))
        if r["where"]:
            lines.append(fold(f"LOCATION:{ics_escape(r['where'])}"))
        if r["url"]:
            lines.append(fold(f"URL:{r['url']}"))
        lines.append(fold(f"DESCRIPTION:{ics_description(r)}"))
        lines.append("STATUS:" + ("CONFIRMED" if r["status"] == "confirmed" else "TENTATIVE"))
        lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    out.write_bytes(("\r\n".join(lines) + "\r\n").encode("utf-8"))
    return out


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--ics", action="store_true")
    args = p.parse_args()
    n = sum(bool(x) for x in [args.dry_run, args.apply, args.ics])
    if n != 1:
        raise SystemExit("choose exactly one of --dry-run --apply --ics")
    if args.ics:
        rows = collect()
        path = write_ics(rows)
        say(path.as_posix())
        return
    rows = collect()
    if args.apply:
        write_toon(rows)
        write_month_fu(rows)
        say(TOON.as_posix())
        say(ENRICH.as_posix())
    gaps = [r for r in rows if r.get("gap") == "true"]
    say(f"n={len(rows)} gaps={len(gaps)}")
    for r in rows:
        flag = "GAP" if r.get("gap") == "true" else "ok "
        loc = (r.get("where") or "-")[:40]
        say(f"{flag} {r['status']:10} {r['start']} {r['title'][:50]} | {loc}")


if __name__ == "__main__":
    main()
