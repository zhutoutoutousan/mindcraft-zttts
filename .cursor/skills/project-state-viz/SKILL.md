---
name: project-state-viz
description: >-
  Dynamically reads mindcraft project state from ROOT through distinct organs
  (self, schedule, cron, inflow, CPU, pedagogy, language stores, skills,
  mezzanine, tmp) and writes purpose-mode HTML. Use when the human asks for
  project visualization, 项目状态, ROOT map, organ dashboard, knowledge-graph
  HTML, Polyglot KG, 语言知识图, 知识结构, or python skills/project-state-viz.py.
---

# Project state viz

Do **not** reimplement this HTML. The generator is `skills/project-state-viz.py`. Copy that script + this skill when rebuilding in another environment.

## Do this

```bash
python skills/project-state-viz.py
python skills/project-state-viz.py --purpose self
python skills/project-state-viz.py --purpose schedule
python skills/project-state-viz.py --serve
```

Output: `tmp/pedagogy/project-state.html`. Script stamps TTL. Open in Chrome/Edge. `--serve` binds `127.0.0.1:8780`+. Hard-refresh (Ctrl+F5) after a restart.

## Rebuild in a new environment

Bring these files; then run the commands above. HTML under `tmp/` is a render — regenerate it, do not hand-edit.

| must copy | why |
|-----------|-----|
| `skills/project-state-viz.py` | collector + HTML/JS generator |
| `skills/fu_render.py` | ontology drawer `.fu.md` bodies |
| `.cursor/skills/project-state-viz/SKILL.md` | this contract |
| `.cursor/skills/project-state-viz/reference.md` | label + store details |
| `skills/project-state-viz.fu.md` | organ rules |
| `pedagogy/universe.graph.md` + `pedagogy/**/*.fu.md` | ontology graph |
| `pedagogy/_learn/polyglot/` | bridge + frames + horizon |
| `pedagogy/_learn/writing-accuracy/lexicon.graph.md` | Wortschatz |
| `ROOT.md` + `CPU.md` + `self/` + `schedule/` + `inflow/` + `cron/` | other organs |

Language canvas contract (do not regress):

1. Nodes show **human word faces** (词面 / 意思 / 句法 pattern), never `Form_fix_ensure_errors_…` or other underscore IDs.
2. Graph files may store `surface=hätte_gern` or quoted `surface="hätte gern"` (`graph_prop` / quoted kv). **Display** still humanizes leftover `_`/`-` via `lang_node_label` / `decorate_lang_verts`. Never paint the vertex id as the canvas label.
3. Default language view: **Expanded** (not collapsed clusters). Polyglot + Wortschatz hide **会话 / 焦点** stars so the structure (意思↔词↔句法) is visible. Chip 「会话」 turns sessions back on.
4. Drawer title = readable label. Body = 词面 / 意思 / 改自 / 相连. Learner textarea **clears on every node** (no leftover inflow take).
5. Language nodes are **not** ontology `.fu`. Do not fetch `/api/vertex` for them. Do not invent STUDY ANSWER.

```bash
python skills/project-state-viz.py --purpose lang-polyglot --serve --no-open
# http://127.0.0.1:8780/project-state.html
```

## Inflow digest

```bash
python skills/project-state-viz.py --purpose inflow --serve
```

Cards for DUMP pending / HUMAN OPEN / NEWS with WHY. Click opens drawer. Write **Your take** → `inflow/takes.toon.md` (lasting) plus tmp cache. Files tab reads `inflow/*.md` via API. Does not drip. Does not invent ANSWER.

## Ontology node → fu body (learner)

```bash
python skills/project-state-viz.py --purpose ontology --serve
# phone LAN:
python skills/project-state-viz.py --purpose ontology --serve --host 0.0.0.0
```

