schema: learn/writing-accuracy-session
date: 2026-10-07
id: koffein-pulver-2026-10-07
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Pulver versehentlich mit Koffein gekauft; heute ohne Pulver, E ueber Essen.
original: "Verdammt, ich habe die Protein Pulver mit Koffeine versehentlich gekauft statt ohne Koffein, so nehme ich es noch nicht. So ziehen Sie es in Betracht. Vielleicht heute ist Cut Tagen"
corrected: "Verdammt, ich habe das Proteinpulver versehentlich mit Koffein statt ohne gekauft — deshalb nehme ich es noch nicht. Ziehen Sie das bitte mit in Betracht. Vielleicht ist heute ein Cut-Tag."
oneFocus: "V2 auch nach Einleitewort: [Vielleicht/Heute/Deshalb] + Verb + Subjekt"
reuseNextSession: "Vielleicht ist heute ein Cut-Tag."
errorTypes: [wortstellung, genus, kompositum, artikel]
gaps:
  - gap: "Vielleicht heute ist Cut Tagen"
    hit: "Vielleicht ist heute ein Cut-Tag"
    frame: "[Einleitewort] + [V2] + [Subjekt] + [ein + Nomen]"
confidence: high

errors_brief:
  - "Vielleicht heute ist -> Vielleicht ist heute: Einleitewort = Position 1, Verb sofort danach (V2); 'Cut Tagen' -> 'ein Cut-Tag' (Artikel + Bindestrich-Kompositum)."
  - "die Protein Pulver -> das Proteinpulver: Genus + Kompositum; 'mit Koffeine' -> 'mit Koffein' (das Koffein, kein -e)."
  - "so nehme ich es noch nicht -> deshalb nehme ich es noch nicht; 'So ziehen Sie es in Betracht' -> 'Ziehen Sie das bitte mit in Betracht'."
