from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


def ffmpeg_exe() -> str:
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as exc:  # noqa: BLE001
        raise SystemExit("pip install imageio-ffmpeg") from exc


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def _ffmpeg_info(src: Path) -> str:
    p = subprocess.run(
        [ffmpeg_exe(), "-i", str(src)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return (p.stderr or "") + (p.stdout or "")


def duration_sec(src: Path) -> float:
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", _ffmpeg_info(src))
    if not m:
        return 0.0
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def video_size(src: Path) -> tuple[int, int]:
    m = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", _ffmpeg_info(src))
    if not m:
        raise SystemExit(f"no video size: {src}")
    return int(m.group(1)), int(m.group(2))


def ffprobe_json(src: Path) -> dict:
    """Best-effort; imageio-ffmpeg often ships ffmpeg only."""
    ff = Path(ffmpeg_exe())
    probe = ff.with_name(ff.name.replace("ffmpeg", "ffprobe"))
    if not probe.exists():
        w, h = video_size(src)
        return {
            "format": {"duration": str(duration_sec(src))},
            "streams": [{"codec_type": "video", "width": w, "height": h}],
        }
    raw = subprocess.check_output(
        [
            str(probe),
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(src),
        ]
    )
    return json.loads(raw)
