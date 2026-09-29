#!/usr/bin/env python3
"""Parody mix: Demucs instrumental + TTS retuned to original vocal F0.

  python .cursor/skills/lyric-parody/scripts/mix.py --job tmp/lyric-parody/slug/job.json
"""
from __future__ import annotations

import argparse
import asyncio
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / ".cursor" / "skills" / "stage-body-composite" / "scripts"))
from ffmpeg_bin import ffmpeg_exe, run  # noqa: E402
from voice_mix import demucs_two  # noqa: E402

from meter import check, units  # noqa: E402

SR = 24000
VOICES = {
    "zh": "zh-CN-YunxiNeural",
    "de": "de-DE-ConradNeural",
    "en": "en-US-GuyNeural",
}


def decode_mono(src: Path, sr: int = SR) -> np.ndarray:
    proc = subprocess.run(
        [
            ffmpeg_exe(),
            "-i",
            str(src),
            "-f",
            "f32le",
            "-acodec",
            "pcm_f32le",
            "-ac",
            "1",
            "-ar",
            str(sr),
            "pipe:1",
        ],
        capture_output=True,
        check=True,
    )
    return np.frombuffer(proc.stdout, dtype=np.float32).astype(np.float64)


def encode_wav(y: np.ndarray, dest: Path, sr: int = SR) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    peak = float(np.max(np.abs(y))) + 1e-9
    pcm = (y / peak * 0.89).astype(np.float32)
    tmp = dest.with_suffix(".f32")
    pcm.tofile(tmp)
    try:
        run(
            [
                ffmpeg_exe(),
                "-y",
                "-loglevel",
                "error",
                "-f",
                "f32le",
                "-ar",
                str(sr),
                "-ac",
                "1",
                "-i",
                str(tmp),
                "-c:a",
                "pcm_s16le",
                str(dest),
            ]
        )
    finally:
        tmp.unlink(missing_ok=True)


def duration_sec(src: Path) -> float:
    y = decode_mono(src)
    return len(y) / float(SR)


def stretch(src: Path, dest: Path, target: float) -> None:
    src_d = max(0.08, duration_sec(src))
    ratio = src_d / max(0.08, target)
    ratio = min(2.0, max(0.5, ratio))
    run(
        [
            ffmpeg_exe(),
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(src),
            "-af",
            f"atempo={ratio:.4f}",
            "-ac",
            "1",
            "-ar",
            str(SR),
            str(dest),
        ]
    )
    y = decode_mono(dest)
    need = int(target * SR)
    if len(y) < need:
        y = np.pad(y, (0, need - len(y)))
    else:
        y = y[:need]
    encode_wav(y, dest)


def follow_f0(tts: Path, vocal_slice: np.ndarray, dest: Path) -> None:
    import pyworld as pw

    x = decode_mono(tts)
    if len(x) < SR // 8:
        encode_wav(x, dest)
        return
    fs = float(SR)
    v = vocal_slice
    if len(v) < 64:
        v = x
    f0_v, t_v = pw.harvest(v, fs)
    f0_v = pw.stonemask(v, f0_v, t_v, fs)
    f0_x, t_x = pw.harvest(x, fs)
    f0_x = pw.stonemask(x, f0_x, t_x, fs)
    sp = pw.cheaptrick(x, f0_x, t_x, fs)
    ap = pw.d4c(x, f0_x, t_x, fs)
    if len(f0_v) < 2:
        y = x
    else:
        idx = np.linspace(0, len(f0_v) - 1, num=len(f0_x))
        f0 = np.interp(idx, np.arange(len(f0_v)), f0_v)
        y = pw.synthesize(f0, sp, ap, fs)
    encode_wav(y, dest)


async def tts_line(text: str, dest: Path, voice: str) -> None:
    import edge_tts

    dest.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(text, voice, rate="+0%", pitch="+0%", volume="+0%").save(
        str(dest)
    )
    if not dest.is_file() or dest.stat().st_size < 800:
        raise RuntimeError(f"TTS empty: {dest}")


