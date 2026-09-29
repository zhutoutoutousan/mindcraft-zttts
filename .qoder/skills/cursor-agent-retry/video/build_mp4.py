#!/usr/bin/env python3
"""Cursor Agent retry prevention — Bilibili + LinkedIn 16:9.

Kit lives in .cursor/skills/cursor-agent-retry/video/
Deliverables land in tmp/cursor-agent-retry-video/ (TTL 5 days).

    python .cursor/skills/cursor-agent-retry/video/make_memes.py
    python .cursor/skills/cursor-agent-retry/video/build_mp4.py
"""
from __future__ import annotations

import asyncio
import io
import random
import re
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
import zlib
from dataclasses import dataclass
from pathlib import Path

import edge_tts
import imageio_ffmpeg
import matplotlib
import numpy as np
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch
from PIL import Image as PILImage

matplotlib.use("Agg")
import matplotlib.pyplot as plt

def repo_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "CPU.md").is_file():
            return p
    raise SystemExit("ASK CPU.md not found")


KIT = Path(__file__).resolve().parent
ROOT = repo_root(KIT)
WORK = ROOT / "tmp" / "cursor-agent-retry-video"
DIAG = KIT / "diagrams"
AUDIO = WORK / "_audio"
SLIDES = WORK / "_slides"
MEMES = WORK / "_memes"
BROLL = WORK / "_broll"
PUML_PNG = WORK / "_puml"
CLIPS = WORK / "_clips"
OUT = WORK / "cursor-retry.mp4"
SRT = WORK / "cursor-retry.de-zh.srt"
ASS = WORK / "cursor-retry.de-zh.ass"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE, RATE, PAUSE = "de-DE-KatjaNeural", "+38%", 0.22
W, H, DPI = 1920, 1080, 100
C_BG, C_DE, C_ZH, C_ACC, C_MUTED, C_CARD = (
    "#0a0e14", "#ffcc80", "#90caf9", "#69f0ae", "#8899aa", "#121a24",
)
RNG = random.Random(20260906)

# Mixkit free (mute): highway / rain — network vibe. Copied if present under fog kits.
BROLL_SRCS = {
    "highway": ROOT / "tmp/fog-science/_broll/03-highway.mp4",
    "rain": ROOT / "tmp/fog-science/_broll/04-rain.mp4",
    "fog": ROOT / "tmp/fog-science/_broll/01-fog.mp4",
}

