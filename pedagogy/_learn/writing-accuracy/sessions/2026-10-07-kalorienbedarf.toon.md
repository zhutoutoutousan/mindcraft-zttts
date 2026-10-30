schema: learn/writing-accuracy-session
date: 2026-10-07
id: kalorienbedarf-2026-10-07
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: TDEE-Frage pro Person ([Name]/Partnerin).
original: "Wie viel Kalorien benötigt für jeder überhaupt?"
corrected: "Wie viele Kalorien benötigt jeder überhaupt?"
oneFocus: "Fragesatz ohne 'fuer': [Wer] benoetigt [was]? -- jeder als Subjekt, kein fuer"
reuseNextSession: "Wie viele Kalorien benötigt jeder überhaupt?"
errorTypes: [praeposition_interferenz, quantor, kasus]
gaps:
  - gap: "benötigt für jeder"
    hit: "benötigt jeder"
    frame: "[Wer] benoetigt [was]?"
confidence: high

errors_brief:
  - "benötigt für jeder -> benötigt jeder: 'fuer' (aus 'for each') entfaellt; 'jeder' ist Subjekt im Nominativ."
  - "Wie viel Kalorien -> Wie viele Kalorien: zaehlbare Einheit -> wie viele (Wiederholung von gestrigem Frame)."
  - "Loesung kurz: eine Frage = Verb an Position 2, Subjekt danach, kein Ueberschuss-Element."
