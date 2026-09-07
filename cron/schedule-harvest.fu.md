- KIND schedule-harvest. Scan CPU.md inflow/ DUMP LEARNING_DUMP .private for dated events. Fill WHAT WHERE WHEN WHY from the open web. Write schedule/. Do not invent times. ICS is a later command when the human asks.

- RECURRING after inflow deliver and on idle
- STORE PATH schedule/harvest.toon.md
- STORE PATH schedule/enrich.toon.md
- STORE PATH schedule/
- TZ Europe/Berlin
- RUN python cron/schedule-harvest.py
- OUTPUT PATH schedule/

- AGENT $id=schedule-harvest-dry $input=. $output=schedule/harvest.toon.md $prompt=python cron/schedule-harvest.py --dry-run. Print dated rows after merge with schedule/enrich.toon.md. Do not write. Any GAP means the overlay is incomplete.

- AGENT $id=schedule-harvest $input=CPU.md $output=schedule/harvest.toon.md $prompt=Do not stop at slugs. For every dated candidate read CPU.md inflow/STATE.md inflow/inflow.fu.md .private/*.fu.md raw/*.fu.md. Then browse the open web until the row has a public title plus WHAT WHERE WHEN WHY and a SOURCE url. Write those facts into schedule/enrich.toon.md. Never invent a clock time. If listings disagree, cite both and pick one. WHERE is a coarse place: venue or city, no street+number, no GPS, no hall/stand id. Do not invent a second event by renaming a listing. Skip paper dumps with no sitting date. Skip exam-module durations with no exam day. Skip invite-only rooms the human cannot enter. Then python cron/schedule-harvest.py --apply so harvest and the month fu merge the overlay.

- AGENT $id=schedule-ics $input=schedule/harvest.toon.md $output=schedule/calendar.ics $when=human-asks $prompt=python cron/schedule-harvest.py --ics. Google Calendar import. SUMMARY is the public title never a slug. LOCATION is a coarse place, never street+number. DESCRIPTION is what, when, and why it matters to the open goal in self/goals.toon.md, without home-city or ID sentences. Never dump source or status into DESCRIPTION. TZ Europe/Berlin. Do not run unless the human asked for ics.

- RULE slug titles are unfinished. Apply is not done until enrich overlay has WHAT WHERE WHEN WHY. ICS DESCRIPTION is the Google popup. If the popup would show only source plus status, the ics job failed.
- RULE do not invent start times. All-day only if no sourced clock exists.
- RULE CPU.md stays the life queue. schedule/ is the calendar store. Pedagogy graph is not a calendar.
- RULE janitor KEEP schedule/*.ics when that file exists. Markdown harvest and enrich stay.
- AGENT $id=schedule-view $input=schedule/enrich.toon.md $output=tmp/schedule/ $prompt=python cron/schedule-view.py. Google-style 7-day PNG plus agenda PNG plus upcoming.html into tmp/schedule/. Stamp ttl. Do not invent times.

- RULE this file is the reusable job. Perfect it when a tick writes a slug without a venue.
