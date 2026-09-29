schema: skills/diagram-arsenal
updated: 2026-09-08
note: Visualization kit for this repo. Not an install log. Do not vendor third-party skills. Do not invent that Archify is installed.
eval.focus: CursorSkill SpatialGraphics
source: https://tt-a1i.github.io/archify/
source: https://github.com/tt-a1i/archify
source: skills/video-generation.fu.md
source: skills/ontology-showcase.fu.md

# When to pick which drawing tool

pick[3]{id,use,avoid,output}:
  Archify,explorable architecture / workflow / sequence / data-flow / lifecycle of agent skills and harnesses,LaTeX PDF stills and ontology PlantUML,self-contained HTML in tmp/ then optional 4x PNG SVG
  PlantUML-Kroki,LaTeX daily-brief / paper-muscle / video stills / ontology puml,explorable skill maps when Archify is the ask,tmp PNG/SVG/PDF via existing kits
  ontology-showcase,universe.graph core + stack PNG and pan-zoom HTML,skill-procedure architecture,tmp/pedagogy/universe.*

archify:
  kind: Cursor/Claude/Codex/OpenCode agent skill. Plain English to architecture HTML.
  site: https://tt-a1i.github.io/archify/
  repo: https://github.com/tt-a1i/archify
  license: MIT per product page. Based on Cocoon-AI/architecture-diagram-generator.
  types[5]: Architecture, Workflow, Sequence, Data Flow, Lifecycle
  install.not_done: true
  install.cursor: npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
  install.note: npx skills CLI wants Node >=22. This machine is Node 20.12.2 so global skill install failed 2026-09-08. Test used git clone into tmp/_archify then node bin/archify.mjs. Do not vendor their tree into pedagogy/.
  lastTest: 2026-09-08 workflow Diagram-Arsenal Test. HTML tmp/archify-diagram-arsenal.html. deliver 9/9 showcase. visual-check containment pass. Viewer UI English (meta.locale omitted).
  trigger: human asks Archify, skill architecture, harness map, agent tool-call diagram, beautiful HTML architecture
  skill.path: .cursor/skills/diagram-arsenal/SKILL.md
  graph: pedagogy/computation/stack/Archify.fu.md

plantuml:
  use: steering/plantuml-crisp.md when that file exists; else skills/video-generation.fu.md contrast skin
  kits[3]: skills/ontology-showcase.fu.md, .cursor/skills/daily-brief, .cursor/skills/cursor-agent-retry
  rule: SVG/PDF over blurry PNG. No vertical truncation.

rule[4]:
  - Archify HTML is a tmp deliverable. Stamp python cron/janitor.py --touch. Do not store generated HTML in pedagogy/.
  - Do not replace PlantUML for page-bound PDF.
  - Do not invent completed diagrams or an install.
  - Do not paste private names, streets, join URLs, or lesion sites into a diagram.
