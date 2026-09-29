schema: learn/writing-accuracy-method
id: writing-accuracy-base-arbitrage
title: Foundational writing accuracy · one stone, N birds
lang: en
targetLang: de
created: 2026-09-07
kind: learning-method
status: active
vertex: WritingAccuracyArbitrage
store: pedagogy/_learn/writing-accuracy/
lexicon: pedagogy/_learn/writing-accuracy/lexicon.graph.md
frames: pedagogy/_learn/polyglot/frames/de.toon.md
bridge: pedagogy/_learn/polyglot/bridge.graph.md
pairing: pedagogy/_learn/polyglot/pairing.toon.md
horizon: pedagogy/_learn/polyglot/horizon.toon.md
signal: pedagogy/_learn/polyglot/last-signal.toon.md
hook_session: .cursor/hooks/writing-accuracy-session.py
hook_prompt: .cursor/hooks/writing-accuracy-prompt.py

codeSwitch:
  detectPrimary: first
  foreignIsland: treat as unknown expression in targetLang
  allowlist: TODO Repo API and other tech/proper nouns
  capture: Concept + surface + missing Frame/Form → bridge + session gaps

grammarLexiconPairing: pedagogy/_learn/polyglot/pairing.toon.md


oneLiner: Do the real job. Give the coding agent instructions in the target language. Capture writing accuracy as a byproduct.

why:
  problem: Standalone writing drills are costly, fake-motivated, and unlike real communication
  leverage: In Cursor, Kiro, or Claude Code you already have to state intent clearly
  arbitrage: One utterance buys both task completion and a genuine writing sample
  birdsMax: ship the main task, produce target-language text, log error types, pick the next micro-focus

howToDo[7]:
  1,Open the work tool (Cursor / Kiro / Claude Code / Grok). Do not open a separate workbook
  2,Write the whole instruction in the target language. Proper nouns may stay as-is (TODO, Laptop, Repo)
  3,Do not draft in L1 and translate. The first draft must be the target language
  4,After send, check that the main job is right first. Language second
  5,Send raw / minimal rewrite / error tags to the language system. Do not change project code for this
  6,Take away only one high-priority form point. Force it into the next coding prompt
  7,If the same error is gone for 3 sessions, demote it. If it returns, make it the only focus that day

whatToCapture:
  not: repo layout, APIs, business TODO detail
  yes: how you request work in the target language
  fields[6]: raw, corrected, errorTypes, oneFocus, reuseNextSession, confidence

errorTypesYouTrack[8]:
  case_gender_article
  prepositions
  word_order_particles
  morphology_endings
  lexis_collocation
  orthography
  register_imperative
  sentence_chunking

sessionLoop:
  before: Read last todayFocus. Force that structure into this prompt
  during: Only care about making the project request clear
  after: Compare with the minimal rewrite. Mark one pattern you will still miss
  next: Open the next session with that structure in sentence one

constraints[5]:
  If the main job fails, the method is void. Finish the work first
  Do not turn the agent into a grammar teacher. Notes stay at a minimal rewrite
  Do not aim to be correct once. Aim to reuse the same structure
  Keep product git and learning logs in separate stores
  Stop when tired. Fatigue garbage input kills the arbitrage

success:
  northStar: Target-language writing that fully expresses intent — eventually near error-free under real work (not workbook perfectionism)
  honest: Absolute zero errors forever is asymptotic; measure productive accuracy under coding prompts
  week: Produce auf + dative, articles, and lass uns … without looking them up
  month: A native reader understands the coding instruction in one pass; only words need fixing, not structure
  horizon: Same accuracy bar rotates across the 16 named langs toward B2+ productive (PolyglotHorizon)
  failIf: You start writing worse on purpose to collect errors; or you drop the job to chase grammar essays

agentRules:
  - Do not invent ANSWER on pedagogy-cpu from these samples
  - Do not paste private employer/Gehalt into the lexicon
  - When logging: write under pedagogy/_learn/writing-accuracy/sessions/ only
  - Prefer minimal rewrite + oneFocus over long grammar essays

drillQuality (learner feedback 2026-09-08, binding for every render):
  point: every drill item must carry `point` naming the test point (考点), rendered visibly on the card — never hidden behind hints
  derivable: the blank must be answerable from prompt + point alone. No clairvoyance items where the expected answer is unpredictable (e.g. a whole sentence after "Okay, ___ .")
  attested: answers come only from session attestations, never invented workbook phrases
  enforce: render_drills.py validates point/blank/stem at render time and fails loudly; a render without these fields is a bug, not a style choice
  fixLoop: learner feedback on drills → update drills.toon.md items + this drillQuality block together, then re-render

errorEscalation (learner feedback 2026-09-18, binding):
  trigger: a drill or 摸底 probe shows errors on important knowledge, or a logged error pattern returns across sessions
  domains: human-named 2026-09-18 — KI-Agent (pedagogy/computation/), Software Engineering (pedagogy/computation/SoftwareEngineering.fu.md), Mathematik (pedagogy/math/Mathematics.fu.md). These need sofortiges ganzheitliches Verständnis, not only single-error fixes
  loop: sofortige Übung the same day → wiederholende Übungen spaced (+1 Tag, +3 Tage, +7 Tage) → Lesen the matching Frame / lexicon Form / .fu.md → Video + Probe hin und her (question → answer → counter-question, spoken)
  exit: the human names vollständiges Verständnis. The agent never invents mastery, never marks the loop done on its own, and never invents ANSWER inside the loop
  scope: language Forms and these knowledge domains alike
  firstCases: daß→dass (logged 2026-09-12, returned 2026-09-18) and weak adjective declension -en after article/possessive (returned in 4+ sessions: privaten Bereich, vielen Insekten, dieser Beschränkung, sofortigen/wiederholenden Übungen)
