- KIND study interface. Human brain to the ontology. Not the life queue.
- STORE PATH pedagogy/universe.graph.md
- STORE PATH pedagogy/ontology.fu.md
- STORE PATH skills/ontology-showcase.fu.md
- STORE PATH skills/project-state-viz.fu.md
- STORE PATH pedagogy/_learn/weights.toon.md
- STORE PATH cron/ontology-weight.fu.md
- STORE PATH tmp/ttl.toon.md
- STORE PATH cron/learn-enrich.fu.md
- STORE PATH cron/interview-anchor.fu.md
- STORE PATH self/learn.toon.md
- STORE PATH self/goals.toon.md
- STORE PATH self/endurance.toon.md
- NOTE CPU.md is calendar and life AGENT. This file is internalization. Harmony: enrich writes V/E. Showcase reads the graph and does not invent vertices. Study GUI is tmp/pedagogy/learn-gui.html. lesson.toon.md self/goals.toon.md self/endurance.toon.md and this file are the store. Janitor keeps cron/*.py skills/*.py. Showcase HTML is tmp/pedagogy/universe.html. Janitor --ttl deletes tmp siblings after 5 days. Bytecode caches are trash.

- PROTOCOL
  - GOALS read self/goals.toon.md every tick. Age and language counts are particulars, not vertices. Sixteen language names live in pedagogy/_learn/polyglot/horizon.toon.md (human 2026-09-07). Do not invent CEFR beyond those bands. 中文/吴语 native_or_bilingual is attested for polyglot stores; do not invent lebenslauf SPRACHEN wording. PLAN $id must match goals.focus. NORTH comes from that goal's north field plus other active goals.
  - PROBE first. One open question on PLAN NOW. Do not lecture. Do not dump CLAIM. Wait.
  - ANSWER human nests text under the open PROBE, or replies in chat and the agent writes ANSWER. Empty ANSWER means wait. Never invent ANSWER.
  - ASSESS from ANSWER against expect in pedagogy/_learn/lesson.toon.md. python cron/learn-enrich.py --assess. Write grasp unknown|weak|partial|firm. Mirror onto E Study STUDIES and propagate a weaker grasp to neighbors.
  - PLAN if missing, create PLAN from self/goals.toon.md north. After ASSESS, move NOW NEXT DONE. If weak, stay and ask a follow-up PROBE. Do not mark STUDY DONE while GAP is empty.
  - GUI optional. python cron/learn-enrich.py --gui writes tmp/pedagogy/learn-gui.html, gather one ANSWER. Janitor --ttl expires it. Do not save html into pedagogy/_learn.
  - TODAY when the human asks 今天干什么 or what should I do today: merge CPU NOTE TODAY + self/training + self/routine (daily + due periodic + optimize) + harvest today + PLAN/PROBE + endurance fog. python skills/project-state-viz.py --purpose today or python cron/routine-enrich.py --today. Do not invent last_done dentist Termin or ANSWER.
  - BASELINE 摸底. python cron/learn-enrich.py --baseline then --baseline-serve. Async gather in tmp/pedagogy/baseline.html. Four expression boxes en zh fr de. Speak in Chrome or Edge: each Speak button is voice-to-text in that language. Skip any language. Stop if sore. Not DAY LOAD. Empty skip. Never invent ANSWER. --ingest-baseline copies to pedagogy/_learn/baseline.toon.md. --apply-study uses English if present else first filled language for STUDY ANSWER. Expression samples stay in the answers file. Do not assess until asked. Do not add Chinese as native.
  - DAY python cron/interview-anchor.py --day. Exact DO list for that calendar date. LOAD is how many items before a SORE check. First unfinished DO is NOW. Human says finished (--done --id) or sore (--sore --text). After SORE, stop. Do not pile more.
  - ENDURANCE self/endurance.toon.md. Sore after intellectual work is a stop signal. Human named it DSB. Nature 2024 is mouse CA1, not a diagnosis. Do not write sore as GenomicInstability. External drills count. Daily 德语助手 法语助手 西语助手 背单词 are Wordschatz, one unit per app session. DAY LOAD is remaining after those three. python cron/interview-anchor.py --external --id de-assistant-wordschatz or fr-assistant-wordschatz or es-assistant-wordschatz when that session is done.
  - SATISFY when the human says this loop worked. python cron/learn-enrich.py --satisfy writes mezzanine/learn-enrich.toon.md. Process changes go in cron/learn-enrich.fu.md or cron/interview-anchor.fu.md.

- DAY $date=2026-09-29
  - LOAD 1
  - TZ Europe/Berlin
  - WHY job seeking as AI agent engineer. Stop on SORE. External Wordschatz counts toward Ausdauer.
  - NOTE 2026-09-29 ~12:13 new day named. Illness not re-named clear this turn. Skip this PROBE and Wordschatz until asked. No gym. Not DSB. Not a diagnosis. Particulars .private/health.fu.md.
  - DO $id=probe-AgentCore $vertex=AgentCore PROBE In your own words: what is Amazon Bedrock AgentCore, and what is it not?
  - DONE 
  - SORE
  - STOP if SORE is not empty. python cron/interview-anchor.py --sore --text. Do not add more DO.

- DAY $date=2026-09-27
  - LOAD 1
  - TZ Europe/Berlin
  - WHY job seeking as AI agent engineer. Stop on SORE. External Wordschatz counts toward Ausdauer.
  - NOTE 2026-09-27 ~11:01 illness not fully re-named clear. Skip this PROBE and Wordschatz until asked. No gym. Not DSB. Not a diagnosis. Particulars .private/health.fu.md.
  - DO $id=probe-AgentCore $vertex=AgentCore PROBE In your own words: what is Amazon Bedrock AgentCore, and what is it not?
  - DONE 
  - SORE
  - STOP if SORE is not empty. python cron/interview-anchor.py --sore --text. Do not add more DO.

- DAY $date=2026-09-25
  - LOAD 1
  - TZ Europe/Berlin
  - WHY job seeking as AI agent engineer. Titles from the Amit Shekhar bank mapped onto this graph. Stop on SORE. External Wordschatz counts toward Ausdauer.
  - NOTE 2026-09-25 ~10:08 illness named. Skip this PROBE and Wordschatz until asked. Not DSB. Not a diagnosis. Particulars .private/health.fu.md.
  - DO $id=probe-AgentCore $vertex=AgentCore PROBE In your own words: what is Amazon Bedrock AgentCore, and what is it not?
  - DONE 
  - SORE
  - STOP if SORE is not empty. python cron/interview-anchor.py --sore --text. Do not add more DO.

- DAY $date=2026-09-24
  - LOAD 1
  - TZ Europe/Berlin
  - WHY job seeking as AI agent engineer. Titles from the Amit Shekhar bank mapped onto this graph. Stop on SORE. External Wordschatz counts toward Ausdauer.
  - DO $id=probe-AgentCore $vertex=AgentCore PROBE In your own words: what is Amazon Bedrock AgentCore, and what is it not?
  - DONE 
  - SORE
  - STOP if SORE is not empty. python cron/interview-anchor.py --sore --text. Do not add more DO.

- DAY $date=2026-09-02
  - LOAD 3
  - EXTERNAL planned 3 Wordschatz daily: 德语助手 法语助手 西语助手. Remaining hire DAY is 1 on budget 4. Log each --external --id de-assistant-wordschatz or fr-assistant-wordschatz or es-assistant-wordschatz. Do not invent a word count.
  - TZ Europe/Berlin
  - WHY job seeking as AI agent engineer. Titles from the Amit Shekhar bank mapped onto this graph. Stop on SORE.
  - DO $id=probe-AgentCore $vertex=AgentCore PROBE In your own words: what is Amazon Bedrock AgentCore, and what is it not?
  - DO $id=q-152-what-is-an-agent-loop-and-how-does-it-decide-whe $vertex=AgentLoop QUESTION What is an agent loop; and how does it decide when to stop? SOURCE https://outcomeschool.com/blog/ai-agent-loop
  - DO $id=q-148-what-is-model-context-protocol-mcp-and-how-does- $vertex=MCP QUESTION What is Model Context Protocol (MCP); and how does it standardize tool integration? SOURCE https://www.youtube.com/watch?v=lnfWvX66FUk
  - DONE 
  - SORE
  - STOP if SORE is not empty. python cron/interview-anchor.py --sore --text. Do not add more DO.

- PLAN $id=languages-b2-16
  - NOW NaturalLanguage
  - NEXT PolyglotHorizon WritingAccuracyArbitrage GrammarFrame DualSubtitle Pedagogy Study FuLanguage
  - DONE
  - ADJUST waiting. Sixteen languages named 2026-09-07 in pedagogy/_learn/polyglot/horizon.toon.md. Age 30 / target 35 in self/goals.toon.md. Do not invent CEFR beyond self-rating bands.
  - ADJUST 2026-09-07 writing-accuracy-base-arbitrage: real coding prompts in targetLang; store pedagogy/_learn/writing-accuracy/; hook sessionStart. Not a fake workbook. Empty PROBE until asked.
  - ADJUST 2026-09-07 polyglot: age-35 / 5y / 16 named langs; GrammarFrame×lexicon pairing; beforeSubmitPrompt detects primaryLang + code-switch gaps. Roster filled (de en es fr it pt fi vi el ru ar hi zh wuu ja ko).
  - ADJUST 2026-09-11 神游 harvest: named priority es fr de; rest on commerce rotation. Official URLs in pedagogy/_learn/polyglot/harvest.toon.md. Do not invent CEFR. Do not pile DAY. Empty PROBE.
  - WHY B2+ productive across the sixteen named languages by about age 35.

- PLAN $id=ai-agent-engineer
  - NOW AgentCore
  - NEXT AgentHarness ContextEngineering AgentHook MultiAgent AgentPlugin AgentToolkit LambdaMicroVM AgentLoop ExperienceStore NestedLearning MCP AgenticEngineering InterviewPrep CursorSkill LLMOps GitHubCI AgentRunMode Evaluation CloudRuntime SearchHarness Kiro RAG RalphLoop Archify SoftwareEngineering PromptEngineering AgentConstitution InformationSecurity ZeroKnowledgeProof Wrangler CloudflareWorkers CloudflareD1 AgentTty JavaProcessEnv SecretSurface HonestButCurious OAuthAuthorization AuthenticatedEncryption SpawnEnv WorkerBinding SecretRotation EnvFile ProcessEnvironment MinSecBinding ApiToken
  - DONE
  - ADJUST 2026-09-27 ~23:13 CPU quota of 100 sent applications (human 2026-09-25) stays a CPU count. Not a goals.north vertex. PLAN NOW stays AgentCore. Employer particulars stay in .private. Empty AgentCore PROBE. Do not invent ANSWER or a sent count.
  - ADJUST 2026-09-14 ~23:40 PLAN NEXT EnvFile ProcessEnvironment MinSecBinding ApiToken from human ask to learn MinSec systematically (shallow→deep ladder mezzanine/minsec-ladder.toon.md; panorama tmp/minsec-ladder/tree.html). NOW stays AgentCore. Not north. Empty AgentCore PROBE. Do not invent ANSWER or paste .env.
  - ADJUST 2026-09-14 ~21:03 PLAN NEXT SecretSurface HonestButCurious OAuthAuthorization AuthenticatedEncryption SpawnEnv WorkerBinding SecretRotation from human completeness pull on MinSec/ZK/CF. NOW stays AgentCore. Not north. Empty PROBE. Do not invent ANSWER.
  - ADJUST 2026-09-14 ~21:01 PLAN NEXT AgentTty JavaProcessEnv from human (agent tty + System.getProperty). NOW stays AgentCore. Not north. Empty PROBE. Do not invent ANSWER or paste env dumps.
  - ADJUST 2026-09-14 ~20:56 PLAN NEXT InformationSecurity ZeroKnowledgeProof Wrangler CloudflareWorkers CloudflareD1 from human MinSec study pull (ZK in infosec vs vendor E2EE; npx wrangler login). NOW stays AgentCore. Not added to goals.north. Empty PROBE. Do not invent ANSWER, a Cloudflare login, or a deployed Worker.
  - ADJUST 2026-09-11 ~10:14 PLAN NEXT PromptEngineering from STUDY empty GAP + 2026-bank split from ContextEngineering (Amit titles + mianling). NOW stays AgentCore. Not added to goals.north (window craft is already ContextEngineering on north). Empty PROBE. Do not invent ANSWER or paste bank essays.
  - ADJUST 2026-09-11 ~09:04 PLAN NEXT SoftwareEngineering from STUDY empty GAP + Cao 2026 CONTRADICT pole (arxiv 2606.05608). NOW stays AgentCore. Not added to goals.north (traditional static-D pole, not a hire line). Empty PROBE. Do not invent that software engineering has ended.
  - ADJUST 2026-09-11 ~07:54 PLAN NEXT Archify from STUDY empty GAP + human 2026-09-08 named it for skill/harness maps + https://tt-a1i.github.io/archify/. NOW stays AgentCore. Not added to goals.north (drawing tool for CursorSkill maps, not a hire line). Empty PROBE. Do not invent a global npx install.
  - ADJUST 2026-09-11 ~06:46 PLAN NEXT RalphLoop from STUDY empty GAP + DUMP strands-agent-loop (inner model-tool heartbeat vs Ralph new-session filesystem). NOW stays AgentCore. Not added to goals.north (human did not name it). Empty PROBE. Do not invent Ralph author or a strands-agents install.
  - ADJUST 2026-09-11 ~00:54 PLAN NEXT Evaluation from STUDY empty GAP + mianling safety theme + DUMP cursor-bugbot-github-check. NOW stays AgentCore. Not added to goals.north (human did not name it). Empty PROBE. Do not invent eval scores or Bugbot enabled here.
  - ADJUST 2026-09-10 ~23:44 PLAN NEXT AgentRunMode from STUDY empty GAP + Cursor Cloud Agents do not use Run Modes (DUMP cursor-cloud-agent-firecracker) vs Copilot on GHA. NOW stays AgentCore. Not added to goals.north (human did not name it). Empty PROBE. Do not invent Run Everything, a Cloud Agents run, or a Copilot assign.
  - ADJUST 2026-09-10 ~22:34 PLAN NEXT GitHubCI from STUDY empty GAP + Origin mirror keeps GitHub Actions + DUMP github-copilot-cloud-agent-gha. NOW stays AgentCore. Not added to goals.north (human did not name it). Empty PROBE. Do not invent this repo's CI, a Copilot assign, or a Codebase claim.
  - ADJUST 2026-09-10 evening PLAN NEXT LLMOps from STUDY stub + Signals LLMOps talk + Langfuse coding-agent tracing. NOW stays AgentCore. Not added to goals.north (human did not name it). Empty PROBE. Do not invent a Langfuse install.
  - ADJUST 2026-09-10 goals.north CursorSkill from Origin start-using. NOW stays AgentCore. Empty PROBE. Do not invent Codebase claim.
  - ADJUST 2026-09-09 graph+STUDY NestedLearning empty GAP. AgentCore stays NOW. DUMP still pending drip.
  - ADJUST 2026-09-06 psyche DUMP: pull hooks + subagents forward on NEXT and goals.north. AgentCore PROBE stays NOW / open ANSWER. ClaudeCode STUDY stays. Fog/rest: do not pile DAY; empty PROBE stays empty until asked. Repo still has no hook store and no plugin package — that is GAP not invented install.
  - ADJUST 2026-09-06 mianling AI Agent 155-theme bank https://www.mianlingai.com/topics/ai-agent-interview-questions-2026/ bottom-up onto AgentHarness ContextEngineering. Strategy pedagogy/_learn/interview-prep-strategy.toon.md. Cron interview-bank-enrich. Do not paste answers. Do not invent ANSWER.
  - WHY Job seeking as AI agent engineer. North now includes AgentHook MultiAgent AgentPlugin (Cursor/Claude harness). Lebenslauf Full-Stack Frontend plus attested Bedrock MCP AWS certs Kiro Claude Code. AgentCore is not a job line.

- PLAN $id=seo-geo-sidework
  - NOW SEO
  - NEXT GenerativeEngineOptimization AnswerEngineOptimization Ecommerce
  - DONE
  - ADJUST 2026-09-06 human SEO/GEO demand + web research. Google Search Central: foundational SEO for AI Overviews; GEO paper arXiv 2311.09735. Empty PROBE until asked. Do not invent client traffic. Do not paste NAP.
  - ADJUST 2026-09-11 神游 opportunity organ hunts public 商机 into DUMP KIND opportunity. Not hire NOW (AgentCore stays focus). Do not invent a bid.
  - WHY Side-site / 杂活 visibility literacy. Citation KPI ≠ sessions. Mirror .cursor/skills/dev-sidework. Not hire NOW (AgentCore stays focus).

- PLAN $id=astrophysics
  - NOW Astrophysics
  - NEXT
  - DONE
  - ADJUST 2026-09-16 human named intent to learn Astrophysik. Vertex + empty GAP. Not added to goals.north (not a hire line). AgentCore stays hire NOW. Empty PROBE until asked. Do not invent ANSWER or a paper ladder.
  - WHY Physics of celestial Matter. Internalization, not a job vertex.

- STUDY $id=AgentHarness
  - WHY 2026 hire bank disaster zone: harness vs prompt vs context. Runtime shell. Empty GAP. Do not invent ANSWER. Do not pile DAY on fog.
  - STORE PATH pedagogy/computation/AgentHarness.fu.md
  - RECALL
  - GAP
  - NOTE 2026-09-28 ~05:43 GAP stays empty. New edge Form INFORMS Matter SOURCE pedagogy/being/being.fu.md does not answer harness vs prompt vs context. Do not invent ANSWER. AgentCore PROBE stays empty.

- STUDY $id=ContextEngineering
  - WHY Window craft: compress unload pollution. Separated from PromptEngineering in 2026 banks. Empty GAP. Do not invent ANSWER. Do not pile DAY on fog.
  - STORE PATH pedagogy/computation/ContextEngineering.fu.md
  - RECALL
  - GAP

- STUDY $id=PromptEngineering
  - WHY 2026 hire banks split this from ContextEngineering (window craft vs steering with language). Graph already STUDIES it from Amit titles; pedagogy-cpu had no stub. Empty GAP. Do not invent ANSWER. Do not paste bank essays. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/language/PromptEngineering.fu.md
  - STORE PATH https://github.com/amitshekhariitbhu/ai-engineering-interview-questions
  - RECALL
  - GAP

- STUDY $id=InterviewPrep
  - WHY Retrieval-first hire pedagogy. Strategy in _learn/interview-prep-strategy.toon.md. Multi-turn PROBE. Empty GAP. Do not invent ANSWER. Do not paste bank essays.
  - STORE PATH pedagogy/language/InterviewPrep.fu.md
  - RECALL
  - GAP

- STUDY $id=AutobiographicalMemory
  - WHY Conway SMS hierarchy for personal knowledge vs ontology Essence. Particulars stay .private. Empty GAP. Do not invent ANSWER. Do not diagnose.
  - STORE PATH pedagogy/biology/AutobiographicalMemory.fu.md
  - RECALL
  - GAP

- STUDY $id=History
  - WHY Collective/project narrative assembled from graph on demand. Soft interview arcs. Empty GAP. Do not invent ANSWER. Do not paste Lebenslauf.
  - STORE PATH pedagogy/language/History.fu.md
  - RECALL
  - GAP

- STUDY $id=AgentCore
  - PHASE probe
  - WHY Job-seeking as AI agent engineer. PLAN NOW is AgentCore from goals.north. Rest is on. Do not invent ANSWER. Do not pile DAY.
  - STORE PATH pedagogy/computation/AgentCore.fu.md
  - PROBE
    - In your own words: what is Amazon Bedrock AgentCore, and what is it not?
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=MemoryAssembly
  - WHY Nature 2024 TLR9 cascade is the first deep body. Walk g.V(MemoryAssembly).in().out().
  - STORE PATH pedagogy/biology/MemoryAssembly.fu.md
  - RECALL
  - GAP
  - DRILL How does TLR9Signalling CONTRADICT GenomicInstability without CONTRADICT ImmediateEarlyGene?

- STUDY $id=GraphTraversal
  - WHY this store is itself a Gremlin walk. Attested in Cosmos Gremlin plus pedagogy/universe.graph.md.
  - STORE PATH pedagogy/math/GraphTraversal.fu.md
  - NOTE 2026-09-28 ~02:53 GAP stays empty. New edge Form INFORMS AgentLoop SOURCE pedagogy/being/being.fu.md. Do not invent ANSWER. AgentCore PROBE stays empty.
  - RECALL
  - GAP

- STUDY $id=AgentLoop
  - WHY inner heartbeat versus outer slash-loop. Source skills/loop-slash/PUBLISH.md.
  - STORE PATH pedagogy/computation/AgentLoop.fu.md
  - NOTE 2026-09-28 ~00:03 GAP stays empty. Sourced claim on AgentLoop.fu.md: the outer maintain /loop skips an organ with no new Matter. Graph edge AgentLoop GROUNDS_IN Form. Do not invent ANSWER. AgentCore PROBE stays empty.
  - RECALL
  - GAP

- STUDY $id=ExperienceStore
  - WHY Hermes skills docs: SKILL.md as procedural memory, agentskills.io portable, same shape as CursorSkill. Graph already has ExperienceStore INFORMS CursorSkill. Empty GAP. Do not invent ANSWER. Do not pile DAY on fog. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/ExperienceStore.fu.md
  - RECALL
  - GAP

- STUDY $id=NestedLearning
  - WHY Google Nested Learning NeurIPS 2025: nested optimization levels and continuum memory. Graph V NestedLearning. Analog of organ-inside-organism. Empty GAP. Do not invent ANSWER. Do not pile DAY on fog. Do not install Hope. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/NestedLearning.fu.md
  - RECALL
  - GAP

- STUDY $id=CursorSkill
  - WHY goals.north 2026-09-10 Origin start-using. SKILL.md as packaged procedure; Origin docs keep GitHub as SoT for synced repos. Graph already STUDIES CursorSkill. Empty GAP. Do not invent ANSWER. Do not invent a claimed codebase or Windows origin CLI. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/CursorSkill.fu.md
  - STORE PATH https://cursor.com/docs/origin
  - RECALL
  - GAP

- STUDY $id=LLMOps
  - WHY Signals day-1 Vechtomova LLMOps in agentic coding; Langfuse coding-agent tracing INFORMS LLMOps from graph tick. Empty GAP. Do not invent ANSWER. Do not invent a Langfuse install. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/LLMOps.fu.md
  - STORE PATH https://langfuse.com/resources/engineering/coding-agent-tracing
  - RECALL
  - GAP

- STUDY $id=AgentToolkit
  - WHY goals.north + PLAN NEXT. AWS Agent Toolkit is curated SKILL.md plus managed AWS MCP Server; product page names Kiro Claude Code Codex. Empty GAP. Do not invent ANSWER. Do not invent a toolkit install in this repo. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/AgentToolkit.fu.md
  - STORE PATH https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/
  - RECALL
  - GAP

- STUDY $id=LambdaMicroVM
  - WHY goals.north + PLAN NEXT. Firecracker isolation for agent-generated code; Agent Toolkit skill aws-lambda-microvms; nested with AgentCore session isolation. Empty GAP. Do not invent ANSWER. Do not invent that this repo's CI already runs MicroVMs. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/LambdaMicroVM.fu.md
  - STORE PATH https://aws.amazon.com/blogs/compute/secure-code-execution-for-ai-agents-with-aws-lambda-microvms/
  - RECALL
  - GAP

- STUDY $id=MCP
  - WHY goals.north + PLAN NEXT. Typed tool protocol for models; AgentCore Gateway and Claude Code wrap MCP; Langfuse Cursor traces log MCP tool calls. Empty GAP. Do not invent ANSWER. Do not invent a new MCP server in this repo. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/MCP.fu.md
  - STORE PATH https://code.claude.com/docs/en/features-overview
  - RECALL
  - GAP

- STUDY $id=GitHubCI
  - WHY Origin docs keep GitHub as SoT for synced repos; Lambda MicroVMs named as CI sandboxes. Empty GAP. Do not invent ANSWER. Do not invent that this repo's GitHub CI runs MicroVMs or that Origin is claimed. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/GitHubCI.fu.md
  - STORE PATH https://cursor.com/docs/origin
  - RECALL
  - GAP

- STUDY $id=AgentRunMode
  - WHY Local Cursor Run Modes (Auto-review / Allowlist / Run Everything) vs Copilot cloud agent on GitHub Actions vs Cloud Agents on a dedicated machine (docs: Cloud Agents do not use Run Modes). Empty GAP. Do not invent ANSWER. Do not invent Fetch allowlist or Run Everything flipped here. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/AgentRunMode.fu.md
  - STORE PATH https://cursor.com/docs/agent/security/run-modes
  - RECALL
  - GAP

- STUDY $id=Evaluation
  - WHY Mianling safety theme maps Evaluation + LLMOps; interview bank titles already CLAIM this vertex. Nested vs Copilot cloud agent running tests in GHA and vs AgentCore PROBE (do not invent eval ANSWER). Empty GAP. Do not invent ANSWER. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/math/Evaluation.fu.md
  - STORE PATH https://github.com/amitshekhariitbhu/ai-engineering-interview-questions
  - RECALL
  - GAP

- STUDY $id=CloudRuntime
  - WHY AgentLoop already INFORMS CloudRuntime via the GitHub 17 Aug 2026 outage postmortem (agentic traffic as capacity). Nested vs Copilot cloud agent on GitHub Actions and Cursor Cloud Agents in Firecracker VMs. Empty GAP. Do not invent ANSWER. Do not invent a live GitHub incident, this repo's CI, or Cloud Agents on this workspace. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/CloudRuntime.fu.md
  - STORE PATH https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/
  - RECALL
  - GAP

- STUDY $id=SearchHarness
  - WHY AgentCore names a Harness service as a managed agent loop in an isolated microVM; SearchHarness is the same shape (search over programs with feedback). Nested vs AgentLoop + Evaluation (Copilot GHA runs tests) and vs DUMP agentcore-harness-managed-loop. Empty GAP. Do not invent ANSWER. Do not invent extra star counts or a profit metric. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/SearchHarness.fu.md
  - STORE PATH https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
  - STORE PATH https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html
  - RECALL
  - GAP

- STUDY $id=Kiro
  - WHY Agent Toolkit for AWS names Kiro as a target IDE; attested in skill.toon.md next to Cursor and Claude Code. Nested vs ClaudeCode STUDY and CursorSkill. Empty GAP. Do not invent ANSWER. Do not invent a Kiro install in this repo or extra employment. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/Kiro.fu.md
  - STORE PATH https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/
  - RECALL
  - GAP

- STUDY $id=RAG
  - WHY Mianling memory/sysdesign themes map RAG; interview-bank EXPECTED_V already OK. Nested vs ContextEngineering APPLIES RAG and vs ExperienceStore. Empty GAP. Do not invent ANSWER. Do not paste cheat-sheet answers. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/RAG.fu.md
  - STORE PATH https://www.mianlingai.com/topics/ai-agent-interview-questions-2026/
  - STORE PATH https://github.com/amitshekhariitbhu/ai-engineering-interview-questions
  - RECALL
  - GAP

- STUDY $id=RalphLoop
  - WHY BV1t9oZBDENp: new session each tick, context through the filesystem. Nested vs this metabolize loop (STATE.md) and vs MultiAgent STUDY (talk prefers MultiAgent, not a CONTRADICT). Empty GAP. Do not invent ANSWER. Do not invent Ralph author, repo, or benchmarks. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/RalphLoop.fu.md
  - STORE PATH https://www.bilibili.com/video/BV1t9oZBDENp
  - RECALL
  - GAP

- STUDY $id=Archify
  - WHY Human 2026-09-08 named Archify for skill/harness maps. Nested vs CursorSkill and vs PlantUML/Kroki (LaTeX/video stills stay). Empty GAP. Do not invent ANSWER. Do not invent a global npx install (this machine was Node 20). Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/Archify.fu.md
  - STORE PATH https://tt-a1i.github.io/archify/
  - RECALL
  - GAP

- STUDY $id=ZeroKnowledgeProof
  - WHY Human 2026-09-14 named ZK inside Informationssicherheit. Split from ClientHeldSecret / MinSec slogan. Empty GAP. Do not invent ANSWER. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/math/ZeroKnowledgeProof.fu.md
  - STORE PATH https://en.wikipedia.org/wiki/Zero-knowledge_proof
  - RECALL
  - GAP
  - DRILL In one sentence: what does a zero-knowledge proof hide, and what does it still convince the verifier of?

- STUDY $id=Wrangler
  - WHY Human 2026-09-14 named npx wrangler login as unfamiliar. Nested vs CloudflareWorkers + D1 + MinSec deploy. Empty GAP. Do not invent ANSWER. Do not invent a completed OAuth login. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/Wrangler.fu.md
  - STORE PATH https://developers.cloudflare.com/workers/wrangler/commands/general/
  - RECALL
  - GAP
  - DRILL What does `npx wrangler login` open, and when would you pass `--device`?

- STUDY $id=CloudflareWorkers
  - WHY Human 2026-09-14 named deeper Cloudflare study while using MinSec. Nested vs Cloudflare D1 Wrangler ClientHeldSecret. Empty GAP. Do not invent ANSWER or a deployed Worker here. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/CloudflareWorkers.fu.md
  - STORE PATH https://developers.cloudflare.com/workers/
  - RECALL
  - GAP

- STUDY $id=AgentTty
  - WHY Human 2026-09-14 named agent tty as a MinSec leak surface. Nested vs ClientHeldSecret and ContextEngineering. Empty GAP. Do not invent ANSWER. Do not paste env dumps. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/AgentTty.fu.md
  - STORE PATH mezzanine/minsec-masterclass.toon.md
  - RECALL
  - GAP
  - DRILL Why does hiding .env from the indexer still fail if the agent runs minsec list?

- STUDY $id=JavaProcessEnv
  - WHY Human 2026-09-14 named Java System.getProperty next to MinSec inject. Nested vs Java + MinSec README. Empty GAP. Do not invent ANSWER. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/JavaProcessEnv.fu.md
  - STORE PATH https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/System.html#getenv(java.lang.String)
  - RECALL
  - GAP
  - DRILL Which Java API reads OS environment, and which reads -D properties?

- STUDY $id=SecretSurface
  - WHY Human 2026-09-14 asked for further Forderungen on likely-missing knowledge for completeness of this Verständnis, based on named gaps (slogan-ZK, wrangler login, AgentTty, getProperty). Empty GAP. Do not invent ANSWER. Do not paste secrets. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/SecretSurface.fu.md
  - RECALL
  - GAP
  - DRILL Name three places a secret can live that are not a gitignored .env.
  - DRILL Honest-but-curious vs ZeroKnowledgeProof vs ClientHeldSecret: one sentence each.
  - DRILL What protocol is npx wrangler login, and how is it not a MinSec API token?
  - DRILL Why AES-GCM is authenticated encryption, and what nonce reuse does.
  - DRILL What does spawn env merge from the parent process?
  - DRILL Worker env.SECRET vs Node process.env vs JVM getProperty vs Wrangler .dev.vars.
  - DRILL Rotate vs revoke vs leftover file vs leftover agent TTY log.

- STUDY $id=EnvFile
  - WHY Human 2026-09-14 asked for a beginner ladder on MinSec. Rung 1: plaintext workspace file vs later crypto. Empty GAP. Do not invent ANSWER. Do not paste .env values. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/EnvFile.fu.md
  - STORE PATH mezzanine/minsec-ladder.toon.md
  - RECALL
  - GAP
  - DRILL After minsec import .env, who can still read the original file?

- STUDY $id=ProcessEnvironment
  - WHY Human 2026-09-14 asked for a beginner ladder on MinSec. Rung 2: OS env block vs .env file vs JVM -D. Empty GAP. Do not invent ANSWER. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/ProcessEnvironment.fu.md
  - STORE PATH mezzanine/minsec-ladder.toon.md
  - RECALL
  - GAP
  - DRILL Name three APIs that read the OS environment, one per language you know.

- STUDY $id=MinSecBinding
  - WHY Human 2026-09-14 asked for a beginner ladder on MinSec. Rung 3: linkage file is not the vault. Empty GAP. Do not invent ANSWER or a completed minsec init. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/MinSecBinding.fu.md
  - STORE PATH mezzanine/minsec-ladder.toon.md
  - RECALL
  - GAP
  - DRILL Which three filenames does the CLI look for, and which one does init write?

- STUDY $id=ApiToken
  - WHY Human 2026-09-14 asked for a beginner ladder on MinSec. Rung 5: bearer token vs OAuth vs Worker secret. Empty GAP. Do not invent ANSWER or paste ms_tok. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/ApiToken.fu.md
  - STORE PATH mezzanine/minsec-ladder.toon.md
  - RECALL
  - GAP
  - DRILL One sentence each: wrangler login, minsec ms_tok, wrangler secret put.

- STUDY $id=MinSec
  - WHY Human 2026-09-14 asked to learn MinSec systematically from shallow to deep. Product vertex; walk mezzanine/minsec-ladder.toon.md. Empty GAP. Do not invent ANSWER, a migrate, or wrangler login. Do not paste secrets. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/stack/MinSec.fu.md
  - STORE PATH mezzanine/minsec-ladder.toon.md
  - STORE PATH https://github.com/cgx9/minsec
  - RECALL
  - GAP
  - DRILL VARIABLE vs SECRET: where does each live at rest?
  - DRILL What does minsec run actually do to the child process?

- STUDY $id=KVCache
  - WHY kvcached is virtual memory for attention state. Source https://github.com/ovg-project/kvcached
  - STORE PATH pedagogy/computation/KVCache.fu.md
  - RECALL
  - GAP

- STUDY $id=AgenticEngineering
  - WHY Cao 2026 claims code becomes ephemeral. CONTRADICTS SoftwareEngineering as a paper claim, not a deletion of Computation.
  - STORE PATH pedagogy/computation/AgenticEngineering.fu.md
  - RECALL
  - GAP
  - DRILL What stays in Computation when decision logic is generated at runtime?

- STUDY $id=SoftwareEngineering
  - WHY Cao 2026 CONTRADICT pole: static decision rules D written before input (NATO 1968 / Brooks). AgenticEngineering already has a STUDY; this vertex did not. Empty GAP. Do not invent ANSWER. Do not delete this V. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/SoftwareEngineering.fu.md
  - STORE PATH https://arxiv.org/html/2606.05608v1
  - RECALL
  - GAP

- STUDY $id=MultiAgent
  - WHY BV1t9oZBDENp harness talk + 2026-09-06 psyche DUMP: learn Cursor/Claude subagents more. Coordinator vs specialists. Do not invent ANSWER. Do not pile DAY on fog.
  - STORE PATH pedagogy/computation/MultiAgent.fu.md
  - PROBE
    - In your own words: what is a subagent for, and how is it not just a longer main-agent turn?
  - ANSWER
  - ASSESS
  - RECALL
  - GAP
  - DRILL Why does the talk prefer MultiAgent over RalphLoop without a CONTRADICT edge?

- STUDY $id=AgentHook
  - WHY 2026-09-06 psyche DUMP: bias learn toward hooks (Claude Code + Cursor create-hook). Quality the model cannot guarantee. Empty ANSWER. Do not invent a hook store. Do not pile DAY on fog.
  - STORE PATH pedagogy/computation/AgentHook.fu.md
  - STORE PATH mezzanine/claude-code-layers.toon.md
  - PROBE
    - Name one lifecycle event a hook can catch, and one failure mode that a prompt-only rule cannot fix.
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=AgentPlugin
  - WHY Bundles skills+hooks+subagents. Psyche pull 2026-09-06. Gap: this repo has no marketplace plugin. Empty ANSWER. Do not invent install.
  - STORE PATH pedagogy/computation/AgentPlugin.fu.md
  - PROBE
    - What problem does a plugin solve that a loose folder of SKILL.md files does not?
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=NaturalLanguage
  - WHY attested SPRACHEN only. Wordschatz is the daily drill, not a new language name.
  - STORE PATH pedagogy/language/NaturalLanguage.fu.md
  - RECALL
  - GAP

- STUDY $id=Wordschatz
  - WHY daily 德语助手 法语助手 西语助手 lexicon drill. Counts as IntellectualLoad. Empty GAP. Do not invent a word count.
  - STORE PATH pedagogy/language/Wordschatz.fu.md
  - RECALL
  - GAP

- STUDY $id=WritingAccuracyArbitrage
  - WHY One stone N birds: target-language agent instructions → writing accuracy byproduct. Method pedagogy/_learn/writing-accuracy/method.toon.md. Lexicon graph separate. Hook injects todayFocus. Empty GAP. Do not invent ANSWER. Do not turn agent into grammar teacher.
  - STORE PATH pedagogy/language/WritingAccuracyArbitrage.fu.md
  - RECALL
  - GAP

- STUDY $id=PolyglotHorizon
  - WHY 16 named languages toward B2+ by age 35. Roster horizon.toon.md. Empty GAP. Do not invent CEFR beyond bands. 中文/吴语 native_or_bilingual per human 2026-09-07.
  - STORE PATH pedagogy/language/PolyglotHorizon.fu.md
  - RECALL
  - GAP
  - NOTE 2026-09-28 ~07:53 GAP stays empty. New edge Form INFORMS PolyglotHorizon SOURCE pedagogy/being/being.fu.md names the rest_pointer rule. It does not fill the roster or a CEFR. Do not invent ANSWER. AgentCore PROBE stays empty.

- STUDY $id=GrammarFrame
  - WHY Grammar = Frame with slots; lexicon fills slots; Chunk = filled Frame. Pairing pedagogy/_learn/polyglot/pairing.toon.md. Empty GAP. Do not invent ANSWER.
  - STORE PATH pedagogy/language/GrammarFrame.fu.md
  - RECALL
  - GAP

- STUDY $id=LanguageDrilling
  - WHY TESOL Lexical Press 2024-03-07. Controlled repetition for Automaticity. Species ChoralRepetition ChainDrill SubstitutionDrill. CONTRADICTS CommunicativePractice when it is the whole lesson. Empty GAP. Do not invent ANSWER. Do not add to DAY.
  - STORE PATH pedagogy/language/LanguageDrilling.fu.md
  - RECALL
  - GAP

- STUDY $id=DualSubtitle
  - WHY languages-b2-16 NEXT. Two-language captions on one picture (Bilibili extension attested; loop-slash DE over EN). Graph already STUDIES DualSubtitle; pedagogy-cpu had no stub. Empty GAP. Do not invent ANSWER. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/language/DualSubtitle.fu.md
  - STORE PATH skills/video-generation.fu.md
  - RECALL
  - GAP

- STUDY $id=SlashCommand
  - WHY attested slashes /loop /goal /onboard /rename-chat /shell and video /schedule. Catalog mezzanine/cursor-slash.toon.md
  - STORE PATH pedagogy/language/SlashCommand.fu.md
  - RECALL
  - GAP

- STUDY $id=ClaudeCode
  - WHY attested CLI. Five harness layers on the graph. Hire-weight after AgentCore. Card vs docs in mezzanine/claude-code-layers.toon.md. Empty GAP until RECALL.
  - STORE PATH pedagogy/computation/stack/ClaudeCode.fu.md
  - RECALL
  - GAP

- STUDY $id=AgentConstitution
  - WHY Claude Code layer: always-on rules (CLAUDE.md) vs this repo ROOT.md + CPU.md + pedagogy-cpu. Graph already INFORMS Agent; pedagogy-cpu had no stub. Empty GAP. Do not invent ANSWER. Do not write a CLAUDE.md into this tree. Do not pile DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/AgentConstitution.fu.md
  - STORE PATH https://code.claude.com/docs/en/features-overview
  - RECALL
  - GAP

- STUDY $id=AWS
  - WHY cloud children ECS EKS Fargate Bedrock SQS CDK CloudFormation DynamoDB. Kafka is not sourced.
  - STORE PATH pedagogy/computation/stack/AWS.fu.md
  - RECALL
  - GAP

- STUDY $id=Ecommerce
  - WHY Home and living goods over the network. Disposition is the stock clock. CrossBorderTrade is the second language and customs clock. SEO GEO AEO PARTICIPATE for findability. Named employer Bewerbung Gehalt stay in .private. Empty GAP. Do not invent ANSWER. Do not add to DAY.
  - STORE PATH pedagogy/computation/Ecommerce.fu.md
  - RECALL
  - GAP

- STUDY $id=SEO
  - WHY Classic link-list visibility. Floor for Google generative features per Search Central. Sidework trust+crawl first. Empty GAP. Do not invent ANSWER. Do not invent client rankings. Do not add to DAY.
  - STORE PATH pedagogy/computation/SEO.fu.md
  - RECALL
  - GAP

- STUDY $id=GenerativeEngineOptimization
  - WHY GEO = citation / visibility inside synthesized answers. KDD 2024 GEO-bench. Google: SEO over AEO/GEO hacks for Google Search. Empty GAP. Do not invent ANSWER. Do not sell paper visibility as sessions. Do not add to DAY.
  - STORE PATH pedagogy/computation/GenerativeEngineOptimization.fu.md
  - RECALL
  - GAP

- STUDY $id=AnswerEngineOptimization
  - WHY AEO = extractable direct answers. Overlaps SEO/GEO. Answer-first blocks. Empty GAP. Do not invent ANSWER. Do not invent quotes. Do not add to DAY.
  - STORE PATH pedagogy/computation/AnswerEngineOptimization.fu.md
  - RECALL
  - GAP

- STUDY $id=Disposition
  - WHY German commercial clock: what is ordered, what sits in stock, when it must arrive. PARTICIPATES Ecommerce. Empty GAP. Do not invent an ERP. Do not add to DAY.
  - STORE PATH pedagogy/computation/Disposition.fu.md
  - RECALL
  - GAP

- STUDY $id=AISafety
  - WHY IFA Hall 25 kitchen robots name trust, safety, and acceptance as physical automation enters intimate spaces. Same vertex as the interview-bank hire titles. Empty GAP. Do not invent ANSWER. Do not add to DAY. AgentCore PROBE stays the open question.
  - STORE PATH pedagogy/computation/AISafety.fu.md
  - RECALL
  - GAP

- STUDY $id=SicknessBehavior
  - WHY Hart/Dantzer motivational reorganization vs named DSB. Packing/inventory same brake. LowDemandIntake while fog. Empty GAP. Do not invent ANSWER. Do not add to DAY. Do not diagnose.
  - STORE PATH pedagogy/biology/SicknessBehavior.fu.md
  - RECALL
  - GAP

- STUDY $id=VideoGeneration
  - WHY script→TTS→PNG→meme→ffmpeg→ASS contract. DualSubtitle type floor. Retry-safe CDN/PIL. Improve via shared video_kit. Empty GAP. Do not invent ANSWER. Do not add to DAY.
  - STORE PATH pedagogy/computation/VideoGeneration.fu.md
  - RECALL
  - GAP

- STUDY $id=AgentStreamDrop
  - WHY stream dies before save. Network ladder + small-turn load. Empty GAP. Do not invent ANSWER. Do not paste private ports. Do not add to DAY.
  - STORE PATH pedagogy/computation/AgentStreamDrop.fu.md
  - RECALL
  - GAP

- STUDY $id=BinauralBeat
  - WHY stereo difference tone; entrainment unreliable; avoid 15 Hz on tests; rest-audio class with Hemi-Sync. Empty GAP. Do not invent ANSWER. Do not add to DAY.
  - STORE PATH pedagogy/biology/BinauralBeat.fu.md
  - RECALL
  - GAP

- STUDY $id=Caffeine
  - WHY EFSA 2015 class ceilings. Sleep damage amplifies fog. Not a personal stack. Empty GAP. Do not invent ANSWER. Do not add to DAY.
  - STORE PATH pedagogy/biology/Caffeine.fu.md
  - RECALL
  - GAP

- STUDY $id=AphthousUlcer
  - WHY mucosa lesion class; watermelon frost vs Kamistad no H2H RCT; red flags → clinic. Empty GAP. Do not invent ANSWER. Do not prescribe. Do not add to DAY.
  - STORE PATH pedagogy/biology/AphthousUlcer.fu.md
  - RECALL
  - GAP

- STUDY $id=LowDemandIntake
  - WHY cheap attention while SicknessBehavior discounts effort. CONTRAST DSB stop. Empty GAP. Do not invent ANSWER. Do not add to DAY.
  - STORE PATH pedagogy/biology/LowDemandIntake.fu.md
  - RECALL
  - GAP

- STUDY $id=AestheticChills
  - WHY Schoeller 2024 CABN review. Fig.1 VTA→NAcc. Fig.2 wanting/liking/learning. Benefits preliminary only. Empty GAP. Do not invent ANSWER. Do not diagnose. Do not add to DAY on fog.
  - STORE PATH pedagogy/biology/AestheticChills.fu.md
  - STORE PATH mezzanine/aesthetic-chills-schoeller-2024.toon.md
  - PROBE
    - In your own words: what are aesthetic chills, and why do they matter for studying embodied reward?
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=IncentiveSalience
  - WHY Berridge wanting/liking/learning as zero-step before Schoeller Fig.2. Empty GAP. Do not invent ANSWER. Do not add to DAY on fog.
  - STORE PATH pedagogy/biology/IncentiveSalience.fu.md
  - PROBE
    - Separate wanting, liking, and learning in one concrete example (food or music).
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=Interoception
  - WHY goosebumps as data; insula; objective vs subjective chill split. Empty GAP. Do not invent ANSWER. Do not add to DAY on fog.
  - STORE PATH pedagogy/biology/Interoception.fu.md
  - PROBE
    - Why can a bodily shiver change how an outside cue feels valuable?
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=PredictiveCoding
  - WHY prediction error vs precision; incoherent primes inhibit chills. Empty GAP. Do not invent ANSWER. Do not add to DAY on fog.
  - STORE PATH pedagogy/math/PredictiveCoding.fu.md
  - PROBE
    - What is precision weighting, in one analogy that is not about dopamine pills?
  - ANSWER
  - ASSESS
  - RECALL
  - GAP

- STUDY $id=Astrophysics
  - WHY Human 2026-09-16 named intent to learn Astrophysik. Physics of celestial Matter. Empty GAP. Do not invent ANSWER. Do not invent a paper ladder until a SOURCE is named. Do not pile DAY. AgentCore stays PLAN NOW for hire.
  - STORE PATH pedagogy/physics/Astrophysics.fu.md
  - STORE PATH https://science.nasa.gov/astrophysics/
  - RECALL
  - GAP

- REVIEW open STUDY whose ANSWER or GAP is empty. Empty means wait or not yet internalized. Do not mark DONE.

- ASK SHOWCASE image or video. Default image. Then AGENT ontology-showcase with matching $output.
- ASK TRAVERSE gremlin-lite. Compact. No essay.
- ASK LEARN answer the open PROBE in chat or under ANSWER. Agent runs --answer --text then --assess. Do not ask the human to open an html file in the repo.
- ASK BASELINE fill tmp/pedagogy/baseline.html or http://127.0.0.1:8777/ in Chrome or Edge, not the Cursor panel. Four boxes: English, 中文, Français, Deutsch. Speak or type. Skip any language. Save. Then --ingest-baseline. Do not invent ANSWER.
- ASK DAY what to do today. python cron/interview-anchor.py --print. Finished: --done --id. Sore: --sore --text. Wordschatz session: --external --id de-assistant-wordschatz or fr-assistant-wordschatz or es-assistant-wordschatz.
- ASK DUMP when back, run dump-drip. Away loops write inflow/DUMP.md only. PII pass then drip. Empty PROBE stays empty.
- ASK CHILLS one rung on aesthetic-chills-ladder. AGENT aesthetic-chills-ladder. Fog day: at most one PROBE.

- AGENT $id=day-plan $input=pedagogy/pedagogy-cpu.fu.md $prompt=python cron/interview-anchor.py --day. Print today's DO in order. Stop. When the human finishes one, --done --id. When they say sore, --sore --text and stop the day. Do not invent ANSWER. Do not spawn janitor.

- AGENT $id=study-probe $input=pedagogy/pedagogy-cpu.fu.md $prompt=Read PROTOCOL. python cron/learn-enrich.py --probe. Ask that one question. Stop. When the human answers, python cron/learn-enrich.py --answer --text their words. Then react. Next PROBE or follow-up. Do not lecture first. Do not invent ANSWER. Do not store html. Do not spawn janitor.

- AGENT $id=learn-enrich $input=pedagogy/universe.graph.md $prompt=Read cron/learn-enrich.fu.md and self/goals.toon.md. python cron/learn-enrich.py --status. If ANSWER present, --assess. Else --probe. NORTH follows goals.focus. Do not spawn janitor.

- AGENT $id=ontology-showcase $input=pedagogy/universe.graph.md $prompt=Read skills/ontology-showcase.fu.md. ASK image or video if $output unset. python skills/ontology-showcase.py --mode image|video --deliver. Deliver into tmp/pedagogy/. python cron/janitor.py --touch. Delete tmp/_work/showcase after the delivered file exists.

- AGENT $id=aesthetic-chills-ladder $input=mezzanine/aesthetic-chills-schoeller-2024.toon.md $prompt=Read mezzanine/aesthetic-chills-schoeller-2024.toon.md and pedagogy/biology/AestheticChills.fu.md. Prefer tmp/aesthetic-chills-framework.pdf as the domain map. Walk six rungs: IncentiveSalience → Interoception → PredictiveCoding → Fig.1 → Fig.2 → Benefits-bounds. Ask ONE PROBE for the current unfinished rung only. Wait for ANSWER. Do not invent ANSWER. Do not lecture the whole paper. Fog: ≤1 rung. Cite doi:10.3758/s13415-024-01168-x. Never prescribe. Do not spawn janitor.

- AGENT $id=minsec-ladder $input=mezzanine/minsec-ladder.toon.md $prompt=Read mezzanine/minsec-ladder.toon.md and SecretSurface / MinSec bodies. Prefer tmp/minsec-ladder/tree.html as the panorama. Walk six rungs: EnvFile → ProcessEnvironment → MinSecBinding → ClientHeldSecret-vs-ZK → ApiToken-vs-OAuth → SecretRotation. Ask ONE PROBE for the current unfinished rung only. Wait for ANSWER. Do not invent ANSWER. Do not lecture all six. Do not paste .env, tokens, or minsec list output. Fog: ≤1 rung. Do not spawn janitor.

- AGENT $id=paper-muscle-ladder $input=.cursor/skills/paper-muscle/SKILL.md $prompt=Read .cursor/skills/paper-muscle/SKILL.md and the active mezzanine curriculum for the seed paper. Ask ONE PROBE for the current unfinished rung only. Wait for ANSWER. Do not invent ANSWER. Do not lecture the whole paper. Framework PDF must already exist or be offered as compile target. Fog: ≤1 rung. Never prescribe. Fresh b-roll rule when video asked. Do not spawn janitor.


- EXECUTED ON 2026-09-02
- AGENT $id=ontology-enrich
  - DONE Nature s41586-024-07220-7 TLR9 memory cascade into pedagogy/biology
  - DONE lebenslauf domains into math physics computation language. No Person vertex.
  - DONE Study FuLanguage ResistanceTraining as attested essences
  - DONE kvcached as KVCache. arXiv 2606.05608 as AgenticEngineering CONTRADICTS SoftwareEngineering. loop-slash as AgentLoop.
  - DONE lebenslauf stack leaves: JavaScript TypeScript AWS ECS EKS SQS React NextJS and 60 more under pedagogy/computation/stack/. Kafka not in skill toon.
  - DONE 2026-09-02 learn-enrich AgentCore AgentToolkit LambdaMicroVM. PROTOCOL is now PROBE then ANSWER then ASSESS then PLAN.
  - DONE 2026-09-02 Claude Code five-layer harness: AgentConstitution AgentHook AgentPlugin onto ClaudeCode CursorSkill MultiAgent MCP. Not NOW. DAY LOAD 3 unchanged.
  - DONE 2026-09-06 fog/video/retry graft: VideoGeneration AgentStreamDrop BinauralBeat Caffeine AphthousUlcer LowDemandIntake. Enriched SicknessBehavior IntellectualLoad DualSubtitle CursorSkill AgentLoop Multimodal Agent. STUDY stubs empty ANSWER. No Person. No private mg.
  - DONE 2026-09-06 meditation session map: AestheticChills vertex; mezzanine/meditation-binaural-2026-09-06.toon.md; private session log; tmp meditation-report PDF+MP4. Entropy metaphor cautioned vs EEG complexity reviews.
  - DONE 2026-09-06 Schoeller 2024 expand: IncentiveSalience Interoception PredictiveCoding; mezzanine curriculum; AGENT aesthetic-chills-ladder; tmp aesthetic-chills-study PDF+MP4 Bilibili-facing.
  - DONE 2026-09-06 paper-muscle skill + aesthetic-chills-framework.pdf (4p domain scaffold) + fresh Mixkit b-roll rebuild; paper-muscle.pdf paradigm.
  - OUTPUT PATH pedagogy/universe.graph.md
