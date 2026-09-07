schema: learn/writing-accuracy-session
date: 2026-09-07
id: cafe-mask-how-it-works
meta:
  sourceLang: de
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: User asking how cafe-mask mp3 works while playing it.

original: Ok, so hab ich mit meine cafe-mask mp3 datei bei mir jetzt gespielt-ing  so wie funktioniert es

corrected: Ok, also ich spiele jetzt meine Café-Mask-MP3 bei mir. Wie funktioniert das?

oneFocus: gespielt / spielen (kein EN -ing am Partizip)
reuseNextSession: Ich spiele jetzt die Café-Mask … Wie funktioniert das?
errorTypes: morphology_endings code_switch_gap case_gender_article sentence_chunking
gaps: gespielt-ing → spiele / spiele … ab
confidence: medium

errors_brief[4]:
  gespielt-ing → spiele jetzt (kein englisches -ing)
  mit meine cafe-mask → meine Café-Mask-MP3 (Akk. Objekt; Maske/Datei)
  datei → Datei / MP3
  Run-on so wie → Punkt + Wie funktioniert das?
