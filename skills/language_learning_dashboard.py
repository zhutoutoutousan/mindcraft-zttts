#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
POLYGLOT = ROOT / "pedagogy" / "_learn" / "polyglot"
WRITING = ROOT / "pedagogy" / "_learn" / "writing-accuracy"
BASELINE = ROOT / "pedagogy" / "_learn" / "baseline-answers.toon.md"
OUT = ROOT / "tmp" / "public-language-dashboard" / "index.html"

BAND_LABELS = {
    "native_or_bilingual": "bilingual / muttersprachlich",
    "professional_working": "beruflich",
    "limited_working": "ausbaufähig",
    "elementary": "Grundlagen",
}

BLOCKED = (".private", "d:/mindcraft", "c:/users", "pedagogy/_learn", "tmp/", "project-state", "/api/")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def ensure_safe_text(value: str) -> str:
    text = " ".join(value.strip().split())
    lowered = text.lower().replace("\\", "/")
    if not text or any(marker in lowered for marker in BLOCKED):
        raise ValueError("Unsafe public dashboard value")
    return text


def safe_url(value: str) -> str | None:
    url = value.strip()
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return None
    if any(marker in url.lower() for marker in BLOCKED):
        return None
    return url


def parse_horizon() -> dict:
    text = read(POLYGLOT / "horizon.toon.md")
    languages = []
    for line in text.splitlines():
        match = re.match(r"^\s{2}([a-z]+),([^,]+),([a-z_]+),([A-Za-z]+)$", line)
        if match:
            code, name, band, script = match.groups()
            if band not in BAND_LABELS:
                continue
            languages.append(
                {
                    "code": code,
                    "name": ensure_safe_text(name),
                    "band": band,
                    "bandLabel": BAND_LABELS[band],
                    "script": script,
                }
            )
    wanted = re.search(r"^want:\s*(.+)$", text, re.MULTILINE)
    target_age = re.search(r"^age_target:\s*(\d+)$", text, re.MULTILINE)
    deadline = re.search(r"^deadline_year:\s*(\d+)$", text, re.MULTILINE)
    if len(languages) != 16 or not wanted or not target_age or not deadline:
        raise ValueError("Invalid horizon source")
    return {
        "goal": ensure_safe_text(wanted.group(1)),
        "targetAge": int(target_age.group(1)),
        "deadlineYear": int(deadline.group(1)),
        "languages": languages,
    }


def parse_facets() -> list[dict]:
    text = read(POLYGLOT / "skills.toon.md")
    facets = []
    for line in text.splitlines():
        match = re.match(r"^\s{2}([a-z]+),([a-z_]+),([^,]+),(.+)$", line)
        if match:
            facet_id, kind, german, english = match.groups()
            facets.append(
                {
                    "id": facet_id,
                    "kind": kind,
                    "label": ensure_safe_text(german),
                    "english": ensure_safe_text(english),
                }
            )
    if len(facets) != 6:
        raise ValueError("Invalid facet source")
    return facets


def parse_commerce() -> dict:
    text = read(POLYGLOT / "commerce.toon.md")
    priority = re.search(r"^named_priority\[\d+\]:\s*(.+)$", text, re.MULTILINE)
    next_lang = re.search(r"^\s*next_lang:\s*(\w+)$", text, re.MULTILINE)
    next_facet = re.search(r"^\s*next_facet:\s*(\w+)$", text, re.MULTILINE)
    if not priority or not next_lang or not next_facet:
        raise ValueError("Invalid harvest allocation")
    return {
        "priority": [item.strip() for item in priority.group(1).split(",")],
        "nextLanguage": next_lang.group(1),
        "nextFacet": next_facet.group(1),
    }


def parse_harvest() -> dict:
    text = read(POLYGLOT / "harvest.toon.md")
    total_match = re.search(r"^rows\[(\d+)\]\{id,lang,facet,title,url,when\}:$", text, re.MULTILINE)
    updated_match = re.search(r"^updated:\s*(.+)$", text, re.MULTILINE)
    if not total_match or not updated_match:
        raise ValueError("Invalid harvest source")
    rows = []
    pattern = re.compile(
        r"^\s*[^,]+,([a-z]+),([a-z]+),(.*),(https?://[^,]+),(\d{4}-\d{2}-\d{2})$"
    )
    for line in text.splitlines():
        match = pattern.match(line)
        if not match:
            continue
        lang, facet, title, url, when = match.groups()
        safe_link = safe_url(url)
        if not safe_link:
            continue
        try:
            rows.append(
                {
                    "lang": lang,
                    "facet": facet,
                    "title": ensure_safe_text(title),
                    "url": safe_link,
                    "when": when,
                }
            )
        except ValueError:
            continue
    total = int(total_match.group(1))
    if len(rows) != total:
        raise ValueError("Harvest rows are incomplete or unsafe")
    return {"total": total, "updated": ensure_safe_text(updated_match.group(1)), "rows": rows}


