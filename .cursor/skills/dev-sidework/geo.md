# GEO (generative engine optimization)

Job: get the **entity cited or recommended inside a synthesized answer**, not a blue-link rank. SEO is still the floor. Do not store brands, domains, NAP, or prompt logs in this file.

## Terms

| Label | Unit of success | Typical surface |
|-------|-----------------|-----------------|
| SEO | URL position in a link list | Classic web search |
| AEO | Your text *is* the extracted answer | Snippets, voice, some AI boxes |
| GEO | Your entity is *named/cited* in a generated answer | Chat-with-search, citation-first engines, search AI summaries |

Tactics overlap ~90%. Google Search Central: Search AI features have **no extra markup, no special AI files**. Indexed + snippet-eligible + people-first content. Same crawl/CDN/robots gates as Search.

Pipeline the agent must keep in mind: **retrieve → select passages → rewrite**. A buried claim in paragraph 4 loses to a 60–120 word self-contained block under a question heading.

## Evidence (do not sell as traffic)

Aggarwal et al., KDD 2024 / arXiv 2311.09735 (GEO-bench ~10k queries): adding **citations, statistics, quotations** lifted *share of the generated answer* on the order of **30–40%** on their visibility metrics. **Keyword stuffing** was flat or negative. Lower-ranked pages gained more than incumbents in that testbed. The 40% is **not** organic sessions.

Industry correlation (treat as signal, not causation): unlinked **brand mentions** across the web often track AI-overview visibility better than classic link metrics. Off-site entity consistency matters.

Recency: retrieval engines bias newer sources vs classic SEO for the same query. Stale pillars go dark.

Safety: engines apply quality/safety filters. Restricted / adult-adjacent offers are often **omitted or refused**, same class of problem as Maps stars. Do not forecast “best X in city” citations for a vertical the model will not recommend.

## Surfaces (classes)

1. **Search AI summaries / conversational search** — same web index as classic search. Ranking in the organic set is the usual ticket. Query fan-out: one user question becomes several sub-queries; a page must answer those sub-questions explicitly.
2. **Chat with live retrieval** — separate search crawlers from **training** crawlers. Blocking the search bot removes citations even if the training bot is allowed.
3. **Citation-first answer engines** — every answer shows sources; easiest to audit by hand.

Do not optimize one surface and call the program done.

## Technical (must)

| Check | Pass |
|-------|------|
| Search crawler | Classic search bot allowed in robots.txt **and** CDN/WAF. HTML text, not only JS/canvas/images |
| Retrieval crawlers | Allow that vendor’s **search/index** and **user-fetch** agents if citations are a goal. Training agents (`*Bot` for weight updates) are a separate opt-out |
| Google training token | `Google-Extended` opts out of some generative **training/grounding outside Search**. It is **not** the Search-index switch. Search AI features follow **Googlebot** + snippet controls (`nosnippet` / `noindex`) |
| `llms.txt` | Optional manifesto. Google Search ignores it. No proven citation lift. Do not spend a cycle on it before robots, HTML, schema |
| Schema | Matches **visible** text. `Organization` / `LocalBusiness` / `FAQPage` / `Article` when the page is actually that. No special “AI schema”. No duplicate blobs |
| SSR | Answer blocks in first HTML. Client-only games/widgets are invisible to retrieval |
| Canonical | One host, one URL per intent (same as crawl requirements) |

## On-page (must)

Lead each section with a **direct answer** (about 40–80 words, then expand). Question-shaped H2/H3. Lists and comparison tables when the query is comparative.

Self-contained claims: number + year + source in one sentence. No “as mentioned above”.

Princeton-style lifts only if the facts are **real**:

- Cite primary sources (do not invent papers).
- Attribute quotations to a real speaker the human confirms.
- Statistics with a date. Vague “many clients” fails extraction.

One pillar that covers fan-out beats ten thin cloned posts. Comparison / “best for / vs / alternatives / price” pages match how people prompt engines. Do not mass-generate generic wellness filler and call it GEO.

Entity: one brand string, one NAP, same as trust table. Mixed names and placeholder phones poison both SEO and GEO.

Freshness: quarterly pass on pages that should be cited; bump facts, not just the copyright year.

## Off-site (should)

Engines overweight a small set of third-party sources (encyclopedia, forums, video transcripts, category review sites, trade press). Unlinked mentions count. Earn listings the vertical **allows**. Do not fake encyclopedia entries, forum sockpuppets, or purchased reviews.

For local service: consistent entity on every directory that will host it; first-party Q&A on the site for prompts directories refuse.

## Measure

Fixed prompt set (buyer questions, not vanity). Re-run the **same** prompts on each surface monthly.

| KPI | Meaning |
|-----|---------|
| Mention rate | Share of prompts where the entity appears |
| Citation rate | Share where **your URL** is a source |
| Share of voice | Mentions / (you + named competitors) on the frozen set |
| Sentiment | Recommend vs warn vs omit |
| Search Console | Search AI clicks sit inside the Web performance report; no separate magic file required |
| Analytics | Referral from chat/answer hosts if they send any |

A 3–6 month trend is the shortest honest window. Do not treat a single chat session as a rank tracker.

Minimum audit without a vendor tool: 20–50 prompts × 2–3 surfaces, log mention / citation / error (wrong hours, wrong city, invented services). Fix the site facts that models are already hallucinating.

## Patch order (GEO layer, after trust + crawl)

1. Confirm retrieval crawlers are not blocked by robots **or** WAF.
2. Answer-first rewrite of money pages (home, services, price, FAQ). Unique titles already done.
3. Real stats/cites/quotes only; delete joke meta and keyword-stuffed titles (stuffing **hurts** GEO).
4. One entity in schema + visible NAP.
5. One comparison or FAQ block that matches actual prompts — not a cloned blog farm.
6. Prompt audit; correct factual drift on-page.
7. Off-site only where the category is allowed.

## Do not

- Promise AI-overview inclusion. Google does not guarantee crawl, index, or serving.
- Equate “+40% GEO” with sessions or bookings.
- Cloak a wrapper page for crawlers.
- Buy mentions, fake experts, or fabricated numbers.
- Ship `llms.txt` as the GEO deliverable.
- Forecast citations in a vertical the model’s safety stack will skip.
