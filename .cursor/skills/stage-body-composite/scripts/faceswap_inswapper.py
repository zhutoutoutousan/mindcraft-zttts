#!/usr/bin/env python3
"""Neural identity swap via InsightFace INSwapper (not affine paste)."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ffmpeg_bin import duration_sec, ffmpeg_exe, run  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
os.environ.setdefault("INSIGHTFACE_ROOT", str(Path.home() / ".insightface"))


def load_swapper():
    from insightface.app import FaceAnalysis
    from insightface.model_zoo import get_model

    app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
    app.prepare(ctx_id=-1, det_size=(640, 640))
    swap_path = Path.home() / ".insightface" / "models" / "inswapper_128.onnx"
    if not swap_path.exists():
        from insightface.utils.storage import download_onnx

        download_onnx(
            "models",
            "inswapper_128.onnx",
            root=str(Path.home() / ".insightface"),
            download_zip=False,
        )
    swapper = get_model(str(swap_path), download=False, providers=["CPUExecutionProvider"])
    if swapper is None:
        raise SystemExit("failed to load inswapper_128.onnx")
    return app, swapper


def biggest(faces):
    if not faces:
        return None
    return max(faces, key=lambda f: (f.bbox[2] - f.bbox[0]) * (f.bbox[3] - f.bbox[1]))


def extract_frame(src: Path, dest: Path, t: float) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-ss",
            f"{t:.3f}",
            "-i",
            str(src),
            "-frames:v",
            "1",
            "-update",
            "1",
            str(dest),
        ]
    )


def extract_span(src: Path, dest_dir: Path, fps: int, seconds: float) -> list[Path]:
    dest_dir.mkdir(parents=True, exist_ok=True)
    for old in dest_dir.glob("*.png"):
        old.unlink()
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(src),
            "-vf",
            f"fps={fps}",
            "-t",
            f"{seconds:.3f}",
            str(dest_dir / "%06d.png"),
        ]
    )
    frames = sorted(dest_dir.glob("*.png"))
    if not frames:
        raise SystemExit(f"no frames from {src}")
    return frames


def encode(frames_dir: Path, dest: Path, fps: int) -> None:
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
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


def mux_audio(silent: Path, src: Path, dest: Path, seconds: float) -> None:
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(silent),
            "-i",
            str(src),
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
            "-movflags",
            "+faststart",
            "-t",
            f"{seconds:.3f}",
            "-shortest",
            str(dest),
        ]
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default="friend-wine")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--t0", type=float, default=4.0)
    ap.add_argument("--fps", type=int, default=15)
    ap.add_argument("--max-seconds", type=float, default=15.0)
    ap.add_argument("--face", default="")
    ap.add_argument("--dancer", default="")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    base = ROOT / "tmp" / args.slug
    indir = base / "_in"
    work = base / "_work"
    work.mkdir(parents=True, exist_ok=True)
    face_path = Path(args.face) if args.face else indir / "face.jpg"
    dancer = Path(args.dancer) if args.dancer else indir / "dancer.mp4"
    if not face_path.exists():
        raise SystemExit(f"need {face_path}")
    if not dancer.exists():
        raise SystemExit(f"need {dancer}")

    print("loading buffalo_l + inswapper (first run downloads weights)")
    app, swapper = load_swapper()
    src = cv2.imread(str(face_path))
    if src is None:
        raise SystemExit(f"cannot read {face_path}")
    src_faces = app.get(src)
    source = biggest(src_faces)
    if source is None:
        raise SystemExit("no face in source still")
    print("source identity locked")

    extract_frame(dancer, work / "inswap_plate.png", args.t0)
    plate = cv2.imread(str(work / "inswap_plate.png"))
    if plate is None:
        raise SystemExit("failed to extract dancer frame")
    dst_faces = app.get(plate)
    target = biggest(dst_faces)
    if target is None:
        raise SystemExit(f"no face in dancer at t={args.t0}")
    preview = swapper.get(plate, target, source, paste_back=True)
    out_prev = work / "inswap_preview.png"
    cv2.imwrite(str(out_prev), preview)
    print(f"preview → {out_prev}")
    if args.preview:
        return 0

    seconds = min(args.max_seconds, duration_sec(dancer) or args.max_seconds)
    frames = extract_span(dancer, work / "inswap_raw", args.fps, seconds)
    out_dir = work / "inswap_comp"
    if out_dir.exists():
        for p in out_dir.glob("*.png"):
            p.unlink()
    else:
        out_dir.mkdir()

    last = target
    n = len(frames)
    for i, fp in enumerate(frames, start=1):
        bgr = cv2.imread(str(fp))
        faces = app.get(bgr)
        hit = biggest(faces)
        if hit is not None:
            last = hit
        if last is None:
            swapped = bgr
        else:
            swapped = swapper.get(bgr, last, source, paste_back=True)
        cv2.imwrite(str(out_dir / f"{i:06d}.png"), swapped)
        if i == 1 or i % 10 == 0 or i == n:
            print(f"inswap {i}/{n}")

    silent = work / "inswap_silent.mp4"
    encode(out_dir, silent, args.fps)
    dest = Path(args.out) if args.out else base / "dancer-face.mp4"
    mux_audio(silent, dancer, dest, seconds)
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
