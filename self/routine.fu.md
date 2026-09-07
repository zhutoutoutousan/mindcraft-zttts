- STORE PATH self/routine.toon.md
- STORE PATH .private/health.fu.md
- PROFILE ROUTINE
- NOTE Daily hygiene + preventive recall. Not ontology Essence. Not a diagnosis. Tips need SOURCE.

- AGENT $id=routine-log $input=self/routine.toon.md $output=self/routine.toon.md $prompt=When the human says they did a daily id (brush-am floss…) or a periodic visit, APPEND log[]{date,id,done,note} and for periodic set last_done=today and next_due from interval_months. Never invent a completion. Reply in the user language.

- AGENT $id=routine-today $input=self/routine.toon.md $output=tmp/pedagogy/project-state.html $prompt=python cron/routine-enrich.py --today then python skills/project-state-viz.py --purpose today. Merge routine into Today. Do not invent ANSWER. Do not invent last_done.

- AGENT $id=routine-optimize $input=self/routine.toon.md $output=self/routine.toon.md $when=human asks 优化习惯 or optimize routine $prompt=Propose at most three optimize[] rows with why + SOURCE or human. Status open. Do not prescribe medicine. Do not invent disease.

- BLOCKER mouth particulars
  - Ulcer sites fog meds stay in .private/health.fu.md. This file only holds generic protocol tips with URL.
