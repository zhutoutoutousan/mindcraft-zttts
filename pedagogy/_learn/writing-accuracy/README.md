# Writing accuracy arbitrage

Target-language coding prompts → genuine writing samples → one micro-focus.

| file | role |
|------|------|
| `method.toon.md` | method contract |
| `state.toon.md` | todayFocus / oneFocus / demotions |
| `sessions/*.toon.md` | raw + minimal rewrite + error tags |
| `lexicon.graph.md` | lemma · form · chunk · sentence · usage |
| `drills.toon.md` | substitution items from attested Frames; every item needs `point` (考点) and a derivable blank — see `method.toon.md` drillQuality (learner feedback 2026-09-08) |
| `render_drills.py` | HTML → `tmp/pedagogy/de-drills.html`; `--serve` writes localStorage + `de-drills-progress.toon.md`; validates point/blank/stem and fails on violation |

Ontology vertex: `WritingAccuracyArbitrage`  
Hook: `.cursor/hooks/writing-accuracy-session.py` via `.cursor/hooks.json` `sessionStart`  
Rule backup: `.cursor/rules/writing-accuracy-arbitrage.mdc`

Log language only under this folder. Do not change product code for logging.
