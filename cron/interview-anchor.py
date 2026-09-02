#!/usr/bin/env python3
"""Anchor AI-engineering interview titles onto the graph and write today's DAY.

    python cron/interview-anchor.py --fetch
    python cron/interview-anchor.py --anchor
    python cron/interview-anchor.py --day
    python cron/interview-anchor.py --day --date 2026-09-02
    python cron/interview-anchor.py --done --id q-012
    python cron/interview-anchor.py --sore --text "head pressure after 2"
    python cron/interview-anchor.py --print
    python cron/interview-anchor.py --apply
"""
from __future__ import annotations

import argparse
import json
import re
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
TZ = ZoneInfo("Europe/Berlin")
REPO = "https://github.com/amitshekhariitbhu/ai-engineering-interview-questions"
RAW = "https://raw.githubusercontent.com/amitshekhariitbhu/ai-engineering-interview-questions/master/README.md"
BANK = ROOT / "pedagogy" / "_learn" / "interview.toon.md"
DONE = ROOT / "self" / "interview.toon.md"
ENDURANCE = ROOT / "self" / "endurance.toon.md"
CPU = ROOT / "pedagogy" / "pedagogy-cpu.fu.md"
GRAPH = ROOT / "pedagogy" / "universe.graph.md"
NATURE = "https://www.nature.com/articles/s41586-024-07220-7"

NEW_VERTICES = [
    ("Transformer", "techne", "sequence-model-of-attention", "computation"),
    ("PromptEngineering", "praxis", "steering-a-model-with-language", "language"),
    ("RAG", "techne", "retrieve-then-generate", "computation"),
    ("FineTuning", "praxis", "adapting-weights-to-a-task", "computation"),
    ("Quantization", "techne", "fewer-bits-per-weight", "computation"),
    ("VectorDatabase", "techne", "nearest-neighbor-over-embeddings", "computation"),
    ("LLMOps", "praxis", "operating-models-in-production", "computation"),
    ("Evaluation", "praxis", "measuring-whether-a-model-did-the-job", "math"),
    ("AISafety", "praxis", "preventing-harm-from-model-actions", "computation"),
    ("Multimodal", "techne", "more-than-text-as-input", "computation"),
    ("IntellectualLoad", "praxis", "bounded-study-before-repair", "biology"),
]

NEW_EDGES = [
    ("Transformer", "APPLIES", "LargeLanguageModel", REPO),
    ("Transformer", "GROUNDS_IN", "Mathematics", REPO),
    ("PromptEngineering", "INFORMS", "LargeLanguageModel", REPO),
    ("PromptEngineering", "PARTICIPATES", "Language", REPO),
    ("RAG", "APPLIES", "LargeLanguageModel", REPO),
    ("RAG", "APPLIES", "VectorDatabase", REPO),
    ("FineTuning", "APPLIES", "LargeLanguageModel", REPO),
    ("Quantization", "APPLIES", "LargeLanguageModel", REPO),
    ("VectorDatabase", "APPLIES", "Computation", REPO),
    ("LLMOps", "APPLIES", "LargeLanguageModel", REPO),
    ("LLMOps", "APPLIES", "CloudRuntime", REPO),
    ("Evaluation", "STUDIES", "LargeLanguageModel", REPO),
    ("Evaluation", "GROUNDS_IN", "Mathematics", REPO),
    ("AISafety", "INFORMS", "Agent", REPO),
    ("Multimodal", "APPLIES", "LargeLanguageModel", REPO),
    ("IntellectualLoad", "ENACTS", "Study", "self/endurance.toon.md"),
    ("IntellectualLoad", "GROUNDS_IN", "DNADamageResponse", NATURE),
    ("IntellectualLoad", "PARTICIPATES", "ResistanceTraining", "self/endurance.toon.md"),
    ("Study", "STUDIES", "Transformer", REPO),
    ("Study", "STUDIES", "RAG", REPO),
    ("Study", "STUDIES", "PromptEngineering", REPO),
    ("Study", "STUDIES", "FineTuning", REPO),
    ("Study", "STUDIES", "MCP", REPO),
    ("Study", "STUDIES", "KVCache", REPO),
    ("Study", "STUDIES", "AgentLoop", REPO),
]

