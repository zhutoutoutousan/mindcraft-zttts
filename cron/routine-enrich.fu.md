- KIND cron gatherer. Enrich self/routine tips and due periodic reminders. Not inflow-news. Not a diagnosis engine.
- STORE PATH self/routine.toon.md
- STORE PATH mezzanine/
- STORE PATH inflow/STATE.md
- RUN python cron/routine-enrich.py
- AGENT $id=routine-enrich $input=cron/routine-enrich.fu.md $output=self/routine.toon.md $when=human asks routine enrich OR maintain organ routine-enrich OR RECURRING weekly $prompt=Follow cron/routine-enrich.fu.md. python cron/routine-enrich.py --due first. Then optionally fetch ONE public oral-care or preventive-care page and APPEND tip[] with SOURCE URL only. Do not invent last_done. Do not invent a clinic Termin. Do not diagnose. Empty PROBE stays empty. Stamp mezzanine/routine-enrich.toon.md if a tip was added.

- RULE Delta is a new tip[] with URL, or a due-list print, or next_due filled only from last_done+interval. No graph CLAIM required.
- RULE Prefer ADA NIDCR or similar public pages. No paywalled copy-paste essays. Title + URL + one-line tip.
- RULE PII clinic street insurance → .private/ only.
