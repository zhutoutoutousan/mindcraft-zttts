# Bilibili 412 + playinfo

Direct `yt-dlp` / `api.bilibili.com` from this agent IP often returns **HTTP 412** (security control). The Cursor browser tab usually already has `__playinfo__`.

## CDP

```js
(() => {
  const play = window.__playinfo__ || {};
  const dash = play.data?.dash || play.result?.dash || {};
  const a = (dash.audio || [])[0] || {};
  const v = (window.__INITIAL_STATE__ || {}).videoData || {};
  return {
    bvid: v.bvid,
    title: v.title,
    owner: v.owner?.name,
    duration: v.duration,
    audioUrl: a.baseUrl || a.base_url,
  };
})()
```

`audioUrl` is a signed m4s. Pass it as `--audio-url` with `--referer` set to the watch URL. Deadline query params expire; re-read `__playinfo__` if curl 403s.

## yt-dlp

When 412 is gone, `identify.py --url` uses yt-dlp audio-only. Do not upgrade yt-dlp unless asked.

## Windows

Use `curl.exe`, not PowerShell `curl`. ffmpeg via `imageio_ffmpeg.get_ffmpeg_exe()`.
