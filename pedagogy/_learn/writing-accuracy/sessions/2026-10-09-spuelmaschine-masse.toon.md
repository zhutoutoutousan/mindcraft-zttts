---
schema: writing-accuracy-session
date: 2026-10-09
id: 2026-10-09-spuelmaschine-masse
lang: de
meta:
  task: kleinanzeigen-listing
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Midea ST 5.31 wi Maße aus EU-Datenblatt (Handbuch)
original: "Spülmaschine, Maße, cm naja"
corrected: "Welche Maße hat die Spülmaschine – in cm?"
oneFocus: "W-Frage mit Verb an Position 2: Welche Maße hat die Spülmaschine?"
reuseNextSession: "Welche Maße hat die Spülmaschine?"
errorTypes:
  - syntax
  - register
gaps: []
confidence: high
errors_brief:
  - type: syntax
    original: "Spülmaschine, Maße, cm?"
    corrected: "Welche Maße hat die Spülmaschine?"
    rule: "W-Frage: W-Fragepronomen + Verb an Position 2 + Subjekt; keine Stichwortkette mit Kommas"
  - type: register
    original: "naja"
    corrected: "(Weglassen)"
    rule: "'naja' als Satzanker ist gesprochene Füllung; in Schrift weglassen oder durch klare Einleitung ersetzen"
