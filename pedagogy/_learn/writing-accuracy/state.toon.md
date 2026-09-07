schema: learn/writing-accuracy-state
targetLang: de
updated: 2026-09-07
method: writing-accuracy-base-arbitrage
status: active

# Force these into sentence one of the next DE coding prompt.
todayFocus[4]:
  nach meinen Eingaben (Dativ Plural, nicht meinem)
  Korrektur (nicht Korrigierung)
  sicherstellen, dass … widergespiegelt wird
  Ein Gedanke = ein Satz

oneFocus: nach meinen Eingaben / Korrektur
reuseNextSession: Nach meinen Eingaben in dieser Chatbox soll eine Korrektur kommen.
confidence: medium

lastSession: 2026-09-07-chat-kg-tmp-promote
oneFocusFrame: nach_meinen_eingaben_korrektur

activeErrors[5]:
  word_order_particles,priority=1,streakClear=0
  morphology_endings,priority=1,streakClear=0
  orthography,priority=1,streakClear=0
  case_gender_article,priority=2,streakClear=0
  code_switch_gap,priority=1,streakClear=0

demoted[0]:

sessionsDir: pedagogy/_learn/writing-accuracy/sessions/
lexicon: pedagogy/_learn/writing-accuracy/lexicon.graph.md
frames: pedagogy/_learn/polyglot/frames/de.toon.md
bridge: pedagogy/_learn/polyglot/bridge.graph.md
signal: pedagogy/_learn/polyglot/last-signal.toon.md
horizon: pedagogy/_learn/polyglot/horizon.toon.md

patterns[5]:
  missing_determiners_on_masc_neut_nouns
  English_or_Chinese_word_order_on_German_particles
  preposition_transfer (in/on, after/for)
  chat_register_in_semi_formal_request
  CJK_or_EN_island_when_DE_Form_missing

note: beforeSubmitPrompt auto-writes GAP vertices into bridge. After rewrite, always ingest_session so Forms attach. Product work stays first.
northStar: Auf Zielsprache vollständig und möglichst fehlerfrei äußern (unter echter Arbeit; asymptotisch, nicht Workbook-Perfektion).
lastFrSession: 2026-09-07-fr-probe
frOneFocus: ajouter à / au (pas sur)
frFrames: pedagogy/_learn/polyglot/frames/fr.toon.md
