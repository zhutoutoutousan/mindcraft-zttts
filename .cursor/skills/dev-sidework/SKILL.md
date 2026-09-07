---
name: dev-sidework
description: >-
  Generic work requirements for side-job / 杂活 client sites (local service,
  booking, i18n, SEO, GEO / AEO, reviews). Use when the human names 杂活,
  development skills, side site, 流量下滑, SEO, GEO, 生成式引擎, AEO, AI Overview,
  AI Mode, citation, ChatGPT, Perplexity, 评价, booking form, NAP, canonical,
  or asks to patch a paid site from another repo.
---

# Dev sidework (杂活)

Work requirements for client/side websites. Pedagogy skills stay in sibling `.cursor/skills/*`. Do not mix PROBE/ANSWER or `.private/` into these files.

Source is usually a **different repo**. Diagnose against the live URL the human names; patch only when that repo is open. Lasting process notes stay in this skill as **generic rules**, never as a tenant dossier. Do not write people names, brand names, domains, phones, emails, or street addresses into this folder.

Checklists: [requirements.md](requirements.md). GEO / AEO: [geo.md](geo.md).

## Hard rules

- Do not invent phones, hours, prices, addresses, or reviews.
- Do not store NAP, client identity, or testimonials in the skill. Read them from the live site or the human.
- One NAP tuple site-wide. Template/placeholder contact is a defect.
- Title, H1, meta, and body must share one intent. Do not cloak a restricted offer behind unrelated wrapper copy.
- Do not write invented testimonials (wrong city, stock names, undated quotes).
- Do not promise Maps / directory star recovery for verticals those surfaces restrict.
- Traffic: fix trust + crawl first. Do not spray generic blog posts. Do not treat a short ranking spike as the baseline.
- GEO is citation inside a generated answer, not a new rank tracker. Do not sell paper visibility lifts as sessions. Do not invent quotes, stats, or third-party mentions. `llms.txt` is optional and unproven.

## When invoked

1. Ask or use the live URL the human already gave. Do not persist it here.
2. Re-check stale facts on the live host: sitemap HTTP, canonical vs redirect host, NAP on home vs booking vs JSON-LD vs footer.
3. Apply [requirements.md](requirements.md) in listed order, then the GEO layer in [geo.md](geo.md).
4. Separate **broken on the site** from **will not return** (spike traffic, restricted-vertical directory stars, AI safety omissions).
