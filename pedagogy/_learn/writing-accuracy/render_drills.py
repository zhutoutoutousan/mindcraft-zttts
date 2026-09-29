#!/usr/bin/env python3
"""Render attested DE substitution drills to tmp HTML + optional local server.

  python pedagogy/_learn/writing-accuracy/render_drills.py
  python pedagogy/_learn/writing-accuracy/render_drills.py --serve
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "cron"))
import temp_ttl  # noqa: E402

DRILLS_SRC = Path(__file__).resolve().parent / "drills.toon.md"
HTML_OUT = temp_ttl.TMP / "pedagogy" / "de-drills.html"
PROGRESS = temp_ttl.TMP / "pedagogy" / "de-drills-progress.toon.md"
DEFAULT_PORT = 8766


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def parse_drills(text: str) -> dict:
    meta: dict[str, str] = {}
    items: list[dict] = []
    cur: dict | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("item:"):
            if cur:
                items.append(cur)
            cur = {}
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if cur is None:
            meta[key] = val
            continue
        if key == "choices":
            cur[key] = [p.strip() for p in val.split("|") if p.strip()]
        elif key == "accept":
            cur[key] = [p.strip() for p in val.split("|") if p.strip()]
        else:
            cur[key] = val
    if cur:
        items.append(cur)
    return {"meta": meta, "items": items}


def write_progress(payload: dict) -> None:
    items = payload.get("items") or {}
    if not isinstance(items, dict):
        items = {}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lines = [
        "schema: learn/writing-accuracy-drill-progress",
        f"updated: {now}",
        f"storageKey: {payload.get('storageKey') or 'mindcraft-de-drills-v1'}",
        f"source: {DRILLS_SRC.as_posix()}",
        "note: learner answers only. Do not invent ANSWER.",
        "",
        "rows[n]{id,ok,value}:",
    ]
    for kid, row in items.items():
        if not isinstance(row, dict):
            continue
        ok = str(row.get("ok") if row.get("ok") is not None else "").strip()
        val = str(row.get("value") or "").replace("\n", " ").strip()[:120]
        lines.append(f"  {kid},{ok},{val}")
    PROGRESS.parent.mkdir(parents=True, exist_ok=True)
    PROGRESS.write_text("\n".join(lines) + "\n", encoding="utf-8")
    temp_ttl.touch()


def render_html(bundle: dict) -> str:
    meta = bundle["meta"]
    items = bundle["items"]
    cards = []
    for i, it in enumerate(items, start=1):
        iid = html.escape(str(it.get("id") or f"i{i}"))
        kind = html.escape(str(it.get("kind") or "cloze"))
        prompt = html.escape(str(it.get("prompt") or ""))
        hint = html.escape(str(it.get("hint") or ""))
        stem = html.escape(str(it.get("stem") or ""))
        frame = html.escape(str(it.get("frame") or ""))
        point = html.escape(str(it.get("point") or ""))
        body = ""
        if it.get("kind") == "choice":
            radios = []
            for j, ch in enumerate(it.get("choices") or []):
                cid = html.escape(f"{it.get('id')}-{j}")
                lab = html.escape(ch)
                radios.append(
                    f'<label class="opt"><input type="radio" name="{iid}" value="{lab}"/> {lab}</label>'
                )
            body = f'<div class="opts">{"".join(radios)}</div>'
        elif it.get("kind") == "rewrite":
            body = (
                f'<p class="stem">{stem}</p>'
                f'<textarea data-id="{iid}" rows="3" lang="de" placeholder="Ein Satz auf Deutsch"></textarea>'
            )
        else:
            body = (
                f'<input type="text" data-id="{iid}" lang="de" autocomplete="off" '
                f'placeholder="Lücke füllen"/>'
            )
        point_html = f'<p class="point">考点: {point}</p>' if point else ""
        cards.append(
            f'<article data-id="{iid}" data-kind="{kind}">'
            f"<header><span>{i}/{len(items)}</span><strong>{frame}</strong></header>"
            f"{point_html}"
            f"<p>{prompt}</p>"
            f"{body}"
            f'<p class="hint" hidden>Hinweis: {hint}</p>'
            f'<p class="verdict" hidden></p>'
            f'<button type="button" class="check" data-id="{iid}">Prüfen</button>'
            f"</article>"
        )
    boot = {
        "storageKey": meta.get("storageKey") or "mindcraft-de-drills-v1",
        "updated": meta.get("updated") or "",
        "items": items,
        "server": True,
    }
    boot_json = json.dumps(boot, ensure_ascii=False).replace("</", "<\\/")
    body = "\n".join(cards)
    return HTML_TMPL.replace("%%BOOT%%", boot_json).replace("%%CARDS%%", body)


HTML_TMPL = r"""<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8"/>
  <title>Deutsch · Frames · lokale Speicherung</title>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <style>
    html, body { margin: 0; background: #0a0e14; color: #e8eef5; font-family: ui-sans-serif, system-ui; }
    main { max-width: 760px; margin: 0 auto; padding: 24px 20px 110px; }
    h1 { font-size: 22px; color: #69f0ae; margin: 0 0 8px; }
    .meta { color: #8b9bb4; margin: 0 0 16px; line-height: 1.45; }
    #progress { height: 8px; background: #2a3544; border-radius: 6px; overflow: hidden; margin: 0 0 18px; }
    #progress > span { display: block; height: 100%; width: 0; background: #69f0ae; }
    article { border: 1px solid #2a3544; border-radius: 12px; padding: 14px 16px; margin: 0 0 14px; background: #11161d; }
    article.ok { border-color: #004d40; }
    article.bad { border-color: #b71c1c; }
    article header { display: flex; gap: 10px; align-items: baseline; color: #80deea; margin-bottom: 8px; }
    article header span { color: #8b9bb4; font-size: 12px; }
    input[type="text"], textarea { width: 100%; box-sizing: border-box; background: #0a0e14; color: #e8eef5; border: 1px solid #2a3544; border-radius: 8px; padding: 10px; font: 15px/1.4 ui-sans-serif, system-ui; }
    .opts { display: flex; flex-wrap: wrap; gap: 10px; margin: 8px 0; }
    .opt { color: #90caf9; cursor: pointer; }
    .stem { color: #ce93d8; font-size: 14px; }
    .point { font-size: 13px; color: #80deea; margin: 0 0 8px; }
    .hint, .verdict { font-size: 13px; color: #8b9bb4; }
    .verdict.ok { color: #69f0ae; }
    .verdict.bad { color: #ef9a9a; }
    button.check { margin-top: 8px; background: #1a237e; color: #e8eef5; border: 1px solid #90caf9; padding: 6px 12px; cursor: pointer; border-radius: 8px; }
    .bar { position: sticky; bottom: 0; background: #0a0e14; border-top: 1px solid #2a3544; padding: 12px 20px; display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
    .bar button { background: #1a237e; color: #e8eef5; border: 1px solid #90caf9; padding: 10px 16px; cursor: pointer; border-radius: 8px; }
    button.done { background: #004d40; border-color: #69f0ae; }
    #status { color: #ce93d8; font-size: 13px; }
    code { color: #80deea; }
  </style>
</head>
<body>
  <main>
    <h1>Deutsch · Übungen zu deinem Kenntnisstand</h1>
    <p class="meta">Nur Frames aus deinen Sessions. Fortschritt liegt in <strong>localStorage</strong> und, wenn der lokale Server läuft, in <code>tmp/pedagogy/de-drills-progress.toon.md</code>. HTML neu erzeugen überschreibt die Antworten nicht. Nichts wird als STUDY ANSWER erfunden.</p>
    <div id="progress" aria-hidden="true"><span></span></div>
    %%CARDS%%
  </main>
  <div class="bar">
    <button type="button" id="check-all">Alle prüfen</button>
    <button type="button" id="save" class="done">Auf Platte schreiben</button>
    <button type="button" id="export">JSON exportieren</button>
    <button type="button" id="import">JSON importieren</button>
    <input id="import-file" type="file" accept="application/json" hidden/>
    <button type="button" id="hints">Hinweise</button>
    <button type="button" id="reset">Lokal zurücksetzen</button>
    <span id="status">idle</span>
  </div>
  <script>window.DRILLS_BOOT = %%BOOT%%;</script>
  <script>
    const BOOT = window.DRILLS_BOOT;
    const KEY = BOOT.storageKey;
    const byId = Object.fromEntries((BOOT.items || []).map((it) => [it.id, it]));

    function norm(s) {
      return String(s || "")
        .trim()
        .toLowerCase()
        .replace(/ß/g, "ss")
        .replace(/ä/g, "ae")
        .replace(/ö/g, "oe")
        .replace(/ü/g, "ue")
        .replace(/[.,!?]/g, "")
        .replace(/\s+/g, " ");
    }

    function load() {
      try {
        return JSON.parse(localStorage.getItem(KEY) || "null") || { v: 1, items: {} };
      } catch (_) {
        return { v: 1, items: {} };
      }
    }

    function saveLocal(state) {
      state.updated = new Date().toISOString();
      try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (_) {}
      paint(state);
    }

    function article(id) { return document.querySelector('article[data-id="' + id + '"]'); }

    function readValue(id) {
      const art = article(id);
      if (!art) return "";
      const kind = art.getAttribute("data-kind");
      if (kind === "choice") {
        const hit = art.querySelector("input[type=radio]:checked");
        return hit ? hit.value : "";
      }
      const field = art.querySelector("input[type=text], textarea");
      return field ? field.value : "";
    }

    function writeValue(id, value) {
      const art = article(id);
      if (!art) return;
      const kind = art.getAttribute("data-kind");
      if (kind === "choice") {
        art.querySelectorAll("input[type=radio]").forEach((el) => {
          el.checked = el.value === value;
        });
        return;
      }
      const field = art.querySelector("input[type=text], textarea");
      if (field) field.value = value || "";
    }

    function grade(id, value) {
      const it = byId[id];
      if (!it) return { ok: false, note: "" };
      const n = norm(value);
      if (!n) return { ok: false, note: "leer" };
      if (it.kind === "choice") {
        const ok = norm(it.answer) === n;
        return { ok, note: ok ? "stimmt" : "erwartet: " + it.answer };
      }
      if (it.kind === "rewrite") {
        const need = norm(it.mustInclude || "");
        const ok = need ? n.includes(need) : (it.accept || []).some((a) => n === norm(a));
        return { ok, note: ok ? "Kenntnisstand ist da" : "Modell: " + (it.accept && it.accept[0] || "") };
      }
      const ok = (it.accept || []).some((a) => n === norm(a) || n.endsWith(norm(a)) || norm(a).endsWith(n));
      const show = (it.accept && it.accept[0]) || "";
      return { ok, note: ok ? "stimmt" : "erwartet: " + show };
    }

    function snapshot() {
      const state = load();
      state.storageKey = KEY;
      state.items = state.items || {};
      for (const it of BOOT.items) {
        const value = readValue(it.id);
        const prev = state.items[it.id] || {};
        state.items[it.id] = Object.assign({}, prev, { value });
      }
      return state;
    }

    function applyCheck(id, state) {
      const value = readValue(id);
      const g = grade(id, value);
      const art = article(id);
      const verd = art.querySelector(".verdict");
      art.classList.toggle("ok", g.ok);
      art.classList.toggle("bad", !g.ok && !!value);
      verd.hidden = false;
      verd.className = "verdict " + (g.ok ? "ok" : "bad");
      verd.textContent = g.note;
      state.items[id] = { value, ok: g.ok, checkedAt: new Date().toISOString() };
    }

    function paint(state) {
      const rows = Object.values(state.items || {});
      const done = rows.filter((r) => r && r.ok === true).length;
      const total = BOOT.items.length;
      document.querySelector("#progress > span").style.width = (total ? (100 * done / total) : 0) + "%";
      const t = state.updated ? "gespeichert " + state.updated : "localStorage bereit";
      document.getElementById("status").textContent = done + "/" + total + " · " + t;
    }

    function restore() {
      const state = load();
      for (const it of BOOT.items) {
        const row = (state.items || {})[it.id];
        if (row && row.value) writeValue(it.id, row.value);
        if (row && row.ok === true) {
          const art = article(it.id);
          art.classList.add("ok");
        }
      }
      paint(state);
    }

    async function postSave(state) {
      try {
        const res = await fetch("/save", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify(state),
        });
        const data = await res.json();
        document.getElementById("status").textContent = data.ok
          ? "Platte: " + (data.path || "ok")
          : "Server abgelehnt";
      } catch (_) {
        document.getElementById("status").textContent = "Nur localStorage (kein Server)";
      }
    }

    document.addEventListener("input", () => saveLocal(snapshot()));
    document.addEventListener("change", () => saveLocal(snapshot()));

    document.querySelectorAll("button.check").forEach((btn) => {
      btn.addEventListener("click", () => {
        const state = snapshot();
        applyCheck(btn.getAttribute("data-id"), state);
        saveLocal(state);
      });
    });

    document.getElementById("check-all").onclick = () => {
      const state = snapshot();
      for (const it of BOOT.items) applyCheck(it.id, state);
      saveLocal(state);
    };

    document.getElementById("save").onclick = () => {
      const state = snapshot();
      saveLocal(state);
      postSave(state);
    };

    document.getElementById("export").onclick = () => {
      const blob = new Blob([JSON.stringify(snapshot(), null, 2)], { type: "application/json" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "de-drills-progress.json";
      a.click();
    };

    document.getElementById("import").onclick = () => document.getElementById("import-file").click();
    document.getElementById("import-file").onchange = (ev) => {
      const file = ev.target.files && ev.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        try {
          const data = JSON.parse(String(reader.result || "{}"));
          saveLocal(data);
          location.reload();
        } catch (_) {
          document.getElementById("status").textContent = "JSON ungültig";
        }
      };
      reader.readAsText(file);
    };

    document.getElementById("hints").onclick = () => {
      document.querySelectorAll(".hint").forEach((el) => { el.hidden = !el.hidden; });
    };

    document.getElementById("reset").onclick = () => {
      try { localStorage.removeItem(KEY); } catch (_) {}
      location.reload();
    };

    restore();
  </script>
</body>
</html>
"""


def validate_items(items: list[dict]) -> list[str]:
    """Drill quality per method.toon.md drillQuality (learner feedback 2026-09-08)."""
    problems: list[str] = []
    for it in items:
        iid = str(it.get("id") or "?")
        if not it.get("point"):
            problems.append(f"{iid}: missing `point` (考点 must be visible on the card)")
        if it.get("kind") == "cloze" and "___" not in str(it.get("prompt") or ""):
            problems.append(f"{iid}: cloze prompt has no ___ blank")
        if it.get("kind") == "rewrite" and not it.get("stem"):
            problems.append(f"{iid}: rewrite needs a stem sentence")
        if not (it.get("accept") or it.get("answer")):
            problems.append(f"{iid}: no accept/answer")
    return problems


def cmd_render() -> dict:
    bundle = parse_drills(_read(DRILLS_SRC))
    if not bundle["items"]:
        raise SystemExit(f"no drills in {DRILLS_SRC}")
    problems = validate_items(bundle["items"])
    if problems:
        raise SystemExit(
            "drill quality violations (method.toon.md drillQuality):\n  "
            + "\n  ".join(problems)
        )
    HTML_OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML_OUT.write_text(render_html(bundle), encoding="utf-8")
    temp_ttl.touch()
    return {"ok": True, "n": len(bundle["items"]), "html": str(HTML_OUT)}


def cmd_serve(host: str = "127.0.0.1", port: int = DEFAULT_PORT) -> None:
    info = cmd_render()
    html_bytes = HTML_OUT.read_bytes()

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"

        def log_message(self, fmt: str, *args) -> None:
            print("DRILLS " + (fmt % args), flush=True)

        def _send(self, code: int, ctype: str, raw: bytes) -> None:
            self.send_response(code)
            self.send_header("content-type", ctype)
            self.send_header("cache-control", "no-store")
            self.send_header("content-length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

        def _json(self, code: int, payload: dict) -> None:
            self._send(code, "application/json; charset=utf-8", json.dumps(payload).encode("utf-8"))

        def do_GET(self) -> None:
            path = self.path.split("?", 1)[0]
            if path in {"/", "/index.html", "/de-drills.html"}:
                self._send(200, "text/html; charset=utf-8", html_bytes)
                return
            if path == "/health":
                self._json(200, {"ok": True, "html": HTML_OUT.as_posix(), "n": info["n"]})
                return
            self.send_error(404)

        def do_POST(self) -> None:
            if self.path != "/save":
                self.send_error(404)
                return
            n = int(self.headers.get("content-length") or "0")
            raw = self.rfile.read(n) if n else b"{}"
            try:
                body = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                self._json(400, {"ok": False})
                return
            write_progress(body if isinstance(body, dict) else {})
            self._json(200, {"ok": True, "path": PROGRESS.as_posix()})

    class Server(HTTPServer):
        allow_reuse_address = False

        def handle_error(self, request, client_address) -> None:
            import traceback

            traceback.print_exc()

    last_err: OSError | None = None
    httpd = None
    bound = port
    for try_port in (port, 8776, 8786):
        try:
            httpd = Server((host, try_port), Handler)
            bound = try_port
            break
        except OSError as exc:
            last_err = exc
            httpd = None
    if httpd is None:
        raise SystemExit(f"drills-serve bind failed: {last_err}")
    print(f"DRILLS http://{host}:{bound}/", flush=True)
    print(f"DRILLS html {HTML_OUT.as_posix()}", flush=True)
    print(f"DRILLS progress {PROGRESS.as_posix()}", flush=True)
    httpd.serve_forever()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--serve", action="store_true")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=DEFAULT_PORT)
    args = p.parse_args()
    if args.serve:
        cmd_serve(host=args.host, port=args.port)
        return 0
    print(json.dumps(cmd_render(), ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
