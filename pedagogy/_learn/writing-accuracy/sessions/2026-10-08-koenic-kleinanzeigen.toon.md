schema: learn/writing-accuracy-session
date: 2026-10-08
id: koenic-kleinanzeigen
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: KOENIC-Heissluftfritteuse (Touch-Display, Sichtfenster) auf Kleinanzeigen verkaufen; Preisempfehlung abgeleitet vom MediaMarkt-Neupreis KAF 71523 B ~58 EUR.

original: "Also gut, hab ich vor, diese auf Kleineanzeige zu verkaufen, welche Preisgestaltung empfolst du?"
corrected: "Also gut, ich habe vor, diese auf Kleinanzeigen zu verkaufen. Welche Preisgestaltung empfehlen Sie mir?"
oneFocus: "V2-Position nach Einleitung: nach der Einleitung Also gut beginnt ein neuer Hauptsatz -> Subjekt vor Verb (ich habe vor), nicht Umstellung (hab ich vor)"
reuseNextSession: "Also gut, ich habe vor, das auf Kleinanzeigen zu verkaufen. Was empfehlen Sie mir?"
errorTypes: wortstellung, orthography, verb_form
gaps: "hab ich vor -> ich habe vor (V2 nach Einleitung); Kleineanzeige -> Kleinanzeigen (Eigenname, Plural); empfolst -> empfehlen/empfiehlst du (Konjugation)"
confidence: high

errors_brief[3]:
  - "hab ich vor -> ich habe vor: nach der satzeinleitenden Fuegung Also gut steht das Finite auf Position 2, davor das Subjekt."
  - "Kleineanzeige -> Kleinanzeigen: Plattformname heisst Kleinanzeigen (mit z, Plural)."
  - "empfolst -> empfiehlst du / empfehlen Sie: empfehlen konjugiert stark (du empfiehlst); empfolst existiert nicht."
