#!/usr/bin/env python3
"""Shared polyglot language detection + code-switch gap heuristics."""
from __future__ import annotations

import re
from collections import Counter

# Proper nouns / tech allowlist — not treated as expression gaps.
ALLOW = {
    "todo",
    "repo",
    "api",
    "pr",
    "mcp",
    "cpu",
    "path",
    "url",
    "html",
    "pdf",
    "mp4",
    "json",
    "yaml",
    "git",
    "github",
    "cursor",
    "claude",
    "kiro",
    "aws",
    "bedrock",
    "laptop",  # borrowed noun used in DE; still allow as proper-ish tech
    "dump",
    "hook",
    "hooks",
    "skill",
    "skills",
    "agent",
    "agents",
    "prompt",
    "ontology",
    "graph",
    "vertex",
    "studio",
    "bilibili",
}

MARKERS: dict[str, set[str]] = {
    "de": {
        "der",
        "die",
        "das",
        "und",
        "ich",
        "nicht",
        "für",
        "fur",
        "auf",
        "mit",
        "ist",
        "ein",
        "eine",
        "einen",
        "einem",
        "eines",
        "lass",
        "lassen",
        "bitte",
        "aber",
        "oder",
        "auch",
        "noch",
        "schon",
        "wenn",
        "dann",
        "mir",
        "dir",
        "uns",
        "euch",
        "kein",
        "keine",
        "dieser",
        "diese",
        "dieses",
        "nach",
        "von",
        "zu",
        "im",
        "am",
        "zum",
        "zur",
        "heute",
        "jetzt",
        "projekt",
        "zustand",
        "änderung",
        "anderung",
        "gib",
        "mache",
        "mach",
        "liegt",
        "tauchen",
        "eintauchen",
        "vergessen",
        "dass",
        "daß",
    },
    "en": {
        "the",
        "and",
        "for",
        "with",
        "please",
        "this",
        "that",
        "make",
        "give",
        "let",
        "lets",
        "don't",
        "dont",
        "not",
        "into",
        "from",
        "have",
        "has",
        "are",
        "is",
        "be",
        "do",
        "does",
        "can",
        "will",
        "would",
        "should",
        "about",
        "after",
        "before",
        "deeper",
        "update",
        "updated",
        "current",
        "state",
        "change",
        "changes",
        "today",
        "now",
        "project",
        "without",
        "but",
        "just",
        "also",
        "only",
    },
    "es": {
        "el",
        "la",
        "los",
        "las",
        "que",
        "para",
        "con",
        "una",
        "uno",
        "por",
        "como",
        "más",
        "mas",
        "está",
        "esta",
        "hay",
        "también",
        "tambien",
        "hoy",
        "ahora",
        "proyecto",
        "dame",
        "haz",
        "sin",
        "pero",
    },
    "fr": {
        "le",
        "la",
        "les",
        "des",
        "un",
        "une",
        "et",
        "pour",
        "avec",
        "pas",
        "que",
        "qui",
        "dans",
        "sur",
        "est",
        "sont",
        "aujourd",
        "projet",
        "mais",
        "aussi",
    },
}

# Latin words, CJK runs, or hybrid code-switch like 内化-ed
TOKEN_RE = re.compile(
    r"[A-Za-zÀ-ÿÄÖÜäöüß]+|[\u4e00-\u9fff]+(?:-[A-Za-z]+)?",
    re.UNICODE,
)


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text or "")


def script_mass(tokens: list[str]) -> Counter:
    c: Counter = Counter()
    for t in tokens:
        if re.search(r"[\u4e00-\u9fff]", t):
            # Per token, not per character — otherwise a ZH stretch drowns DE/FR markers.
            c["zh"] += 1
        elif re.search(r"[ÄÖÜäöüß]", t):
            c["de"] += 2
        elif re.search(r"[À-ÿ]", t):
            c["romance"] += 1
        else:
            c["latin"] += 1
    return c


def score_langs(tokens: list[str]) -> Counter:
    scores: Counter = Counter()
    lower = [t.lower() for t in tokens]
    for lang, words in MARKERS.items():
        for t in lower:
            if t in words:
                scores[lang] += 1
    sm = script_mass(tokens)
    if sm.get("zh", 0):
        scores["zh"] += sm["zh"]
    if sm.get("de", 0):
        scores["de"] += sm["de"]
    # weak prior: latin-only unmarked tokens don't invent a language
    return scores


def primary_lang(text: str, default: str = "en") -> tuple[str, Counter]:
    tokens = tokenize(text)
    if not tokens:
        return default, Counter()
    scores = score_langs(tokens)
    if not scores:
        if any(re.search(r"[\u4e00-\u9fff]", t) for t in tokens):
            return "zh", Counter(zh=len(tokens))
        return default, Counter()
    # Grammar-word evidence beats CJK mass: after a ZH stretch, a DE/FR/ES
    # coding prompt still counts as attempting that language (≥2 markers).
    for lang in ("de", "fr", "es"):
        if scores.get(lang, 0) >= 2:
            return lang, scores
    return scores.most_common(1)[0][0], scores


def foreign_islands(
    text: str,
    primary: str,
    target: str,
    scores: Counter | None = None,
) -> list[dict]:
    """Sparse non-target tokens → expression gaps when the utterance attempts targetLang."""
    tokens = tokenize(text)
    lower = [t.lower() for t in tokens]
    scores = scores or Counter()
    target_score = scores.get(target, 0)
    primary_score = scores.get(primary, 0) or 1
    attempting_target = (
        primary == target
        or target_score >= 2
        or (target_score / primary_score) >= 0.35
    )
    if not attempting_target:
        return []

    gaps: list[dict] = []
    seen: set[str] = set()

    en_content = {
        "deeper",
        "update",
        "updated",
        "current",
        "state",
        "change",
        "changes",
        "please",
        "without",
        "after",
        "before",
        "today",
        "project",
        "make",
        "give",
        "lets",
        "don't",
        "dont",
        "dive",
        "diving",
        "forget",
        "remember",
        "list",
    }

    for raw, low in zip(tokens, lower):
        if low in ALLOW or (raw.isupper() and len(raw) <= 6):
            continue
        src = None
        if re.search(r"[\u4e00-\u9fff]", raw):
            src = "zh"
        else:
            for lang, words in MARKERS.items():
                if low in words and lang != target:
                    src = lang
                    break
            if src is None and low in en_content and target != "en":
                src = "en"
        if src is None or src == target:
            continue
        key = f"{src}:{low}"
        if key in seen:
            continue
        seen.add(key)
        gaps.append(
            {
                "surface": raw,
                "fromLang": src,
                "targetLang": target,
                "kind": "code_switch_gap",
                "meaning": "unknown-how-to-say-in-target",
            }
        )
    return gaps[:20]


def analyze(text: str, target: str = "de") -> dict:
    primary, scores = primary_lang(text, default="en")
    # Prefer target as primary when it is a close second (coding prompt mostly in target).
    if target in scores and primary != target:
        if scores[target] >= scores[primary] * 0.8 or scores[target] >= 2:
            primary = target
    gaps = foreign_islands(text, primary, target, scores)
    n = len(tokenize(text))
    method_hit = bool(n) and (
        scores.get(target, 0) >= 2
        or (primary in {"de", "fr", "es"} and scores.get(primary, 0) >= 2)
    )
    return {
        "primaryLang": primary,
        "targetLang": target,
        "scores": dict(scores),
        "gaps": gaps,
        "tokenCount": n,
        "mix": bool(gaps),
        "methodHit": method_hit,
    }
