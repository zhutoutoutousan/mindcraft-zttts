schema: learn/writing-accuracy-session
date: 2026-10-01
id: koerpergroesse
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Body stats + question whether to eat more. "Körperentzug" read as Klimmzug (15 Wdh). No PII.
original: Also gut, da wiege ich [Gewicht], Körper Größe [Groesse], Muskelaufbau überdurchschnittlich, Körperentzug 15 wdh. So soll ich mehr verzehren?
corrected: Also gut, ich wiege [Gewicht] bei einer Körpergröße von [Groesse], mein Muskelaufbau ist überdurchschnittlich, Klimmzug: 15 Wiederholungen. Soll ich mehr verzehren?
oneFocus: Kompositum-Frame — Körpergröße zusammenschreiben (Körper + Größe -> Körpergröße)
reuseNextSession: bei einer Körpergröße von [Groesse]
errorTypes: compound_noun_split, unit_format, word_choice, sentence_structure
gaps: Körper Größe -> Körpergröße (Kompositum); [Groesse] -> [Groesse] (Einheit mit Leerzeichen); Körperentzug -> Klimmzug (Wortverwechslung); "So soll ich..." -> "Soll ich..." (So als Fragebeginn weglassen)
confidence: high

errors_brief[3]:
  Körper Größe -> Körpergröße (Kompositum zusammenschreiben)
  [Groesse] -> [Groesse] (Leerzeichen vor Einheit)
  Körperentzug -> Klimmzug (Wortverwechslung)