TOPIC_VERTEX = {
    "Must Know": "LargeLanguageModel",
    "LLM Fundamentals": "LargeLanguageModel",
    "Prompt Engineering": "PromptEngineering",
    "Retrieval-Augmented Generation (RAG)": "RAG",
    "AI Agents and Agentic Systems": "Agent",
    "Fine-Tuning and Model Adaptation": "FineTuning",
    "Vector Databases and Embeddings": "VectorDatabase",
    "AI System Design": "AgenticEngineering",
    "LLMOps and Production AI": "LLMOps",
    "Evaluation and Testing": "Evaluation",
    "AI Safety, Ethics, and Responsible AI": "AISafety",
    "Multimodal AI": "Multimodal",
    "AI Infrastructure and Scalability": "CloudRuntime",
    "Coding and Practical Implementation": "Python",
    "Behavioral and Scenario-Based Questions": "Study",
}

HINTS = [
    ("kv cache", "KVCache"),
    ("paged attention", "KVCache"),
    ("model context protocol", "MCP"),
    ("sandbox", "LambdaMicroVM"),
    ("microvm", "LambdaMicroVM"),
    ("agent toolkit", "AgentToolkit"),
    ("agentcore", "AgentCore"),
    ("agent loop", "AgentLoop"),
    ("loop engineering", "AgentLoop"),
    ("multi-agent", "MultiAgent"),
    ("subagent", "MultiAgent"),
    ("agent skill", "CursorSkill"),
    ("harness engineering", "SearchHarness"),
    ("agent memory", "ExperienceStore"),
    ("graph engineering", "GraphTraversal"),
    ("langchain", "AgentLoop"),
    ("langgraph", "AgentLoop"),
    ("fine-tun", "FineTuning"),
    ("lora", "FineTuning"),
    ("qlora", "FineTuning"),
    ("rlhf", "FineTuning"),
    ("quantiz", "Quantization"),
    ("rag", "RAG"),
    ("vector", "VectorDatabase"),
    ("embedd", "VectorDatabase"),
    ("prompt", "PromptEngineering"),
    ("transformer", "Transformer"),
    ("self-attention", "Transformer"),
    ("multi-head", "Transformer"),
    ("flash attention", "Transformer"),
    ("rope", "Transformer"),
    ("llmops", "LLMOps"),
    ("evaluat", "Evaluation"),
    ("guardrail", "AISafety"),
    ("jailbreak", "AISafety"),
    ("prompt injection", "AISafety"),
    ("multimodal", "Multimodal"),
    ("mcp", "MCP"),
    ("agent", "Agent"),
    ("llm", "LargeLanguageModel"),
]

NORTH_FIRST = [
    "AgentCore",
    "AgentLoop",
    "MCP",
    "AgentToolkit",
    "LambdaMicroVM",
    "KVCache",
    "Agent",
    "RAG",
    "Transformer",
    "PromptEngineering",
    "LargeLanguageModel",
]


def today() -> str:
    return datetime.now(TZ).strftime("%Y-%m-%d")


def cell(text: str) -> str:
    return " ".join(text.replace(",", ";").split())


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:48] or "q"


def map_vertex(topic: str, title: str) -> str:
    hay = title.lower()
    for needle, vid in HINTS:
        if needle in hay:
            return vid
    token = title.strip().lower()
    token_map = {
        "llm": "LargeLanguageModel",
        "rag": "RAG",
        "mcp": "MCP",
        "agent": "Agent",
        "fine-tuning": "FineTuning",
        "quantization": "Quantization",
    }
    if token in token_map:
        return token_map[token]
    return TOPIC_VERTEX.get(topic, "LargeLanguageModel")


