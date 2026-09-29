# SKILL stage-body-composite

TESTED unsatisfied — scripts exist; no local dancer/plate/song yet. Do not invent a finished MP4.

## Contract

- Joke form: person A matted onto singer B's standing box; audio is song C. Default recipe `friend-wine`: 许家印跳舞 × concert singer box × 朋友的酒. Human 2026-09-12: plate is 林力建, not Pavarotti.
- Distinct from `skills/video-generation.fu.md` (German TTS + dual captions + Mixkit). Do not run edge-tts Katja on this cut unless the human names a VO layer.
- Human supplies local `_in/` files. Agent does not download concert masters or the song.
- Preview one composite still before full encode. `--max-seconds` default 20 (Shorts-length).
- MEDIA bytes stay in `tmp/<slug>/`. Stamp janitor TTL. Do not commit `_in/` or the master.
- No GenerateImage. No lyrics dump into pedagogy.

## Commands

```powershell
pip install rembg pillow imageio-ffmpeg onnxruntime
python .cursor/skills/stage-body-composite/scripts/build.py --slug friend-wine --preview
python .cursor/skills/stage-body-composite/scripts/build.py --slug friend-wine --max-seconds 20
python cron/janitor.py --touch
```

OUTPUT tmp/friend-wine/friend-wine.mp4
HARD: missing `_in` → STOP and list filenames.

## Explain card (human)

When the human asks 怎么弄 / how this skill works: read `.cursor/skills/stage-body-composite/SKILL.md`. Do not fetch Pavarotti or 朋友的酒.
