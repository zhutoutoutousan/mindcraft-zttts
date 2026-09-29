---
name: video-bgm-id
description: >-
  Identifies background BGM in a Bilibili, YouTube, or local clip via Shazam
  audio fingerprint. Use when the human names BGM, 背景音乐, 查BGM, 原曲, 配乐,
  识曲, Shazam, or pastes a BV / YouTube URL asking what song is playing.
---

# Video BGM id

Fingerprint the **audio**, do not guess from the title. Output under `tmp/bgm-id/`. Stamp TTL.

```
python .cursor/skills/video-bgm-id/scripts/identify.py --url https://www.bilibili.com/video/BV...
python .cursor/skills/video-bgm-id/scripts/identify.py --file tmp/bgm-id/clip.wav
python cron/janitor.py --touch
```

Needs `shazamio` + `imageio-ffmpeg` (or ffmpeg on PATH). `pip install shazamio imageio-ffmpeg`.

## Agent pipeline

1. Run `identify.py --url <page>` (or `--file` if audio already exists).
2. If it prints `NEED_BROWSER_PLAYINFO` (Bilibili HTTP 412): open the video in the Cursor browser, CDP `window.__playinfo__.data.dash.audio[0].baseUrl` (or `base_url`), then:

```
python .cursor/skills/video-bgm-id/scripts/identify.py --audio-url "<baseUrl>" --referer "<watch URL>" --id BV...
```

3. Report **title + artist + Shazam URL**. Empty `matches` → say unknown; do not invent a song.
4. `python cron/janitor.py --touch`

Several 15–20s windows plus the full clip. One window matching is enough if title repeats.

## Hard

- MEDIA bytes stay in `tmp/bgm-id/`. Do not commit wav/m4s/mp4.
- Do not dump lyrics. Do not claim a license or that the UP cleared the track.
- Do not treat the Bilibili search-box placeholder as the song.
- Comments/简介 are hints only; fingerprint wins.
- YouTube/Bilibili masters are for identify, not for muxing into another cut (`stage-body-composite` still forbids that).

Browser playinfo details: [reference.md](reference.md).
