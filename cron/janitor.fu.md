- KIND janitor. Sweep the working tree. Markdown is the store. Stray non-markdown goes to recycle/. tmp/ is TTL, not recycle.
- RECURRING after SHOWCASE deliver and on idle
- STORE PATH recycle/JOURNAL.md
- STORE PATH tmp/ttl.toon.md
- RUN python cron/janitor.py
- OUTPUT PATH recycle/

- AGENT $id=janitor-dry $input=. $output=recycle/JOURNAL.md $prompt=python cron/janitor.py --dry-run. Print TRASH lines for bytecode caches, TTL lines for tmp siblings, and the recycle list. Do not move. Do not delete.

- AGENT $id=janitor-trash $input=. $output=recycle/JOURNAL.md $prompt=python cron/janitor.py --trash. Delete __pycache__ .pytest_cache .mypy_cache .ruff_cache and loose *.pyc *.pyo. Also python cron/janitor.py --ttl logic: if last_run is 5 days old, delete tmp siblings. Keep tmp/ttl.toon.md. Do not recycle bytecode. Do not --apply.

- AGENT $id=janitor-ttl $input=tmp/ttl.toon.md $output=recycle/JOURNAL.md $prompt=python cron/janitor.py --ttl. Read last_run. If 5 days have lapsed, delete every file in tmp except ttl.toon.md. Do not recycle. Do not --apply.

- AGENT $id=janitor-touch $input=tmp/ttl.toon.md $prompt=python cron/janitor.py --touch. Stamp last_run now. Call after a deliverable is written into tmp/.

- AGENT $id=janitor $input=. $output=recycle/ $prompt=python cron/janitor.py --apply. First delete bytecode caches in place. Then expire tmp siblings if last_run is 5 days old. Then move every other non-markdown file to recycle/<original-relative-path>. Preserve path. Collision: append UTC stamp. Append recycle/JOURNAL.md. Never enter .git recycle .cursor tmp. Never move cron/janitor.py. Never move a .md file including .fu.md .toon.md .graph.md.

- RULE markdown stays in place. Recycle is the bin, not delete. Restore by moving back.
- RULE bytecode cache is trash. Delete __pycache__ and *.pyc. Never KEEP them. Never recycle them.
- RULE tmp is not recycle. ttl.toon.md stays. Siblings die after 5 days from last_run. cron/temp.fu.md is the job.
- RULE do not touch .git. Do not touch recycle/. Do not touch .cursor/. Do not recycle tmp/.
- RULE KEEP cron/*.py and skills/*.py so janitor and showcase still run after a sweep. KEEP skills/*.puml skills/*.json. KEEP root .gitignore. KEEP root LICENSE. KEEP root submit.ps1. KEEP schedule/*.ics when the human asked for a calendar export. Do not KEEP pedagogy/universe.html. That render lives in tmp/pedagogy/.
- RULE empty directories after a move may be removed. Do not remove pedagogy/ being math physics biology computation language tmp inflow even if empty.
- RULE Windows: Being.fu.md is markdown. pedagogy/universe.html is a leftover deliverable. Move or delete it. Do not KEEP it in pedagogy/.
