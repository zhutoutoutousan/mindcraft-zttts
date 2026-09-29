schema: learn/writing-accuracy-session
date: 2026-09-19
id: zusammenfassung-politik
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Block A Zusammenfassung DLF-Kommentar + Bitte Politik-Basics in den Graph
original: |-
  Bei CDU sieht es nicht so gut aus. In Mecklenburg Vorpommern hat SPD besiegelt, die vor vorhanden Kanzler sehr schrecklich.
  Hinweise: Fügen Sie die grundlegenden Kenntnisse auf Deutsch Politik zur Kenntnis-graph hinzu. Bei mir fehlt es strukturierte Kenntnisse
corrected: |-
  Der CDU geht es schlecht: In Mecklenburg-Vorpommern hat die SPD gesiegt, und der amtierende Kanzler schneidet sehr schlecht ab.
  Fügen Sie die grundlegenden Kenntnisse zur deutschen Politik dem Wissensgraph hinzu. Mir fehlen strukturierte Kenntnisse.
oneFocus: hat die SPD gesiegt — gesiegt/gewonnen ≠ besiegelt (besiegeln = endgültig festmachen, z. B. einen Vertrag)
oneFocusFrame: siegen_besiegeln_lexikon
reuseNextSession: Der CDU geht es schlecht: In Mecklenburg-Vorpommern hat die SPD gesiegt.
errorTypes:
  - lexikon
  - grammatik
  - stil
confidence: high
errors_brief:
  - Mecklenburg Vorpommern → Mecklenburg-Vorpommern (Bindestrich im Namen)
  - hat SPD besiegelt → hat die SPD gesiegt/gewonnen (besiegeln ≠ siegen: besiegeln = etwas endgültig festmachen)
  - die vor vorhanden Kanzler sehr schrecklich → der amtierende Kanzler schneidet sehr schlecht ab (schrecklich = horrible Person, schlecht abschneiden = Ergebnis)
  - zur Kenntnis-graph hinzu → dem Wissensgraph hinzu (Dativ, Genus)
  - bei mir fehlt es strukturierte Kenntnisse → mir fehlen strukturierte Kenntnisse (fehlen + Nominativ Plural)
