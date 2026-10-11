---
name: goethe-b2-sprechen
description: >-
  Runs a Goethe-Zertifikat B2 Sprechen rehearsal in writing (Vortrag, two
  partner questions, discussion), scores the official examiner grid out of 100,
  and writes a German LaTeX decision PDF. Deduplicates new themes against
  used.toon.md. A later block repeats the previous model test and runs drills
  cut from that sitting's errors. Use when the human names Goethe B2, Sprechen,
  Modellsatz, Prüfungsvorbereitung, Beschluss, Wiederholung, Retake, or asks to
  prepare the speaking exam the same way with a new topic.
---

# Goethe-Zertifikat B2 Sprechen

Same exam each day. New themes. The human writes spoken German instead of speaking. Aussprache is scored only when the human states a band, and the PDF says there is no recording.

Do not invent a pass. Do not reuse a theme on the new card. Do not score the module before Teil 2 is written.

A retake is the exception: it repeats the previous model test on purpose and is not marked again in used.toon.md.

## Read first

On a later day, before the new card, run:

```
python .cursor/skills/goethe-b2-sprechen/scripts/due.py --date YYYY-MM-DD
```

If it prints a due item, do the new card first. A bit later in that sitting, run the drills, then the retake. If the human stops after the new card, leave the item open.

Then pick the new card:

```
python .cursor/skills/goethe-b2-sprechen/scripts/pick_topic.py
```

That prints two unused Teil-1 themes and one unused Teil-2 question. Offer those. Then mark them immediately, including the Teil-1 theme the human does not choose:

```
python .cursor/skills/goethe-b2-sprechen/scripts/pick_topic.py --mark --date YYYY-MM-DD --teil1 ID --teil1 ID --teil2 ID
```

`--mark` exits with an error if an id or a normalized title is already in [used.toon.md](used.toon.md). If the pool is empty, say so. Do not invent a repeat and do not paraphrase a used title into a "new" one.

Pool: [topics.toon.md](topics.toon.md). Log: [used.toon.md](used.toon.md).

## Session

1. Teil 1. The human picks one of the two themes. Vortrag in spoken sentences: Einleitung, Hauptteil, Schluss. Several alternatives, pros and cons with a judgment, one alternative in more detail. About four minutes of speech, written out.
2. Two partner questions on what they actually said. They answer.
3. Teil 2. State one partner position in a sentence before they write. They write their position, a reaction to that sentence, and a last line that is clearly dafür or dagegen.
4. Score only now. Then the PDF.

Channel: Sie in the seminar and the discussion. English and other languages stay out of the exam text.

## Points

One examiner. Pass is 60 of 100. Bands are only A B C D E. No in-between scores. Round the raw total from 0,5 up.

Teil 1, max 44:

| Criterion | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| Erfüllung | 8 | 6 | 4 | 2 | 0 |
| Kohärenz | 8 | 6 | 4 | 2 | 0 |
| Wortschatz | 8 | 6 | 4 | 2 | 0 |
| Strukturen | 8 | 6 | 4 | 2 | 0 |
| Fragen und Antworten | 12 | 9 | 6 | 3 | 0 |

Teil 2, max 40:

| Criterion | A | B | C | D | E |
| --- | --- | --- | --- | --- | --- |
| Erfüllung | 10 | 7,5 | 5 | 2,5 | 0 |
| Interaktion | 10 | 7,5 | 5 | 2,5 | 0 |
| Wortschatz | 10 | 7,5 | 5 | 2,5 | 0 |
| Strukturen | 10 | 7,5 | 5 | 2,5 | 0 |

Aussprache, once for both parts: 16 / 12 / 8 / 4 / 0. Leave it open unless the human names a band. C is just under B2. D is clearly under. No reaction to the partner sentence is Interaktion D.

## PDF

Copy [template.tex](template.tex) to `tmp/goethe-b2-sprechen-YYYY-MM-DD.tex`. If that file exists, use `-2`. Fill every section, in this order:

1. Beschluss: bestanden or nicht bestanden, raw total, rounded total, line at 60
2. Vorgang of this sitting
3. For Teil 1, each partner question, and Teil 2: Frage, Antwort verbatim, Vorgang, korrigierte Antwort
4. Analyse
5. Empfehlungen, at most five, about the next sitting
6. Rubrik table
7. Fehlerliste: every error in that sitting's exam text, numbered T1 / P1 / P2 / T2. The same slip is listed every time it occurs. Name two sentences that were already correct so they are not mistaken for omissions.
8. Modellantworten that hit the speech functions. They are the target, not a new opinion.

German body. Compile:

```
python .cursor/skills/daily-brief/scripts/compile.py tmp/goethe-b2-sprechen-YYYY-MM-DD.tex
```

LaTeX and PDF only in `tmp/`. No home address, no lesion sites, no private names.

The writing-accuracy ingest stays a separate rule. Do not copy one sitting's error list into this skill.

## Later block

New themes stay deduped. The previous sitting comes back one calendar day later, after the new card.

1. Drills in the due file. Each drill is one spoken sentence aimed at one error from that sitting. No new theme.
2. Retake of that sitting's Teil-1 theme and Teil-2 question. Same shape: Vortrag, two partner questions, discussion. The human writes without the corrected text or the model answer in front of them.
3. Score the retake on the same grid. PDF name: `tmp/goethe-b2-sprechen-YYYY-MM-DD-retake.tex`.
4. Close the item and open the next one, due the following day, from the new card's errors:

```
python .cursor/skills/goethe-b2-sprechen/scripts/due.py --close FROM_DATE --add --due NEXT_DATE --from NEW_DATE --teil1 ID --teil2 ID --drills PATH
```

First queued retake: [queue.toon.md](queue.toon.md), drills [drills/2026-10-03.toon.md](drills/2026-10-03.toon.md), due 2026-10-04. Theme of that retake: Finanzierung des Studiums, then Sollen Studierende ihre Professoren beurteilen?
