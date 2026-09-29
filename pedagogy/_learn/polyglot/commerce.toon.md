schema: learn/polyglot-commerce
kind: harvest-allocation
as_of: 2026-09-11
note: Particulars of attention for 神游 polyglot-harvest. Not CEFR. Not a Person. Do not invent bands beyond horizon.toon.md.

# Human 2026-09-11: 西语法语德语 currently first; rest still get ticks. Allocate by named priority + Berlin/EU commercial hooks, not invented dollar ranks.
named_priority[3]: es, fr, de
native_skip_learner_harvest[3]: en, zh, wuu
rest_cycle[10]: it, pt, ru, ja, ko, fi, vi, el, ar, hi

rotation:
  pattern: es, fr, de, es, fr, de, rest
  rest_pointer: ar
  last_lang: fr
  next_lang: de
  next_facet: hoeren
  facets[6]: lesen, hoeren, schreiben, sprechen, wortschatz, grammatik

why:
  de: Berlin hire + Goethe/DW public B2 materials. Horizon band professional_working — harvest maintains productive B2+, does not invent a new CEFR.
  es: limited_working gap + Instituto Cervantes CVC free ELE (lecturas, DELE modelos, podcast). EU/LATAM sidework GEO later; do not invent a client.
  fr: limited_working gap + TV5MONDE FLE video exercises (official). EU/francophone sidework GEO later; do not invent a client.
  rest: one slot after every two named-priority passes. Romance cluster it/pt sits next to es/fr. Do not skip elementary langs forever.

rule: One NEW sourced URL per polyglot-harvest tick. Skip if the same URL is already in harvest.toon.md. Do not invent drills as ANSWER. Do not pile DAY. Empty PROBE stays empty.
store: pedagogy/_learn/polyglot/harvest.toon.md
source: human 2026-09-11 named 西语法语德语优先 其余也照顾到
source: pedagogy/_learn/polyglot/horizon.toon.md
source: pedagogy/_learn/polyglot/skills.toon.md