SEGMENTS: list[tuple[str, str, str, str, str, str | None, str | None]] = [
    (
        "01", "hook", "01-drop",
        "Agent stopped retrying. Klingt wie Server-Crash. Ist es nicht. Der Client-Stream bricht ab, bevor Fortschritt gespeichert ist. Retry setzt am letzten Speicherpunkt an.",
        "Agent stopped retrying。听起来像服务器崩了。其实不是。客户端流在进度保存前断了。点 Retry 从上次保存点继续。",
        "01-drop.png", "fog",
    ),
    (
        "02", "halves", "02-halves",
        "Zwei Hälften. Netzwerk-Leiter: HTTP, Proxy, Hotspot. Und Agent-Last: kleine Turns, keine Bildstürme. Nur Clash fixen und trotzdem sieben GenerateImage parallel — der Stream stirbt weiter.",
        "两半。网络梯子：HTTP、代理、热点对照。以及 Agent 负载：小回合、不要图像风暴。只修 Clash 却并行七次出图——流照样死。",
        "02-two.png", "highway",
    ),
    (
        "03", "diag", "cards",
        "Schritt一: Cursor Settings, Network, Run Diagnostics. Ausgabe behalten. Dann HTTP Compatibility Mode auf HTTP/1.1 — gleich disableHttp2. Danach jeden Cursor.exe killen und neu starten. Reload Window reicht nicht.",
        "第一步：设置→网络→诊断，留着输出。然后兼容模式打到 HTTP/1.1，等同 disableHttp2。改完杀掉所有 Cursor.exe 再开。只 Reload 不够。",
        "03-http.png", "rain",
    ),
    (
        "04", "ladder", "03-ladder",
        "Hotspot-对照: hält Agent auf Handy-Daten und stirbt im LAN oder VPN — der aktuelle Pfad ist schuld. Clash: Regelmodus, mixed oder HTTP Port in http.proxy. Kein SOCKS rein. Lieber kein TUN, kein System-Global.",
        "热点对照：手机流量稳、局域网或 VPN 死——路径有问题。Clash：规则模式，mixed/HTTP 端口填进 http.proxy。别填 SOCKS。优先别开 TUN、别系统全局。",
        "03-http.png", "highway",
    ),
    (
        "05", "proxy", "05-proxy",
        "proxySupport default override plus leeres http.proxy heißt nackte Verbindung. Entweder Port füllen oder Support auf on oder fallback. Standalone-App und VS-Code-Extension sind zwei Welten — Settings angleichen.",
        "proxySupport 默认 override 且代理为空＝裸连。要么填端口，要么改成 on/fallback。独立 App 和 VS Code 扩展是两套——设置要对齐。",
        "02-two.png", "rain",
    ),
    (
        "06", "agent", "04-agent-load",
        "Agent-Seite: maximal drei bis vier Tools pro Turn. Bilder lokal mit PIL oder make_memes. Höchstens zwei GenerateImage, und nur wenn du es willst. Web: bekannte CDN-URL, Shell-Download — nicht zehn Gallery-Seiten parallel fetchen.",
        "Agent 侧：每回合最多三到四个工具。图用本地 PIL 或 make_memes。GenerateImage 最多两次且仅当你点名。网页：已知 CDN 用 Shell 下——别并行抓十个图库页。",
        "04-small.png", "fog",
    ),
    (
        "07", "heavy", "cards2",
        "Schwere Jobs splitten: erst Skripte und Assets schreiben, Encode oder XeLaTeX im nächsten Turn. Nach Interrupt: Inventar von _memes, _broll, _audio — nur Lücken nachbauen. Nie denselben Megabatch nochmal abfeuern.",
        "重活拆开：先写脚本和素材，下一回合再编码或编译。中断后：盘点 _memes/_broll/_audio——只补缺口。禁止原样重放那个超级批次。",
        "05-nope.png", "highway",
    ),
    (
        "08", "dont", "dont",
        "Nicht zuerst: workspaceStorage löschen, .cursorignore, GPU aus. Die helfen andere Bugs. disableHttp1SSE als Erstschritt ist Cargo-Cult — offizieller Fallback ist HTTP/1.1 SSE. Zertifikat-Bypass nur letzte Not.",
        "别先清 workspaceStorage、改 ignore、关 GPU——那是别的毛病。一上来关 disableHttp1SSE 是跟风；官方回退就是 HTTP/1.1 SSE。关证书校验只当最后手段。",
        "05-nope.png", "rain",
    ),
    (
        "09", "retry", "close",
        "Merksatz: Drop vor Save. Zwei Hälften fixen. HTTP/1.1, Proxy richtig, Hotspot testen. Agent klein halten. Dann Retry klicken — nicht gleich neuen Chat öffnen, außer die Session selbst ist kaputt. Quellen: Cursor Forum und Network-Docs. Danke.",
        "口诀：掉在保存前。修两半。HTTP/1.1、代理填对、热点对照。Agent 保持小。然后点 Retry——别动不动新开聊天，除非会话真坏了。来源：Cursor 论坛与网络文档。谢谢。",
        "01-drop.png", "fog",
    ),
]


@dataclass
class Cue:
    sid: str
    section: str
    de: str
    zh: str
    start: float
    end: float


