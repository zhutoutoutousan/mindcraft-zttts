#!/usr/bin/env python3
"""Matte dancer onto concert plate + mux song. See ../SKILL.md."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ffmpeg_bin import duration_sec as probe_duration  # noqa: E402
from ffmpeg_bin import ffmpeg_exe, run, video_size  # noqa: E402
from matte import matte_png  # noqa: E402

VIDEO_EXTS = {".mp4", ".mov", ".webm", ".mkv", ".avi"}
AUDIO_EXTS = {".m4a", ".mp3", ".wav", ".aac", ".flac", ".ogg", ".mp4", ".mkv", ".webm"}


def find_one(folder: Path, names: list[str], exts: set[str]) -> Path | None:
    if not folder.exists():
        return None
    for n in names:
        for ext in exts:
            p = folder / f"{n}{ext}"
            if p.exists():
                return p
    for p in sorted(folder.iterdir()):
        if p.suffix.lower() in exts and p.stem.split(".")[0] in names:
            return p
    return None


def link_or_copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return
    try:
        os.link(src, dest)
    except OSError:
        shutil.copy2(src, dest)


def ensure_inputs(indir: Path, staging: Path) -> None:
    pairs = (
        ("dancer", VIDEO_EXTS),
        ("plate", VIDEO_EXTS),
        ("song", AUDIO_EXTS),
    )
    for name, exts in pairs:
        if find_one(indir, [name], exts):
            continue
        src = find_one(staging, [name], exts)
        if src is None:
            continue
        link_or_copy(src, indir / src.name)


def missing_report(indir: Path) -> list[str]:
    need = []
    if find_one(indir, ["dancer"], VIDEO_EXTS) is None:
        need.append("dancer.mp4  — person to cut out")
    if find_one(indir, ["plate"], VIDEO_EXTS) is None:
        need.append("plate.mp4   — concert plate (singer standing)")
    if find_one(indir, ["song"], AUDIO_EXTS) is None:
        need.append("song.m4a / song.mp4  — replacement audio")
    return need


def vf_chain(fps: int | None, scale: tuple[int, int] | None) -> str | None:
    parts = []
    if fps:
        parts.append(f"fps={fps}")
    if scale:
        parts.append(f"scale={scale[0]}:{scale[1]}:flags=lanczos")
    return ",".join(parts) if parts else None


def extract_frame(
    src: Path,
    dest: Path,
    t: float = 0.0,
    scale: tuple[int, int] | None = None,
) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [ffmpeg_exe(), "-y", "-ss", f"{t:.3f}", "-i", str(src)]
    vf = vf_chain(None, scale)
    if vf:
        cmd += ["-vf", vf]
    cmd += ["-frames:v", "1", "-update", "1", str(dest)]
    run(cmd)


def sr_to_canvas(src_png: Path, dest_png: Path, canvas: tuple[int, int]) -> None:
    from enhance_hd import sr_folder

    work = dest_png.parent
    one_in = work / "_sr_one_in"
    one_out = work / "_sr_one_out"
    if one_in.exists():
        shutil.rmtree(one_in)
    if one_out.exists():
        shutil.rmtree(one_out)
    one_in.mkdir()
    shutil.copy2(src_png, one_in / "000001.png")
    sr_folder(one_in, one_out, "realesr-animevideov3", 4)
    hits = sorted(one_out.glob("*.png"))
    if not hits:
        raise SystemExit("plate SR failed")
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(hits[0]),
            "-vf",
            f"scale={canvas[0]}:{canvas[1]}:flags=lanczos",
            "-frames:v",
            "1",
            "-update",
            "1",
            str(dest_png),
        ]
    )


def sr_span_to_canvas(src_dir: Path, dest_dir: Path, canvas: tuple[int, int]) -> list[Path]:
    from enhance_hd import sr_folder

    sr_dir = src_dir.parent / (src_dir.name + "_sr")
    sr_folder(src_dir, sr_dir, "realesr-animevideov3", 4)
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True)
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(sr_dir / "%06d.png"),
            "-vf",
            f"scale={canvas[0]}:{canvas[1]}:flags=lanczos",
            str(dest_dir / "%06d.png"),
        ]
    )
    frames = sorted(dest_dir.glob("*.png"))
    if not frames:
        raise SystemExit("no HD plate frames")
    return frames


def duration_sec(src: Path) -> float:
    return probe_duration(src)


def load_bbox(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for k in ("x", "y", "w", "h"):
        if k not in data:
            raise SystemExit(f"bbox.json missing {k}")
    out = {k: int(data[k]) for k in ("x", "y", "w", "h")}
    if "plate_start" in data:
        out["plate_start"] = float(data["plate_start"])
    canvas = data.get("canvas")
    if isinstance(canvas, list) and len(canvas) == 2:
        out["canvas"] = (int(canvas[0]), int(canvas[1]))
    if isinstance(data.get("cover"), dict):
        cover = {k: int(data["cover"][k]) for k in ("x", "y", "w", "h")}
        if "sample_x" in data["cover"]:
            cover["sample_x"] = int(data["cover"]["sample_x"])
            cover["sample_y"] = int(data["cover"]["sample_y"])
        out["cover"] = cover
    return out


def crop_fg(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    alpha = im.split()[-1].point(lambda p: 255 if p > 20 else 0)
    box = alpha.getbbox()
    if not box:
        return im
    return im.crop(box)


def hide_singer(
    plate: Image.Image,
    bbox: dict,
    person_alpha: Image.Image | None = None,
    pad: int = 16,
) -> Image.Image:
    """Stamp wood grain only where the concert singer stood."""
    import cv2
    import numpy as np

    rgb = np.array(plate.convert("RGB"))
    h, w = rgb.shape[:2]
    if person_alpha is not None:
        rgba = person_alpha.convert("RGBA")
        mask = np.array(rgba.split()[-1])
        if mask.shape[0] != h or mask.shape[1] != w:
            mask = cv2.resize(mask, (w, h), interpolation=cv2.INTER_NEAREST)
        mask = cv2.dilate(mask, np.ones((21, 21), np.uint8), iterations=2)
        mask = cv2.GaussianBlur(mask, (31, 31), 0)
        _, mask = cv2.threshold(mask, 24, 255, cv2.THRESH_BINARY)
        box = bbox.get("cover") or bbox
        x, y, bw, bh = int(box["x"]), int(box["y"]), int(box["w"]), int(box["h"])
        gate = np.zeros_like(mask)
        cv2.rectangle(
            gate,
            (max(0, x - 40), max(0, y - 20)),
            (min(w - 1, x + bw + 40), min(h - 1, y + bh + 20)),
            255,
            -1,
        )
        mask = cv2.bitwise_and(mask, gate)
        mask = cv2.GaussianBlur(mask, (15, 15), 0)
    else:
        box = bbox.get("cover") or bbox
        x, y, bw, bh = int(box["x"]), int(box["y"]), int(box["w"]), int(box["h"])
        mask = np.zeros((h, w), np.uint8)
        cv2.rectangle(
            mask,
            (max(0, x - pad), max(0, y - pad)),
            (min(w - 1, x + bw + pad), min(h - 1, y + bh + pad)),
            255,
            -1,
        )
        mask = cv2.GaussianBlur(mask, (41, 41), 0)
    sx = int((bbox.get("cover") or bbox).get("sample_x") or int(w * 0.88))
    sx = int(np.clip(sx, 0, max(0, w - 40)))
    strip = rgb[:, sx : sx + 36]
    if strip.size == 0:
        return plate.convert("RGBA")
    wood = np.tile(strip, (1, int(np.ceil(w / max(1, strip.shape[1]))) + 1, 1))[:, :w]
    wood = cv2.GaussianBlur(wood, (11, 5), 0)
    a = (mask.astype(np.float32) / 255.0)[:, :, None]
    hole = (mask > 80).astype(np.uint8)
    filled = cv2.inpaint(rgb, hole, 10, cv2.INPAINT_TELEA) if int(hole.sum()) > 40 else rgb
    mixed = (filled.astype(np.float32) * a + rgb.astype(np.float32) * (1.0 - a)).astype(np.uint8)
    return Image.fromarray(mixed).convert("RGBA")


def paste_on_plate(
    plate: Image.Image,
    matte: Image.Image,
    bbox: dict,
    person_alpha: Image.Image | None = None,
) -> Image.Image:
    out = hide_singer(plate, bbox, person_alpha=person_alpha)
    fg = crop_fg(matte)
    if fg.size[1] != bbox["h"] and fg.size[1] > 0:
        ratio = bbox["h"] / fg.size[1]
        fg = fg.resize((max(1, int(fg.size[0] * ratio)), bbox["h"]), Image.Resampling.LANCZOS)
    cx = bbox["x"] + bbox["w"] // 2
    x = cx - fg.size[0] // 2
    y = bbox["y"] + bbox["h"] - fg.size[1]
    # clip overlay to canvas (PIL alpha_composite rejects negative dest)
    px, py = 0, 0
    if x < 0:
        fg = fg.crop((-x, 0, fg.size[0], fg.size[1]))
        x = 0
    if y < 0:
        fg = fg.crop((0, -y, fg.size[0], fg.size[1]))
        y = 0
    if x + fg.size[0] > out.size[0]:
        fg = fg.crop((0, 0, out.size[0] - x, fg.size[1]))
    if y + fg.size[1] > out.size[1]:
        fg = fg.crop((0, 0, fg.size[0], out.size[1] - y))
    if fg.size[0] > 0 and fg.size[1] > 0:
        out.alpha_composite(fg, (x + px, y + py))
    return out.convert("RGB")


def extract_span(
    src: Path,
    dest_dir: Path,
    fps: int,
    seconds: float,
    start: float = 0.0,
    scale: tuple[int, int] | None = None,
) -> list[Path]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    for old in dest_dir.glob("*.png"):
        old.unlink()
    cmd = [ffmpeg_exe(), "-y"]
    if start > 0:
        cmd += ["-ss", f"{start:.3f}"]
    cmd += ["-i", str(src), "-vf", vf_chain(fps, scale) or f"fps={fps}", "-t", f"{seconds:.3f}", str(dest_dir / "%06d.png")]
    run(cmd)
    frames = sorted(dest_dir.glob("*.png"))
    if not frames:
        raise SystemExit(f"no frames from {src}")
    return frames


def loop_pick(frames: list[Path], i: int) -> Path:
    return frames[i % len(frames)]


def encode_silent(frames_dir: Path, dest: Path, fps: int) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-framerate",
            str(fps),
            "-i",
            str(frames_dir / "%06d.png"),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-an",
            str(dest),
        ]
    )


def mux_song(silent: Path, song: Path, dest: Path, seconds: float, song_start: float = 0.0) -> None:
    fade_out = max(0.0, seconds - 0.3)
    cmd = [ffmpeg_exe(), "-y", "-i", str(silent)]
    if song_start > 0:
        cmd += ["-ss", f"{song_start:.3f}"]
    cmd += [
        "-i",
        str(song),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-af",
        f"volume=8dB,afade=t=in:st=0:d=0.05,afade=t=out:st={fade_out:.3f}:d=0.3",
        "-t",
        f"{seconds:.3f}",
        "-shortest",
        "-movflags",
        "+faststart",
        str(dest),
    ]
    run(cmd)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default="friend-wine")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--max-seconds", type=float, default=20.0)
    ap.add_argument("--fps", type=int, default=15)
    ap.add_argument("--t0", type=float, default=4.0, help="preview timestamp on dancer; plate uses plate_start+t0")
    ap.add_argument("--dancer", default="", help="override dancer video path")
    ap.add_argument("--song-start", type=float, default=6.0, help="skip quiet intro on song.mp4")
    ap.add_argument("--audio", default="", help="override muxed audio (wav/m4a/mp4)")
    ap.add_argument("--plate-sr", action="store_true", help="Real-ESRGAN plate frames to canvas")
    args = ap.parse_args()

    base = ROOT / "tmp" / args.slug
    indir = base / "_in"
    work = base / "_work"
    indir.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)
    ensure_inputs(indir, ROOT / "tmp")

    missing = missing_report(indir)
    dancer = Path(args.dancer) if args.dancer else find_one(indir, ["dancer"], VIDEO_EXTS)
    plate = find_one(indir, ["plate"], VIDEO_EXTS)
    song = find_one(indir, ["song"], AUDIO_EXTS)
    if args.dancer:
        dancer = Path(args.dancer)
        if not dancer.exists():
            raise SystemExit(f"dancer not found: {dancer}")
    if missing:
        print("Need in " + str(indir).replace("\\", "/") + ":")
        for line in missing:
            print("  " + line)
        print("I will not download these.")
        return 2

    assert dancer and plate and song
    bbox_path = indir / "bbox.json"
    if not bbox_path.exists():
        print("Write tmp/{}/_in/bbox.json with {{x,y,w,h}} then rerun --preview.".format(args.slug))
        return 2
    bbox = load_bbox(bbox_path)
    scale = bbox.get("canvas")
    plate_start = float(bbox.get("plate_start") or 0.0)
    plate_t = plate_start + args.t0

    plate0 = work / "plate0.png"
    if args.plate_sr and scale:
        raw0 = work / "plate0_raw.png"
        extract_frame(plate, raw0, t=plate_t)
        sr_to_canvas(raw0, plate0, scale)
    else:
        extract_frame(plate, plate0, t=plate_t, scale=scale)
    pw, ph = video_size(plate)
    print(f"plate native {pw}x{ph}  start={plate_start}s  frame@{plate_t:.1f}s → {plate0}")
    if scale:
        print(f"canvas {scale[0]}x{scale[1]}")

    extract_frame(dancer, work / "dancer0.png", t=args.t0)
    matte0 = work / "dancer0_matte.png"
    matte_png(work / "dancer0.png", matte0)
    plate_person = work / "plate0_person.png"
    matte_png(plate0, plate_person, model="u2net_human_seg")
    preview = work / "preview.png"
    paste_on_plate(
        Image.open(plate0),
        Image.open(matte0),
        bbox,
        person_alpha=Image.open(plate_person),
    ).save(preview)
    print(f"preview → {preview}")
    if args.preview:
        return 0

    seconds = min(args.max_seconds, duration_sec(song) or args.max_seconds)
    if seconds <= 0:
        seconds = args.max_seconds

    dancer_frames = extract_span(dancer, work / "dancer_raw", args.fps, seconds)
    if args.plate_sr and scale:
        plate_native_dir = work / "plate_raw"
        extract_span(plate, plate_native_dir, args.fps, seconds, start=plate_start)
        plate_frames = sr_span_to_canvas(plate_native_dir, work / "plate_hd", scale)
    else:
        plate_frames = extract_span(
            plate, work / "plate_raw", args.fps, seconds, start=plate_start, scale=scale
        )

    matte_dir = work / "dancer_matte"
    matte_dir.mkdir(exist_ok=True)
    matte_cache: dict[Path, Path] = {}
    n = int(round(seconds * args.fps))
    out_dir = work / "comp"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir()

    plate_matte_dir = work / "plate_person"
    plate_matte_dir.mkdir(exist_ok=True)
    plate_matte_cache: dict[Path, Path] = {}

    for i in range(n):
        dpath = loop_pick(dancer_frames, i)
        if dpath not in matte_cache:
            dest = matte_dir / dpath.name
            matte_png(dpath, dest)
            matte_cache[dpath] = dest
        ppath = loop_pick(plate_frames, i)
        if ppath not in plate_matte_cache:
            pdest = plate_matte_dir / ppath.name
            matte_png(ppath, pdest, model="u2net_human_seg")
            plate_matte_cache[ppath] = pdest
        frame = paste_on_plate(
            Image.open(ppath),
            Image.open(matte_cache[dpath]),
            bbox,
            person_alpha=Image.open(plate_matte_cache[ppath]),
        )
        frame.save(out_dir / f"{i + 1:06d}.png")
        if (i + 1) % 15 == 0 or i == 0:
            print(f"composite {i + 1}/{n}")

    silent = work / "silent.mp4"
    encode_silent(out_dir, silent, args.fps)
    dest = base / f"{args.slug}.mp4"
    audio = Path(args.audio) if args.audio else song
    if args.audio and not audio.exists():
        raise SystemExit(f"audio not found: {audio}")
    song_start = 0.0 if args.audio else args.song_start
    mux_song(silent, audio, dest, seconds, song_start=song_start)
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
