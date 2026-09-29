- KIND temp deliverables. On-demand video, image, html, latex pdf for a human to look at. Not the ontology. Not the life queue.
- DIR tmp
- LAPSE DAYS 5
- STORE PATH tmp/ttl.toon.md
- RUN python cron/janitor.py --ttl
- RUN python cron/janitor.py --purge
- RUN python cron/janitor.py --touch
- RUN python cron/schedule-view.py
- RUN python cron/schedule-view.py --plate
- RUN python cron/schedule-view.py --next
- RUN python cron/private-take.py
- RUN python .cursor/skills/daily-brief/scripts/compile.py
- OUTPUT PATH tmp/schedule/
- OUTPUT PATH tmp/take.html
- OUTPUT PATH tmp/day-YYYY-MM-DD.pdf
- OUTPUT PATH tmp/fog-state-YYYY-MM-DD.pdf

- RULE LaTeX and PDF renders only into tmp/. Never .private/ pedagogy/ self/ recycle/. Source .tex sits next to the PDF in tmp/. Intermediates (.aux .log .out) stay in tmp/.

- AGENT $id=temp-ttl $input=tmp/ttl.toon.md $prompt=python cron/janitor.py --ttl. Read last_run. If 5 days have lapsed and tmp has expirable files, promote named caches then delete every file in tmp except ttl.toon.md and tmp/pedagogy/mindcraft-hall.html. Do not recycle. Do not --apply.

- RULE Showcase writes tmp/pedagogy/. Video render writes tmp/loop-slash/. Kit is skills/loop-slash/. Study GUI writes tmp/pedagogy/learn-gui.html. 摸底 writes tmp/pedagogy/baseline.html. Schedule week view writes tmp/schedule/. Share plate is tmp/schedule/plate-<date>.png via --plate. Private clocks splice into tmp/take.html. Not schedule/.
- RULE persist only ttl.toon.md and tmp/pedagogy/mindcraft-hall.html. last_run stamps when a deliverable is written. ROOT and janitor --ttl read it. Before delete, python cron/tmp_promote.py copies named caches (inflow takes, learner notes, baseline answers, de-drills-progress) into lasting stores. Other HTML/media/build scripts expire. Do not invent CLAIM.
- RULE after lapse, delete siblings in place. Recycle is the bin for stray non-markdown elsewhere, not for tmp. --purge skips the 5-day wait when the human asks.
- RULE --touch after every deliver so last_run is now. Do not stamp last_run when only ttl exists.
- RULE do not KEEP pedagogy/universe.html in pedagogy/. That path is tmp/pedagogy/universe.html.
