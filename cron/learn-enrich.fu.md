- KIND learn-enrich. Recurring job-seeking study loop. Lebenslauf and skills are the attested base. Internet CLAIM with SOURCE is additive. pedagogy-cpu is the human interface. Lesson pack is pedagogy/_learn/lesson.toon.md. GUI is ephemeral tempfile via --gui, never stored in the repo. After gather, --assess propagates grasp. On SATISFY write mezzanine/learn-enrich.toon.md. Change the process in this file.
- RECURRING 5m while the AI-agent-engineer job-seeking goal is open
- STORE PATH pedagogy/universe.graph.md
- STORE PATH pedagogy/pedagogy-cpu.fu.md
- STORE PATH self/learn.toon.md
- STORE PATH self/lebenslauf.toon.md
- STORE PATH self/identity/skill.toon.md
- STORE PATH self/goals.toon.md
- STORE PATH pedagogy/_learn/lesson.toon.md
- STORE PATH pedagogy/_learn/baseline-probes.toon.md
- STORE PATH mezzanine/learn-enrich.toon.md
- RUN python cron/learn-enrich.py
- OUTPUT PATH pedagogy/pedagogy-cpu.fu.md
- RULE every tick read self/goals.toon.md. focus chooses PLAN. north fields merge into pick order. Age and language counts stay particulars. Do not invent the 16 language names. Do not add Chinese as native.

- AGENT $id=learn-pick $input=self/goals.toon.md $output=pedagogy/_learn/state.toon.md $prompt=python cron/learn-enrich.py --pick. Read self/goals.toon.md first. Print JSON. Prefer empty GAP on the focused goal's north. If current target grasp is unknown or weak, keep it. Do not invent a vertex name that is not on a goal north or already on the graph.

- AGENT $id=learn-enrich $input=pedagogy/_learn/state.toon.md $output=pedagogy/universe.graph.md $when=after learn-pick $prompt=Read self/goals.toon.md then the picked id. Read self/lebenslauf.toon.md self/identity/skill.toon.md. Search the internet for how others practice this techne. If focus is languages-b2-16, enrich NaturalLanguage without inventing unnamed languages and without adding Chinese as native. Add CLAIM to pedagogy/<branch>/<id>.fu.md. Add V/E only with SOURCE=. Never delete Being Essence Form Matter. Never add Kafka unless skill.toon names it. Never add a Person Job vertex. Age stays in self/goals.toon.md.

- AGENT $id=learn-lesson $input=pedagogy/_learn/lesson.toon.md $output=pedagogy/pedagogy-cpu.fu.md $when=after learn-enrich $prompt=Write or refresh pedagogy/_learn/lesson.toon.md with probe expect claim neighbor source drill. python cron/learn-enrich.py --lesson. That writes PROBE onto pedagogy-cpu and deletes leftover html in pedagogy/_learn. Do not store html. Optional --gui writes a tempfile for one gather then delete. Ask the PROBE. Wait for ANSWER.

- AGENT $id=learn-grade $input=pedagogy/pedagogy-cpu.fu.md $output=self/learn.toon.md $when=answer-present $prompt=python cron/learn-enrich.py --assess. Mirror grasp onto E Study STUDIES <id>. Propagate a weaker grasp onto neighbors. Reorder PLAN NOW NEXT DONE. If weak, keep NOW and write a follow-up PROBE. Sweep leftover html. Do not mark STUDY DONE while GAP is empty.

- AGENT $id=learn-satisfy $input=pedagogy/pedagogy-cpu.fu.md $output=mezzanine/learn-enrich.toon.md $when=human-ok $prompt=python cron/learn-enrich.py --satisfy. Capture that this process worked. Further process changes go in cron/learn-enrich.fu.md.

- AGENT $id=learn-baseline $input=pedagogy/_learn/baseline-probes.toon.md $output=tmp/pedagogy/baseline.html $prompt=python cron/learn-enrich.py --baseline-serve. 摸底 in tmp. Four expression boxes en zh fr de. Browser Speak is voice-to-text per language. Async. Do not invent ANSWER. Do not assess. Do not add Chinese as native. Do not spawn janitor --apply.

- RULE do not persist study html in pedagogy/_learn. GUI is tmp/pedagogy/learn-gui.html. 摸底 is tmp/pedagogy/baseline.html. ttl.toon.md stamps last_run. lesson.toon.md and pedagogy-cpu.fu.md are the store.
- RULE closed loop: PROBE, human ANSWER, --assess, PLAN adjusts. No fake scores.
- RULE this file is the reusable job. Perfect it when a tick fails or the human wants a process change. Do not copy the job into CPU.md as a bare AGENT.
