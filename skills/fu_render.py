#!/usr/bin/env python3
"""Parse .fu.md nested lists and render HTML. Unknown TAG still renders.

Fu form (ROOT): nested unordered lists. First token after "- " is TAG in CAPITAL
or CAPITAL_SNAKE. Nested list is scope. Domain nouns are not TAG.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

TAG_RE = re.compile(r"^- ([A-Z][A-Z0-9_]*)(?:\s+(.*))?$")
MEDIA_KINDS = ("PAGE", "VIDEO", "FIG", "AUDIO", "CODE", "GEO", "IMAGE")

# Visual families for known tags (unknown → generic)
TAG_CLASS = {
    "VERTEX": "fu-meta",
    "KIND": "fu-meta",
    "GLOSS": "fu-meta",
    "STORE": "fu-store",
    "CLAIM": "fu-claim",
    "SOURCE": "fu-source",
    "MEDIA": "fu-media",
    "NOTE": "fu-note",
    "CONTRADICT": "fu-warn",
    "BLOCKER": "fu-warn",
    "PROBE": "fu-learn",
    "ANSWER": "fu-learn",
    "ASSESS": "fu-learn",
    "RECALL": "fu-learn",
    "GAP": "fu-learn",
    "DRILL": "fu-learn",
    "STUDY": "fu-learn",
    "PLAN": "fu-plan",
    "DAY": "fu-plan",
    "DO": "fu-plan",
    "NOW": "fu-plan",
    "NEXT": "fu-plan",
    "DONE": "fu-done",
    "WHY": "fu-note",
    "AGENT": "fu-agent",
    "SCHEDULE": "fu-agent",
    "TODO": "fu-agent",
    "RECURRING": "fu-agent",
    "RESEARCH": "fu-agent",
    "DUMP": "fu-agent",
    "LEARNING_DUMP": "fu-agent",
    "PROFILE": "fu-meta",
    "OUTPUT": "fu-store",
    "PROTOCOL": "fu-meta",
    "RULE": "fu-note",
    "ASK": "fu-note",
    "RUN": "fu-store",
    "ADJUST": "fu-plan",
    "PHASE": "fu-learn",
    "STOP": "fu-warn",
    "SORE": "fu-warn",
    "LOAD": "fu-plan",
    "EXTERNAL": "fu-plan",
    "TZ": "fu-meta",
    "LANG": "fu-meta",
    "FILE": "fu-meta",
    "FORM": "fu-meta",
    "DIR": "fu-meta",
    "TAG": "fu-meta",
    "NOT_TAG": "fu-warn",
    "KV": "fu-meta",
    "MEANING": "fu-note",
    "INTERFACE": "fu-meta",
    "GRAPH": "fu-meta",
    "SCHEMA": "fu-meta",
    "FOLDERS": "fu-meta",
    "TRAVERSE": "fu-meta",
    "EDGE": "fu-meta",
    "LABEL": "fu-meta",
    "BODY": "fu-note",
    "CLOCK": "fu-plan",
    "LOOP": "fu-agent",
    "LEARN": "fu-learn",
    "HUMAN": "fu-note",
    "SKILL": "fu-store",
    "TMP": "fu-store",
    "STATE": "fu-store",
    "CONTEXT": "fu-store",
    "EXECUTION": "fu-meta",
    "EXECUTED": "fu-meta",
}


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def parse_fu(text: str) -> list[dict]:
    """Return forest of {tag, payload, children}."""
    roots: list[dict] = []
    stack: list[tuple[int, dict]] = []  # indent, node

    for raw in text.splitlines():
        if not raw.strip():
            continue
        stripped = raw.lstrip(" ")
        if not stripped.startswith("- "):
            if stack:
                node = stack[-1][1]
                cont = raw.strip()
                if cont:
                    node["payload"] = (node.get("payload") or "") + " " + cont
            continue
        ind = _indent(raw)
        body = stripped[2:]
        m = re.match(r"^([A-Z][A-Z0-9_]*)(?:\s+(.*))?$", body)
        if m:
            tag, payload = m.group(1), (m.group(2) or "").strip()
        else:
            tag, payload = "_TEXT", body.strip()

        node = {"tag": tag, "payload": payload, "children": []}
        while stack and stack[-1][0] >= ind:
            stack.pop()
        if stack:
            stack[-1][1]["children"].append(node)
        else:
            roots.append(node)
        stack.append((ind, node))
    return roots


def _linkify(payload: str) -> str:
    esc = html.escape(payload)
    return re.sub(
        r"(https?://[^\s<]+)",
        r'<a href="\1" target="_blank" rel="noopener">\1</a>',
        esc,
    )


def _media_html(payload: str) -> str:
    parts = payload.split(None, 1)
    kind = parts[0] if parts else ""
    rest = parts[1] if len(parts) > 1 else ""
    if kind in MEDIA_KINDS and rest.startswith("http"):
        label = html.escape(kind)
        url = html.escape(rest)
        if kind == "VIDEO":
            return (
                f'<div class="fu-media-card"><span class="fu-pill">{label}</span> '
                f'<a href="{url}" target="_blank" rel="noopener">{url}</a>'
                f'<div class="fu-embed"><iframe src="{url}" loading="lazy" '
                f'allowfullscreen referrerpolicy="no-referrer"></iframe></div></div>'
            )
        return (
            f'<div class="fu-media-card"><span class="fu-pill">{label}</span> '
            f'<a href="{url}" target="_blank" rel="noopener">{url}</a></div>'
        )
    return _linkify(payload)


def render_node(node: dict, depth: int = 0) -> str:
    tag = node.get("tag") or "_TEXT"
    payload = node.get("payload") or ""
    kids = node.get("children") or []
    cls = TAG_CLASS.get(tag, "fu-generic")

    if tag == "_TEXT":
        inner = _linkify(payload)
        child_html = "".join(render_node(c, depth + 1) for c in kids)
        if child_html:
            return f'<div class="fu-text">{inner}<div class="fu-nest">{child_html}</div></div>'
        return f'<div class="fu-text">{inner}</div>'

    if tag == "MEDIA":
        body = _media_html(payload)
    elif tag == "STORE" and payload.upper().startswith("PATH "):
        path = html.escape(payload[5:].strip())
        body = f'<code class="fu-path">{path}</code>'
    elif tag in ("SOURCE",) or payload.startswith("http"):
        body = _linkify(payload)
    else:
        body = _linkify(payload)

    child_html = "".join(render_node(c, depth + 1) for c in kids)
    nest = f'<div class="fu-nest">{child_html}</div>' if child_html else ""
    return (
        f'<article class="fu-node {cls}" data-tag="{html.escape(tag)}">'
        f'<header><span class="fu-tag">{html.escape(tag)}</span>'
        f'<span class="fu-payload">{body}</span></header>{nest}</article>'
    )


def render_fu(text: str) -> str:
    forest = parse_fu(text)
    if not forest:
        return '<p class="fu-empty">Empty .fu.md</p>'
    return '<div class="fu-doc">' + "".join(render_node(n) for n in forest) + "</div>"


def render_fu_file(path: Path) -> dict:
    if not path.exists():
        return {
            "ok": False,
            "path": str(path),
            "html": f'<p class="fu-empty">Missing {html.escape(str(path))}</p>',
            "raw": "",
            "tags": [],
        }
    raw = path.read_text(encoding="utf-8")
    forest = parse_fu(raw)
    tags = sorted({n["tag"] for n in _walk(forest) if n["tag"] != "_TEXT"})
    return {
        "ok": True,
        "path": path.as_posix(),
        "html": render_fu(raw),
        "raw": raw,
        "tags": tags,
    }


def _walk(nodes: list[dict]):
    for n in nodes:
        yield n
        yield from _walk(n.get("children") or [])


FU_CSS = """
.fu-doc { font-size: 13px; line-height: 1.45; }
.fu-node { border: 1px solid #2a3544; border-radius: 8px; padding: 10px 12px; margin: 0 0 8px; background: #121a24; }
.fu-node header { display: flex; gap: 10px; align-items: flex-start; flex-wrap: wrap; }
.fu-tag { font-size: 10px; letter-spacing: 0.06em; color: #69f0ae; border: 1px solid #2d4a3a; border-radius: 999px; padding: 1px 8px; flex: 0 0 auto; }
.fu-payload { color: #e8eef5; flex: 1 1 200px; }
.fu-payload a { color: #82b1ff; }
.fu-nest { margin: 8px 0 0 12px; padding-left: 10px; border-left: 2px solid #2a3544; }
.fu-claim { border-color: #3e4a2a; }
.fu-source { opacity: 0.92; }
.fu-media { border-color: #3a2a4a; }
.fu-media-card { display: grid; gap: 6px; }
.fu-pill { font-size: 10px; color: #ce93d8; }
.fu-embed iframe { width: 100%; min-height: 180px; border: 0; border-radius: 6px; background: #000; }
.fu-learn { border-color: #2a3a5a; background: #0f1624; }
.fu-warn { border-color: #5a3030; }
.fu-plan { border-color: #4a3a20; }
.fu-agent { border-color: #2a4a4a; }
.fu-meta .fu-tag { color: #8b9bb4; }
.fu-generic .fu-tag { color: #ffcc80; border-color: #5a4a30; }
.fu-text { color: #c5d0e0; margin: 4px 0; }
.fu-path { color: #69f0ae; word-break: break-all; }
.fu-empty { color: #8b9bb4; }
"""
