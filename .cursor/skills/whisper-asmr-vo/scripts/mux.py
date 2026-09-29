#!/usr/bin/env python3
"""Mux picture + whisper VO + burnt-in German ASS.

  python .cursor/skills/whisper-asmr-vo/scripts/mux.py --video clip.webm --work tmp/slug --out tmp/slug/slug.mp4
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def ffmpeg_ok(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", errors="replace")[-5000:]
        raise RuntimeError(f"ffmpeg failed ({proc.returncode}):\n{err}")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--video", required=True, type=Path)
    p.add_argument("--work", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()
    video = args.video
    vo = args.work / "voiceover.wav"
    ass = args.work / "captions.de.ass"
    if not video.is_file():
        print("ASK missing video", video)
        return 2
    if not vo.is_file() or not ass.is_file():
        print("ASK run synthesize.py first", args.work)
        return 2
    args.out.parent.mkdir(parents=True, exist_ok=True)
    ass_esc = ass.resolve().as_posix().replace(":", "\\:").replace("'", "\\'")
    ffmpeg_ok([
        FFMPEG, "-y",
        "-i", str(video),
        "-i", str(vo),
        "-map", "0:v:0", "-map", "1:a:0",
        "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,format=yuv420p,ass='{ass_esc}'",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(args.out),
    ])
    print("MUX", args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
