#!/usr/bin/env python3
"""Cypher-like first-person hall over live mindcraft organs.

    python skills/mindcraft-hall.py
    python skills/mindcraft-hall.py --serve
    python skills/mindcraft-hall.py --serve --no-open

Writes tmp/pedagogy/mindcraft-hall.html. Open in Chrome/Edge (pointer lock).
Does not invent STUDY ANSWER. Does not paste .private bodies.
"""
from __future__ import annotations

import argparse
import http.server
import importlib.util
import json
import mimetypes
import re
import socket
import socketserver
import sys
import webbrowser
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "skills" / "mindcraft-hall.html"
OUT = ROOT / "tmp" / "pedagogy" / "mindcraft-hall.html"


def _load_psv():
    path = ROOT / "skills" / "project-state-viz.py"
    spec = importlib.util.spec_from_file_location("project_state_viz", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def _trim(s: object, n: int = 220) -> str:
    t = " ".join(str(s or "").split())
    return t if len(t) <= n else t[: n - 1] + "…"


def _caesar(text: str, shift: int = 3) -> str:
    out = []
    for ch in text:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)


_YT = re.compile(
    r"(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/shorts/)([\w-]{11})",
    re.I,
)
_BILI = re.compile(r"bilibili\.com/video/(BV[\w]+)", re.I)
_URL = re.compile(r"https?://[^\s)\]>\"']+")
_MEDIA_FU = re.compile(r"MEDIA\s+(VIDEO|FIG|PAGE|CODE|AUDIO)\s+(\S+)")


def _media_from(*parts: object) -> dict:
    blob = " ".join(str(p or "") for p in parts)
    urls = _URL.findall(blob)
    yt = _YT.search(blob)
    bili = _BILI.search(blob)
    media = {
        "kind": "text",
        "url": urls[0] if urls else "",
        "yt": "",
        "bili": "",
        "thumb": "",
        "embed": "",
        "src": "",
    }
    if yt:
        vid = yt.group(1)
        media.update(
            {
                "kind": "youtube",
                "yt": vid,
                "url": f"https://www.youtube.com/watch?v={vid}",
                "thumb": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg",
                "embed": f"https://www.youtube-nocookie.com/embed/{vid}?rel=0&cc_load_policy=1&cc_lang_pref=de&hl=de",
            }
        )
        return media
    if bili:
        bvid = bili.group(1)
        media.update(
            {
                "kind": "bilibili",
                "bili": bvid,
                "url": f"https://www.bilibili.com/video/{bvid}",
                "embed": f"https://player.bilibili.com/player.html?bvid={bvid}&high_quality=1",
            }
        )
        return media
    if urls:
        u = urls[0]
        low = u.lower()
        media["url"] = u
        if low.endswith((".mp4", ".webm", ".ogg")):
            media["kind"] = "video"
            media["src"] = u
        elif low.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
            media["kind"] = "image"
            media["thumb"] = u
        elif ".pdf" in low.split("?", 1)[0]:
            media["kind"] = "pdf"
        else:
            media["kind"] = "page"
    return media


def _teleport_for(path: str = "", kind: str = "", title: str = "") -> str:
    """Map a file/organ to a hall room. Language stores win over pedagogy/."""
    blob = f"{path} {title} {kind}".lower().replace("\\", "/")
    if any(
        s in blob
        for s in (
            "polyglot",
            "writing-accuracy",
            "horizon.toon",
            "wortschatz",
            "cipher",
            "todayfocus",
        )
    ):
        return "language"
    for needle, room in (
        ("cpu.md", "cpu"),
        ("pedagogy/", "pedagogy"),
        ("universe.graph", "pedagogy"),
        ("graph.md", "pedagogy"),
        ("inflow/", "inflow"),
        ("self/", "self"),
        (".private", "self"),
        ("hall-library", "library"),
        ("recovery-cycle", "war"),
        ("endurance.toon", "war"),
        ("training.toon", "war"),
        ("cron/", "cron"),
        ("schedule/", "schedule"),
        (".cursor/skills", "skills"),
        ("skills/", "skills"),
        ("mezzanine/", "skills"),
        ("tmp/", "skills"),
        ("root.md", "nave"),
        ("recycle", "nave"),
    ):
        if needle in blob:
            return room
    name = (path or title).lower()
    for needle, room in (
        ("cpu", "cpu"),
        ("pedagogy", "pedagogy"),
        ("inflow", "inflow"),
        ("schedule", "schedule"),
        ("cron", "cron"),
        ("skills", "skills"),
        ("mezzanine", "skills"),
        ("tmp", "skills"),
        ("self", "self"),
        ("private", "self"),
        ("agent", "cpu"),
    ):
        token = name.replace("dir ", "").replace("file ", "").replace("tag ", "").strip()
        if token == needle or token.startswith(needle + ".") or needle in token.split():
            return room
        if needle in blob and kind == "organ":
            return room
    kind_room = {
        "agent": "cpu",
        "todo": "cpu",
        "note": "cpu",
        "probe": "pedagogy",
        "branch": "pedagogy",
        "graph": "pedagogy",
        "lang": "language",
        "horizon": "language",
        "focus": "language",
        "store": "language",
        "state": "inflow",
        "dump": "inflow",
        "news": "inflow",
        "goals": "self",
        "north": "self",
        "endurance": "self",
        "train": "self",
        "file": "self",
        "job": "cron",
        "harvest": "schedule",
        "skill": "skills",
        "lib": "skills",
        "ttl": "skills",
        "organ": "nave",
        "today": "nave",
        "cabinet": "nave",
    }
    return kind_room.get((kind or "").lower(), "nave")


def _item(kind: str, title: str, body: str, path: str = "", extra: dict | None = None) -> dict:
    row = {
        "kind": kind,
        "title": _trim(title, 80),
        "body": _trim(body, 420),
        "path": path,
    }
    if extra:
        row.update(extra)
    if "teleport" not in row:
        row["teleport"] = _teleport_for(path, kind, title)
    if "media" not in row:
        url_blob = row.get("url") or ""
        urls = row.get("urls") or []
        if isinstance(urls, list):
            url_blob = " ".join([url_blob, *[str(u) for u in urls]])
        row["media"] = _media_from(title, body, path, url_blob)
    return row


def _collect_clips(state: dict) -> list[dict]:
    """YouTube / Bilibili / local tmp media as hall screens. Cap keeps the JSON small."""
    seen: set[str] = set()
    clips: list[dict] = []

    def add(kind: str, title: str, body: str, path: str, *src: object) -> None:
        if len(clips) >= 18:
            return
        media = _media_from(title, body, path, *src)
        key = media.get("yt") or media.get("bili") or media.get("src") or media.get("thumb") or media.get("url")
        if not key or key in seen:
            return
        if media["kind"] not in {"youtube", "bilibili", "video", "image"}:
            return
        seen.add(str(key))
        clips.append(
            _item(
                media["kind"],
                title,
                body,
                path,
                {"media": media, "teleport": _teleport_for(path, media["kind"], title)},
            )
        )

    inflow = state.get("inflow") or {}
    for d in (inflow.get("digest") or []) + (inflow.get("pending") or []) + (inflow.get("news") or []):
        add(
            d.get("lane") or d.get("bucket") or "dump",
            d.get("title") or d.get("id") or "CAPTURE",
            d.get("note") or d.get("why") or "",
            "inflow/DUMP.md",
            " ".join(d.get("urls") or []),
            " ".join(d.get("sources") or []),
            d.get("url") or "",
        )
    for e in (state.get("graph") or {}).get("edges") or []:
        src = e.get("SOURCE") or e.get("source") or ""
        if "youtu" not in src.lower() and "bilibili" not in src.lower():
            continue
        add(
            "edge",
            f"{e.get('src')} · {e.get('label')} · {e.get('dst')}",
            src,
            "pedagogy/universe.graph.md",
            src,
        )
    ped = ROOT / "pedagogy"
    if ped.is_dir():
        for p in sorted(ped.rglob("*.fu.md")):
            if len(clips) >= 18:
                break
            parts = p.parts
            if "sessions" in parts or ".private" in parts:
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")[:12000]
            except OSError:
                continue
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            for mk, url in _MEDIA_FU.findall(text):
                if mk in {"VIDEO", "FIG"}:
                    add(mk.lower(), p.stem, url, rel, url)
            for vid in _YT.findall(text):
                add("youtube", p.stem, vid, rel, f"https://www.youtube.com/watch?v={vid}")
            for bvid in _BILI.findall(text):
                add("bilibili", p.stem, bvid, rel, f"https://www.bilibili.com/video/{bvid}")
    interview = ROOT / "pedagogy" / "_learn" / "interview.toon.md"
    if interview.is_file():
        try:
            itext = interview.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            itext = ""
        for vid in dict.fromkeys(_YT.findall(itext)):
            add(
                "youtube",
                f"interview · {vid}",
                f"https://www.youtube.com/watch?v={vid}",
                "pedagogy/_learn/interview.toon.md",
                f"https://www.youtube.com/watch?v={vid}",
            )
    tmp = ROOT / "tmp"
    if tmp.is_dir():
        for p in sorted(tmp.rglob("*")):
            if len(clips) >= 18:
                break
            if not p.is_file() or p.suffix.lower() not in {".mp4", ".webm", ".png", ".jpg", ".jpeg", ".webp"}:
                continue
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
            src = "/media/" + rel
            kind = "video" if p.suffix.lower() in {".mp4", ".webm"} else "image"
            media = {
                "kind": kind,
                "url": src,
                "yt": "",
                "bili": "",
                "thumb": src if kind == "image" else "",
                "embed": "",
                "src": src if kind == "video" else "",
            }
            key = src
            if key in seen:
                continue
            seen.add(key)
            clips.append(_item(kind, p.name, f"local {kind}", rel, {"media": media, "teleport": "skills"}))
    return clips


