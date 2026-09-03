- TODO job seeking as AI agent engineer developer
  - STORE PATH cron/learn-enrich.fu.md
  - STORE PATH cron/interview-anchor.fu.md
  - STORE PATH cron/inflow-news.fu.md
  - STORE PATH cron/temp.fu.md
  - STORE PATH tmp/ttl.toon.md
  - STORE PATH self/learn.toon.md
  - STORE PATH self/goals.toon.md
  - STORE PATH self/endurance.toon.md
  - STORE PATH self/training.toon.md
  - NOTE 2026-09-03 DSB recovery. Walk only. Do not spawn interview-anchor --day. AgentCore PROBE still empty. Daily 德语助手 法语助手 西语助手 背单词, one unit each. Loop 20m inflow-news still running. Loop 30m maintain STOPPED 11:14 by human. Do not re-arm unless asked. Do not nest bare AGENT janitor --apply.

- NOTE TODAY 2026-09-03 packed 11:32 Europe/Berlin. tmp purged except ttl. Away inflow goes to DUMP.md. Drip when back.
  - BODY DSB recovery. Scapular sore. Rotation residual. Chest lats forearm DOMS. Walk only.
  - CLOCK 12:30 Agentur Potsdam Empfang. Bag street ID list in .private/after-agentur.fu.md
  - RETURN after Agentur: sit. Log the visit in .private/after-agentur.fu.md. If quiet, AgentCore PROBE one sentence. Then three 助手 if not logged. Goethe Schreiben only if still quiet. Skip workshop pre-reads until PROBE. Skip IFA today.
  - DAILY 德语助手 背单词. Log --external --id de-assistant-wordschatz
  - DAILY 法语助手 背单词. Log --external --id fr-assistant-wordschatz. Do not invent a French CEFR.
  - DAILY 西语助手 背单词. Log --external --id es-assistant-wordschatz
  - LEARN AgentCore PROBE still empty. One sentence. Do not invent ANSWER. Do not pile --day.
  - LEARN Goethe B2 Schreiben if quiet after Agentur. https://bfu.goethe.de/b2_mod_2MX6/schreiben.php
  - LEARN Tomorrow: workshop 11:30 then IFA after 13:30. No heavy bench.

- AGENT $id=temp-ttl $input=tmp/ttl.toon.md $prompt=python cron/janitor.py --ttl. If last_run is 5 days old, delete tmp siblings. Keep ttl.toon.md. Do not recycle. Do not --apply.

- SCHEDULE 2026-09-04–08 Attend IFA Berlin https://www.ifa-berlin.com/de/ Messe Berlin, Messedamm 22, 14055 Berlin — Fr 04.09. Privatbesucher 12:00–18:00 (Vormittag bis 12:00 nur Fachbesucher), Sa–Di 05.–08.09. 10:00–18:00; Hallen schließen 18:00

- SCHEDULE 2026-09-04 11:30–13:30 REGISTERED Running Sandboxed Coding Agents in your CI/CD Pipeline — AWS Workshops, Online (~2h). Lambda MicroVMs, Agent Toolkit for AWS, Cedar policy in AgentCore. overlap IFA Fr 04.09 Privatbesucher from 12:00 — workshop first, Messe after 13:30 if same day.

- SCHEDULE 2026-09-03 12:30 ~20min Agentur für Arbeit Potsdam Empfang. Particulars and bag in .private/after-agentur.fu.md

- AGENT $id=inflow-news $input=cron/inflow-news.fu.md $output=inflow/DUMP.md $prompt=Follow cron/inflow-news.fu.md. Away-loop: APPEND CAPTURE into inflow/DUMP.md. python cron/inflow-news.py --status then --stamp. Skip STATE ids. Unknown unknowns allowed. No PII. Not latex. Not pdf. Do not drip. Do not invent ANSWER.

- AGENT $id=dump-drip $input=cron/dump-drip.fu.md $output=inflow/inflow.fu.md $when=human is back $prompt=Follow cron/dump-drip.fu.md. Two passes: PII into .private first, then drip DUMP.md into inflow schedule pedagogy. Stamp STATE. Do not invent ANSWER.

- TODO introduction and deep dive of all agent pane slash commands on cursor into mezzanine
  - DONE 2026-09-02 catalog from skills-cursor SKILL.md into mezzanine/cursor-slash.toon.md
  - STORE PATH mezzanine/cursor-slash.toon.md
  - STORE PATH pedagogy/language/SlashCommand.fu.md
  - NOTE deep internalization is STUDY SlashCommand on pedagogy-cpu. Empty GAP until the human writes RECALL.

- LEARNING_DUMP QUEUED https://www.bilibili.com/video/BV1t9oZBDENp
  - DONE 2026-09-02 ontology-enrich MultiAgent RalphLoop ExperienceStore
  - STORE PATH pedagogy/computation/MultiAgent.fu.md

- LEARNING_DUMP human 2026-09-02 infographic Claude Code five layers https://code.claude.com/docs/en/features-overview
  - DONE 2026-09-02 ontology-enrich AgentConstitution CursorSkill AgentHook MultiAgent AgentPlugin. Card vs docs in mezzanine. Not NOW. AgentCore PROBE stays open. DAY LOAD 3 full.
  - STORE PATH mezzanine/claude-code-layers.toon.md
  - STORE PATH pedagogy/computation/AgentConstitution.fu.md
  - STORE PATH pedagogy/computation/AgentHook.fu.md
  - STORE PATH pedagogy/computation/AgentPlugin.fu.md

- TODO RECURRING Watch Jugend debattiert and writing exercise
  - TODO Research writing exercise online solutions for Goethe B2

- RESEARCH https://www.nature.com/articles/s41586-024-07220-7 extract axioms
  - DONE 2026-09-02 ontology-enrich into pedagogy/universe.graph.md and pedagogy/biology/
  - STORE PATH mezzanine/s41586-024-07220-7.toon.md

- TODO Develop namelos.xyz
  - BLOCKER Current approach still not very clear

- TODO Develop gastronomie tool Verkaufer:innen menu inventory equipment tickets sales Android + AWS website Stripe
  - STORE PATH https://github.com/zhutoutoutousan/quick-gastro
  - TODO mezzanine TOON for design-process educational mp4 DE playback DE+EN subs while coding
  - TODO React Native + AWS Next.js ECS CDK credentials later
  - TODO property tests + Playwright e2e + mp4 + interview questions + LaTeX PDF PlantUML architecture

- DUMP https://arxiv.org/html/2606.05608v1
  - DONE 2026-09-02 ontology-enrich AgenticEngineering CONTRADICTS SoftwareEngineering
  - STORE PATH pedagogy/computation/AgenticEngineering.fu.md

- DUMP f-university prototype nested unordered lists + CAPITAL tags. persist EXECUTION NUMBER CONTEXT STORE PATH EXECUTED ON.

- RESEARCH https://github.com/ovg-project/kvcached
  - DONE 2026-09-02 ontology-enrich KVCache
  - STORE PATH pedagogy/computation/KVCache.fu.md

- RESEARCH https://americantesol.com/blogger/drilling-old-school-technique-modern-applications-in-esl/
  - DONE 2026-09-03 ontology-enrich LanguageDrilling
  - STORE PATH pedagogy/language/LanguageDrilling.fu.md
  - STORE PATH mezzanine/tesol-drilling.toon.md


- DUMP