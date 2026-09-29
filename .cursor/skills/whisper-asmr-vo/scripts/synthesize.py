#!/usr/bin/env python3
"""Beats JSON → German whisper/ASMR voiceover + DE captions.

  python .cursor/skills/whisper-asmr-vo/scripts/synthesize.py --beats beats.json --out tmp/slug
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path

import edge_tts
import imageio_ffmpeg
import numpy as np
import pyworld as pw

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
PAUSE = 0.7
# True whisper is unvoiced. Do not low-pass the air band away.
ASMR_AF = (
    "highpass=f=80,"
    "equalizer=f=220:width_type=h:width=100:g=2.5,"
    "equalizer=f=5500:width_type=h:width=2200:g=3,"
    "acompressor=threshold=-20dB:ratio=2.2:attack=12:release=160:makeup=7,"
    "volume=0.95,haas,"
    "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
)
WHISPER_SR = 24000


def repo_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "CPU.md").is_file():
            return p
    raise SystemExit("ASK CPU.md not found")


def audio_duration(path: Path) -> float:
    proc = subprocess.run(
        [FFMPEG, "-i", str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", proc.stderr)
    if not m:
        return 4.0
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def ffmpeg_ok(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", errors="replace")[-4000:]
        raise RuntimeError(f"ffmpeg failed ({proc.returncode}):\n{err}")


def asmr_filter(src: Path, dest: Path, pad: float = 0.0) -> None:
    af = ASMR_AF
    if pad > 0.04:
        af = f"{ASMR_AF},apad=pad_dur={pad:.3f}"
    def run(filtergraph: str) -> None:
        ffmpeg_ok([
            FFMPEG, "-y", "-i", str(src),
            "-af", filtergraph, "-ac", "2", "-ar", "48000", str(dest),
        ])
    try:
        run(af)
    except RuntimeError:
        run(af.replace(",haas", ""))


def decode_mono(src: Path, sr: int = WHISPER_SR) -> np.ndarray:
    proc = subprocess.run(
        [
            FFMPEG, "-i", str(src), "-f", "f32le", "-acodec", "pcm_f32le",
            "-ac", "1", "-ar", str(sr), "pipe:1",
        ],
        capture_output=True,
        check=True,
    )
    return np.frombuffer(proc.stdout, dtype=np.float32).astype(np.float64)


def encode_wav_file(y: np.ndarray, dest: Path, sr: int = WHISPER_SR) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    peak = float(np.max(np.abs(y))) + 1e-9
    pcm = (y / peak * 0.92).astype(np.float32)
    tmp = dest.with_suffix(".f32")
    pcm.tofile(tmp)
    try:
        ffmpeg_ok([
            FFMPEG, "-y", "-f", "f32le", "-ar", str(sr), "-ac", "1",
            "-i", str(tmp), "-c:a", "pcm_s16le", str(dest),
        ])
    finally:
        tmp.unlink(missing_ok=True)


def to_true_whisper(src: Path, dest: Path) -> None:
    """Unvoice modal TTS: zero F0, full aperiodicity (WORLD)."""
    x = decode_mono(src, WHISPER_SR)
    if len(x) < WHISPER_SR // 4:
        raise RuntimeError(f"audio too short: {src}")
    fs = float(WHISPER_SR)
    _f0, t = pw.harvest(x, fs)
    f0 = pw.stonemask(x, _f0, t, fs)
    sp = pw.cheaptrick(x, f0, t, fs)
    ap = pw.d4c(x, f0, t, fs)
    y = pw.synthesize(np.zeros_like(f0), sp, np.ones_like(ap), fs)
    encode_wav_file(y, dest, WHISPER_SR)


async def tts_try(text: str, path: Path, voice: str, rate: str, pitch: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, volume="+0%").save(str(path))
    if not path.is_file() or path.stat().st_size < 800:
        raise RuntimeError(f"TTS empty: {path}")


def fmt_srt(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def fmt_ass(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def wrap_de(text: str) -> str:
    lines = textwrap.wrap(text, width=40, break_long_words=False)[:3]
    return r"\N".join(lines) if lines else text


def write_captions(cues: list[dict], work: Path) -> None:
    srt_lines = []
    for i, c in enumerate(cues, 1):
        srt_lines += [str(i), f"{fmt_srt(c['start'])} --> {fmt_srt(c['end'])}", c["de"], ""]
    (work / "captions.de.srt").write_text("\n".join(srt_lines), encoding="utf-8")
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: DE,Segoe UI,44,&H00D4E0E8,&H00000000,&H64101010,&H80000000,-1,0,0,0,100,100,0,0,1,2.2,6,2,90,90,78,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = [
        f"Dialogue: 0,{fmt_ass(c['start'])},{fmt_ass(c['end'])},DE,,0,0,0,,{wrap_de(c['de'])}"
        for c in cues
    ]
    (work / "captions.de.ass").write_text(header + "\n".join(ev) + "\n", encoding="utf-8")


async def run(beats_path: Path, work: Path) -> int:
    spec = json.loads(beats_path.read_text(encoding="utf-8"))
    voice = spec.get("voice") or "de-DE-KatjaNeural"
    rate = spec.get("rate") or "-10%"
    pitch = spec.get("pitch") or "+0Hz"
    beats = spec["beats"]
    audio_dir = work / "_audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    cues = []
    wavs = []
    t = 0.35
    for beat in beats:
        sid = beat["id"]
        de = (beat.get("de") or "").strip()
        if not de:
            raise SystemExit(f"empty de on beat {sid}")
        raw = audio_dir / f"{sid}.raw.mp3"
        whispered = audio_dir / f"{sid}.whisper.wav"
        asmr = audio_dir / f"{sid}.asmr.wav"
        await tts_try(de, raw, voice, rate, pitch)
        to_true_whisper(raw, whispered)
        spoken = audio_duration(whispered)
        if spoken > 18:
            raise SystemExit(f"TTS too long ({spoken:.1f}s) on {sid}; refuse SSML-as-speech")
        hold = max(spoken + PAUSE, float(beat.get("min_hold") or 0))
        asmr_filter(whispered, asmr, pad=max(0.0, hold - spoken))
        cues.append({
            "id": sid,
            "de": de,
            "start": t,
            "end": t + spoken,
            "hold": hold,
            "pose": beat.get("pose") or {},
            "look": beat.get("look") or {},
        })
        wavs.append(asmr)
        t += hold

    lst = audio_dir / "concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in wavs), encoding="utf-8")
    vo = work / "voiceover.wav"
    ffmpeg_ok([
        FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
        "-i", str(lst), "-c:a", "pcm_s16le", str(vo),
    ])
    write_captions(cues, work)
    (work / "cues.json").write_text(
        json.dumps({
            "voice": voice, "rate": rate, "pitch": pitch,
            "engine": "world-unvoice",
            "cues": cues,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"VO {vo}  cues={len(cues)}  dur={t:.1f}s")
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--beats", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()
    if not args.beats.is_file():
        print("ASK missing beats", args.beats)
        return 2
    args.out.mkdir(parents=True, exist_ok=True)
    return asyncio.run(run(args.beats, args.out))


if __name__ == "__main__":
    sys.exit(main())