def _graph_preview(graph: dict) -> dict:
    verts = graph.get("verts") or []
    edges = graph.get("edges") or []
    slim_v = [
        {
            "id": v.get("id") or "",
            "gloss": _trim(v.get("gloss") or v.get("id"), 48),
            "branch": v.get("branch") or "",
        }
        for v in verts[:28]
    ]
    ids = {v["id"] for v in slim_v if v["id"]}
    slim_e = []
    for e in edges:
        a, b = e.get("src") or "", e.get("dst") or ""
        if a in ids and b in ids:
            slim_e.append({"src": a, "dst": b, "label": e.get("label") or ""})
        if len(slim_e) >= 36:
            break
    return {"verts": slim_v, "edges": slim_e}


BOARD = ROOT / "inflow" / "hall-board.toon.md"
ROOMS_OK = (
    "nave",
    "cpu",
    "pedagogy",
    "language",
    "inflow",
    "self",
    "cron",
    "schedule",
    "skills",
    "war",
    "library",
)

_ALERT_TITLE = {
    "fog": "Fog · sickness-behavior",
    "gi": "GI · named unspecified",
    "mucosa": "mucosa · not named fully healed",
    "dental": "tooth · named",
    "cough": "cough · named span",
    "acne": "acne · named span",
    "pain": "pain · named",
    "doms": "DOMS · named",
}

_MUSCLE_GROUPS = (
    ("head", "Kopf", ("head", "systemic")),
    ("chest", "Brust", ("chest",)),
    ("lats", "Lats", ("lats", "back")),
    ("scapula_L", "scapula L", ("left scapula", "scapula")),
    ("scapula_R", "scapula R", ("right scapula",)),
    ("forearm", "Unterarm", ("forearm",)),
    ("core", "Rumpf", ("core", "core/ab", "ab", "gut")),
    ("quads", "Quad", ("quads", "quad")),
    ("hams", "Ham", ("hamstring", "hams")),
    ("calves", "Wade", ("calf", "calves")),
)


def _region_hit(region: str, needles: tuple[str, ...]) -> bool:
    blob = (region or "").lower()
    return any(n in blob for n in needles)


def _coarse_place(where: str) -> str:
    w = (where or "").lower()
    if "online" in w or "aws workshop" in w:
        return "Online"
    if "potsdam" in w:
        return "Potsdam"
    if "berlin" in w or "kreuzberg" in w or "mitte" in w:
        return "Berlin"
    if not where.strip():
        return ""
    return "coarse"


def _parse_when(s: str) -> datetime | None:
    t = (s or "").strip()
    if not t:
        return None
    t = t.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(t)
    except ValueError:
        m = re.match(r"(\d{4}-\d{2}-\d{2})", t)
        if m:
            return datetime.fromisoformat(m.group(1))
    return None


def _hhmm(s: object) -> float | None:
    t = str(s or "").strip()
    m = re.search(r"\b(\d{1,2})[:hH.](\d{2})\b", t)
    if m:
        h, mi = int(m.group(1)), int(m.group(2))
        if h == 24 and mi == 0:
            return 24.0
        if 0 <= h <= 23 and 0 <= mi <= 59:
            return h + mi / 60.0
        return None
    m = re.fullmatch(r"(\d{1,2})", t)
    if m:
        h = int(m.group(1))
        if 0 <= h <= 24:
            return float(h)
    return None


DAYLOG = ROOT / "inflow" / "hall-day.toon.md"


def load_hall_day(day: str = "") -> list[dict]:
    if not DAYLOG.is_file():
        return []
    items: list[dict] = []
    cur: dict | None = None
    for raw in DAYLOG.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.rstrip()
        if line.startswith("item:"):
            if cur and cur.get("id"):
                items.append(cur)
            cur = {
                "id": "",
                "date": "",
                "start": "",
                "end": "",
                "label": "",
                "note": "",
            }
            continue
        if cur is None or ":" not in line:
            continue
        key, _, val = line.strip().partition(":")
        key, val = key.strip(), val.strip()
        if key in cur:
            cur[key] = val
    if cur and cur.get("id"):
        items.append(cur)
    if day:
        items = [x for x in items if (x.get("date") or "")[:10] == day[:10]]
    return items


def save_hall_day(items: list[dict]) -> None:
    lines = [
        "schema: inflow/hall-day",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "kind: IST day log. Suggested SOLL is computed. Not DUMP. No .private.",
        "tz: Europe/Berlin",
        "",
    ]
    for it in items[-40:]:
        if not it.get("id"):
            continue
        lines.extend(
            [
                "item:",
                f"  id: {it.get('id', '')}",
                f"  date: {(it.get('date') or '')[:10]}",
                f"  start: {it.get('start') or ''}",
                f"  end: {it.get('end') or ''}",
                f"  label: {_trim(it.get('label'), 80)}",
                f"  note: {_trim(it.get('note'), 160)}",
                "",
            ]
        )
    DAYLOG.parent.mkdir(parents=True, exist_ok=True)
    DAYLOG.write_text("\n".join(lines) + "\n", encoding="utf-8")


