- TODO job seeking as AI agent engineer developer
  - STORE PATH cron/learn-enrich.fu.md
  - STORE PATH cron/interview-anchor.fu.md
  - STORE PATH cron/inflow-news.fu.md
  - STORE PATH cron/temp.fu.md
  - STORE PATH cron/maintain.fu.md
  - STORE PATH tmp/ttl.toon.md
  - STORE PATH self/learn.toon.md
  - STORE PATH self/goals.toon.md
  - STORE PATH self/endurance.toon.md
  - STORE PATH self/training.toon.md
  - STORE PATH self/routine.toon.md
  - STORE PATH self/routine.fu.md
  - STORE PATH cron/routine-enrich.fu.md
  - NOTE 2026-09-03 ~23:51. Maintain STOPPED. Last organ pedagogy-cpu STUDY AISafety. Next would be DUMP.

- NOTE TODAY 2026-09-06 ~10:33 Europe/Berlin. Weigh-in logged in gitignored self/training.toon.md. Park Babelsberg walk then easy swim. Residual lats DOMS and a little ab DOMS. skipHeavyPressUntilClear still true. Mouth particulars stay in .private/health.fu.md.
  - BODY easy swim, not a pull session. Stop if left scapula nags. No heavy bench. No IFA.
  - CLOCK Monday 2026-09-07 REST. Skip IFA halls. Skip HPI AI RoundTable 16:00 Potsdam. Skip 10:50 Dream Stage kitchen AI panel.
  - CLOCK Tuesday 2026-09-08: IFA Agent-Ready 13:45 Hall 25 skipped while rest is on. Halls close 18:00. ClickHouse/Grafana 18:00–21:00 CEST CLASH named evening call in .private/rosenblatt-2026-09-08.fu.md. Named call wins. Do not invent RSVP.
  - LOOP STOPPED 2026-09-06 ~10:06. Human terminated AGENT_LOOP_TICK_restenrich. Do not re-arm. Pending DUMP stays in inflow/DUMP.md until dump-drip.
  - LEARN AgentCore PROBE still empty. After swim, at most one sentence if the head is quiet. Do not invent ANSWER. Do not pile DAY.
  - LEARN Home and living e-commerce plus Disposition as industry. Named employer Bewerbung Gehalt stay in .private/CPU.md. Do not copy those here.

- AGENT $id=temp-ttl $input=tmp/ttl.toon.md $prompt=python cron/janitor.py --ttl. If last_run is 5 days old, delete tmp siblings. Keep ttl.toon.md. Do not recycle. Do not --apply.

- SCHEDULE 2026-09-04–08 Attend IFA Berlin https://www.ifa-berlin.com/de/ Messe Berlin, Messedamm 22, 14055 Berlin — Fr 04.09. Privatbesucher 12:00–18:00 (Vormittag bis 12:00 nur Fachbesucher), Sa–Di 05.–08.09. 10:00–18:00; Hallen schließen 18:00

- SCHEDULE 2026-09-04 11:30–13:30 REGISTERED Running Sandboxed Coding Agents in your CI/CD Pipeline — AWS Workshops, Online (~2h). Lambda MicroVMs, Agent Toolkit for AWS, Cedar policy in AgentCore. CLASH: Empfang follow-up is the same 11:30. Particulars in .private. Empfang wins. IFA after Amt if quiet.

- SCHEDULE 2026-09-03 12:30 ~20min Agentur für Arbeit Potsdam Empfang. Particulars and bag in .private/after-agentur.fu.md

- AGENT $id=maintain $input=cron/maintain.fu.md $output=inflow/STATE.md $when=human asks 保养 or a maintain loop is armed $prompt=Follow cron/maintain.fu.md. One organ per tick. NEW sourced delta. If the work would match last_organ last_delta, skip to the next organ. Do not restate DUMP-empty PROBE-empty session-planned. Do not invent ANSWER. Do not pile DAY. Do not add Chinese as native. Do not start a second maintain loop.

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

- DUMP Learn from hermes agent https://github.com/NousResearch/hermes-agent
  - NOTE 2026-09-06 captured into inflow/DUMP.md $id=hermes-agent-self-improving-loop. Away: do not drip. Empty PROBE stays empty.
- DUMP Graft context layer https://graft.nanonets.ai
  - NOTE 2026-09-06 queued inflow/DUMP.md $id=graft-context-layer-nanonets. STATUS pending. Fog/rest: do not drip, do not invent install. Empty PROBE stays empty.
- DUMP Psyche: learn Cursor/Claude Code subagents + hooks; bias system toward that
  - NOTE 2026-09-06 ~16:48 dripped inflow/DUMP.md $id=psyche-hooks-subagents-learn. goals.north + PLAN NEXT front-load AgentHook MultiAgent AgentPlugin. STUDY stubs empty ANSWER. Empty AgentCore PROBE stays empty. Do not invent hook store.