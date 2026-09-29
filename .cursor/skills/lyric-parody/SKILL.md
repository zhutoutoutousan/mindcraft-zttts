---
name: lyric-parody
description: >-
  Rewrites a song's lyrics while keeping the original tune, meter, and line
  timings (填词戏仿). Optional local mix: Demucs instrumental + TTS retuned to
  the original vocal F0. Use when the human names 改词, 填词, 曲调不变, 换歌词,
  戏仿歌词, 改编歌词, parody lyrics, same melody, same tune, or wants new words
  on an existing song.
---

# Lyric parody（曲调不变，只换词）

Job is **same tune, new words**. Not a new composition. Not a lyrics dump of the original.

Output under `tmp/lyric-parody/<slug>/`. Stamp TTL.

```
python .cursor/skills/lyric-parody/scripts/meter.py --job tmp/lyric-parody/<slug>/job.json
python .cursor/skills/lyric-parody/scripts/mix.py --job tmp/lyric-parody/<slug>/job.json
python cron/janitor.py --touch
```

Needs `edge-tts` `numpy` `pyworld` `imageio-ffmpeg`. Mix also needs `demucs`. Align without `--cues` needs `faster-whisper` (or `openai-whisper`). `pip install edge-tts numpy pyworld imageio-ffmpeg demucs faster-whisper`

## Agent pipeline

1. Name the **tune** (title + artist). If the human only drops audio, run `video-bgm-id` first. Do not guess the song.
2. Build a **skeleton** of line lengths only (`n` = 字 for ZH, syllables for EN/DE). Optional `t0`/`t1` if mixing. **Do not paste original lyrics** into pedagogy, SKILL, or chat.
3. Write parody lines that match each `n`, keep 句读 / rhyme family, keep chorus repeats as repeats.
4. Write `tmp/lyric-parody/<slug>/job.json` (see [reference.md](reference.md)). Run `meter.py`. Fix mismatches before mixing.
5. Mix **only** if the human names 出音频 / 混音 / 唱出来 / cover, **and** a **local** file exists. Then `mix.py`.
6. Report the new lyrics + (if mixed) the wav path. `python cron/janitor.py --touch`

## Meter (this is the tune)

ZH: one 汉字 ≈ one note. Punctuation and spaces do not count.  
EN/DE: count syllables; stressed beats stay on the same slots as the skeleton.  
A line that is ±0 vs skeleton is a pass. ±1 only on a pickup/breath line, marked `flex: true`. Chorus lines that repeat in the original must repeat the same parody line.

Theme comes from the human (default: whatever cut is in chat). Do not invent STUDY ANSWER, street NAP, or recruiter names as lyrics.

## Mix (optional)

`mix.py` splits local audio with Demucs, follows the original vocal **F0** with WORLD, drops new words onto the instrumental. That is a **scratch sing** (speech timbre on the old melody), not a studio cover. Do not claim it is the original singer.

Default voice `zh-CN-YunxiNeural`. DE → `de-DE-ConradNeural`. EN → `en-US-GuyNeural`.

## Hard

- MEDIA bytes stay in `tmp/lyric-parody/`. Do not commit wav/mp3/mp4.
- Do not dump original lyrics. Skeleton counts and parody lines are the deliverable.
- Do not claim a license, fair use as legal advice, or that the UP/label cleared it.
- Do not yt-dlp / curl YouTube or Bilibili masters into this kit (`video-bgm-id` identify-only; `stage-body-composite` still forbids that mux).
- Human drops **local** audio for mix. No GenerateImage of the singer.
- Parody overlay only. No scam / impersonation-as-real-release packaging.
