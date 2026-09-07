schema: learn/polyglot-grammar-lexicon-pairing
id: frame-slot-fill
created: 2026-09-07
vertex: GrammarFrame
status: active

# How grammar and vocabulary work together (cross-lingual)

oneLiner: Grammar is a Frame with slots. Vocabulary is Lemmas/Forms that fill slots. A Chunk is a filled Frame. Code-switch = Concept spoken with a foreign Lemma because the target Frame or Form is missing.

layers[6]:
  Concept, language-neutral meaning (device-location, hortative-dive, purpose-today)
  Frame, target-language grammar pattern (case government, particle order, hortative)
  Lemma, dictionary word in one language
  Form, inflected surface (meinem Laptop, dieses Projekt)
  Chunk, Frame with slots filled by Forms
  Sentence, ordered Chunks for one intent

pairingRules[6]:
  1,Never drill bare grammar without at least one Lemma that fits the Frame
  2,Never add a Lemma without naming which Frame(s) it participates in
  3,oneFocus per session = one Frame (or one slot inside a Frame), not a word list
  4,SubstitutionDrill: keep Frame fixed, swap 3 Lemmas that fit the same slots
  5,WritingAccuracyArbitrage: force the Frame into the next coding prompt; new Lemmas come from code-switch gaps
  6,Cross-lang bridge: Concept --EXPRESSES--> Lemma_L1 and Lemma_L2; gap when Concept has Lemma_other but missing Lemma_target or Frame_target

codeSwitchPolicy:
  detect: primary language of the utterance first. DE/FR/ES function words (≥2) beat CJK mass after a ZH stretch. Empty prompts must not reset last-signal to en.
  target: state.targetLang (default de) when doing writing-accuracy arbitrage
  allowlist: TODO Repo API PR MCP CPU PATH URL proper nouns code identifiers brand names
  foreignIsland: sparse tokens from a non-primary / non-target language
  meaning: treat island as Concept the learner could not express in targetLang
  capture: Concept + wrong_surface + missing Frame/Form → bridge.graph + session gaps[]
  not: treat every English tech noun as a gap when allowlisted

hookFlow:
  sessionStart: inject targetLang + todayFocus Frames + polyglot horizon reminder
  beforeSubmitPrompt: detect primaryLang + foreignIslands → write last-signal + **auto GAP vertices into bridge.graph.md**
  afterRewrite: write sessions/*.toon.md then `python pedagogy/_learn/writing-accuracy/ingest_session.py --session …` to attach Forms
  agent: job first; gaps already in graph; ingest Forms without waiting to be asked


antiPatterns[4]:
  Grammar PDF with zero words
  Anki lemma with no Frame
  Inventing CEFR levels beyond human self-rating bands
  Farming errors by writing worse on purpose
