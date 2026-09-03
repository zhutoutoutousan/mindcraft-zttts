- KIND interview-anchor. Fetch AI-engineering interview question titles from Amit Shekhar's bank. Anchor each title to a graph vertex. Write today's DAY slice on pedagogy-cpu. Gauge intellectual load. Do not copy answers. Do not invent DSB in the human brain.
- RECURRING after learn-enrich pick and on the morning of a study day
- STORE PATH pedagogy/_learn/interview.toon.md
- STORE PATH self/interview.toon.md
- STORE PATH self/endurance.toon.md
- STORE PATH pedagogy/pedagogy-cpu.fu.md
- STORE PATH pedagogy/universe.graph.md
- STORE PATH self/goals.toon.md
- RUN python cron/interview-anchor.py
- SOURCE https://github.com/amitshekhariitbhu/ai-engineering-interview-questions
- OUTPUT PATH pedagogy/pedagogy-cpu.fu.md

- AGENT $id=interview-fetch $input=. $output=pedagogy/_learn/interview.toon.md $prompt=python cron/interview-anchor.py --fetch. Pull the README. Store topic, title, first SOURCE url, mapped vertex. Titles only. Never paste answers.

- AGENT $id=interview-graph $input=pedagogy/_learn/interview.toon.md $output=pedagogy/universe.graph.md $when=after interview-fetch $prompt=python cron/interview-anchor.py --anchor. Add missing topic vertices. CLAIM that this bank points here. Cite SOURCE. Never delete Being Essence Form Matter. Never add Kafka. Never add a Person Job vertex.

- AGENT $id=interview-day $input=self/endurance.toon.md $output=pedagogy/pedagogy-cpu.fu.md $when=after interview-graph $prompt=python cron/interview-anchor.py --day. Date is today Europe/Berlin unless --date. LOAD is remaining after planned daily external (德语助手 法语助手 西语助手). First DO is the open PROBE if ANSWER is empty. Then that many interview titles on north vertices. Print the slice in order. Stop. Wait for the human. Do not rewrite a DAY that already has DO.

- AGENT $id=interview-done $input=pedagogy/pedagogy-cpu.fu.md $output=self/interview.toon.md $when=human-finished $prompt=python cron/interview-anchor.py --done --id the-id. Mark that DO done. Do not invent remaining answers.

- AGENT $id=interview-sore $input=pedagogy/pedagogy-cpu.fu.md $output=self/endurance.toon.md $when=human-sore $prompt=python cron/interview-anchor.py --sore --text their words. Write SORE on DAY. Append the endurance log including today's external units. Lower budget next time. Do not call sore GenomicInstability. Do not diagnose DSB. The Nature paper is mouse CA1, not this calendar.

- AGENT $id=interview-external $input=self/endurance.toon.md $output=self/endurance.toon.md $when=human-external $prompt=python cron/interview-anchor.py --external --id de-assistant-wordschatz or fr-assistant-wordschatz or es-assistant-wordschatz. Log one Wordschatz unit. Do not invent a word count. Do not diagnose DSB.

- RULE the purpose is internalization for the AI-agent-engineer goal. A day slice is exact. The human says finished or sore. The agent does not pile more DO after SORE.
- RULE answers stay at their SOURCE urls. This repo stores titles and vertices.
- RULE IntellectualLoad is the bounded-study vertex. External Wordschatz (德语助手 法语助手 西语助手) is one unit per app session. DAY LOAD is remaining after planned daily external. Sore is a stop signal like scapular pain in training.toon.md. Hypothesis DSB is the human's name for the sore. Cite Nature 2024 only as the mouse DDR, with the contradiction that activity-induced enhancer breaks repair in minutes and persistent extranuclear fragments are a different class.
- RULE this file is the reusable job. Perfect it when a day slice is vague or a title is stored without a vertex.
- RULE do not copy the job into CPU.md as a bare AGENT. Do not spawn janitor.
