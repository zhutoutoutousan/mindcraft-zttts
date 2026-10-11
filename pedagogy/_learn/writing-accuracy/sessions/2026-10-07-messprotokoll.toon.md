schema: learn/writing-accuracy-session
date: 2026-10-07
id: messprotokoll-2026-10-07
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Kritik an Schaetzwerten; echter Loop = Gewichtstrend vs Aufnahme.
original: "Also, dies sind doch nur für protokollieren, die echte Kenntnisse darauf liegt in dem Verhältnis zwischen Gewicht gemessen jeden Tag und echter Essen gegessen mit Kalorie gebrannt."
corrected: "Diese Zahlen dienen doch nur dem Protokoll — das echte Wissen liegt im Verhältnis zwischen dem täglich gemessenen Gewicht und dem tatsächlich Gegessenen bzw. den verbrannten Kalorien."
oneFocus: "Nominalisierung des Partizips: [Artikel] + [Partizip II substantiviert] -- das Gemessene, das Gegessene"
reuseNextSession: "Das echte Wissen liegt im Verhältnis zwischen dem täglich gemessenen Gewicht und dem tatsächlich Gegessenen."
errorTypes: [nominalisierung, genus, plural, verbvalenz]
gaps:
  - gap: "echter Essen gegessen / Gewicht gemessen jeden Tag"
    hit: "das täglich gemessene Gewicht / das tatsächlich Gegessene"
    frame: "[Artikel] + [Adverb] + [Partizip II] als Nomen"
confidence: high

errors_brief:
  - "echter Essen gegessen -> dem tatsächlich Gegessenen: Partizip als Nomen = gross + Artikel; 'Gewicht gemessen jeden Tag' -> 'dem täglich gemessenen Gewicht' (Attribut vor dem Nomen)."
  - "die echte Kenntnisse darauf liegt -> das echte Wissen liegt darin: Genus (das Wissen), 'liegen in+Dat', darin statt darauf."
  - "Kalorie gebrannt -> Kalorien verbrannt: Plural + Verb 'verbrauchen/verbrennen'; 'für protokollieren' -> 'zum Protokollieren'."
