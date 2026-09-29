# Polyglot layer

Cross-lingual learning under the 16-language / age-35 horizon.

| file | role |
|------|------|
| `horizon.toon.md` | age 35 · **16 named langs** + self-rating bands · zero unnamed slots |
| `commerce.toon.md` | 神游 allocation: ES/FR/DE first · rest rotation · not CEFR |
| `harvest.toon.md` | sourced learning URLs per lang/facet |
| `skills.toon.md` | GER facets under each lang (Hörverstehen, Schreiben, …) · no per-skill CEFR |
| `pairing.toon.md` | GrammarFrame × lexicon (slots → Forms → Chunks) |
| `frames/<lang>.toon.md` | per-language Frames |
| `bridge.graph.md` | Concept ↔ Lemma_L1/L2 ↔ NEEDS_FRAME |
| `last-signal.toon.md` | written by `beforeSubmitPrompt` (primaryLang + gaps) |

Code-switch rule: main language first; sparse foreign words (non-allowlist) = **unknown how to say in targetLang**.

Ontology: `PolyglotHorizon` · `GrammarFrame` · `WritingAccuracyArbitrage`
