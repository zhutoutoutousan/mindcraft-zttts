schema: learn/writing-accuracy-session
date: 2026-09-18
id: konnektor-fusion-runde-1
lang: de
meta:
  task: guided_drill_response
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Human's own answers to Konnektor-Fusion round 1 (obwohl/deshalb) on the air mattress. obwohl-clause was correct — verb at end, comma right. No PII in this session.

original: a) Ich liege auf der Luftmatratze. Ich mache Schrei Übungen, obwohl es so viel Insekten gibt. b) Die Aufgaben sind kurz. Ich bleibe dran, deshalb verbessert meine Deutschkenntnisse nicht so erheblich

corrected: a) Ich liege auf der Luftmatratze. Ich mache Schreibübungen, obwohl es so viele Insekten gibt. b) Die Aufgaben sind kurz, deshalb bleibe ich dran. (erweitert: Ich bleibe dran, deshalb verbessern sich meine Deutschkenntnisse.)

oneFocus: deshalb leitet die Folge ein — Die Aufgaben sind kurz, deshalb bleibe ich dran.
reuseNextSession: Die Aufgaben sind kurz, deshalb bleibe ich dran.
errorTypes: compound quantifier connector_logic verb_agreement reflexive
confidence: high

errors_brief[3]:
  Schrei Übungen → Schreibübungen (ein Wort — sonst sind es Schrei-Übungen)
  obwohl es so viel Insekten gibt → obwohl es so viele Insekten gibt (vor Plural-Nomen: viele)
  deshalb verbessert meine Deutschkenntnisse nicht so erheblich → deshalb bleibe ich dran (deshalb nennt die Folge; erweitert: deshalb verbessern sich meine Deutschkenntnisse — Plural-Verb + reflexiv)
