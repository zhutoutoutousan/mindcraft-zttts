#!/usr/bin/env python3
"""Split 朋友的酒 into instrumental + vocals, convert vocal timbre
toward the concert plate singer, remix. Local files only."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ffmpeg_bin import ffmpeg_exe, run  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]


def wav(src: Path, dest: Path, start: float = 0.0, seconds: float | None = None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [ffmpeg_exe(), "-y", "-loglevel", "error"]
    if start > 0:
        cmd += ["-ss", f"{start:.3f}"]
    cmd += ["-i", str(src)]
    if seconds is not None:
        cmd += ["-t", f"{seconds:.3f}"]
    cmd += ["-ac", "2", "-ar", "44100", str(dest)]
    run(cmd)


def demucs_two(src: Path, out_dir: Path) -> tuple[Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        "-m",
        "demucs",
        "--two-stems",
        "vocals",
        "-n",
        "htdemucs",
        "-o",
        str(out_dir),
        str(src),
    ]
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)
    stem = src.stem
    hits_v = list(out_dir.rglob(f"{stem}/vocals.wav")) or list(out_dir.rglob("vocals.wav"))
    hits_i = list(out_dir.rglob(f"{stem}/no_vocals.wav")) or list(out_dir.rglob("no_vocals.wav"))
    if not hits_v or not hits_i:
        raise SystemExit(f"demucs stems missing under {out_dir}")
    return hits_v[0], hits_i[0]


def mix(vocals: Path, inst: Path, dest: Path, seconds: float) -> None:
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(vocals),
            "-i",
            str(inst),
            "-filter_complex",
            "volume=1.15[v];[1:a]volume=0.85[i];[v][i]amix=inputs=2:duration=first:dropout_transition=0,"
            f"afade=t=in:st=0:d=0.04,afade=t=out:st={max(0, seconds-0.3):.3f}:d=0.3,alimiter=limit=0.95",
            "-t",
            f"{seconds:.3f}",
            "-ac",
            "2",
            "-ar",
            "44100",
            str(dest),
        ]
    )


def convert_seedvc(source: Path, ref: Path, dest: Path) -> None:
    """Zero-shot singing/speech VC if seed-vc is installed."""
    try:
        from seed_vc.inference import main as seed_main  # type: ignore
    except Exception:
        seed_main = None
    if seed_main is None:
        # CLI fallback used by Plachtaa/seed-vc
        for mod in ("inference.py",):
            pass
    exe = shutil.which("seed-vc")
    if exe:
        subprocess.run([exe, "--source", str(source), "--target", str(ref), "--output", str(dest)], check=True)
        return
    # Try python -m
    r = subprocess.run(
        [
            sys.executable,
            "-m",
            "seed_vc",
            "--source",
            str(source),
            "--target",
            str(ref),
            "--output",
            str(dest),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if r.returncode == 0 and dest.exists():
        return
    raise SystemExit("seed-vc not installed; cannot convert timbre")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", default="friend-wine")
    ap.add_argument("--seconds", type=float, default=15.0)
    ap.add_argument("--song-start", type=float, default=6.0)
    ap.add_argument("--convert", action="store_true")
    args = ap.parse_args()

    base = ROOT / "tmp" / args.slug
    song = base / "_in" / "song.mp4"
    plate = base / "_in" / "plate.mp4"
    work = base / "_work" / "audio"
    work.mkdir(parents=True, exist_ok=True)
    if not song.exists():
        raise SystemExit(f"need {song}")

    clip = work / "song_clip.wav"
    wav(song, clip, start=args.song_start, seconds=args.seconds + 1.0)
    print("demucs song clip")
    vocals, inst = demucs_two(clip, work / "demucs_song")
    shutil.copy2(vocals, work / "song_vocals.wav")
    shutil.copy2(inst, work / "song_inst.wav")
    print(f"instrumental → {work / 'song_inst.wav'}")

    converted = work / "song_vocals.wav"
    if args.convert:
        if not plate.exists():
            raise SystemExit("need plate.mp4 as voice reference")
        ref = work / "plate_ref.wav"
        wav(plate, ref, start=20.0, seconds=18.0)
        print("demucs plate reference")
        ref_v, _ref_i = demucs_two(ref, work / "demucs_plate")
        shutil.copy2(ref_v, work / "lin_ref.wav")
        dest_c = work / "vocals_lin.wav"
        print("timbre convert toward plate singer")
        convert_seedvc(vocals, work / "lin_ref.wav", dest_c)
        converted = dest_c

    mix_path = work / "friend_wine_mix.wav"
    mix(converted, inst, mix_path, args.seconds)
    print(f"mix → {mix_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
