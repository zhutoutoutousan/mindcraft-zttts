---
name: owa-eml-export
description: >-
  Export Outlook Web (OWA) mailbox messages one-by-one as .eml via Playwright
  attached to a debug Chrome session (CDP :9222). Use when the user asks to
  bulk-export Outlook web mail, download inbox as EML/MSG, automate
  Datei/Herunterladen or More items download, fix OWA RPA/Playwright export,
  or preserve evidence from outlook.cloud.microsoft before account lockout.
---

# OWA EML Export (Playwright + CDP) — single-file skill

**Portable:** copy this one `SKILL.md` anywhere. Extract the fenced files at the bottom when you need to run.

## When to use

- Inbox/folder dump from `outlook.cloud.microsoft`
- Desktop Outlook broken (`credential invalid 6008`, "use personal account") but **web still works**
- Evidence preservation before tenant/account lockout
- Prefer code over Power Automate Desktop

## Stack

| Piece | Choice |
|-------|--------|
| Lib | Playwright Python (`pip install playwright`) |
| Session | CDP attach `http://127.0.0.1:9222` to **user** Chrome |
| UI path | Email header **More items** `⋯` → **Herunterladen** → **Als EML herunterladen** |
| Avoid | Cursor IDE browser MCP; OWA multi-select export; MSA personal login for work mail |

## Reproduce (agent checklist)

```
- [ ] Close normal Chrome; run START_CHROME_DEBUG.bat
- [ ] User logs work/school account in that Chrome; open Inbox
- [ ] GET http://127.0.0.1:9222/json/version OK
- [ ] set PYTHONIOENCODING=utf-8 & PYTHONUNBUFFERED=1
- [ ] Smoke: python export_owa_eml.py --max 5 --out <dir>
- [ ] Expect 5 different .eml; then --max 800+
- [ ] Do not click Outlook while exporting
- [ ] Judge success by --out file count + Python "Saved N"; ignore flaky Windows find exit codes
```

## Correct download path (DE OWA)

1. Click list `[role="listbox"] [role="option"]` (`force=True`) until reading pane has body.
2. Ready signal: button **More items** (far-right on **email** row: Reactions/Reply/Forward/`⋯` — NOT top **Weitere Optionen**).
3. Open menu; scroll until leaf **Herunterladen**.
4. Hover `.fui-MenuItem` (`role=button`, `aria-haspopup=menu`) — not `role=menuitem`.
5. Click **Als EML herunterladen**.
6. `expect_download` → `save_as`.
7. **ArrowDown**; wait selection key change + More items back; dedupe `data-convid`/aria-label.

EN: More items / Download / Download as EML | Inbox | Reply.

## Hard rules

- Playwright+CDP only (unless user insists on PAD).
- Never drive Cursor browser for user mailbox.
- Never treat pasted OWA `appstate` as auth tokens.
- Do **not** Escape immediately before More items (collapses pane).
- Do **not** fall back to clicking first list row on failure (duplicate first mail).

## Pitfalls (field notes)

### Auth & session

| Pitfall | See | Fix |
|---------|-----|-----|
| Desktop dead, web OK | 6008; 改用个人帐户 | Stay on OWA; desktop hit MSA not Entra |
| Fresh debug profile | FIDO/PIN | User finishes biometrics once |
| Cursor browser | Login wall | CDP to user Chrome only |
| Pasted appstate | Feels like session | Not a token; PII risk |
| Debug profile | Re-login | `%LOCALAPPDATA%\ChromeDebugOWA` expected |

### Wrong UI

| Pitfall | See | Fix |
|---------|-----|-----|
| No mail open | Datei Herunterladen grey | Open body in reading pane |
| Top Weitere Optionen | Wrong menu | Email-header More items |
| Datei flyout | Submenu vanishes | Prefer More items path |
| menuitem Herunterladen | count 0 | Fluent button + haspopup |
| Below fold | Text missing | Scroll popover |
| Click without hover | No EML/MSG | mouseover then Als EML |

