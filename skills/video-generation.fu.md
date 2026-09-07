# SKILL video-generation

TESTED SATISFIED 2026-09-01 · revised 2026-09-06 partner meme+broll + type floor + retry-safe meme/CDN hard rules.

## Contract

- Playback: German only · `de-DE-KatjaNeural` · **rate +35% to +40%** (never default crawl)
- Subtitles: dual burnt-in DE (gold `#ffcc80`) over second language (cyan `#90caf9`) + sidecar `.srt` / `.ass`
  - Default second language: EN. Partner / ZH cuts: put ZH in the cyan slot (spoken still DE)
- Voice of the talk: **presentation**, not recitation. Questions to camera, analogies, punchlines. Do not read a paper abstract aloud.
- Picture, **two masters every cut** when publishing social (never only one):
  - Landscape `16:9` `1920×1080` — YouTube / Bilibili / LinkedIn / Facebook long-form
  - Portrait `9:16` `1080×1920` — Douyin / TikTok / 快手 / 视频号 / Reels / Shorts canvas
- Short partner notes may ship **16:9 only** under `tmp/<slug>/` (TTL 5 days). Still obey type floor + meme/b-roll rules below.
- Portrait **safe zone**: keep type and diagrams out of the top 12% and bottom 18% (platform chrome). Right 8% clear of like/share stack.
- **Type floor** (matplotlib pt @ 1920×1080 / 100dpi, landscape):
  - DE subtitle ≥ **22** · second-lang ≥ **20** · ASS DE ≥ **40** · ASS second ≥ **34**
  - Slide body labels ≥ **18** · hero line ≥ **30**
  - Portrait floor unchanged: DE ≥24, second ≥20, code ≥18, hook ≥36
  - Phone-unreadable captions fail the cut.
- Hook cut: portrait **≤ 59.9 s** at a beat boundary for Shorts / Reels-reach. A 7–10 min deep dive must **not** be uploaded as a Short.
- Mezzanine: `mezzanine/<slug>.toon.md` is the spoken source of truth for deep dives
- Evidence (deep dives): run `python skills/loop-slash/bench_loop.py` first. Myths without a measurement or a cited skill/doc line do not ship.
- Deliverables under `tmp/<slug>/`. Stamp `tmp/ttl.toon.md` (`python cron/janitor.py --touch`). Janitor `--ttl` deletes tmp siblings 5 days after last_run.

## Meme + public b-roll (required for playful / partner cuts)

Do **not** ship a wall of tiny diagram slides alone when the human asked for 玩梗 / 表情包 / 配视频.

**HARD (stream / retry safety — see `.cursor/skills/cursor-agent-retry`):**

- Memes: **local script only** by default (`make_memes.py` / PIL). Store under `tmp/<slug>/_memes/`. Do **not** open a multi-`GenerateImage` batch. If the human insists on API images: ≤2 per turn, then stop.
- B-roll: Mixkit / Coverr / Pexels free license. Prefer known CDN URLs (`https://assets.mixkit.co/videos/<id>/<id>-720.mp4`) downloaded with Shell into `_broll/`. Do **not** parallel-`WebFetch` many gallery HTML pages to hunt clips. Mute b-roll; never steal audio. One-line attribution (source + id) in the builder.
- Pipeline split: (1) write scripts + make memes + download b-roll; (2) TTS/slides/encode in a later turn if the path is flaky. On interrupt: reuse existing `_memes/` `_broll/` `_audio/`; rebuild only missing steps.
- Intercut per beat: still + meme (~half) → short matching b-roll. Corner-paste stickers; clear of subtitle bar (~bottom 24%) and header. Fixed RNG seed for corners.

Partner reference kit: `tmp/fog-partner/` — `make_memes.py` then `build_mp4.py`.

## Style bar (fail the cut if any is true)

- Sounds like a textbook being read
- No analogy in the first 60 seconds
- Diagrams are only bullet lists
- PlantUML arrows black / dark-on-dark (`#0a0e14`). Lines must be `#69f0ae` or `#90caf9`, thickness ≥ 3
- Speech feels sleepy / default TTS rate
- Under 7 minutes for a deep dive
- Portrait is a letterboxed 16:9 with black bars
- Captions look like footnotes (below type floor)
- Partner/playful cut ships with **no** memes and **no** public b-roll when the human asked for them
- Deep-dive file shipped to a ≤3 min shelf instead of the hook

## Pipeline

1. Author beats (`id`, `section`, `visual`, `de`, `second-lang`, optional `meme`, `broll`)
2. Deep dive: PlantUML via Kroki; partner: matplotlib cards OK
3. `edge-tts` German per beat at `rate="+38%"` · 0.22s pause
4. Render still PNG per beat · paste meme from `_memes/`
5. ffmpeg: still clip + looped/cropped Mixkit clip per beat → concat → mux AAC → burn ASS
6. Stamp TTL. Deliver `tmp/<slug>/<slug>.mp4` (+ portrait masters when publishing)

## Voices / colors

- DE voice: `de-DE-KatjaNeural` @ `+38%`
- Second language: subtitle only (EN or ZH)
- DE sub `#ffcc80` · second `#90caf9` · accent `#69f0ae`

## Commands

```powershell
pip install edge-tts imageio-ffmpeg matplotlib numpy pillow
python tmp/fog-partner/make_memes.py
python tmp/fog-partner/build_mp4.py
python skills/loop-slash/render.py --force
python cron/janitor.py --touch
```

FFmpeg: `imageio_ffmpeg.get_ffmpeg_exe()`

OUTPUT tmp/fog-partner/partner.mp4
OUTPUT tmp/loop-slash/loop-slash.mp4
OUTPUT tmp/video-pipeline/video-pipeline.mp4
HARD: never copy another slug's `_broll/`; download new Mixkit CDN ids (see `.cursor/skills/paper-muscle`).
ARCHIVE_URL pending

## Explain card (human)

When the human asks how this skill works / how to improve it:

```
python .cursor/skills/daily-brief/scripts/compile.py tmp/video-pipeline.tex
python tmp/video-pipeline/make_memes.py
python tmp/video-pipeline/build_mp4.py
python cron/janitor.py --touch
```

PDF: `tmp/video-pipeline.pdf`. MP4: `tmp/video-pipeline/video-pipeline.mp4`. Lasting contract stays in this file; improvement backlog details may live in the PDF until promoted here.

## Improve backlog (promote after shipped)

1. Shared `skills/video_kit/` (tts, burn_ass_win, intercut, type_floor) — stop copying `build_mp4.py`
2. `--demo sid` PNG-only preview (DEV CI pipeline lesson)
3. TTS text-hash cache (telegraph/script-to-video)
4. Default `--aspect both` for publish cuts (steal from loop-slash)
5. Optional Whisper word-level captions for Shorts only
6. `broll.toml` fixed Mixkit ids + attribution
7. Offline PlantUML JAR fallback beside Kroki
8. QA gate: audio/video drift, missing meme, type-floor scan

GitHub refs (read, do not vendor blindly): telegraph/script-to-video · Anionex/banana-slides · jmjava/documentation-generator · premkumarofficeoff/Automated-Video-Generator · NesDevr/video-factory · SamurAIGPT/Text-To-Video-AI
