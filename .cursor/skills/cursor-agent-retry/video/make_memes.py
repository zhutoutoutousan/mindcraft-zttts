#!/usr/bin/env python3
"""Local memes for cursor-retry video. Output: tmp/cursor-agent-retry-video/_memes/"""
from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "tmp" / "cursor-agent-retry-video" / "_memes"
OUT.mkdir(parents=True, exist_ok=True)
FONT_B = Path(r"C:\Windows\Fonts\msyhbd.ttc")
FONT = Path(r"C:\Windows\Fonts\msyh.ttc")
if not FONT_B.exists():
    FONT_B = FONT


def fnt(n: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_B), n)


def cap(d, text, y, fill, size, w):
    font = fnt(size)
    bb = d.textbbox((0, 0), text, font=font)
    x = (w - (bb[2] - bb[0])) // 2
    for ox, oy in ((-2, 0), (2, 0), (0, -2), (0, 2)):
        d.text((x + ox, y + oy), text, font=font, fill="black")
    d.text((x, y), text, font=font, fill=fill)


def sticker(name, draw, top, bot):
    w = 720
    img = Image.new("RGB", (w, w), "#0A0E14")
    d = ImageDraw.Draw(img)
    d.rectangle([8, 8, w - 9, w - 9], outline="white", width=10)
    draw(d, w)
    cap(d, top, 36, "#FFEB3B", 40, w)
    cap(d, bot, w - 100, "#90CAF9", 34, w)
    p = OUT / name
    img.save(p)
    print(p.as_posix(), p.stat().st_size)


def m_drop(d, w):
    d.line([120, 360, 600, 360], fill="#FF8A80", width=10)
    d.polygon([(520, 320), (600, 360), (520, 400)], fill="#FF8A80")
    d.text((250, 280), "STREAM", font=fnt(36), fill="#FFCC80")


def m_two(d, w):
    d.ellipse([100, 240, 320, 460], outline="#69F0AE", width=6)
    d.ellipse([400, 240, 620, 460], outline="#FFCC80", width=6)
    d.text((150, 330), "NET", font=fnt(36), fill="#69F0AE")
    d.text((450, 330), "LOAD", font=fnt(32), fill="#FFCC80")


def m_http(d, w):
    d.rectangle([160, 260, 560, 480], outline="#90CAF9", width=5)
    d.text((220, 340), "HTTP/1.1", font=fnt(48), fill="#90CAF9")


def m_small(d, w):
    for i in range(3):
        d.rectangle([140 + i * 150, 280, 260 + i * 150, 420], outline="#69F0AE", width=4)
        d.text((170 + i * 150, 330), str(i + 1), font=fnt(40), fill="#69F0AE")


def m_nope(d, w):
    d.ellipse([200, 220, 520, 540], outline="#FF8A80", width=10)
    d.line([240, 260, 480, 500], fill="#FF8A80", width=10)


if __name__ == "__main__":
    for n, fn, t, b in [
        ("01-drop.png", m_drop, "STREAM DROP", "掉线在保存前"),
        ("02-two.png", m_two, "TWO HALVES", "网络+负载"),
        ("03-http.png", m_http, "HTTP/1.1", "先兼容模式"),
        ("04-small.png", m_small, "SMALL TURN", "≤3-4 tools"),
        ("05-nope.png", m_nope, "NO STORM", "禁止图像风暴"),
    ]:
        sticker(n, fn, t, b)
