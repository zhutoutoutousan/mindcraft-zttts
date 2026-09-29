# Generic site work requirements

Apply to any 杂活 local-service / booking site. Fill facts from the live page or the human. Do not copy identity into this file.

## Traffic

- Period totals that include a sharp spike are lagging averages. Read the daily curve.
- If one referrer (usually web search) is most of the traffic and the host still serves, treat a collapse as **ranking / quality**, not hosting.
- A one-week head-term spike on a thin or mixed-intent domain is often a volatility borrow. It is not a KPI.
- Restricted or adult-adjacent offers are impression-capped (SafeSearch, spam/quality). Do not forecast hotel-spa type head terms.

## Trust (must be true on every locale)

| Check | Pass |
|-------|------|
| One brand string | Header, title, schema `name`, footer, OG agree |
| One NAP | Phone, email, hours, address identical on home, booking, contact, footer, JSON-LD |
| No placeholders | Reject obvious template phones, US-style dummy numbers, unused `@` mailboxes |
| Hours | Door hours = schema = booking copy. No 24/7 vs Sunday-closed split |
| Currency | One currency on the booking form; listed prices match the menu |
| Booking | CTA actually works. “System under development” is a conversion defect if you still ask for leads |
| Titles | Unique per URL. Home ≠ booking ≠ service. No keyword stuffing of unrelated products into every `<title>` |
| H1 | Names the real service + locality intent. Not stock wellness filler on a different offer |
| Social proof | Only first-party, dated, consented. No invented distant-city quotes. No review widget until a collect path exists |
| Schema | One `LocalBusiness` (or subtype). Real `image`/`logo` URLs (not 404). No duplicate blobs. Geo/hours match the door |
| Games / toys | Optional below the booking path. Not the SEO H1 |

## Crawl

| Check | Pass |
|-------|------|
| Host | Redirect host = canonical = sitemap `<loc>` = hreflang = OG url = JSON-LD `@id` = robots Host |
| Sitemap | HTTP 200 on GET; `lastmod` moves when pages change; GSC fetch agrees |
| i18n | Each locale has its own URLs and titles; do not clone filler posts across languages as “content” |
| Indexing | `index,follow` only on URLs you want ranked |

## GEO

Citation inside generated answers is a **separate KPI** from organic sessions. Do the trust + crawl tables first, then [geo.md](geo.md).

Short version: answer-first HTML, real numbers/cites, one entity, allow **retrieval** crawlers, do not block classic search bots, do not treat `llms.txt` as work done. Restricted verticals are often skipped by model safety — same honesty rule as directory stars.

## Reviews

- Maps / major local directories restrict or strip sexually explicit and many adult-themed reviews. Do not promise a public star flywheel in those verticals.
- Honest channel: post-visit first-party (chat app / SMS / on-site form). Never buy or fabricate reviews.

## Patch order (when the site repo is open)

1. One host (canonical stack matches the live redirect).
2. One NAP (delete placeholders unless the human confirms that mailbox/number is real).
3. Unique titles; one intent per URL.
4. Remove fake social proof; add first-party collection only if asked.
5. Schema: one blob, real asset URLs, hours that match.
6. Booking: one currency, working contact CTA, drop “under development” if taking requests.
7. Homepage: service H1 first; demote games.
8. Regenerated sitemap; confirm crawl 200.
9. GEO layer ([geo.md](geo.md)): retrieval crawlers, answer-first money pages, prompt audit. Not more blog posts.

## Will not come back from CSS

Spike-week daily counts. Directory stars for a restricted vertical. Ranking as a luxury generic-category head term against established hotels. A search engine the property never ranked in.

Success: crawl-clean Search Console, one reachable phone, stable brand + honest long-tail queries.

## Do not

Cloak. Buy reviews or AI mentions. Mass-generate generic blog articles. Invent statistics or expert quotes for GEO. Write people names, brands, domains, NAP, or booking dumps into this skill.
