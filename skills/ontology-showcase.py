#!/usr/bin/env python3
"""Render pedagogy/universe.graph.md without overlapping nodes.

    python skills/ontology-showcase.py --mode image --deliver
    python skills/ontology-showcase.py --mode video --deliver

Image deliverable is three files under tmp/pedagogy/:
  universe.png         core essence tree (no stack leaves)
  universe.stack.png   stack tools in labeled family panels
  universe.html        full graph, pan and zoom
"""
from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
import networkx as nx

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from matplotlib.patheffects import withStroke

ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "pedagogy" / "universe.graph.md"
TMP = ROOT / "tmp" / "_work" / "showcase"
OUT_DIR = ROOT / "tmp" / "pedagogy"
OUT_PNG = OUT_DIR / "universe.png"
OUT_STACK = OUT_DIR / "universe.stack.png"
OUT_HTML = OUT_DIR / "universe.html"
OUT_MP4 = OUT_DIR / "universe.mp4"
PUML = OUT_DIR / "universe.puml"

C_BG = "#0a0e14"
C_TEXT = "#e8eef5"
C_MUTED = "#8b9bb4"
C_ACC = "#69f0ae"

KIND_FILL = {
    "transcendental": "#1a237e",
    "formal": "#004d40",
    "natural": "#1b3a4b",
    "techne": "#3e2723",
    "praxis": "#4a148c",
    "semiosis": "#0d47a1",
}
KIND_EDGE = {
    "transcendental": "#90caf9",
    "formal": "#69f0ae",
    "natural": "#80deea",
    "techne": "#ffcc80",
    "praxis": "#ce93d8",
    "semiosis": "#82b1ff",
}
LABEL_COLOR = {
    "ISA": "#90caf9",
    "PARTICIPATES": "#ce93d8",
    "INFORMS": "#69f0ae",
    "RECEIVES": "#80cbc4",
    "STUDIES": "#ffcc80",
    "GROUNDS_IN": "#ffab91",
    "APPLIES": "#82b1ff",
    "ENACTS": "#f48fb1",
    "MEDIATES": "#b39ddb",
    "TRANSMITS": "#a5d6a7",
    "CONTRADICTS": "#ef5350",
}
KIND_ORDER = [
    "transcendental",
    "formal",
    "natural",
    "techne",
    "praxis",
    "semiosis",
]
STACK_FAMILIES = [
    ("languages", ["JavaScript", "TypeScript", "GoLang", "Python", "Java", "NodeJS"]),
    ("web-ui", ["React", "NextJS", "Vue", "TailwindCSS", "Redux", "Figma", "MicroFrontend"]),
    ("servers", ["SpringBoot", "FastAPI", "NestJS", "REST", "WebSocket", "GoFiber", "LabVIEW"]),
    ("stores", ["Redis", "Redisson", "PostgreSQL", "MongoDB", "MySQL", "Supabase", "DynamoDB", "PostGIS", "AzureCosmosGremlin"]),
    ("aws", ["AWS", "ECS", "EKS", "Fargate", "Bedrock", "SQS", "CDK", "CloudFormation"]),
    ("cloud-other", ["Azure"]),
    ("place", ["MapLibre", "DeckGL", "GeoJSON", "MCP", "OSM", "ALKIS", "MaStR", "BKG"]),
    ("agents", ["LargeLanguageModel", "Kiro", "ClaudeCode", "SemanticKernel"]),
    ("graphics", ["ThreeJS", "D3", "BIMFACE", "WebGL", "Unity"]),
    ("ops", ["Docker", "Kubernetes", "GitHubCI", "Playwright", "Sentry"]),
    ("search-trade", ["MetaTrader", "Bandit", "GeneticSearch", "AST", "InAppPurchase"]),
]

V_RE = re.compile(r"^V\s+(\S+)\s+(.*)$")
E_RE = re.compile(r"^E\s+(\S+)\s+(\S+)\s+(\S+)(?:\s+(.*))?$")
KV_RE = re.compile(r"(\S+)=(\S+)")


