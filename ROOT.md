- LANG fu
  - FILE .fu.md
  - FORM nested unordered lists. First token after "- " is a TAG in CAPITAL_SNAKE or CAPITAL.
  - NO hash headings in .fu.md. No markdown tables. No domain nouns as TAG.
  - TAG is control for the runtime. Payload after the TAG is arguments. Nested list is scope.
  - READ ROOT.md then CPU.md then pedagogy/pedagogy-cpu.fu.md. Spawn AGENT in CPU.md this tick. Spawn STUDY PROBE from pedagogy-cpu.fu.md when the human is studying. Library .fu.md under self/ skills/ cron/ do not auto-spawn unless CPU.md or pedagogy-cpu.fu.md names them or SCHEDULE is due.

- FILE CPU.md
  - KIND explicit run queue
  - MEANING tasks the human currently wants executed. Not archive. Not library.
  - Runtime spawns every root AGENT in CPU.md in document order unless BLOCKER or $when fails.
  - SCHEDULE in CPU.md arms future ticks. TODO in CPU.md is backlog, not a spawn.
  - After DONE, move the node out of CPU.md into the owning .fu.md or .private.

- FILE *.graph.md
  - KIND gremlin-lite knowledge graph. Human readable. Machine traversable.
  - LINE V id then key=value props. Vertex. Required: kind gloss. Optional: body=path to the essay file.
  - LINE E from LABEL to then key=value. Directed edge.
  - LABEL vocabulary: ISA PARTICIPATES INFORMS RECEIVES STUDIES GROUNDS_IN APPLIES ENACTS MEDIATES TRANSMITS CONTRADICTS
  - Prop SOURCE=url-or-path on every edge added by cron. Seed edges may omit SOURCE.
  - BODY files hold CLAIM MEDIA SOURCE. MEDIA is URL only. No image or video bytes in vertex bodies. Showcase deliverable is tmp/pedagogy/universe.png universe.stack.png universe.html universe.mp4. ttl.toon.md stamps last_run.
  - Canonical store: pedagogy/universe.graph.md

- DIR pedagogy
  - KIND philosophical ontology. Essence of what is, not a CV. Universal tree of what is known here.
  - SCHEMA pedagogy/ontology.fu.md
  - GRAPH pedagogy/universe.graph.md
  - INTERFACE pedagogy/pedagogy-cpu.fu.md
  - MEANING pedagogy-cpu is the study surface. GOALS in self/goals.toon.md. PROBE first. ANSWER. ASSESS onto the graph. PLAN adjusts. REVIEW TRAVERSE SHOWCASE. Life queue stays CPU.md.
  - FOLDERS being math physics biology computation language are human-readable branches. Each vertex with claims has pedagogy/<branch>/<id>.fu.md. On Windows the root vertex file is also the folder index. The graph is the truth.

- DIR cron
  - KIND scheduled gatherers. Nest RECURRING AGENT.
  - Enrich ontology from RESEARCH DUMP LEARNING_DUMP. Additive. Cite SOURCE. Default $output=pedagogy/universe.graph.md
  - LEARN-ENRICH cron/learn-enrich.fu.md reads self/goals.toon.md, picks NORTH from the focused goal, writes pedagogy/_learn/lesson.toon.md, probes on pedagogy-cpu, assesses into self/learn.toon.md and E Study STUDIES. Study GUI is ephemeral. On SATISFY write mezzanine/learn-enrich.toon.md.
  - INTERVIEW-ANCHOR cron/interview-anchor.fu.md fetches AI-engineering interview titles, maps them onto graph vertices, writes a dated DAY slice on pedagogy-cpu, and logs intellectual load in self/endurance.toon.md. Titles and SOURCE urls only. Do not copy answers. Sore stops the day.
  - INFLOW-NEWS cron/inflow-news.fu.md gathers news, ideas, tech, and unknown unknowns into inflow/DUMP.md while the human is away. Skip ids in inflow/STATE.md. Not latex. Not pdf. Drip on return: cron/dump-drip.fu.md.
  - SCHEDULE-HARVEST cron/schedule-harvest.fu.md reads CPU.md inflow/ dumps, then the agent fills WHAT WHERE WHEN WHY from the open web into schedule/enrich.toon.md. Python merges that overlay. Slug titles are not a finished store. ICS only when the human asks python cron/schedule-harvest.py --ics.
  - JANITOR cron/janitor.fu.md moves non-markdown files to recycle/. Markdown stays. Bytecode caches (__pycache__, *.pyc) are deleted, not recycled. Restore recycled files by moving back. tmp/ is not recycle: python cron/janitor.py --ttl deletes tmp siblings when tmp/ttl.toon.md last_run is 5 days old. Keep ttl.toon.md.

- DIR inflow
  - KIND inbound news the human can read. Not the life queue. Not the ontology.
  - STORE PATH inflow/inflow.fu.md
  - STATE inflow/STATE.md is the skip list. Later ticks must not repeat those ids.
  - MEANING each NEWS row needs a URL and a WHY that touches an open goal or a dated calendar row. LEARN points at study vertices. DUMP.md is the away-loop buffer. Drip via cron/dump-drip.fu.md when the human is back. PII never stays in DUMP.md.

