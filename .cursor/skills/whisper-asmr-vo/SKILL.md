---
name: whisper-asmr-vo
description: >-
  Generates 悄悄话 ASMR German voiceover plus German subtitles (edge-tts
  close-mic, ffmpeg proximity chain, burnt-in DE captions + sidecar SRT/ASS).
  Use when the human names 悄悄话, ASMR, Flüstern, German whisper voiceover,
  德语旁白, 德语字幕, intimate VO, or wants a reusable DE whisper layer on a cut.
  Distinct from the Katja +38% presentation kit in skills/video-generation.fu.md.
---

# Whisper ASMR VO (German)

Quiet close-mic German. Not a talk. Not Katja at `+38%`.

Spoken **German only**. Captions **German only** (cream, not dual ZH/EN). Output under `tmp/<slug>/`. Stamp TTL.

## Contract

| | Presentation kit | This kit |
| --- | --- | --- |
| Voice | `de-DE-KatjaNeural` `+38%` | same voice **or** Conrad, `rate -18%…-28%`, `pitch -4Hz…-10Hz` |
| Tone | questions, punchlines | 悄悄话 / Flüstern / ASMR: short clauses, **du**, present, breath gaps |
| Subs | DE gold + second cyan | **DE only**, cream `#e8e0d4`, type floor DE ≥ 22 |
| Mix | dry TTS | **WORLD unvoice** (F0=0, aperiodicity=1) then close-mic Haas. Not EQ-on-modal-speech. |

Fail the cut if it is still **modal voice** (真声 / voiced pitch). Slow Katja plus a lowpass is not 悄悄话. Edge-tts has no German `whispering` style on the free endpoint.

## Pipeline

1. Author beats JSON: `id`, `de`, optional `pose` `{x,z,yaw,pitch}`.
2. Synthesize:

```
python .cursor/skills/whisper-asmr-vo/scripts/synthesize.py --beats <beats.json> --out tmp/<slug>
```

Writes `_audio/*.raw.mp3`, `_audio/*.asmr.wav`, `voiceover.wav`, `captions.de.srt`, `captions.de.ass`, `cues.json`.

3. Picture (any source: Playwright, ffmpeg stills, existing mp4). Then mux:

```
python .cursor/skills/whisper-asmr-vo/scripts/mux.py --video <clip> --work tmp/<slug> --out tmp/<slug>/<slug>.mp4
```

4. `python cron/janitor.py --touch`

## Voice rules

- One sentence, then air. No compound walls.
- No `.private`, no street+number, no lesion sites, no invented STUDY ANSWER.
- Prefer `de-DE-KatjaNeural` as the German formant source, then **unvoice** with pyworld. `de-DE-ConradNeural` if the human names a male whisper.
- Do not send `<speak>` SSML into edge-tts. Do not rely on Azure `style=whispering` unless a paid Speech key exists.
- Do not stack hall classical under the whisper unless the human names it; then hall music ≤ -28 dB.

## Hall promo

Mindcraft Hall first-person cut: `.cursor/skills/mindcraft-hall` + this kit.

```
python .cursor/skills/mindcraft-hall/scripts/promo.py
```

Opens `http://127.0.0.1:8781/mindcraft-hall.html?tour=1` in Chrome via Playwright, drives `__hall.setPose`, muxes this VO. Hall server must already be up (`python skills/mindcraft-hall.py --serve --no-open`).

## Hard

- MEDIA bytes stay in `tmp/`. Do not commit wav/mp4.
- Do not use this kit on `stage-body-composite` (that cut is song-only) unless the human names a VO layer.
- Ctrl+T/W/N still belong to Chrome; tour mode does not need WASD.
