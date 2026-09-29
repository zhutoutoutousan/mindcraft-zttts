---
name: mindcraft-hall
description: >-
  Builds a Cypher-like first-person 3D museum over live mindcraft organs (ROOT,
  CPU, pedagogy, language, inflow, self, cron, schedule, skills). Use when the
  human asks for Cypher, 3D hall, first-person repo, 馆, 漫游 mindcraft, or
  python skills/mindcraft-hall.py.
---

# Mindcraft Hall (Cypher-like)

Do **not** hand-edit `tmp/pedagogy/mindcraft-hall.html`. Regenerate it.

```bash
python skills/mindcraft-hall.py
python skills/mindcraft-hall.py --serve
python skills/mindcraft-hall.py --serve --no-open
```

Output: `tmp/pedagogy/mindcraft-hall.html`. Script stamps TTL.

`--serve` binds `127.0.0.1:8781`+ (skips busy ports). Print the URL it actually bound.

Open in **Chrome or Edge**. Pointer lock and WASD fail in the Cursor Simple Browser. Click the gate to enter — that click **batch-allows** in-world YouTube (muted autoplay, German captions). Up to four screens play at once with perspective (**near large, far small**). **P** toggles hall music. Hall music pauses while a YouTube/video stage or the 2×2 deck is open.

Promo (Playwright + 悄悄话 ASMR German VO/subs): hall server up, then

```
python .cursor/skills/mindcraft-hall/scripts/promo.py
```

Opens `?tour=1&mute=1` in Chrome (no pointer lock, hall Klassik off so the ASMR VO is the only track). Output `tmp/hall-promo/hall-promo.mp4`. Voice kit: `.cursor/skills/whisper-asmr-vo`.

Nave **file cabinets** hold live files as **tokens**, not paper: octahedrons for links, mini-TVs for YouTube/Bilibili, dodecahedrons for text. They bob and spin.

**E** inspects a plaque. **Tab** / **I** opens a PDA: new words (into `pedagogy/_learn/polyglot/pda.toon.md` + lexicon), quick notes, warp to any room. **F** reads / embeds / plays. YouTube screens **autoplay in the hall** when you walk up (muted, **German captions** `cc_lang_pref=de`). **F** opens the stage with sound and the same DE captions, resuming the last timestamp. **嵌页** iframes the URL (YouTube nocookie, Bilibili player, Google Docs / PDF preview, or the raw page). Sites that send `X-Frame-Options` stay blank — use **在浏览器打开**. **N** creates a pin (or a library book). **K** / **收藏** copies a live DUMP/news URL onto the board without editing DUMP. **改/删** only work on pins (`crud: true`) or user books. **T** warps. **M** quad screens. **G** flashcards. After warp the horizon stays level (YXZ look, no roll).

Pins persist in `inflow/hall-board.toon.md` via `POST /api/board`. Not DUMP. Not ontology. No `.private`. Locked PROBE stays empty.

**作战室** is the north chamber (turn around from spawn, or **T** / minimap). Interior stays dark; the nave star-sky hides while you are inside. North wall is today's **0:00–24:00** strip: SOLL from stores (routine slots, PLAN NOW stretch, caffeine gate after 14:00, SRM dinner/bed anchors) plus IST you log. **L** or **F** on the TAG plaque writes `inflow/hall-day.toon.md`. Coarse places only. Unreported muscle is not sore. No `.private` paste. Not a week calendar.

**书库** is the east wooden atrium (nave **LIB** cabinet / pad, or **T** / minimap). Lacquered panel walls, brass moulding, parquet floor with a live reflector. You cannot walk out (position clamp). **Turn around at the west gold ring and press T** to return to the nave; PDA 传送 / minimap also warp. East rings are **1/2/3F** lifts. Open well through 2F/3F galleries, chandelier + west window light, book/shelf shadows. Pudong-like stacks on three floors. Books are live PDF / YouTube / page URLs. **N** in the library writes `inflow/hall-library.toon.md` via `POST /api/library`. Central + wall screens default to feeds from PLAN NOW, goals/north, `targetLang`, and grasp-unknown nodes — not invented ANSWER. **M** opens a 2×2 deck (iframes only then). **G** / flashcard screen uses `pedagogy/_learn/writing-accuracy/drills.toon.md`. Harvest rows seed language shelves. No `.private`.

