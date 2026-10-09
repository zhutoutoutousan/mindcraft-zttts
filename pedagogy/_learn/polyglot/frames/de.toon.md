schema: learn/grammar-frames
lang: de
updated: 2026-09-18
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
  id: auch_am_selben_tag
  gloss: additive-same-day
  pattern: NP + ist + am selben Tag + ebenfalls + Partizip II
  slots[2]: NP_nom, PARTIZIP_II
  fillers[2]: die-linke-Skapula, abgeklungen
  anti: 也同期 as one Chinese compound in DE; auch ohne Zeitangabe
  concept: recovered-same-day-too
  from_session: 2026-09-08-scapula-auch-zeitgleich

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

frame:
  id: um_zu_infinitiv
  gloss: purpose-um-zu
  pattern: um + es / NP + zu + Inf
  slots[2]: PRON_or_NP, V_inf
  fillers[2]: es, testen
  anti: es zu testen as afterthought without um; english "to test it" calque without um
  concept: in-order-to-test-it
  from_session: 2026-09-08-archify-diagram-test

frame:
  id: korrektur_nicht_korrigierung
  gloss: correction-noun
  pattern: die Korrektur (f)
  slots[1]: NP_nom_f
  fillers[1]: die-Korrektur
  anti: Korrigierung; nacktes augenblick as time adverb
  concept: a-correction
  from_session: 2026-09-08-korrektur-hook

frame:
  id: zu_Dat_kenntnisstand
  gloss: matching-existing-level
  pattern: zu + Dat (gemäß Niveau / Stand)
  slots[1]: NP_dat
  fillers[3]: meinem-Kenntnisstand, meinen-Deutschkenntnissen, diesem-Stand
  anti: nach + Nom for according-to; Grasp as EN island; Deutsch sprache as two tokens
  concept: matching-existing-grasp
  from_session: 2026-09-08-uebungen-kenntnisstand

frame:
  id: lokale_Speicherung_zur_Aktualisierung
  gloss: local-storage-for-updates
  pattern: mit + Adj + Speicherung + zur + N_f
  slots[2]: ADJ, NP_dat_f
  fillers[2]: lokaler, Aktualisierung
  anti: Lokal Speicherung; zu Aktualisierung without der/zur
  concept: persist-progress-locally
  from_session: 2026-09-08-html-drills-localstorage

frame:
  id: darunterliegende_Faehigkeiten
  gloss: underlying-skills-on-tree
  pattern: die darunterliegenden Fähigkeiten
  slots[1]: NP_acc_pl
  fillers[1]: die-darunterliegenden-Fähigkeiten
  anti: unterliegene; unterliegene Skills as EN calque without darunter
  concept: underlying-skills
  from_session: 2026-09-08-skilltree-facets

frame:
  id: dieses_Video_zum_Inflow
  gloss: add-this-video-to-inflow
  pattern: dieses + N_n + zum + N_m
  slots[2]: NP_acc_n, NP_dat_m
  fillers[2]: dieses-Video, zum-Inflow
  anti: diese ohne Nomen; zur Inflow; Hilfsreich; Interviewsgespräch
  concept: add-named-url-to-inflow
  from_session: 2026-09-08-inflow-compact-bilibili

frame:
  id: immer_noch_danach
  gloss: still-no-update-after-that
  pattern: danach immer noch keine + N_f
  slots[1]: NP_nom_f
  fillers[1]: keine-Aktualisierung
  anti: IMMER NOCH nachdem without a finite clause; nachdem as 'after that'
  concept: still-no-update
  from_session: 2026-09-08-hook-json-parse

frame:
  id: Workout_Planung
  gloss: workout-plan-compound
  pattern: eine Workout-Planung
  slots[1]: NP_acc_f
  fillers[1]: eine-Workout-Planung
  anti: Plannung; Workout Plannung as two tokens
  concept: todays-workout-plan
  from_session: 2026-09-08-workout-planung-heute

frame:
  id: Ich_logge
  gloss: verb-second-ich-logge
  pattern: Ich logge noch + Clause
  slots[1]: CLAUSE
  fillers[1]: Brain-Fog-ist-noch-da
  anti: Loggen ich; English log as first word
  concept: I-am-logging
  from_session: 2026-09-08-fog-mundgeschwuer-log

frame:
  id: andere_Koerperteile
  gloss: other-body-parts-acc-pl
  pattern: andere + N_pl (Akk)
  slots[1]: NP_acc_pl
  fillers[1]: andere-Körperteile
  anti: anderes Körperteilen; anderes + Dat
  concept: train-other-parts
  from_session: 2026-09-08-andere-koerperteile

frame:
  id: eine_Zusammenfassung_Akk
  gloss: feminine-accusative-indefinite
  pattern: eine + N_f (Akk)
  slots[1]: NP_acc_f
  fillers[1]: eine-Zusammenfassung
  anti: ein Zusammenfassung; ein + fem noun
  concept: give-me-a-summary
  from_session: 2026-09-09-zusammenfassung-tag-starten

frame:
  id: in_Akk_private
  gloss: put-into-private-folder
  pattern: Nimm das in + Akk (Ordner)
  slots[1]: NP_acc_folder
  fillers[1]: .private
  anti: in + Dat when motion into; 里边 without in+Akk
  concept: store-in-private
  from_session: 2026-09-10-in-private-aufnehmen

frame:
  id: wieder_vs_immer_noch
  gloss: recurrence-versus-residual
  pattern: wieder + Perfekt vs immer noch + NP
  slots[2]: V_perf, NP_problem
  fillers[2]: wieder-angefangen-zu-schmerzen, immer-noch-ein-Problem
  anti: immer noch angefangen (mixes residual with onset)
  concept: pain-came-back
  from_session: 2026-09-15-scapula-wieder-angefangen

