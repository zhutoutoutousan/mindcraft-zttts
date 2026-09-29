#!/usr/bin/env python3
"""Replace dancer head with a matted tombstone still. Not a face identity swap."""
from __future__ import annotations

import argparse
import math
import shutil
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ffmpeg_bin import duration_sec, ffmpeg_exe, run  # noqa: E402
from faceswap import detect_faces, encode, extract_frame, extract_span, largest, mux_audio, yunet  # noqa: E402
from matte import matte_png  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]


def cut_tomb(src: Path, dest: Path) -> Image.Image:
    """Crop the central stone, rembg, keep flowers at the plinth."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    box = (int(w * 0.26), int(h * 0.10), int(w * 0.74), int(h * 0.92))
    crop = dest.with_name("tomb_crop.png")
    im.crop(box).save(crop)
    matte_png(crop, dest)
    cut = Image.open(dest).convert("RGBA")
    a = cut.split()[-1]
    bb = a.getbbox()
    if bb:
        cut = cut.crop(bb)
        cut.save(dest)
    return cut


def neck_of(face: np.ndarray) -> tuple[float, float, float, float]:
    x, y, bw, bh = [float(v) for v in face[:4]]
    le = face[4:6]
    re = face[6:8]
    angle = math.degrees(math.atan2(float(re[1] - le[1]), float(re[0] - le[0])))
    nx = x + bw * 0.50
    ny = y + bh * 1.02
    return nx, ny, max(bw, 8.0), angle


def hide_head(bgr: np.ndarray, face: np.ndarray) -> np.ndarray:
    """Cover original skull so hair does not peek around the stone."""
    out = bgr.copy()
    x, y, bw, bh = [float(v) for v in face[:4]]
    cx = int(x + bw * 0.50)
    cy = int(y + bh * 0.38)
    ax = max(12, int(bw * 0.78))
    ay = max(16, int(bh * 0.95))
    sx = min(out.shape[1] - 2, max(1, int(x + bw * 0.50)))
    sy = min(out.shape[0] - 2, max(1, int(y + bh * 1.62)))
    color = tuple(int(v) for v in out[sy, sx])
    cv2.ellipse(out, (cx, cy), (ax, ay), 0, 0, 360, color, -1)
    return out


def paste_tomb(
    frame_bgr: np.ndarray,
    face: np.ndarray,
    tomb: Image.Image,
    scale: float,
) -> np.ndarray:
    nx, ny, bw, angle = neck_of(face)
    target_w = max(24, int(bw * scale))
    ratio = target_w / tomb.size[0]
    tw = target_w
    th = max(24, int(tomb.size[1] * ratio))
    stone = tomb.resize((tw, th), Image.Resampling.LANCZOS)
    if abs(angle) > 0.4:
        stone = stone.rotate(-angle, resample=Image.Resampling.BICUBIC, expand=True)
    base = Image.fromarray(cv2.cvtColor(hide_head(frame_bgr, face), cv2.COLOR_BGR2RGB)).convert("RGBA")
    px = int(nx - stone.size[0] * 0.50)
    py = int(ny - stone.size[1] * 0.84)
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    layer.paste(stone, (px, py), stone)
    out = Image.alpha_composite(base, layer)
    return cv2.cvtColor(np.array(out.convert("RGB")), cv2.COLOR_RGB2BGR)


def smooth(prev: np.ndarray | None, face: np.ndarray, alpha: float = 0.55) -> np.ndarray:
    if prev is None:
        return face
    out = face.copy()
    out[:4] = alpha * face[:4] + (1.0 - alpha) * prev[:4]
    out[4:14] = alpha * face[4:14] + (1.0 - alpha) * prev[4:14]
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default="friend-wine")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--t0", type=float, default=4.0)
    ap.add_argument("--fps", type=int, default=15)
    ap.add_argument("--max-seconds", type=float, default=15.0)
    ap.add_argument("--scale", type=float, default=2.55, help="tomb width vs face width")
    ap.add_argument("--tomb", default="")
    ap.add_argument("--dancer", default="")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    base = ROOT / "tmp" / args.slug
    indir = base / "_in"
    work = base / "_work"
    indir.mkdir(parents=True, exist_ok=True)
    work.mkdir(parents=True, exist_ok=True)

    tomb_src = Path(args.tomb) if args.tomb else indir / "tomb.jpg"
    dancer = Path(args.dancer) if args.dancer else indir / "dancer.mp4"
    if not tomb_src.exists():
        raise SystemExit(f"need {tomb_src}")
    if not dancer.exists():
        raise SystemExit(f"need {dancer}")

    tomb_cut = work / "tomb_cut.png"
    tomb = cut_tomb(tomb_src, tomb_cut)
    print(f"tomb cut {tomb.size[0]}x{tomb.size[1]} → {tomb_cut}")

    extract_frame(dancer, work / "tomb_plate.png", args.t0)
    plate = cv2.imread(str(work / "tomb_plate.png"))
    if plate is None:
        raise SystemExit("failed to extract dancer frame")
    det = yunet((plate.shape[1], plate.shape[0]))
    faces = detect_faces(det, plate)
    if len(faces) == 0:
        raise SystemExit(f"no face in dancer at t={args.t0}")
    preview = paste_tomb(plate, largest(faces), tomb, args.scale)
    out_prev = work / "tomb_preview.png"
    cv2.imwrite(str(out_prev), preview)
    print(f"preview → {out_prev}")
    if args.preview:
        return 0

    seconds = min(args.max_seconds, duration_sec(dancer) or args.max_seconds)
    frames = extract_span(dancer, work / "tomb_raw", args.fps, seconds)
    out_dir = work / "tomb_comp"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir()

    last = None
    n = len(frames)
    for i, fp in enumerate(frames, start=1):
        bgr = cv2.imread(str(fp))
        hits = detect_faces(det, bgr)
        if len(hits):
            last = smooth(last, largest(hits))
        if last is None:
            swapped = bgr
        else:
            swapped = paste_tomb(bgr, last, tomb, args.scale)
        cv2.imwrite(str(out_dir / f"{i:06d}.png"), swapped)
        if i == 1 or i % 15 == 0 or i == n:
            print(f"tomb {i}/{n}")

    silent = work / "tomb_silent.mp4"
    encode(out_dir, silent, args.fps)
    dest = Path(args.out) if args.out else base / "dancer-tomb.mp4"
    mux_audio(silent, dancer, dest, seconds)
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
