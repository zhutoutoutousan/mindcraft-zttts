# Lyric parody — job JSON + mix

## job.json

```json
{
  "slug": "donut-wang",
  "tune": "title — artist",
  "lang": "zh",
  "voice": "zh-CN-YunxiNeural",
  "audio": "tmp/foo.mp3",
  "lines": [
    {"n": 7, "text": "邯郸降世华北吴", "t0": 12.40, "t1": 15.10},
    {"n": 7, "text": "半盒十金店员赠", "flex": false}
  ]
}
```

| Field | Need |
| --- | --- |
| `tune` | Title + artist, no lyric body |
| `lang` | `zh` / `en` / `de` |
| `lines[].n` | Skeleton length the parody must match |
| `lines[].text` | New words |
| `lines[].t0` `t1` | Mix timestamps (seconds). Omit if lyrics-only |
| `lines[].flex` | Allow ±1 字/syllable |
| `audio` | Local path for `mix.py` |
| `voice` | edge-tts voice |

`meter.py` prints `OK` or lists `line i expected n got m`.

## Counting

- ZH: `\u4e00-\u9fff` plus `0-9A-Za-z` as one unit each. Skip `，。！？、；：…—-·,.!? ` and quotes.
- EN/DE: lowercase, split on `[^a-zäöüß]+`, then vowel groups (`[aeiouyäöü]+`). Silent `e` at end of 2+ letter English words still counts as a syllable here (keep it simple). `n` is that count.

Write the skeleton from a local listen / Whisper alignment **in memory**. Persist only `n` and times.

## Alignment without cues

`mix.py` transcribes the **vocals** stem, groups tokens with pause > 0.35s into lines, writes `n`+`t0`+`t1` (no original words) into `tmp/lyric-parody/<slug>/cues.json`. Then pair by index with `lines[].text`. Line-count mismatch → take `min`, warn, do not invent extra melody.

## F0 follow

For each cue: slice original vocals → `harvest` F0. TTS the parody line → `atempo` to cue length → WORLD `cheaptrick`/`d4c` on the TTS → `synthesize` with the **original F0** resampled onto the TTS frames. Overlay onto silence, `amix` with `no_vocals`.

If `pyworld` missing, refuse the mix (speech-only overlay is not 曲调不变). If `demucs` missing, refuse the mix.

## Voices

| lang | default |
| --- | --- |
| zh | `zh-CN-YunxiNeural` |
| de | `de-DE-ConradNeural` |
| en | `en-US-GuyNeural` |

Do not send SSML `<speak>` into edge-tts.

## Example meter (invented, not a real song)

```
n: 7 / 7 / 8 / 8
parody:
  盘古开口其形圆
  尧舜禅让半盒甜
  张骞凿空走线去
  店员多赠封神年
```
