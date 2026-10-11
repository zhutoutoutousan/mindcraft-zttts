---
schema: writing-accuracy-session
date: 2026-10-09
id: 2026-10-09-bier-weggelassen
lang: de
meta:
  task: nutrition
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Bier weggelassen nach Empfehlung; Tagesstand korrigiert
original: "Also habe ich den Bier weggelassen, was gibt's danach?"
corrected: "Also habe ich das Bier weggelassen. Was gibt es danach?"
oneFocus: "das Bier (Neutrum) → Akkusativ: das Bier weggelassen, nicht den Bier"
reuseNextSession: "Ich habe das Bier weggelassen."
errorTypes:
  - case_gender_article
  - zeichensetzung
gaps: []
confidence: high
errors_brief:
  - type: case_gender_article
    original: "den Bier"
    corrected: "das Bier"
    rule: "Bier ist Neutrum (das Bier); Akkusativ Singular Neutrum = das"
  - type: zeichensetzung
    original: "weggelassen, was gibt's danach?"
    corrected: "weggelassen. Was gibt es danach?"
    rule: "Neuer Hauptsatz → Punkt und Großschreibung, kein Komma"
  - type: stil
    original: "gibt's danach"
    corrected: "gibt es danach"
    rule: "In Schriftsprache 'es' ausschreiben; 'gibt's' umgangssprachlich"