PUML_CONTRAST = r"""
<style>
root {
  FontColor #e8eef5
  LineColor #69f0ae
  LineThickness 2.5
  BackgroundColor #0a0e14
}
arrow {
  LineColor #69f0ae
  LineThickness 2.5
  FontColor #e8eef5
}
activity {
  BackgroundColor #121a24
  FontColor #e8eef5
  LineColor #69f0ae
}
partition {
  LineColor #90caf9
  FontColor #ffcc80
  BackgroundColor #1a2530
}
</style>
skinparam ArrowColor #69f0ae
skinparam ArrowThickness 3
skinparam activityBorderColor #69f0ae
skinparam activityBackgroundColor #121a24
skinparam activityFontColor #e8eef5
skinparam activityDiamondBorderColor #90caf9
skinparam activityDiamondBackgroundColor #1a2530
skinparam activityDiamondFontColor #e8eef5
skinparam noteBorderColor #ffcc80
skinparam noteBackgroundColor #1a2530
skinparam noteFontColor #e8eef5
skinparam rectangleBorderColor #69f0ae
skinparam rectangleBackgroundColor #121a24
skinparam databaseBorderColor #90caf9
skinparam databaseBackgroundColor #121a24
skinparam titleFontColor #e8eef5
"""


def cjk_font():
    for name in ("msyhbd.ttc", "msyh.ttc"):
        p = Path(r"C:\Windows\Fonts") / name
        if p.is_file():
            return font_manager.FontProperties(fname=str(p))
    return font_manager.FontProperties()


FP = cjk_font()


def wrap(text: str, width: int = 48, max_lines: int = 4) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False)[:max_lines])


def audio_duration(path: Path) -> float:
    proc = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", proc.stderr)
    if not m:
        return 5.0
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


async def tts_save(text: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(str(path))


def png_wh(blob: bytes) -> tuple[int, int]:
    if blob[:8] != b"\x89PNG\r\n\x1a\n" or len(blob) < 24:
        return 0, 0
    import struct
    return struct.unpack(">II", blob[16:24])


def png_is_dark(blob: bytes) -> bool:
    w, h = png_wh(blob)
    if h < 40:
        return False
    arr = np.asarray(PILImage.open(io.BytesIO(blob)).convert("RGB").resize((32, 32)))
    return float(arr.mean()) < 140


def with_contrast(src: str) -> str:
    block = PUML_CONTRAST.strip()
    return src.replace("@enduml", block + "\n@enduml", 1) if "@enduml" in src else src + "\n" + block


def _plantuml_encode(src: str) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    data = zlib.compress(src.encode("utf-8"))[2:-4]
    out = []
    for i in range(0, len(data), 3):
        b1 = data[i]
        b2 = data[i + 1] if i + 1 < len(data) else 0
        b3 = data[i + 2] if i + 2 < len(data) else 0
        n = (b1 << 16) + (b2 << 8) + b3
        out.append(alphabet[(n >> 18) & 63])
        out.append(alphabet[(n >> 12) & 63])
        out.append(alphabet[(n >> 6) & 63])
        out.append(alphabet[n & 63])
    return "".join(out)


def render_puml(stem: str) -> Path:
    puml = DIAG / f"{stem}.puml"
    out = PUML_PNG / f"{stem}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.is_file() and out.stat().st_mtime >= puml.stat().st_mtime:
        return out
    src = with_contrast(puml.read_text(encoding="utf-8"))
    req = urllib.request.Request(
        "https://kroki.io/plantuml/png",
        data=src.encode("utf-8"),
        headers={"Content-Type": "text/plain", "User-Agent": "mindcraft-zttts/1.0", "Accept": "image/png"},
        method="POST",
    )
    blob = b""
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            blob = resp.read()
    except (urllib.error.URLError, TimeoutError, urllib.error.HTTPError):
        blob = b""
    if png_is_dark(blob):
        out.write_bytes(blob)
        return out
    encoded = _plantuml_encode(src)
    for url in (
        "https://www.plantuml.com/plantuml/png/" + encoded,
        "https://www.plantuml.com/plantuml/png/~1" + encoded,
    ):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "mindcraft-zttts/1.0"}), timeout=90) as resp:
                fb = resp.read()
            if png_is_dark(fb):
                out.write_bytes(fb)
                return out
        except Exception:
            continue
    # fallback placeholder
    img = PILImage.new("RGB", (1200, 600), "#0a0e14")
    img.save(out)
    return out


