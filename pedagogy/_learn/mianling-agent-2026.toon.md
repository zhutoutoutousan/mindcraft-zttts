schema: learn/interview-bank-themes
note: Theme map from public Agent interview banks. Titles/themes only. Do not paste model answers. Do not invent ANSWER. Companies in theme tags are zeitgeist labels from the bank page, not job offers.
as_of: 2026-09-06
tz: Europe/Berlin
primary.SOURCE: https://www.mianlingai.com/topics/ai-agent-interview-questions-2026/
secondary.SOURCE: https://github.com/amitshekhariitbhu/ai-engineering-interview-questions
count.note: Mianling page claims 155 Agent-focused items as of 2026-09. This file stores nine theme buckets mapped to ontology vertices — not 155 answer rows.

theme[]{id,label_zh,vertex,hire_heat,note}:
  arch,基础概念与架构模式,Agent AgentLoop AgenticEngineering,high,ReAct vs Plan-Execute; Agent vs Workflow
  harness,Agent Harness 与运行时工程,AgentHarness AgentCore CursorSkill AgentHook AgentPlugin,critical,2026 disaster zone per bank — design motive not brand memorization
  tools,工具调用 MCP 与 Skills,MCP CursorSkill AgentToolkit,critical,FC vs MCP vs Skill boundaries; progressive disclosure
  memory,记忆管理与上下文工程,ContextEngineering ExperienceStore RAG KVCache Memory,critical,compress/unload/pollution; long-horizon memory
  multi,多智能体协作与编排,MultiAgent AgentLoop,high,isolation; failure rollback; markdown task handoff risks
  safety,评估幻觉与安全兜底,AISafety Evaluation LLMOps,high,loop kill; HITL pause; injection; observability
  sysdesign,系统设计题,AgentHarness MultiAgent RAG AISafety,high,PR review agent; ops agent; knowledge agent — project storytelling required
  code,Agent 手撕代码,AgentLoop MCP ContextEngineering,medium,min ReAct; router; dead-loop detector — production in own words
  soft,软性与职业发展,InterviewPrep History AutobiographicalMemory,high,deep dive YOUR project; Skills you wrote; Plan vs Agent mode

angle.layers[4]:
  - external — cron zeitgeist + inflow NEWS on AgentHarness MCP MultiAgent
  - enterprise — theme hire_heat from banks; company tags as soft prior only
  - interviewer — algo vs app-eng vs platform; ask role before dumping CoT trivia
  - job-family — ai-agent-engineer north vs languages; never invent Gehalt

rule[6]:
  - Bottom-up: new bank themes → missing V/E with SOURCE URL only.
  - Top-down: InterviewPrep strategy steers PROBE/DAY; empty ANSWER stays empty.
  - Cron may re-fetch bank page metadata / theme list; never commit scraped answer essays.
  - Multi-turn dialogue = follow-up PROBE on weak grasp; not auto-filled cheat sheet.
  - Humanity/history: AutobiographicalMemory + History vertices; particulars stay .private/.
  - Dual bank: Amit Shekhar titles already in pedagogy/_learn/interview.toon.md; Mianling is second SOURCE for CN hire zeitgeist.
