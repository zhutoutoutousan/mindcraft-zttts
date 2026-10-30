schema: learn/writing-accuracy-session
date: 2026-10-08
id: leberkaese-mit-freundin
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Foto-Logging Essen (Leberkaese + Wurstsemmel, geteilt) -> neuer Tagesabschnitt in .private/nutrition.toon.md; Sprachteil = Datumsatz + Komma-Spleiss.
original: "Heute ist 8.10.2026, habe ich diese mit meiner Freundin zusammen gegessen"
corrected: "Heute ist der 8.10.2026. Das habe ich zusammen mit meiner Freundin gegessen."
oneFocus: "Satzgrenze nach Datumsangabe: [Heute ist der + Datum]. + neuer Satz [Das] + [V2]; Rueckbezug aufs Essen = das, nicht diese"
reuseNextSession: "Heute ist der 8.10.2026. Das habe ich zusammen mit meiner Freundin gegessen."
errorTypes: wortstellung,artikel,pronomen
gaps: Heute ist 8.10.2026, habe ich -> Heute ist der 8.10.2026. Das habe ich (Komma verbindet keine zwei Hauptsätze -> Punkt; Datum mit Artikel der; diese -> das als Rueckbezug)
confidence: high

errors_brief[3]:
  "Heute ist 8.10.2026, habe ich -> Heute ist der 8.10.2026. Das habe ich: Komma-Spleiss (zwei Hauptsätze) -> Punkt; Datum mit Artikel (der 8.10.)."
  "diese -> das: diese braucht ein Nomen dahinter; Bezug auf das Essen = das/dieses."
  "mit meiner Freundin zusammen gegessen -> zusammen mit meiner Freundin gegessen (Standard-Konnektor; umgangssprachlich ok)."