def header(fig, section: str, sid: str) -> None:
    ax = fig.add_axes([0.04, 0.90, 0.92, 0.08])
    ax.axis("off")
    ax.text(0, 0.55, "Cursor Agent Retry  ·  Stream Drop verhindern", fontsize=26, color="white", fontweight="bold", va="center")
    ax.text(0, 0.05, f"{sid} · {section.upper()} · DE+38% · DE+ZH · B站/LinkedIn · PlantUML", fontsize=13, color=C_MUTED, va="center")


def sub_bar(fig, de: str, zh: str) -> None:
    ax = fig.add_axes([0.03, 0.02, 0.94, 0.24])
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012", facecolor="#0a1018", edgecolor=C_ZH, lw=3, transform=ax.transAxes))
    ax.text(0.02, 0.72, wrap(de, 50, 4), fontsize=17, color=C_DE, fontweight="bold", va="center", transform=ax.transAxes, linespacing=1.12)
    ax.text(0.02, 0.28, wrap(zh, 28, 3), fontsize=16, color=C_ZH, va="center", transform=ax.transAxes, fontproperties=FP, linespacing=1.12)


def show_puml(ax, stem: str) -> None:
    png = render_puml(stem)
    ax.imshow(plt.imread(png))
    ax.axis("off")
    ax.set_facecolor(C_BG)


def vis_cards(ax) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    steps = [("1", "Diagnostics"), ("2", "HTTP/1.1"), ("3", "Kill Cursor.exe"), ("4", "Relaunch")]
    for i, (n, t) in enumerate(steps):
        x = 0.4 + i * 2.4
        ax.add_patch(FancyBboxPatch((x, 2.0), 2.2, 2.4, boxstyle="round,pad=0.03", facecolor=C_CARD, edgecolor=C_ACC, lw=3))
        ax.text(x + 1.1, 3.6, n, color=C_ACC, fontsize=28, ha="center", fontweight="bold")
        ax.text(x + 1.1, 2.7, t, color=C_DE, fontsize=14, ha="center")


def vis_cards2(ax) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    for i, (t, e) in enumerate([("Write assets", C_ACC), ("Encode next turn", C_DE), ("Inventory gaps", C_ZH), ("No megabatch replay", "#ff8a80")]):
        y = 4.2 - i * 0.95
        ax.add_patch(FancyBboxPatch((1.2, y), 7.6, 0.8, boxstyle="round,pad=0.02", facecolor=C_CARD, edgecolor=e, lw=2.5))
        ax.text(5, y + 0.4, t, color=e, fontsize=20, ha="center", va="center", fontweight="bold")


def vis_dont(ax) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    bad = ["workspaceStorage wipe", ".cursorignore first", "GPU off first", "disableHttp1SSE first"]
    for i, t in enumerate(bad):
        x = 0.4 + (i % 2) * 4.8
        y = 3.4 if i < 2 else 1.4
        ax.add_patch(FancyBboxPatch((x, y), 4.4, 1.5, boxstyle="round,pad=0.03", facecolor=C_CARD, edgecolor="#ff8a80", lw=3))
        ax.text(x + 2.2, y + 0.75, t, color="#ff8a80", fontsize=16, ha="center", va="center")


def vis_close(ax) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((1.0, 1.6), 8.0, 3.2, boxstyle="round,pad=0.04", facecolor=C_CARD, edgecolor=C_ACC, lw=3))
    ax.text(5, 3.8, "Drop vor Save · Zwei Hälften", color=C_ACC, fontsize=28, ha="center", fontweight="bold")
    ax.text(5, 2.7, "掉在保存前 · 修两半 · 再点 Retry", color=C_ZH, fontsize=22, ha="center", fontproperties=FP)
    ax.text(5, 1.95, "Skill: .cursor/skills/cursor-agent-retry/", color=C_MUTED, fontsize=14, ha="center")


