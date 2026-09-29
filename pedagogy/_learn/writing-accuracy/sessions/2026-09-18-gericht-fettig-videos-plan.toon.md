schema: learn/writing-accuracy-session
date: 2026-09-18
id: gericht-fettig-videos-plan
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Human still on the Oktoberfest air mattress, hands greasy after eating a dish — switching to the video phase of the escalation loop. Job: save loop progress (memory + task), list the queued YouTube videos from the AgentCore and LambdaMicroVM vertices. No PII in this session.

original: So habe ich gerade Gericht verzehrt, ist mein Hand sehr Öllig. So schaue ich im Folgenden meistens Videos zu schauen ja, speichern Sie den Progress und listen Sie den Videos auf zu aufrufen

corrected: Ich habe gerade ein Gericht verzehrt, jetzt ist meine Hand sehr fettig. Im Folgenden schaue ich also meistens Videos. Speichere den Fortschritt und liste die Videos auf, die ich aufrufen soll, ja?

oneFocus: meine Hand — Hand ist Femininum: meine Hand, nie mein Hand.
reuseNextSession: Meine Hand ist fettig — ich habe gerade ein Gericht verzehrt.
errorTypes: word_order case_gender_article lexis_collocation morphology_endings register_imperative syntax_infinitive
confidence: high

errors_brief[5]:
  habe ich gerade Gericht verzehrt → Ich habe gerade ein Gericht verzehrt (Hauptsatz: Subjekt vor Verb; Gericht braucht Artikel: ein Gericht, Akk.)
  ist mein Hand sehr Öllig → ist meine Hand sehr fettig (Hand ist feminin → meine; nach Essen heißt es fettig, ölig = ölhaltig wie Maschinenöl)
  So schaue ich im Folgenden meistens Videos zu schauen ja → Im Folgenden schaue ich also meistens Videos (kein zweites schauen — das doppelte schauen streichen; also = folglich; Verbzweitstellung)
  speichern Sie den Progress → Speichere den Fortschritt (Progress ist Denglisch — Fortschritt; du-Form)
  listen Sie den Videos auf zu aufrufen → liste die Videos auf, die ich aufrufen soll (Akk. Pl. die Videos, nicht den; Relativsatz statt zu-Infinitiv; du-Form)
