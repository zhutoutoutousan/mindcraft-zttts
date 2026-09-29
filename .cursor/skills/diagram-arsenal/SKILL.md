---
name: diagram-arsenal
description: >-
  Picks the drawing tool for architecture of agent skills and harnesses.
  Archify for explorable HTML (architecture, workflow, sequence, data flow,
  lifecycle). PlantUML/Kroki for LaTeX PDF and video stills. Use when the
  human names Archify, skill architecture, harness map, agent tool-call
  diagram, beautiful HTML architecture, or diagram arsenal.
---

# Diagram arsenal

Read `skills/arsenal.toon.md` first. Library contract: `skills/arsenal.fu.md`. Vertex: `pedagogy/computation/stack/Archify.fu.md`.

Do **not** vendor [Archify](https://tt-a1i.github.io/archify/). Do not invent an install. Do not invent a completed diagram.

## Pick

| Ask | Tool | Output |
| --- | --- | --- |
| Skill / harness / tool-call architecture, explorable HTML | Archify | `tmp/*.html` (optional 4× PNG/SVG) |
| Daily brief, paper PDF, video still, ontology puml | PlantUML / Kroki as existing kits | tmp PDF/PNG |
| `universe.graph` core + stack | `skills/ontology-showcase.py` | `tmp/pedagogy/universe.*` |

## Archify

Site: https://tt-a1i.github.io/archify/  
Repo: https://github.com/tt-a1i/archify

1. If `~/.cursor/skills/archify/SKILL.md` exists, follow **that** skill. Put the HTML in `tmp/`. Then `python cron/janitor.py --touch`.
2. If it does not exist, prefer a tmp clone over a broken npx on Node 20:

```bash
git clone --depth 1 https://github.com/tt-a1i/archify.git tmp/_archify
node tmp/_archify/archify/bin/archify.mjs doctor
```

Global install still wants Node >=22:

```bash
npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
```

3. Follow `archify/SKILL.md`: write JSON, `validate --quality showcase`, then `deliver`. HTML only in `tmp/`. Do not vendor their tree into `pedagogy/`.

## Must not

- Streets, join URLs, private names, lesion sites on a figure
- Blurry upscaled PNG in LaTeX (PlantUML path still prefers SVG/PDF)
- Storing generated HTML under `pedagogy/`