VIS_FN = {
    "cards": vis_cards,
    "cards2": vis_cards2,
    "dont": vis_dont,
    "close": vis_close,
}


def paste_meme(png: Path, meme_name: str | None) -> None:
    if not meme_name:
        return
    meme = MEMES / meme_name
    if not meme.is_file():
        return
    base = PILImage.open(png).convert("RGBA")
    stick = PILImage.open(meme).convert("RGBA")
    size = RNG.randint(250, 320)
    stick = stick.resize((size, size), PILImage.Resampling.LANCZOS)
    side = RNG.choice(["tl", "tr", "br"])
    m = 36
    if side == "tl":
        xy = (m, 105)
    elif side == "tr":
        xy = (W - size - m, 105)
    else:
        xy = (W - size - m, int(H * 0.48) - size // 2)
    base.alpha_composite(stick, xy)
    base.convert("RGB").save(png)


def draw_slide(sid, section, visual, de, zh, meme, png: Path) -> None:
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI, facecolor=C_BG)
    header(fig, section, sid)
    ax = fig.add_axes([0.04, 0.30, 0.92, 0.56])
    ax.set_facecolor(C_BG)
    if visual in VIS_FN:
        VIS_FN[visual](ax)
    else:
        show_puml(ax, visual)
    sub_bar(fig, de, zh)
    png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png, facecolor=C_BG)
    plt.close(fig)
    paste_meme(png, meme)


