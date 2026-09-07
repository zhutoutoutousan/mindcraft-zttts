#!/usr/bin/env python3
"""Routine due-check and today slice for self/routine.toon.md.

    python cron/routine-enrich.py --due
    python cron/routine-enrich.py --today
    python cron/routine-enrich.py --mark-done brush-am
    python cron/routine-enrich.py --mark-periodic dental-checkup --date 2026-09-01

Does not invent last_done. Does not diagnose. Tips stay human/agent sourced.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORE = ROOT / "self" / "routine.toon.md"


def read() -> str:
    return STORE.read_text(encoding="utf-8") if STORE.exists() else ""


def write(text: str) -> None:
    STORE.write_text(text, encoding="utf-8")


def berlin_today() -> date:
    try:
        from zoneinfo import ZoneInfo

        return datetime.now(ZoneInfo("Europe/Berlin")).date()
    except Exception:
        return date.today()


def parse_daily(text: str) -> list[dict]:
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("daily["):
            started = True
            continue
        if started and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            break
        if started and re.match(r"^\s+\S+,", line):
            # id,slot,label,label_zh,active,minutes,protocol,source
            parts = _split_csvish(line.strip())
            if len(parts) >= 5:
                rows.append(
                    {
                        "id": parts[0],
                        "slot": parts[1],
                        "label": parts[2],
                        "label_zh": parts[3] if len(parts) > 3 else "",
                        "active": (parts[4] if len(parts) > 4 else "true").lower()
                        == "true",
                        "minutes": parts[5] if len(parts) > 5 else "",
                        "protocol": parts[6] if len(parts) > 6 else "",
                        "source": parts[7] if len(parts) > 7 else "",
                    }
                )
    return rows


def parse_periodic(text: str) -> list[dict]:
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("periodic["):
            started = True
            continue
        if started and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            break
        if started and re.match(r"^\s+\S+,", line):
            parts = _split_csvish(line.strip())
            if len(parts) >= 4:
                rows.append(
                    {
                        "id": parts[0],
                        "label": parts[1],
                        "label_zh": parts[2],
                        "interval_months": int(parts[3] or 0),
                        "last_done": parts[4] if len(parts) > 4 else "",
                        "next_due": parts[5] if len(parts) > 5 else "",
                        "status": parts[6] if len(parts) > 6 else "open",
                        "source": parts[7] if len(parts) > 7 else "",
                        "note": parts[8] if len(parts) > 8 else "",
                    }
                )
    return rows


def parse_optimize(text: str) -> list[dict]:
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("optimize["):
            started = True
            continue
        if started and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            break
        if started and re.match(r"^\s+\S+,", line):
            parts = _split_csvish(line.strip())
            if len(parts) >= 5:
                rows.append(
                    {
                        "id": parts[0],
                        "habit": parts[1],
                        "change": parts[2],
                        "why": parts[3],
                        "status": parts[4],
                        "source": parts[5] if len(parts) > 5 else "",
                    }
                )
    return rows


def parse_tips(text: str) -> list[dict]:
    rows = []
    started = False
    for line in text.splitlines():
        if line.startswith("tip["):
            started = True
            continue
        if started and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            break
        if started and re.match(r"^\s+\S+,", line):
            parts = _split_csvish(line.strip())
            if len(parts) >= 4:
                rows.append(
                    {
                        "id": parts[0],
                        "topic": parts[1],
                        "text": parts[2],
                        "source": parts[3],
                        "added": parts[4] if len(parts) > 4 else "",
                    }
                )
    return rows


def _split_csvish(line: str) -> list[str]:
    """Split on commas not inside double quotes."""
    out = []
    cur = []
    in_q = False
    for ch in line:
        if ch == '"':
            in_q = not in_q
            cur.append(ch)
        elif ch == "," and not in_q:
            out.append("".join(cur).strip().strip('"'))
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip().strip('"'))
    return out


def add_months(d: date, months: int) -> date:
    m = d.month - 1 + months
    y = d.year + m // 12
    m = m % 12 + 1
    day = min(d.day, [31, 29 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1])
    return date(y, m, day)


def compute_due(rows: list[dict], today: date) -> list[dict]:
    out = []
    for r in rows:
        item = dict(r)
        last = r.get("last_done") or ""
        nxt = r.get("next_due") or ""
        interval = int(r.get("interval_months") or 0)
        if last and interval:
            try:
                ld = date.fromisoformat(last[:10])
                computed = add_months(ld, interval)
                item["next_due"] = computed.isoformat()
                nxt = item["next_due"]
            except ValueError:
                pass
        if not last:
            item["due_state"] = "ask-human-log-last"
        elif nxt:
            try:
                nd = date.fromisoformat(nxt[:10])
                if nd <= today:
                    item["due_state"] = "due"
                elif nd <= today + timedelta(days=30):
                    item["due_state"] = "soon"
                else:
                    item["due_state"] = "ok"
            except ValueError:
                item["due_state"] = "ask-human"
        else:
            item["due_state"] = "ask-human"
        out.append(item)
    return out


def cmd_due() -> int:
    text = read()
    today = berlin_today()
    due = compute_due(parse_periodic(text), today)
    print(f"TODAY {today.isoformat()} Europe/Berlin")
    for r in due:
        print(
            f"  [{r['due_state']}] {r['id']}  last={r.get('last_done') or '—'}  "
            f"next={r.get('next_due') or '—'}  {r['label']}"
        )
    return 0


def cmd_today() -> int:
    text = read()
    today = berlin_today()
    daily = [d for d in parse_daily(text) if d.get("active")]
    due = compute_due(parse_periodic(text), today)
    opts = [o for o in parse_optimize(text) if o.get("status") == "open"]
    tips = parse_tips(text)[-3:]
    print(f"# routine today {today.isoformat()}")
    print("## daily")
    for d in daily:
        print(f"- [{d['slot']}] {d['id']}: {d['label']} / {d['label_zh']} ({d['minutes']}m)")
        if d.get("protocol"):
            print(f"  protocol: {d['protocol'][:160]}")
    print("## periodic")
    for r in due:
        if r["due_state"] in ("due", "soon", "ask-human-log-last"):
            print(
                f"- [{r['due_state']}] {r['id']}: {r['label']} / {r['label_zh']} "
                f"(every {r['interval_months']}mo)"
            )
    print("## optimize open")
    for o in opts[:3]:
        print(f"- {o['id']}: {o['change']} ({o['why'][:100]})")
    print("## recent tips")
    for t in tips:
        print(f"- {t['id']}: {t['text'][:120]}")
    return 0


def append_log(hid: str, note: str = "") -> None:
    today = berlin_today().isoformat()
    text = read()
    if "log[]" not in text:
        text += "\nlog[]{{date,id,done,note}}:\n"
    line = f"  {today},{hid},true,{note or 'logged'}\n"
    # insert before agentHints if present
    if "agentHints[" in text:
        text = text.replace("agentHints[", line + "agentHints[", 1)
    else:
        text += line
    # bump updated
    text = re.sub(
        r"^updated:.*$",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        text,
        count=1,
        flags=re.M,
    )
    write(text)


def mark_periodic(pid: str, when: str) -> None:
    text = read()
    rows = parse_periodic(text)
    target = next((r for r in rows if r["id"] == pid), None)
    if not target:
        raise SystemExit(f"unknown periodic id {pid}")
    d = date.fromisoformat(when[:10])
    nxt = add_months(d, int(target["interval_months"] or 0)).isoformat()
    # rewrite periodic line
    new_lines = []
    in_per = False
    for line in text.splitlines():
        if line.startswith("periodic["):
            in_per = True
            new_lines.append(line)
            continue
        if in_per and re.match(r"^[a-zA-Z]", line) and not line.startswith(" "):
            in_per = False
        if in_per and line.strip().startswith(pid + ","):
            parts = _split_csvish(line.strip())
            # id,label,label_zh,interval,last,next,status,source,note
            while len(parts) < 9:
                parts.append("")
            parts[4] = d.isoformat()
            parts[5] = nxt
            parts[6] = "scheduled" if parts[6] == "open" else parts[6]
            # rebuild with quotes for note/source if commas
            def q(s: str) -> str:
                return f'"{s}"' if ("," in s or not s) else s

            new_lines.append(
                "  "
                + ",".join(
                    [
                        parts[0],
                        q(parts[1]),
                        q(parts[2]),
                        parts[3],
                        parts[4],
                        parts[5],
                        parts[6],
                        q(parts[7]),
                        q(parts[8]),
                    ]
                )
            )
            continue
        new_lines.append(line)
    write("\n".join(new_lines) + "\n")
    append_log(pid, f"periodic done; next_due {nxt}")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--due", action="store_true")
    p.add_argument("--today", action="store_true")
    p.add_argument("--mark-done", metavar="DAILY_ID")
    p.add_argument("--mark-periodic", metavar="PERIODIC_ID")
    p.add_argument("--date", default="")
    args = p.parse_args()
    n = sum(bool(x) for x in [args.due, args.today, args.mark_done, args.mark_periodic])
    if n != 1:
        raise SystemExit("choose exactly one of --due --today --mark-done --mark-periodic")
    if args.due:
        return cmd_due()
    if args.today:
        return cmd_today()
    if args.mark_done:
        append_log(args.mark_done)
        print(f"LOGGED {args.mark_done}")
        return 0
    when = args.date or berlin_today().isoformat()
    mark_periodic(args.mark_periodic, when)
    print(f"PERIODIC {args.mark_periodic} last_done={when}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
