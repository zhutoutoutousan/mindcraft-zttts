---
name: paper-muscle
description: Builds a zero-to-paper academic muscle curriculum into pedagogy vertices plus a LaTeX framework PDF and optional Bilibili-facing MP4. Use when the human asks to 读论文, expand academic muscle, paper ladder, 学术肌肉, theoretical review scaffold, domain knowledge graph from a paper, or AGENT paper-muscle / aesthetic-chills-ladder style study.
---

# Paper muscle (读论文 → 图谱肌肉)

Paradigm: one open-access (or attested) paper becomes a **domain scaffold** in `pedagogy/`, not a two-page summary. The human expands it later via PROBE/ANSWER. Do not invent ANSWER. On inflammatory fog / sickness-behavior days: at most one rung.

## Read first

- `pedagogy/ontology.fu.md` — vertex/edge rules; no Person; claims in bodies
- `pedagogy/universe.graph.md` — existing V/E before grafting
- `pedagogy/pedagogy-cpu.fu.md` — STUDY / AGENT patterns
- Target paper (human URL or uploaded markdown). Prefer OA DOI.
- `.cursor/skills/fog-rest` if fog named — LowDemandIntake; skip lexicon pile

## HARD

- **Framework PDF ≠ blurb.** Ship a domain map: layers, vertex glossary, edge table, methods taxonomy, evidence grades, open GAP slots for later enrichment. Thin “两句话” fails the cut.
- **Do not dump the whole paper into chat.** Ladder: one PROBE per unfinished rung.
- **Privacy:** no lesion sites, private mg, or diagnosis from a chill paper.
- **Video (if asked):** follow `skills/video-generation.fu.md`. **Fresh Mixkit CDN ids** into `tmp/<slug>/_broll/` — do **not** copy prior fog/highway/rain kits. Local PIL memes only. Attribution line in builder.
- **MEDIA in vertices:** URL only (FIG/PAGE). Never paste figure bytes into pedagogy bodies.

## Pipeline

1. **Seed paper** — doi, title, year, kind (review / RCT / methods). Fig URLs if any.
2. **Prerequisite vertices** — invent only essences missing from the graph (e.g. IncentiveSalience before AestheticChills). Gloss one line; body holds CLAIMs + SOURCE.
3. **Domain framework TeX** — write `tmp/<slug>-framework.tex` (or skill template), compile with `python .cursor/skills/daily-brief/scripts/compile.py`.
4. **Mezzanine curriculum** — `mezzanine/<slug>.toon.md` ladder + methods muscle list.
5. **Wire** `universe.graph.md` V/E + STUDY stubs (empty ANSWER) + optional AGENT `$id=<slug>-ladder`.
6. **Optional MP4** — presentation DE+ZH; show *how the ladder works*, not abstract karaoke.
7. **Paradigm card** — when human asks for the skill itself as PDF: compile `.cursor/skills/paper-muscle/template.tex` → `tmp/paper-muscle.pdf`.
8. Stamp `python cron/janitor.py --touch`.

## Ladder shape (default six rungs)

1. Prerequisite constructs (wanting/liking or math definitions)
2. Body / measurement layer (interoception, instruments)
3. Computational / formal frame (predictive coding, model equation as schematic)
4. Paper Figure / Results map A
5. Paper Figure / Results map B (or primary contrast)
6. Benefits / applications **with bounds** (what NOT claimed)

Rename rungs to fit the paper. Fog day: stop after one PROBE.

## Evidence grades (for framework tables)

| Grade | Meaning |
|---|---|
| A | Multiple converging primary studies + clear methods |
| B | Solid primary or strong review claim |
| C | Preliminary / small-n / single modality |
| Spec | Author speculation or future work |
| Bound | Explicit non-claim (not Rx, imaging-limited, etc.) |

## Agent

```
AGENT $id=paper-muscle-ladder
Read mezzanine curriculum + seed vertex bodies.
Ask ONE PROBE for current unfinished rung.
Wait ANSWER. Do not invent ANSWER. Do not lecture whole paper.
Fog: ≤1 rung. Cite DOI + figure URLs when pointing at maps.
Never prescribe clinical protocols from chill/reward papers.
```

## Commands

```powershell
python .cursor/skills/daily-brief/scripts/compile.py tmp/<slug>-framework.tex
python .cursor/skills/daily-brief/scripts/compile.py .cursor/skills/paper-muscle/template.tex
# optional video
python tmp/<slug>/make_memes.py
# download NEW mixkit ids only — see broll.toml in kit
python tmp/<slug>/build_mp4.py
python cron/janitor.py --touch
```

OUTPUT `tmp/paper-muscle.pdf` (paradigm)
OUTPUT `tmp/<slug>-framework.pdf` (domain scaffold)
OUTPUT `tmp/<slug>/<slug>.mp4` (optional)

## Fail the cut if

- Framework PDF has no graph/edge section and no expansion GAP slots
- MP4 reuses another slug’s `_broll/` files without new CDN download
- Skill or PDF invents ANSWER or a diagnosis
- Vertex bodies store image/video bytes
