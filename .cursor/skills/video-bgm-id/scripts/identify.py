#!/usr/bin/env python3
"""Fingerprint BGM with Shazam. MEDIA stays in tmp/bgm-id/.

    python .cursor/skills/video-bgm-id/scripts/identify.py --url https://www.bilibili.com/video/BV...
    python .cursor/skills/video-bgm-id/scripts/identify.py --audio-url <m4s> --referer <watch> --id BV...
    python .cursor/skills/video-bgm-id/scripts/identify.py --file clip.wav
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "tmp" / "bgm-id"


def ffmpeg_exe() -> str:
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as exc:  # noqa: BLE001
        raise SystemExit("pip install imageio-ffmpeg") from exc


def slug_from(url: str | None, explicit: str | None) -> str:
    if explicit:
        return re.sub(r"[^A-Za-z0-9._-]+", "_", explicit)[:80]
    if not url:
        return "clip"
    m = re.search(r"(BV[0-9A-Za-z]+)", url)
    if m:
        return m.group(1)
    path = urlparse(url).path.rstrip("/").split("/")[-1] or "clip"
    return re.sub(r"[^A-Za-z0-9._-]+", "_", path)[:80]


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, **kw)


def download_audio_url(url: str, dest: Path, referer: str | None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "curl.exe" if sys.platform.startswith("win") else "curl",
        "-L",
        "--fail",
        "-A",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/128.0.0.0 Safari/537.36",
        "-o",
        str(dest),
        url,
    ]
    if referer:
        cmd[1:1] = ["-H", f"Referer: {referer}"]
    run(cmd)


def ytdlp_audio(url: str, dest_wav: Path) -> None:
    dest_wav.parent.mkdir(parents=True, exist_ok=True)
    stem = dest_wav.with_suffix("")
    try:
        run(
            [
                "yt-dlp",
                "--no-update",
                "-x",
                "--audio-format",
                "wav",
                "-o",
                str(stem) + ".%(ext)s",
                url,
            ]
        )
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or b"").decode("utf-8", "replace") if isinstance(exc.stderr, bytes) else ""
        if "412" in err or "Precondition Failed" in err:
            print("NEED_BROWSER_PLAYINFO")
            raise SystemExit(2) from exc
        raise
    if not dest_wav.is_file():
        raise SystemExit(f"yt-dlp produced no wav: {dest_wav}")


def to_wav(src: Path, dest: Path, extra: list[str] | None = None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    cmd = [ffmpeg_exe(), "-y", "-i", str(src)]
    if extra:
        cmd.extend(extra)
    cmd.extend(["-ac", "1", "-ar", "44100", str(dest)])
    run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def windows(src_wav: Path) -> list[tuple[str, Path]]:
    clips: list[tuple[str, Path]] = [("full", src_wav)]
    specs = [("t10-25", ["-ss", "10", "-t", "15"]), ("t20-40", ["-ss", "20", "-t", "20"]), ("t40-60", ["-ss", "40", "-t", "20"])]
    for name, extra in specs:
        dest = src_wav.with_name(f"{src_wav.stem}-{name}.wav")
        try:
            to_wav(src_wav, dest, extra)
        except subprocess.CalledProcessError:
            continue
        if dest.is_file() and dest.stat().st_size > 8000:
            clips.append((name, dest))
    return clips


def compact(rec: dict) -> dict:
    track = rec.get("track") or {}
    matches = rec.get("matches") or []
    return {
        "title": track.get("title"),
        "artist": track.get("subtitle"),
        "url": track.get("url"),
        "key": track.get("key"),
        "isrc": track.get("isrc"),
        "genre": (track.get("genres") or {}).get("primary") if isinstance(track.get("genres"), dict) else None,
        "match_ids": [m.get("id") for m in matches if isinstance(m, dict)],
    }


async def shazam_all(clips: list[tuple[str, Path]]) -> dict[str, dict]:
    from shazamio import Shazam

    shazam = Shazam()
    out: dict[str, dict] = {}
    for name, path in clips:
        rec = await shazam.recognize(str(path))
        out[name] = compact(rec if isinstance(rec, dict) else {})
    return out


def pick(hits: dict[str, dict]) -> dict | None:
    counts: dict[tuple[str, str], int] = {}
    best: dict[tuple[str, str], dict] = {}
    for row in hits.values():
        title, artist = row.get("title"), row.get("artist")
        if not title:
            continue
        key = (title, artist or "")
        counts[key] = counts.get(key, 0) + 1
        best[key] = row
    if not counts:
        return None
    winner = max(counts, key=counts.get)
    row = dict(best[winner])
    row["windows"] = counts[winner]
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--audio-url")
    ap.add_argument("--referer")
    ap.add_argument("--file")
    ap.add_argument("--id")
    args = ap.parse_args()
    if not (args.url or args.audio_url or args.file):
        raise SystemExit("need --url, --audio-url, or --file")

    OUT.mkdir(parents=True, exist_ok=True)
    slug = slug_from(args.url or args.audio_url, args.id)
    wav = OUT / f"{slug}.wav"

    if args.file:
        src = Path(args.file)
        if src.suffix.lower() == ".wav":
            wav = src
        else:
            to_wav(src, wav)
    elif args.audio_url:
        raw = OUT / f"{slug}.m4s"
        download_audio_url(args.audio_url, raw, args.referer or args.url)
        to_wav(raw, wav)
    else:
        ytdlp_audio(args.url, wav)

    hits = asyncio.run(shazam_all(windows(wav)))
    chosen = pick(hits)
    report = {"id": slug, "source": args.url or args.file or args.audio_url, "chosen": chosen, "windows": hits}
    report_path = OUT / f"{slug}.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not chosen:
        print("NO_MATCH")
        raise SystemExit(3)


if __name__ == "__main__":
    main()
