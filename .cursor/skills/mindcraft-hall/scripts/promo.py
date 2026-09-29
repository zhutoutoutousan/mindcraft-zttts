#!/usr/bin/env python3
"""Playwright first-person promo of Mindcraft Hall + whisper ASMR German VO.

  python skills/mindcraft-hall.py --serve --no-open
  python .cursor/skills/mindcraft-hall/scripts/promo.py

Uses Chrome. Pointer lock is not needed (?tour=1).
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve()
for p in [ROOT, *ROOT.parents]:
    if (p / "CPU.md").is_file():
        ROOT = p
        break
else:
    raise SystemExit("ASK CPU.md not found")

KIT = Path(__file__).resolve().parent.parent
BEATS = KIT / "promo.beats.json"
SYNTH = ROOT / ".cursor" / "skills" / "whisper-asmr-vo" / "scripts" / "synthesize.py"
MUX = ROOT / ".cursor" / "skills" / "whisper-asmr-vo" / "scripts" / "mux.py"
WORK = ROOT / "tmp" / "hall-promo"
URL = "http://127.0.0.1:8781/mindcraft-hall.html?tour=1&mute=1"
W, H = 1920, 1080


def hall_up() -> None:
    try:
        urllib.request.urlopen("http://127.0.0.1:8781/mindcraft-hall.html", timeout=8).read(32)
    except Exception as exc:  # noqa: BLE001
        raise SystemExit("ASK start hall: python skills/mindcraft-hall.py --serve --no-open") from exc


def synth() -> list[dict]:
    WORK.mkdir(parents=True, exist_ok=True)
    cues_path = WORK / "cues.json"
    vo = WORK / "voiceover.wav"
        if vo.is_file() and cues_path.is_file():
        pack = json.loads(cues_path.read_text(encoding="utf-8"))
        cues = pack["cues"]
        total = sum(float(c["hold"]) for c in cues)
        if pack.get("engine") == "world-unvoice" and 8 < total < 90:
            print("reuse VO", f"{total:.1f}s")
            return cues
    subprocess.run(
        [sys.executable, str(SYNTH), "--beats", str(BEATS), "--out", str(WORK)],
        check=True,
    )
    cues = json.loads((WORK / "cues.json").read_text(encoding="utf-8"))["cues"]
    return cues


def pose(c: dict, key: str) -> dict:
    src = c.get(key) or c.get("pose") or {}
    return {
        "x": float(src.get("x", 0)),
        "z": float(src.get("z", 14)),
        "yaw": float(src.get("yaw", 0)),
        "pitch": float(src.get("pitch", 0)),
    }


def record(cues: list[dict]) -> Path:
    from playwright.sync_api import sync_playwright

    pw_dir = WORK / "_pw"
    if pw_dir.exists():
        for old in pw_dir.glob("*"):
            old.unlink()
    pw_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",
            headless=False,
            args=["--autoplay-policy=no-user-gesture-required"],
        )
        context = browser.new_context(
            viewport={"width": W, "height": H},
            record_video_dir=str(pw_dir),
            record_video_size={"width": W, "height": H},
        )
        page = context.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_function("() => window.__hall && window.__hall.setPose", timeout=30000)
        page.wait_for_timeout(900)

        first = pose(cues[0], "pose")
        page.evaluate("(p) => window.__hall.setPose(p.x, p.z, p.yaw, p.pitch)", first)
        page.wait_for_timeout(400)

        for i, cue in enumerate(cues):
            a = pose(cues[i - 1], "look") if i else pose(cue, "pose")
            b = pose(cue, "look") if cue.get("look") else pose(cue, "pose")
            hold_ms = int(max(cue["hold"], 1.2) * 1000)
            steps = max(8, hold_ms // 50)
            for s in range(steps + 1):
                t = s / steps
                page.evaluate(
                    """({a, b, t}) => window.__hall.lerpPose(a, b, t)""",
                    {"a": a, "b": b, "t": t},
                )
                page.wait_for_timeout(hold_ms / steps)

        page.wait_for_timeout(600)
        page.close()
        raw = Path(page.video.path()) if page.video else None
        context.close()
        browser.close()
        dest = WORK / "tour.webm"
        if raw is None or not raw.is_file():
            hits = list(pw_dir.glob("*.webm"))
            raw = hits[0] if hits else None
        if raw is None or not raw.is_file():
            raise SystemExit("ASK playwright video missing")
        dest.write_bytes(raw.read_bytes())
        return dest


def mux(video: Path) -> Path:
    out = WORK / "hall-promo.mp4"
    subprocess.run(
        [sys.executable, str(MUX), "--video", str(video), "--work", str(WORK), "--out", str(out)],
        check=True,
    )
    return out


def touch() -> None:
    jan = ROOT / "cron" / "janitor.py"
    if jan.is_file():
        subprocess.run([sys.executable, str(jan), "--touch"], check=False)


def main() -> int:
    hall_up()
    print("TTS whisper…")
    cues = synth()
    print("Playwright tour…")
    video = record(cues)
    print("mux…")
    out = mux(video)
    touch()
    print("DELIVERED", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
