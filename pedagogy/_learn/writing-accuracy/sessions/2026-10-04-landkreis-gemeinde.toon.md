schema: learn/writing-accuracy-session
date: 2026-10-04
id: landkreis-gemeinde
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: User asked for district/municipality-level info near Bad Belzig. Delivered Landkreis Potsdam-Mittelmark + Stadt Bad Belzig compact block with sources. Corrected "Municipalitaet" -> Gemeinde.
original: Meine, nahe Bad Belzig, Landkreisweise oder Municipalität
corrected: Meinst du die Landkreisebene oder die Gemeindeebene nahe Bad Belzig?
oneFocus: "Municipalitaet" existiert im Deutschen nicht - hier: die Gemeinde (Kommune); Verwaltungsstufen Gemeinde -> Landkreis -> Bundesland; "landkreisweise" -> auf Landkreisebene
reuseNextSession: die Landkreisebene oder die Gemeindeebene
errorTypes: anglicism, word_choice
gaps: Landkreisweise -> auf Landkreisebene (praeziser); Municipalitaet -> die Gemeinde (gibt es nicht im Deutschen)
confidence: high

errors_brief[3]:
  Municipalitaet -> die Gemeinde
  Landkreisweise -> auf Landkreisebene
  die Landkreisebene oder die Gemeindeebene (Wiederverwendbar)