def parse_public_german() -> dict:
    text = read(WRITING / "state.toon.md")
    section = text.split("publicDashboard:\n", maxsplit=1)
    if len(section) != 2:
        raise ValueError("Missing public German dashboard projection")
    public = section[1]

    def scalar(key: str) -> str:
        match = re.search(rf"^\s{{2}}{key}:\s*(.+)$", public, re.MULTILINE)
        if not match:
            raise ValueError(f"Missing {key}")
        return ensure_safe_text(match.group(1))

    def labels(key: str) -> list[str]:
        match = re.search(rf"^\s{{2}}{key}\[\d+\]:\n((?:\s{{4}}.+\n?)+)", public, re.MULTILINE)
        if not match:
            raise ValueError(f"Missing {key}")
        return [ensure_safe_text(line.strip()) for line in match.group(1).splitlines()]

    active_errors = re.findall(r"^\s{2}[a-z_]+,priority=\d+,streakClear=\d+$", text, re.MULTILINE)
    frame_count = len(re.findall(r"^frame:$", read(POLYGLOT / "frames" / "de.toon.md"), re.MULTILINE))
    session_counts = Counter()
    for path in (WRITING / "sessions").glob("????-??-??-*.toon.md"):
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.name)
        if match:
            session_counts[match.group(1)] += 1
    sessions = [
        {"date": date, "count": count}
        for date, count in sorted(session_counts.items(), reverse=True)[:14]
    ]
    return {
        "language": scalar("activeLanguage"),
        "focus": scalar("activeFocus"),
        "errorLabels": labels("activeErrorLabels"),
        "formGroups": labels("formGroups"),
        "nextAction": scalar("nextAction"),
        "activeErrorCount": len(active_errors),
        "frameCount": frame_count,
        "sessions": sessions,
    }


def parse_baseline() -> dict:
    text = read(BASELINE)
    langs_match = re.search(r"^langs:\s*(.+)$", text, re.MULTILINE)
    if not langs_match:
        raise ValueError("Invalid baseline source")
    langs = langs_match.group(1).split()
    prompt_count = len(re.findall(r"^node:$", text, re.MULTILINE))
    completed = {lang: 0 for lang in langs}
    for lang in langs:
        for match in re.finditer(rf"^\s*answer\.{re.escape(lang)}:\s*(.*)$", text, re.MULTILINE):
            if match.group(1).strip():
                completed[lang] += 1
    return {"languages": langs, "promptCount": prompt_count, "completed": completed}


def parse_drills() -> dict:
    text = read(WRITING / "drill-progress.toon.md")
    rows = [line for line in text.splitlines() if re.match(r"^\s{2}[^,]+,(True|False|),", line)]
    completed = sum(",True," in line for line in rows)
    return {"total": len(rows), "completed": completed}


def build_payload() -> dict:
    horizon = parse_horizon()
    facets = parse_facets()
    commerce = parse_commerce()
    harvest = parse_harvest()
    language_names = {item["code"]: item["name"] for item in horizon["languages"]}
    facet_names = {item["id"]: item["label"] for item in facets}
    band_counts = Counter(item["band"] for item in horizon["languages"])
    harvest_counts = Counter(row["lang"] for row in harvest["rows"])
    facet_counts = Counter(row["facet"] for row in harvest["rows"])
    payload = {
        "schema": "language-learning-dashboard/v1",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "horizon": horizon,
        "facets": facets,
        "bandCounts": dict(band_counts),
        "german": parse_public_german(),
        "baseline": parse_baseline(),
        "drills": parse_drills(),
        "harvest": {
            "total": harvest["total"],
            "updated": harvest["updated"],
            "rows": harvest["rows"],
            "languageCounts": dict(harvest_counts),
            "facetCounts": dict(facet_counts),
        },
        "allocation": commerce,
        "languageNames": language_names,
        "facetNames": facet_names,
    }
    serialized = json.dumps(payload, ensure_ascii=False).lower().replace("\\", "/")
    if any(marker in serialized for marker in BLOCKED):
        raise ValueError("Public payload failed safety check")
    if len(payload["horizon"]["languages"]) != 16 or len(payload["facets"]) != 6:
        raise ValueError("Dashboard invariant failed")
    return payload


