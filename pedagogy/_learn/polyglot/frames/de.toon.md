schema: learn/grammar-frames
lang: de
updated: 2026-09-07
note: Frames own slots. Lemmas fill slots. oneFocus picks one Frame.

frame:
  id: auf_Dat_device
  gloss: location-on-device
  pattern: auf + Dat (device surface)
  slots[1]: NP_dat_m_or_n
  fillers[1]: meinem-Laptop
  anti: in + Acc/Nom for device location
  concept: device-location
  from_session: 2026-09-07

frame:
  id: det_Nom_masc
  gloss: masculine-nominative-with-article
  pattern: der + Adj + N_m
  slots[1]: NP_nom_m
  fillers[1]: der-aktuelle-Zustand
  anti: bare masc noun; aktualisiert when aktuell meant
  concept: current-state
  from_session: 2026-09-07

frame:
  id: det_Akk_neut
  gloss: neuter-accusative-demonstrative
  pattern: dieses + N_n
  slots[1]: NP_acc_n
  fillers[1]: dieses-Projekt
  anti: diese Projekt
  concept: this-project
  from_session: 2026-09-07

frame:
  id: lass_uns_Vinf
  gloss: hortative-lets
  pattern: lass uns (+ Adv) + particle-verb Inf
  slots[2]: ADV, V_particle_inf
  fillers[2]: tiefer, eintauchen
  anti: lassen wir tauchen; English word order on particles
  concept: lets-dive-deeper
  from_session: 2026-09-07

frame:
  id: fuer_purpose
  gloss: purpose-or-time-for
  pattern: für + time/project NP
  slots[1]: NP_purpose
  fillers[2]: für-heute, für-dieses-Projekt
  anti: nach for purpose; redundant für mich
  concept: for-today-or-project
  from_session: 2026-09-07

frame:
  id: Bitte_Imperativ
  gloss: polite-imperative
  pattern: Bitte + Imperativ-e (written)
  slots[1]: V_imp
  fillers[2]: mache, gib
  anti: chat mach; capital Gib mid-clause
  concept: polite-request
  from_session: 2026-09-07

frame:
  id: mein_erster_N_m
  gloss: possessive-adj-masc-nominative
  pattern: mein + -er + N_m (Nom)
  slots[1]: NP_nom_m
  fillers[1]: mein-erster-Test
  anti: mein Erste Test; bare Erste
  concept: my-first-test
  from_session: 2026-09-07-dashboard

frame:
  id: haette_gern_zuerst
  gloss: polite-wish-with-zu-infinitive
  pattern: Ich hätte gern zuerst + NP + zu-Inf
  slots[2]: NP_acc, V_zu_inf
  fillers[2]: mein-Dashboard, einzusehen
  anti: Ich hatte gern; augenblick as calque
  concept: would-like-to-view
  from_session: 2026-09-07-dashboard

frame:
  id: fuer_dieses_Projekt
  gloss: purpose-this-project
  pattern: für + dieses + Projekt
  slots[1]: NP_acc_n
  fillers[1]: für-dieses-Projekt
  anti: für diese projekt
  concept: for-this-project
  from_session: 2026-09-07-dashboard
  reinforces: det_Akk_neut