def fetch_readme() -> str:
    req = urllib.request.Request(RAW, headers={"User-Agent": "mindcraft-zttts-interview-anchor"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse_questions(md: str) -> list[dict]:
    lines = md.splitlines()
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "### Must Know":
            start = i
            break
    topic = ""
    out: list[dict] = []
    pending: dict | None = None
    for line in lines[start:]:
        if line.startswith("## ") and not line.startswith("###"):
            break
        hm = re.match(r"^### (.+)$", line)
        if hm:
            if pending:
                out.append(pending)
                pending = None
            topic = hm.group(1).strip()
            continue
        am = re.search(r"Answer:.*\((https?://[^)]+)\)", line)
        if am and pending:
            pending["url"] = am.group(1)
            continue
        qm = re.match(r"^- (.+)$", line)
        if not qm or not topic:
            continue
        title = qm.group(1).strip()
        if title.lower().startswith("learn about"):
            continue
        if pending:
            out.append(pending)
        pending = {
            "topic": topic,
            "title": title,
            "url": REPO,
            "vertex": map_vertex(topic, title),
        }
    if pending:
        out.append(pending)
    for i, row in enumerate(out, start=1):
        row["id"] = f"q-{i:03d}-{slug(row['title'])}"
    return out


def write_bank(rows: list[dict]) -> None:
    BANK.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "schema: interview/bank",
        f"source: {REPO}",
        "note: titles and first SOURCE url only. Do not copy answers into this repo.",
        f"updated: {datetime.now(TZ).isoformat(timespec='minutes')}",
        f"n: {len(rows)}",
        "nodes[]{id,topic,vertex,title,url}:",
    ]
    for r in rows:
        lines.append(
            f"  {r['id']},{cell(r['topic'])},{r['vertex']},{cell(r['title'])},{r['url']}"
        )
    BANK.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_bank() -> list[dict]:
    if not BANK.exists():
        return []
    rows: list[dict] = []
    for line in BANK.read_text(encoding="utf-8").splitlines():
        if not line.startswith("  "):
            continue
        parts = line.strip().split(",", 4)
        if len(parts) < 5:
            continue
        rows.append(
            {
                "id": parts[0],
                "topic": parts[1],
                "vertex": parts[2],
                "title": parts[3],
                "url": parts[4],
            }
        )
    return rows


def load_done() -> set[str]:
    if not DONE.exists():
        return set()
    ids: set[str] = set()
    for line in DONE.read_text(encoding="utf-8").splitlines():
        if line.startswith("  "):
            ids.add(line.strip().split(",", 1)[0])
    return ids


def append_done(qid: str, date: str, vertex: str) -> None:
    if not DONE.exists():
        DONE.write_text(
            "schema: learner/interview\n"
            f"source: {REPO}\n"
            "note: finished titles. Particulars of practice. Not a Person vertex.\n"
            "nodes[]{id,date,vertex}:\n",
            encoding="utf-8",
        )
    text = DONE.read_text(encoding="utf-8")
    if f"  {qid}," in text:
        return
    if not text.endswith("\n"):
        text += "\n"
    DONE.write_text(text + f"  {qid},{date},{vertex}\n", encoding="utf-8")


def endurance_budget() -> int:
    if not ENDURANCE.exists():
        return 3
    text = ENDURANCE.read_text(encoding="utf-8")
    m = re.search(r"^budget\.now:\s*(\d+)", text, re.M)
    if m:
        return max(1, min(5, int(m.group(1))))
    return 3


def parse_activities(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    cur: dict[str, str] = {}
    for line in text.splitlines():
        if line.strip() == "activity:":
            if cur.get("id"):
                rows.append(cur)
            cur = {}
            continue
        m = re.match(r"^\s{2}([a-z]+):\s*(.*)$", line)
        if m and cur is not None:
            key = m.group(1)
            if key in {"id", "label", "vertex", "recur", "units", "note"}:
                cur[key] = m.group(2).strip()
        if line.startswith("session[") or line.startswith("log["):
            if cur.get("id"):
                rows.append(cur)
            cur = {}
    if cur.get("id"):
        rows.append(cur)
    return rows


def planned_external() -> int:
    if not ENDURANCE.exists():
        return 0
    total = 0
    for act in parse_activities(ENDURANCE.read_text(encoding="utf-8")):
        if act.get("recur") == "daily":
            try:
                total += max(0, int(act.get("units") or "1"))
            except ValueError:
                total += 1
    return total


def remaining_load() -> int:
    return max(1, endurance_budget() - planned_external())


def today_external(date: str) -> int:
    if not ENDURANCE.exists():
        return 0
    total = 0
    in_sess = False
    for line in ENDURANCE.read_text(encoding="utf-8").splitlines():
        if line.startswith("session["):
            in_sess = True
            continue
        if in_sess:
            if not line.startswith("  ") or line.startswith("log["):
                break
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) >= 3 and parts[0] == date:
                try:
                    total += int(parts[2])
                except ValueError:
                    total += 1
    return total


def append_session(date: str, aid: str, units: int, note: str) -> None:
    text = ENDURANCE.read_text(encoding="utf-8")
    marker = "session[]{date,id,units,note}:"
    if marker not in text:
        raise SystemExit("endurance store missing session[] header")
    if not text.endswith("\n"):
        text += "\n"
    line = f"  {date},{aid},{units},{cell(note) or 'done'}\n"
    if f"  {date},{aid}," in text:
        return
    text = text.replace(marker + "\n", marker + "\n" + line, 1)
    ENDURANCE.write_text(text, encoding="utf-8")


def set_endurance_budget(n: int) -> None:
    n = max(1, min(5, n))
    text = ENDURANCE.read_text(encoding="utf-8")
    text = re.sub(r"^budget\.now:\s*\d+", f"budget.now: {n}", text, count=1, flags=re.M)
    ENDURANCE.write_text(text, encoding="utf-8")


def append_endurance(date: str, done_n: int, budget: int, sore: str) -> None:
    text = ENDURANCE.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    ext = today_external(date)
    note = cell(sore) if sore else "clean"
    ENDURANCE.write_text(
        text + f"  {date},{done_n},{budget},{cell(sore) if sore else 'none'},{ext},{note}\n",
        encoding="utf-8",
    )


def body_path(vid: str, folder: str) -> Path:
    return ROOT / "pedagogy" / folder / (vid + ".fu.md")


def write_body(vid: str, kind: str, gloss: str, folder: str) -> None:
    path = body_path(vid, folder)
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    extra = ""
    if vid == "IntellectualLoad":
        extra = (
            "- CLAIM Human 2026-09-02 reports post-study head/brain sore and names it DSB. "
            "Nature 2024: activity can induce transient DNA breaks in CA1 enhancers that repair within minutes. "
            "Persistent extranuclear genomic fragments are a different class. "
            "Do not write this calendar's study as CFC. Do not write sore as GenomicInstability. "
            "Stop on SORE. Log self/endurance.toon.md.\n"
            f"- SOURCE {NATURE}\n"
        )
    else:
        extra = (
            f"- CLAIM Interview titles from {REPO} that map here are the hire-pressure form of this techne. "
            "Answers stay at their SOURCE urls. Do not paste cheat-sheet answers into this body.\n"
        )
    path.write_text(
        f"- VERTEX {vid}\n"
        f"- KIND {kind}\n"
        f"- GLOSS {gloss}\n"
        "- STORE PATH pedagogy/universe.graph.md\n"
        f"{extra}"
        f"- SOURCE {REPO}\n",
        encoding="utf-8",
    )


def upsert_graph() -> None:
    text = GRAPH.read_text(encoding="utf-8")
    existing_v = set(re.findall(r"^V (\S+)", text, re.M))
    existing_e = set(
        re.findall(r"^E (\S+)\s+(\S+)\s+(\S+)", text, re.M)
    )
    v_lines = []
    for vid, kind, gloss, folder in NEW_VERTICES:
        write_body(vid, kind, gloss, folder)
        rel = body_path(vid, folder).relative_to(ROOT).as_posix()
        if vid not in existing_v:
            v_lines.append(f"V {vid} kind={kind} gloss={gloss} body={rel}")
    e_lines = []
    for frm, lab, to, src in NEW_EDGES:
        if (frm, lab, to) not in existing_e:
            e_lines.append(f"E {frm} {lab} {to} SOURCE={src}")
    if not v_lines and not e_lines:
        return
    m = re.search(r"^E ", text, re.M)
    insert_at = m.start() if m else len(text)
    block = ""
    if v_lines:
        block += "\n".join(v_lines) + "\n"
    if e_lines:
        block += "\n".join(e_lines) + "\n"
    GRAPH.write_text(text[:insert_at] + block + text[insert_at:], encoding="utf-8")


def patch_index() -> None:
    comp = ROOT / "pedagogy" / "computation" / "computation.fu.md"
    if comp.exists():
        t = comp.read_text(encoding="utf-8")
        add = " Transformer RAG FineTuning Quantization VectorDatabase LLMOps AISafety Multimodal"
        if "Transformer" not in t:
            t = t.replace(
                "AgentToolkit LambdaMicroVM",
                "AgentToolkit LambdaMicroVM" + add,
            )
            comp.write_text(t, encoding="utf-8")
    bio = ROOT / "pedagogy" / "biology" / "biology.fu.md"
    if bio.exists():
        t = bio.read_text(encoding="utf-8")
        if "IntellectualLoad" not in t:
            t = t.replace("ResistanceTraining", "ResistanceTraining IntellectualLoad")
            bio.write_text(t, encoding="utf-8")
    lang = ROOT / "pedagogy" / "language" / "language.fu.md"
    if lang.exists():
        t = lang.read_text(encoding="utf-8")
        if "PromptEngineering" not in t and "- VERTEX " in t:
            t = t.replace("FuLanguage", "FuLanguage PromptEngineering", 1)
            lang.write_text(t, encoding="utf-8")
    mathf = ROOT / "pedagogy" / "math" / "math.fu.md"
    if mathf.exists():
        t = mathf.read_text(encoding="utf-8")
        if "Evaluation" not in t and "- VERTEX " in t:
            t = t.replace("TypeSystem", "TypeSystem Evaluation", 1)
            mathf.write_text(t, encoding="utf-8")


def read_open_probe() -> dict | None:
    text = CPU.read_text(encoding="utf-8") if CPU.exists() else ""
    m = re.search(
        r"^-\s+STUDY\s+\$id=(\S+)(.*?)(?=^-\s+(STUDY|PLAN|DAY|REVIEW|ASK|AGENT|EXECUTED|KIND)|\Z)",
        text,
        re.M | re.S,
    )
    # prefer PLAN NOW
    pm = re.search(r"^-\s+PLAN\s+\$id=ai-agent-engineer\n(?:  .*\n)*?  - NOW (\S+)", text, re.M)
    now = pm.group(1) if pm else None
    block = None
    vid = now
    if vid:
        bm = re.search(
            rf"^-\s+STUDY\s+\$id={re.escape(vid)}\n((?:  .*\n)*)",
            text,
            re.M,
        )
        if bm:
            block = bm.group(0)
    if not block:
        return None
    probe_m = re.search(r"  - PROBE\n    - (.+)", block)
    ans_m = re.search(r"  - ANSWER\n(    - .+)?", block)
    answer = ""
    if ans_m and ans_m.group(1):
        answer = ans_m.group(1).strip()
    # empty ANSWER line with no nested text
    if re.search(r"  - ANSWER\n  - ASSESS", block):
        answer = ""
    if answer:
        return None
    probe = probe_m.group(1).strip() if probe_m else f"What is {vid} in your own words?"
    return {"id": f"probe-{vid}", "vertex": vid, "title": probe, "kind": "PROBE", "url": ""}


def pick_questions(rows: list[dict], budget: int, skip: set[str]) -> list[dict]:
    picked: list[dict] = []
    probe = read_open_probe()
    if probe and probe["id"] not in skip:
        picked.append(probe)
    by_v: dict[str, list[dict]] = {}
    for r in rows:
        if r["id"] in skip:
            continue
        if "?" not in r["title"] and len(r["title"]) < 28:
            continue
        by_v.setdefault(r["vertex"], []).append(r)
    for vid in NORTH_FIRST:
        if len(picked) >= budget:
            break
        pool = by_v.get(vid) or []
        if not pool:
            continue
        # skip if probe already covers this vertex
        if any(p.get("vertex") == vid and p.get("kind") == "PROBE" for p in picked):
            continue
        picked.append({**pool[0], "kind": "QUESTION"})
    if len(picked) < budget:
        for r in rows:
            if r["id"] in skip or any(p["id"] == r["id"] for p in picked):
                continue
            if r["vertex"] == "Study":
                continue
            if "?" not in r["title"] and len(r["title"]) < 28:
                continue
            picked.append({**r, "kind": "QUESTION"})
            if len(picked) >= budget:
                break
    return picked[:budget]


def format_day(date: str, budget: str, items: list[dict], done_ids: set[str], sore: str) -> str:
    lines = [
        f"- DAY $date={date}",
        f"  - LOAD {budget}",
        "  - TZ Europe/Berlin",
        "  - WHY job seeking as AI agent engineer. Titles from the Amit Shekhar bank mapped onto this graph. Stop on SORE. External Wordschatz counts toward Ausdauer.",
    ]
    for it in items:
        mark = " DONE" if it["id"] in done_ids else ""
        kind = it.get("kind") or "QUESTION"
        url = f" SOURCE {it['url']}" if it.get("url") else ""
        lines.append(
            f"  - DO $id={it['id']} $vertex={it['vertex']} {kind} {it['title']}{url}{mark}"
        )
    lines.append("  - DONE " + (" ".join(sorted(done_ids)) if done_ids else ""))
    lines.append(f"  - SORE {sore}".rstrip())
    lines.append("  - STOP if SORE is not empty. python cron/interview-anchor.py --sore --text. Do not add more DO.")
    return "\n".join(lines)


def parse_day(text: str, date: str) -> dict:
    m = re.search(
        rf"^-\s+DAY \$date={re.escape(date)}\n((?:  .*\n)*)",
        text,
        re.M,
    )
    if not m:
        return {"items": [], "done": set(), "sore": "", "budget": endurance_budget()}
    block = m.group(0)
    done: set[str] = set()
    dm = re.search(r"  - DONE(?: (.+))?", block)
    if dm and dm.group(1):
        done.update(dm.group(1).split())
    items = []
    for line in block.splitlines():
        im = re.match(
            r"  - DO \$id=(\S+) \$vertex=(\S+) (PROBE|QUESTION) (.+?)(?: SOURCE (\S+))?( DONE)?$",
            line,
        )
        if im:
            qid = im.group(1)
            if " DONE" in line or qid in done:
                done.add(qid)
            items.append(
                {
                    "id": qid,
                    "vertex": im.group(2),
                    "kind": im.group(3),
                    "title": im.group(4).replace(" DONE", "").strip(),
                    "url": im.group(5) or "",
                }
            )
    sm = re.search(r"  - SORE(?: (.+))?$", block, re.M)
    sore = (sm.group(1) or "").strip() if sm else ""
    bm = re.search(r"  - LOAD (\d+)", block)
    budget = int(bm.group(1)) if bm else endurance_budget()
    return {"items": items, "done": done, "sore": sore, "budget": budget}


def write_day_block(date: str, block: str) -> None:
    text = CPU.read_text(encoding="utf-8")
    new = re.sub(
        rf"^-\s+DAY \$date={re.escape(date)}\n(?:  .*\n)*",
        block + "\n",
        text,
        count=1,
        flags=re.M,
    )
    if new == text:
        # insert after PROTOCOL block
        m = re.search(r"^- PROTOCOL\n(?:  .*\n)+", text, re.M)
        if m:
            text = text[: m.end()] + "\n" + block + "\n" + text[m.end() :]
        else:
            text = block + "\n" + text
        CPU.write_text(text, encoding="utf-8")
        return
    CPU.write_text(new, encoding="utf-8")


def cmd_fetch() -> list[dict]:
    rows = parse_questions(fetch_readme())
    write_bank(rows)
    print(json.dumps({"n": len(rows), "path": BANK.as_posix()}, indent=2))
    return rows


def cmd_anchor() -> None:
    upsert_graph()
    patch_index()
    print(json.dumps({"graph": GRAPH.as_posix(), "vertices": [v[0] for v in NEW_VERTICES]}, indent=2))


def cmd_day(date: str) -> list[dict]:
    rows = load_bank()
    if not rows:
        rows = cmd_fetch()
    existing = parse_day(CPU.read_text(encoding="utf-8") if CPU.exists() else "", date)
    skip = load_done() | existing["done"]
    if existing["sore"]:
        print_plan(date, existing["items"], existing["done"], existing["sore"], existing["budget"])
        return existing["items"]
    if existing["items"]:
        items = existing["items"]
        budget = existing["budget"]
    else:
        budget = remaining_load()
        items = pick_questions(rows, budget, skip)
    block = format_day(date, str(budget), items, existing["done"], existing["sore"])
    write_day_block(date, block)
    print_plan(date, items, existing["done"], existing["sore"], budget)
    return items


def print_plan(date: str, items: list[dict], done: set[str], sore: str, budget: int) -> None:
    print(f"DAY {date} LOAD {budget}" + (f" SORE {sore}" if sore else ""))
    open_i = next((i for i, it in enumerate(items) if it["id"] not in done), None)
    for i, it in enumerate(items, start=1):
        state = "DONE" if it["id"] in done else ("NOW" if open_i is not None and items[open_i]["id"] == it["id"] else "TODO")
        print(f"  {i}. [{state}] {it['kind']} {it['vertex']}: {it['title']}")
        if it.get("url"):
            print(f"      {it['url']}")
    if sore:
        print("STOP. No more DO today.")
    else:
        print("Say finished with the NOW id, or say sore and stop.")
        print(f"EXTERNAL planned={planned_external()} logged_today={today_external(date)} remaining_if_fresh_day={remaining_load()}")


def cmd_print(date: str) -> None:
    d = parse_day(CPU.read_text(encoding="utf-8"), date)
    if not d["items"]:
        cmd_day(date)
        return
    print_plan(date, d["items"], d["done"], d["sore"], d["budget"])


def cmd_done(qid: str, date: str) -> None:
    text = CPU.read_text(encoding="utf-8")
    d = parse_day(text, date)
    hit = next((it for it in d["items"] if it["id"] == qid), None)
    if not hit:
        raise SystemExit(f"no DO {qid} on {date}")
    d["done"].add(qid)
    append_done(qid, date, hit["vertex"])
    block = format_day(date, str(d["budget"]), d["items"], d["done"], d["sore"])
    write_day_block(date, block)
    n_done = len(d["done"])
    if n_done >= d["budget"] and not d["sore"]:
        append_endurance(date, n_done, d["budget"], "")
        set_endurance_budget(d["budget"] + 1)
    print_plan(date, d["items"], d["done"], d["sore"], d["budget"])


def cmd_sore(note: str, date: str) -> None:
    d = parse_day(CPU.read_text(encoding="utf-8"), date)
    if not d["items"]:
        raise SystemExit(f"no DAY {date}")
    d["sore"] = cell(note) or "sore"
    n_done = len(d["done"])
    append_endurance(date, n_done, d["budget"], d["sore"])
    set_endurance_budget(d["budget"] - 1)
    block = format_day(date, str(d["budget"]), d["items"], d["done"], d["sore"])
    write_day_block(date, block)
    print_plan(date, d["items"], d["done"], d["sore"], d["budget"])


def cmd_external(aid: str, date: str, note: str, sore: str) -> None:
    if not ENDURANCE.exists():
        raise SystemExit("missing self/endurance.toon.md")
    acts = parse_activities(ENDURANCE.read_text(encoding="utf-8"))
    hit = next((a for a in acts if a.get("id") == aid), None)
    if not hit:
        known = " ".join(a.get("id", "") for a in acts)
        raise SystemExit(f"no activity {aid}. known: {known}")
    try:
        units = max(1, int(hit.get("units") or "1"))
    except ValueError:
        units = 1
    append_session(date, aid, units, note or hit.get("label") or aid)
    if sore:
        append_endurance(date, 0, endurance_budget(), sore)
        set_endurance_budget(endurance_budget() - 1)
    print(
        json.dumps(
            {
                "date": date,
                "id": aid,
                "vertex": hit.get("vertex", "Wordschatz"),
                "units": units,
                "today_external": today_external(date),
                "planned": planned_external(),
                "budget": endurance_budget(),
                "remaining_if_fresh_day": remaining_load(),
                "sore": sore,
            },
            indent=2,
        )
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--fetch", action="store_true")
    p.add_argument("--anchor", action="store_true")
    p.add_argument("--day", action="store_true")
    p.add_argument("--done", action="store_true")
    p.add_argument("--sore", action="store_true")
    p.add_argument("--print", action="store_true")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--external", action="store_true")
    p.add_argument("--date", default="")
    p.add_argument("--id", default="")
    p.add_argument("--text", default="")
    args = p.parse_args()
    n = sum(bool(x) for x in [args.fetch, args.anchor, args.day, args.done, args.sore, args.print, args.apply, args.external])
    if n != 1:
        raise SystemExit("choose exactly one of --fetch --anchor --day --done --sore --print --apply --external")
    date = args.date or today()
    if args.fetch:
        cmd_fetch()
        return
    if args.anchor:
        if not BANK.exists():
            cmd_fetch()
        cmd_anchor()
        return
    if args.day:
        if not BANK.exists():
            cmd_fetch()
        cmd_anchor()
        cmd_day(date)
        return
    if args.print:
        cmd_print(date)
        return
    if args.done:
        if not args.id:
            raise SystemExit("--done needs --id")
        cmd_done(args.id, date)
        return
    if args.sore:
        if not args.text:
            raise SystemExit("--sore needs --text")
        cmd_sore(args.text, date)
        return
    if args.external:
        if not args.id:
            raise SystemExit("--external needs --id")
        cmd_external(args.id, date, args.text, "")
        return
    cmd_fetch()
    cmd_anchor()
    cmd_day(date)


if __name__ == "__main__":
    main()
