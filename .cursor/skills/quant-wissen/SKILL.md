---
name: quant-wissen
description: >-
  Reads and updates the QuantTradingWissen self-improvement graph (MT5, risk,
  backtest discipline, agent harness). Use when the human asks to internalize
  quant/trading lessons, update the Kenntnisse-Graph, SRS for Deflated Sharpe /
  SameSymbolBeta, or map live cluster-next observations into pedagogy.
---

# Quant-Wissen (Harness + Graph)

## Paths

| Role | Path |
|------|------|
| Subgraph | `pedagogy/_learn/quant-mt5/quant-wissen.graph.md` |
| State | `pedagogy/_learn/quant-mt5/state.toon.md` |
| Universe V | `QuantTradingWissen` in `pedagogy/universe.graph.md` |
| Body | `pedagogy/computation/QuantTradingWissen.fu.md` |
| Live store | `D:/profitable-expert-advisor/frontline/cluster-next/reports/LIVE_LESSONS_*.md` |
| Hochschule | `pedagogy/_learn/quant-mt5/hochschule/kursplan.md` + `immatrikulation.toon.md` |

## Agent paradigm (do this)

1. **Job first** on `practiceBase` (MT5 / code).
2. **Acceptance:** sleeve claims only from Strategy Tester HTML/XML.
3. **Internalize:** new durable lesson → add/update V/E in `quant-wissen.graph.md` + one line in `state.toon.md` `nextActions` / `srsThisWeek`. If ontology-level, append V/E on `QuantTradingWissen` in `universe.graph.md`.
4. **Loop:** hypothesize → test → diagnose → decide → write ExperienceStore (not chat-only).
5. **SRS:** one concept/week, five sentences (see graph section).

## Do not

- Treat Python book ports as acceptance.
- Dump YouTube lists into the graph unless asked.
- Edit product trading code solely to log language/learning.
