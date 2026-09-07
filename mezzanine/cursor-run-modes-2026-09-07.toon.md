schema: cursor/run-modes
kind: ingest (not CLAIM)
tz: Europe/Berlin
date: 2026-09-07
source: https://cursor.com/docs/agent/security/run-modes
source: https://cursor.com/docs/enterprise/model-and-integration-management#model-access-control
source: inflow HUMAN OPEN cursor-fetch-without-permission
note: Human take promoted out of tmp/pedagogy/inflow-takes so janitor TTL cannot eat it. Not STUDY ANSWER.

session:
  done: ""
  current: Reading run-modes with German and English dual text
  note: Auto-review required
  question: What does sandbox actually mean in Cursor. What is a classifier.
  bookmark: Auto-review classifier runs on a small Cursor-managed model. Today that is Claude 4.5 Haiku or GPT-5.4 Mini.
  relation: enterprise model-access-control can gray out Auto-review if those models are blocked.

promote:
  vertex: AgentRunMode
  dump: cursor-fetch-without-permission stays HUMAN OPEN / answered until human closes
  not: pedagogy-cpu ANSWER
