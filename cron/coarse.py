"""Strip pinpointable place and ID strings from public render text."""
from __future__ import annotations

import re

STREET_RE = re.compile(
    r"\b[\w.ÄÖÜäöüß-]+(?:straße|strasse|str\.|weg|damm|platz|allee|ring)\s+\d+(?:\s*[–-]\s*\d+)?",
    re.IGNORECASE,
)
PLZ_RE = re.compile(r"\b\d{5}\b")
LIVE_RE = re.compile(r"I live in [^.]*\.?", re.IGNORECASE)
PRIVATE_RE = re.compile(r"\.private/\S+")
ID_RE = re.compile(
    r"\b(Ausweis|Meldebescheinigung|Melde|Terminbestätigung|bag list|ID list|file number)\b[^.]*\.?",
    re.IGNORECASE,
)
HALL_RE = re.compile(r"\bHall(?:e)?\s*\d+(?:\.\d+)?(?:\s*/\s*\d+)?\b", re.IGNORECASE)
STAND_RE = re.compile(r"\b(?:Stand|H)\d[\w.-]*\b", re.IGNORECASE)


def coarse_place(text: str) -> str:
    if not text:
        return ""
    s = STREET_RE.sub("", text)
    s = HALL_RE.sub("", s)
    s = STAND_RE.sub("", s)
    s = PLZ_RE.sub("", s)
    s = LIVE_RE.sub("", s)
    s = PRIVATE_RE.sub("", s)
    s = ID_RE.sub("", s)
    s = re.sub(r"\s*,\s*,+", ",", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip(" ,;./")
