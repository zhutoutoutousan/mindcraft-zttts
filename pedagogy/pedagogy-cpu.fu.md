- KIND study interface. Human brain to the ontology. Not the life queue.
- STORE PATH pedagogy/universe.graph.md
- STORE PATH pedagogy/ontology.fu.md
- STORE PATH skills/ontology-showcase.fu.md
- STORE PATH tmp/ttl.toon.md
- STORE PATH cron/learn-enrich.fu.md
- STORE PATH cron/interview-anchor.fu.md
- STORE PATH self/learn.toon.md
- STORE PATH self/goals.toon.md
- STORE PATH self/endurance.toon.md
- NOTE CPU.md is calendar and life AGENT. This file is internalization. Harmony: enrich writes V/E. Showcase reads the graph and does not invent vertices. Study GUI is tmp/pedagogy/learn-gui.html. lesson.toon.md self/goals.toon.md self/endurance.toon.md and this file are the store. Janitor keeps cron/*.py skills/*.py. Showcase HTML is tmp/pedagogy/universe.html. Janitor --ttl deletes tmp siblings after 5 days. Bytecode caches are trash.

- PROTOCOL
  - GOALS read self/goals.toon.md every tick. Age and language counts are particulars, not vertices. Do not invent the 16 language names. Do not add Chinese as native. PLAN $id must match goals.focus. NORTH comes from that goal's north field plus other active goals.
  - PROBE first. One open question on PLAN NOW. Do not lecture. Do not dump CLAIM. Wait.
  - ANSWER human nests text under the open PROBE, or replies in chat and the agent writes ANSWER. Empty ANSWER means wait. Never invent ANSWER.
  - ASSESS from ANSWER against expect in pedagogy/_learn/lesson.toon.md. python cron/learn-enrich.py --assess. Write grasp unknown|weak|partial|firm. Mirror onto E Study STUDIES and propagate a weaker grasp to neighbors.
  - PLAN if missing, create PLAN from self/goals.toon.md north. After ASSESS, move NOW NEXT DONE. If weak, stay and ask a follow-up PROBE. Do not mark STUDY DONE while GAP is empty.
  - GUI optional. python cron/learn-enrich.py --gui writes tmp/pedagogy/learn-gui.html, gather one ANSWER. Janitor --ttl expires it. Do not save html into pedagogy/_learn.
  - BASELINE 摸底. python cron/learn-enrich.py --baseline then --baseline-serve. Async gather in tmp/pedagogy/baseline.html. Four expression boxes en zh fr de. Speak in Chrome or Edge: each Speak button is voice-to-text in that language. Skip any language. Stop if sore. Not DAY LOAD. Empty skip. Never invent ANSWER. --ingest-baseline copies to pedagogy/_learn/baseline.toon.md. --apply-study uses English if present else first filled language for STUDY ANSWER. Expression samples stay in the answers file. Do not assess until asked. Do not add Chinese as native.
  - DAY python cron/interview-anchor.py --day. Exact DO list for that calendar date. LOAD is how many items before a SORE check. First unfinished DO is NOW. Human says finished (--done --id) or sore (--sore --text). After SORE, stop. Do not pile more.
  - ENDURANCE self/endurance.toon.md. Sore after intellectual work is a stop signal. Human named it DSB. Nature 2024 is mouse CA1, not a diagnosis. Do not write sore as GenomicInstability. External drills count. 德语助手 wordschatz is Wordschatz, one unit per session. DAY LOAD is remaining after planned daily external. python cron/interview-anchor.py --external --id de-assistant-wordschatz when that session is done.
  - SATISFY when the human says this loop worked. python cron/learn-enrich.py --satisfy writes mezzanine/learn-enrich.toon.md. Process changes go in cron/learn-enrich.fu.md or cron/interview-anchor.fu.md.

- DAY $date=2026-09-02
  - LOAD 3
  - EXTERNAL planned 1 Wordschatz 德语助手 daily. Remaining hire DAY would be 2 on a fresh --day. Today's 3 DO already written. Log the session --external --id de-assistant-wordschatz. Do not invent a word count.
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
  - NEXT DualSubtitle Pedagogy Study FuLanguage
  - DONE
  - ADJUST waiting. Do not invent the 16 names. Attested en C1 de B2+ es. Age 30 is in self/goals.toon.md not a vertex.
  - WHY B2+ in 16 languages. Names of the other 13 not given.

- PLAN $id=ai-agent-engineer
  - NOW AgentCore
  - NEXT AgentToolkit LambdaMicroVM AgentLoop MCP AgenticEngineering ClaudeCode
  - DONE
  - ADJUST waiting first ANSWER. Claude Code five-layer harness is on the graph. Not this PROBE.
  - WHY job seeking as AI agent engineer. Workshop 2026-09-04. Lebenslauf is Full-Stack Frontend plus attested Bedrock MCP AWS certs Kiro Claude Code. AgentCore is not a job line.

- STUDY $id=AgentCore
  - PHASE probe
  - WHY Job-seeking as AI agent engineer. AWS workshop 2026-09-04.
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
  - WHY BV1t9oZBDENp harness talk. Coordinator versus Ralph while-loop.
  - STORE PATH pedagogy/computation/MultiAgent.fu.md
  - RECALL
  - GAP
  - DRILL Why does the talk prefer MultiAgent over RalphLoop without a CONTRADICT edge?

- STUDY $id=NaturalLanguage
  - WHY attested SPRACHEN only. Wordschatz is the daily drill, not a new language name.
  - STORE PATH pedagogy/language/NaturalLanguage.fu.md
  - RECALL
  - GAP

- STUDY $id=Wordschatz
  - WHY daily 德语助手 lexicon drill. Counts as IntellectualLoad. Empty GAP. Do not invent a word count.
  - STORE PATH pedagogy/language/Wordschatz.fu.md
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

- REVIEW open STUDY whose ANSWER or GAP is empty. Empty means wait or not yet internalized. Do not mark DONE.

- ASK SHOWCASE image or video. Default image. Then AGENT ontology-showcase with matching $output.
- ASK TRAVERSE gremlin-lite. Compact. No essay.
- ASK LEARN answer the open PROBE in chat or under ANSWER. Agent runs --answer --text then --assess. Do not ask the human to open an html file in the repo.
- ASK BASELINE fill tmp/pedagogy/baseline.html or http://127.0.0.1:8765/ in Chrome or Edge. Four boxes: English, 中文, Français, Deutsch. Speak or type. Skip any language. Save. Then --ingest-baseline. Do not invent ANSWER.
- ASK DAY what to do today. python cron/interview-anchor.py --print. Finished: --done --id. Sore: --sore --text. Wordschatz session: --external --id de-assistant-wordschatz.

- AGENT $id=day-plan $input=pedagogy/pedagogy-cpu.fu.md $prompt=python cron/interview-anchor.py --day. Print today's DO in order. Stop. When the human finishes one, --done --id. When they say sore, --sore --text and stop the day. Do not invent ANSWER. Do not spawn janitor.

- AGENT $id=study-probe $input=pedagogy/pedagogy-cpu.fu.md $prompt=Read PROTOCOL. python cron/learn-enrich.py --probe. Ask that one question. Stop. When the human answers, python cron/learn-enrich.py --answer --text their words. Then react. Next PROBE or follow-up. Do not lecture first. Do not invent ANSWER. Do not store html. Do not spawn janitor.

- AGENT $id=learn-enrich $input=pedagogy/universe.graph.md $prompt=Read cron/learn-enrich.fu.md and self/goals.toon.md. python cron/learn-enrich.py --status. If ANSWER present, --assess. Else --probe. NORTH follows goals.focus. Do not spawn janitor.

- AGENT $id=ontology-showcase $input=pedagogy/universe.graph.md $prompt=Read skills/ontology-showcase.fu.md. ASK image or video if $output unset. python skills/ontology-showcase.py --mode image|video --deliver. Deliver into tmp/pedagogy/. python cron/janitor.py --touch. Delete tmp/_work/showcase after the delivered file exists.

- EXECUTED ON 2026-09-02
- AGENT $id=ontology-enrich
  - DONE Nature s41586-024-07220-7 TLR9 memory cascade into pedagogy/biology
  - DONE lebenslauf domains into math physics computation language. No Person vertex.
  - DONE Study FuLanguage ResistanceTraining as attested essences
  - DONE kvcached as KVCache. arXiv 2606.05608 as AgenticEngineering CONTRADICTS SoftwareEngineering. loop-slash as AgentLoop.
  - DONE lebenslauf stack leaves: JavaScript TypeScript AWS ECS EKS SQS React NextJS and 60 more under pedagogy/computation/stack/. Kafka not in skill toon.
  - DONE 2026-09-02 learn-enrich AgentCore AgentToolkit LambdaMicroVM. PROTOCOL is now PROBE then ANSWER then ASSESS then PLAN.
  - DONE 2026-09-02 Claude Code five-layer harness: AgentConstitution AgentHook AgentPlugin onto ClaudeCode CursorSkill MultiAgent MCP. Not NOW. DAY LOAD 3 unchanged.
  - OUTPUT PATH pedagogy/universe.graph.md