def day_mutate(body: dict) -> dict:
    op = str(body.get("op") or "").strip()
    items = load_hall_day()
    blob = f"{body.get('label') or ''} {body.get('note') or ''}".lower()
    if ".private" in blob:
        return {"ok": False, "error": "no .private"}
    day = str(body.get("date") or "").strip()[:10]
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
        try:
            from zoneinfo import ZoneInfo

            day = datetime.now(ZoneInfo("Europe/Berlin")).strftime("%Y-%m-%d")
        except Exception:
            day = datetime.now(timezone(timedelta(hours=2))).strftime("%Y-%m-%d")
    if op == "create":
        start = _hhmm(body.get("start"))
        end = _hhmm(body.get("end"))
        if start is None or end is None:
            return {"ok": False, "error": "start/end HH:MM"}
        if end <= start:
            return {"ok": False, "error": "end after start"}
        label = str(body.get("label") or "").strip()
        if not label:
            return {"ok": False, "error": "label required"}
        nid = str(body.get("id") or "").strip() or (
            "ist-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        )
        nid = re.sub(r"[^a-zA-Z0-9._-]", "-", nid)[:80]

        def fmt(h: float) -> str:
            hh = int(h)
            mm = int(round((h % 1) * 60))
            if mm == 60:
                hh, mm = hh + 1, 0
            return f"{hh:02d}:{mm:02d}"

        items.append(
            {
                "id": nid,
                "date": day,
                "start": fmt(start),
                "end": fmt(end),
                "label": label[:80],
                "note": str(body.get("note") or "")[:160],
            }
        )
    elif op == "update":
        iid = str(body.get("id") or "").strip()
        found = next((x for x in items if x.get("id") == iid), None)
        if not found:
            return {"ok": False, "error": "unknown id"}

        def fmt(h: float) -> str:
            hh = int(h)
            mm = int(round((h % 1) * 60))
            if mm == 60:
                hh, mm = hh + 1, 0
            return f"{hh:02d}:{mm:02d}"

        if "start" in body:
            start = _hhmm(body.get("start"))
            if start is None:
                return {"ok": False, "error": "start HH:MM"}
            found["start"] = fmt(start)
        if "end" in body:
            end = _hhmm(body.get("end"))
            if end is None:
                return {"ok": False, "error": "end HH:MM"}
            found["end"] = fmt(end)
        if "label" in body:
            found["label"] = str(body.get("label") or "")[:80]
        if "note" in body:
            found["note"] = str(body.get("note") or "")[:160]
        if "date" in body:
            found["date"] = day
    elif op == "delete":
        iid = str(body.get("id") or "").strip()
        items = [x for x in items if x.get("id") != iid]
    else:
        return {"ok": False, "error": "bad op"}
    save_hall_day(items)
    return {"ok": True, "items": load_hall_day(day)}


def _day_pack(state: dict, origin: date, day_s: str) -> dict:
    """0–24 SOLL from stores + IST log. Not a week calendar. No invented Termin."""
    today = state.get("today") or {}
    suggest: list[dict] = []

    def add(start: float, end: float, label: str, kind: str, source: str) -> None:
        suggest.append(
            {
                "start": round(start, 2),
                "end": round(min(end, 24.0), 2),
                "label": _trim(label, 56),
                "kind": kind,
                "source": source,
            }
        )

    add(7.5, 9.0, "routine.daily morning · Hygiene", "slot", "self/routine.toon.md")
    add(10.0, 13.0, f"valued work · PLAN NOW {today.get('plan_now') or '—'}", "work", "CPU / pedagogy")
    add(14.0, 24.0, "no caffeine after 14:00", "gate", "CPU NOTE")
    add(15.0, 18.0, "contiguous stretch · not going-out", "work", "NOTE TODAY Zeitstruktur")
    add(18.0, 19.0, "SRM dinner ±45min · not a Termin", "anchor", "Monk 2002")
    add(21.0, 22.5, "routine.daily evening · Hygiene", "slot", "self/routine.toon.md")
    add(23.0, 24.0, "SRM bed ±45min · log IST wake/bed", "anchor", "Monk 2002")
    harvest_today = today.get("harvest_today") or []
    if not harvest_today:
        harvest_today = [
            r
            for r in ((state.get("schedule") or {}).get("harvest") or [])[:16]
            if (r.get("start") or "").startswith(day_s[:10])
        ]
    for r in harvest_today[:12]:
        st = _parse_when(r.get("start") or "")
        en = _parse_when(r.get("end") or "") or st
        if not st:
            hs, he = _hhmm(r.get("start")), _hhmm(r.get("end"))
            if hs is None:
                continue
            add(
                hs,
                he if he is not None else min(hs + 1, 24),
                _trim(r.get("title"), 50),
                "harvest",
                "schedule/harvest",
            )
            continue
        if st.date() != origin:
            continue
        sh = st.hour + st.minute / 60
        eh = (en.hour + en.minute / 60) if en and en.date() == origin else min(sh + 1, 24)
        if eh <= sh:
            eh = min(sh + 1, 24)
        add(sh, eh, _trim(r.get("title") or r.get("id"), 50), "harvest", "schedule/harvest")
    actual = []
    for it in load_hall_day(day_s[:10]):
        hs, he = _hhmm(it.get("start")), _hhmm(it.get("end"))
        if hs is None or he is None:
            continue
        actual.append(
            {
                "id": it.get("id"),
                "start": hs,
                "end": he,
                "label": it.get("label") or "",
                "note": it.get("note") or "",
                "crud": True,
            }
        )
    try:
        from zoneinfo import ZoneInfo

        now = datetime.now(ZoneInfo("Europe/Berlin"))
    except Exception:
        now = datetime.now(timezone(timedelta(hours=2)))
    now_h = now.hour + now.minute / 60 if now.date() == origin else None
    return {
        "date": day_s[:10],
        "tz": "Europe/Berlin",
        "nowHour": None if now_h is None else round(now_h, 2),
        "foggy": bool(today.get("foggy")),
        "planNow": today.get("plan_now") or "",
        "note": "SOLL = store suggestion. IST = your log. Not a week calendar. Empty PROBE stays empty.",
        "suggest": suggest,
        "actual": actual,
    }


def _war_pack(state: dict) -> dict:
    """Coarse war-room snapshot. No .private bodies, no lesion sites, no invented DOMS."""
    today = state.get("today") or {}
    self_pack = state.get("self") or {}
    train = self_pack.get("training") or {}
    endu = self_pack.get("endurance") or {}
    rec = self_pack.get("recovery") or train.get("recovery") or {}
    sched = state.get("schedule") or {}
    flags = train.get("flags") or {}
    open_rows = list(rec.get("open") or [])
    episodes = list(rec.get("episodes") or [])

    muscles = []
    for mid, label, needles in _MUSCLE_GROUPS:
        status = "unreported"
        note = "nicht gemeldet"
        for row in open_rows:
            if row.get("kind") == "doms" and _region_hit(row.get("region") or "", needles):
                status = "sore"
                note = f"open since {row.get('onset') or '?'}"
                break
            if mid == "head" and row.get("kind") == "fog":
                status = "flag"
                note = "fog named present"
                break
            if mid == "core" and row.get("kind") == "gi":
                status = "flag"
                note = "GI named unspecified"
                break
            if mid == "scapula_L" and row.get("kind") == "pain" and _region_hit(
                row.get("region") or "", needles
            ):
                status = "flag"
                note = f"open since {row.get('onset') or '?'}"
                break
        if status == "unreported":
            for row in episodes:
                if row.get("cleared") and row.get("cleared") != "open":
                    if row.get("kind") == "doms" and _region_hit(row.get("region") or "", needles):
                        status = "quiet"
                        note = f"recovered {row.get('cleared')}"
                        break
                    if mid == "scapula_L" and row.get("kind") == "pain" and _region_hit(
                        row.get("region") or "", needles
                    ):
                        status = "quiet"
                        note = f"recovered {row.get('cleared')}"
                        break
        if mid == "scapula_L" and str(flags.get("leftScapulaPain") or "").lower() == "true":
            status = "flag"
            note = "training.flags leftScapulaPain"
        muscles.append({"id": mid, "label": label, "status": status, "note": note})

    alerts = []
    if today.get("foggy") and not any(r.get("kind") == "fog" for r in open_rows):
        alerts.append(
            {
                "id": "today-fog",
                "kind": "fog",
                "level": "warn",
                "title": _ALERT_TITLE["fog"],
                "body": "CPU NOTE TODAY · not DSB · skip lexicon/PROBE until asked",
            }
        )
    for row in open_rows:
        kind = (row.get("kind") or "open")[:24]
        if kind in {"fog-sexual", "sexual"}:
            continue
        title = _ALERT_TITLE.get(kind, f"{kind} · named")
        body = " · ".join(
            x
            for x in (
                row.get("region") or "",
                f"onset {row.get('onset')}" if row.get("onset") else "",
                "open" if (row.get("cleared") or "open") == "open" else f"cleared {row.get('cleared')}",
            )
            if x
        )
        alerts.append(
            {
                "id": row.get("id") or kind,
                "kind": kind,
                "level": "warn" if kind in {"fog", "gi", "pain"} else "note",
                "title": title,
                "body": _trim(body, 180),
            }
        )

    pins = [{"id": "berlin", "lon": 13.41, "lat": 52.52, "label": "Berlin TZ"}]
    events = []
    gantt_rows = []
    day_s = today.get("date") or datetime.now().strftime("%Y-%m-%d")
    try:
        origin = date.fromisoformat(day_s[:10])
    except ValueError:
        origin = date.today()
    marks: dict[str, int] = {}
    for r in (sched.get("harvest") or [])[:16]:
        where = _coarse_place(r.get("where") or "")
        title = _trim(r.get("title") or r.get("id"), 56)
        if not title:
            continue
        st = _parse_when(r.get("start") or "")
        en = _parse_when(r.get("end") or "") or st
        events.append({"title": title, "when": _trim(r.get("start") or "", 40), "where": where})
        if where == "Berlin" and not any(p["id"] == "berlin-evt" for p in pins):
            pins.append({"id": "berlin-evt", "lon": 13.41, "lat": 52.52, "label": title[:22]})
        if where == "Potsdam" and not any(p["id"] == "potsdam" for p in pins):
            pins.append({"id": "potsdam", "lon": 13.06, "lat": 52.40, "label": "Potsdam"})
        if st:
            key = st.date().isoformat()
            marks[key] = marks.get(key, 0) + 1
            start_off = (st.date() - origin).days
            end_off = (en.date() - origin).days if en else start_off
            if end_off < start_off:
                end_off = start_off
            gantt_rows.append(
                {
                    "title": title,
                    "start": start_off,
                    "end": min(end_off, start_off + 14),
                    "status": (r.get("status") or "candidate")[:16],
                    "where": where,
                }
            )

    tasks = []
    for a in (today.get("actions") or [])[:14]:
        tasks.append(
            {
                "pri": int(a.get("priority") or 9),
                "kind": (a.get("kind") or "task")[:16],
                "text": _trim(a.get("text") or a.get("source") or "", 90),
            }
        )
    cpu = state.get("cpu") or {}
    for td in (cpu.get("todos") or [])[:8]:
        if td.get("done"):
            continue
        tasks.append(
            {
                "pri": 3,
                "kind": "todo",
                "text": _trim(td.get("text") or "", 90),
            }
        )
    if today.get("plan_now"):
        tasks.insert(
            0,
            {
                "pri": 2,
                "kind": "plan",
                "text": _trim(f"PLAN NOW {today.get('plan_now')} · empty PROBE stays empty", 90),
            },
        )

    latest_sore = ""
    for lg in reversed(endu.get("logs") or []):
        if lg.get("sore"):
            latest_sore = lg.get("sore") or ""
            break

    month_days = []
    first = origin.replace(day=1)
    start_wd = first.weekday()  # Mon=0
    if origin.month == 12:
        nxt = date(origin.year + 1, 1, 1)
    else:
        nxt = date(origin.year, origin.month + 1, 1)
    n = (nxt - first).days
    for d in range(1, n + 1):
        iso = date(origin.year, origin.month, d).isoformat()
        month_days.append(
            {
                "d": d,
                "n": marks.get(iso, 0),
                "today": d == origin.day,
            }
        )

    return {
        "tz": "Europe/Berlin",
        "date": day_s[:10],
        "weekday": today.get("weekday") or "",
        "foggy": bool(today.get("foggy")),
        "sore": latest_sore,
        "budget": (endu.get("budget_now") or ""),
        "bodyweightKg": train.get("bodyweightKg") or "",
        "pressGate": str(flags.get("skipHeavyPressUntilClear") or "false").lower() == "true",
        "planNow": today.get("plan_now") or "",
        "muscles": muscles,
        "alerts": alerts[:10],
        "pins": pins,
        "events": events,
        "tasks": tasks[:16],
        "gantt": {"origin": origin.isoformat(), "span": 16, "rows": gantt_rows[:12]},
        "calendar": {
            "year": origin.year,
            "month": origin.month,
            "today": origin.day,
            "startWd": start_wd,
            "days": month_days,
        },
        "day": _day_pack(state, origin, day_s),
    }


def load_hall_board() -> list[dict]:
    if not BOARD.is_file():
        return []
    items: list[dict] = []
    cur: dict | None = None
    for raw in BOARD.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.rstrip()
        if line.startswith("item:"):
            if cur and cur.get("id"):
                items.append(cur)
            cur = {
                "id": "",
                "room": "inflow",
                "kind": "page",
                "title": "",
                "body": "",
                "url": "",
                "deleted": False,
            }
            continue
        if cur is None:
            continue
        s = line.strip()
        if ":" not in s:
            continue
        key, _, val = s.partition(":")
        key, val = key.strip(), val.strip()
        if key == "deleted":
            cur["deleted"] = val.lower() in {"true", "yes", "1"}
        elif key in cur:
            cur[key] = val
    if cur and cur.get("id"):
        items.append(cur)
    return [x for x in items if not x.get("deleted")]


def save_hall_board(items: list[dict]) -> None:
    lines = [
        "schema: inflow/hall-board",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "kind: human pins on Mindcraft Hall",
        "note: Not DUMP. Not ontology. No .private. Locked PROBE stays empty.",
        "",
    ]
    for it in items:
        if it.get("deleted") or not it.get("id"):
            continue
        lines.extend(
            [
                "item:",
                f"  id: {it.get('id', '')}",
                f"  room: {it.get('room') or 'inflow'}",
                f"  kind: {it.get('kind') or 'page'}",
                f"  title: {_trim(it.get('title'), 80)}",
                f"  body: {_trim(it.get('body'), 400)}",
                f"  url: {(it.get('url') or '')[:500]}",
                "",
            ]
        )
    BOARD.parent.mkdir(parents=True, exist_ok=True)
    BOARD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _apply_board(payload: dict) -> None:
    rooms = payload.get("rooms") or {}
    for pin in load_hall_board():
        room = pin.get("room") if pin.get("room") in rooms else "inflow"
        url = pin.get("url") or ""
        row = _item(
            pin.get("kind") or "page",
            pin.get("title") or pin.get("id") or "pin",
            pin.get("body") or "",
            "inflow/hall-board.toon.md",
            {
                "crud": True,
                "id": pin.get("id"),
                "url": url,
                "urls": [url] if url else [],
                "teleport": room,
            },
        )
        rooms[room]["items"] = [row] + list(rooms[room].get("items") or [])


def board_mutate(body: dict) -> dict:
    op = str(body.get("op") or "").strip()
    items = load_hall_board()
    blob = f"{body.get('url') or ''} {body.get('body') or ''} {body.get('title') or ''}".lower()
    if ".private" in blob:
        return {"ok": False, "error": "no .private"}
    if op == "create":
        url = str(body.get("url") or "").strip()
        if url and not url.startswith(("http://", "https://")):
            return {"ok": False, "error": "url must be http(s)"}
        rid = str(body.get("room") or "inflow").strip()
        if rid not in ROOMS_OK:
            rid = "inflow"
        nid = str(body.get("id") or "").strip() or (
            "pin-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        )
        nid = re.sub(r"[^a-zA-Z0-9._-]", "-", nid)[:80]
        if any(x.get("id") == nid for x in items):
            nid = nid + "-n"
        items.append(
            {
                "id": nid,
                "room": rid,
                "kind": str(body.get("kind") or "page")[:32],
                "title": str(body.get("title") or "pin")[:80],
                "body": str(body.get("body") or "")[:400],
                "url": url[:500],
            }
        )
    elif op == "update":
        iid = str(body.get("id") or "").strip()
        found = next((x for x in items if x.get("id") == iid), None)
        if not found:
            return {"ok": False, "error": "unknown id"}
        url = str(body.get("url") if "url" in body else found.get("url") or "").strip()
        if url and not url.startswith(("http://", "https://")):
            return {"ok": False, "error": "url must be http(s)"}
        if "title" in body:
            found["title"] = str(body.get("title") or "")[:80]
        if "body" in body:
            found["body"] = str(body.get("body") or "")[:400]
        if "url" in body:
            found["url"] = url[:500]
        if "room" in body and body.get("room") in ROOMS_OK:
            found["room"] = body["room"]
        if "kind" in body:
            found["kind"] = str(body.get("kind") or "page")[:32]
    elif op == "delete":
        iid = str(body.get("id") or "").strip()
        items = [x for x in items if x.get("id") != iid]
    else:
        return {"ok": False, "error": "bad op"}
    save_hall_board(items)
    return {"ok": True, "items": load_hall_board()}


LIBRARY = ROOT / "inflow" / "hall-library.toon.md"
LIB_SHELVES = ("agent", "language", "pedagogy", "biology", "user")


def load_hall_library() -> list[dict]:
    if not LIBRARY.is_file():
        return []
    items: list[dict] = []
    cur: dict | None = None
    for raw in LIBRARY.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.rstrip()
        if line.startswith("item:"):
            if cur and cur.get("id"):
                items.append(cur)
            cur = {
                "id": "",
                "shelf": "user",
                "kind": "pdf",
                "title": "",
                "body": "",
                "url": "",
            }
            continue
        if cur is None or ":" not in line:
            continue
        key, _, val = line.strip().partition(":")
        key, val = key.strip(), val.strip()
        if key in cur:
            cur[key] = val
    if cur and cur.get("id"):
        items.append(cur)
    return items


def save_hall_library(items: list[dict]) -> None:
    lines = [
        "schema: inflow/hall-library",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "kind: user books on the hall library. PDF/YouTube/page URLs. Not DUMP. No .private.",
        "",
    ]
    for it in items:
        if not it.get("id"):
            continue
        shelf = it.get("shelf") if it.get("shelf") in LIB_SHELVES else "user"
        lines.extend(
            [
                "item:",
                f"  id: {it.get('id', '')}",
                f"  shelf: {shelf}",
                f"  kind: {it.get('kind') or 'pdf'}",
                f"  title: {_trim(it.get('title'), 80)}",
                f"  body: {_trim(it.get('body'), 240)}",
                f"  url: {(it.get('url') or '')[:500]}",
                "",
            ]
        )
    LIBRARY.parent.mkdir(parents=True, exist_ok=True)
    LIBRARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


def library_mutate(body: dict) -> dict:
    op = str(body.get("op") or "").strip()
    items = load_hall_library()
    blob = f"{body.get('url') or ''} {body.get('body') or ''} {body.get('title') or ''}".lower()
    if ".private" in blob:
        return {"ok": False, "error": "no .private"}
    if op == "create":
        url = str(body.get("url") or "").strip()
        if not url.startswith(("http://", "https://")):
            return {"ok": False, "error": "url must be http(s)"}
        nid = str(body.get("id") or "").strip() or (
            "book-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        )
        nid = re.sub(r"[^a-zA-Z0-9._-]", "-", nid)[:80]
        kind = str(body.get("kind") or "pdf")[:16]
        low = url.lower()
        if kind == "pdf" and ("youtu" in low or "bilibili" in low):
            kind = "youtube" if "youtu" in low else "bilibili"
        elif low.endswith(".pdf"):
            kind = "pdf"
        items.append(
            {
                "id": nid,
                "shelf": body.get("shelf") if body.get("shelf") in LIB_SHELVES else "user",
                "kind": kind,
                "title": str(body.get("title") or "book")[:80],
                "body": str(body.get("body") or "")[:240],
                "url": url[:500],
            }
        )
    elif op == "update":
        iid = str(body.get("id") or "").strip()
        found = next((x for x in items if x.get("id") == iid), None)
        if not found:
            return {"ok": False, "error": "unknown id"}
        if "url" in body:
            url = str(body.get("url") or "").strip()
            if not url.startswith(("http://", "https://")):
                return {"ok": False, "error": "url must be http(s)"}
            found["url"] = url[:500]
        if "title" in body:
            found["title"] = str(body.get("title") or "")[:80]
        if "body" in body:
            found["body"] = str(body.get("body") or "")[:240]
        if "shelf" in body and body.get("shelf") in LIB_SHELVES:
            found["shelf"] = body["shelf"]
        if "kind" in body:
            found["kind"] = str(body.get("kind") or "pdf")[:16]
    elif op == "delete":
        iid = str(body.get("id") or "").strip()
        items = [x for x in items if x.get("id") != iid]
    else:
        return {"ok": False, "error": "bad op"}
    save_hall_library(items)
    return {"ok": True, "items": load_hall_library()}


def _parse_drills(n: int = 8) -> list[dict]:
    path = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "drills.toon.md"
    if not path.is_file():
        return []
    cards: list[dict] = []
    cur: dict | None = None
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if raw.startswith("item:"):
            if cur and cur.get("prompt"):
                cards.append(cur)
            cur = {
                "id": "",
                "kind": "cloze",
                "prompt": "",
                "accept": "",
                "answer": "",
                "choices": "",
                "hint": "",
                "frame": "",
            }
            continue
        if cur is None or ":" not in raw:
            continue
        key, _, val = raw.strip().partition(":")
        key, val = key.strip(), val.strip()
        if key in cur:
            cur[key] = val
    if cur and cur.get("prompt"):
        cards.append(cur)
    return cards[:n]


def _harvest_learn_urls(limit: int = 12) -> list[dict]:
    path = ROOT / "pedagogy" / "_learn" / "polyglot" / "harvest.toon.md"
    if not path.is_file():
        return []
    rows: list[dict] = []
    started = False
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith("rows["):
            started = True
            continue
        if not started or not line.startswith("  "):
            continue
        parts = [p.strip() for p in line.strip().split(",")]
        if len(parts) < 6:
            continue
        url = parts[-2]
        if not url.startswith("http"):
            continue
        rows.append(
            {
                "id": parts[0],
                "shelf": "language",
                "kind": "pdf" if ".pdf" in url.lower() else "page",
                "title": _trim(",".join(parts[3:-2]), 70),
                "body": f"{parts[1]} · {parts[2]}",
                "url": url[:500],
            }
        )
        if len(rows) >= limit:
            break
    return rows


def _library_pack(state: dict, clips: list[dict]) -> dict:
    """Books + customized screens. No invented ANSWER. No .private."""
    today = state.get("today") or {}
    goals = state.get("goals") or {}
    learn = (state.get("self") or {}).get("learn") or {}
    lang = state.get("language") or {}
    user_books = []
    for it in load_hall_library():
        media = _media_from(it.get("title"), it.get("url"))
        user_books.append(
            {
                **it,
                "crud": True,
                "media": media,
                "teleport": "library",
            }
        )
    auto = _harvest_learn_urls(36)
    auto.sort(key=lambda b: 0 if b.get("kind") == "pdf" else 1)
    north = " ".join((goals.get("north") or [])[:8]).lower()
    plan = (today.get("plan_now") or learn.get("target") or "").lower()
    for c in clips[:8]:
        media = c.get("media") or {}
        title = c.get("title") or ""
        blob = f"{title} {c.get('body') or ''}".lower()
        shelf = "agent" if any(k in blob or k in north or k in plan for k in ("agent", "core", "mcp", "cursor")) else "pedagogy"
        auto.append(
            {
                "id": f"clip-{c.get('title', 'x')[:24]}",
                "shelf": shelf,
                "kind": media.get("kind") or "youtube",
                "title": _trim(title, 70),
                "body": _trim(c.get("body"), 120),
                "url": media.get("url") or "",
                "media": media,
                "teleport": "library",
            }
        )
    books = user_books + auto
    seen: set[str] = set()
    slim = []
    for b in books:
        u = b.get("url") or (b.get("media") or {}).get("url") or ""
        if not u or u in seen:
            continue
        seen.add(u)
        if "media" not in b:
            b["media"] = _media_from(b.get("title"), u)
        slim.append(b)
        if len(slim) >= 48:
            break

    weak = [
        n.get("id")
        for n in (learn.get("nodes") or [])
        if (n.get("grasp") or "unknown") in {"unknown", "weak", ""}
    ]
    focus = lang.get("oneFocus") or "in + Akk"
    target = lang.get("targetLang") or "de"
    pdf = next((b for b in slim if (b.get("kind") == "pdf") or ".pdf" in (b.get("url") or "").lower()), None)
    yt = next((b for b in slim if (b.get("media") or {}).get("kind") == "youtube"), None)
    lang_page = next(
        (
            b
            for b in slim
            if b.get("shelf") == "language" and b is not pdf and ".pdf" not in (b.get("url") or "").lower()
        ),
        None,
    )
    agent_page = next((b for b in slim if b.get("shelf") == "agent"), None)
    used_urls = {
        (pdf or {}).get("url") or "",
        (yt or {}).get("url") or "",
        (lang_page or {}).get("url") or "",
    }
    extra = user_books[0] if user_books else next(
        (b for b in slim if (b.get("url") or "") not in used_urls),
        slim[1] if len(slim) > 1 else None,
    )
    screens = [
        {
            "id": "main",
            "role": "pdf",
            "why": f"PLAN NOW {today.get('plan_now') or '—'} · grasp {', '.join(weak[:3]) or 'unlogged'}",
            "book": pdf or slim[0] if slim else None,
        },
        {
            "id": "a",
            "role": "youtube",
            "why": f"north {goals.get('focus') or '—'}",
            "book": yt or agent_page,
        },
        {
            "id": "b",
            "role": "page",
            "why": f"targetLang {target} · {focus}",
            "book": lang_page,
        },
        {
            "id": "c",
            "role": "flashcard",
            "why": f"Frame · {focus} · not ANSWER",
            "book": None,
        },
        {
            "id": "d",
            "role": "page",
            "why": "user shelf first, else harvest",
            "book": extra,
        },
    ]
    return {
        "books": slim,
        "screens": screens,
        "cards": _parse_drills(8),
        "focus": focus,
        "target": target,
        "planNow": today.get("plan_now") or "",
        "weak": weak[:6],
        "north": (goals.get("north") or [])[:8],
    }


WATCH = ROOT / "inflow" / "hall-watch.toon.md"


def load_hall_watch() -> list[dict]:
    if not WATCH.is_file():
        return []
    items: list[dict] = []
    cur: dict | None = None
    for raw in WATCH.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.rstrip()
        if line.startswith("item:"):
            if cur and cur.get("id"):
                items.append(cur)
            cur = {"id": "", "kind": "youtube", "yt": "", "seconds": "0", "title": ""}
            continue
        if cur is None or ":" not in line:
            continue
        key, _, val = line.strip().partition(":")
        key, val = key.strip(), val.strip()
        if key in cur:
            cur[key] = val
    if cur and cur.get("id"):
        items.append(cur)
    return items


def save_hall_watch(items: list[dict]) -> None:
    lines = [
        "schema: inflow/hall-watch",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "kind: YouTube resume timestamps for hall exhibits. Not DUMP. No .private.",
        "",
    ]
    for it in items[-80:]:
        if not it.get("id"):
            continue
        sec = it.get("seconds") or "0"
        try:
            sec_n = max(0, min(int(float(sec)), 12 * 3600))
        except (TypeError, ValueError):
            sec_n = 0
        lines.extend(
            [
                "item:",
                f"  id: {it.get('id', '')}",
                f"  kind: {it.get('kind') or 'youtube'}",
                f"  yt: {it.get('yt') or ''}",
                f"  seconds: {sec_n}",
                f"  title: {_trim(it.get('title'), 80)}",
                "",
            ]
        )
    WATCH.parent.mkdir(parents=True, exist_ok=True)
    WATCH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def watch_mutate(body: dict) -> dict:
    op = str(body.get("op") or "upsert").strip()
    items = load_hall_watch()
    yt = str(body.get("yt") or "").strip()
    if not yt:
        m = _YT.search(str(body.get("url") or ""))
        yt = m.group(1) if m else ""
    yt = re.sub(r"[^a-zA-Z0-9_-]", "", yt)[:11]
    if op == "delete":
        iid = str(body.get("id") or (f"yt-{yt}" if yt else "")).strip()
        items = [x for x in items if x.get("id") != iid and x.get("yt") != yt]
        save_hall_watch(items)
        return {"ok": True, "items": items}
    if op not in {"upsert", "create", "update"}:
        return {"ok": False, "error": "bad op"}
    if len(yt) != 11:
        return {"ok": False, "error": "need youtube id"}
    try:
        seconds = max(0, min(int(float(body.get("seconds") or 0)), 12 * 3600))
    except (TypeError, ValueError):
        return {"ok": False, "error": "seconds"}
    nid = f"yt-{yt}"
    found = next((x for x in items if x.get("yt") == yt or x.get("id") == nid), None)
    row = found or {"id": nid, "kind": "youtube", "yt": yt, "seconds": "0", "title": ""}
    row["seconds"] = str(seconds)
    row["yt"] = yt
    row["kind"] = "youtube"
    if body.get("title"):
        row["title"] = str(body.get("title") or "")[:80]
    if not found:
        items.append(row)
    save_hall_watch(items)
    return {"ok": True, "item": row, "seconds": seconds}


def _watch_pack() -> dict:
    out = {}
    for it in load_hall_watch():
        yt = it.get("yt") or ""
        if len(yt) != 11:
            continue
        try:
            sec = max(0, int(float(it.get("seconds") or 0)))
        except (TypeError, ValueError):
            sec = 0
        out[yt] = {"seconds": sec, "title": it.get("title") or ""}
    return out


PDA = ROOT / "pedagogy" / "_learn" / "polyglot" / "pda.toon.md"
LEXICON = ROOT / "pedagogy" / "_learn" / "writing-accuracy" / "lexicon.graph.md"


def load_hall_pda() -> dict:
    words: list[dict] = []
    notes: list[dict] = []
    if not PDA.is_file():
        return {"words": words, "notes": notes}
    cur: dict | None = None
    kind = ""
    for raw in PDA.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.rstrip()
        if line.startswith("word:"):
            if cur and cur.get("id") and kind == "word":
                words.append(cur)
            elif cur and cur.get("id") and kind == "note":
                notes.append(cur)
            cur = {"id": "", "surface": "", "gloss": "", "lang": "de", "note": "", "when": "", "room": ""}
            kind = "word"
            continue
        if line.startswith("note:"):
            if cur and cur.get("id") and kind == "word":
                words.append(cur)
            elif cur and cur.get("id") and kind == "note":
                notes.append(cur)
            cur = {"id": "", "text": "", "when": "", "room": ""}
            kind = "note"
            continue
        if cur is None or ":" not in line.strip():
            continue
        key, _, val = line.strip().partition(":")
        key, val = key.strip(), val.strip()
        if key in cur:
            cur[key] = val
    if cur and cur.get("id") and kind == "word":
        words.append(cur)
    elif cur and cur.get("id") and kind == "note":
        notes.append(cur)
    return {"words": words[-40:], "notes": notes[-40:]}


def save_hall_pda(data: dict) -> None:
    lines = [
        "schema: learn/polyglot-pda",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}",
        "kind: PDA captures from Mindcraft Hall",
        "note: Not ANSWER. No .private. Words also stamp lexicon.graph.md.",
        "",
    ]
    for it in data.get("words") or []:
        if not it.get("id"):
            continue
        lines.extend(
            [
                "word:",
                f"  id: {it.get('id')}",
                f"  surface: {_trim(it.get('surface'), 80)}",
                f"  gloss: {_trim(it.get('gloss'), 80)}",
                f"  lang: {(it.get('lang') or 'de')[:8]}",
                f"  note: {_trim(it.get('note'), 120)}",
                f"  when: {(it.get('when') or '')[:24]}",
                f"  room: {(it.get('room') or '')[:24]}",
                "",
            ]
        )
    for it in data.get("notes") or []:
        if not it.get("id"):
            continue
        lines.extend(
            [
                "note:",
                f"  id: {it.get('id')}",
                f"  text: {_trim(it.get('text'), 240)}",
                f"  when: {(it.get('when') or '')[:24]}",
                f"  room: {(it.get('room') or '')[:24]}",
                "",
            ]
        )
    PDA.parent.mkdir(parents=True, exist_ok=True)
    PDA.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _pda_stamp_lexicon(surface: str, gloss: str, lang: str) -> None:
    if not LEXICON.is_file() or not surface:
        return
    text = LEXICON.read_text(encoding="utf-8", errors="ignore")
    if surface.lower() in text.lower():
        return
    vid = "Pda_" + re.sub(r"[^A-Za-z0-9]+", "_", surface)[:40].strip("_")
    if not vid or vid == "Pda":
        vid = "Pda_" + datetime.now(timezone.utc).strftime("%H%M%S")
    gloss_s = re.sub(r"\s+", "-", (gloss or "pda-capture").strip())[:80] or "pda-capture"
    line = f"V {vid} kind=lemma lang={lang} surface={surface.replace(' ', '-')} gloss={gloss_s} source=pda\n"
    LEXICON.write_text(text.rstrip() + "\n" + line, encoding="utf-8")


def pda_mutate(body: dict) -> dict:
    op = str(body.get("op") or "").strip()
    data = load_hall_pda()
    blob = f"{body.get('surface') or ''} {body.get('gloss') or ''} {body.get('note') or ''} {body.get('text') or ''}"
    if ".private" in blob.lower():
        return {"ok": False, "error": "no .private"}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    room = str(body.get("room") or "")[:24]
    lang = str(body.get("lang") or "de")[:8]
    if op == "word":
        surface = str(body.get("surface") or "").strip()[:80]
        if not surface:
            return {"ok": False, "error": "surface required"}
        nid = str(body.get("id") or "").strip() or (
            "w-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        )
        nid = re.sub(r"[^a-zA-Z0-9._-]", "-", nid)[:80]
        row = {
            "id": nid,
            "surface": surface,
            "gloss": str(body.get("gloss") or "")[:80],
            "lang": lang,
            "note": str(body.get("note") or "")[:120],
            "when": now,
            "room": room,
        }
        data["words"] = [x for x in data["words"] if x.get("id") != nid]
        data["words"].append(row)
        data["words"] = data["words"][-40:]
        save_hall_pda(data)
        _pda_stamp_lexicon(surface, row["gloss"], lang)
        return {"ok": True, "pda": {**data, "lang": lang}, "item": row}
    if op == "note":
        text = str(body.get("text") or "").strip()[:240]
        if not text:
            return {"ok": False, "error": "text required"}
        nid = str(body.get("id") or "").strip() or (
            "n-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        )
        nid = re.sub(r"[^a-zA-Z0-9._-]", "-", nid)[:80]
        row = {"id": nid, "text": text, "when": now, "room": room}
        data["notes"] = [x for x in data["notes"] if x.get("id") != nid]
        data["notes"].append(row)
        data["notes"] = data["notes"][-40:]
        save_hall_pda(data)
        return {"ok": True, "pda": {**data, "lang": lang}, "item": row}
    if op == "delete":
        iid = str(body.get("id") or "").strip()
        if not iid:
            return {"ok": False, "error": "id"}
        data["words"] = [x for x in data["words"] if x.get("id") != iid]
        data["notes"] = [x for x in data["notes"] if x.get("id") != iid]
        save_hall_pda(data)
        return {"ok": True, "pda": {**data, "lang": lang}}
    return {"ok": False, "error": "bad op"}


def hall_payload(state: dict) -> dict:
    today = state.get("today") or {}
    cpu = state.get("cpu") or {}
    graph = state.get("graph") or {}
    lang = state.get("language") or {}
    inflow = state.get("inflow") or {}
    self_pack = state.get("self") or {}
    cron = state.get("cron") or {}
    schedule = state.get("schedule") or {}
    skills = state.get("skills") or {}
    goals = state.get("goals") or {}
    studies = state.get("studies") or []
    tmp = state.get("tmp") or {}
    mezz = state.get("mezzanine") or {}

    organs = []
    for o in (state.get("organs") or [])[:18]:
        organs.append(
            {
                "tag": o.get("tag") or "",
                "name": o.get("name") or "",
                "kind": _trim(o.get("kind"), 120),
                "meaning": _trim(o.get("meaning"), 200),
            }
        )

    actions = []
    for a in (today.get("actions") or [])[:14]:
        if a.get("kind") == "injury":
            # flags only — no lesion-site expansion
            actions.append(
                _item(
                    "today",
                    f"injury · {a.get('source')}",
                    a.get("text") or "",
                    "self/training.toon.md",
                )
            )
        else:
            actions.append(
                _item(
                    a.get("kind") or "today",
                    f"{a.get('kind')} · {a.get('source')}",
                    a.get("text") or "",
                    "",
                )
            )

    cpu_items = []
    headline = (cpu.get("note_today") or {}).get("headline") or today.get("headline")
    if headline:
        cpu_items.append(_item("note", "NOTE TODAY", headline, "CPU.md"))
    for ag in (cpu.get("agents") or [])[:8]:
        cpu_items.append(
            _item(
                "agent",
                f"AGENT {ag.get('id')}",
                f"$when={ag.get('when')} · {ag.get('prompt')}",
                "CPU.md",
            )
        )
    for td in (cpu.get("todos") or [])[:10]:
        mark = "DONE" if td.get("done") else "OPEN"
        cpu_items.append(_item("todo", f"TODO {mark}", td.get("text") or "", "CPU.md"))
    for sc in (cpu.get("schedules") or [])[:6]:
        cpu_items.append(_item("schedule", "SCHEDULE", sc.get("text") or "", "CPU.md"))

    branch_counts = graph.get("branch_counts") or {}
    verts = graph.get("verts") or []
    by_branch: dict[str, list] = {}
    for v in verts:
        b = v.get("branch") or "other"
        by_branch.setdefault(b, []).append(v)
    ped_items = [
        _item(
            "graph",
            "universe.graph",
            f"V{graph.get('v_count') or 0} E{graph.get('e_count') or 0} · 本体在 pedagogy/，不是履历。",
            "pedagogy/universe.graph.md",
        )
    ]
    for b, n in sorted(branch_counts.items(), key=lambda kv: -kv[1])[:8]:
        samples = by_branch.get(b) or []
        glosses = " · ".join(
            _trim(s.get("gloss") or s.get("id"), 40) for s in samples[:4]
        )
        ped_items.append(
            _item("branch", f"{b} ×{n}", glosses or "no gloss", f"pedagogy/{b}/")
        )
    empty = [s for s in studies if not s.get("answered")][:8]
    for s in empty:
        ped_items.append(
            _item(
                "probe",
                f"empty PROBE · {s.get('id')}",
                (s.get("probe") or s.get("why") or "PROBE empty. Do not invent ANSWER."),
                "pedagogy/pedagogy-cpu.fu.md",
                {"locked": True},
            )
        )

    hz = lang.get("horizon") or {}
    langs = hz.get("langs") or []
    focus = lang.get("oneFocus") or ""
    lang_items = [
        _item(
            "horizon",
            f"horizon · {hz.get('count') or len(langs)} langs",
            f"age {hz.get('age_target') or '?'} · {(hz.get('want') or '')[:180]}",
            "pedagogy/_learn/polyglot/horizon.toon.md",
        ),
        _item(
            "focus",
            f"todayFocus · {lang.get('targetLang') or 'de'}",
            focus or "(no oneFocus in state)",
            "pedagogy/_learn/writing-accuracy/state.toon.md",
        ),
    ]
    for L in langs[:16]:
        lang_items.append(
            _item(
                "lang",
                f"{L.get('code')} · {L.get('name')}",
                f"band {L.get('band')} · script {L.get('script') or '—'}",
                "pedagogy/_learn/polyglot/horizon.toon.md",
            )
        )
    poly_n = ((lang.get("polyglot") or {}).get("v_count")) or len(
        ((lang.get("polyglot") or {}).get("verts") or [])
    )
    wort_n = ((lang.get("wortschatz") or {}).get("v_count")) or len(
        ((lang.get("wortschatz") or {}).get("verts") or [])
    )
    if not poly_n:
        poly = lang.get("polyglot") or {}
        poly_n = len(poly.get("verts") or [])
        wort_n = len((lang.get("wortschatz") or {}).get("verts") or [])
    lang_items.append(
        _item(
            "store",
            "bridge / lexicon",
            f"polyglot verts {poly_n} · wortschatz verts {wort_n} · labels are word faces, not vertex ids.",
            "pedagogy/_learn/polyglot/bridge.graph.md",
        )
    )

    cipher_plain = focus or (lang.get("targetLang") or "in + Akk")
    inflow_items = []
    st = inflow.get("state") or {}
    if st:
        inflow_items.append(
            _item(
                "state",
                "inflow STATE",
                " · ".join(
                    x
                    for x in (
                        st.get("loop"),
                        st.get("maintain"),
                        f"last_organ {st.get('last_organ')}" if st.get("last_organ") else "",
                    )
                    if x
                )
                or "STATE header",
                "inflow/STATE.md",
            )
        )
    for d in (inflow.get("digest") or [])[:12]:
        urls = list(d.get("urls") or []) + list(d.get("sources") or [])
        inflow_items.append(
            _item(
                d.get("lane") or "dump",
                d.get("title") or d.get("id") or "CAPTURE",
                _trim(d.get("note") or d.get("why") or d.get("kind") or d.get("id"), 420),
                "inflow/DUMP.md",
                {"urls": urls, "url": urls[0] if urls else ""},
            )
        )
    for n in (inflow.get("news") or [])[:6]:
        n_urls = list(n.get("urls") or []) + ([n.get("url")] if n.get("url") else [])
        inflow_items.append(
            _item(
                "news",
                n.get("title") or n.get("id") or "NEWS",
                n.get("why") or "",
                "inflow/inflow.fu.md",
                {"urls": n_urls, "url": n_urls[0] if n_urls else ""},
            )
        )

    goals_north = goals.get("north") or []
    self_items = [
        _item("goals", f"focus · {goals.get('focus') or '—'}", ", ".join(goals.get("active") or [])[:200], "self/goals.toon.md"),
        _item("north", "goals.north", ", ".join(goals_north[:8]) or "(empty)", "self/goals.toon.md"),
        _item(
            "endurance",
            "endurance budget",
            (self_pack.get("endurance") or {}).get("budget_now") or "",
            "self/endurance.toon.md",
        ),
        _item(
            "train",
            "training flags",
            ", ".join((self_pack.get("training") or {}).get("flags_true") or [])[:220],
            "self/training.toon.md",
        ),
    ]
    for f in (self_pack.get("files") or [])[:10]:
        self_items.append(_item("file", f.get("name") or "", f.get("kind") or "", f.get("path") or f"self/{f.get('name')}"))

    cron_items = []
    for j in (cron.get("jobs") or [])[:14]:
        cron_items.append(
            _item(
                "job",
                Path(j.get("file") or "").name,
                f"{j.get('kind')} · agents {', '.join(j.get('agents') or []) or '—'} · {'RECURRING' if j.get('recurring') else 'once'}",
                j.get("file") or "cron/",
            )
        )

    sched_items = []
    for r in (schedule.get("harvest") or [])[:10]:
        sched_items.append(
            _item(
                r.get("status") or "harvest",
                r.get("title") or r.get("id") or "row",
                f"{r.get('start') or ''} {r.get('where') or ''} · {r.get('status') or ''}",
                "schedule/harvest.toon.md",
            )
        )
    for t in (schedule.get("cpu_schedules") or [])[:6]:
        sched_items.append(_item("cpu", "CPU SCHEDULE", t.get("text") or "", "CPU.md"))

    skill_items = []
    for s in (skills.get("cursor_skills") or [])[:16]:
        skill_items.append(
            _item("skill", s.get("name") or "", s.get("description") or "", s.get("path") or "")
        )
    for f in (skills.get("library") or [])[:8]:
        skill_items.append(_item("lib", f.get("name") or "", f.get("kind") or "", f.get("path") or ""))

    tmp_items = [
        _item(
            "ttl",
            "tmp TTL",
            json.dumps(tmp.get("ttl") or {}, ensure_ascii=False)[:200],
            "tmp/ttl.toon.md",
        )
    ]
    for sib in (tmp.get("siblings") or [])[:10]:
        tmp_items.append(_item(sib.get("kind") or "file", sib.get("name") or "", "", f"tmp/{sib.get('name')}"))

    mezz_items = []
    for f in (mezz.get("files") or [])[:12]:
        mezz_items.append(_item("note", f.get("name") or "", "ingest note, not a claim", f.get("path") or f"mezzanine/{f.get('name')}"))

    probe = today.get("probe") or {}
    clips = _collect_clips(state)
    war = _war_pack(state)
    library = _library_pack(state, clips)
    lib_items = []
    for b in (library.get("books") or [])[:24]:
        url = b.get("url") or ""
        extra = {
            "teleport": "library",
            "url": url,
            "urls": [url] if url else [],
            "shelf": b.get("shelf") or "user",
        }
        if b.get("crud"):
            extra["crud"] = True
            extra["id"] = b.get("id")
        row = _item(
            b.get("kind") or "page",
            b.get("title") or "book",
            b.get("body") or b.get("shelf") or "",
            "inflow/hall-library.toon.md",
            extra,
        )
        if b.get("media"):
            row["media"] = b["media"]
        lib_items.append(row)
    war_items = [
        _item(
            "war",
            "Lagezentrale",
            f"fog={war.get('sore') or ('named' if war.get('foggy') else 'not named')} · budget {war.get('budget')} · alerts {len(war.get('alerts') or [])}",
            "self/recovery-cycle.toon.md",
            {"teleport": "war"},
        )
    ]
    for al in (war.get("alerts") or [])[:8]:
        war_items.append(
            _item(
                al.get("kind") or "war",
                al.get("title") or al.get("id") or "alert",
                al.get("body") or "",
                "self/recovery-cycle.toon.md",
                {"teleport": "war"},
            )
        )
    sore_n = sum(1 for m in (war.get("muscles") or []) if m.get("status") in {"sore", "flag"})
    war_items.append(
        _item(
            "train",
            f"muscles · {sore_n} flagged",
            " · ".join(
                f"{m.get('label')}:{m.get('status')}"
                for m in (war.get("muscles") or [])
                if m.get("status") != "unreported"
            )[:220]
            or "all unreported",
            "self/training.toon.md",
            {"teleport": "war"},
        )
    )
    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "today": {
            "date": today.get("date") or "",
            "weekday": today.get("weekday") or "",
            "headline": _trim(today.get("headline"), 280),
            "focus": today.get("focus") or "",
            "plan_now": today.get("plan_now") or "",
            "foggy": bool(today.get("foggy")),
            "pending_dumps": today.get("pending_dumps") or 0,
            "probe": {
                "id": probe.get("id") or "",
                "text": _trim(probe.get("text"), 360),
                "answered": bool(probe.get("answered")),
            },
        },
        "stats": {
            "v": graph.get("v_count") or 0,
            "e": graph.get("e_count") or 0,
            "empty_probes": len(empty),
            "agents": len(cpu.get("agents") or []),
            "langs": len(langs),
            "clips": len(clips),
            "books": len(library.get("books") or []),
        },
        "organs": organs,
        "clips": clips,
        "graph_preview": _graph_preview(graph),
        "cipher": {
            "shift": 3,
            "plain": cipher_plain,
            "encoded": _caesar(cipher_plain, 3),
            "hint": "Caesar +3 on todayFocus — Cypher homage. Decode at the language desk.",
        },
        "rooms": {
            "nave": {
                "title": "ROOT · the living hall",
                "hint": "Organs are different KINDs. Walk a doorway; do not flatten them into one graph.",
                "items": organs[:12] and [
                    _item(
                        "organ",
                        f"{o['tag']} {o['name']}",
                        o["meaning"] or o["kind"],
                        o.get("name") or "",
                    )
                    for o in organs[:12]
                ]
                + actions,
            },
            "cpu": {
                "title": "CPU · run queue",
                "hint": "AGENT / TODO / SCHEDULE. Not archive. Not ontology.",
                "items": cpu_items,
            },
            "pedagogy": {
                "title": "Pedagogy · what is",
                "hint": "Empty PROBE stays empty. Tablets with a lock are unsolved.",
                "items": ped_items,
            },
            "language": {
                "title": "Language · 16 named → B2+",
                "hint": "Word faces, not vertex ids. Cipher desk is the Cypher nod.",
                "items": lang_items,
            },
            "inflow": {
                "title": "Inflow · inbound buffer",
                "hint": "Not the life queue. Drip when asked.",
                "items": inflow_items,
            },
            "self": {
                "title": "Self · particulars",
                "hint": "Goals, endurance, training flags. No .private paste.",
                "items": self_items,
            },
            "cron": {
                "title": "Cron · gatherers",
                "hint": "Scheduled jobs. Not the briefing. Not CPU.",
                "items": cron_items,
            },
            "schedule": {
                "title": "Schedule · calendar store",
                "hint": "Harvested rows. CPU still arms ticks.",
                "items": sched_items,
            },
            "skills": {
                "title": "Skills · agent libraries",
                "hint": "Spawn only when CPU or pedagogy-cpu names them.",
                "items": skill_items + mezz_items[:4] + tmp_items[:4],
            },
            "war": {
                "title": "作战室 · Lagezentrale",
                "hint": "World map, body holograph, named states only. No .private paste. Unreported muscle is not sore.",
                "items": war_items,
            },
            "library": {
                "title": "书库 · Pudong stacks",
                "hint": "Wood atrium, shelves by kind, PDF/YouTube URLs. N adds a book. M quad screens. G flashcards. No .private. Empty PROBE stays empty.",
                "items": lib_items,
            },
        },
        "war": war,
        "library": library,
        "watch": _watch_pack(),
        "pda": {
            **load_hall_pda(),
            "lang": (lang.get("targetLang") or "de"),
        },
    }
    _apply_board(payload)
    return payload


def write_hall(payload: dict, path: Path) -> None:
    html = TEMPLATE.read_text(encoding="utf-8")
    blob = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
    if "__HALL_JSON__" not in html:
        raise SystemExit("template missing __HALL_JSON__")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html.replace("__HALL_JSON__", blob), encoding="utf-8")


def _free_port(host: str, start: int) -> int:
    for port in range(start, start + 8):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind((host, port))
            except OSError:
                continue
            return port
    raise SystemExit("no free port")


def serve(path: Path, host: str, port: int, open_browser: bool, rebuild) -> int:
    class Handler(http.server.BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"

        def log_message(self, fmt, *args):
            sys.stderr.write("HALL " + (fmt % args) + "\n")

        def _json(self, code: int, obj: dict) -> None:
            raw = json.dumps(obj, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("content-type", "application/json; charset=utf-8")
            self.send_header("cache-control", "no-store")
            self.send_header("content-length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def do_GET(self) -> None:
            from urllib.parse import unquote, urlparse

            pth = unquote(urlparse(self.path).path)
            if pth in {"/", "/index.html", "/mindcraft-hall.html"}:
                if rebuild:
                    try:
                        rebuild()
                    except Exception as exc:
                        sys.stderr.write(f"HALL rebuild failed: {exc}\n")
                raw = path.read_bytes()
                self.send_response(200)
                self.send_header("content-type", "text/html; charset=utf-8")
                self.send_header("cache-control", "no-store")
                self.send_header("permissions-policy", "autoplay=*, fullscreen=*")
                self.send_header("content-length", str(len(raw)))
                self.end_headers()
                self.wfile.write(raw)
                return
            if pth == "/api/board":
                self._json(200, {"ok": True, "items": load_hall_board()})
                return
            if pth == "/api/library":
                self._json(200, {"ok": True, "items": load_hall_library()})
                return
            if pth == "/api/day":
                day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
                self._json(200, {"ok": True, "items": load_hall_day(day)})
                return
            if pth == "/api/watch":
                self._json(200, {"ok": True, "watch": _watch_pack()})
                return
            if pth == "/api/pda":
                self._json(200, {"ok": True, "pda": load_hall_pda()})
                return
            if pth.startswith("/media/"):
                rel = Path(unquote(pth[len("/media/") :]))
                target = (ROOT / rel).resolve()
                tmp_root = (ROOT / "tmp").resolve()
                try:
                    target.relative_to(tmp_root)
                except ValueError:
                    self.send_error(403)
                    return
                if not target.is_file():
                    self.send_error(404)
                    return
                data = target.read_bytes()
                ctype = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
                self.send_response(200)
                self.send_header("content-type", ctype)
                self.send_header("content-length", str(len(data)))
                self.send_header("cache-control", "public, max-age=120")
                self.end_headers()
                self.wfile.write(data)
                return
            self.send_error(404)

        def do_POST(self) -> None:
            from urllib.parse import urlparse

            pth = urlparse(self.path).path
            n = int(self.headers.get("content-length") or "0")
            raw = self.rfile.read(n) if n else b"{}"
            try:
                body = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                self._json(400, {"ok": False, "error": "bad json"})
                return
            if pth == "/api/watch":
                out = watch_mutate(body if isinstance(body, dict) else {})
                self._json(200 if out.get("ok") else 400, out)
                return
            if pth == "/api/pda":
                out = pda_mutate(body if isinstance(body, dict) else {})
                self._json(200 if out.get("ok") else 400, out)
                return
            if pth == "/api/day":
                out = day_mutate(body if isinstance(body, dict) else {})
                if out.get("ok") and rebuild:
                    try:
                        rebuild()
                    except Exception as exc:
                        sys.stderr.write(f"HALL rebuild failed: {exc}\n")
                self._json(200 if out.get("ok") else 400, out)
                return
            if pth == "/api/library":
                out = library_mutate(body if isinstance(body, dict) else {})
                if out.get("ok") and rebuild:
                    try:
                        rebuild()
                    except Exception as exc:
                        sys.stderr.write(f"HALL rebuild failed: {exc}\n")
                self._json(200 if out.get("ok") else 400, out)
                return
            if pth != "/api/board":
                self.send_error(404)
                return
            out = board_mutate(body if isinstance(body, dict) else {})
            if out.get("ok") and rebuild:
                try:
                    rebuild()
                except Exception as exc:
                    sys.stderr.write(f"HALL rebuild failed: {exc}\n")
            self._json(200 if out.get("ok") else 400, out)

    class Reuse(socketserver.TCPServer):
        allow_reuse_address = True

    httpd = Reuse((host, port), Handler)
    url = f"http://{host}:{port}/mindcraft-hall.html"
    print(f"HALL {url}", flush=True)
    if open_browser:
        webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("HALL stop")
    finally:
        httpd.server_close()
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--serve", action="store_true")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=8781)
    p.add_argument("--no-open", action="store_true")
    p.add_argument("--out", type=Path, default=OUT)
    args = p.parse_args()
    psv = _load_psv()
    state = psv.collect_state()
    payload = hall_payload(state)
    write_hall(payload, args.out)
    psv.stamp_ttl()
    print(f"DELIVERED {args.out}", flush=True)
    print(
        f"V{payload['stats']['v']} empty_probes={payload['stats']['empty_probes']} "
        f"langs={payload['stats']['langs']}",
        flush=True,
    )
    if args.serve:
        port = args.port if args.port else 8781
        if args.port == 8781:
            port = _free_port(args.host, 8781)

        def _rebuild() -> None:
            st = psv.collect_state()
            write_hall(hall_payload(st), args.out)

        return serve(
            args.out,
            args.host,
            port,
            open_browser=not args.no_open,
            rebuild=_rebuild,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
