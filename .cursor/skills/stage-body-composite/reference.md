# Stage body composite — recipes

## bbox.json

Pixels on the **plate** frame (not the dancer). Example for 1920×1080, tenor standing center-right:

```json
{"x": 780, "y": 160, "w": 420, "h": 860}
```

`build.py --preview` prints plate size. Open `_work/plate0.png`, measure the singer, rewrite bbox, preview again.

Scale rule: dancer alpha canvas is resized so **height = bbox.h**. Horizontal center of the matte lands on `x + w/2`. Feet sit on `y + h`.

## ffmpeg cheap path (already-matted dancer)

If `dancer.webm` / `dancer.mov` already has alpha:

```
ffmpeg -i plate.mp4 -c:v libvpx-vp9 -i dancer.webm -filter_complex "[1:v]scale=-1:860[fg];[0:v][fg]overlay=780:160:shortest=1[v]" -map "[v]" -an -t 20 silent.mp4
ffmpeg -i silent.mp4 -i song.m4a -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest -t 20 out.mp4
```

Windows: use `imageio_ffmpeg.get_ffmpeg_exe()` (same as the TTS kit). Do not assume `ffmpeg` is on PATH.

## Matte (no alpha on dancer)

Default in `scripts/matte.py`: `rembg` session `u2net_human_seg`. First run downloads the weights (not a song).

```
pip install rembg pillow imageio-ffmpeg onnxruntime
```

If CUDA is present, `onnxruntime-gpu` is optional. CPU is the default.

Erode alpha 1–2 px after rembg to kill green/halo fringe.

Do **not** batch `GenerateImage`. Do **not** scrape stock sites for a fake Pavarotti.

## Tracked box (rung 2)

Only if the tenor walks. OpenCV HOG / a local YOLO weights file the human already has. Do not download a new detector "to be helpful" in a foggy turn. Write `_work/bbox_track.jsonl` (`t,x,y,w,h`) and feed composite.

## Mouth keep (rung 3)

After overlay, copy plate pixels inside an ellipse near the top-third of bbox (mouth). This keeps a tenor-mouth read without a lip-sync model. MuseTalk / Wav2Lip stay **off** unless named.

## Audio

- `-map` song only. `-shortest` or `--max-seconds`.
- Soft fade 0.3 s in/out on audio.
- Do not beat-align unless the human names a downbeat list.

## Portrait

Pavarotti plates are usually 16:9. Douyin: crop around bbox (`crop=w:h:x:y` then scale 1080×1920), keep type out of top 12% / bottom 18% if any caption is burnt. Default master is 16:9.

## Missing files — agent copy

```
Need in tmp/friend-wine/_in/:
  dancer.mp4  — 许家印跳舞 (or named dancer)
  plate.mp4   — 帕瓦罗蒂 concert plate
  song.m4a    — 朋友的酒 audio
  bbox.json   — after plate0.png exists
I will not download these.
```
