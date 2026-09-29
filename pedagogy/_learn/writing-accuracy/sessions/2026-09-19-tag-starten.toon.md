schema: learn/writing-accuracy-session
date: 2026-09-19
id: tag-starten
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Day-start prompt for the daily brief. No PII in this session.

original: Guten Morgen, es ist jetzt 19.9 heute, starten Sie meinen Tag

corrected: Guten Morgen, heute ist der 19.9. – starten Sie meinen Tag.

oneFocus: Heute ist der 19.9. (V2-Datumsangabe)
oneFocusFrame: date_v2
reuseNextSession: Heute ist der 19.9. – starten Sie meinen Tag.
errorTypes: word_order punctuation
confidence: high

errors_brief[2]:
  es ist jetzt 19.9 heute → heute ist der 19.9. (V2: „heute" auf Position 1, Verb bleibt auf Position 2)
  fehlende Punkte: nach „19.9" und am Satzende vor „starten"
