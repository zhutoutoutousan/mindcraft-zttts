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
  id: mynoise-brown
  label: myNoise Brown as Lücken/desk bed
  vertex: IntellectualLoad
  recur: with visual language work
  units: 0
  note: human 2026-09-24 named fitting; wants more regular use. URL https://mynoise.net/NoiseMachines/whiteNoiseGenerator.php preset Brown. XOR DW audio. Not binaural overlay. Not a budget unit. Do not invent a daily clock.
activity:
  id: es-assistant-wordschatz
  label: 西语助手 背单词
  vertex: Wordschatz
  recur: daily
  units: 1
  note: human 2026-09-03. Daily ES lexicon. Attested Spanisch is verhandlungssicher. Do not invent a word count. Log --external --id es-assistant-wordschatz
session[]{date,id,units,note}:
  2026-09-10,de-assistant-wordschatz,1,named 36 min; 180 words. Fog beginning to dissipate. Not named clear. Not DSB.
  2026-09-07,run-modes-dual-lang,1,Dual-lang read of cursor run-modes. IntellectualLoad unit. Inflow take persisted to inflow/takes.toon.md. Not named DSB sore. Empty PROBE stays empty.
log[]{date,done,budget,sore,external,note}:
  2026-09-29,,4,illness-not-renamed,,Human ~12:13 named day start and asked for today's decision state. Illness not re-named this turn. Not DSB. Not named fog. Skip lexicon and PROBE until asked. No gym. Do not invent ANSWER. Do not pile DAY.
  2026-09-27,,4,illness-partial,,Human ~11:01 named day start. One illness class named gone; the rest not re-named. Lower trapezius named. Not DSB. Not a diagnosis. Skip lexicon and PROBE until asked. No gym. Particulars .private/health.fu.md. Do not invent ANSWER. Do not pile DAY.
  2026-09-25,,4,illness-named,,Human ~10:08 named considerable illness. Not DSB. Not a diagnosis. Skip lexicon and PROBE until asked. No gym. Particulars .private/health.fu.md. Do not invent ANSWER. Do not pile DAY.
  2026-09-24,,4,fog-cleared,,Human ~22:26 named Fireflies.ai Business canceled; paid until 2026-09-29 then Free. Do not invent other cancellations or ANSWER. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,,Human ~21:49 named summarize regular service payments from all mail to cancel carefully. Used bank CSV not IMAP. Not cancelled. Gmail IMAP_USER still empty. Do not invent ANSWER. Do not pile extra DAY.
  2026-09-24,dw-hoeren,4,fog-cleared,dw-done,Human ~21:33 named DW Übung currently done; asked how to capture Gmail into this project. Not named AgentCore ANSWER. Do not paste a Gmail password. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,dw-umgang-vier-wendungen,Human ~20:48 named DW Lücken ungenügend; four Umgang chunks (Laden schmeißen, Faust in der Tasche, sich in einer Rolle sehen, im Nacken sitzen haben) NOW. Not named DW finished. Do not invent ANSWER or a CEFR. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,,Human ~16:05 named Nahrungsergänzungsmittel already taken; proceed. KEEP sitting named taken. Not named which retinol or Ibuprofen. DW not named finished. AgentCore PROBE still NOW. Do not invent ANSWER. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,,Human ~15:55 named back. Hygiene sitting not named done in words. KEEP and desk still after if unfinished. DW not named finished. AgentCore PROBE still NOW. Do not invent ANSWER or a KEEP sitting. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,,Human ~15:46 named going to brush now and wash face. Not named done. KEEP and desk still after. DW Manuskript/Lücken not named finished. Do not invent ANSWER or a KEEP sitting. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,mynoise-keep,Human ~15:30 named myNoise very fitting; wants more regular use later. Default White Noise Player + Brown. XOR DW. Not done with DW. Do not invent a daily clock or ANSWER. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,dw-hoeren-manuscript-gaps,Human ~15:16 named DW Übungen with Manuskript + Lücken now; asked music/binaural bed. Not done. XOR: DW audio vs bed. Binaural is rest 12–20 min between blocks, not overlay (Klichowski 15 Hz worsened tests). Do not invent a word count or ANSWER. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,dw-hoeren-starting,Human named starting DW Learn German Hörverstehen Übungen (not 德语助手). Simultaneous ask: reduce project entropy. Not done. Do not invent a word count or that AgentCore ANSWER exists. Do not pile extra DAY.
  2026-09-24,,4,fog-cleared,,Human ~14:03 named pre-day ritual: Ibuprofen first (left scapula, not taken), then brush, KEEP supplements, sort desk; then start planning. DAY LOAD 1 still waits on AgentCore PROBE. Do not invent ANSWER, a taken dose, or KEEP sitting. Do not pile extra DAY. Press gate stays closed.
  2026-09-24,,4,fog-cleared,,Human ~14:00 named more conscious and biologically more willing to plan something complicated. New day opened. DAY LOAD 1 = open AgentCore PROBE. Not DSB. Do not invent ANSWER. Do not invent a clean-day budget raise. Press gate stays closed (right scapula 2026-09-23). ES 西语助手 still starting not done. Empty PROBE is NOW until they answer.
  2026-09-23,,4,fog-cleared,es-assistant-starting,Human named start stuffing ES Wortschatz into 西语助手 (Sphelper). Not done. Do not invent a word count. No FR/DE piled. Empty PROBE. Seed: CVC PCIC nociones específicas 7.4 búsqueda de trabajo already harvested.
  2026-09-23,,4,fog-cleared,,Human named 脑雾 消除. Not DSB. Do not invent a clean-day budget raise. Wordschatz/PROBE no longer auto-skip; resume when asked. Mouth particulars stay .private/. Press gate is training (right scapula named).
  2026-09-18,,4,fog-cleared,,Human named no longer suffering brain fog (leide ich nicht mehr) and en route to Oktoberfest. Not DSB. Do not invent a clean-day budget raise. Lexicon/PROBE resume when asked.
  2026-09-14,,4,fog-present,,Wake ~11:00. Starting routine. Skip lexicon/PROBE until asked. Do not pile DAY. Particulars .private/.
  2026-09-13,,4,fog-present,,Human ~15:18 named recent GI discomfort (肠胃不适), unspecified. Same calendar as named fog. Not a GI diagnosis. Soft non-acid still default. Skip lexicon/PROBE until asked. Do not pile DAY.
  2026-09-13,,4,fog-present,,Human ~15:06 named fog still present. Hypothesis: daily going-out plus brain not on valued work. Wants a contiguous fixed-routine stretch; named lack of routine and no felt planned progress toward goals. Term: time structure (Jahoda; Bond & Feather 1988). Not DSB. Not named clear. Skip lexicon/PROBE until asked. Do not pile DAY. Do not invent a bipolar label.
  2026-09-11,,4,fog-almost-gone,,Human woke ~10:22. Named fog 几乎已经没有了; ulcers 几乎已经完全愈合. Not named clear/healed. Not DSB. Named no other abnormal state except one loose tooth. Hard thought OK. Empty PROBE. Do not pile DAY. Do not invent a dental diagnosis.
  2026-09-10,de-assistant-wordschatz,4,fog-dissipating,1,Human named 36 min 180 words DE 助手 done ~12:23. Fog 开始消散. Not named clear. Not DSB. No FR/ES piled. Empty PROBE. Do not pile DAY.
  2026-09-10,,4,fog-receding,,Human named cough last 3-4 days. Same SB window. Not a chest diagnosis invented. Hard thought still named OK. Empty PROBE. Do not pile DAY.
  2026-09-10,,4,fog-receding,,Human named sickness behaviour 已经好多了 plus motivation for hard thought. Acne named. Not named gone. Not DSB. Hard thought OK. Empty PROBE until asked. Do not pile DAY. Do not invent fog-cleared.
  2026-09-09,,4,fog-receding,,Human woke ~11:28. Named sickness behaviour 明显消退. Not named gone. Not DSB. Empty PROBE. Do not pile DAY. Lexicon only if asked. Do not invent fog-cleared.
  2026-09-08,,4,fog-not-dsb,,Human 19:12 named speech-motor plus light communication as tiring; sleep does not fix. Same fog cluster. Skip voice-heavy work. Skip gym. Empty PROBE. Do not invent ME/CFS. Do not start a cut.
  2026-09-08,,4,fog-not-dsb,,Human 19:04 named the 19:00 call cancelled. Heat still named. Skip gym. Empty PROBE. Do not invent fever or meetup attendance.
  2026-09-08,,4,fog-not-dsb,,Human 19:02 named whole-body heat. Same fog cluster. Skip gym. Skip lexicon unless they ask to finish the DE session already started. Empty PROBE. Do not invent fever.
  2026-09-08,,4,fog-not-dsb,de-assistant-starting,Human 18:33 named starting DE 助手 on Luftmatratze. Fog still present. Do not invent word count. Named 19:00 call wins. No FR ES or PROBE until asked.
  2026-09-08,,4,fog-not-dsb,,Human named fog still present plus oral ulcers still present. Skip lexicon. Empty PROBE. Do not pile DAY. Not DSB.
  2026-09-07,run-modes-dual-lang,4,,,Dual-lang docs intake logged as one unit. Not fog. Not DSB sore named. Take mirrored to AgentRunMode + endurance.
  2026-09-06,,4,fog-not-dsb,,Human named inflammation-like fog and skip lexicon. Not DSB. Empty PROBE stays empty. Do not pile DAY.
  2026-09-03,,4,recovery,,DSB recovery. Planned daily external is now 3 (DE FR ES 助手). AgentCore PROBE is the remaining hire unit if the head is quiet. Do not pile --day. Do not diagnose.
