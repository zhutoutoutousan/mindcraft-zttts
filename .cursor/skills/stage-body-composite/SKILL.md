---
name: stage-body-composite
description: >-
  Mattes a dancer (or any person clip) onto a concert plate where a singer
  stands, then muxes a third-party song so the stage reads as that tenor
  singing the song. Default recipe: 许家印跳舞 onto a concert singer's standing box + 朋友的酒.
  This cut's plate is 林力建 (not Pavarotti) when the human names that swap.
  Use when the human names 朋友的酒, 许家印跳舞, 林力建, 帕瓦罗蒂, 扣人, 抠像换人,
  stage-body-composite, or asks to paste a person onto an opera/concert singer.
---

# Stage body composite

This is **not** the German TTS slide kit in `skills/video-generation.fu.md`.
Here the joke is: **person A occupies singer B's spot; audio is song C.**

Default recipe `friend-wine`: 许家印跳舞 → concert singer standing box → 朋友的酒.
This run's plate is **林力建** (human 2026-09-12), not Pavarotti.

## HARD

- Human drops **local** files. Do **not** yt-dlp / curl concert masters or the song into the repo.
- Do **not** commit `_in/` videos or the muxed master. Output stays `tmp/<slug>/`.
- Do **not** dump copyrighted lyrics into SKILL.md or pedagogy.
- Do **not** `GenerateImage` the dancer or the tenor. Use the provided clip/still.
- Do **not** claim the cut is an official Pavarotti release or that anyone applied/attended.
- Parody overlay only. No scam / impersonation-as-real-news packaging.
- Face still `face.jpg` onto `dancer.mp4` is a second cut (`dancer-face.mp4`). Same parody rule. Do not label the still as a named identity unless the human named them.
- Retry-safe: matte may be thousands of frames. Preview **one frame** before full encode. No parallel image APIs.

## Inputs

Put files in `tmp/<slug>/_in/` (default slug `friend-wine`):

| File | Role |
| --- | --- |
| `dancer.mp4` (or `.mov` / `.webm`) | Person to cut out (许家印跳舞) |
| `plate.mp4` | Concert plate (this cut: 林力建) |
| `song.m4a` / `.mp3` / `.wav` / `.mp4` | Audio (朋友的酒; video is stripped) |
| `bbox.json` | `{x,y,w,h}` of the singer box on the **plate** (pixels) |

A still of the dancer is not enough for a dance cut. A still can seed a Ken-Burns placeholder only if the human names that fallback.

## Agent pipeline

Copy this checklist:

```
- [ ] _in files present (else STOP and list missing names)
- [ ] plate0.png extracted; bbox.json exists (else STOP, ask for box)
- [ ] preview.png looks planted on the singing spot
- [ ] matte + overlay + mux → tmp/<slug>/<slug>.mp4
- [ ] python cron/janitor.py --touch
```

```
python .cursor/skills/stage-body-composite/scripts/build.py --slug friend-wine --preview
python .cursor/skills/stage-body-composite/scripts/build.py --slug friend-wine --max-seconds 20
python cron/janitor.py --touch
```

`--preview` writes `_work/preview.png` only. Human adjusts `bbox.json`, then full build.

Duration = `min(song, max-seconds)`. Loop dancer (and plate if shorter) to fill. Mute both videos; audio is song only.

## Three rungs (pick the lowest that ships)

1. **Overlay (default).** Matte dancer → scale to `bbox` height → paste on plate frames → mux song.
2. **Tracked box.** Same, but bbox follows the largest person on the plate (see [reference.md](reference.md)). Only if overlay slips off the tenor.
3. **Mouth keep (optional).** After overlay, paste a small ellipse from the original plate (tenor mouth) on top. Do **not** run a face-swap / lip-sync model unless the human names that rung.

剪映 / CapCut is allowed as a human-speed path for rung 1 (抠像 → 叠加到人声位置 → 替换音频). Agent still must not fetch the masters.

## Fail the cut

- Dancer still has original background (failed matte)
- Person planted on orchestra / ceiling, not the singing spot
- Plate audio still audible under 朋友的酒
- Agent downloaded YouTube as a "help"
- Full encode ran before preview.png existed

## Contract file

`skills/stage-body-composite.fu.md` — lasting rules. Details: [reference.md](reference.md).
