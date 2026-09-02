# SKILL video-generation

TESTED SATISFIED 2026-09-01 · revised 2026-09-01 dual-aspect + worldwide publish pack.

## Contract

- Playback: German only · `de-DE-KatjaNeural` · **rate +35% to +40%** (never default crawl)
- Subtitles: dual burnt-in DE (gold) over EN (cyan) + sidecar `.srt` / `.ass`
- Voice of the talk: **presentation**, not recitation. Questions to camera, analogies, punchlines. Do not read a paper abstract aloud.
- Picture, **two masters every cut** (never only one):
  - Landscape `16:9` `1920×1080` — YouTube / Bilibili / LinkedIn / Facebook long-form
  - Portrait `9:16` `1080×1920` — Douyin / TikTok / 快手 / 视频号 / Reels / Shorts canvas
- Portrait **safe zone**: keep type and diagrams out of the top 12% and bottom 18% (platform chrome). Right 8% clear of like/share stack.
- Portrait **type floor** (matplotlib pt @ 1080×1920 / 100dpi): DE sub ≥24, EN sub ≥20, code ≥18, hook headline ≥36. Phone-unreadable captions fail the cut. Fill the 1080px width — do not wrap to a skinny column.
- Hook cut: portrait **≤ 59.9 s** at a beat boundary for Shorts / Reels-reach / Spotlight / Snapchat. A 7–10 min deep dive must **not** be uploaded as a Short.
- Mezzanine: `mezzanine/<slug>.toon.md` is the spoken source of truth
- Evidence: run `python skills/loop-slash/bench_loop.py` first. Myths without a measurement or a cited skill/doc line do not ship.
- Key code: parser, cron gaps, sentinel, the commands you type — on screen, not only in the mouth.
- Publish pack: `skills/loop-slash/PUBLISH.md` is the copy-paste form for **all** target platforms. Fill it before the human sits in any uploader.
- Deliverables: `tmp/loop-slash/` masters, covers, sidecars. Stamp `tmp/ttl.toon.md`. Janitor `--ttl` deletes tmp siblings 5 days after last_run. There is no videos/ folder.
- After human revise → social upload → paste URLs into ARCHIVE_URL below → **then** cleanup (never before)

## Style bar (fail the cut if any is true)

- Sounds like a textbook being read
- No analogy in the first 60 seconds
- Diagrams are only bullet lists
- PlantUML arrows, lifelines, or group boxes are black / dark-on-dark (`#0a0e14`). Lines must be `#69f0ae` or `#90caf9`, thickness ≥ 3. Render injects `PUML_CONTRAST` before `@enduml`.
- Speech feels sleepy / default TTS rate
- Under 7 minutes for a deep dive
- Portrait is a letterboxed 16:9 with black bars (must be a real 9:16 layout)
- Portrait DE/EN captions or code look like footnotes on a phone
- Deep-dive file shipped to a ≤3 min shelf (Shorts / Reels-reach) instead of the hook

## Pipeline

1. Author mezzanine beats (`id`, `section`, `visual`, `de`, `en`) — DE is spoken, EN is subtitle only
2. Write `skills/loop-slash/diagrams/*.puml` — dark bg `#0a0e14` but **never black arrows**. Kroki `POST https://kroki.io/plantuml/png`. Renderer injects contrast skinparams before `@enduml`.
3. `edge-tts` German per beat at `rate="+38%"` · 0.22s pause (not 0.4s)
4. One slide PNG per beat **per aspect** (PlantUML image or code) — stills, not per-frame matplotlib
5. ffmpeg concat stills + mux AAC → `16:9` master, `9:16` master, `9:16` hook
6. Covers: `cover.16x9.png` · `cover.9x16.png` · `cover.3x4.png` (Xiaohongshu)
7. `chapters.txt` from real cue times · `PUBLISH.md` copy-paste pack
8. Deliver:

```
tmp/loop-slash/loop-slash.mp4              16:9 master
tmp/loop-slash/loop-slash.9x16.mp4         9:16 master
tmp/loop-slash/loop-slash.hook.9x16.mp4    ≤60s portrait hook
tmp/loop-slash/loop-slash.de-en.srt
skills/loop-slash/PUBLISH.md
```

## Which file goes where

| File | Platforms |
| --- | --- |
| `<slug>.mp4` (16:9) | YouTube long · Bilibili 投稿 · LinkedIn · Facebook video · X · Reddit · Vimeo · Rumble · Dailymotion · 西瓜 / 头条横屏 |
| `<slug>.9x16.mp4` (9:16 full) | 抖音 · 快手 · 视频号 · 小红书 · TikTok · Bilibili Story · 微博 · 知乎 · Instagram 长视频 |
| `<slug>.hook.9x16.mp4` (≤60s) | YouTube Shorts · Instagram Reels (reach) · Facebook Reels · Snapchat Spotlight · Pinterest Idea · Lemon8 · Threads |

## Cleanup — only after user confirms the upload

Do **not** delete anything while the user is still revising.

When the user says the video is uploaded and satisfied (and ARCHIVE_URL is filled):

```powershell
python skills/loop-slash/render.py --cleanup --confirmed-uploaded
```

Deletes work dirs under `tmp/loop-slash/`: `_audio/`, `_slides/`, `_slides_9x16/`, concat lists, `_pause.mp3`, `full.mp3`, `_silent*.mp4`
Keeps kit: `skills/loop-slash/render.py`, `diagrams/*.puml`, mezzanine, `PUBLISH.md`, this skill file
Masters in tmp die with janitor `--ttl` after 5 days, or `--also-mp4` on cleanup after upload confirm.

## Voices / colors

- DE voice: `de-DE-KatjaNeural` @ `+38%`
- EN: subtitle only
- DE sub `#ffcc80` · EN sub `#90caf9` · accent `#69f0ae`

## Commands

```powershell
pip install edge-tts imageio-ffmpeg matplotlib numpy pillow
python skills/loop-slash/render.py
python skills/loop-slash/render.py --force
python skills/loop-slash/render.py --aspect 9x16
```

`--force` rebuilds TTS + both aspects. Default reuses `_audio/` if present.
`--aspect both|16x9|9x16` (default `both`). Existing 16:9 master is skipped unless `--force`.

FFmpeg: `imageio_ffmpeg.get_ffmpeg_exe()`

OUTPUT tmp/loop-slash/loop-slash.mp4
OUTPUT tmp/loop-slash/loop-slash.9x16.mp4
OUTPUT tmp/loop-slash/loop-slash.hook.9x16.mp4
ARCHIVE_URL pending
