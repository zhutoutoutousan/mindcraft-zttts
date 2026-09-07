- KIND inflow-news. Gather news that matters to this human. Away-loop writes DUMP.md. Drip when the human is back. Not latex. Not pdf. Not a general news wire.
- RECURRING 20m while job-seeking and language goals are open
- STORE PATH inflow/DUMP.md
- STORE PATH inflow/inflow.fu.md
- STORE PATH inflow/STATE.md
- STORE PATH self/goals.toon.md
- STORE PATH CPU.md
- STORE PATH cron/dump-drip.fu.md
- RUN python cron/inflow-news.py
- OUTPUT PATH inflow/DUMP.md

- AGENT $id=inflow-news $input=self/goals.toon.md $output=inflow/DUMP.md $prompt=Away-loop. Read self/goals.toon.md CPU.md the current month file under schedule/ inflow/STATE.md inflow/DUMP.md. python cron/inflow-news.py --status. Search the open web for NEW items that touch open goals, PLAN NOW vertices, dated calendar titles already in schedule/, and unknown unknowns next to north. Do not search by home city, personal domain, street, or ID. APPEND CAPTURE rows under PENDING in inflow/DUMP.md with TITLE URL WHY LEARN KIND news|idea|tech|unknown. Skip STATE ids. Stamp new ids. No Ausweis Melde personal phone Amt file number. Not latex. Not pdf. Do not drip. Do not invent event times. Do not invent ANSWER. Do not add Chinese as native. Do not spawn dump-drip. Do not spawn janitor --apply.

- AGENT $id=inflow-news-status $input=inflow/STATE.md $output=inflow/STATE.md $prompt=python cron/inflow-news.py --status. Print skip count and last stamp. Do not write news.

- RULE matters means it touches an open goal, a dated row already on the calendar, a DUMP the human wrote, or a useful blind spot next to north.
- RULE the human reads inflow/inflow.fu.md after drip. DUMP.md is the away buffer.
- RULE LEARN points at a graph vertex or a DAY DO. Empty PROBE stays empty. Never invent ANSWER.
- RULE this file is the reusable job. Perfect it when a tick writes filler.
- RULE pinpointable particulars stay in .private/. Dump and inflow name public pages and clocks, not bag lists.
- RULE when the human is back, run cron/dump-drip.fu.md. Loop ticks must not.
