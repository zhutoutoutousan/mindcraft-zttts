schema: learn/writing-accuracy-session
date: 2026-09-08
id: korrektur-hook-datei
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Job was explaining that hooks detect + internalize while the agent supplies the Korrektur. Manual loop run because Qoder hooks activate after IDE restart.

original: Ach so, hmm... So wenn Ich auf Deutsch meine Meinung eingeben, machst du Korrigierung danach oder? Es muß von Hooks Datei stammen ja

corrected: Ach so, hmm... Wenn ich auf Deutsch meine Meinung eingebe, machst du danach die Korrektur, oder? Sie muss aus der Hook-Datei stammen, ja?

oneFocus: Verbposition: wenn-Satz Verb ans Ende, Hauptsatz Verbzweit (Ich-logge-Frame)
reuseNextSession: Wenn ich auf Deutsch meine Meinung eingebe, machst du danach die Korrektur, oder? Sie muss aus der Hook-Datei stammen, ja?
errorTypes: verb_position capitalization noun_choice article preposition compound_spelling
gaps: Korrigierung → die Korrektur · von Hooks Datei → aus der Hook-Datei
confidence: high

errors_brief[5]:
  Ich → ich (Kleinschreibung im Satzinnern)
  eingeben → eingebe (wenn-Satz: finites Verb ans Ende)
  machst du Korrigierung → machst du die Korrektur (Nomen-Wahl + Artikel)
  Es muß → Sie muss (Rückbezug auf die Korrektur; ß → ss)
  von Hooks Datei stammen ja → aus der Hook-Datei stammen, ja? (Präposition + Kompositum + Satzzeichen)
