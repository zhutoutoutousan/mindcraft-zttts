---
name: daily-brief
description: Builds a German daily rest/train/learn LaTeX PDF into tmp/day-YYYY-MM-DD.pdf with muscle-group tables, weight/strength analysis, ontology figures, and forgetting-curve tracking. Use when the human asks for 每日报告, Tagesbericht, daily briefing, daily PDF, 日报, Kraftanalyse, Muskelgruppen, DOMS-Tabelle, or a latex pdf of today's plan.
---

# Daily brief PDF

Write `tmp/day-YYYY-MM-DD.tex` from [template.tex](template.tex). Compile with:

```
python .cursor/skills/daily-brief/scripts/compile.py tmp/day-YYYY-MM-DD.tex
```

Body language is **German**. Keep Wordschatz app names as stored (德语助手 法语助手 西语助手). Do not invent ANSWER, sets, laps, RSVP, or a cleared joint.

This skill stays generic. Do not bake venues, streets, GPS, halls, employers, private counterparties, lesion sites, or today's itinerary into `SKILL.md` or `template.tex`. Read particulars from stores each run.

## Privacy

Never copy into the skill, the template, or the PDF:

- email, phone, join URL, calendar token
- street + number, GPS, entrance, hall/stand id, home address
- private counterparty names that live only in `.private/`
- lesion sites, counts, photos, or other pinpointable health detail

PDF may use a public event **title + clock** from tracked schedule when the human asked for a planner. Coarse place only (home, park, pool, fair, call). Named private calls: clock + title already in CPU/schedule; never the join link. Health: at most one line the human already said today, no sites.

## Read first

- `CPU.md` clocks and timezone
- current month file under `schedule/` — today plus the next two days
- `self/training.toon.md` bodyweight, flags, last sets, nextSession
- `self/learn.toon.md` grasp
- `pedagogy/pedagogy-cpu.fu.md` PLAN NOW and empty PROBE
- `self/goals.toon.md` north
- `.private/health.fu.md` — one-line status only, per Privacy
- `.private/fog-stack.fu.md` — if fog / sickness-behavior / appetite dip / executive brake is named today, put it in the PDF status (coarse: class + skip lexicon; no mg, no lesion sites)
- `.private/` calendar notes — clock + public title only

## Layout

Heading and `tabularx` must not share a paragraph.

- After every heading: `\par` then the table
- Tables use `\linewidth` not `\textwidth`
- Never wrap `tabularx` in `{footnotesize ...}` without `\par` before and after
- Copy column spec from the template. `\blocktable` is 3 columns. `\muscletable` is 5: Gruppe, DOMS, Kraft, Heute, Naechste
- Unreported muscle groups: DOMS = nicht gemeldet. Do not invent soreness
- Target 3 pages with figures. Required TikZ: (1) muscle map, (2) forgetting curve, (3) north ontology chain
- If page 4, cut DUMP prose, not the muscle table or figures
- Header TZ comes from CPU, not from this skill

## Pages

1. Today's named rest/train from stores. Clocks. Weight. Muscle table + map. Strength.
2. Next sessions and optional public-event planner if asked. Pedagogy methods table. Forgetting-curve figure.
3. Ontology status figure. LOAD 1. Stop if sore.

## Weight

Log `athlete.bodyweightKg` and `log[]` weigh-in before compiling. Delta vs previous logged kg only. No BMI without height. No fat-loss claim on a short swing.

## Strength

Unreported groups stay nicht gemeldet. A pain flag is not DOMS. Residual DOMS on a pulling group is not a pull day. Write next 1–3 sessions from the store. Do not invent completed. Do not invent a cleared joint.

## Pedagogy track

STUDY empty GAP is wait. PLAN NOW without ANSWER: the forgetting curve has not started for that vertex. Wordschatz: log only if `--external` exists; do not invent a word count. Name methods that exist: PROBE/ANSWER/ASSESS, Wordschatz, LanguageDrilling, DAY LOAD, 摸底, dump-drip. A paper is not a diagnosis.

## Learn

PLAN NOW stays the north vertex until an ANSWER exists. Empty GAP is wait. Do not pile a past DAY LOAD.