- DIR schedule
  - KIND calendar store. Harvested SCHEDULE rows. Not the life queue. CPU.md still arms ticks.
  - STORE PATH schedule/harvest.toon.md
  - ENRICH schedule/enrich.toon.md is the sourced WHAT WHERE WHEN WHY overlay. Do not invent times. Cite url.
  - MONTH files schedule/<year>-<month>.fu.md nest WHAT WHERE WHEN WHY under each SCHEDULE.
  - ICS schedule/calendar.ics only after the human asks. TZ Europe/Berlin.

- DIR .private
  - KIND gitignored life notes. Pinpointable particulars: bag lists, Ausweis, Melde, personal phone, Amt file numbers, what a clerk said.
  - MEANING CPU.md may name a public office and a clock. Ontology stays universal. self/identity and lebenslauf are also gitignored. Do not paste those facts into inflow/ or pedagogy/.

- DIR recycle
  - KIND bin for non-markdown swept by janitor. Not delete. JOURNAL.md is markdown so it stays.

- DIR skills
  - KIND agent libraries. Visualization and other tools. Spawn only when CPU.md or pedagogy-cpu.fu.md names them.
  - SHOWCASE skills/ontology-showcase.fu.md renders core PNG, stack-family PNG, and pan-zoom HTML into tmp/pedagogy/. ASK image or video on deliver. Stamp tmp/ttl.toon.md. Intermediates may die after the delivered file exists.
  - VIDEO kit is skills/loop-slash/. Masters render only into tmp/loop-slash/. No videos/ folder.

- DIR tmp
  - KIND on-demand human deliverables. Video, image, html. Not the store.
  - STORE PATH tmp/ttl.toon.md
  - MEANING ttl.toon.md is the only persistent file in this folder. last_run is when a deliverable was written. On ingest python cron/janitor.py --ttl. If last_run is 5 days old, delete every sibling. Keep ttl.toon.md.
  - VIDEO masters render into tmp/loop-slash/. Kit stays in skills/loop-slash/.
  - PEDAGOGY graph stays in pedagogy/. Showcase GUI and PNG/mp4 render into tmp/pedagogy/.

- TAG AGENT
  - KIND declaration. Runtime creates a real agent process. Not a comment. Not a label.
  - FORM AGENT $id=... $prompt=... $input=... $output=... $when=... $lang=...
  - $id required unique in file
  - $prompt required. Natural language job. May say "read STORE".
  - $input path the agent may read. Default STORE PATH of nearest ancestor.
  - $output path the agent may write. Default $input.
  - $when optional. Skip spawn until true. Examples: after $id, SCHEDULE datetime, STORE key false.
  - $lang optional. Default: user current language.
  - NEST under TODO or SCHEDULE to bind trigger. Bare AGENT at root of CPU.md starts on ingest.

- TAG STORE
  - KIND path bind. Local persistence the agent may read/write.
  - FORM STORE PATH relative/path.toon.md or relative/path.graph.md
  - STATE is alias of STORE for read-mostly snapshots.
  - CONTEXT STORE PATH same as STORE PATH. Desktop may show this.

- TAG TODO
  - KIND work node. Open until DONE.
  - FORM TODO text
  - MAY nest AGENT, BLOCKER, STORE, RESEARCH.

- TAG DONE
  - KIND close a TODO. Runtime must not spawn nested AGENT again.

- TAG SCHEDULE
  - KIND time trigger. FORM SCHEDULE ISO-date or ISO-range then payload.
  - MAY nest AGENT. Runtime arms the agent at that time.

- TAG RECURRING
  - KIND cron-like. Nest AGENT. Payload is interval text until a real cron field exists.

- TAG BLOCKER
  - KIND halt. Nested AGENT must not run while BLOCKER holds.
  - Payload is a predicate: STORE key, symptom, missing input.

- TAG RESEARCH
  - KIND ingest URL or question. MAY nest AGENT $output=mezzanine or PDF.

- TAG DUMP
  - KIND capture blob. Not executable. MAY nest AGENT to process later.

- TAG LEARNING_DUMP
  - KIND queued media ingest. Same as DUMP plus QUEUED.

- TAG PROFILE
  - KIND identity pointer. Payload is a role name. Nest STORE for that role.

- TAG OUTPUT
  - KIND artifact type for a parent AGENT: PDF, mp4, toon, graph, puml, PATH.

- NOT_TAG
  - Domain facts are not TAG. Write them in STORE toon or GRAPH, not as ATHLETE FLAG LAST NEXT.
  - Examples forbidden as TAG: ATHLETE, FLAG, LAST, NEXT, REPLY, TRUTH, SKILL, RULES, Bankdrücken, CLASS, VERTEX as fu TAG.
  - VERTEX and EDGE live only inside *.graph.md and pedagogy/ontology.fu.md payload.

- KV optional on any node for desktop observability
  - EXECUTION NUMBER /ulid
  - EXECUTED ON /datetime
  - CONTEXT STORE PATH /path
