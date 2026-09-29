#!/usr/bin/env python3
"""Paste a still face onto dancer.mp4 using YuNet 5-point align. See ../SKILL.md."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ffmpeg_bin import duration_sec, ffmpeg_exe, run  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]
MODEL = Path(__file__).resolve().parent / "models" / "face_detection_yunet_2023mar.onnx"


def yunet(size: tuple[int, int], score: float = 0.45) -> cv2.FaceDetectorYN:
    if not MODEL.exists():
        raise SystemExit(f"missing YuNet model: {MODEL}")
    det = cv2.FaceDetectorYN_create(str(MODEL), "", size, score, 0.3, 5000)
    return det


def detect_faces(det: cv2.FaceDetectorYN, bgr: np.ndarray) -> np.ndarray:
    h, w = bgr.shape[:2]
    det.setInputSize((w, h))
    _ok, faces = det.detect(bgr)
    if faces is None or len(faces) == 0:
        return np.zeros((0, 15), dtype=np.float32)
    faces = faces[faces[:, -1] >= 0.7]
    if len(faces) == 0:
        return np.zeros((0, 15), dtype=np.float32)
    return faces


def largest(faces: np.ndarray) -> np.ndarray:
    areas = faces[:, 2] * faces[:, 3]
    return faces[int(np.argmax(areas))]


def pts5(face: np.ndarray) -> np.ndarray:
    return face[4:14].reshape(5, 2).astype(np.float32)


def face_mask(shape: tuple[int, int], box: np.ndarray, scale: float = 1.0) -> np.ndarray:
    h, w = shape[:2]
    x, y, bw, bh = [float(v) for v in box[:4]]
    mask = np.zeros((h, w), dtype=np.uint8)
    cx = int(x + bw * 0.5)
    cy = int(y + bh * 0.52)
    ax = max(8, int(bw * 0.55 * scale))
    ay = max(10, int(bh * 0.68 * scale))
    cv2.ellipse(mask, (cx, cy), (ax, ay), 0, 0, 360, 255, -1)
    k = max(7, int(min(bw, bh) * 0.18) | 1)
    mask = cv2.GaussianBlur(mask, (k, k), 0)
    return mask


def cutout_face(bgr: np.ndarray, face: np.ndarray) -> np.ndarray:
    mask = face_mask(bgr.shape, face, scale=1.05)
    out = bgr.copy()
    out[mask < 24] = 0
    return out


def swap_frame(
    src_bgr: np.ndarray,
    src_pts: np.ndarray,
    dst_bgr: np.ndarray,
    dst_face: np.ndarray,
) -> np.ndarray:
    dst_pts = pts5(dst_face)
    m, _ = cv2.estimateAffinePartial2D(src_pts, dst_pts, method=cv2.LMEDS)
    if m is None:
        return dst_bgr
    h, w = dst_bgr.shape[:2]
    warped = cv2.warpAffine(
        src_bgr,
        m,
        (w, h),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0, 0, 0),
    )
    mask = face_mask((h, w), dst_face, scale=1.0)
    warped_ok = (warped.sum(axis=2) > 12).astype(np.uint8) * 255
    mask = cv2.bitwise_and(mask, warped_ok)
    ys, xs = np.where(mask > 16)
    if len(xs) < 20:
        return dst_bgr
    cx, cy = int(xs.mean()), int(ys.mean())
    try:
        return cv2.seamlessClone(warped, dst_bgr, mask, (cx, cy), cv2.NORMAL_CLONE)
    except cv2.error:
        alpha = (mask.astype(np.float32) / 255.0)[:, :, None]
        mixed = warped.astype(np.float32) * alpha + dst_bgr.astype(np.float32) * (1.0 - alpha)
        return mixed.astype(np.uint8)


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
    ap.add_argument("--face", default="", help="still to paste; default tmp/<slug>/_in/face.jpg")
    ap.add_argument("--dancer", default="", help="override dancer.mp4")
    ap.add_argument("--out", default="", help="output mp4; default dancer-face.mp4")
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

    src_bgr = cv2.imread(str(face_path))
    if src_bgr is None:
        raise SystemExit(f"cannot read {face_path}")
    src_det = yunet((src_bgr.shape[1], src_bgr.shape[0]))
    src_faces = detect_faces(src_det, src_bgr)
    if len(src_faces) == 0:
        raise SystemExit("no face in face.jpg")
    src_face = largest(src_faces)
    src_pts = pts5(src_face)
    src_bgr = cutout_face(src_bgr, src_face)
    print(f"source face {face_path.name} landmarks ok")

    extract_frame(dancer, work / "face_plate.png", args.t0)
    plate = cv2.imread(str(work / "face_plate.png"))
    if plate is None:
        raise SystemExit("failed to extract dancer frame")
    dst_det = yunet((plate.shape[1], plate.shape[0]))
    dst_faces = detect_faces(dst_det, plate)
    if len(dst_faces) == 0:
        raise SystemExit(f"no face in dancer at t={args.t0}")
    preview = swap_frame(src_bgr, src_pts, plate, largest(dst_faces))
    out_prev = work / "face_preview.png"
    cv2.imwrite(str(out_prev), preview)
    print(f"preview → {out_prev}")
    if args.preview:
        return 0

    seconds = min(args.max_seconds, duration_sec(dancer) or args.max_seconds)
    frames = extract_span(dancer, work / "face_raw", args.fps, seconds)
    out_dir = work / "face_comp"
    if out_dir.exists():
        for p in out_dir.glob("*.png"):
            p.unlink()
    else:
        out_dir.mkdir()

    last = None
    n = len(frames)
    for i, fp in enumerate(frames, start=1):
        bgr = cv2.imread(str(fp))
        faces = detect_faces(dst_det, bgr)
        if len(faces):
            last = largest(faces)
        if last is None:
            swapped = bgr
        else:
            swapped = swap_frame(src_bgr, src_pts, bgr, last)
        cv2.imwrite(str(out_dir / f"{i:06d}.png"), swapped)
        if i == 1 or i % 15 == 0 or i == n:
            print(f"faceswap {i}/{n}")

    silent = work / "face_silent.mp4"
    encode(out_dir, silent, args.fps)
    dest = Path(args.out) if args.out else base / "dancer-face.mp4"
    mux_audio(silent, dancer, dest, seconds)
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