def parse_graph(path: Path) -> tuple[list[dict], list[dict]]:
    verts: list[dict] = []
    edges: list[dict] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("graph:") or line.startswith("engine:"):
            continue
        m = V_RE.match(line)
        if m:
            props = dict(KV_RE.findall(m.group(2)))
            verts.append({"id": m.group(1), **props})
            continue
        m = E_RE.match(line)
        if m:
            props = dict(KV_RE.findall(m.group(4) or ""))
            edges.append({"src": m.group(1), "label": m.group(2), "dst": m.group(3), **props})
    return verts, edges


def is_stack(v: dict) -> bool:
    return "/stack/" in v.get("body", "")


def split_core(verts: list[dict], edges: list[dict]):
    core = [v for v in verts if not is_stack(v)]
    ids = {v["id"] for v in core}
    core_e = [e for e in edges if e["src"] in ids and e["dst"] in ids]
    return core, core_e


def multipartite_pos(verts: list[dict]) -> dict[str, tuple[float, float]]:
    per_kind: dict[str, list[str]] = defaultdict(list)
    for v in verts:
        kind = v.get("kind", "praxis")
        if kind not in KIND_ORDER:
            kind = "praxis"
        per_kind[kind].append(v["id"])
    wrap = 8
    g = nx.Graph()
    layer = 0
    for kind in KIND_ORDER:
        ids = per_kind.get(kind, [])
        if not ids:
            continue
        for i in range(0, len(ids), wrap):
            chunk = ids[i : i + wrap]
            for vid in chunk:
                g.add_node(vid, layer=layer)
            layer += 1
    raw = nx.multipartite_layout(g, subset_key="layer", align="horizontal", scale=1.0)
    xs = [p[0] for p in raw.values()]
    ys = [p[1] for p in raw.values()]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    dx = (maxx - minx) or 1.0
    dy = (maxy - miny) or 1.0
    return {
        k: (0.07 + 0.86 * (p[0] - minx) / dx, 0.12 + 0.78 * (p[1] - miny) / dy)
        for k, p in raw.items()
    }


def node_size(pos: dict[str, tuple[float, float]]) -> tuple[float, float]:
    ids = list(pos)
    if len(ids) < 2:
        return 0.12, 0.07
    md = 1.0
    for i, a in enumerate(ids):
        ax, ay = pos[a]
        for b in ids[i + 1 :]:
            bx, by = pos[b]
            md = min(md, math.hypot(ax - bx, ay - by))
    nw = min(0.13, max(0.045, md * 0.62))
    nh = nw * 0.52
    return nw, nh


