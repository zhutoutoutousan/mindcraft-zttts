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
  - WHY B2+ productive across the sixteen named languages by about age 35.

- PLAN $id=ai-agent-engineer
  - NOW AgentCore
  - NEXT AgentHarness ContextEngineering AgentHook MultiAgent AgentPlugin AgentToolkit LambdaMicroVM AgentLoop MCP AgenticEngineering InterviewPrep
  - DONE
  - ADJUST 2026-09-06 psyche DUMP: pull hooks + subagents forward on NEXT and goals.north. AgentCore PROBE stays NOW / open ANSWER. ClaudeCode STUDY stays. Fog/rest: do not pile DAY; empty PROBE stays empty until asked. Repo still has no hook store and no plugin package — that is GAP not invented install.
  - ADJUST 2026-09-06 mianling AI Agent 155-theme bank https://www.mianlingai.com/topics/ai-agent-interview-questions-2026/ bottom-up onto AgentHarness ContextEngineering. Strategy pedagogy/_learn/interview-prep-strategy.toon.md. Cron interview-bank-enrich. Do not paste answers. Do not invent ANSWER.
  - WHY Job seeking as AI agent engineer. North now includes AgentHook MultiAgent AgentPlugin (Cursor/Claude harness). Lebenslauf Full-Stack Frontend plus attested Bedrock MCP AWS certs Kiro Claude Code. AgentCore is not a job line.

- PLAN $id=seo-geo-sidework
  - NOW SEO
  - NEXT GenerativeEngineOptimization AnswerEngineOptimization Ecommerce
  - DONE
  - ADJUST 2026-09-06 human SEO/GEO demand + web research. Google Search Central: foundational SEO for AI Overviews; GEO paper arXiv 2311.09735. Empty PROBE until asked. Do not invent client traffic. Do not paste NAP.
  - WHY Side-site / 杂活 visibility literacy. Citation KPI ≠ sessions. Mirror .cursor/skills/dev-sidework. Not hire NOW (AgentCore stays focus).

- STUDY $id=AgentHarness
  - WHY 2026 hire bank disaster zone: harness vs prompt vs context. Runtime shell. Empty GAP. Do not invent ANSWER. Do not pile DAY on fog.
  - STORE PATH pedagogy/computation/AgentHarness.fu.md
  - RECALL
  - GAP

- STUDY $id=ContextEngineering
  - WHY Window craft: compress unload pollution. Separated from PromptEngineering in 2026 banks. Empty GAP. Do not invent ANSWER. Do not pile DAY on fog.
  - STORE PATH pedagogy/computation/ContextEngineering.fu.md
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
  - RECALL
  - GAP

- STUDY $id=AgentLoop
  - WHY inner heartbeat versus outer slash-loop. Source skills/loop-slash/PUBLISH.md.
  - STORE PATH pedagogy/computation/AgentLoop.fu.md
  - RECALL
  - GAP

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
