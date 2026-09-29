from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageFilter


def _erode_alpha(im: Image.Image, px: int = 2) -> Image.Image:
    r, g, b, a = im.convert("RGBA").split()
    a = a.filter(ImageFilter.MinFilter(2 * px + 1))
    out = Image.merge("RGBA", (r, g, b, a))
    return out


def matte_png(src: Path, dest: Path, model: str = "u2net") -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        from rembg import new_session, remove
    except ImportError as exc:
        raise SystemExit("pip install rembg onnxruntime pillow") from exc

    cache = getattr(matte_png, "_sessions", None)
    if cache is None:
        cache = {}
        matte_png._sessions = cache  # type: ignore[attr-defined]
    session = cache.get(model)
    if session is None:
        session = new_session(model)
        cache[model] = session

    with Image.open(src) as im:
        cut = remove(im, session=session)
        if not isinstance(cut, Image.Image):
            cut = Image.open(src).convert("RGBA")
        _erode_alpha(cut.convert("RGBA")).save(dest)
