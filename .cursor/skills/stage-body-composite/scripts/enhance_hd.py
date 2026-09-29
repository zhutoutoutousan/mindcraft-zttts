#!/usr/bin/env python3
"""Delogo corner marks then Real-ESRGAN to 1920x1080. See ../SKILL.md."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.request import urlopen

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ffmpeg_bin import duration_sec, ffmpeg_exe, run, video_size  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
ZIP_URL = (
    "https://github.com/xinntao/Real-ESRGAN/releases/download/"
    "v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip"
)

# 1024x576 dancer / face / tomb (Bilibili + 千问)
DELOGO_1024 = (
    "delogo=x=8:y=8:w=252:h=54:show=0,"
    "delogo=x=828:y=508:w=192:h=64:show=0"
)


def tool_dir() -> Path:
    return ROOT / "tmp" / "friend-wine" / "_tools" / "realesrgan"


def esrgan_exe() -> Path:
    hits = list(tool_dir().rglob("realesrgan-ncnn-vulkan.exe"))
    if hits:
        return hits[0]
    dest = tool_dir()
    dest.mkdir(parents=True, exist_ok=True)
    zpath = dest / "realesrgan-windows.zip"
    print(f"download {ZIP_URL}")
    with urlopen(ZIP_URL, timeout=120) as r, zpath.open("wb") as f:
        shutil.copyfileobj(r, f)
    with zipfile.ZipFile(zpath) as zf:
        zf.extractall(dest)
    hits = list(dest.rglob("realesrgan-ncnn-vulkan.exe"))
    if not hits:
        raise SystemExit("realesrgan exe missing after unzip")
    return hits[0]


def delogo_filter(w: int, h: int) -> str | None:
    # Only the rooftop dancer family carries Bilibili + 千问 corners.
    if w == 1024 and h == 576:
        return DELOGO_1024
    return None


def extract_pngs(src: Path, dest: Path, vf: str | None) -> list[Path]:
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    cmd = [ffmpeg_exe(), "-y", "-loglevel", "error", "-i", str(src)]
    if vf:
        cmd += ["-vf", vf]
    cmd += [str(dest / "%06d.png")]
    run(cmd)
    frames = sorted(dest.glob("*.png"))
    if not frames:
        raise SystemExit(f"no frames from {src}")
    return frames


def sr_folder(src_dir: Path, dest_dir: Path, model: str, scale: int) -> None:
    if dest_dir.exists():
        shutil.rmtree(dest_dir)
    dest_dir.mkdir(parents=True)
    exe = esrgan_exe()
    cmd = [
        str(exe),
        "-i",
        str(src_dir),
        "-o",
        str(dest_dir),
        "-n",
        model,
        "-s",
        str(scale),
        "-f",
        "png",
        "-g",
        "0",
        "-j",
        "1:2:2",
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True, cwd=str(exe.parent))


def encode_hd(frames: Path, audio: Path, dest: Path, fps: float, seconds: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    silent = dest.with_name(dest.stem + "_silent.mp4")
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-framerate",
            f"{fps:.4f}",
            "-i",
            str(frames / "%06d.png"),
            "-vf",
            "scale=1920:1080:flags=lanczos:force_original_aspect_ratio=decrease,"
            "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
            "-c:v",
            "libx264",
            "-preset",
            "slow",
            "-crf",
            "16",
            "-an",
            str(silent),
        ]
    )
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(silent),
            "-i",
            str(audio),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0?",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-t",
            f"{seconds:.3f}",
            "-shortest",
            "-movflags",
            "+faststart",
            str(dest),
        ]
    )
    silent.unlink(missing_ok=True)


def preview_one(src: Path, work: Path, model: str, scale: int) -> Path:
    w, h = video_size(src)
    vf = delogo_filter(w, h)
    raw = work / "hd_preview_in.png"
    out = work / "hd_preview.png"
    cmd = [ffmpeg_exe(), "-y", "-loglevel", "error", "-ss", "4", "-i", str(src), "-frames:v", "1", "-update", "1"]
    if vf:
        cmd += ["-vf", vf]
    cmd += [str(raw)]
    run(cmd)
    sr_dir = work / "hd_preview_sr"
    if sr_dir.exists():
        shutil.rmtree(sr_dir)
    sr_dir.mkdir()
    one_in = work / "hd_preview_one"
    if one_in.exists():
        shutil.rmtree(one_in)
    one_in.mkdir()
    shutil.copy2(raw, one_in / "000001.png")
    sr_folder(one_in, sr_dir, model, scale)
    hits = sorted(sr_dir.glob("*.png"))
    if not hits:
        raise SystemExit("esrgan produced no preview")
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(hits[0]),
            "-vf",
            "scale=1920:1080:flags=lanczos",
            "-frames:v",
            "1",
            "-update",
            "1",
            str(out),
        ]
    )
    print(f"preview → {out}")
    return out


def enhance_clip(src: Path, dest: Path, work: Path, model: str, scale: int) -> None:
    w, h = video_size(src)
    seconds = duration_sec(src) or 15.0
    fps = 15.0
    info_fps = 15.0
    # keep source frame count; 15fps composites, 30fps dancer
    n_guess = max(1, int(round(seconds * 15)))
    vf = delogo_filter(w, h)
    raw = work / f"{src.stem}_clean"
    frames = extract_pngs(src, raw, vf)
    info_fps = len(frames) / seconds if seconds else 15.0
    sr = work / f"{src.stem}_sr"
    sr_folder(raw, sr, model, scale)
    encode_hd(sr, src, dest, info_fps, seconds)
    print(f"wrote {dest}  ({w}x{h} → 1920x1080, {len(frames)} frames)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default="friend-wine")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--src", default="")
    ap.add_argument("--model", default="realesr-animevideov3")
    ap.add_argument("--scale", type=int, default=2)
    args = ap.parse_args()

    base = ROOT / "tmp" / args.slug
    work = base / "_work"
    work.mkdir(parents=True, exist_ok=True)
    esrgan_exe()

    clips = []
    if args.src:
        clips = [Path(args.src)]
    else:
        clips = [
            base / "dancer-face.mp4",
            base / "dancer-tomb.mp4",
            base / "friend-wine.mp4",
        ]
    clips = [p for p in clips if p.exists()]
    if not clips:
        raise SystemExit("no clips")

    if args.preview:
        preview_one(clips[0], work, args.model, args.scale)
        return 0

    for src in clips:
        dest = base / f"{src.stem}-hd.mp4"
        print(f"enhance {src.name}")
        enhance_clip(src, dest, work, args.model, args.scale)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