def render_html(payload: dict) -> str:
    data = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<title>Sprachlernstand</title>
<style>
:root {{ --bg:#07111f; --panel:#101e32; --line:#29445f; --text:#edf6ff; --muted:#9eb4ca; --accent:#52c7ff; --accent2:#7ff0c2; --warn:#ffca75; --danger:#ff9f9f; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; min-width:320px; background:radial-gradient(circle at top right,#163357,#07111f 48%); color:var(--text); font:16px/1.5 Inter,Segoe UI,Arial,sans-serif; }}
a {{ color:var(--accent); }}
.shell {{ width:min(1180px,calc(100% - 32px)); margin:0 auto; padding:32px 0 64px; }}
.eyebrow,.section-label {{ color:var(--accent); font-size:.76rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; }}
h1 {{ margin:.3rem 0; font-size:clamp(2rem,7vw,4.5rem); line-height:1.04; }}
h2 {{ margin:0 0 1rem; font-size:clamp(1.35rem,3vw,2rem); }}
h3 {{ margin:.1rem 0 .4rem; font-size:1.05rem; }}
.subtle,.stamp {{ color:var(--muted); }}
nav {{ display:flex; flex-wrap:wrap; gap:8px; margin:28px 0 20px; }}
button,select,input {{ font:inherit; }}
.tab, .filter {{ border:1px solid var(--line); background:var(--panel); color:var(--text); border-radius:999px; padding:9px 14px; cursor:pointer; }}
.tab[aria-selected="true"],.tab:hover,.filter:hover {{ border-color:var(--accent); background:#173454; }}
.tab:focus-visible,.filter:focus-visible,a:focus-visible {{ outline:3px solid var(--accent2); outline-offset:3px; }}
.view {{ display:none; }} .view.active {{ display:block; }}
.grid {{ display:grid; grid-template-columns:repeat(12,minmax(0,1fr)); gap:14px; }}
.card {{ grid-column:span 3; background:color-mix(in srgb,var(--panel) 92%,transparent); border:1px solid var(--line); border-radius:18px; padding:18px; min-width:0; }}
.card.wide {{ grid-column:span 6; }} .card.full {{ grid-column:1/-1; }}
.metric {{ margin:.35rem 0; font-size:2rem; font-weight:800; }}
.pill-row {{ display:flex; flex-wrap:wrap; gap:7px; }}
.pill {{ display:inline-flex; align-items:center; gap:6px; border:1px solid var(--line); border-radius:999px; padding:4px 9px; color:#cce0f1; font-size:.85rem; }}
.stack {{ display:grid; gap:10px; }}
.lang-card {{ display:grid; gap:10px; padding:16px; border:1px solid var(--line); border-radius:16px; background:#0b192a; }}
.lang-head {{ display:flex; justify-content:space-between; gap:10px; align-items:baseline; }}
.lang-name {{ font-size:1.15rem; font-weight:800; }}
.band {{ color:var(--accent2); font-size:.84rem; text-align:right; }}
.skill-grid {{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:6px; }}
.skill {{ padding:7px; border-radius:9px; background:#132943; color:#cfe1f4; font-size:.82rem; text-align:center; }}
.controls {{ display:flex; flex-wrap:wrap; gap:10px; margin:0 0 16px; }}
.controls select,.controls input {{ border:1px solid var(--line); border-radius:10px; background:#0b192a; color:var(--text); padding:9px 11px; min-width:150px; }}
.controls input {{ flex:1 1 220px; }}
.resource {{ display:flex; justify-content:space-between; gap:14px; border-top:1px solid var(--line); padding:13px 0; }}
.resource:first-child {{ border-top:0; }}
.resource-title {{ font-weight:700; }} .resource-meta {{ color:var(--muted); font-size:.87rem; }}
.list {{ margin:0; padding-left:1.2rem; }} .list li {{ margin:.35rem 0; }}
.timeline {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(112px,1fr)); gap:9px; }}
.timeline-item {{ border:1px solid var(--line); border-radius:12px; padding:11px; background:#0b192a; }}
.timeline-count {{ color:var(--accent2); font-size:1.45rem; font-weight:800; }}
.notice {{ border-left:4px solid var(--warn); background:#241e17; border-radius:10px; padding:13px; color:#ffe4b5; }}
.empty {{ color:var(--muted); padding:18px 0; }}
@media (max-width:820px) {{ .card,.card.wide {{ grid-column:span 6; }} }}
@media (max-width:520px) {{ .shell {{ width:min(100% - 22px,1180px); padding-top:22px; }} .card,.card.wide {{ grid-column:1/-1; }} .resource {{ display:block; }} .resource a {{ display:inline-block; margin-top:8px; }} .skill-grid {{ grid-template-columns:repeat(2,minmax(0,1fr)); }} }}
</style>
</head>
<body>
<main class="shell">
  <header>
    <div class="eyebrow">Privater Sprachlern-Export · keine Rohsessions</div>
    <h1>Sprachlernstand</h1>
    <p class="subtle">Horizon, Lernstruktur, Deutsch-Praxis, Quellen und Baselines in einer eigenständigen Ansicht.</p>
    <p class="stamp" id="stamp"></p>
  </header>
  <nav aria-label="Sprachlern-Bereiche">
    <button class="tab" data-tab="overview" aria-selected="true">Übersicht</button>
    <button class="tab" data-tab="horizon" aria-selected="false">16 Sprachen</button>
    <button class="tab" data-tab="german" aria-selected="false">Deutsch-Praxis</button>
    <button class="tab" data-tab="harvest" aria-selected="false">Ressourcen</button>
    <button class="tab" data-tab="baseline" aria-selected="false">Baselines</button>
  </nav>
  <section class="view active" id="overview" aria-label="Übersicht"></section>
  <section class="view" id="horizon" aria-label="Sprachhorizont"></section>
  <section class="view" id="german" aria-label="Deutsch-Praxis"></section>
  <section class="view" id="harvest" aria-label="Ressourcenharvest"></section>
  <section class="view" id="baseline" aria-label="Baseline-Status"></section>
</main>
<script>
const DATA = {data};
const bands = Object.keys(DATA.bandCounts);
const bandLabel = id => ({{ native_or_bilingual:'bilingual / muttersprachlich', professional_working:'beruflich', limited_working:'ausbaufähig', elementary:'Grundlagen' }})[id] || id;
const byId = id => document.getElementById(id);
const node = (tag, text, className='') => {{ const el=document.createElement(tag); el.textContent=text; if(className) el.className=className; return el; }};
const pill = text => node('span', text, 'pill');
const card = (label, value, detail, wide=false) => {{ const el=document.createElement('article'); el.className='card'+(wide?' wide':''); el.append(node('div',label,'section-label'),node('div',value,'metric'),node('div',detail,'subtle')); return el; }};

document.getElementById('stamp').textContent = `Stand: ${{DATA.generatedAt}} · ${{DATA.harvest.total}} geprüfte Lernquellen`;

function renderOverview() {{
  const view=byId('overview'); view.replaceChildren();
  const grid=node('div','', 'grid');
  grid.append(
    card('HORIZON', String(DATA.horizon.languages.length), `Sprachen · Zielalter ${{DATA.horizon.targetAge}}`),
    card('DEUTSCH', DATA.german.focus, `${{DATA.german.activeErrorCount}} aktive Fehlertypen`),
    card('DRILLS', `${{DATA.drills.completed}} / ${{DATA.drills.total}}`, 'abgeschlossene Lernitems'),
    card('BASELINES', `${{Object.values(DATA.baseline.completed).reduce((a,b)=>a+b,0)}} / ${{DATA.baseline.promptCount * DATA.baseline.languages.length}}`, 'beantwortete Proben'),
  );
  const allocation=document.createElement('article'); allocation.className='card wide';
  allocation.append(node('div','NÄCHSTER HARVEST','section-label'),node('h3',`${{DATA.languageNames[DATA.allocation.nextLanguage]}} · ${{DATA.facetNames[DATA.allocation.nextFacet]}}`),node('p','Priorität: '+DATA.allocation.priority.map(code=>DATA.languageNames[code]).join(' · '),'subtle'));
  grid.append(allocation);
  const bandsCard=document.createElement('article'); bandsCard.className='card wide'; bandsCard.append(node('div','SELBSTEINSCHÄTZUNG','section-label')); const row=node('div','', 'pill-row'); bands.forEach(id=>row.append(pill(`${{DATA.bandCounts[id]}} × ${{bandLabel(id)}}`))); bandsCard.append(row); grid.append(bandsCard);
  const action=document.createElement('article'); action.className='card full'; action.append(node('div','NÄCHSTER SCHRITT','section-label'),node('h3',DATA.german.nextAction),node('p','Die Fertigkeiten sind Strukturkategorien, keine einzeln vergebenen CEFR-Tests.','subtle')); grid.append(action);
  view.append(grid);
}}

function renderHorizon() {{
  const view=byId('horizon'); view.replaceChildren();
  view.append(node('h2','16 Sprachen und sechs Fertigkeiten'));
  view.append(node('p','Die Bänder sind Selbsteinschätzungen auf Sprachebene. Die sechs Fertigkeiten erhalten keine erfundenen Einzelwerte.','subtle'));
  const controls=node('div','', 'controls'); const select=document.createElement('select'); select.setAttribute('aria-label','Sprachband filtern'); select.append(new Option('Alle Bänder','all')); bands.forEach(id=>select.append(new Option(`${{bandLabel(id)}} (${{DATA.bandCounts[id]}})`,id))); controls.append(select); view.append(controls);
  const list=node('div','', 'grid'); view.append(list);
  function draw() {{ list.replaceChildren(); DATA.horizon.languages.filter(lang=>select.value==='all'||lang.band===select.value).forEach(lang=>{{ const article=document.createElement('article'); article.className='lang-card'; const head=node('div','', 'lang-head'); const name=node('div',`${{lang.name}} (${{lang.code}})`,'lang-name'); const band=node('div',lang.bandLabel,'band'); head.append(name,band); const skills=node('div','', 'skill-grid'); DATA.facets.forEach(facet=>skills.append(node('div',facet.label,'skill'))); article.append(head,node('div',`Schrift: ${{lang.script}}`,'resource-meta'),skills); const holder=document.createElement('div'); holder.className='card wide'; holder.append(article); list.append(holder); }}); }}
  select.addEventListener('change',draw); draw();
}}

function renderGerman() {{
  const view=byId('german'); view.replaceChildren();
  view.append(node('h2','Deutsch-Praxis: Genauigkeit unter echter Arbeit'));
  const grid=node('div','', 'grid');
  const focus=document.createElement('article'); focus.className='card wide'; focus.append(node('div','AKTUELLER FOKUS','section-label'),node('h3',DATA.german.focus),node('p',DATA.german.nextAction,'subtle')); grid.append(focus);
  grid.append(card('FEHLERTYPEN',String(DATA.german.activeErrorCount),'aktiv beobachtete Kategorien'),card('GRAMMATIK-FRAMES',String(DATA.german.frameCount),'attestierte Rahmen'),card('DRILLS',`${{DATA.drills.completed}} / ${{DATA.drills.total}}`,'abgeschlossen'));
  const errors=document.createElement('article'); errors.className='card wide'; errors.append(node('div','AKTIVE KATEGORIEN','section-label')); const errorList=node('ul','', 'list'); DATA.german.errorLabels.forEach(label=>errorList.append(node('li',label))); errors.append(errorList); grid.append(errors);
  const forms=document.createElement('article'); forms.className='card wide'; forms.append(node('div','FORMGRUPPEN','section-label')); const formList=node('ul','', 'list'); DATA.german.formGroups.forEach(label=>formList.append(node('li',label))); forms.append(formList); grid.append(forms);
  const timeline=document.createElement('article'); timeline.className='card full'; timeline.append(node('div','SCHREIBAKTIVITÄT','section-label'),node('p','Gezählt werden nur sichere Tagesaggregate; Rohtexte und Korrekturen bleiben privat.','subtle')); const items=node('div','', 'timeline'); DATA.german.sessions.forEach(item=>{{ const entry=node('div','', 'timeline-item'); entry.append(node('div',item.date,'resource-meta'),node('div',String(item.count),'timeline-count'),node('div','Sessions','resource-meta')); items.append(entry); }}); timeline.append(items); grid.append(timeline);
  view.append(grid);
}}

function renderHarvest() {{
  const view=byId('harvest'); view.replaceChildren();
  view.append(node('h2','Ressourcenharvest'));
  view.append(node('p',`${{DATA.harvest.total}} überprüfte Quellen · letzter Datenstand ${{DATA.harvest.updated}}.`,`subtle`));
  const controls=node('div','', 'controls'); const language=document.createElement('select'); language.setAttribute('aria-label','Sprache filtern'); language.append(new Option('Alle Sprachen','all')); DATA.horizon.languages.forEach(item=>language.append(new Option(`${{item.name}} (${{DATA.harvest.languageCounts[item.code]||0}})`,item.code))); const facet=document.createElement('select'); facet.setAttribute('aria-label','Fertigkeit filtern'); facet.append(new Option('Alle Fertigkeiten','all')); DATA.facets.forEach(item=>facet.append(new Option(`${{item.label}} (${{DATA.harvest.facetCounts[item.id]||0}})`,item.id))); const search=document.createElement('input'); search.type='search'; search.placeholder='Quellen durchsuchen'; search.setAttribute('aria-label','Quellen durchsuchen'); controls.append(language,facet,search); view.append(controls);
  const summary=node('p','', 'subtle'); view.append(summary); const list=node('div','', 'card full'); view.append(list); const more=document.createElement('button'); more.className='filter'; more.textContent='Mehr laden'; view.append(more); let limit=24;
  function draw() {{ const query=search.value.trim().toLocaleLowerCase(); const rows=DATA.harvest.rows.filter(row=>(language.value==='all'||row.lang===language.value)&&(facet.value==='all'||row.facet===facet.value)&&(!query||row.title.toLocaleLowerCase().includes(query))); summary.textContent=`${{rows.length}} Quellen passen zum Filter.`; list.replaceChildren(); rows.slice(0,limit).forEach(row=>{{ const item=node('article','', 'resource'); const left=node('div',''); left.append(node('div',row.title,'resource-title'),node('div',`${{DATA.languageNames[row.lang]||row.lang}} · ${{DATA.facetNames[row.facet]||row.facet}} · ${{row.when}}`,'resource-meta')); const link=document.createElement('a'); link.href=row.url; link.target='_blank'; link.rel='noopener noreferrer'; link.textContent='Quelle öffnen'; item.append(left,link); list.append(item); }}); if(!rows.length) list.append(node('p','Keine Quelle passt zu diesem Filter.','empty')); more.hidden=rows.length<=limit; }}
  [language,facet].forEach(control=>control.addEventListener('change',()=>{{limit=24;draw();}})); search.addEventListener('input',()=>{{limit=24;draw();}}); more.addEventListener('click',()=>{{limit+=24;draw();}}); draw();
}}

function renderBaseline() {{
  const view=byId('baseline'); view.replaceChildren();
  view.append(node('h2','Baseline-Proben'));
  view.append(node('p','Eine leere Probe ist keine Bewertung. Erst eigene Antworten erzeugen einen Score.','notice'));
  const grid=node('div','', 'grid'); DATA.baseline.languages.forEach(code=>{{ const complete=DATA.baseline.completed[code]; const item=card(DATA.languageNames[code]||code.toUpperCase(),`${{complete}} / ${{DATA.baseline.promptCount}}`,complete?'Antworten vorhanden':'Noch keine Antwort'); grid.append(item); }}); const total=Object.values(DATA.baseline.completed).reduce((sum,value)=>sum+value,0); const all=DATA.baseline.promptCount*DATA.baseline.languages.length; const totalCard=document.createElement('article'); totalCard.className='card full'; totalCard.append(node('div','GESAMT','section-label'),node('h3',`${{total}} von ${{all}} Baseline-Antworten`),node('p',total?'Fortschritt basiert auf eigenen Antworten.':'Noch kein Baseline-Score vorhanden.','subtle')); grid.append(totalCard); view.append(grid);
}}

renderOverview(); renderHorizon(); renderGerman(); renderHarvest(); renderBaseline();
document.querySelectorAll('.tab').forEach(button=>button.addEventListener('click',()=>{{ const id=button.dataset.tab; document.querySelectorAll('.tab').forEach(item=>item.setAttribute('aria-selected',String(item===button))); document.querySelectorAll('.view').forEach(view=>view.classList.toggle('active',view.id===id)); }}));
</script>
</body>
</html>"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=OUT)
    args = parser.parse_args()
    payload = build_payload()
    output = render_html(payload)
    if any(marker in output.lower().replace("\\", "/") for marker in BLOCKED):
        raise ValueError("Rendered dashboard failed safety check")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(output, encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(args.out), "resources": payload["harvest"]["total"]}))


if __name__ == "__main__":
    main()