Click a graph node → drawer renders the vertex `.fu.md` via `skills/fu_render.py` (every CAPITAL TAG; unknown TAG still shown). Learner grasp + note POST to `pedagogy/_learn/learner-notes.toon.md` (tmp cache). Does **not** invent STUDY ANSWER on pedagogy-cpu.

## Today (default)

```bash
python skills/project-state-viz.py
python skills/project-state-viz.py --purpose today
```

Merges CPU NOTE TODAY · **training plan + injury** · harvest covering Berlin date · PLAN NOW / empty PROBE · endurance fog · DUMP · weights. Priority: injury/stop → body/train/calendar → learn/drill → soft north. Does not invent tasks, ANSWER, or a quiet scapula.

## Train / Injury

```bash
python skills/project-state-viz.py --purpose train
```

Reads `self/training.toon.md`: flags/injury, periodization, week plan, sessions + blocks, nextSession, pain/DOMS log, rules. Today view surfaces today's week row + session.

## Weights + mastery (ontology)

```bash
python cron/ontology-weight.py          # refresh pedagogy/_learn/weights.toon.md
python skills/project-state-viz.py --purpose weights
python skills/project-state-viz.py --purpose ontology
```

Dims: `hire` (goals.north) · `plan` (PLAN NOW/NEXT) · `study` (empty ANSWER) · `zeit` (harvest/NEWS keywords) · `maslow` (heuristic layer, not clinical). Each row has `reason` + `mastery` from `self/learn.toon.md`. Maintain organ `ontology-weight` may run this. Graph: **node size ∝ total weight**, border thickness ∝ mastery, click shows reason. Ontology / Hire / Core / Stack: left toolbar **Group by Branch|Kind|Flat**, **Collapsed/Expanded** clusters, filter chips per group. Double-click a cluster ellipse to expand.

## Schedule views

`--purpose schedule` then Table / **Calendar** / **Gantt** toggles on harvest rows (confirmed vs candidate).

## Organs ≠ one view

Each store is a different KIND. Do not flatten them into one graph.

| purpose | store | display |
|---------|-------|---------|
| `project` | ROOT + pulse cards | click into any organ |
| `self` | goals / endurance / training / learn | particulars tables (no .private paste) |
| `schedule` | harvest + enrich + month + CPU SCHEDULE | calendar rows |
| `cron` | cron/*.fu.md + *.py | gatherer jobs (≠ life queue) |
| `inflow` | DUMP + STATE + NEWS | pending / open / skip / news |
| `runtime` | CPU.md | AGENT · TODO · SCHEDULE · NOTE |
| `study` | pedagogy-cpu | empty ANSWER + STUDY subgraph |
| `hire` / `ontology` / `core` / `stack` | universe.graph | filtered knowledge graphs |
| `lang-polyglot` | `_learn/polyglot/bridge.graph.md` | 意思/词/句法 · readable faces |
| `lang-wortschatz` | `_learn/writing-accuracy/lexicon.graph.md` | 词 / 词形 / 搭配 |
| `lang-grammar` | `_learn/polyglot/frames/*.toon.md` | Frame · Slot · filler |
| `lang-skilltree` | `_learn/polyglot/horizon.toon.md` | Horizon → Band → 16 langs |
| `skills` | skills/ + .cursor/skills | library inventory |
| `mezzanine` | mezzanine/ | ingest notes (not claims) |
| `tmp` | tmp/ttl + siblings | deliverable TTL |

Language graphs are **not** `pedagogy/universe.graph.md`. Do not merge them into ontology.

## Hard rules

- Never invent ANSWER
- Never paste `.private/` body into HTML (lebenslauf name-only ok)
- Re-run script to refresh snapshot; sidebar only switches purpose client-side
- Ontology PNG/mp4 remains `skills/ontology-showcase.py`
- Language node labels: `lang_node_label` in the Python generator — do not fall back to vertex id on the canvas

## Related

- [reference.md](reference.md)
- `skills/project-state-viz.fu.md`
