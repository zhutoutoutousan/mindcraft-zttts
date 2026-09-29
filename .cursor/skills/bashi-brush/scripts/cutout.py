"""Flood the white margin of a reference still. Interior whites (eyes) stay.

Writes tmp/bashi-brush/roo.png. Straight alpha, RGB 0 where cleared.
"""

import argparse
import os
from collections import deque

from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", "..", ".."))
WORK = os.path.join(REPO, "tmp", "bashi-brush")


def cutout(src, out, threshold):
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    px = im.load()

    def is_bg(r, g, b):
        return r > threshold and g > threshold and b > threshold

    seen = bytearray(w * h)
    q = deque()

    def push(x, y):
        i = y * w + x
        if seen[i]:
            return
        r, g, b, _a = px[x, y]
        if not is_bg(r, g, b):
            return
        seen[i] = 1
        q.append((x, y))

    for x in range(w):
        push(x, 0)
        push(x, h - 1)
    for y in range(h):
        push(0, y)
        push(w - 1, y)
    while q:
        x, y = q.popleft()
        px[x, y] = (0, 0, 0, 0)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    push(nx, ny)

    minx, miny, maxx, maxy = w, h, 0, 0
    opaque = leftover = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if not a:
                continue
            opaque += 1
            if is_bg(r, g, b):
                leftover += 1
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
    if opaque == 0:
        raise SystemExit("cutout removed everything; raise nothing, lower --threshold only if the photo is not white-backed")
    box = (max(0, minx - 1), max(0, miny - 1), min(w, maxx + 2), min(h, maxy + 2))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.crop(box).save(out)
    print(f"wrote {out} crop={box} opaque={opaque} leftover_white={leftover}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Reference photo, white background")
    ap.add_argument("--out", default=os.path.join(WORK, "roo.png"))
    ap.add_argument("--threshold", type=int, default=230)
    args = ap.parse_args()
    cutout(args.src, args.out, args.threshold)


if __name__ == "__main__":
    main()