def draw_core(verts, edges, pos, visible, path, title, subtitle) -> None:
    n = max(len(visible), 8)
    fig_w, fig_h, dpi = 24.0, 16.0 + n * 0.08, 130
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.08)
    ax.axis("off")
    nw, nh = node_size({k: pos[k] for k in visible if k in pos})
    for e in edges:
        if e["src"] not in visible or e["dst"] not in visible:
            continue
        x1, y1 = pos[e["src"]]
        x2, y2 = pos[e["dst"]]
        color = LABEL_COLOR.get(e["label"], C_ACC)
        rad = 0.18 if e["label"] == "CONTRADICTS" else 0.06
        ax.add_patch(
            FancyArrowPatch(
                (x1, y1),
                (x2, y2),
                arrowstyle="-|>",
                mutation_scale=12,
                linewidth=1.5,
                color=color,
                connectionstyle=f"arc3,rad={rad}",
                shrinkA=22,
                shrinkB=22,
                alpha=0.85,
                zorder=1,
            )
        )
        if e["label"] in {"CONTRADICTS", "ISA"}:
            ax.text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                e["label"],
                color=color,
                fontsize=7,
                ha="center",
                va="center",
                zorder=2,
                path_effects=[withStroke(linewidth=3, foreground=C_BG)],
            )
    by = {v["id"]: v for v in verts}
    for vid in visible:
        if vid not in pos:
            continue
        x, y = pos[vid]
        kind = by[vid].get("kind", "praxis")
        ax.add_patch(
            FancyBboxPatch(
                (x - nw / 2, y - nh / 2),
                nw,
                nh,
                boxstyle="round,pad=0.004,rounding_size=0.01",
                facecolor=KIND_FILL.get(kind, "#121a24"),
                edgecolor=KIND_EDGE.get(kind, C_ACC),
                linewidth=1.8,
                zorder=3,
            )
        )
        ax.text(x, y + nh * 0.12, vid, color=C_TEXT, fontsize=8, ha="center", va="center", fontweight="bold", zorder=4)
        gloss = by[vid].get("gloss", "").replace("-", " ")[:36]
        ax.text(x, y - nh * 0.22, gloss, color=C_MUTED, fontsize=5.5, ha="center", va="center", zorder=4)
    ax.text(0.5, 1.05, title, color=C_ACC, fontsize=16, ha="center", va="top", fontweight="bold")
    ax.text(0.5, 1.015, subtitle, color=C_MUTED, fontsize=8, ha="center", va="top")
    for i, kind in enumerate(KIND_ORDER):
        ax.add_patch(
            FancyBboxPatch(
                (0.02 + i * 0.16, 0.015),
                0.012,
                0.016,
                boxstyle="round,pad=0.001",
                facecolor=KIND_FILL[kind],
                edgecolor=KIND_EDGE[kind],
                linewidth=1.2,
                zorder=5,
            )
        )
        ax.text(0.038 + i * 0.16, 0.023, kind, color=C_MUTED, fontsize=7, va="center")
    fig.savefig(path, facecolor=C_BG, bbox_inches="tight", pad_inches=0.12)
    plt.close(fig)


