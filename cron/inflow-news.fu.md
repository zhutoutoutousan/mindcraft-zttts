- KIND inflow-news. Gather news that matters to this human. Not latex. Not pdf. Not a general news wire.
- RECURRING 20m while job-seeking and language goals are open
- STORE PATH inflow/inflow.fu.md
- STORE PATH inflow/STATE.md
- STORE PATH self/goals.toon.md
- STORE PATH CPU.md
- RUN python cron/inflow-news.py
- OUTPUT PATH inflow/inflow.fu.md

- AGENT $id=inflow-news $input=self/goals.toon.md $output=inflow/inflow.fu.md $prompt=Read self/goals.toon.md CPU.md schedule/2026-9.fu.md inflow/STATE.md inflow/inflow.fu.md. python cron/inflow-news.py --status. Search the open web for NEW items that matter: hireable AI-agent-engineer north AgentCore AgentToolkit LambdaMicroVM AgentLoop MCP AgenticEngineering; attested languages en C1 de B2+ es; Berlin and Potsdam rooms; IFA this week; Goethe B2 speaking and writing; namelos.xyz; gastronomie Stripe. Write NEWS rows into inflow/inflow.fu.md with TITLE URL WHY LEARN. Skip ids already in STATE. Do not invent a clock time. If listings disagree, cite both. Skip invite-only rooms the human cannot enter. Skip past events unless the page is still a reading SOURCE. Then python cron/inflow-news.py --stamp with the new ids. Do not write latex pdf puml. Do not invent ANSWER. Do not add Chinese as native. Do not spawn janitor --apply from CPU.md.

- RULE matters means it touches an open goal, a dated row already on the calendar, or a DUMP the human wrote. Hacker-news noise without that hook is skip.
- RULE the human reads inflow/inflow.fu.md. Old briefing.pdf and per-tick latex folders are leftover. Janitor may recycle non-markdown there.
- RULE LEARN points at a graph vertex or a DAY DO. Empty PROBE stays empty. Never invent ANSWER.
- RULE this file is the reusable job. Perfect it when a tick writes filler.

- AGENT $id=inflow-news-status $input=inflow/STATE.md $output=inflow/STATE.md $prompt=python cron/inflow-news.py --status. Print skip count and last stamp. Do not write news.
