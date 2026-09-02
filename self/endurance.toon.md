schema: learner/endurance
note: particulars of intellectual load. Not a Person vertex. Human 2026-09-02 names post-study sore as DSB. Nature 2024 is mouse CA1 DNA-damage response. Do not write sore as GenomicInstability. Do not diagnose.
tz: Europe/Berlin
budget.default: 3
budget.now: 3
budget.note: start at 3 units per day until a sore log exists. After sore, drop by 1, floor 1. After a clean day, raise by 1, cap 5. A unit is one DAY DO or one logged external session. DAY LOAD is remaining after planned daily external.
unit: one DAY DO or one logged external session
hypothesis: human 2026-09-02. Head/brain sore after a stretch of intellectual work. Named DSB. Gauge empirically. External drills count.
source: human 2026-09-02
source: https://www.nature.com/articles/s41586-024-07220-7
activity:
  id: de-assistant-wordschatz
  label: 德语助手 wordschatz
  vertex: Wordschatz
  recur: daily
  units: 1
  note: human 2026-09-02. Daily lexicon drill. Do not invent a word count. Log a session with python cron/interview-anchor.py --external --id de-assistant-wordschatz
session[]{date,id,units,note}:
log[]{date,done,budget,sore,external,note}:
