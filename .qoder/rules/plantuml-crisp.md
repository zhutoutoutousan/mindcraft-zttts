---
description: PlantUML must be crisp and never vertically cropped in PDF/LaTeX
alwaysApply: true
---

# PlantUML：禁止糊图 + 禁止垂直截断

Before generating or embedding any PlantUML diagram, read and follow `steering/plantuml-crisp.md`.

## Must

- Prefer **SVG or PDF** export over PNG.
- If PNG: `skinparam dpi 300` (or higher), short side **≥ 1200px**; do not upscale a small PNG in LaTeX/Markdown.
- Long activity chains (≥5 steps): use **`left to right direction`**, or split into two figures. Do not ship a page-tall vertical strip.
- In LaTeX always set **both** caps, e.g. `width=0.9\textwidth,height=0.78\textheight,keepaspectratio`. Width-only on a tall PNG causes bottom clipping (black bar).
- Use `[p]` / own page when the figure is still tall after LTR.
- Keep `.puml` source; zoom 150% — text sharp; **start and stop nodes fully visible**.

## Must not

- Deliver blurry, pixelated, or screenshot diagrams.
- Stretch low-res PNG with large `width=\textwidth`.
- Allow **vertical truncation** (cropped last steps, cut `stop` node, footer black bar over the diagram).
- Fix truncation by cropping harder or ignoring Overfull `\vbox` warnings.

If a prior PDF figure is blurry **or** clipped, regenerate per `steering/plantuml-crisp.md` and rebuild.
