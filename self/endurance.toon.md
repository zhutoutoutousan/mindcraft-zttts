schema: learner/endurance
note: particulars of intellectual load. Not a Person vertex. Human 2026-09-02 names post-study sore as DSB. Nature 2024 is mouse CA1 DNA-damage response. Do not write sore as GenomicInstability. Do not diagnose.
tz: Europe/Berlin
budget.default: 4
budget.now: 4
budget.note: daily external is 3 lexicon sessions (DE FR ES assistants). One session is one unit. DAY LOAD is remaining after those three. After sore, drop by 1, floor 1. After a clean day, raise by 1, cap 5. A unit is one DAY DO or one logged external session.
unit: one DAY DO or one logged external session
hypothesis: human 2026-09-02. Head/brain sore after a stretch of intellectual work. Named DSB. Gauge empirically. External drills count.
source: human 2026-09-02
source: human 2026-09-03 three daily 助手 背单词
source: https://www.nature.com/articles/s41586-024-07220-7
activity:
  id: de-assistant-wordschatz
  label: 德语助手 背单词
  vertex: Wordschatz
  recur: daily
  units: 1
  note: human 2026-09-02. Daily DE lexicon. Do not invent a word count. Log python cron/interview-anchor.py --external --id de-assistant-wordschatz
activity:
  id: fr-assistant-wordschatz
  label: 法语助手 背单词
  vertex: Wordschatz
  recur: daily
  units: 1
  note: human 2026-09-03. Daily FR lexicon. Not a SPRACHEN level. Do not invent a French CEFR. Log --external --id fr-assistant-wordschatz
activity:
  id: es-assistant-wordschatz
  label: 西语助手 背单词
  vertex: Wordschatz
  recur: daily
  units: 1
  note: human 2026-09-03. Daily ES lexicon. Attested Spanisch is verhandlungssicher. Do not invent a word count. Log --external --id es-assistant-wordschatz
session[]{date,id,units,note}:
  2026-09-07,run-modes-dual-lang,1,Dual-lang read of cursor run-modes. IntellectualLoad unit. Inflow take persisted to inflow/takes.toon.md. Not named DSB sore. Empty PROBE stays empty.
log[]{date,done,budget,sore,external,note}:
  2026-09-07,run-modes-dual-lang,4,,,Dual-lang docs intake logged as one unit. Not fog. Not DSB sore named. Take mirrored to AgentRunMode + endurance.
  2026-09-06,,4,fog-not-dsb,,Human named inflammation-like fog and skip lexicon. Not DSB. Empty PROBE stays empty. Do not pile DAY.
  2026-09-03,,4,recovery,,DSB recovery. Planned daily external is now 3 (DE FR ES 助手). AgentCore PROBE is the remaining hire unit if the head is quiet. Do not pile --day. Do not diagnose.