def draw_stack_panels(verts: list[dict], path: Path) -> None:
    by = {v["id"]: v for v in verts}
    families: list[tuple[str, list[str]]] = []
    used: set[str] = set()
    for name, ids in STACK_FAMILIES:
        have = [i for i in ids if i in by]
        if have:
            families.append((name, have))
            used.update(have)
    leftover = sorted(v["id"] for v in verts if is_stack(v) and v["id"] not in used)
    if leftover:
        families.append(("other", leftover))
    cols = 3
    rows = math.ceil(len(families) / cols)
    fig_w, fig_h, dpi = 24.0, 5.2 * rows, 120
    fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=dpi)
    fig.patch.set_facecolor(C_BG)
    ax.set_facecolor(C_BG)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.axis("off")
    ax.set_title("stack families  ·  not a CV  ·  Kafka not sourced", color=C_ACC, fontsize=16, pad=12)
    pad = 0.06
    for i, (name, ids) in enumerate(families):
        r, c = divmod(i, cols)
        y0 = rows - r - 1
        x0 = c
        ax.add_patch(
            Rectangle(
                (x0 + pad, y0 + pad),
                1 - 2 * pad,
                1 - 2 * pad,
                facecolor="#121a24",
                edgecolor="#ffcc80",
                linewidth=1.6,
                zorder=1,
            )
        )
        ax.text(x0 + 0.5, y0 + 1 - pad - 0.08, name, color=C_ACC, fontsize=11, ha="center", va="top", fontweight="bold")
        inner_w = 1 - 2 * pad - 0.08
        inner_h = 1 - 2 * pad - 0.18
        n = len(ids)
        wrap = 3 if n > 4 else max(n, 1)
        nr = math.ceil(n / wrap)
        cw, ch = inner_w / wrap, inner_h / nr
        chip_w, chip_h = cw * 0.88, ch * 0.62
        for j, vid in enumerate(ids):
            rr, cc = divmod(j, wrap)
            cx = x0 + pad + 0.04 + cc * cw + cw / 2
            cy = y0 + pad + 0.06 + (nr - 1 - rr) * ch + ch / 2
            ax.add_patch(
                FancyBboxPatch(
                    (cx - chip_w / 2, cy - chip_h / 2),
                    chip_w,
                    chip_h,
                    boxstyle="round,pad=0.01,rounding_size=0.02",
                    facecolor=KIND_FILL["techne"],
                    edgecolor=KIND_EDGE["techne"],
                    linewidth=1.3,
                    zorder=2,
                )
            )
            ax.text(cx, cy, vid, color=C_TEXT, fontsize=8, ha="center", va="center", zorder=3)
    fig.savefig(path, facecolor=C_BG, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


def write_html(verts: list[dict], edges: list[dict], path: Path) -> None:
    nodes = []
    for v in verts:
        kind = v.get("kind", "praxis")
        nodes.append(
            {
                "id": v["id"],
                "label": v["id"],
                "title": v.get("gloss", "").replace("-", " "),
                "group": kind,
                "level": KIND_ORDER.index(kind) if kind in KIND_ORDER else 4,
                "shape": "box",
                "color": {
                    "background": KIND_FILL.get(kind, "#121a24"),
                    "border": KIND_EDGE.get(kind, C_ACC),
                },
                "font": {"color": "#e8eef5", "size": 14},
            }
        )
    vis_edges = []
    for e in edges:
        vis_edges.append(
            {
                "from": e["src"],
                "to": e["dst"],
                "label": e["label"],
                "arrows": "to",
                "color": {"color": LABEL_COLOR.get(e["label"], C_ACC)},
                "font": {"color": LABEL_COLOR.get(e["label"], C_ACC), "size": 10, "strokeWidth": 0},
            }
        )
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>universe.graph</title>
  <script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
  <style>
    html, body {{ margin: 0; height: 100%; background: #0a0e14; color: #8b9bb4; font-family: ui-sans-serif, system-ui; }}
    #bar {{ padding: 10px 16px; border-bottom: 1px solid #2a3544; }}
    #bar strong {{ color: #69f0ae; }}
    #net {{ height: calc(100% - 48px); }}
  </style>
</head>
<body>
  <div id="bar"><strong>universe.graph</strong> · pan, scroll-zoom, drag nodes · stack leaves included · Kafka not sourced</div>
  <div id="net"></div>
  <script>
    const nodes = new vis.DataSet({json.dumps(nodes)});
    const edges = new vis.DataSet({json.dumps(vis_edges)});
    const net = new vis.Network(document.getElementById('net'), {{nodes, edges}}, {{
      physics: {{
        enabled: true,
        solver: 'forceAtlas2Based',
        forceAtlas2Based: {{ gravitationalConstant: -80, springLength: 90, avoidOverlap: 1 }},
        stabilization: {{ iterations: 250 }}
      }},
      interaction: {{ hover: true, navigationButtons: true, keyboard: true }},
      nodes: {{ margin: 8, widthConstraint: {{ maximum: 160 }} }},
      edges: {{ smooth: {{ type: 'cubicBezier', forceDirection: 'vertical', roundness: 0.4 }} }}
    }});
    net.once('stabilized', () => net.setOptions({{ physics: false }}));
  </script>
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def write_puml(verts: list[dict], edges: list[dict], path: Path) -> None:
    core, core_e = split_core(verts, edges)
    lines = [
        "@startuml",
        "skinparam backgroundColor #0a0e14",
        "skinparam defaultFontColor #e8eef5",
        "skinparam ArrowColor #69f0ae",
        "skinparam ArrowThickness 2",
        "skinparam rectangleBorderColor #90caf9",
        "skinparam rectangleBackgroundColor #121a24",
        "skinparam packageBorderColor #90caf9",
        "skinparam packageBackgroundColor #0d141c",
        "skinparam shadowing false",
        "title universe.graph core — stack leaves omitted",
        "",
    ]
    buckets: dict[str, list[str]] = defaultdict(list)
    for v in core:
        buckets[v.get("kind", "praxis")].append(v["id"])
    for kind in KIND_ORDER:
        ids = buckets.get(kind, [])
        if not ids:
            continue
        lines.append(f'package "{kind}" {{')
        for vid in ids:
            lines.append(f"  rectangle {vid}")
        lines.append("}")
        lines.append("")
    for e in core_e:
        lines.append(f"{e['src']} --> {e['dst']} : {e['label']}")
    lines.append("@enduml")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def stamp_ttl() -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "cron" / "janitor.py"), "--touch"],
        check=True,
    )