Performance: `powerPreference: high-performance`, WebGL2, no stencil, antialias off when DPR > 1, pixelRatio cap 1.15 (1.0 on >1080p). HUD shows the unmasked GPU name + fps — if it says SwiftShader / Basic Render Driver, Chrome is on CPU: Settings → System → Use hardware acceleration. Nave marble floor reflector stays **on in every organ side room** (CPU, Pedagogy, … cron/skills); only library (parquet) and war (hex) swap it out. Floor RT is **2048 standing / 1024 walking** (opaque floor under the mirror so it never flashes white). Nave walls are honed stone with clearcoat only — **no vertical planar reflectors** (those smear a vanishing-point wedge when you look along the hall). Freeze nave shadow updates while moving. Skip CSS3D composite when no in-world YouTube is visible. In-cabinet mini-TVs stay as posters (CSS3D would draw through the case). Wall / library screens still play in-world, but a raycast hides them when a wall or cabinet is in front. PointLights instead of RectArea in nave/side rooms, library/war hidden when you are elsewhere. Hall keys use a hidden keytrap input so Chrome / Vimium / YouTube iframes cannot eat WASD: capture + `preventDefault` + `stopImmediatePropagation`, refocus every frame while walking. PDA and forms still type. Esc still unlocks the mouse — that is a Chrome pointer-lock rule. Ctrl+T / Ctrl+W / Ctrl+N cannot be captured.

## What it is

A white vaulted hall in the spirit of [Cypher](https://store.steampowered.com/app/746710/Cypher/) (Matthew Brown, 2018): first-person walk, plaques, a Caesar desk. The **nave** opens to a milky-way sky; vault lamps stay bright (interior 灯火通明). Organs stay different KINDs — side rooms, not one force-graph.

| room | store |
|------|--------|
| nave | ROOT organs + Today actions |
| CPU | AGENT / TODO / SCHEDULE / NOTE TODAY |
| Pedagogy | universe.graph branches + empty PROBE tablets |
| Language | horizon langs + todayFocus cipher |
| Inflow | STATE + DUMP digest |
| Self | goals / flags (no `.private` body) |
| Cron | gatherer jobs |
| Schedule | harvest rows |
| Skills | cursor skills + tmp TTL |
| War | Lagezentrale: map, holograph, named states |
| Library | Wood atrium, PDF/YouTube books, customized screens, flashcards |

## Hard rules

- Never invent STUDY ANSWER. Locked tablets are empty PROBEs.
- Never paste `.private/` bodies.
- Re-run the script to refresh the snapshot; the page rebuilds on each GET when `--serve`.
- TTL/purge keeps `tmp/pedagogy/mindcraft-hall.html`. Do not hand-edit it; regenerate. Other `tmp/` siblings expire.
- Pins live only in `inflow/hall-board.toon.md`. Hall delete is not DUMP delete.
- Library books live only in `inflow/hall-library.toon.md`. URL must be http(s). Not DUMP.
- YouTube resume times live in `inflow/hall-watch.toon.md`. Auto-save on pause/close, or type `mm:ss` and 记下. Next **F** starts at that second.
- PDA captures live in `pedagogy/_learn/polyglot/pda.toon.md` via `POST /api/pda` (no page rebuild). Words also stamp `lexicon.graph.md`. Not ANSWER. No `.private`.
- Not a replacement for `project-state-viz.py` dashboards.

## Related

- `skills/mindcraft-hall.py` + `skills/mindcraft-hall.html`
- `skills/project-state-viz.py` (collector)