def fmt_srt(t: float) -> str:
    h, m = int(t // 3600), int((t % 3600) // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def fmt_ass(t: float) -> str:
    h, m = int(t // 3600), int((t % 3600) // 60)
    s = t % 60
    cs = int(round((s - int(s)) * 100))
    return f"{h:d}:{m:02d}:{int(s):02d}.{cs:02d}"


def write_subs(cues: list[Cue]) -> None:
    lines = []
    for i, c in enumerate(cues, 1):
        lines += [str(i), f"{fmt_srt(c.start)} --> {fmt_srt(c.end)}", f"DE: {c.de}", f"ZH: {c.zh}", ""]
    SRT.write_text("\n".join(lines), encoding="utf-8")
    header_ass = """[Script Info]
Title: cursor-retry DE+ZH
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Alignment, MarginL, MarginR, MarginV, BorderStyle, Outline, Encoding
Style: DE,Microsoft YaHei,38,&H0080CCFF,&H00101010,&H80000000,-1,2,40,40,100,1,3,1
Style: ZH,Microsoft YaHei,32,&H00F9CA90,&H00101010,&H80000000,0,2,40,40,48,1,3,1

[Events]
Format: Layer, Start, End, Style, Text
"""
    ev = []
    for c in cues:
        ev.append(f"Dialogue: 0,{fmt_ass(c.start)},{fmt_ass(c.end)},DE,{c.de}")
        ev.append(f"Dialogue: 0,{fmt_ass(c.start)},{fmt_ass(c.end)},ZH,{c.zh}")
    ASS.write_text(header_ass + "\n".join(ev) + "\n", encoding="utf-8")


def ffmpeg_ok(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", errors="replace")[-4000:]
        raise RuntimeError(f"ffmpeg failed ({proc.returncode}):\n{err}")


def make_still_clip(png: Path, dest: Path, hold: float) -> None:
    ffmpeg_ok([
        FFMPEG, "-y", "-loop", "1", "-i", str(png), "-t", f"{hold:.3f}",
        "-vf", "scale=1920:1080,setsar=1", "-pix_fmt", "yuv420p",
        "-c:v", "libx264", "-crf", "20", "-r", "30", str(dest),
    ])


def make_broll_clip(src: Path, dest: Path, hold: float) -> None:
    ffmpeg_ok([
        FFMPEG, "-y", "-stream_loop", "-1", "-i", str(src), "-t", f"{hold:.3f}",
        "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1",
        "-an", "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", "-r", "30", str(dest),
    ])


def ensure_broll() -> None:
    BROLL.mkdir(parents=True, exist_ok=True)
    for key, src in BROLL_SRCS.items():
        dest = BROLL / f"{key}.mp4"
        if dest.is_file():
            continue
        if src.is_file():
            dest.write_bytes(src.read_bytes())
            print("broll copy", key)
        else:
            print("ASK missing broll", src)


def encode_mux(parts: list[Path], full_audio: Path, out: Path) -> None:
    lst = CLIPS / "parts.concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in parts), encoding="utf-8")
    silent = out.with_name(out.stem + "._silent.mp4")
    ffmpeg_ok([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(silent)])
    mux = out.with_name(out.stem + "._mux.mp4")
    ffmpeg_ok([
        FFMPEG, "-y", "-i", str(silent), "-i", str(full_audio),
        "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", str(mux),
    ])
    ass_esc = ASS.resolve().as_posix().replace(":", "\\:").replace("'", "\\'")
    ffmpeg_ok([
        FFMPEG, "-y", "-i", str(mux),
        "-vf", f"ass='{ass_esc}'",
        "-c:a", "copy", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", str(out),
    ])
    silent.unlink(missing_ok=True)
    mux.unlink(missing_ok=True)


async def main() -> int:
    if not (ROOT / "CPU.md").is_file():
        print("ASK CPU.md")
        return 2
    if not any(MEMES.glob("*.png")):
        print("ASK run make_memes.py first")
        return 2
    ensure_broll()
    for d in (AUDIO, SLIDES, CLIPS, PUML_PNG):
        d.mkdir(parents=True, exist_ok=True)

    print("TTS…")
    durs, wavs = [], []
    for sid, _a, _b, de, _z, _m, _br in SEGMENTS:
        mp3 = AUDIO / f"{sid}.mp3"
        if not mp3.is_file():
            await tts_save(de, mp3)
        d = audio_duration(mp3)
        durs.append(d)
        wavs.append(mp3)
        print(f"  {sid} {d:.2f}s")

    pause = AUDIO / "_pause.mp3"
    if not pause.is_file():
        subprocess.run(
            [FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(PAUSE), "-q:a", "9", str(pause)],
            check=True, capture_output=True,
        )
    parts_a = []
    for i, w in enumerate(wavs):
        parts_a.append(w)
        if i < len(wavs) - 1:
            parts_a.append(pause)
    lst = AUDIO / "full.concat.txt"
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in parts_a), encoding="utf-8")
    full = AUDIO / "full.mp3"
    ffmpeg_ok([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(full)])

    print("PlantUML + slides…")
    # pre-render puml stems used
    for stem in ("01-drop", "02-halves", "03-ladder", "04-agent-load", "05-proxy"):
        render_puml(stem)
        print(" ", stem)

    cues, video_parts, t = [], [], 0.0
    for i, (row, dur) in enumerate(zip(SEGMENTS, durs)):
        sid, section, visual, de, zh, meme, bkey = row
        hold = dur + (PAUSE if i < len(SEGMENTS) - 1 else 0.0)
        png = SLIDES / f"{sid}.png"
        draw_slide(sid, section, visual, de, zh, meme, png)
        still_t = max(2.5, hold * 0.6)
        b_t = max(1.4, hold - still_t)
        still_mp4 = CLIPS / f"{sid}-still.mp4"
        make_still_clip(png, still_mp4, still_t)
        video_parts.append(still_mp4)
        bsrc = BROLL / f"{bkey}.mp4" if bkey else None
        b_mp4 = CLIPS / f"{sid}-broll.mp4"
        if bsrc and bsrc.is_file():
            make_broll_clip(bsrc, b_mp4, b_t)
        else:
            make_still_clip(png, b_mp4, b_t)
        video_parts.append(b_mp4)
        cues.append(Cue(sid, section, de, zh, t, t + dur))
        t += hold
        print(" ", sid, section)

    write_subs(cues)
    print("Encode…")
    encode_mux(video_parts, full, OUT)
    print(OUT.as_posix(), f"{t:.1f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
