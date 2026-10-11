---
name: fiverr-phish-guard
description: >-
  Judges Fiverr inbox messages, HTML "project" files, and off-platform links
  as phishing before anyone opens them. Use when the human names Fiverr,
  fiverr.com, a buyer chat, Subtitling, Untertitel, an HTML attachment, a
  Continue page, "work is sent", "please review", Betrug, or asks whether a
  freelance message is legitimate.
---

# Fiverr phish guard

A real order exists only in a session the human opened by typing `fiverr.com`. Buyers do not send HTML order confirmations. Fiverr staff do not ask in chat for a password, a card, or a QR code. HTTPS on any other host is not Fiverr.

Verdict in the first sentence. Read files as text. Do not open the link in a browser, do not preview the HTML, do not fetch the page body, do not repeat a live redirect (raw IP, `/go`, id parameter) as a clickable URL.

## Two shapes (2026-10-04, defanged)

**HTML lure.** Short page, one huge embedded image, title `Continue`. The picture impersonates Fiverr: service purchased, account verification still pending, brand green. A button and a few-second timer assign `window.location` to a host that is not `fiverr.com` — often a raw IP over plain `http`. Non-Apple browsers may swap the picture for one hosted on that same host. The file on disk is the lure. Harm starts when a browser follows the next host (fake login or a download). Reading the source in an editor does not run it.

**Chat link.** Display name looks generated (letters, underscore, digits). The text says the work is already sent and asks to review details at an external URL. Same campaign when the host was registered only days earlier and sits behind a proxy. Incident, do not visit: `donequickstone.com`, registered 2026-10-01, message 2026-10-04, name shape `cal_pyf` plus digits.

## Safe checks

- Host is exactly `fiverr.com` (or a subdomain of it). Anything else is off-platform.
- In HTML: title, button label, where `location` is assigned, and whether that host is `fiverr.com`.
- Domain age via RDAP only (`https://rdap.verisign.com/com/v1/domain/<host>` for `.com`). Registration within days of the message is a sign. DNS that lands on a CDN does not clear the host.
- Neighbor-address reputation only from public reports. Do not request the lure path.

## After a hit

- Do not click. If a browser already followed, close the tab and type nothing.
- A password typed on that page is changed only at `fiverr.com`, from a device that did not follow the link. Turn on two-factor authentication.
- Report and block inside Fiverr. Tell the human to delete the HTML. Delete it yourself only when they ask.
- Orders are checked by typing `fiverr.com`, not by the link in the chat.
---
