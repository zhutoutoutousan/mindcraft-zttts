# project-state-viz reference

## Why separate purposes

ROOT already says these are different KINDs:

- **CPU** = life run queue (AGENT/TODO/SCHEDULE)
- **cron** = scheduled gatherers (not the briefing, not ontology)
- **inflow** = news buffer + skip list + drip
- **schedule** = calendar store (harvest/enrich/month), not CPU
- **self** = learner particulars (goals, endurance, training, grasp)
- **pedagogy** = universal ontology + study interface
- **language stores** = polyglot bridge / lexicon / frames / horizon (not universe.graph)
- **mezzanine** = ingest notes before claims
- **skills** = agent libraries
- **tmp** = TTL renders

A single force-graph cannot show a DUMP pending row and a SCHEDULE clash the same way. Purpose modes are the display contract.

## Collectors (live)

Script reads at generate time:

- `ROOT.md` organs
- `self/*.toon.md` / `*.fu.md` (pulse parsers for goals/endurance/learn/training)
- `schedule/harvest.toon.md`, `enrich.toon.md`, `*.fu.md`
- `cron/*.fu.md` + `*.py`
- `inflow/DUMP.md`, `STATE.md`, `inflow.fu.md` NEWS, `inflow/takes.toon.md`
- `CPU.md` AGENT/TODO/SCHEDULE/NOTE
- `pedagogy/pedagogy-cpu.fu.md` PLAN/STUDY
- `pedagogy/universe.graph.md` V/E
- `pedagogy/_learn/polyglot/bridge.graph.md`
- `pedagogy/_learn/polyglot/frames/*.toon.md`
- `pedagogy/_learn/polyglot/horizon.toon.md`
- `pedagogy/_learn/writing-accuracy/lexicon.graph.md` + `state.toon.md`
- `.cursor/skills/*/SKILL.md`, `skills/*`
- `mezzanine/*`, `tmp/ttl.toon.md`, `recycle/` count

## Language labels (must survive a rebuild)

Graph **ids** stay machine-safe (`Form_fix_…`). Canvas **labels** must be human.

Pack path: `parse_graph` / `frames_to_graph` / `skilltree_from_horizon` → `_graph_pack` → `decorate_lang_verts` → `lang_node_label`.

| kind | what the human should read |
|------|----------------------------|
| concept | gloss as a phrase (`location on a device`) |
| lemma / form | surface words (`hätte gern sichergestellt`) |
| frame | pattern (`auf + Dat (device surface)`) |
| gap | `缺口 ·` + surface |
| session | `7.9. intern hook` (date + short name) — hidden by default |
| lang | `de · Deutsch` |

`humanize_lang_text` replaces `_` and `-` with spaces and restores a few German holes (`h tte` → `hätte`). Do not paint `v.id` on language nodes unless surface and gloss are both empty.

Drawer: `langVertexHtml` — 词面 / 意思 / 改自 / 相连. `/api/vertex` is ontology-only.

Default UI for `lang-polyglot` and `lang-wortschatz`: `groupBy=kind`, `clustered=false`, filter out `session` and `focus`.

Edge words on language graphs: Chinese short labels (`表达` `句法` `改`); `FROM_SESSION` is blank so session spokes do not shout.

## Color legend (graph modes only)

- Fill = vertex kind
- Amber border = goals.north
- Red border = PLAN NOW

Language kind chips: 意思 / 词 / 词形 / 句法 / 会话 / 缺口 (see `KIND_READ` in the generator).

## CLI

```
python skills/project-state-viz.py
  [--purpose today|train|routine|project|self|schedule|cron|inflow|runtime|
            study|weights|hire|ontology|core|stack|
            lang-polyglot|lang-wortschatz|lang-grammar|lang-skilltree|
            skills|mezzanine|tmp]
  [--serve] [--host 127.0.0.1] [--no-open] [--out PATH]
```

`--serve` rebuilds HTML on process start. After code edits, restart the process and hard-refresh the browser.