def ffmpeg_bin() -> str:
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"


def render_video(verts, edges, pos, tmp: Path) -> Path:
    tmp.mkdir(parents=True, exist_ok=True)
    frames: list[Path] = []
    visible: set[str] = set()
    by_kind: dict[str, list[str]] = defaultdict(list)
    for v in verts:
        by_kind[v.get("kind", "praxis")].append(v["id"])
    step = 0
    for kind in KIND_ORDER:
        ids = by_kind.get(kind, [])
        if not ids:
            continue
        visible.update(ids)
        step += 1
        fp = tmp / f"frame-{step:02d}.png"
        draw_core(verts, edges, pos, set(visible), fp, "universe.graph", f"reveal · {kind}")
        frames.append(fp)
    concat = tmp / "frames.concat.txt"
    lines = []
    for fp in frames:
        lines.append(f"file '{fp.resolve().as_posix()}'")
        lines.append("duration 1.8")
    lines.append(f"file '{frames[-1].resolve().as_posix()}'")
    concat.write_text("\n".join(lines) + "\n", encoding="utf-8")
    out = tmp / "universe.mp4"
    cmd = [
        ffmpeg_bin(),
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat),
        "-vf",
        "fps=30,scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p",
        "-movflags",
        "+faststart",
        str(out),
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or b"").decode("utf-8", "replace")
        raise SystemExit(f"ffmpeg failed\n{err[-4000:]}") from exc
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["image", "video", "ask"], default="ask")
    p.add_argument("--deliver", action="store_true")
    p.add_argument("--keep-tmp", action="store_true")
    args = p.parse_args()
    if args.mode == "ask":
        print("ASK SHOWCASE image or video. Default image. Re-run with --mode image|video.")
        return 2
    verts, edges = parse_graph(GRAPH)
    core, core_e = split_core(verts, edges)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_puml(verts, edges, PUML)
    if TMP.exists():
        shutil.rmtree(TMP)
    TMP.mkdir(parents=True, exist_ok=True)
    if args.mode == "image":
        pos = multipartite_pos(core)
        core_png = TMP / "core.png"
        stack_png = TMP / "stack.png"
        draw_core(
            core,
            core_e,
            pos,
            {v["id"] for v in core},
            core_png,
            "universe.graph",
            "core essence  ·  stack tools on universe.stack.png and universe.html",
        )
        draw_stack_panels(verts, stack_png)
        write_html(verts, edges, OUT_HTML)
        if args.deliver:
            shutil.copy2(core_png, OUT_PNG)
            shutil.copy2(stack_png, OUT_STACK)
            if not args.keep_tmp and TMP.exists():
                shutil.rmtree(TMP)
            stamp_ttl()
            print(f"DELIVERED {OUT_PNG}")
            print(f"DELIVERED {OUT_STACK}")
            print(f"DELIVERED {OUT_HTML}")
            print("TMP deleted" if not TMP.exists() else f"TMP kept {TMP}")
        else:
            stamp_ttl()
            print(f"TMP {core_png} {stack_png}")
        return 0
    pos = multipartite_pos(core)
    artifact = render_video(core, core_e, pos, TMP)
    if args.deliver:
        shutil.copy2(artifact, OUT_MP4)
        if not args.keep_tmp and TMP.exists():
            shutil.rmtree(TMP)
        stamp_ttl()
        print(f"DELIVERED {OUT_MP4}")
        print("TMP deleted" if not TMP.exists() else f"TMP kept {TMP}")
    else:
        stamp_ttl()
        print(f"TMP {artifact}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
