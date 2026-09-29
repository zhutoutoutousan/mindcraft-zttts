schema: self/recovery-cycle
updated: "2026-09-27"
note: Named spans for learning how long DOMS vs joint-like pain vs fog last in this log. Generic typical bands are literature class not a diagnosis. Fog is not an injury banner. Mucosa/acne particulars stay .private/; only coarse clocks here.

split[3]:
  injury: live flags in training.toon.md. Recovered named clears the Today Injury card.
  doms: muscle soreness after load. Changes exercise choice. Not skipHeavyPress unless the joint is also named.
  fog: sickness-behavior in endurance.toon.md. Skip lexicon. Not left-scapula.

typical[]{kind,region,peak,usualClear,source,note}:
  doms,general muscle,24-72h after novel or eccentric,usually 2-5d sometimes ~7d,Cheung 2003 Sports Med 33:145,generic class not this body
  uri,systemic,often peaks day 2-3,usually 7-10d; cough may linger weeks,StatPearls NBK532961; Heikkinen 2020 PMC7204877,generic class not this illness. Not a diagnosis. Not an organism.
  sore-throat,pharynx,often the earliest symptom,~40pct by day 3 and ~85pct by 1 week; usually within 2 weeks,NICE CKS sore-throat-acute; NICE NG84; CDC sore-throat,generic class not this throat.
  fever-class,systemic,early phase if present,often only a few days in adults when it is a cold,StatPearls NBK532961,no thermometer in this log. A named-gone day is this person's clock.
  headache-with-uri,head,early with malaise,tracks the illness,StatPearls NBK532961,no separate week. Do not invent migraine.
  lower-trapezius,scapular,no generic clear-day,named span only,Park 2020 PMC7115121 is a 4-week program not a clear date,do not invent a trapezius week. Lower fibers are trained more than stretched. Quality stays .private/.
  pain,joint-like after press,no generic day-count in this store,named span only,Cavaliere zero-pain-in-range,do not invent a typical scapula week
  fog,systemic,while the inflammatory signal is named,open until named clear,Dantzer Nat Rev Neurosci 2008,not DSB. Not a press flag.
  mucosa,oral,pain often days 1-3 of a bout,common minor aphthous ~7-14d then red-flag if longer,AphthousUlcer.fu.md 1-2 week clinician flag,generic class not this mouth. Particulars .private/
  cough,airway,no quality named,acute cough often days to ~2-3 weeks then clinician if persistent,named span only,generic class not this chest. Do not invent an organism
  gi,gut,no quality named,named span only,sickness-behavior anorexia class Hart 1988,generic class not this gut. Do not invent IBS or infection
  acne,skin,no generic day-count in this store,named span only,first log 2026-09-10,do not invent a typical acne week

episode[]{id,kind,region,onset,cleared,days,note}:
  2026-09-01-left-scapula,pain,left scapula,2026-09-01,2026-09-08,7,onset after bench 100x2. Named recovered 2026-09-08. Recurred before 2026-09-15. Quality never named sharp.
  2026-09-01-chest-doms,doms,chest,2026-09-01,2026-09-06,5,first log 2026-09-03 expected ~48h. Named recovered 2026-09-06.
  2026-09-01-forearm-doms,doms,forearm,2026-09-01,2026-09-06,5,first log 2026-09-03. Named recovered 2026-09-06.
  2026-09-01-lats-doms,doms,lats,2026-09-01,2026-09-08,7,first log 2026-09-03. Residual named 2026-09-06. All muscle DOMS recovered 2026-09-08.
  2026-09-06-core-doms,doms,core/ab,2026-09-06,2026-09-08,2,little ab DOMS named 2026-09-06. All named muscle DOMS recovered 2026-09-08.
  2026-09-13-gi,gi,gut,named 2026-09-13,2026-09-14,1,human 2026-09-14 named Magen-Darm-Beschwerden gänzlich weg. Particulars .private/.
  2026-09-03-mucosa,mucosa,oral,2026-09-03,2026-09-14,11,human 2026-09-14 named Aphthen gänzlich weg. Brush aversion from sores not named gone. Acid-supplement gate still needs that conjunct. Particulars .private/.
  2026-09-08-fog,fog,systemic,2026-09-06,2026-09-18,12,human 2026-09-18 named leide ich nicht mehr. Not DSB. Endurance log same date fog-cleared. No budget raise invented.

open[]{id,kind,region,onset,cleared,days,note}:
  2026-09-27-lower-trapezius,pain,lower trapezius,named 2026-09-27,open,0,constant sensation named. Not DOMS. Not a scapula side-swap. Quality stays .private/. Not quiet.
  2026-09-25-illness,illness,systemic,2026-09-25,partial 2026-09-27,2,human named a two-day illness. One class named gone 2026-09-27. Other named kinds not re-named gone. Not a diagnosis. Particulars .private/.
  2026-09-15-left-scapula,pain,left scapula,before 2026-09-15,open,unspecified,human 2026-09-15 named 左肩胛骨那边仍然开始疼了. Recurrence after 2026-09-08 recovered. Quality unspecified. Not quiet. Do not invent sharp vs dull or a cause.
  2026-09-11-tooth,dental,one tooth,named 2026-09-11,open,0,human named alveolar-bone resorption plus looseness. Not a diagnosis. Particulars .private/. Not the aphthous clock. Do not invent a Termin.
  2026-09-10-cough,cough,airway,2026-09-06..07,open,~3-4,not re-named 2026-09-11 (human named no other abnormal state except the tooth). Last named 2026-09-10 最近三四天. Not a diagnosis. Particulars .private/.
  2026-09-10-acne,acne,skin,2026-09-10,open,1,not re-named 2026-09-11. First named some acne 2026-09-10. No type invented. Not a resume cue for neem/oregano.

rule[4]:
  - Recovered named (pain or DOMS) must not keep Injury / blockers on Today.
  - nextHeavyBenchEarliest is a plan clock. Not a blocker after skipHeavyPressUntilClear is false.
  - Particular days here beat generic typical until a new named span.
  - Do not invent sets laps RIR or a fog clear date.
