- KIND temp deliverables. On-demand video, image, html for a human to look at. Not the ontology. Not the life queue.
- DIR tmp
- LAPSE DAYS 5
- STORE PATH tmp/ttl.toon.md
- RUN python cron/janitor.py --ttl
- RUN python cron/janitor.py --purge
- RUN python cron/janitor.py --touch
- RUN python cron/schedule-view.py
- RUN python cron/schedule-view.py --plate
- RUN python cron/schedule-view.py --next
- OUTPUT PATH tmp/schedule/

- AGENT $id=temp-ttl $input=tmp/ttl.toon.md $prompt=python cron/janitor.py --ttl. Read last_run. If 5 days have lapsed and tmp has siblings, delete every file in tmp except ttl.toon.md. Do not recycle. Do not --apply.

- RULE Showcase writes tmp/pedagogy/. Video render writes tmp/loop-slash/. Kit is skills/loop-slash/. Study GUI writes tmp/pedagogy/learn-gui.html. 摸底 writes tmp/pedagogy/baseline.html. Schedule week view writes tmp/schedule/. Share plate is tmp/schedule/plate-<date>.png via --plate.
- RULE ttl.toon.md is the only persistent file in tmp. last_run stamps when a deliverable is written. ROOT and janitor --ttl read it.
- RULE after lapse, delete siblings in place. Recycle is the bin for stray non-markdown elsewhere, not for tmp. --purge skips the 5-day wait when the human asks.
- RULE --touch after every deliver so last_run is now. Do not stamp last_run when only ttl exists.
- RULE do not KEEP pedagogy/universe.html in pedagogy/. That path is tmp/pedagogy/universe.html.