frame:
  id: zum_Dat_neut
  gloss: return-to-neuter-thing
  pattern: zu + Dat n → zum + N_n
  slots[1]: NP_dat_n
  fillers[1]: Kenntnisdiagramm
  anti: zur + masc/neut; English Diagram; Kentnisse
  concept: go-back-to-diagram
  from_session: 2026-09-15-zum-kenntnisdiagramm

frame:
  id: anhand_Gen_system
  gloss: using-the-existing-system
  pattern: anhand + Gen (meines vorhandenen Systems)
  slots[1]: NP_gen_n
  fillers[1]: meines-vorhandenen-Systems
  anti: anhand der meiner; vorhande without -en; den + plural Übungen
  concept: collect-from-existing-store
  from_session: 2026-09-15-franzoesische-uebungen-anhand

frame:
  id: orth_dass
  gloss: orthography-conjunction-dass
  pattern: Konjunktion dass — seit 1996 ss, nie ß
  slots[1]: KONJ
  fillers[1]: dass
  anti: daß (alte Schreibung; Rückfall 2026-09-12, Rückfälle 2026-09-18 ×2 — zweimal am selben Tag, Drill dreimal offen); Missverständnis 2026-09-18: ß nach langem Vokal sei optional — nein, Pflicht in DE/AT (*Strasse/*Fuss falsch); nur die Schweiz/Liechtenstein schreiben immer ss; vor 1996 stand ß auch nach kurzem Vokal am Wortende (daß, muß, Fluß), daher die Rückfälle
  concept: dass-spelling
  from_session: 2026-09-12-melde-mich-krank

frame:
  id: schwache_dekl_en
  gloss: weak-adjective-ending-en
  pattern: nach Artikel/Possessiv/Demonstrativ trägt das Adjektiv -en (Dat. Sg., Akk. Sg. m/f, alle Plural)
  slots[1]: ADJ_endung
  fillers[4]: privaten-Bereich, vielen-Insekten, weiteren-geschäftlichen-Gelegenheiten, wiederholenden-Übungen
  anti: zur private Bereich; so viel Insekten; weitere geschäftliche; sofortliche und wiederholende
  concept: adjective-agreement-after-determiner
  from_session: 2026-09-18-beziehungen-private-bereich

frame:
  id: zahl_adj_stark
  gloss: numeral-strong-adjective-no-s
  pattern: Zahlwort + Adj(-e stark) + N_pl ohne -s
  slots[1]: NP_nom_pl
  fillers[1]: zwei-neue-Schwerpunkte
  anti: zwei neues Schwerpunkts; -s am Nomen nach Zahlwort; Kontrast zu schwache_dekl_en: nach Artikel schwach -en, nach Zahlwort stark -e
  concept: two-new-focal-points
  from_session: 2026-09-18-microvm-tiefer-eintauchen

frame:
  id: laden_schmeissen
  gloss: run-the-shop
  pattern: Akk den Laden + schmeißen/schmiss/geschmissen
  slots[1]: NP_acc_m
  fillers[3]: den-Laden, den-Betrieb, das-Büro
  anti: den Laden werfen; der Laden schmeißen
  concept: run-a-business-colloquial
  from_session: 2026-09-24-umgang-vier-wendungen

frame:
  id: faust_tasche
  gloss: hide-anger
  pattern: eine Faust in der Tasche machen
  slots[1]: V_machen
  fillers[1]: machte-die-Faust-in-der-Tasche
  anti: eine Faust in der Tasche haben; Faust in die Tasche (Akk)
  concept: swallow-protest
  from_session: 2026-09-24-umgang-vier-wendungen

frame:
  id: sich_in_rolle_sehen
  gloss: see-oneself-in-a-role
  pattern: sich + in + Dat Rolle + sehen
  slots[2]: REFL, NP_dat_f
  fillers[1]: sich-in-der-Rolle-einer-Firmenchefin-sehen
  anti: sich eine Rolle sehen; in die Rolle sehen (ohne sich)
  concept: picture-oneself-as
  from_session: 2026-09-24-umgang-vier-wendungen

frame:
  id: im_nacken_sitzen
  gloss: someone-on-your-back
  pattern: jemanden im Nacken sitzen haben
  slots[1]: NP_acc
  fillers[3]: ihn, den-Vater, niemanden
  anti: jemand im Nacken sitzen; im Nacken sitzen wollen ohne haben
  concept: pressure-from-a-person
  from_session: 2026-09-24-umgang-vier-wendungen

frame:
  id: wenn_es_gibt
  gloss: wenn-clause-with-es-gibt
  pattern: Wenn es + PP + NP + gibt
  slots[2]: PP, NP_nom
  fillers[1]: Wenn-es-Unsicherheit-gibt
  anti: Wenn bei X gibt es; Wenn X gibt es
  concept: if-there-is-uncertainty
  from_session: 2026-10-09-proteingetraenke-becher

frame:
  id: im_oeffentlichen_bereich
  gloss: in-the-public-area-dative
  pattern: im + Adj + Bereich (Dat m.)
  slots[1]: NP_dat_m
  fillers[1]: im-öffentlichen-Bereich
  anti: ins öffentliche Bereich (Bereich is m., not n.)
  concept: in-the-public-area
  from_session: 2026-10-09-oeffentlicher-pr-bereich

frame:
  id: eine_Fehlerliste_Akk
  gloss: feminine-accusative-error-list
  pattern: eine + Fehlerliste (Akk. f.)
  slots[1]: NP_acc_f
  fillers[1]: eine-Fehlerliste
  anti: ein Fehlerlist; die Fehlerlist
  concept: an-error-list
  from_session: 2026-10-09-eine-fehlerliste