def whisper_cues(vocals: Path, lang: str) -> list[dict]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise SystemExit("pip install faster-whisper") from exc
    model = WhisperModel("base", device="cpu", compute_type="int8")
    wl = None if lang == "zh" else lang
    segs, _info = model.transcribe(str(vocals), language=wl, word_timestamps=True)
    words: list[tuple[float, float, str]] = []
    for seg in segs:
        for w in seg.words or []:
            tok = (w.word or "").strip()
            if tok:
                words.append((float(w.start), float(w.end), tok))
    if not words:
        return []
    lines: list[dict] = []
    buf = [words[0]]
    for cur in words[1:]:
        gap = cur[0] - buf[-1][1]
        if gap > 0.35:
            text = "".join(t for _a, _b, t in buf)
            lines.append(
                {
                    "t0": round(buf[0][0], 3),
                    "t1": round(buf[-1][1], 3),
                    "n": units(text, lang),
                }
            )
            buf = [cur]
        else:
            buf.append(cur)
    text = "".join(t for _a, _b, t in buf)
    lines.append(
        {
            "t0": round(buf[0][0], 3),
            "t1": round(buf[-1][1], 3),
            "n": units(text, lang),
        }
    )
    return lines


def mix_wavs(vocals: Path, inst: Path, dest: Path) -> None:
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
            "[0:a]volume=1.12[v];[1:a]volume=0.82[i];"
            "[v][i]amix=inputs=2:duration=first:dropout_transition=0,alimiter=limit=0.95",
            "-ac",
            "2",
            "-ar",
            "44100",
            str(dest),
        ]
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True)
    args = ap.parse_args()
    job_path = Path(args.job)
    job = json.loads(job_path.read_text(encoding="utf-8"))
    errs = check(job)
    if errs:
        print("\n".join(errs))
        raise SystemExit(2)
    audio = Path(job.get("audio") or "")
    if not audio.is_file():
        raise SystemExit("job.audio missing — lyrics-only, skip mix")
    lang = job.get("lang") or "zh"
    voice = job.get("voice") or VOICES.get(lang, VOICES["zh"])
    slug = job.get("slug") or job_path.parent.name
    work = ROOT / "tmp" / "lyric-parody" / slug
    work.mkdir(parents=True, exist_ok=True)
    print("demucs")
    vocals, inst = demucs_two(audio, work / "demucs")
    v = decode_mono(vocals)
    lines = list(job["lines"])
    if not all("t0" in r and "t1" in r for r in lines):
        cues = whisper_cues(vocals, lang)
        (work / "cues.json").write_text(
            json.dumps(cues, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        n = min(len(lines), len(cues))
        if n == 0:
            raise SystemExit("no cues from vocals")
        if len(lines) != len(cues):
            print(f"WARN line count parody={len(lines)} cues={len(cues)} pair={n}")
        for i in range(n):
            lines[i]["t0"] = cues[i]["t0"]
            lines[i]["t1"] = cues[i]["t1"]
        lines = lines[:n]
    total = max(len(v) / float(SR), max(float(r["t1"]) for r in lines) + 0.4)
    bed = np.zeros(int(total * SR) + SR, dtype=np.float64)
    raw_dir = work / "_tts"
    raw_dir.mkdir(exist_ok=True)
    for i, row in enumerate(lines):
        t0 = float(row["t0"])
        t1 = float(row["t1"])
        dur = max(0.12, t1 - t0)
        raw = raw_dir / f"{i:03d}.mp3"
        stretched = raw_dir / f"{i:03d}.stretch.wav"
        sung = raw_dir / f"{i:03d}.f0.wav"
        asyncio.run(tts_line(row["text"], raw, voice))
        stretch(raw, stretched, dur)
        a0 = int(t0 * SR)
        a1 = a0 + int(dur * SR)
        slice_v = v[max(0, a0) : min(len(v), a1)]
        follow_f0(stretched, slice_v, sung)
        y = decode_mono(sung)
        end = min(len(bed), a0 + len(y))
        bed[a0:end] += y[: end - a0]
    new_v = work / "parody-vocals.wav"
    encode_wav(bed, new_v)
    dest = work / f"{slug}.wav"
    mix_wavs(new_v, inst, dest)
    print("wav", dest, dest.stat().st_size)


if __name__ == "__main__":
    main()