### Navigation

| Pitfall | See | Fix |
|---------|-----|-----|
| Virtual list index | Same mail twice | ArrowDown + key change + dedupe |
| rows.first fallback | Always mail #1 | Only click aria-selected=true |
| Escape before download | More items missing | Do not Escape before open menu |
| ArrowDown too fast | Empty pane | Wait/re-click selected |
| skip duplicate loop | End of list | Stop or scroll listbox |

### Tooling

| Pitfall | See | Fix |
|---------|-----|-----|
| PS heredoc python | Parse error | Write .py file |
| Piped stdout | Silent progress | PYTHONUNBUFFERED=1; watch folder |
| Emoji subjects | UnicodeEncodeError | PYTHONIOENCODING=utf-8 |
| Multi-select Relevant | No export | One-by-one; never leeren |
| find exit 2 | False failure | Trust Python Saved N |
| "Control my Chrome" | No CDP | Start debug Chrome |

## Extract & run these files

Save the following blocks as sibling files next to each other, then run.

### File: `requirements.txt`

```
playwright>=1.40.0
```

### File: `START_CHROME_DEBUG.bat`

```bat
@echo off
REM Close ALL Chrome windows first, then run this bat.
REM Opens Chrome with remote debugging so Playwright can attach to your Outlook login.

set PORT=9222
set PROFILE=%LOCALAPPDATA%\ChromeDebugOWA

echo.
echo === Start Chrome with debugging on port %PORT% ===
echo 1) Close every Chrome window completely.
echo 2) This window will start a fresh Chrome profile folder:
echo    %PROFILE%
echo 3) In that Chrome, login Outlook once, open inbox, then run export_owa_eml.py
echo.

taskkill /IM chrome.exe /F >nul 2>&1
timeout /t 2 /nobreak >nul

start "" "%ProgramFiles%\Google\Chrome\Application\chrome.exe" ^
  --remote-debugging-port=%PORT% ^
  --user-data-dir="%PROFILE%" ^
  "https://outlook.cloud.microsoft/mail/"

if errorlevel 1 (
  start "" "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" ^
    --remote-debugging-port=%PORT% ^
    --user-data-dir="%PROFILE%" ^
    "https://outlook.cloud.microsoft/mail/"
)

echo Chrome started. Login if needed, then:
echo   python export_owa_eml.py
echo.
pause

```

### File: `RUN_EXPORT.bat`

```bat
@echo off
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
echo Saving to: %~dp0..\mail-eml
echo Keep the debug Chrome window open. Do not use the mouse on Outlook while exporting.
python export_owa_eml.py --max 800 --format eml --delay-ms 700
echo.
echo Done. Open folder:
explorer "%~dp0..\mail-eml"
pause

```

### File: `export_owa_eml.py`

