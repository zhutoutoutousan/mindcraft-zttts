- STORE PATH self/training.toon.md
- PROFILE FITNESS

- BLOCKER STORE flags.leftScapulaPain or radiating left arm
  - skip heavy press, skip kip, skip wide pullup
  - radiating left arm: skip all press
  - remaining scapular pain: no 92.5. Light Cavaliere technique press only if quality is not sharp.

- BLOCKER STORE flags.skipHeavyPressUntilClear
  - 40 percent relief on 2026-09-02 is not quiet. No 92.5-95 until quiet.

- SCHEDULE 2026-09-02–06 unplanned deload microcycle. Walk and optional Cavaliere technique test on 2026-09-06 only if not sharp. Overlap Agentur 2026-09-03 and IFA/AWS 2026-09-04–05.

- SCHEDULE 2026-09-07 earliest heavy bench IF STORE flags.skipHeavyPressUntilClear is false
  - BLOCKER STORE flags.skipHeavyPressUntilClear

- AGENT $id=training-log $input=self/training.toon.md $output=self/training.toon.md $prompt=When the user pastes working sets as load x reps RIR, append log[] and rewrite session. Never drop a set. Reply in the user language.

- AGENT $id=training-check $input=self/training.toon.md $output=self/training.toon.md $prompt=Ask pain quality dull vs sharp for left scapula. Sharp: flags.leftScapulaPain true, skipHeavyPressUntilClear true, rewrite nextSession.condition. Quiet: may clear skip. Forty percent relief is not quiet. Do not prescribe through sharp or radiating pain.

- AGENT $id=training-plan $input=self/training.toon.md $output=self/training.toon.md $when=after training-check quiet $prompt=Write nextSession only. Warmup 40/60/75/85. Top 92.5-95kg x4-5. Backoff 85-90kg x5-6 x2. No 70 to 100 jump. No 1RM test. Use sessionEstimated1rmKg 110-115 not claimed 120.

- AGENT $id=training-periodize $input=self/training.toon.md $output=self/training.toon.md $prompt=This week through 2026-09-06 is the RP deload after the 2026-09-01 scapular stop. Next 4-week press mesocycle starts after quiet plus a pain-free technique press. From sessionEstimated1rmKg 110-115. Ignore Bankdruecken_Plan.xlsx 120kg percents. Hard training does not drop fatigue.

- AGENT $id=training-pull $input=self/training.toon.md $output=self/training.toon.md $prompt=If free pullups under 8 reps: max 3 free sets then assisted chin or lat pulldown 8-10 x2. Assist 40-45kg if fatigued. Face pulls 12-15 x2 only if pain-free. Rest 2.5-3min free, 2min machines.

- AGENT $id=training-list $input=self/training.toon.md $when=user says auflisten $prompt=Print compact tables of last session, weekUntil2026-09-06, and nextSession. No extra prose.
