- KIND dump-drip. Run when the human is back. Turn DUMP.md into the rest of the system. Two passes.
- STORE PATH inflow/DUMP.md
- STORE PATH inflow/inflow.fu.md
- STORE PATH inflow/STATE.md
- STORE PATH pedagogy/universe.graph.md
- STORE PATH schedule/
- STORE PATH .private/
- STORE PATH self/goals.toon.md

- AGENT $id=dump-drip $input=inflow/DUMP.md $output=inflow/inflow.fu.md $prompt=The human is back. Two passes. Pass one: read DUMP.md CPU.md inflow/inflow.fu.md schedule/ pedagogy/. Move pinpointable particulars (Ausweis Melde personal phone Amt file number home address bag list clerk notes) into .private/. Strip them from DUMP.md inflow/ CPU.md schedule/ pedagogy/. Pass two: every CAPTURE with STATUS pending becomes NEWS on inflow/inflow.fu.md or a SCHEDULE row or a graph CLAIM. KIND unknown may become STUDY with empty GAP, never an invented ANSWER. Skip STATE ids. Stamp new ids. Mark those CAPTURE STATUS dripped. Leave HUMAN OPEN until the human closes them. Do not write latex pdf. Do not add Chinese as native. Do not spawn janitor --apply.

- PASS 1 PII
  - MOVE to .private/ anything that pins this person
  - MOVE Bewerbung Gehalt Eintritt employer letters into .private/. Named firm stays there. Pedagogy may gain industry vertices only.
  - STRIP from tracked markdown after the move
  - KEEP public event titles. Drop street+number, GPS, hall/stand id, home address, and ID papers from tracked files

- PASS 2 DRIP
  - NEWS TITLE URL WHY LEARN into inflow/inflow.fu.md
  - dated rooms into schedule/ with SOURCE url. Do not invent a clock
  - named clinic or personal invites stay in .private/. Splice tmp/take.html. Not schedule/
  - domain claims onto existing vertices or a new vertex. Cite SOURCE
  - unknown unknowns: STUDY empty GAP or a CLAIM that this is a blind spot. Do not invent facts
  - python cron/inflow-news.py --stamp --ids the new ids

- RULE Loop must not run this AGENT. Loop only appends DUMP.md.
- RULE Empty PROBE stays empty.