```python
# -*- coding: utf-8 -*-
"""
Open-source RPA-ish export for Outlook Web (OWA) via Playwright.

Uses: Playwright (Apache-2.0) — https://github.com/microsoft/playwright-python

What it does
------------
Attaches to Chrome started with --remote-debugging-port=9222,
opens each mail in the current list, and downloads via:
  Datei -> Herunterladen -> Als EML herunterladen
one by one.

How to run
----------
1) Double-click START_CHROME_DEBUG.bat  (closes normal Chrome first)
2) In that Chrome, log into your OWA account if needed
3) Optionally search (e.g. Formal Notice) so the list is filtered
4) python export_owa_eml.py
   python export_owa_eml.py --max 30
   python export_owa_eml.py --format msg
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path

from playwright.sync_api import TimeoutError as PwTimeout
from playwright.sync_api import sync_playwright

CDP_URL = "http://127.0.0.1:9222"
# Default next to CWD so the skill copy is portable; override with --out
OUT_DIR = Path.cwd() / "mail-eml"
OUTLOOK_HOST_HINTS = ("outlook.cloud.microsoft", "outlook.office.com", "outlook.office365.com")


def sanitize(name: str, max_len: int = 80) -> str:
    name = re.sub(r"[\\/:*?\"<>|\r\n\t]+", "_", name).strip(" ._")
    return (name or "mail")[:max_len]


def find_outlook_page(browser):
    for ctx in browser.contexts:
        for page in ctx.pages:
            url = (page.url or "").lower()
            if any(h in url for h in OUTLOOK_HOST_HINTS):
                return page
    # fallback: first page
    for ctx in browser.contexts:
        if ctx.pages:
            return ctx.pages[0]
    return None


def reading_pane_ready(page) -> bool:
    """True when a mail is open in the reading pane."""
    try:
        if page.get_by_role("button", name="More items").count():
            if page.get_by_role("button", name="More items").last.is_visible(timeout=300):
                return True
    except Exception:
        pass
    for name in (r"^Antworten$", r"^Antwort$", r"^Reply$"):
        btn = page.get_by_role("button", name=re.compile(name, re.I))
        try:
            if btn.count() and btn.first.is_visible(timeout=300):
                return True
        except Exception:
            continue
    return False


def message_rows(page):
    """Mail list rows in the middle pane."""
    # OWA list items are often role=option inside a listbox
    opts = page.locator('[role="listbox"] [role="option"]')
    if opts.count() > 0:
        return opts
    opts = page.locator('[role="option"]')
    if opts.count() > 0:
        return opts
    return page.locator('[data-convid], [data-selection-index]')


def selected_mail_key(page) -> str:
    """Stable-ish id for currently selected list row."""
    return page.evaluate(
        """() => {
          const o = document.querySelector('[role="option"][aria-selected="true"]');
          if (!o) return '';
          return (o.getAttribute('data-convid')
            || o.getAttribute('data-selection-index')
            || o.getAttribute('aria-label')
            || o.innerText
            || '').slice(0, 180);
        }"""
    ) or ""


def ensure_mail_selected(page, index: int = 0) -> bool:
    """Click a list row so the reading pane loads. Return True if ready."""
    page.keyboard.press("Escape")
    page.wait_for_timeout(200)

    rows = message_rows(page)
    n = rows.count()
    if n == 0:
        print("  !! no mail rows found in list")
        return False
    idx = min(index, n - 1)
    rows.nth(idx).scroll_into_view_if_needed()
    rows.nth(idx).click(timeout=8000, force=True)
    page.wait_for_timeout(900)
    for _ in range(20):
        if page.get_by_role("button", name="More items").count():
            try:
                if page.get_by_role("button", name="More items").last.is_visible(timeout=400):
                    return True
            except Exception:
                pass
        page.wait_for_timeout(250)
    page.keyboard.press("Enter")
    page.wait_for_timeout(900)
    return page.get_by_role("button", name="More items").count() > 0


def wait_more_items(page, tries: int = 25) -> bool:
    for _ in range(tries):
        more = page.get_by_role("button", name="More items")
        try:
            if more.count() and more.last.is_visible(timeout=300):
                return True
        except Exception:
            pass
        page.wait_for_timeout(200)
    return False


def go_next_mail(page, prev_key: str) -> bool:
    """Move to next mail via ArrowDown; wait until reading pane is ready."""
    # Close any open menus without clearing selection if possible
    page.keyboard.press("Escape")
    page.wait_for_timeout(120)
    for _ in range(8):
        page.keyboard.press("ArrowDown")
        page.wait_for_timeout(450)
        key = selected_mail_key(page)
        if key and key != prev_key:
            if wait_more_items(page):
                return True
            # selection changed but pane slow — click selected row
            page.locator('[role="option"][aria-selected="true"]').first.click(force=True)
            page.wait_for_timeout(700)
            if wait_more_items(page):
                return True
    page.evaluate(
        """() => {
          const lb = document.querySelector('[role="listbox"]');
          if (lb) lb.scrollTop += 280;
        }"""
    )
    page.wait_for_timeout(400)
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(800)
    return wait_more_items(page)


def _open_more_actions(page) -> None:
    """Open email reading-pane header ⋯ = button 'More items' (far right)."""
    if not wait_more_items(page):
        # one recovery click on selected row
        sel = page.locator('[role="option"][aria-selected="true"]')
        if sel.count():
            sel.first.click(force=True)
            page.wait_for_timeout(900)
    more = page.get_by_role("button", name="More items")
    if not (more.count() and more.last.is_visible()):
        raise RuntimeError("Email-window header ⋯ (More items) not found — is a mail open?")
    more.last.click(timeout=5000)
    page.wait_for_timeout(500)


def click_download_menu(page, fmt: str) -> None:
    """More items ⋯ -> scroll -> hover Herunterladen -> Als EML/MSG."""
    label = "Als EML herunterladen" if fmt == "eml" else "Als MSG herunterladen"

    # Do NOT Escape here — it can collapse the reading pane in OWA.
    _open_more_actions(page)

    for _ in range(16):
        if page.evaluate(
            """() => !![...document.querySelectorAll('*')].find(e =>
              e.childElementCount===0 && (e.innerText||'').trim()==='Herunterladen' && e.getClientRects().length)"""
        ):
            break
        page.mouse.move(1300, 480)
        page.mouse.wheel(0, 240)
        page.wait_for_timeout(100)

    opened = page.evaluate(
        r"""() => {
          const leaf = [...document.querySelectorAll('*')].find(e =>
            e.childElementCount===0 && (e.innerText||'').trim()==='Herunterladen');
          if (!leaf) return false;
          const item = leaf.closest('.fui-MenuItem') || leaf.parentElement;
          item.scrollIntoView({block:'nearest'});
          const r = item.getBoundingClientRect();
          const x = r.right - 6, y = r.top + r.height/2;
          for (const type of ['pointerover','pointerenter','mouseover','mouseenter','mousemove']) {
            item.dispatchEvent(new MouseEvent(type, {bubbles:true, clientX:x, clientY:y}));
          }
          return true;
        }"""
    )
    if not opened:
        raise RuntimeError("Herunterladen not found in More items menu (scroll?)")
    page.wait_for_timeout(650)

    clicked = page.evaluate(
        """(label) => {
          const el = [...document.querySelectorAll('*')].find(e => (e.innerText||'').trim()===label);
          if (!el) return false;
          (el.closest('.fui-MenuItem') || el).click();
          return true;
        }""",
        label,
    )
    if not clicked:
        raise RuntimeError(f"Submenu item not found: {label}")
    page.wait_for_timeout(200)


def current_subject(page) -> str:
    key = selected_mail_key(page)
    if key:
        # aria-label often starts with sender then subject
        parts = re.split(r"\s{2,}|\n", key)
        guess = parts[0] if parts else key
        return sanitize(guess)[:80]
    for sel in (
        '[data-app-section="ConversationReadingPane"] [role="heading"]',
        '[data-app-section="ConversationReadingPane"] h1',
        '[aria-label*="Betreff"]',
        '[role="main"] h1',
    ):
        loc = page.locator(sel).first
        try:
            if loc.count() and loc.is_visible(timeout=500):
                t = (loc.inner_text(timeout=1000) or "").strip().split("\n")[0]
                bad = {"navigationsbereich", "inbox", "posteingang", "mail"}
                if t and t.lower() not in bad and len(t) < 200:
                    return sanitize(t)
        except Exception:
            continue
    return "mail"


def goto_inbox(page) -> None:
    """Focus Inbox folder if possible."""
    for name in ("Inbox", "Posteingang"):
        loc = page.get_by_role("treeitem", name=re.compile(rf"^{name}", re.I))
        if loc.count() == 0:
            loc = page.get_by_text(name, exact=True)
        try:
            if loc.count() and loc.first.is_visible(timeout=800):
                loc.first.click(timeout=5000)
                page.wait_for_timeout(1200)
                return
        except Exception:
            continue


def export_loop(page, out_dir: Path, fmt: str, max_count: int, delay_ms: int) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    saved = 0
    fails = 0
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    seen: set[str] = set()

    print(f"Output: {out_dir}")
    print(f"Format: .{fmt}  max={max_count}")
    print("---")

    goto_inbox(page)
    if not ensure_mail_selected(page, index=0):
        print("!! could not open first inbox mail")
        return 0

    for i in range(max_count):
        key = selected_mail_key(page)
        if key and key in seen:
            print(f"[{i+1}/{max_count}] skip duplicate, advancing...")
            if not go_next_mail(page, key):
                print("!! no more mails to advance to")
                break
            continue
        if key:
            seen.add(key)

        subj = current_subject(page)
        print(f"[{i+1}/{max_count}] {subj[:70]}")

        try:
            with page.expect_download(timeout=25000) as dl_info:
                click_download_menu(page, fmt)
            download = dl_info.value
            suggested = download.suggested_filename or f"{subj}.{fmt}"
            stem = sanitize(Path(suggested).stem)
            final = out_dir / f"{stamp}_{i+1:04d}_{stem}.{fmt}"
            # avoid overwrite if same stem
            if final.exists():
                final = out_dir / f"{stamp}_{i+1:04d}_{stem}_{saved+1}.{fmt}"
            download.save_as(str(final))
            print(f"  -> {final.name} ({final.stat().st_size} bytes)")
            saved += 1
            fails = 0
        except Exception as e:
            fails += 1
            print(f"  !! failed: {e}")
            try:
                page.keyboard.press("Escape")
            except Exception:
                pass
            if fails >= 8:
                print("!! too many consecutive failures, stopping")
                break

        page.wait_for_timeout(delay_ms)
        prev = key or selected_mail_key(page)
        if not go_next_mail(page, prev):
            print("!! reached end of loaded list")
            break

    print(f"Unique keys seen: {len(seen)}")
    return saved


def main() -> int:
    ap = argparse.ArgumentParser(description="Export OWA mails one-by-one as EML/MSG via Playwright")
    ap.add_argument("--cdp", default=CDP_URL, help="Chrome DevTools endpoint")
    ap.add_argument("--out", type=Path, default=OUT_DIR, help="Output folder")
    ap.add_argument("--format", choices=("eml", "msg"), default="eml")
    ap.add_argument("--max", type=int, default=500, help="Max mails to export this run")
    ap.add_argument("--delay-ms", type=int, default=800, help="Pause between mails")
    args = ap.parse_args()

    print(f"Connecting to Chrome at {args.cdp} ...")
    print(f"Saving into: {args.out.resolve()}")
    try:
        with sync_playwright() as p:
            browser = p.chromium.connect_over_cdp(args.cdp)
            page = find_outlook_page(browser)
            if page is None:
                print("No browser page found. Is Chrome running with --remote-debugging-port=9222?")
                return 2
            page.bring_to_front()
            print(f"Attached: {page.url}")
            n = export_loop(page, args.out, args.format, args.max, args.delay_ms)
            print(f"Done. Saved {n} file(s) -> {args.out.resolve()}")
            return 0 if n else 1
    except Exception as e:
        print("Cannot attach to Chrome.")
        print(f"  {e}")
        print()
        print("Fix:")
        print("  1) Run START_CHROME_DEBUG.bat")
        print("  2) Login Outlook in that Chrome window")
        print("  3) Open Inbox, then re-run this script")
        return 2


if __name__ == "__main__":
    sys.exit(main())

```
