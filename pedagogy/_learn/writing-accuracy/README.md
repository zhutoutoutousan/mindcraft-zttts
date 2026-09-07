# Writing accuracy arbitrage

Target-language coding prompts → genuine writing samples → one micro-focus.

| file | role |
|------|------|
| `method.toon.md` | method contract |
| `state.toon.md` | todayFocus / oneFocus / demotions |
| `sessions/*.toon.md` | raw + minimal rewrite + error tags |
| `lexicon.graph.md` | lemma · form · chunk · sentence · usage |

Ontology vertex: `WritingAccuracyArbitrage`  
Hook: `.cursor/hooks/writing-accuracy-session.py` via `.cursor/hooks.json` `sessionStart`  
Rule backup: `.cursor/rules/writing-accuracy-arbitrage.mdc`

Log language only under this folder. Do not change product code for logging.
