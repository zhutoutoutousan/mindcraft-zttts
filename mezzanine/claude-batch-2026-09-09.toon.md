schema: mezzanine/claude-batch
as_of: 2026-09-09T00:32:00Z
source: https://code.claude.com/docs/en/commands
source: https://code.claude.com/docs/en/agents
note: Ingest. HUMAN OPEN claude-batch advanced to researched. Do not invent a local /batch experiment. Empty PROBE stays empty.
official:
  kind: bundled skill (prompt-orchestrated), not a fixed built-in command
  split: 5 to 30 independent units after a plan the human approves
  spawn: one background subagent per unit in an isolated git worktree
  each: implement, run tests, open a pull request
  requires: git repository
  example: /batch migrate src/ from Solid to React
nested:
  vs_cursor_loop: this repo /loop 20m is organ rotation while asleep; /batch is Claude Code MultiAgent+worktree parallelism
  vs_compact: /compact summarizes context; /batch fans out work
  analog: Nested Learning levels (fast subagent vs slow plan) — not an install of Hope
graph: pedagogy/computation/MultiAgent.fu.md
graph: pedagogy/language/SlashCommand.fu.md
