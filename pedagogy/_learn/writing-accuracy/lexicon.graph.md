# writing-accuracy lexicon graph (lemma · form · chunk · sentence · usage)
# Separate from pedagogy/universe.graph.md. Not Person/Job. Additive from sessions.
# V kinds: lemma | form | chunk | sentence | usage | pattern | session
# E labels: ISA PARTICIPATES INFORMS RECEIVES STUDIES GROUNDS_IN APPLIES ENACTS MEDIATES TRANSMITS CONTRADICTS
# Extra local labels ok in this file: HAS_FORM USES IN_SENTENCE FIXES FROM_SESSION COLLOCATES

V Laptop kind=lemma gloss=portable-computer gender=m lang=de
V Zustand kind=lemma gloss=state-condition gender=m lang=de
V Projekt kind=lemma gloss=project gender=n lang=de
V Aenderung kind=lemma gloss=change-modification gender=f lang=de surface=Änderung
V Liste kind=lemma gloss=list gender=f lang=de
V eintauchen kind=lemma gloss=dive-into particle=ein lang=de
V aktuell kind=lemma gloss=current-present pos=adj lang=de
V aktualisiert kind=lemma gloss=updated-participle pos=adj lang=de
V dass kind=lemma gloss=subordinating-that orth=ss lang=de
V TODO kind=lemma gloss=task-marker lang=en register=borrowed

V Form_Laptop_Dat kind=form lemma=Laptop surface=meinem-Laptop case=dat
V Form_Zustand_Nom kind=form lemma=Zustand surface=der-aktuelle-Zustand case=nom
V Form_Projekt_Akk kind=form lemma=Projekt surface=dieses-Projekt case=acc
V Form_Aenderung_Pl kind=form lemma=Aenderung surface=Aenderungen number=pl
V Form_TODO_Liste kind=form lemma=TODO surface=eine-TODO-Liste support=Liste
V Form_eintauchen_Inf kind=form lemma=eintauchen surface=tiefer-eintauchen

V Chunk_auf_meinem_Laptop kind=chunk gloss=location-on-device
V Chunk_lass_uns_Inf kind=chunk gloss=hortative-lets
V Chunk_fuer_heute kind=chunk gloss=purpose-time-today
V Chunk_fuer_dieses_Projekt kind=chunk gloss=purpose-project
V Chunk_Bitte_Imperativ kind=chunk gloss=polite-imperative-frame

V Sent_2026-09-07_raw kind=sentence date=2026-09-07 role=raw
V Sent_2026-09-07_fix kind=sentence date=2026-09-07 role=corrected
V Session_2026-09-07 kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07.toon.md

V Usage_auf_vs_in_device kind=usage gloss=device-surface-takes-auf-not-in
V Usage_fuer_vs_nach_purpose kind=usage gloss=purpose-takes-fuer-not-nach
V Usage_aktuell_vs_aktualisiert kind=usage gloss=current-vs-updated
V Usage_lass_uns_particle kind=usage gloss=hortative-plus-particle-verb

V Pat_missing_det_masc_neut kind=pattern gloss=missing-determiners-on-masc-neut
V Pat_L1_particle_order kind=pattern gloss=EN-ZH-order-on-German-particles
V Pat_prep_transfer kind=pattern gloss=preposition-transfer
V Pat_chat_register kind=pattern gloss=chat-register-in-semi-formal-request

E Laptop HAS_FORM Form_Laptop_Dat
E Zustand HAS_FORM Form_Zustand_Nom
E Projekt HAS_FORM Form_Projekt_Akk
E Aenderung HAS_FORM Form_Aenderung_Pl
E TODO HAS_FORM Form_TODO_Liste
E eintauchen HAS_FORM Form_eintauchen_Inf
E aktuell COLLOCATES Zustand SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07.toon.md
E aktualisiert CONTRADICTS aktuell SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07.toon.md

E Chunk_auf_meinem_Laptop USES Form_Laptop_Dat
E Chunk_auf_meinem_Laptop APPLIES Usage_auf_vs_in_device
E Chunk_lass_uns_Inf USES Form_eintauchen_Inf
E Chunk_lass_uns_Inf APPLIES Usage_lass_uns_particle
E Chunk_fuer_heute APPLIES Usage_fuer_vs_nach_purpose
E Chunk_fuer_dieses_Projekt USES Form_Projekt_Akk
E Chunk_Bitte_Imperativ APPLIES Pat_chat_register

E Sent_2026-09-07_fix USES Chunk_auf_meinem_Laptop
E Sent_2026-09-07_fix USES Chunk_lass_uns_Inf
E Sent_2026-09-07_fix USES Chunk_fuer_heute
E Sent_2026-09-07_fix USES Chunk_fuer_dieses_Projekt
E Sent_2026-09-07_fix USES Chunk_Bitte_Imperativ
E Sent_2026-09-07_fix USES Form_Zustand_Nom
E Sent_2026-09-07_fix USES Form_TODO_Liste
E Sent_2026-09-07_fix USES Form_Aenderung_Pl
E Sent_2026-09-07_fix FIXES Sent_2026-09-07_raw
E Sent_2026-09-07_raw FROM_SESSION Session_2026-09-07
E Sent_2026-09-07_fix FROM_SESSION Session_2026-09-07

E Pat_missing_det_masc_neut IN_SENTENCE Sent_2026-09-07_raw
E Pat_L1_particle_order IN_SENTENCE Sent_2026-09-07_raw
E Pat_prep_transfer IN_SENTENCE Sent_2026-09-07_raw
E Pat_chat_register IN_SENTENCE Sent_2026-09-07_raw
E Usage_aktuell_vs_aktualisiert IN_SENTENCE Sent_2026-09-07_fix
E dass FROM_SESSION Session_2026-09-07

# --- session 2026-09-07-dashboard (erster Live-Test) ---
V Test kind=lemma gloss=trial-test gender=m lang=de
V Dashboard kind=lemma gloss=project-dashboard gender=n lang=de register=borrowed
V einsehen kind=lemma gloss=inspect-view particle=none lang=de
V haette_gern kind=lemma gloss=would-like pos=modal_wish lang=de surface=haette-gern

V Form_Test_Nom kind=form lemma=Test surface=mein-erster-Test case=nom
V Form_Dashboard_Akk kind=form lemma=Dashboard surface=mein-Dashboard case=acc
V Form_einsehen_Inf kind=form lemma=einsehen surface=einzusehen
V Form_haette_gern kind=form lemma=haette_gern surface=Ich-haette-gern

V Chunk_mein_erster_Test kind=chunk gloss=my-first-test-nom
V Chunk_Dashboard_einsehen kind=chunk gloss=view-dashboard-request
V Chunk_fuer_dieses_Projekt_dash kind=chunk gloss=for-this-project
V Chunk_haette_gern_zuerst kind=chunk gloss=polite-wish-first

V Sent_2026-09-07_dash_raw kind=sentence date=2026-09-07 role=raw
V Sent_2026-09-07_dash_fix kind=sentence date=2026-09-07 role=corrected
V Session_2026-09-07_dashboard kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-dashboard.toon.md

V Usage_erster_vs_Erste kind=usage gloss=adj-ending-masc-nom-mein-erster
V Usage_haette_gern_wish kind=usage gloss=Konjunktiv-II-wunsch-hatte-vs-haette
V Usage_augenblick_vs_kurz kind=usage gloss=kurz-or-auf-einen-Blick-not-augenblick-calque

E Test HAS_FORM Form_Test_Nom
E Dashboard HAS_FORM Form_Dashboard_Akk
E einsehen HAS_FORM Form_einsehen_Inf
E haette_gern HAS_FORM Form_haette_gern
E Projekt HAS_FORM Form_Projekt_Akk

E Chunk_mein_erster_Test USES Form_Test_Nom
E Chunk_mein_erster_Test APPLIES Usage_erster_vs_Erste
E Chunk_Dashboard_einsehen USES Form_Dashboard_Akk
E Chunk_Dashboard_einsehen USES Form_einsehen_Inf
E Chunk_fuer_dieses_Projekt_dash USES Form_Projekt_Akk
E Chunk_haette_gern_zuerst USES Form_haette_gern
E Chunk_haette_gern_zuerst APPLIES Usage_haette_gern_wish

E Sent_2026-09-07_dash_fix USES Chunk_mein_erster_Test
E Sent_2026-09-07_dash_fix USES Chunk_Dashboard_einsehen
E Sent_2026-09-07_dash_fix USES Chunk_fuer_dieses_Projekt_dash
E Sent_2026-09-07_dash_fix USES Chunk_haette_gern_zuerst
E Sent_2026-09-07_dash_fix FIXES Sent_2026-09-07_dash_raw
E Sent_2026-09-07_dash_raw FROM_SESSION Session_2026-09-07_dashboard
E Sent_2026-09-07_dash_fix FROM_SESSION Session_2026-09-07_dashboard
E Pat_missing_det_masc_neut IN_SENTENCE Sent_2026-09-07_dash_raw
E Usage_erster_vs_Erste IN_SENTENCE Sent_2026-09-07_dash_fix
E Usage_haette_gern_wish IN_SENTENCE Sent_2026-09-07_dash_fix
E Usage_augenblick_vs_kurz FROM_SESSION Session_2026-09-07_dashboard

# ingest-session 2026-09-07T12:17:58Z first-arbitrage-test-dashboard
V Session_first_arbitrage_test_dashboard kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-dashboard.toon.md
V Sent_first_arbitrage_test_dashboard_raw kind=sentence date=2026-09-07 role=raw
V Sent_first_arbitrage_test_dashboard_fix kind=sentence date=2026-09-07 role=corrected
E Sent_first_arbitrage_test_dashboard_fix FIXES Sent_first_arbitrage_test_dashboard_raw
E Sent_first_arbitrage_test_dashboard_raw FROM_SESSION Session_first_arbitrage_test_dashboard
E Sent_first_arbitrage_test_dashboard_fix FROM_SESSION Session_first_arbitrage_test_dashboard

# ingest-session 2026-09-07T12:17:58Z ensure-errors-internalized-hook
V Session_ensure_errors_internalized_hook kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-internalize-hook.toon.md
V Sent_ensure_errors_internalized_hook_raw kind=sentence date=2026-09-07 role=raw
V Sent_ensure_errors_internalized_hook_fix kind=sentence date=2026-09-07 role=corrected
E Sent_ensure_errors_internalized_hook_fix FIXES Sent_ensure_errors_internalized_hook_raw
E Sent_ensure_errors_internalized_hook_raw FROM_SESSION Session_ensure_errors_internalized_hook
E Sent_ensure_errors_internalized_hook_fix FROM_SESSION Session_ensure_errors_internalized_hook

# ingest-session 2026-09-07T12:21:32Z cafe-mask-how-it-works
V Session_cafe_mask_how_it_works kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-cafe-mask-how.toon.md
V Sent_cafe_mask_how_it_works_raw kind=sentence date=2026-09-07 role=raw
V Sent_cafe_mask_how_it_works_fix kind=sentence date=2026-09-07 role=corrected
E Sent_cafe_mask_how_it_works_fix FIXES Sent_cafe_mask_how_it_works_raw
E Sent_cafe_mask_how_it_works_raw FROM_SESSION Session_cafe_mask_how_it_works
E Sent_cafe_mask_how_it_works_fix FROM_SESSION Session_cafe_mask_how_it_works

# ingest-session 2026-09-07T12:29:12Z language-panel-menu
V Session_language_panel_menu kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-language-panel.toon.md
V Sent_language_panel_menu_raw kind=sentence date=2026-09-07 role=raw
V Sent_language_panel_menu_fix kind=sentence date=2026-09-07 role=corrected
E Sent_language_panel_menu_fix FIXES Sent_language_panel_menu_raw
E Sent_language_panel_menu_raw FROM_SESSION Session_language_panel_menu
E Sent_language_panel_menu_fix FROM_SESSION Session_language_panel_menu

# ingest-session 2026-09-07T12:30:15Z method-goal-fehlerfrei-aeussern
V Session_method_goal_fehlerfrei_aeussern kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-method-goal.toon.md
V Sent_method_goal_fehlerfrei_aeussern_raw kind=sentence date=2026-09-07 role=raw
V Sent_method_goal_fehlerfrei_aeussern_fix kind=sentence date=2026-09-07 role=corrected
E Sent_method_goal_fehlerfrei_aeussern_fix FIXES Sent_method_goal_fehlerfrei_aeussern_raw
E Sent_method_goal_fehlerfrei_aeussern_raw FROM_SESSION Session_method_goal_fehlerfrei_aeussern
E Sent_method_goal_fehlerfrei_aeussern_fix FROM_SESSION Session_method_goal_fehlerfrei_aeussern

# ingest-session 2026-09-07T12:32:01Z fr-probe-expliquer-ajouter-kg lang=fr
V Session_fr_probe_expliquer_ajouter_kg kind=session date=2026-09-07 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-fr-probe.toon.md
V Sent_fr_probe_expliquer_ajouter_kg_raw kind=sentence date=2026-09-07 lang=fr role=raw
V Sent_fr_probe_expliquer_ajouter_kg_fix kind=sentence date=2026-09-07 lang=fr role=corrected
E Sent_fr_probe_expliquer_ajouter_kg_fix FIXES Sent_fr_probe_expliquer_ajouter_kg_raw
E Sent_fr_probe_expliquer_ajouter_kg_raw FROM_SESSION Session_fr_probe_expliquer_ajouter_kg
E Sent_fr_probe_expliquer_ajouter_kg_fix FROM_SESSION Session_fr_probe_expliquer_ajouter_kg

# ingest-session 2026-09-07T14:25:21Z inflow-take-dsb-graph-persist lang=de
V Session_inflow_take_dsb_graph_persist kind=session date=2026-09-07 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-inflow-dsb-persist.toon.md
V Sent_inflow_take_dsb_graph_persist_raw kind=sentence date=2026-09-07 lang=de role=raw
V Sent_inflow_take_dsb_graph_persist_fix kind=sentence date=2026-09-07 lang=de role=corrected
E Sent_inflow_take_dsb_graph_persist_fix FIXES Sent_inflow_take_dsb_graph_persist_raw
E Sent_inflow_take_dsb_graph_persist_raw FROM_SESSION Session_inflow_take_dsb_graph_persist
E Sent_inflow_take_dsb_graph_persist_fix FROM_SESSION Session_inflow_take_dsb_graph_persist

# ingest-session 2026-09-07T14:30:25Z chat-correct-kg-tmp-promote lang=de
V Session_chat_correct_kg_tmp_promote kind=session date=2026-09-07 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-chat-kg-tmp-promote.toon.md
V Sent_chat_correct_kg_tmp_promote_raw kind=sentence date=2026-09-07 lang=de role=raw
V Sent_chat_correct_kg_tmp_promote_fix kind=sentence date=2026-09-07 lang=de role=corrected
E Sent_chat_correct_kg_tmp_promote_fix FIXES Sent_chat_correct_kg_tmp_promote_raw
E Sent_chat_correct_kg_tmp_promote_raw FROM_SESSION Session_chat_correct_kg_tmp_promote
E Sent_chat_correct_kg_tmp_promote_fix FROM_SESSION Session_chat_correct_kg_tmp_promote

# ingest-session 2026-09-08T14:38:27Z scapula-auch-zeitgleich lang=de
V Session_scapula_auch_zeitgleich kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-scapula-auch-zeitgleich.toon.md
V Sent_scapula_auch_zeitgleich_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_scapula_auch_zeitgleich_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_scapula_auch_zeitgleich_fix FIXES Sent_scapula_auch_zeitgleich_raw
E Sent_scapula_auch_zeitgleich_raw FROM_SESSION Session_scapula_auch_zeitgleich
E Sent_scapula_auch_zeitgleich_fix FROM_SESSION Session_scapula_auch_zeitgleich

# ingest-session 2026-09-08T14:49:41Z archify-diagram-test lang=de
V Session_archify_diagram_test kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-archify-diagram-test.toon.md
V Sent_archify_diagram_test_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_archify_diagram_test_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_archify_diagram_test_fix FIXES Sent_archify_diagram_test_raw
E Sent_archify_diagram_test_raw FROM_SESSION Session_archify_diagram_test
E Sent_archify_diagram_test_fix FROM_SESSION Session_archify_diagram_test

# ingest-session 2026-09-08T14:55:32Z korrektur-hook lang=de
V Session_korrektur_hook kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-korrektur-hook.toon.md
V Sent_korrektur_hook_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_korrektur_hook_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_korrektur_hook_fix FIXES Sent_korrektur_hook_raw
E Sent_korrektur_hook_raw FROM_SESSION Session_korrektur_hook
E Sent_korrektur_hook_fix FROM_SESSION Session_korrektur_hook

# ingest-session 2026-09-08T15:00:00Z uebungen-kenntnisstand lang=de
V Session_uebungen_kenntnisstand kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-uebungen-kenntnisstand.toon.md
V Sent_uebungen_kenntnisstand_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_uebungen_kenntnisstand_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_uebungen_kenntnisstand_fix FIXES Sent_uebungen_kenntnisstand_raw
E Sent_uebungen_kenntnisstand_raw FROM_SESSION Session_uebungen_kenntnisstand
E Sent_uebungen_kenntnisstand_fix FROM_SESSION Session_uebungen_kenntnisstand

# ingest-session 2026-09-08T15:04:33Z html-drills-localstorage lang=de
V Session_html_drills_localstorage kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-html-drills-localstorage.toon.md
V Sent_html_drills_localstorage_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_html_drills_localstorage_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_html_drills_localstorage_fix FIXES Sent_html_drills_localstorage_raw
E Sent_html_drills_localstorage_raw FROM_SESSION Session_html_drills_localstorage
E Sent_html_drills_localstorage_fix FROM_SESSION Session_html_drills_localstorage

# ingest-session 2026-09-08T15:11:11Z skilltree-facets lang=de
V Session_skilltree_facets kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-skilltree-facets.toon.md
V Sent_skilltree_facets_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_skilltree_facets_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_skilltree_facets_fix FIXES Sent_skilltree_facets_raw
E Sent_skilltree_facets_raw FROM_SESSION Session_skilltree_facets
E Sent_skilltree_facets_fix FROM_SESSION Session_skilltree_facets

# ingest-session 2026-09-08T15:20:24Z inflow-compact-bilibili lang=de
V Session_inflow_compact_bilibili kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-inflow-compact-bilibili.toon.md
V Sent_inflow_compact_bilibili_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_inflow_compact_bilibili_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_inflow_compact_bilibili_fix FIXES Sent_inflow_compact_bilibili_raw
E Sent_inflow_compact_bilibili_raw FROM_SESSION Session_inflow_compact_bilibili
E Sent_inflow_compact_bilibili_fix FROM_SESSION Session_inflow_compact_bilibili

# ingest-session 2026-09-08T15:29:09Z hook-json-parse lang=de
V Session_hook_json_parse kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-hook-json-parse.toon.md
V Sent_hook_json_parse_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_hook_json_parse_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_hook_json_parse_fix FIXES Sent_hook_json_parse_raw
E Sent_hook_json_parse_raw FROM_SESSION Session_hook_json_parse
E Sent_hook_json_parse_fix FROM_SESSION Session_hook_json_parse

# ingest-session 2026-09-08T15:31:39Z workout-planung-heute lang=de
V Session_workout_planung_heute kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-workout-planung-heute.toon.md
V Sent_workout_planung_heute_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_workout_planung_heute_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_workout_planung_heute_fix FIXES Sent_workout_planung_heute_raw
E Sent_workout_planung_heute_raw FROM_SESSION Session_workout_planung_heute
E Sent_workout_planung_heute_fix FROM_SESSION Session_workout_planung_heute

# ingest-session 2026-09-08T15:33:49Z fog-mundgeschwuer-log lang=de
V Session_fog_mundgeschwuer_log kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-fog-mundgeschwuer-log.toon.md
V Sent_fog_mundgeschwuer_log_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_fog_mundgeschwuer_log_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_fog_mundgeschwuer_log_fix FIXES Sent_fog_mundgeschwuer_log_raw
E Sent_fog_mundgeschwuer_log_raw FROM_SESSION Session_fog_mundgeschwuer_log
E Sent_fog_mundgeschwuer_log_fix FROM_SESSION Session_fog_mundgeschwuer_log

# ingest-session 2026-09-08T16:17:38Z andere-koerperteile lang=de
V Session_andere_koerperteile kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-andere-koerperteile.toon.md
V Sent_andere_koerperteile_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_andere_koerperteile_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_andere_koerperteile_fix FIXES Sent_andere_koerperteile_raw
E Sent_andere_koerperteile_raw FROM_SESSION Session_andere_koerperteile
E Sent_andere_koerperteile_fix FROM_SESSION Session_andere_koerperteile

# ingest-session 2026-09-08T16:36:12Z nahrungsergaenzung-routine lang=de
V Session_nahrungsergaenzung_routine kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-nahrungsergaenzung-routine.toon.md
V Sent_nahrungsergaenzung_routine_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_nahrungsergaenzung_routine_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_nahrungsergaenzung_routine_fix FIXES Sent_nahrungsergaenzung_routine_raw
E Sent_nahrungsergaenzung_routine_raw FROM_SESSION Session_nahrungsergaenzung_routine
E Sent_nahrungsergaenzung_routine_fix FROM_SESSION Session_nahrungsergaenzung_routine

# ingest-session 2026-09-08T16:42:10Z latexpdf-nahrung-workout lang=de
V Session_latexpdf_nahrung_workout kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-latexpdf-nahrung-workout.toon.md
V Sent_latexpdf_nahrung_workout_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_latexpdf_nahrung_workout_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_latexpdf_nahrung_workout_fix FIXES Sent_latexpdf_nahrung_workout_raw
E Sent_latexpdf_nahrung_workout_raw FROM_SESSION Session_latexpdf_nahrung_workout
E Sent_latexpdf_nahrung_workout_fix FROM_SESSION Session_latexpdf_nahrung_workout

# ingest-session 2026-09-08T16:55:08Z gym-ist-beintraining-schwimmen lang=de
V Session_gym_ist_beintraining_schwimmen kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-gym-ist-beintraining-schwimmen.toon.md
V Sent_gym_ist_beintraining_schwimmen_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_gym_ist_beintraining_schwimmen_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_gym_ist_beintraining_schwimmen_fix FIXES Sent_gym_ist_beintraining_schwimmen_raw
E Sent_gym_ist_beintraining_schwimmen_raw FROM_SESSION Session_gym_ist_beintraining_schwimmen
E Sent_gym_ist_beintraining_schwimmen_fix FROM_SESSION Session_gym_ist_beintraining_schwimmen

# ingest-session 2026-09-08T18:29:30Z korrektur-hook-datei lang=de
V Session_korrektur_hook_datei kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-korrektur-hook-datei.toon.md
V Sent_korrektur_hook_datei_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_korrektur_hook_datei_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_korrektur_hook_datei_fix FIXES Sent_korrektur_hook_datei_raw
E Sent_korrektur_hook_datei_raw FROM_SESSION Session_korrektur_hook_datei
E Sent_korrektur_hook_datei_fix FROM_SESSION Session_korrektur_hook_datei

# ingest-session 2026-09-08T19:24:30Z uebung-zum-sprachenlernen lang=de
V Session_uebung_zum_sprachenlernen kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-uebung-zum-sprachenlernen.toon.md
V Sent_uebung_zum_sprachenlernen_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_uebung_zum_sprachenlernen_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_uebung_zum_sprachenlernen_fix FIXES Sent_uebung_zum_sprachenlernen_raw
E Sent_uebung_zum_sprachenlernen_raw FROM_SESSION Session_uebung_zum_sprachenlernen
E Sent_uebung_zum_sprachenlernen_fix FROM_SESSION Session_uebung_zum_sprachenlernen

# ingest-session 2026-09-08T19:38:35Z rueckmeldung-drill-quality lang=de
V Session_rueckmeldung_drill_quality kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-rueckmeldung-drill-quality.toon.md
V Sent_rueckmeldung_drill_quality_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_rueckmeldung_drill_quality_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_rueckmeldung_drill_quality_fix FIXES Sent_rueckmeldung_drill_quality_raw
E Sent_rueckmeldung_drill_quality_raw FROM_SESSION Session_rueckmeldung_drill_quality
E Sent_rueckmeldung_drill_quality_fix FROM_SESSION Session_rueckmeldung_drill_quality

# ingest-session 2026-09-08T19:41:02Z html-datei-ab-jetzt lang=de
V Session_html_datei_ab_jetzt kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-html-datei-ab-jetzt.toon.md
V Sent_html_datei_ab_jetzt_raw kind=sentence date=2026-09-08 lang=de role=raw
V Sent_html_datei_ab_jetzt_fix kind=sentence date=2026-09-08 lang=de role=corrected
E Sent_html_datei_ab_jetzt_fix FIXES Sent_html_datei_ab_jetzt_raw
E Sent_html_datei_ab_jetzt_raw FROM_SESSION Session_html_datei_ab_jetzt
E Sent_html_datei_ab_jetzt_fix FROM_SESSION Session_html_datei_ab_jetzt

# ingest-session 2026-09-09T09:38:21Z zusammenfassung-tag-starten lang=de
V Session_zusammenfassung_tag_starten kind=session date=2026-09-09 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-09-zusammenfassung-tag-starten.toon.md
V Sent_zusammenfassung_tag_starten_raw kind=sentence date=2026-09-09 lang=de role=raw
V Sent_zusammenfassung_tag_starten_fix kind=sentence date=2026-09-09 lang=de role=corrected
E Sent_zusammenfassung_tag_starten_fix FIXES Sent_zusammenfassung_tag_starten_raw
E Sent_zusammenfassung_tag_starten_raw FROM_SESSION Session_zusammenfassung_tag_starten
E Sent_zusammenfassung_tag_starten_fix FROM_SESSION Session_zusammenfassung_tag_starten

# ingest-session 2026-09-10T13:38:54Z in-private-aufnehmen lang=de
V Session_in_private_aufnehmen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-in-private-aufnehmen.toon.md
V Sent_in_private_aufnehmen_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_in_private_aufnehmen_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_in_private_aufnehmen_fix FIXES Sent_in_private_aufnehmen_raw
E Sent_in_private_aufnehmen_raw FROM_SESSION Session_in_private_aufnehmen
E Sent_in_private_aufnehmen_fix FROM_SESSION Session_in_private_aufnehmen

# ingest-session 2026-09-10T13:56:09Z chatbasierte-lueckentexte lang=de
V Session_chatbasierte_lueckentexte kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-chatbasierte-lueckentexte.toon.md
V Sent_chatbasierte_lueckentexte_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_chatbasierte_lueckentexte_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_chatbasierte_lueckentexte_fix FIXES Sent_chatbasierte_lueckentexte_raw
E Sent_chatbasierte_lueckentexte_raw FROM_SESSION Session_chatbasierte_lueckentexte
E Sent_chatbasierte_lueckentexte_fix FROM_SESSION Session_chatbasierte_lueckentexte

# ingest-session 2026-09-10T13:57:54Z wissensgraph-rueckmeldung lang=de
V Session_wissensgraph_rueckmeldung kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-wissensgraph-rueckmeldung.toon.md
V Sent_wissensgraph_rueckmeldung_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_wissensgraph_rueckmeldung_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_wissensgraph_rueckmeldung_fix FIXES Sent_wissensgraph_rueckmeldung_raw
E Sent_wissensgraph_rueckmeldung_raw FROM_SESSION Session_wissensgraph_rueckmeldung
E Sent_wissensgraph_rueckmeldung_fix FROM_SESSION Session_wissensgraph_rueckmeldung

# ingest-session 2026-09-10T13:59:14Z zehn-fragen lang=de
V Session_zehn_fragen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-zehn-fragen.toon.md
V Sent_zehn_fragen_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_zehn_fragen_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_zehn_fragen_fix FIXES Sent_zehn_fragen_raw
E Sent_zehn_fragen_raw FROM_SESSION Session_zehn_fragen
E Sent_zehn_fragen_fix FROM_SESSION Session_zehn_fragen

# ingest-session 2026-09-10T13:59:57Z lueckenuebungen-nicht-fragen lang=de
V Session_lueckenuebungen_nicht_fragen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebungen-nicht-fragen.toon.md
V Sent_lueckenuebungen_nicht_fragen_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_lueckenuebungen_nicht_fragen_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_lueckenuebungen_nicht_fragen_fix FIXES Sent_lueckenuebungen_nicht_fragen_raw
E Sent_lueckenuebungen_nicht_fragen_raw FROM_SESSION Session_lueckenuebungen_nicht_fragen
E Sent_lueckenuebungen_nicht_fragen_fix FROM_SESSION Session_lueckenuebungen_nicht_fragen

# ingest-session 2026-09-10T14:00:56Z lueckenuebung-konjunktiv-ii-zeit lang=de
V Session_lueckenuebung_konjunktiv_ii_zeit kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebung-konjunktiv-ii-zeit.toon.md
V Sent_lueckenuebung_konjunktiv_ii_zeit_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_lueckenuebung_konjunktiv_ii_zeit_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_lueckenuebung_konjunktiv_ii_zeit_fix FIXES Sent_lueckenuebung_konjunktiv_ii_zeit_raw
E Sent_lueckenuebung_konjunktiv_ii_zeit_raw FROM_SESSION Session_lueckenuebung_konjunktiv_ii_zeit
E Sent_lueckenuebung_konjunktiv_ii_zeit_fix FROM_SESSION Session_lueckenuebung_konjunktiv_ii_zeit

# ingest-session 2026-09-10T14:03:16Z lueckenuebung-vertrag-unterzeichnet lang=de
V Session_lueckenuebung_vertrag_unterzeichnet kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebung-vertrag-unterzeichnet.toon.md
V Sent_lueckenuebung_vertrag_unterzeichnet_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_lueckenuebung_vertrag_unterzeichnet_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_lueckenuebung_vertrag_unterzeichnet_fix FIXES Sent_lueckenuebung_vertrag_unterzeichnet_raw
E Sent_lueckenuebung_vertrag_unterzeichnet_raw FROM_SESSION Session_lueckenuebung_vertrag_unterzeichnet
E Sent_lueckenuebung_vertrag_unterzeichnet_fix FROM_SESSION Session_lueckenuebung_vertrag_unterzeichnet

# ingest-session 2026-09-11T14:45:36Z bei-mir-rhythmus lang=de
V Session_bei_mir_rhythmus kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-bei-mir-rhythmus.toon.md
V Sent_bei_mir_rhythmus_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_bei_mir_rhythmus_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_bei_mir_rhythmus_fix FIXES Sent_bei_mir_rhythmus_raw
E Sent_bei_mir_rhythmus_raw FROM_SESSION Session_bei_mir_rhythmus
E Sent_bei_mir_rhythmus_fix FROM_SESSION Session_bei_mir_rhythmus

# ingest-session 2026-09-11T14:46:18Z einwaende-geprueft lang=de
V Session_einwaende_geprueft kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-einwaende-geprueft.toon.md
V Sent_einwaende_geprueft_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_einwaende_geprueft_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_einwaende_geprueft_fix FIXES Sent_einwaende_geprueft_raw
E Sent_einwaende_geprueft_raw FROM_SESSION Session_einwaende_geprueft
E Sent_einwaende_geprueft_fix FROM_SESSION Session_einwaende_geprueft

# ingest-session 2026-09-11T14:52:25Z vorlaeufige-werte-betonen lang=de
V Session_vorlaeufige_werte_betonen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-vorlaeufige-werte-betonen.toon.md
V Sent_vorlaeufige_werte_betonen_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_vorlaeufige_werte_betonen_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_vorlaeufige_werte_betonen_fix FIXES Sent_vorlaeufige_werte_betonen_raw
E Sent_vorlaeufige_werte_betonen_raw FROM_SESSION Session_vorlaeufige_werte_betonen
E Sent_vorlaeufige_werte_betonen_fix FROM_SESSION Session_vorlaeufige_werte_betonen

# ingest-session 2026-09-11T14:53:03Z entwicklung-rueckgaengig-werden lang=de
V Session_entwicklung_rueckgaengig_werden kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-entwicklung-rueckgaengig-werden.toon.md
V Sent_entwicklung_rueckgaengig_werden_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_entwicklung_rueckgaengig_werden_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_entwicklung_rueckgaengig_werden_fix FIXES Sent_entwicklung_rueckgaengig_werden_raw
E Sent_entwicklung_rueckgaengig_werden_raw FROM_SESSION Session_entwicklung_rueckgaengig_werden
E Sent_entwicklung_rueckgaengig_werden_fix FROM_SESSION Session_entwicklung_rueckgaengig_werden

# ingest-session 2026-09-12T13:09:16Z vorschlag-mehrheitlich-angenommen lang=de
V Session_vorschlag_mehrheitlich_angenommen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-vorschlag-mehrheitlich-angenommen.toon.md
V Sent_vorschlag_mehrheitlich_angenommen_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_vorschlag_mehrheitlich_angenommen_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_vorschlag_mehrheitlich_angenommen_fix FIXES Sent_vorschlag_mehrheitlich_angenommen_raw
E Sent_vorschlag_mehrheitlich_angenommen_raw FROM_SESSION Session_vorschlag_mehrheitlich_angenommen
E Sent_vorschlag_mehrheitlich_angenommen_fix FROM_SESSION Session_vorschlag_mehrheitlich_angenommen

# ingest-session 2026-09-12T13:11:50Z ressourcenverbrauch-senken lang=de
V Session_ressourcenverbrauch_senken kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-ressourcenverbrauch-senken.toon.md
V Sent_ressourcenverbrauch_senken_raw kind=sentence date=2026-09-10 lang=de role=raw
V Sent_ressourcenverbrauch_senken_fix kind=sentence date=2026-09-10 lang=de role=corrected
E Sent_ressourcenverbrauch_senken_fix FIXES Sent_ressourcenverbrauch_senken_raw
E Sent_ressourcenverbrauch_senken_raw FROM_SESSION Session_ressourcenverbrauch_senken
E Sent_ressourcenverbrauch_senken_fix FROM_SESSION Session_ressourcenverbrauch_senken

# ingest-session 2026-09-12T13:14:46Z bedingungen-einigen lang=de
V Session_bedingungen_einigen kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-bedingungen-einigen.toon.md
V Sent_bedingungen_einigen_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_bedingungen_einigen_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_bedingungen_einigen_fix FIXES Sent_bedingungen_einigen_raw
E Sent_bedingungen_einigen_raw FROM_SESSION Session_bedingungen_einigen
E Sent_bedingungen_einigen_fix FROM_SESSION Session_bedingungen_einigen

# ingest-session 2026-09-12T13:17:04Z entscheidung-weil lang=de
V Session_entscheidung_weil kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-entscheidung-weil.toon.md
V Sent_entscheidung_weil_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_entscheidung_weil_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_entscheidung_weil_fix FIXES Sent_entscheidung_weil_raw
E Sent_entscheidung_weil_raw FROM_SESSION Session_entscheidung_weil
E Sent_entscheidung_weil_fix FROM_SESSION Session_entscheidung_weil

# ingest-session 2026-09-12T13:20:05Z versaeumen-obwohl lang=de
V Session_versaeumen_obwohl kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-versaeumen-obwohl.toon.md
V Sent_versaeumen_obwohl_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_versaeumen_obwohl_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_versaeumen_obwohl_fix FIXES Sent_versaeumen_obwohl_raw
E Sent_versaeumen_obwohl_raw FROM_SESSION Session_versaeumen_obwohl
E Sent_versaeumen_obwohl_fix FROM_SESSION Session_versaeumen_obwohl

# ingest-session 2026-09-12T13:21:12Z fehlerquellen-um-auszuschliessen lang=de
V Session_fehlerquellen_um_auszuschliessen kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-fehlerquellen-um-auszuschliessen.toon.md
V Sent_fehlerquellen_um_auszuschliessen_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_fehlerquellen_um_auszuschliessen_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_fehlerquellen_um_auszuschliessen_fix FIXES Sent_fehlerquellen_um_auszuschliessen_raw
E Sent_fehlerquellen_um_auszuschliessen_raw FROM_SESSION Session_fehlerquellen_um_auszuschliessen
E Sent_fehlerquellen_um_auszuschliessen_fix FROM_SESSION Session_fehlerquellen_um_auszuschliessen

# ingest-session 2026-09-12T13:22:41Z auswerten-entscheidung-aussetzen lang=de
V Session_auswerten_entscheidung_aussetzen kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-auswerten-entscheidung-aussetzen.toon.md
V Sent_auswerten_entscheidung_aussetzen_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_auswerten_entscheidung_aussetzen_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_auswerten_entscheidung_aussetzen_fix FIXES Sent_auswerten_entscheidung_aussetzen_raw
E Sent_auswerten_entscheidung_aussetzen_raw FROM_SESSION Session_auswerten_entscheidung_aussetzen
E Sent_auswerten_entscheidung_aussetzen_fix FROM_SESSION Session_auswerten_entscheidung_aussetzen

# ingest-session 2026-09-12T13:23:31Z anzahl-luecken lang=de
V Session_anzahl_luecken kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-anzahl-luecken.toon.md
V Sent_anzahl_luecken_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_anzahl_luecken_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_anzahl_luecken_fix FIXES Sent_anzahl_luecken_raw
E Sent_anzahl_luecken_raw FROM_SESSION Session_anzahl_luecken
E Sent_anzahl_luecken_fix FROM_SESSION Session_anzahl_luecken

# ingest-session 2026-09-12T13:25:14Z png-leistungszusammenfassung lang=de
V Session_png_leistungszusammenfassung kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-png-leistungszusammenfassung.toon.md
V Sent_png_leistungszusammenfassung_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_png_leistungszusammenfassung_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_png_leistungszusammenfassung_fix FIXES Sent_png_leistungszusammenfassung_raw
E Sent_png_leistungszusammenfassung_raw FROM_SESSION Session_png_leistungszusammenfassung
E Sent_png_leistungszusammenfassung_fix FROM_SESSION Session_png_leistungszusammenfassung

# ingest-session 2026-09-12T13:38:56Z in-den-privaten-ordner lang=de
V Session_in_den_privaten_ordner kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-in-den-privaten-ordner.toon.md
V Sent_in_den_privaten_ordner_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_in_den_privaten_ordner_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_in_den_privaten_ordner_fix FIXES Sent_in_den_privaten_ordner_raw
E Sent_in_den_privaten_ordner_raw FROM_SESSION Session_in_den_privaten_ordner
E Sent_in_den_privaten_ordner_fix FROM_SESSION Session_in_den_privaten_ordner

# ingest-session 2026-09-12T14:48:37Z bahnsteigtueren lang=de
V Session_bahnsteigtueren kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-bahnsteigtueren.toon.md
V Sent_bahnsteigtueren_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_bahnsteigtueren_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_bahnsteigtueren_fix FIXES Sent_bahnsteigtueren_raw
E Sent_bahnsteigtueren_raw FROM_SESSION Session_bahnsteigtueren
E Sent_bahnsteigtueren_fix FROM_SESSION Session_bahnsteigtueren

# ingest-session 2026-09-12T14:54:57Z b2-teil1-anfrage lang=de
V Session_b2_teil1_anfrage kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-b2-teil1-anfrage.toon.md
V Sent_b2_teil1_anfrage_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_b2_teil1_anfrage_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_b2_teil1_anfrage_fix FIXES Sent_b2_teil1_anfrage_raw
E Sent_b2_teil1_anfrage_raw FROM_SESSION Session_b2_teil1_anfrage
E Sent_b2_teil1_anfrage_fix FROM_SESSION Session_b2_teil1_anfrage

# ingest-session 2026-09-12T15:14:46Z wissensgraph-kopten lang=de
V Session_wissensgraph_kopten kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-wissensgraph-kopten.toon.md
V Sent_wissensgraph_kopten_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_wissensgraph_kopten_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_wissensgraph_kopten_fix FIXES Sent_wissensgraph_kopten_raw
E Sent_wissensgraph_kopten_raw FROM_SESSION Session_wissensgraph_kopten
E Sent_wissensgraph_kopten_fix FROM_SESSION Session_wissensgraph_kopten

# ingest-session 2026-09-12T16:15:34Z b2-uebung-nochmal lang=de
V Session_b2_uebung_nochmal kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-b2-uebung-nochmal.toon.md
V Sent_b2_uebung_nochmal_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_b2_uebung_nochmal_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_b2_uebung_nochmal_fix FIXES Sent_b2_uebung_nochmal_raw
E Sent_b2_uebung_nochmal_raw FROM_SESSION Session_b2_uebung_nochmal
E Sent_b2_uebung_nochmal_fix FROM_SESSION Session_b2_uebung_nochmal

# ingest-session 2026-09-12T23:18:34Z in-tmp-aufnehmen lang=de
V Session_in_tmp_aufnehmen kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-in-tmp-aufnehmen.toon.md
V Sent_in_tmp_aufnehmen_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_in_tmp_aufnehmen_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_in_tmp_aufnehmen_fix FIXES Sent_in_tmp_aufnehmen_raw
E Sent_in_tmp_aufnehmen_raw FROM_SESSION Session_in_tmp_aufnehmen
E Sent_in_tmp_aufnehmen_fix FROM_SESSION Session_in_tmp_aufnehmen

# ingest-session 2026-09-12T23:27:20Z screenshots-in-pdf lang=de
V Session_screenshots_in_pdf kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-screenshots-in-pdf.toon.md
V Sent_screenshots_in_pdf_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_screenshots_in_pdf_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_screenshots_in_pdf_fix FIXES Sent_screenshots_in_pdf_raw
E Sent_screenshots_in_pdf_raw FROM_SESSION Session_screenshots_in_pdf
E Sent_screenshots_in_pdf_fix FROM_SESSION Session_screenshots_in_pdf

# ingest-session 2026-09-12T23:47:25Z ideation-in-pdf lang=de
V Session_ideation_in_pdf kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-ideation-in-pdf.toon.md
V Sent_ideation_in_pdf_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_ideation_in_pdf_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_ideation_in_pdf_fix FIXES Sent_ideation_in_pdf_raw
E Sent_ideation_in_pdf_raw FROM_SESSION Session_ideation_in_pdf
E Sent_ideation_in_pdf_fix FROM_SESSION Session_ideation_in_pdf

# ingest-session 2026-09-13T00:05:40Z cypher-in-hall lang=de
V Session_cypher_in_hall kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-cypher-in-hall.toon.md
V Sent_cypher_in_hall_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_cypher_in_hall_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_cypher_in_hall_fix FIXES Sent_cypher_in_hall_raw
E Sent_cypher_in_hall_raw FROM_SESSION Session_cypher_in_hall
E Sent_cypher_in_hall_fix FROM_SESSION Session_cypher_in_hall

# ingest-session 2026-09-13T00:12:30Z licht-in-boden lang=de
V Session_licht_in_boden kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-licht-in-boden.toon.md
V Sent_licht_in_boden_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_licht_in_boden_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_licht_in_boden_fix FIXES Sent_licht_in_boden_raw
E Sent_licht_in_boden_raw FROM_SESSION Session_licht_in_boden
E Sent_licht_in_boden_fix FROM_SESSION Session_licht_in_boden

# ingest-session 2026-09-13T00:21:30Z shenyou-in-loop lang=de
V Session_shenyou_in_loop kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-shenyou-in-loop.toon.md
V Sent_shenyou_in_loop_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_shenyou_in_loop_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_shenyou_in_loop_fix FIXES Sent_shenyou_in_loop_raw
E Sent_shenyou_in_loop_raw FROM_SESSION Session_shenyou_in_loop
E Sent_shenyou_in_loop_fix FROM_SESSION Session_shenyou_in_loop

# ingest-session 2026-09-13T12:17:45Z dateischrank-teleportpunkt lang=de
V Session_dateischrank_teleportpunkt kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-dateischrank-teleportpunkt.toon.md
V Sent_dateischrank_teleportpunkt_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_dateischrank_teleportpunkt_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_dateischrank_teleportpunkt_fix FIXES Sent_dateischrank_teleportpunkt_raw
E Sent_dateischrank_teleportpunkt_raw FROM_SESSION Session_dateischrank_teleportpunkt
E Sent_dateischrank_teleportpunkt_fix FROM_SESSION Session_dateischrank_teleportpunkt

# ingest-session 2026-09-13T12:42:49Z teleport-welt-schief lang=de
V Session_teleport_welt_schief kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-teleport-welt-schief.toon.md
V Sent_teleport_welt_schief_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_teleport_welt_schief_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_teleport_welt_schief_fix FIXES Sent_teleport_welt_schief_raw
E Sent_teleport_welt_schief_raw FROM_SESSION Session_teleport_welt_schief
E Sent_teleport_welt_schief_fix FROM_SESSION Session_teleport_welt_schief

# ingest-session 2026-09-13T12:50:12Z vitrinen-brauchen-inhalt lang=de
V Session_vitrinen_brauchen_inhalt kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-vitrinen-brauchen-inhalt.toon.md
V Sent_vitrinen_brauchen_inhalt_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_vitrinen_brauchen_inhalt_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_vitrinen_brauchen_inhalt_fix FIXES Sent_vitrinen_brauchen_inhalt_raw
E Sent_vitrinen_brauchen_inhalt_raw FROM_SESSION Session_vitrinen_brauchen_inhalt
E Sent_vitrinen_brauchen_inhalt_fix FROM_SESSION Session_vitrinen_brauchen_inhalt

# ingest-session 2026-09-13T13:15:46Z nicht-nur-klartext lang=de
V Session_nicht_nur_klartext kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-nicht-nur-klartext.toon.md
V Sent_nicht_nur_klartext_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_nicht_nur_klartext_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_nicht_nur_klartext_fix FIXES Sent_nicht_nur_klartext_raw
E Sent_nicht_nur_klartext_raw FROM_SESSION Session_nicht_nur_klartext
E Sent_nicht_nur_klartext_fix FROM_SESSION Session_nicht_nur_klartext

# ingest-session 2026-09-13T14:08:29Z lagezentrale-mit-weltkarte lang=de
V Session_lagezentrale_mit_weltkarte kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-lagezentrale-mit-weltkarte.toon.md
V Sent_lagezentrale_mit_weltkarte_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_lagezentrale_mit_weltkarte_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_lagezentrale_mit_weltkarte_fix FIXES Sent_lagezentrale_mit_weltkarte_raw
E Sent_lagezentrale_mit_weltkarte_raw FROM_SESSION Session_lagezentrale_mit_weltkarte
E Sent_lagezentrale_mit_weltkarte_fix FROM_SESSION Session_lagezentrale_mit_weltkarte

# ingest-session 2026-09-13T14:15:34Z lagezentrale-braucht-kalender lang=de
V Session_lagezentrale_braucht_kalender kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-lagezentrale-braucht-kalender.toon.md
V Sent_lagezentrale_braucht_kalender_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_lagezentrale_braucht_kalender_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_lagezentrale_braucht_kalender_fix FIXES Sent_lagezentrale_braucht_kalender_raw
E Sent_lagezentrale_braucht_kalender_raw FROM_SESSION Session_lagezentrale_braucht_kalender
E Sent_lagezentrale_braucht_kalender_fix FROM_SESSION Session_lagezentrale_braucht_kalender

# ingest-session 2026-09-13T14:28:53Z elektronisches-buecherregal lang=de
V Session_elektronisches_buecherregal kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-elektronisches-buecherregal.toon.md
V Sent_elektronisches_buecherregal_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_elektronisches_buecherregal_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_elektronisches_buecherregal_fix FIXES Sent_elektronisches_buecherregal_raw
E Sent_elektronisches_buecherregal_raw FROM_SESSION Session_elektronisches_buecherregal
E Sent_elektronisches_buecherregal_fix FROM_SESSION Session_elektronisches_buecherregal

# ingest-session 2026-09-13T14:38:31Z von-aussen-lagezentrale lang=de
V Session_von_aussen_lagezentrale kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-von-aussen-lagezentrale.toon.md
V Sent_von_aussen_lagezentrale_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_von_aussen_lagezentrale_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_von_aussen_lagezentrale_fix FIXES Sent_von_aussen_lagezentrale_raw
E Sent_von_aussen_lagezentrale_raw FROM_SESSION Session_von_aussen_lagezentrale
E Sent_von_aussen_lagezentrale_fix FROM_SESSION Session_von_aussen_lagezentrale

# ingest-session 2026-09-13T14:44:31Z ab-diesem-zeitstempel lang=de
V Session_ab_diesem_zeitstempel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-ab-diesem-zeitstempel.toon.md
V Sent_ab_diesem_zeitstempel_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_ab_diesem_zeitstempel_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_ab_diesem_zeitstempel_fix FIXES Sent_ab_diesem_zeitstempel_raw
E Sent_ab_diesem_zeitstempel_raw FROM_SESSION Session_ab_diesem_zeitstempel
E Sent_ab_diesem_zeitstempel_fix FROM_SESSION Session_ab_diesem_zeitstempel

# ingest-session 2026-09-13T14:50:22Z kathedrale-schritte-klassik lang=de
V Session_kathedrale_schritte_klassik kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-kathedrale-schritte-klassik.toon.md
V Sent_kathedrale_schritte_klassik_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_kathedrale_schritte_klassik_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_kathedrale_schritte_klassik_fix FIXES Sent_kathedrale_schritte_klassik_raw
E Sent_kathedrale_schritte_klassik_raw FROM_SESSION Session_kathedrale_schritte_klassik
E Sent_kathedrale_schritte_klassik_fix FROM_SESSION Session_kathedrale_schritte_klassik

# ingest-session 2026-09-13T14:59:33Z laufen-ruckelt-licht-schatten lang=de
V Session_laufen_ruckelt_licht_schatten kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-laufen-ruckelt-licht-schatten.toon.md
V Sent_laufen_ruckelt_licht_schatten_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_laufen_ruckelt_licht_schatten_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_laufen_ruckelt_licht_schatten_fix FIXES Sent_laufen_ruckelt_licht_schatten_raw
E Sent_laufen_ruckelt_licht_schatten_raw FROM_SESSION Session_laufen_ruckelt_licht_schatten
E Sent_laufen_ruckelt_licht_schatten_fix FROM_SESSION Session_laufen_ruckelt_licht_schatten

# ingest-session 2026-09-13T15:17:33Z youtube-in-der-szene lang=de
V Session_youtube_in_der_szene kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-youtube-in-der-szene.toon.md
V Sent_youtube_in_der_szene_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_youtube_in_der_szene_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_youtube_in_der_szene_fix FIXES Sent_youtube_in_der_szene_raw
E Sent_youtube_in_der_szene_raw FROM_SESSION Session_youtube_in_der_szene
E Sent_youtube_in_der_szene_fix FROM_SESSION Session_youtube_in_der_szene

# ingest-session 2026-09-13T15:23:14Z videos-auf-einmal-erlauben lang=de
V Session_videos_auf_einmal_erlauben kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-videos-auf-einmal-erlauben.toon.md
V Sent_videos_auf_einmal_erlauben_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_videos_auf_einmal_erlauben_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_videos_auf_einmal_erlauben_fix FIXES Sent_videos_auf_einmal_erlauben_raw
E Sent_videos_auf_einmal_erlauben_raw FROM_SESSION Session_videos_auf_einmal_erlauben
E Sent_videos_auf_einmal_erlauben_fix FROM_SESSION Session_videos_auf_einmal_erlauben

# ingest-session 2026-09-13T15:29:25Z pda-woerter-festhalten lang=de
V Session_pda_woerter_festhalten kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-pda-woerter-festhalten.toon.md
V Sent_pda_woerter_festhalten_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_pda_woerter_festhalten_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_pda_woerter_festhalten_fix FIXES Sent_pda_woerter_festhalten_raw
E Sent_pda_woerter_festhalten_raw FROM_SESSION Session_pda_woerter_festhalten
E Sent_pda_woerter_festhalten_fix FROM_SESSION Session_pda_woerter_festhalten
V Pda_Handger_t kind=lemma lang=de surface=Handgerät gloss=PDA source=pda

# ingest-session 2026-09-13T15:40:11Z bibliothek-holzspiegel lang=de
V Session_bibliothek_holzspiegel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bibliothek-holzspiegel.toon.md
V Sent_bibliothek_holzspiegel_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_bibliothek_holzspiegel_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_bibliothek_holzspiegel_fix FIXES Sent_bibliothek_holzspiegel_raw
E Sent_bibliothek_holzspiegel_raw FROM_SESSION Session_bibliothek_holzspiegel
E Sent_bibliothek_holzspiegel_fix FROM_SESSION Session_bibliothek_holzspiegel

# ingest-session 2026-09-13T15:45:18Z mittelgang-sternenhimmel lang=de
V Session_mittelgang_sternenhimmel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-mittelgang-sternenhimmel.toon.md
V Sent_mittelgang_sternenhimmel_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_mittelgang_sternenhimmel_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_mittelgang_sternenhimmel_fix FIXES Sent_mittelgang_sternenhimmel_raw
E Sent_mittelgang_sternenhimmel_raw FROM_SESSION Session_mittelgang_sternenhimmel
E Sent_mittelgang_sternenhimmel_fix FROM_SESSION Session_mittelgang_sternenhimmel

# ingest-session 2026-09-13T16:08:28Z sternenhimmel-ohne-verzoegerung lang=de
V Session_sternenhimmel_ohne_verzoegerung kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-sternenhimmel-ohne-verzoegerung.toon.md
V Sent_sternenhimmel_ohne_verzoegerung_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_sternenhimmel_ohne_verzoegerung_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_sternenhimmel_ohne_verzoegerung_fix FIXES Sent_sternenhimmel_ohne_verzoegerung_raw
E Sent_sternenhimmel_ohne_verzoegerung_raw FROM_SESSION Session_sternenhimmel_ohne_verzoegerung
E Sent_sternenhimmel_ohne_verzoegerung_fix FROM_SESSION Session_sternenhimmel_ohne_verzoegerung

# ingest-session 2026-09-13T16:14:53Z bibliothek-feine-materialien lang=de
V Session_bibliothek_feine_materialien kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bibliothek-feine-materialien.toon.md
V Sent_bibliothek_feine_materialien_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_bibliothek_feine_materialien_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_bibliothek_feine_materialien_fix FIXES Sent_bibliothek_feine_materialien_raw
E Sent_bibliothek_feine_materialien_raw FROM_SESSION Session_bibliothek_feine_materialien
E Sent_bibliothek_feine_materialien_fix FROM_SESSION Session_bibliothek_feine_materialien

# ingest-session 2026-09-13T17:33:41Z gpu-ohne-kollision lang=de
V Session_gpu_ohne_kollision kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-gpu-ohne-kollision.toon.md
V Sent_gpu_ohne_kollision_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_gpu_ohne_kollision_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_gpu_ohne_kollision_fix FIXES Sent_gpu_ohne_kollision_raw
E Sent_gpu_ohne_kollision_raw FROM_SESSION Session_gpu_ohne_kollision
E Sent_gpu_ohne_kollision_fix FROM_SESSION Session_gpu_ohne_kollision

# ingest-session 2026-09-13T17:39:35Z leichter-lernplan-muede lang=de
V Session_leichter_lernplan_muede kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-leichter-lernplan-muede.toon.md
V Sent_leichter_lernplan_muede_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_leichter_lernplan_muede_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_leichter_lernplan_muede_fix FIXES Sent_leichter_lernplan_muede_raw
E Sent_leichter_lernplan_muede_raw FROM_SESSION Session_leichter_lernplan_muede
E Sent_leichter_lernplan_muede_fix FROM_SESSION Session_leichter_lernplan_muede

# ingest-session 2026-09-13T17:40:59Z allgemeine-uebungsfrage-asynchron lang=de
V Session_allgemeine_uebungsfrage_asynchron kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-allgemeine-uebungsfrage-asynchron.toon.md
V Sent_allgemeine_uebungsfrage_asynchron_raw kind=sentence date=2026-09-12 lang=de role=raw
V Sent_allgemeine_uebungsfrage_asynchron_fix kind=sentence date=2026-09-12 lang=de role=corrected
E Sent_allgemeine_uebungsfrage_asynchron_fix FIXES Sent_allgemeine_uebungsfrage_asynchron_raw
E Sent_allgemeine_uebungsfrage_asynchron_raw FROM_SESSION Session_allgemeine_uebungsfrage_asynchron
E Sent_allgemeine_uebungsfrage_asynchron_fix FROM_SESSION Session_allgemeine_uebungsfrage_asynchron

# ingest-session 2026-09-13T17:41:54Z allgemeine-frage-nicht-deutsch lang=de
V Session_allgemeine_frage_nicht_deutsch kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-allgemeine-frage-nicht-deutsch.toon.md
V Sent_allgemeine_frage_nicht_deutsch_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_allgemeine_frage_nicht_deutsch_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_allgemeine_frage_nicht_deutsch_fix FIXES Sent_allgemeine_frage_nicht_deutsch_raw
E Sent_allgemeine_frage_nicht_deutsch_raw FROM_SESSION Session_allgemeine_frage_nicht_deutsch
E Sent_allgemeine_frage_nicht_deutsch_fix FROM_SESSION Session_allgemeine_frage_nicht_deutsch

# ingest-session 2026-09-13T17:43:07Z probefrage-aus-wissensgraph lang=de
V Session_probefrage_aus_wissensgraph kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-probefrage-aus-wissensgraph.toon.md
V Sent_probefrage_aus_wissensgraph_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_probefrage_aus_wissensgraph_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_probefrage_aus_wissensgraph_fix FIXES Sent_probefrage_aus_wissensgraph_raw
E Sent_probefrage_aus_wissensgraph_raw FROM_SESSION Session_probefrage_aus_wissensgraph
E Sent_probefrage_aus_wissensgraph_fix FROM_SESSION Session_probefrage_aus_wissensgraph

# ingest-session 2026-09-13T18:54:17Z in-dieses-system-integrieren lang=de
V Session_in_dieses_system_integrieren kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-in-dieses-system-integrieren.toon.md
V Sent_in_dieses_system_integrieren_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_in_dieses_system_integrieren_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_in_dieses_system_integrieren_fix FIXES Sent_in_dieses_system_integrieren_raw
E Sent_in_dieses_system_integrieren_raw FROM_SESSION Session_in_dieses_system_integrieren
E Sent_in_dieses_system_integrieren_fix FROM_SESSION Session_in_dieses_system_integrieren

# ingest-session 2026-09-13T18:56:25Z bodenspiegelung-in-jedem-raum lang=de
V Session_bodenspiegelung_in_jedem_raum kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bodenspiegelung-in-jedem-raum.toon.md
V Sent_bodenspiegelung_in_jedem_raum_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_bodenspiegelung_in_jedem_raum_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_bodenspiegelung_in_jedem_raum_fix FIXES Sent_bodenspiegelung_in_jedem_raum_raw
E Sent_bodenspiegelung_in_jedem_raum_raw FROM_SESSION Session_bodenspiegelung_in_jedem_raum
E Sent_bodenspiegelung_in_jedem_raum_fix FROM_SESSION Session_bodenspiegelung_in_jedem_raum

# ingest-session 2026-09-13T19:01:32Z w-bleibt-chrome-kurzbefehl lang=de
V Session_w_bleibt_chrome_kurzbefehl kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-w-bleibt-chrome-kurzbefehl.toon.md
V Sent_w_bleibt_chrome_kurzbefehl_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_w_bleibt_chrome_kurzbefehl_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_w_bleibt_chrome_kurzbefehl_fix FIXES Sent_w_bleibt_chrome_kurzbefehl_raw
E Sent_w_bleibt_chrome_kurzbefehl_raw FROM_SESSION Session_w_bleibt_chrome_kurzbefehl
E Sent_w_bleibt_chrome_kurzbefehl_fix FROM_SESSION Session_w_bleibt_chrome_kurzbefehl

# ingest-session 2026-09-13T19:37:17Z fluester-asmr-deutsche-untertitel lang=de
V Session_fluester_asmr_deutsche_untertitel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-fluester-asmr-deutsche-untertitel.toon.md
V Sent_fluester_asmr_deutsche_untertitel_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_fluester_asmr_deutsche_untertitel_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_fluester_asmr_deutsche_untertitel_fix FIXES Sent_fluester_asmr_deutsche_untertitel_raw
E Sent_fluester_asmr_deutsche_untertitel_raw FROM_SESSION Session_fluester_asmr_deutsche_untertitel
E Sent_fluester_asmr_deutsche_untertitel_fix FROM_SESSION Session_fluester_asmr_deutsche_untertitel

# ingest-session 2026-09-13T20:46:04Z echtes-fluestern-keine-modalstimme lang=de
V Session_echtes_fluestern_keine_modalstimme kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-echtes-fluestern-keine-modalstimme.toon.md
V Sent_echtes_fluestern_keine_modalstimme_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_echtes_fluestern_keine_modalstimme_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_echtes_fluestern_keine_modalstimme_fix FIXES Sent_echtes_fluestern_keine_modalstimme_raw
E Sent_echtes_fluestern_keine_modalstimme_raw FROM_SESSION Session_echtes_fluestern_keine_modalstimme
E Sent_echtes_fluestern_keine_modalstimme_fix FROM_SESSION Session_echtes_fluestern_keine_modalstimme

# ingest-session 2026-09-13T21:42:07Z github-fuer-echtes-fluestern lang=de
V Session_github_fuer_echtes_fluestern kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-github-fuer-echtes-fluestern.toon.md
V Sent_github_fuer_echtes_fluestern_raw kind=sentence date=2026-09-13 lang=de role=raw
V Sent_github_fuer_echtes_fluestern_fix kind=sentence date=2026-09-13 lang=de role=corrected
E Sent_github_fuer_echtes_fluestern_fix FIXES Sent_github_fuer_echtes_fluestern_raw
E Sent_github_fuer_echtes_fluestern_raw FROM_SESSION Session_github_fuer_echtes_fluestern
E Sent_github_fuer_echtes_fluestern_fix FROM_SESSION Session_github_fuer_echtes_fluestern

# ingest-session 2026-09-13T22:28:56Z inflow-orca-ade lang=de
V Session_inflow_orca_ade kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-inflow-orca-ade.toon.md
V Sent_inflow_orca_ade_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_inflow_orca_ade_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_inflow_orca_ade_fix FIXES Sent_inflow_orca_ade_raw
E Sent_inflow_orca_ade_raw FROM_SESSION Session_inflow_orca_ade
E Sent_inflow_orca_ade_fix FROM_SESSION Session_inflow_orca_ade

# ingest-session 2026-09-14T09:21:02Z aufgestanden-hall-inflow lang=de
V Session_aufgestanden_hall_inflow kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-aufgestanden-hall-inflow.toon.md
V Sent_aufgestanden_hall_inflow_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_aufgestanden_hall_inflow_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_aufgestanden_hall_inflow_fix FIXES Sent_aufgestanden_hall_inflow_raw
E Sent_aufgestanden_hall_inflow_raw FROM_SESSION Session_aufgestanden_hall_inflow
E Sent_aufgestanden_hall_inflow_fix FROM_SESSION Session_aufgestanden_hall_inflow

# ingest-session 2026-09-14T09:29:29Z zu-viele-emails-ki-agent lang=de
V Session_zu_viele_emails_ki_agent kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zu-viele-emails-ki-agent.toon.md
V Sent_zu_viele_emails_ki_agent_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_zu_viele_emails_ki_agent_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_zu_viele_emails_ki_agent_fix FIXES Sent_zu_viele_emails_ki_agent_raw
E Sent_zu_viele_emails_ki_agent_raw FROM_SESSION Session_zu_viele_emails_ki_agent
E Sent_zu_viele_emails_ki_agent_fix FROM_SESSION Session_zu_viele_emails_ki_agent

# ingest-session 2026-09-14T09:30:19Z nahrungsergaenzung-heute lang=de
V Session_nahrungsergaenzung_heute kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nahrungsergaenzung-heute.toon.md
V Sent_nahrungsergaenzung_heute_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_nahrungsergaenzung_heute_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_nahrungsergaenzung_heute_fix FIXES Sent_nahrungsergaenzung_heute_raw
E Sent_nahrungsergaenzung_heute_raw FROM_SESSION Session_nahrungsergaenzung_heute
E Sent_nahrungsergaenzung_heute_fix FROM_SESSION Session_nahrungsergaenzung_heute

# ingest-session 2026-09-14T09:33:39Z nuancen-aktualisierte-empfehlung lang=de
V Session_nuancen_aktualisierte_empfehlung kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nuancen-aktualisierte-empfehlung.toon.md
V Sent_nuancen_aktualisierte_empfehlung_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_nuancen_aktualisierte_empfehlung_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_nuancen_aktualisierte_empfehlung_fix FIXES Sent_nuancen_aktualisierte_empfehlung_raw
E Sent_nuancen_aktualisierte_empfehlung_raw FROM_SESSION Session_nuancen_aktualisierte_empfehlung
E Sent_nuancen_aktualisierte_empfehlung_fix FROM_SESSION Session_nuancen_aktualisierte_empfehlung

# ingest-session 2026-09-14T09:36:04Z wie-man-es-macht lang=de
V Session_wie_man_es_macht kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wie-man-es-macht.toon.md
V Sent_wie_man_es_macht_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_wie_man_es_macht_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_wie_man_es_macht_fix FIXES Sent_wie_man_es_macht_raw
E Sent_wie_man_es_macht_raw FROM_SESSION Session_wie_man_es_macht
E Sent_wie_man_es_macht_fix FROM_SESSION Session_wie_man_es_macht

# ingest-session 2026-09-14T09:37:45Z nutzungsempfehlung-oregano-neem lang=de
V Session_nutzungsempfehlung_oregano_neem kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nutzungsempfehlung-oregano-neem.toon.md
V Sent_nutzungsempfehlung_oregano_neem_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_nutzungsempfehlung_oregano_neem_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_nutzungsempfehlung_oregano_neem_fix FIXES Sent_nutzungsempfehlung_oregano_neem_raw
E Sent_nutzungsempfehlung_oregano_neem_raw FROM_SESSION Session_nutzungsempfehlung_oregano_neem
E Sent_nutzungsempfehlung_oregano_neem_fix FROM_SESSION Session_nutzungsempfehlung_oregano_neem

# ingest-session 2026-09-14T09:41:45Z aphthen-gaenzlich-weg lang=de
V Session_aphthen_gaenzlich_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-aphthen-gaenzlich-weg.toon.md
V Sent_aphthen_gaenzlich_weg_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_aphthen_gaenzlich_weg_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_aphthen_gaenzlich_weg_fix FIXES Sent_aphthen_gaenzlich_weg_raw
E Sent_aphthen_gaenzlich_weg_raw FROM_SESSION Session_aphthen_gaenzlich_weg
E Sent_aphthen_gaenzlich_weg_fix FROM_SESSION Session_aphthen_gaenzlich_weg

# ingest-session 2026-09-14T09:43:48Z wo-finde-ich-imap-titan lang=de
V Session_wo_finde_ich_imap_titan kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wo-finde-ich-imap-titan.toon.md
V Sent_wo_finde_ich_imap_titan_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_wo_finde_ich_imap_titan_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_wo_finde_ich_imap_titan_fix FIXES Sent_wo_finde_ich_imap_titan_raw
E Sent_wo_finde_ich_imap_titan_raw FROM_SESSION Session_wo_finde_ich_imap_titan
E Sent_wo_finde_ich_imap_titan_fix FROM_SESSION Session_wo_finde_ich_imap_titan

# ingest-session 2026-09-14T09:47:07Z blickwinkel-materialfehler lang=de
V Session_blickwinkel_materialfehler kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-blickwinkel-materialfehler.toon.md
V Sent_blickwinkel_materialfehler_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_blickwinkel_materialfehler_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_blickwinkel_materialfehler_fix FIXES Sent_blickwinkel_materialfehler_raw
E Sent_blickwinkel_materialfehler_raw FROM_SESSION Session_blickwinkel_materialfehler
E Sent_blickwinkel_materialfehler_fix FROM_SESSION Session_blickwinkel_materialfehler

# ingest-session 2026-09-14T09:50:17Z enable-titan-on-other-apps-fehlt lang=de
V Session_enable_titan_on_other_apps_fehlt kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-enable-titan-on-other-apps-fehlt.toon.md
V Sent_enable_titan_on_other_apps_fehlt_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_enable_titan_on_other_apps_fehlt_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_enable_titan_on_other_apps_fehlt_fix FIXES Sent_enable_titan_on_other_apps_fehlt_raw
E Sent_enable_titan_on_other_apps_fehlt_raw FROM_SESSION Session_enable_titan_on_other_apps_fehlt
E Sent_enable_titan_on_other_apps_fehlt_fix FROM_SESSION Session_enable_titan_on_other_apps_fehlt

# ingest-session 2026-09-14T09:54:58Z imap-example-triage-env lang=de
V Session_imap_example_triage_env kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-imap-example-triage-env.toon.md
V Sent_imap_example_triage_env_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_imap_example_triage_env_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_imap_example_triage_env_fix FIXES Sent_imap_example_triage_env_raw
E Sent_imap_example_triage_env_raw FROM_SESSION Session_imap_example_triage_env
E Sent_imap_example_triage_env_fix FROM_SESSION Session_imap_example_triage_env

# ingest-session 2026-09-14T09:56:18Z imap-passwort-webmail-oder-godaddy lang=de
V Session_imap_passwort_webmail_oder_godaddy kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-imap-passwort-webmail-oder-godaddy.toon.md
V Sent_imap_passwort_webmail_oder_godaddy_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_imap_passwort_webmail_oder_godaddy_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_imap_passwort_webmail_oder_godaddy_fix FIXES Sent_imap_passwort_webmail_oder_godaddy_raw
E Sent_imap_passwort_webmail_oder_godaddy_raw FROM_SESSION Session_imap_passwort_webmail_oder_godaddy
E Sent_imap_passwort_webmail_oder_godaddy_fix FROM_SESSION Session_imap_passwort_webmail_oder_godaddy

# ingest-session 2026-09-14T09:58:30Z private-env-ausprobieren lang=de
V Session_private_env_ausprobieren kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-private-env-ausprobieren.toon.md
V Sent_private_env_ausprobieren_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_private_env_ausprobieren_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_private_env_ausprobieren_fix FIXES Sent_private_env_ausprobieren_raw
E Sent_private_env_ausprobieren_raw FROM_SESSION Session_private_env_ausprobieren
E Sent_private_env_ausprobieren_fix FROM_SESSION Session_private_env_ausprobieren

# ingest-session 2026-09-14T10:19:14Z mails-nach-system-sortieren lang=de
V Session_mails_nach_system_sortieren kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mails-nach-system-sortieren.toon.md
V Sent_mails_nach_system_sortieren_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_mails_nach_system_sortieren_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_mails_nach_system_sortieren_fix FIXES Sent_mails_nach_system_sortieren_raw
E Sent_mails_nach_system_sortieren_raw FROM_SESSION Session_mails_nach_system_sortieren
E Sent_mails_nach_system_sortieren_fix FROM_SESSION Session_mails_nach_system_sortieren

# ingest-session 2026-09-14T10:56:45Z zero-inbox-todo lang=de
V Session_zero_inbox_todo kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zero-inbox-todo.toon.md
V Sent_zero_inbox_todo_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_zero_inbox_todo_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_zero_inbox_todo_fix FIXES Sent_zero_inbox_todo_raw
E Sent_zero_inbox_todo_raw FROM_SESSION Session_zero_inbox_todo
E Sent_zero_inbox_todo_fix FROM_SESSION Session_zero_inbox_todo

# ingest-session 2026-09-14T11:06:02Z zero-inbox-goal-loop lang=de
V Session_zero_inbox_goal_loop kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zero-inbox-goal-loop.toon.md
V Sent_zero_inbox_goal_loop_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_zero_inbox_goal_loop_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_zero_inbox_goal_loop_fix FIXES Sent_zero_inbox_goal_loop_raw
E Sent_zero_inbox_goal_loop_raw FROM_SESSION Session_zero_inbox_goal_loop
E Sent_zero_inbox_goal_loop_fix FROM_SESSION Session_zero_inbox_goal_loop

# ingest-session 2026-09-14T11:37:55Z life-ordner-zusammenlegen-werbung-weg lang=de
V Session_life_ordner_zusammenlegen_werbung_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-life-ordner-zusammenlegen-werbung-weg.toon.md
V Sent_life_ordner_zusammenlegen_werbung_weg_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_life_ordner_zusammenlegen_werbung_weg_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_life_ordner_zusammenlegen_werbung_weg_fix FIXES Sent_life_ordner_zusammenlegen_werbung_weg_raw
E Sent_life_ordner_zusammenlegen_werbung_weg_raw FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg
E Sent_life_ordner_zusammenlegen_werbung_weg_fix FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg

# ingest-session 2026-09-14T13:59:56Z billing-rechnungen-keine-payback lang=de
V Session_billing_rechnungen_keine_payback kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-rechnungen-keine-payback.toon.md
V Sent_billing_rechnungen_keine_payback_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_billing_rechnungen_keine_payback_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_billing_rechnungen_keine_payback_fix FIXES Sent_billing_rechnungen_keine_payback_raw
E Sent_billing_rechnungen_keine_payback_raw FROM_SESSION Session_billing_rechnungen_keine_payback
E Sent_billing_rechnungen_keine_payback_fix FROM_SESSION Session_billing_rechnungen_keine_payback

# ingest-session 2026-09-14T14:02:53Z leere-ordner-loeschen lang=de
V Session_leere_ordner_loeschen kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-leere-ordner-loeschen.toon.md
V Sent_leere_ordner_loeschen_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_leere_ordner_loeschen_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_leere_ordner_loeschen_fix FIXES Sent_leere_ordner_loeschen_raw
E Sent_leere_ordner_loeschen_raw FROM_SESSION Session_leere_ordner_loeschen
E Sent_leere_ordner_loeschen_fix FROM_SESSION Session_leere_ordner_loeschen

# ingest-session 2026-09-14T14:29:48Z mails-statistisch-klassifizieren-pdf lang=de
V Session_mails_statistisch_klassifizieren_pdf kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mails-statistisch-klassifizieren-pdf.toon.md
V Sent_mails_statistisch_klassifizieren_pdf_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_mails_statistisch_klassifizieren_pdf_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_mails_statistisch_klassifizieren_pdf_fix FIXES Sent_mails_statistisch_klassifizieren_pdf_raw
E Sent_mails_statistisch_klassifizieren_pdf_raw FROM_SESSION Session_mails_statistisch_klassifizieren_pdf
E Sent_mails_statistisch_klassifizieren_pdf_fix FROM_SESSION Session_mails_statistisch_klassifizieren_pdf

# ingest-session 2026-09-14T15:20:02Z ablehnung-loeschen-anmerkungswuerdig lang=de
V Session_ablehnung_loeschen_anmerkungswuerdig kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-ablehnung-loeschen-anmerkungswuerdig.toon.md
V Sent_ablehnung_loeschen_anmerkungswuerdig_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_ablehnung_loeschen_anmerkungswuerdig_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_ablehnung_loeschen_anmerkungswuerdig_fix FIXES Sent_ablehnung_loeschen_anmerkungswuerdig_raw
E Sent_ablehnung_loeschen_anmerkungswuerdig_raw FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig
E Sent_ablehnung_loeschen_anmerkungswuerdig_fix FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig

# ingest-session 2026-09-14T15:25:18Z anstrengen-aesthetischer-chill lang=de
V Session_anstrengen_aesthetischer_chill kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-anstrengen-aesthetischer-chill.toon.md
V Sent_anstrengen_aesthetischer_chill_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_anstrengen_aesthetischer_chill_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_anstrengen_aesthetischer_chill_fix FIXES Sent_anstrengen_aesthetischer_chill_raw
E Sent_anstrengen_aesthetischer_chill_raw FROM_SESSION Session_anstrengen_aesthetischer_chill
E Sent_anstrengen_aesthetischer_chill_fix FROM_SESSION Session_anstrengen_aesthetischer_chill

# ingest-session 2026-09-14T16:24:47Z payback-loeschen-ordner-kuerzen lang=de
V Session_payback_loeschen_ordner_kuerzen kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-payback-loeschen-ordner-kuerzen.toon.md
V Sent_payback_loeschen_ordner_kuerzen_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_payback_loeschen_ordner_kuerzen_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_payback_loeschen_ordner_kuerzen_fix FIXES Sent_payback_loeschen_ordner_kuerzen_raw
E Sent_payback_loeschen_ordner_kuerzen_raw FROM_SESSION Session_payback_loeschen_ordner_kuerzen
E Sent_payback_loeschen_ordner_kuerzen_fix FROM_SESSION Session_payback_loeschen_ordner_kuerzen

# ingest-session 2026-09-14T17:03:53Z billing-n26-werbung-raus lang=de
V Session_billing_n26_werbung_raus kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-n26-werbung-raus.toon.md
V Sent_billing_n26_werbung_raus_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_billing_n26_werbung_raus_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_billing_n26_werbung_raus_fix FIXES Sent_billing_n26_werbung_raus_raw
E Sent_billing_n26_werbung_raus_raw FROM_SESSION Session_billing_n26_werbung_raus
E Sent_billing_n26_werbung_raus_fix FROM_SESSION Session_billing_n26_werbung_raus

# ingest-session 2026-09-14T17:09:26Z billing-loeschvorschlag-aehnliche-mails lang=de
V Session_billing_loeschvorschlag_aehnliche_mails kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-loeschvorschlag-aehnliche-mails.toon.md
V Sent_billing_loeschvorschlag_aehnliche_mails_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_billing_loeschvorschlag_aehnliche_mails_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_billing_loeschvorschlag_aehnliche_mails_fix FIXES Sent_billing_loeschvorschlag_aehnliche_mails_raw
E Sent_billing_loeschvorschlag_aehnliche_mails_raw FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails
E Sent_billing_loeschvorschlag_aehnliche_mails_fix FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails

# ingest-session 2026-09-14T17:52:40Z mailbox-shenyou-wertlos-weg lang=de
V Session_mailbox_shenyou_wertlos_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mailbox-shenyou-wertlos-weg.toon.md
V Sent_mailbox_shenyou_wertlos_weg_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_mailbox_shenyou_wertlos_weg_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_mailbox_shenyou_wertlos_weg_fix FIXES Sent_mailbox_shenyou_wertlos_weg_raw
E Sent_mailbox_shenyou_wertlos_weg_raw FROM_SESSION Session_mailbox_shenyou_wertlos_weg
E Sent_mailbox_shenyou_wertlos_weg_fix FROM_SESSION Session_mailbox_shenyou_wertlos_weg

# ingest-session 2026-09-14T18:21:26Z linkedin-post-ins-deutsche lang=de
V Session_linkedin_post_ins_deutsche kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-linkedin-post-ins-deutsche.toon.md
V Sent_linkedin_post_ins_deutsche_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_linkedin_post_ins_deutsche_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_linkedin_post_ins_deutsche_fix FIXES Sent_linkedin_post_ins_deutsche_raw
E Sent_linkedin_post_ins_deutsche_raw FROM_SESSION Session_linkedin_post_ins_deutsche
E Sent_linkedin_post_ins_deutsche_fix FROM_SESSION Session_linkedin_post_ins_deutsche

# ingest-session 2026-09-14T18:32:42Z billing-aelter-als-ein-jahr-weg lang=de
V Session_billing_aelter_als_ein_jahr_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-aelter-als-ein-jahr-weg.toon.md
V Sent_billing_aelter_als_ein_jahr_weg_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_billing_aelter_als_ein_jahr_weg_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_billing_aelter_als_ein_jahr_weg_fix FIXES Sent_billing_aelter_als_ein_jahr_weg_raw
E Sent_billing_aelter_als_ein_jahr_weg_raw FROM_SESSION Session_billing_aelter_als_ein_jahr_weg
E Sent_billing_aelter_als_ein_jahr_weg_fix FROM_SESSION Session_billing_aelter_als_ein_jahr_weg

# ingest-session 2026-09-14T18:35:00Z wie-man-es-benutzt lang=de
V Session_wie_man_es_benutzt kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wie-man-es-benutzt.toon.md
V Sent_wie_man_es_benutzt_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_wie_man_es_benutzt_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_wie_man_es_benutzt_fix FIXES Sent_wie_man_es_benutzt_raw
E Sent_wie_man_es_benutzt_raw FROM_SESSION Session_wie_man_es_benutzt
E Sent_wie_man_es_benutzt_fix FROM_SESSION Session_wie_man_es_benutzt

# ingest-session 2026-09-14T18:41:02Z noch-diese-solchen-nachrichten lang=de
V Session_noch_diese_solchen_nachrichten kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-noch-diese-solchen-nachrichten.toon.md
V Sent_noch_diese_solchen_nachrichten_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_noch_diese_solchen_nachrichten_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_noch_diese_solchen_nachrichten_fix FIXES Sent_noch_diese_solchen_nachrichten_raw
E Sent_noch_diese_solchen_nachrichten_raw FROM_SESSION Session_noch_diese_solchen_nachrichten
E Sent_noch_diese_solchen_nachrichten_fix FROM_SESSION Session_noch_diese_solchen_nachrichten

# ingest-session 2026-09-14T19:01:23Z kenntnisse-ueber-zk lang=de
V Session_kenntnisse_ueber_zk kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-kenntnisse-ueber-zk.toon.md
V Sent_kenntnisse_ueber_zk_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_kenntnisse_ueber_zk_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_kenntnisse_ueber_zk_fix FIXES Sent_kenntnisse_ueber_zk_raw
E Sent_kenntnisse_ueber_zk_raw FROM_SESSION Session_kenntnisse_ueber_zk
E Sent_kenntnisse_ueber_zk_fix FROM_SESSION Session_kenntnisse_ueber_zk

# ingest-session 2026-09-14T19:01:52Z life-linkedin-dhl-korrespondenz lang=de
V Session_life_linkedin_dhl_korrespondenz kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-life-linkedin-dhl-korrespondenz.toon.md
V Sent_life_linkedin_dhl_korrespondenz_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_life_linkedin_dhl_korrespondenz_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_life_linkedin_dhl_korrespondenz_fix FIXES Sent_life_linkedin_dhl_korrespondenz_raw
E Sent_life_linkedin_dhl_korrespondenz_raw FROM_SESSION Session_life_linkedin_dhl_korrespondenz
E Sent_life_linkedin_dhl_korrespondenz_fix FROM_SESSION Session_life_linkedin_dhl_korrespondenz

# ingest-session 2026-09-14T19:03:18Z auch-agent-tty lang=de
V Session_auch_agent_tty kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-auch-agent-tty.toon.md
V Sent_auch_agent_tty_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_auch_agent_tty_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_auch_agent_tty_fix FIXES Sent_auch_agent_tty_raw
E Sent_auch_agent_tty_raw FROM_SESSION Session_auch_agent_tty
E Sent_auch_agent_tty_fix FROM_SESSION Session_auch_agent_tty

# ingest-session 2026-09-14T19:05:50Z vollstaendigkeit-verstaendnis lang=de
V Session_vollstaendigkeit_verstaendnis kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-vollstaendigkeit-verstaendnis.toon.md
V Sent_vollstaendigkeit_verstaendnis_raw kind=sentence date=2026-09-14 lang=de role=raw
V Sent_vollstaendigkeit_verstaendnis_fix kind=sentence date=2026-09-14 lang=de role=corrected
E Sent_vollstaendigkeit_verstaendnis_fix FIXES Sent_vollstaendigkeit_verstaendnis_raw
E Sent_vollstaendigkeit_verstaendnis_raw FROM_SESSION Session_vollstaendigkeit_verstaendnis
E Sent_vollstaendigkeit_verstaendnis_fix FROM_SESSION Session_vollstaendigkeit_verstaendnis

# ingest-session 2026-09-15T12:57:03Z scapula-wieder-angefangen lang=de
V Session_scapula_wieder_angefangen kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-scapula-wieder-angefangen.toon.md
V Sent_scapula_wieder_angefangen_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_scapula_wieder_angefangen_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_scapula_wieder_angefangen_fix FIXES Sent_scapula_wieder_angefangen_raw
E Sent_scapula_wieder_angefangen_raw FROM_SESSION Session_scapula_wieder_angefangen
E Sent_scapula_wieder_angefangen_fix FROM_SESSION Session_scapula_wieder_angefangen

# ingest-session 2026-09-15T13:22:29Z zum-kenntnisdiagramm lang=de
V Session_zum_kenntnisdiagramm kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-zum-kenntnisdiagramm.toon.md
V Sent_zum_kenntnisdiagramm_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_zum_kenntnisdiagramm_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_zum_kenntnisdiagramm_fix FIXES Sent_zum_kenntnisdiagramm_raw
E Sent_zum_kenntnisdiagramm_raw FROM_SESSION Session_zum_kenntnisdiagramm
E Sent_zum_kenntnisdiagramm_fix FROM_SESSION Session_zum_kenntnisdiagramm

# ingest-session 2026-09-15T18:24:32Z advanzia-pin-geldautomat-rueckmeldung lang=de
V Session_advanzia_pin_geldautomat_rueckmeldung kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-advanzia-pin-geldautomat-rueckmeldung.toon.md
V Sent_advanzia_pin_geldautomat_rueckmeldung_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_advanzia_pin_geldautomat_rueckmeldung_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_advanzia_pin_geldautomat_rueckmeldung_fix FIXES Sent_advanzia_pin_geldautomat_rueckmeldung_raw
E Sent_advanzia_pin_geldautomat_rueckmeldung_raw FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung
E Sent_advanzia_pin_geldautomat_rueckmeldung_fix FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung

# ingest-session 2026-09-15T18:26:46Z advanzia-todo-protokollieren lang=de
V Session_advanzia_todo_protokollieren kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-advanzia-todo-protokollieren.toon.md
V Sent_advanzia_todo_protokollieren_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_advanzia_todo_protokollieren_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_advanzia_todo_protokollieren_fix FIXES Sent_advanzia_todo_protokollieren_raw
E Sent_advanzia_todo_protokollieren_raw FROM_SESSION Session_advanzia_todo_protokollieren
E Sent_advanzia_todo_protokollieren_fix FROM_SESSION Session_advanzia_todo_protokollieren

# ingest-session 2026-09-15T19:20:56Z email-an-advanzia-absenden lang=de
V Session_email_an_advanzia_absenden kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-email-an-advanzia-absenden.toon.md
V Sent_email_an_advanzia_absenden_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_email_an_advanzia_absenden_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_email_an_advanzia_absenden_fix FIXES Sent_email_an_advanzia_absenden_raw
E Sent_email_an_advanzia_absenden_raw FROM_SESSION Session_email_an_advanzia_absenden
E Sent_email_an_advanzia_absenden_fix FROM_SESSION Session_email_an_advanzia_absenden

# ingest-session 2026-09-15T19:24:32Z empfaenger-fuer-diese-email lang=de
V Session_empfaenger_fuer_diese_email kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-empfaenger-fuer-diese-email.toon.md
V Sent_empfaenger_fuer_diese_email_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_empfaenger_fuer_diese_email_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_empfaenger_fuer_diese_email_fix FIXES Sent_empfaenger_fuer_diese_email_raw
E Sent_empfaenger_fuer_diese_email_raw FROM_SESSION Session_empfaenger_fuer_diese_email
E Sent_empfaenger_fuer_diese_email_fix FROM_SESSION Session_empfaenger_fuer_diese_email

# ingest-session 2026-09-15T19:28:48Z franzoesische-uebungen-anhand lang=de
V Session_franzoesische_uebungen_anhand kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-franzoesische-uebungen-anhand.toon.md
V Sent_franzoesische_uebungen_anhand_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_franzoesische_uebungen_anhand_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_franzoesische_uebungen_anhand_fix FIXES Sent_franzoesische_uebungen_anhand_raw
E Sent_franzoesische_uebungen_anhand_raw FROM_SESSION Session_franzoesische_uebungen_anhand
E Sent_franzoesische_uebungen_anhand_fix FROM_SESSION Session_franzoesische_uebungen_anhand

# ingest-session 2026-09-15T19:47:04Z zusammenfassung-aller-emails-latex-pdf lang=de
V Session_zusammenfassung_aller_emails_latex_pdf kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-zusammenfassung-aller-emails-latex-pdf.toon.md
V Sent_zusammenfassung_aller_emails_latex_pdf_raw kind=sentence date=2026-09-15 lang=de role=raw
V Sent_zusammenfassung_aller_emails_latex_pdf_fix kind=sentence date=2026-09-15 lang=de role=corrected
E Sent_zusammenfassung_aller_emails_latex_pdf_fix FIXES Sent_zusammenfassung_aller_emails_latex_pdf_raw
E Sent_zusammenfassung_aller_emails_latex_pdf_raw FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf
E Sent_zusammenfassung_aller_emails_latex_pdf_fix FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf

# ingest-session 2026-09-16T09:17:48Z wie-macht-man-dann-3d-szene lang=de
V Session_wie_macht_man_dann_3d_szene kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-wie-macht-man-dann-3d-szene.toon.md
V Sent_wie_macht_man_dann_3d_szene_raw kind=sentence date=2026-09-16 lang=de role=raw
V Sent_wie_macht_man_dann_3d_szene_fix kind=sentence date=2026-09-16 lang=de role=corrected
E Sent_wie_macht_man_dann_3d_szene_fix FIXES Sent_wie_macht_man_dann_3d_szene_raw
E Sent_wie_macht_man_dann_3d_szene_raw FROM_SESSION Session_wie_macht_man_dann_3d_szene
E Sent_wie_macht_man_dann_3d_szene_fix FROM_SESSION Session_wie_macht_man_dann_3d_szene

# ingest-session 2026-09-16T09:26:40Z versuch-das-dann-mal-in-tmp lang=de
V Session_versuch_das_dann_mal_in_tmp kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-versuch-das-dann-mal-in-tmp.toon.md
V Sent_versuch_das_dann_mal_in_tmp_raw kind=sentence date=2026-09-16 lang=de role=raw
V Sent_versuch_das_dann_mal_in_tmp_fix kind=sentence date=2026-09-16 lang=de role=corrected
E Sent_versuch_das_dann_mal_in_tmp_fix FIXES Sent_versuch_das_dann_mal_in_tmp_raw
E Sent_versuch_das_dann_mal_in_tmp_raw FROM_SESSION Session_versuch_das_dann_mal_in_tmp
E Sent_versuch_das_dann_mal_in_tmp_fix FROM_SESSION Session_versuch_das_dann_mal_in_tmp

# ingest-session 2026-09-16T09:27:13Z kenntnisse-der-astrophysik-graph lang=de
V Session_kenntnisse_der_astrophysik_graph kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-kenntnisse-der-astrophysik-graph.toon.md
V Sent_kenntnisse_der_astrophysik_graph_raw kind=sentence date=2026-09-16 lang=de role=raw
V Sent_kenntnisse_der_astrophysik_graph_fix kind=sentence date=2026-09-16 lang=de role=corrected
E Sent_kenntnisse_der_astrophysik_graph_fix FIXES Sent_kenntnisse_der_astrophysik_graph_raw
E Sent_kenntnisse_der_astrophysik_graph_raw FROM_SESSION Session_kenntnisse_der_astrophysik_graph
E Sent_kenntnisse_der_astrophysik_graph_fix FROM_SESSION Session_kenntnisse_der_astrophysik_graph

# ingest-session 2026-09-16T09:35:05Z dann-ist-xiaoxin-also-nur-reupload lang=de
V Session_dann_ist_xiaoxin_also_nur_reupload kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-dann-ist-xiaoxin-also-nur-reupload.toon.md
V Sent_dann_ist_xiaoxin_also_nur_reupload_raw kind=sentence date=2026-09-16 lang=de role=raw
V Sent_dann_ist_xiaoxin_also_nur_reupload_fix kind=sentence date=2026-09-16 lang=de role=corrected
E Sent_dann_ist_xiaoxin_also_nur_reupload_fix FIXES Sent_dann_ist_xiaoxin_also_nur_reupload_raw
E Sent_dann_ist_xiaoxin_also_nur_reupload_raw FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload
E Sent_dann_ist_xiaoxin_also_nur_reupload_fix FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload

# ingest-session 2026-09-16T18:05:56Z um-die-reaktionsfaehigkeit-zu-testen lang=de
V Session_um_die_reaktionsfaehigkeit_zu_testen kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-um-die-reaktionsfaehigkeit-zu-testen.toon.md
V Sent_um_die_reaktionsfaehigkeit_zu_testen_raw kind=sentence date=2026-09-16 lang=de role=raw
V Sent_um_die_reaktionsfaehigkeit_zu_testen_fix kind=sentence date=2026-09-16 lang=de role=corrected
E Sent_um_die_reaktionsfaehigkeit_zu_testen_fix FIXES Sent_um_die_reaktionsfaehigkeit_zu_testen_raw
E Sent_um_die_reaktionsfaehigkeit_zu_testen_raw FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen
E Sent_um_die_reaktionsfaehigkeit_zu_testen_fix FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen

# ingest-session 2026-09-16T19:02:46Z sobald-es-rot-wird-laeuft-die-zeit lang=de
V Session_sobald_es_rot_wird_laeuft_die_zeit kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-sobald-es-rot-wird-laeuft-die-zeit.toon.md
V Sent_sobald_es_rot_wird_laeuft_die_zeit_raw kind=sentence date=2026-09-16 lang=de role=raw
V Sent_sobald_es_rot_wird_laeuft_die_zeit_fix kind=sentence date=2026-09-16 lang=de role=corrected
E Sent_sobald_es_rot_wird_laeuft_die_zeit_fix FIXES Sent_sobald_es_rot_wird_laeuft_die_zeit_raw
E Sent_sobald_es_rot_wird_laeuft_die_zeit_raw FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit
E Sent_sobald_es_rot_wird_laeuft_die_zeit_fix FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit

# ingest-session 2026-09-17T18:13:53Z workout-planung-oktoberfest lang=de
V Session_workout_planung_oktoberfest kind=session date=2026-09-17 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-17-workout-planung-oktoberfest.toon.md
V Sent_workout_planung_oktoberfest_raw kind=sentence date=2026-09-17 lang=de role=raw
V Sent_workout_planung_oktoberfest_fix kind=sentence date=2026-09-17 lang=de role=corrected
E Sent_workout_planung_oktoberfest_fix FIXES Sent_workout_planung_oktoberfest_raw
E Sent_workout_planung_oktoberfest_raw FROM_SESSION Session_workout_planung_oktoberfest
E Sent_workout_planung_oktoberfest_fix FROM_SESSION Session_workout_planung_oktoberfest

# ingest-session 2026-09-17T22:13:42Z starte-die-shenyou lang=de
V Session_starte_die_shenyou kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-starte-die-shenyou.toon.md
V Sent_starte_die_shenyou_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_starte_die_shenyou_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_starte_die_shenyou_fix FIXES Sent_starte_die_shenyou_raw
E Sent_starte_die_shenyou_raw FROM_SESSION Session_starte_die_shenyou
E Sent_starte_die_shenyou_fix FROM_SESSION Session_starte_die_shenyou

# ingest-session 2026-09-18T10:22:39Z tagesuebersicht-3d-html lang=de
V Session_tagesuebersicht_3d_html kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tagesuebersicht-3d-html.toon.md
V Sent_tagesuebersicht_3d_html_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_tagesuebersicht_3d_html_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_tagesuebersicht_3d_html_fix FIXES Sent_tagesuebersicht_3d_html_raw
E Sent_tagesuebersicht_3d_html_raw FROM_SESSION Session_tagesuebersicht_3d_html
E Sent_tagesuebersicht_3d_html_fix FROM_SESSION Session_tagesuebersicht_3d_html

# ingest-session 2026-09-18T10:55:28Z nginx-link-3d-halle lang=de
V Session_nginx_link_3d_halle kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-nginx-link-3d-halle.toon.md
V Sent_nginx_link_3d_halle_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_nginx_link_3d_halle_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_nginx_link_3d_halle_fix FIXES Sent_nginx_link_3d_halle_raw
E Sent_nginx_link_3d_halle_raw FROM_SESSION Session_nginx_link_3d_halle
E Sent_nginx_link_3d_halle_fix FROM_SESSION Session_nginx_link_3d_halle

# ingest-session 2026-09-18T10:57:38Z cli-befehl-3d-halle lang=de
V Session_cli_befehl_3d_halle kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-cli-befehl-3d-halle.toon.md
V Sent_cli_befehl_3d_halle_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_cli_befehl_3d_halle_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_cli_befehl_3d_halle_fix FIXES Sent_cli_befehl_3d_halle_raw
E Sent_cli_befehl_3d_halle_raw FROM_SESSION Session_cli_befehl_3d_halle
E Sent_cli_befehl_3d_halle_fix FROM_SESSION Session_cli_befehl_3d_halle

# ingest-session 2026-09-18T10:59:13Z oeffentlicher-ngrok-link lang=de
V Session_oeffentlicher_ngrok_link kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-oeffentlicher-ngrok-link.toon.md
V Sent_oeffentlicher_ngrok_link_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_oeffentlicher_ngrok_link_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_oeffentlicher_ngrok_link_fix FIXES Sent_oeffentlicher_ngrok_link_raw
E Sent_oeffentlicher_ngrok_link_raw FROM_SESSION Session_oeffentlicher_ngrok_link
E Sent_oeffentlicher_ngrok_link_fix FROM_SESSION Session_oeffentlicher_ngrok_link

# ingest-session 2026-09-18T11:04:27Z mobil-3d-halle-optimieren lang=de
V Session_mobil_3d_halle_optimieren kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-mobil-3d-halle-optimieren.toon.md
V Sent_mobil_3d_halle_optimieren_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_mobil_3d_halle_optimieren_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_mobil_3d_halle_optimieren_fix FIXES Sent_mobil_3d_halle_optimieren_raw
E Sent_mobil_3d_halle_optimieren_raw FROM_SESSION Session_mobil_3d_halle_optimieren
E Sent_mobil_3d_halle_optimieren_fix FROM_SESSION Session_mobil_3d_halle_optimieren

# ingest-session 2026-09-18T11:21:14Z hud-3d-szene lang=de
V Session_hud_3d_szene kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-hud-3d-szene.toon.md
V Sent_hud_3d_szene_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_hud_3d_szene_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_hud_3d_szene_fix FIXES Sent_hud_3d_szene_raw
E Sent_hud_3d_szene_raw FROM_SESSION Session_hud_3d_szene
E Sent_hud_3d_szene_fix FROM_SESSION Session_hud_3d_szene

# ingest-session 2026-09-18T11:30:09Z tageszusammenfassung lang=de
V Session_tageszusammenfassung kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tageszusammenfassung.toon.md
V Sent_tageszusammenfassung_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_tageszusammenfassung_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_tageszusammenfassung_fix FIXES Sent_tageszusammenfassung_raw
E Sent_tageszusammenfassung_raw FROM_SESSION Session_tageszusammenfassung
E Sent_tageszusammenfassung_fix FROM_SESSION Session_tageszusammenfassung

# ingest-session 2026-09-18T11:33:34Z todo-zeitplan lang=de
V Session_todo_zeitplan kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-todo-zeitplan.toon.md
V Sent_todo_zeitplan_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_todo_zeitplan_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_todo_zeitplan_fix FIXES Sent_todo_zeitplan_raw
E Sent_todo_zeitplan_raw FROM_SESSION Session_todo_zeitplan
E Sent_todo_zeitplan_fix FROM_SESSION Session_todo_zeitplan

# ingest-session 2026-09-18T13:28:20Z oktoberfest-unterwegs lang=de
V Session_oktoberfest_unterwegs kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-oktoberfest-unterwegs.toon.md
V Sent_oktoberfest_unterwegs_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_oktoberfest_unterwegs_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_oktoberfest_unterwegs_fix FIXES Sent_oktoberfest_unterwegs_raw
E Sent_oktoberfest_unterwegs_raw FROM_SESSION Session_oktoberfest_unterwegs
E Sent_oktoberfest_unterwegs_fix FROM_SESSION Session_oktoberfest_unterwegs

# ingest-session 2026-09-18T13:30:36Z recovery-zusammenfassung lang=de
V Session_recovery_zusammenfassung kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-recovery-zusammenfassung.toon.md
V Sent_recovery_zusammenfassung_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_recovery_zusammenfassung_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_recovery_zusammenfassung_fix FIXES Sent_recovery_zusammenfassung_raw
E Sent_recovery_zusammenfassung_raw FROM_SESSION Session_recovery_zusammenfassung
E Sent_recovery_zusammenfassung_fix FROM_SESSION Session_recovery_zusammenfassung

# ingest-session 2026-09-18T13:41:16Z luftmatratze-uebungsplan lang=de
V Session_luftmatratze_uebungsplan kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-luftmatratze-uebungsplan.toon.md
V Sent_luftmatratze_uebungsplan_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_luftmatratze_uebungsplan_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_luftmatratze_uebungsplan_fix FIXES Sent_luftmatratze_uebungsplan_raw
E Sent_luftmatratze_uebungsplan_raw FROM_SESSION Session_luftmatratze_uebungsplan
E Sent_luftmatratze_uebungsplan_fix FROM_SESSION Session_luftmatratze_uebungsplan

# ingest-session 2026-09-18T13:44:55Z schreibuebungen-bite-sized lang=de
V Session_schreibuebungen_bite_sized kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-schreibuebungen-bite-sized.toon.md
V Sent_schreibuebungen_bite_sized_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_schreibuebungen_bite_sized_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_schreibuebungen_bite_sized_fix FIXES Sent_schreibuebungen_bite_sized_raw
E Sent_schreibuebungen_bite_sized_raw FROM_SESSION Session_schreibuebungen_bite_sized
E Sent_schreibuebungen_bite_sized_fix FROM_SESSION Session_schreibuebungen_bite_sized

# ingest-session 2026-09-18T15:46:45Z beziehungen-private-bereich lang=de
V Session_beziehungen_private_bereich kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-beziehungen-private-bereich.toon.md
V Sent_beziehungen_private_bereich_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_beziehungen_private_bereich_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_beziehungen_private_bereich_fix FIXES Sent_beziehungen_private_bereich_raw
E Sent_beziehungen_private_bereich_raw FROM_SESSION Session_beziehungen_private_bereich
E Sent_beziehungen_private_bereich_fix FROM_SESSION Session_beziehungen_private_bereich

# ingest-session 2026-09-18T15:52:43Z ganzheitlicher-uebungsueberblick lang=de
V Session_ganzheitlicher_uebungsueberblick kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-ganzheitlicher-uebungsueberblick.toon.md
V Sent_ganzheitlicher_uebungsueberblick_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_ganzheitlicher_uebungsueberblick_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_ganzheitlicher_uebungsueberblick_fix FIXES Sent_ganzheitlicher_uebungsueberblick_raw
E Sent_ganzheitlicher_uebungsueberblick_raw FROM_SESSION Session_ganzheitlicher_uebungsueberblick
E Sent_ganzheitlicher_uebungsueberblick_fix FROM_SESSION Session_ganzheitlicher_uebungsueberblick

# ingest-session 2026-09-18T16:02:46Z odyssee-start lang=de
V Session_odyssee_start kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-odyssee-start.toon.md
V Sent_odyssee_start_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_odyssee_start_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_odyssee_start_fix FIXES Sent_odyssee_start_raw
E Sent_odyssee_start_raw FROM_SESSION Session_odyssee_start
E Sent_odyssee_start_fix FROM_SESSION Session_odyssee_start

# ingest-session 2026-09-18T16:06:10Z was-soll-ich-jetzt-machen lang=de
V Session_was_soll_ich_jetzt_machen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-was-soll-ich-jetzt-machen.toon.md
V Sent_was_soll_ich_jetzt_machen_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_was_soll_ich_jetzt_machen_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_was_soll_ich_jetzt_machen_fix FIXES Sent_was_soll_ich_jetzt_machen_raw
E Sent_was_soll_ich_jetzt_machen_raw FROM_SESSION Session_was_soll_ich_jetzt_machen
E Sent_was_soll_ich_jetzt_machen_fix FROM_SESSION Session_was_soll_ich_jetzt_machen

# ingest-session 2026-09-18T16:11:49Z konnektor-fusion-runde-1 lang=de
V Session_konnektor_fusion_runde_1 kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-konnektor-fusion-runde-1.toon.md
V Sent_konnektor_fusion_runde_1_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_konnektor_fusion_runde_1_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_konnektor_fusion_runde_1_fix FIXES Sent_konnektor_fusion_runde_1_raw
E Sent_konnektor_fusion_runde_1_raw FROM_SESSION Session_konnektor_fusion_runde_1
E Sent_konnektor_fusion_runde_1_fix FROM_SESSION Session_konnektor_fusion_runde_1

# ingest-session 2026-09-18T16:22:31Z agentcore-probe-stimme lang=de
V Session_agentcore_probe_stimme kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-agentcore-probe-stimme.toon.md
V Sent_agentcore_probe_stimme_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_agentcore_probe_stimme_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_agentcore_probe_stimme_fix FIXES Sent_agentcore_probe_stimme_raw
E Sent_agentcore_probe_stimme_raw FROM_SESSION Session_agentcore_probe_stimme
E Sent_agentcore_probe_stimme_fix FROM_SESSION Session_agentcore_probe_stimme

# ingest-session 2026-09-18T16:27:09Z eskalationsregel-fehlerwissen lang=de
V Session_eskalationsregel_fehlerwissen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-eskalationsregel-fehlerwissen.toon.md
V Sent_eskalationsregel_fehlerwissen_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_eskalationsregel_fehlerwissen_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_eskalationsregel_fehlerwissen_fix FIXES Sent_eskalationsregel_fehlerwissen_raw
E Sent_eskalationsregel_fehlerwissen_raw FROM_SESSION Session_eskalationsregel_fehlerwissen
E Sent_eskalationsregel_fehlerwissen_fix FROM_SESSION Session_eskalationsregel_fehlerwissen

# ingest-session 2026-09-18T16:30:07Z eskalationsdomaenen-ki-software-mathe lang=de
V Session_eskalationsdomaenen_ki_software_mathe kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-eskalationsdomaenen-ki-software-mathe.toon.md
V Sent_eskalationsdomaenen_ki_software_mathe_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_eskalationsdomaenen_ki_software_mathe_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_eskalationsdomaenen_ki_software_mathe_fix FIXES Sent_eskalationsdomaenen_ki_software_mathe_raw
E Sent_eskalationsdomaenen_ki_software_mathe_raw FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe
E Sent_eskalationsdomaenen_ki_software_mathe_fix FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe

# ingest-session 2026-09-18T16:32:11Z agentcore-fortfahren-mit lang=de
V Session_agentcore_fortfahren_mit kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-agentcore-fortfahren-mit.toon.md
V Sent_agentcore_fortfahren_mit_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_agentcore_fortfahren_mit_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_agentcore_fortfahren_mit_fix FIXES Sent_agentcore_fortfahren_mit_raw
E Sent_agentcore_fortfahren_mit_raw FROM_SESSION Session_agentcore_fortfahren_mit
E Sent_agentcore_fortfahren_mit_fix FROM_SESSION Session_agentcore_fortfahren_mit

# ingest-session 2026-09-18T16:47:47Z microvm-tiefer-eintauchen lang=de
V Session_microvm_tiefer_eintauchen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-microvm-tiefer-eintauchen.toon.md
V Sent_microvm_tiefer_eintauchen_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_microvm_tiefer_eintauchen_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_microvm_tiefer_eintauchen_fix FIXES Sent_microvm_tiefer_eintauchen_raw
E Sent_microvm_tiefer_eintauchen_raw FROM_SESSION Session_microvm_tiefer_eintauchen
E Sent_microvm_tiefer_eintauchen_fix FROM_SESSION Session_microvm_tiefer_eintauchen

# ingest-session 2026-09-18T16:56:12Z chaboo-mobile-toiletten lang=de
V Session_chaboo_mobile_toiletten kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-chaboo-mobile-toiletten.toon.md
V Sent_chaboo_mobile_toiletten_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_chaboo_mobile_toiletten_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_chaboo_mobile_toiletten_fix FIXES Sent_chaboo_mobile_toiletten_raw
E Sent_chaboo_mobile_toiletten_raw FROM_SESSION Session_chaboo_mobile_toiletten
E Sent_chaboo_mobile_toiletten_fix FROM_SESSION Session_chaboo_mobile_toiletten

# ingest-session 2026-09-18T17:09:17Z marken-dass-antwort lang=de
V Session_marken_dass_antwort kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-marken-dass-antwort.toon.md
V Sent_marken_dass_antwort_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_marken_dass_antwort_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_marken_dass_antwort_fix FIXES Sent_marken_dass_antwort_raw
E Sent_marken_dass_antwort_raw FROM_SESSION Session_marken_dass_antwort
E Sent_marken_dass_antwort_fix FROM_SESSION Session_marken_dass_antwort

# ingest-session 2026-09-18T17:24:22Z ss-pflicht-nicht-optional lang=de
V Session_ss_pflicht_nicht_optional kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-ss-pflicht-nicht-optional.toon.md
V Sent_ss_pflicht_nicht_optional_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_ss_pflicht_nicht_optional_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_ss_pflicht_nicht_optional_fix FIXES Sent_ss_pflicht_nicht_optional_raw
E Sent_ss_pflicht_nicht_optional_raw FROM_SESSION Session_ss_pflicht_nicht_optional
E Sent_ss_pflicht_nicht_optional_fix FROM_SESSION Session_ss_pflicht_nicht_optional

# ingest-session 2026-09-18T17:37:54Z gericht-fettig-videos-plan lang=de
V Session_gericht_fettig_videos_plan kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gericht-fettig-videos-plan.toon.md
V Sent_gericht_fettig_videos_plan_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_gericht_fettig_videos_plan_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_gericht_fettig_videos_plan_fix FIXES Sent_gericht_fettig_videos_plan_raw
E Sent_gericht_fettig_videos_plan_raw FROM_SESSION Session_gericht_fettig_videos_plan
E Sent_gericht_fettig_videos_plan_fix FROM_SESSION Session_gericht_fettig_videos_plan

# ingest-session 2026-09-18T17:43:18Z firecracker-kernel-modell lang=de
V Session_firecracker_kernel_modell kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-firecracker-kernel-modell.toon.md
V Sent_firecracker_kernel_modell_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_firecracker_kernel_modell_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_firecracker_kernel_modell_fix FIXES Sent_firecracker_kernel_modell_raw
E Sent_firecracker_kernel_modell_raw FROM_SESSION Session_firecracker_kernel_modell
E Sent_firecracker_kernel_modell_fix FROM_SESSION Session_firecracker_kernel_modell

# ingest-session 2026-09-18T17:54:10Z gehirnausdauer-leichte-runde lang=de
V Session_gehirnausdauer_leichte_runde kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gehirnausdauer-leichte-runde.toon.md
V Sent_gehirnausdauer_leichte_runde_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_gehirnausdauer_leichte_runde_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_gehirnausdauer_leichte_runde_fix FIXES Sent_gehirnausdauer_leichte_runde_raw
E Sent_gehirnausdauer_leichte_runde_raw FROM_SESSION Session_gehirnausdauer_leichte_runde
E Sent_gehirnausdauer_leichte_runde_fix FROM_SESSION Session_gehirnausdauer_leichte_runde

# ingest-session 2026-09-18T17:56:44Z on-passe-au-francais lang=fr
V Session_on_passe_au_francais kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-on-passe-au-francais.toon.md
V Sent_on_passe_au_francais_raw kind=sentence date=2026-09-18 lang=fr role=raw
V Sent_on_passe_au_francais_fix kind=sentence date=2026-09-18 lang=fr role=corrected
E Sent_on_passe_au_francais_fix FIXES Sent_on_passe_au_francais_raw
E Sent_on_passe_au_francais_raw FROM_SESSION Session_on_passe_au_francais
E Sent_on_passe_au_francais_fix FROM_SESSION Session_on_passe_au_francais

# ingest-session 2026-09-18T18:07:20Z energie-ohne-denkkraft-mathe-spass lang=fr
V Session_energie_ohne_denkkraft_mathe_spass kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-energie-ohne-denkkraft-mathe-spass.toon.md
V Sent_energie_ohne_denkkraft_mathe_spass_raw kind=sentence date=2026-09-18 lang=fr role=raw
V Sent_energie_ohne_denkkraft_mathe_spass_fix kind=sentence date=2026-09-18 lang=fr role=corrected
E Sent_energie_ohne_denkkraft_mathe_spass_fix FIXES Sent_energie_ohne_denkkraft_mathe_spass_raw
E Sent_energie_ohne_denkkraft_mathe_spass_raw FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass
E Sent_energie_ohne_denkkraft_mathe_spass_fix FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass

# ingest-session 2026-09-18T18:16:25Z total-francais-astrophysique lang=fr
V Session_total_francais_astrophysique kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-total-francais-astrophysique.toon.md
V Sent_total_francais_astrophysique_raw kind=sentence date=2026-09-18 lang=fr role=raw
V Sent_total_francais_astrophysique_fix kind=sentence date=2026-09-18 lang=fr role=corrected
E Sent_total_francais_astrophysique_fix FIXES Sent_total_francais_astrophysique_raw
E Sent_total_francais_astrophysique_raw FROM_SESSION Session_total_francais_astrophysique
E Sent_total_francais_astrophysique_fix FROM_SESSION Session_total_francais_astrophysique

# ingest-session 2026-09-18T18:30:41Z courbatures-cerveau lang=fr
V Session_courbatures_cerveau kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-courbatures-cerveau.toon.md
V Sent_courbatures_cerveau_raw kind=sentence date=2026-09-18 lang=fr role=raw
V Sent_courbatures_cerveau_fix kind=sentence date=2026-09-18 lang=fr role=corrected
E Sent_courbatures_cerveau_fix FIXES Sent_courbatures_cerveau_raw
E Sent_courbatures_cerveau_raw FROM_SESSION Session_courbatures_cerveau
E Sent_courbatures_cerveau_fix FROM_SESSION Session_courbatures_cerveau

# ingest-session 2026-09-18T18:38:10Z enfin-vietnamien lang=fr
V Session_enfin_vietnamien kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-enfin-vietnamien.toon.md
V Sent_enfin_vietnamien_raw kind=sentence date=2026-09-18 lang=fr role=raw
V Sent_enfin_vietnamien_fix kind=sentence date=2026-09-18 lang=fr role=corrected
E Sent_enfin_vietnamien_fix FIXES Sent_enfin_vietnamien_raw
E Sent_enfin_vietnamien_raw FROM_SESSION Session_enfin_vietnamien
E Sent_enfin_vietnamien_fix FROM_SESSION Session_enfin_vietnamien

# ingest-session 2026-09-18T18:46:45Z bia-keine-ahnung lang=fr
V Session_bia_keine_ahnung kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-bia-keine-ahnung.toon.md
V Sent_bia_keine_ahnung_raw kind=sentence date=2026-09-18 lang=fr role=raw
V Sent_bia_keine_ahnung_fix kind=sentence date=2026-09-18 lang=fr role=corrected
E Sent_bia_keine_ahnung_fix FIXES Sent_bia_keine_ahnung_raw
E Sent_bia_keine_ahnung_raw FROM_SESSION Session_bia_keine_ahnung
E Sent_bia_keine_ahnung_fix FROM_SESSION Session_bia_keine_ahnung

# ingest-session 2026-09-18T18:52:36Z tagesabschluss-pdf-latex lang=de
V Session_tagesabschluss_pdf_latex kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tagesabschluss-pdf-latex.toon.md
V Sent_tagesabschluss_pdf_latex_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_tagesabschluss_pdf_latex_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_tagesabschluss_pdf_latex_fix FIXES Sent_tagesabschluss_pdf_latex_raw
E Sent_tagesabschluss_pdf_latex_raw FROM_SESSION Session_tagesabschluss_pdf_latex
E Sent_tagesabschluss_pdf_latex_fix FROM_SESSION Session_tagesabschluss_pdf_latex

# ingest-session 2026-09-18T18:54:46Z pdf-hier-oeffnen lang=de
V Session_pdf_hier_oeffnen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-pdf-hier-oeffnen.toon.md
V Sent_pdf_hier_oeffnen_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_pdf_hier_oeffnen_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_pdf_hier_oeffnen_fix FIXES Sent_pdf_hier_oeffnen_raw
E Sent_pdf_hier_oeffnen_raw FROM_SESSION Session_pdf_hier_oeffnen
E Sent_pdf_hier_oeffnen_fix FROM_SESSION Session_pdf_hier_oeffnen

# ingest-session 2026-09-18T19:02:15Z gute-nacht-bonne-nuit lang=de
V Session_gute_nacht_bonne_nuit kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gute-nacht-bonne-nuit.toon.md
V Sent_gute_nacht_bonne_nuit_raw kind=sentence date=2026-09-18 lang=de role=raw
V Sent_gute_nacht_bonne_nuit_fix kind=sentence date=2026-09-18 lang=de role=corrected
E Sent_gute_nacht_bonne_nuit_fix FIXES Sent_gute_nacht_bonne_nuit_raw
E Sent_gute_nacht_bonne_nuit_raw FROM_SESSION Session_gute_nacht_bonne_nuit
E Sent_gute_nacht_bonne_nuit_fix FROM_SESSION Session_gute_nacht_bonne_nuit

# ingest-session 2026-09-19T10:25:57Z tag-starten lang=de
V Session_tag_starten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tag-starten.toon.md
V Sent_tag_starten_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_tag_starten_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_tag_starten_fix FIXES Sent_tag_starten_raw
E Sent_tag_starten_raw FROM_SESSION Session_tag_starten
E Sent_tag_starten_fix FROM_SESSION Session_tag_starten

# ingest-session 2026-09-19T10:32:42Z tag-fokus lang=de
V Session_tag_fokus kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tag-fokus.toon.md
V Sent_tag_fokus_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_tag_fokus_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_tag_fokus_fix FIXES Sent_tag_fokus_raw
E Sent_tag_fokus_raw FROM_SESSION Session_tag_fokus
E Sent_tag_fokus_fix FROM_SESSION Session_tag_fokus

# ingest-session 2026-09-19T10:58:41Z kein-gym lang=de
V Session_kein_gym kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-kein-gym.toon.md
V Sent_kein_gym_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_kein_gym_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_kein_gym_fix FIXES Sent_kein_gym_raw
E Sent_kein_gym_raw FROM_SESSION Session_kein_gym
E Sent_kein_gym_fix FROM_SESSION Session_kein_gym

# ingest-session 2026-09-19T12:34:31Z odyssee-videos-start lang=de
V Session_odyssee_videos_start kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-odyssee-videos-start.toon.md
V Sent_odyssee_videos_start_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_odyssee_videos_start_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_odyssee_videos_start_fix FIXES Sent_odyssee_videos_start_raw
E Sent_odyssee_videos_start_raw FROM_SESSION Session_odyssee_videos_start
E Sent_odyssee_videos_start_fix FROM_SESSION Session_odyssee_videos_start

# ingest-session 2026-09-19T12:44:14Z news-job-skillfrage lang=de
V Session_news_job_skillfrage kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-news-job-skillfrage.toon.md
V Sent_news_job_skillfrage_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_news_job_skillfrage_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_news_job_skillfrage_fix FIXES Sent_news_job_skillfrage_raw
E Sent_news_job_skillfrage_raw FROM_SESSION Session_news_job_skillfrage
E Sent_news_job_skillfrage_fix FROM_SESSION Session_news_job_skillfrage

# ingest-session 2026-09-19T12:52:27Z tagesaufgaben-integrieren lang=de
V Session_tagesaufgaben_integrieren kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tagesaufgaben-integrieren.toon.md
V Sent_tagesaufgaben_integrieren_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_tagesaufgaben_integrieren_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_tagesaufgaben_integrieren_fix FIXES Sent_tagesaufgaben_integrieren_raw
E Sent_tagesaufgaben_integrieren_raw FROM_SESSION Session_tagesaufgaben_integrieren
E Sent_tagesaufgaben_integrieren_fix FROM_SESSION Session_tagesaufgaben_integrieren

# ingest-session 2026-09-19T12:54:41Z chat-auflisten lang=de
V Session_chat_auflisten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-chat-auflisten.toon.md
V Sent_chat_auflisten_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_chat_auflisten_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_chat_auflisten_fix FIXES Sent_chat_auflisten_raw
E Sent_chat_auflisten_raw FROM_SESSION Session_chat_auflisten
E Sent_chat_auflisten_fix FROM_SESSION Session_chat_auflisten

# ingest-session 2026-09-19T13:01:24Z antwort-zu-kurz lang=de
V Session_antwort_zu_kurz kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-antwort-zu-kurz.toon.md
V Sent_antwort_zu_kurz_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_antwort_zu_kurz_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_antwort_zu_kurz_fix FIXES Sent_antwort_zu_kurz_raw
E Sent_antwort_zu_kurz_raw FROM_SESSION Session_antwort_zu_kurz
E Sent_antwort_zu_kurz_fix FROM_SESSION Session_antwort_zu_kurz

# ingest-session 2026-09-19T13:07:27Z plain-antwort lang=de
V Session_plain_antwort kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-plain-antwort.toon.md
V Sent_plain_antwort_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_plain_antwort_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_plain_antwort_fix FIXES Sent_plain_antwort_raw
E Sent_plain_antwort_raw FROM_SESSION Session_plain_antwort
E Sent_plain_antwort_fix FROM_SESSION Session_plain_antwort

# ingest-session 2026-09-19T13:10:35Z alles-im-chat lang=de
V Session_alles_im_chat kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-alles-im-chat.toon.md
V Sent_alles_im_chat_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_alles_im_chat_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_alles_im_chat_fix FIXES Sent_alles_im_chat_raw
E Sent_alles_im_chat_raw FROM_SESSION Session_alles_im_chat
E Sent_alles_im_chat_fix FROM_SESSION Session_alles_im_chat

# ingest-session 2026-09-19T13:16:10Z nie-sehen lang=de
V Session_nie_sehen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-nie-sehen.toon.md
V Sent_nie_sehen_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_nie_sehen_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_nie_sehen_fix FIXES Sent_nie_sehen_raw
E Sent_nie_sehen_raw FROM_SESSION Session_nie_sehen
E Sent_nie_sehen_fix FROM_SESSION Session_nie_sehen

# ingest-session 2026-09-19T13:17:28Z block-a-start lang=de
V Session_block_a_start kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-block-a-start.toon.md
V Sent_block_a_start_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_block_a_start_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_block_a_start_fix FIXES Sent_block_a_start_raw
E Sent_block_a_start_raw FROM_SESSION Session_block_a_start
E Sent_block_a_start_fix FROM_SESSION Session_block_a_start

# ingest-session 2026-09-19T13:20:28Z anweisungen lang=de
V Session_anweisungen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-anweisungen.toon.md
V Sent_anweisungen_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_anweisungen_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_anweisungen_fix FIXES Sent_anweisungen_raw
E Sent_anweisungen_raw FROM_SESSION Session_anweisungen
E Sent_anweisungen_fix FROM_SESSION Session_anweisungen

# ingest-session 2026-09-19T13:23:16Z chat-sichtbarkeit lang=de
V Session_chat_sichtbarkeit kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-chat-sichtbarkeit.toon.md
V Sent_chat_sichtbarkeit_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_chat_sichtbarkeit_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_chat_sichtbarkeit_fix FIXES Sent_chat_sichtbarkeit_raw
E Sent_chat_sichtbarkeit_raw FROM_SESSION Session_chat_sichtbarkeit
E Sent_chat_sichtbarkeit_fix FROM_SESSION Session_chat_sichtbarkeit

# ingest-session 2026-09-19T13:25:57Z self-contained-context lang=de
V Session_self_contained_context kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-self-contained-context.toon.md
V Sent_self_contained_context_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_self_contained_context_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_self_contained_context_fix FIXES Sent_self_contained_context_raw
E Sent_self_contained_context_raw FROM_SESSION Session_self_contained_context
E Sent_self_contained_context_fix FROM_SESSION Session_self_contained_context

# ingest-session 2026-09-19T13:29:29Z browser-dw lang=de
V Session_browser_dw kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-browser-dw.toon.md
V Sent_browser_dw_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_browser_dw_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_browser_dw_fix FIXES Sent_browser_dw_raw
E Sent_browser_dw_raw FROM_SESSION Session_browser_dw
E Sent_browser_dw_fix FROM_SESSION Session_browser_dw

# ingest-session 2026-09-19T13:31:03Z norm-langsamkeit lang=de
V Session_norm_langsamkeit kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-norm-langsamkeit.toon.md
V Sent_norm_langsamkeit_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_norm_langsamkeit_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_norm_langsamkeit_fix FIXES Sent_norm_langsamkeit_raw
E Sent_norm_langsamkeit_raw FROM_SESSION Session_norm_langsamkeit
E Sent_norm_langsamkeit_fix FROM_SESSION Session_norm_langsamkeit

# ingest-session 2026-09-19T13:34:15Z c1-hoerverstehen lang=de
V Session_c1_hoerverstehen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-c1-hoerverstehen.toon.md
V Sent_c1_hoerverstehen_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_c1_hoerverstehen_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_c1_hoerverstehen_fix FIXES Sent_c1_hoerverstehen_raw
E Sent_c1_hoerverstehen_raw FROM_SESSION Session_c1_hoerverstehen
E Sent_c1_hoerverstehen_fix FROM_SESSION Session_c1_hoerverstehen

# ingest-session 2026-09-19T13:36:21Z fest-zu-laut lang=de
V Session_fest_zu_laut kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-fest-zu-laut.toon.md
V Sent_fest_zu_laut_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_fest_zu_laut_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_fest_zu_laut_fix FIXES Sent_fest_zu_laut_raw
E Sent_fest_zu_laut_raw FROM_SESSION Session_fest_zu_laut
E Sent_fest_zu_laut_fix FROM_SESSION Session_fest_zu_laut

# ingest-session 2026-09-19T13:39:25Z alternative-jetzt lang=de
V Session_alternative_jetzt kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-alternative-jetzt.toon.md
V Sent_alternative_jetzt_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_alternative_jetzt_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_alternative_jetzt_fix FIXES Sent_alternative_jetzt_raw
E Sent_alternative_jetzt_raw FROM_SESSION Session_alternative_jetzt
E Sent_alternative_jetzt_fix FROM_SESSION Session_alternative_jetzt

# ingest-session 2026-09-19T13:49:50Z pause-eine lang=de
V Session_pause_eine kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-pause-eine.toon.md
V Sent_pause_eine_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_pause_eine_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_pause_eine_fix FIXES Sent_pause_eine_raw
E Sent_pause_eine_raw FROM_SESSION Session_pause_eine
E Sent_pause_eine_fix FROM_SESSION Session_pause_eine

# ingest-session 2026-09-19T13:54:37Z pause-minuten lang=de
V Session_pause_minuten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-pause-minuten.toon.md
V Sent_pause_minuten_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_pause_minuten_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_pause_minuten_fix FIXES Sent_pause_minuten_raw
E Sent_pause_minuten_raw FROM_SESSION Session_pause_minuten
E Sent_pause_minuten_fix FROM_SESSION Session_pause_minuten

# ingest-session 2026-09-19T14:02:01Z axiome-system lang=de
V Session_axiome_system kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-axiome-system.toon.md
V Sent_axiome_system_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_axiome_system_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_axiome_system_fix FIXES Sent_axiome_system_raw
E Sent_axiome_system_raw FROM_SESSION Session_axiome_system
E Sent_axiome_system_fix FROM_SESSION Session_axiome_system

# ingest-session 2026-09-19T14:05:13Z axiome-system-voll lang=de
V Session_axiome_system_voll kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-axiome-system-voll.toon.md
V Sent_axiome_system_voll_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_axiome_system_voll_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_axiome_system_voll_fix FIXES Sent_axiome_system_voll_raw
E Sent_axiome_system_voll_raw FROM_SESSION Session_axiome_system_voll
E Sent_axiome_system_voll_fix FROM_SESSION Session_axiome_system_voll

# ingest-session 2026-09-19T14:10:00Z mathe-ziel-astro lang=de
V Session_mathe_ziel_astro kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-mathe-ziel-astro.toon.md
V Sent_mathe_ziel_astro_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_mathe_ziel_astro_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_mathe_ziel_astro_fix FIXES Sent_mathe_ziel_astro_raw
E Sent_mathe_ziel_astro_raw FROM_SESSION Session_mathe_ziel_astro
E Sent_mathe_ziel_astro_fix FROM_SESSION Session_mathe_ziel_astro

# ingest-session 2026-09-19T14:34:34Z zweite-lesung-akku lang=de
V Session_zweite_lesung_akku kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-zweite-lesung-akku.toon.md
V Sent_zweite_lesung_akku_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_zweite_lesung_akku_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_zweite_lesung_akku_fix FIXES Sent_zweite_lesung_akku_raw
E Sent_zweite_lesung_akku_raw FROM_SESSION Session_zweite_lesung_akku
E Sent_zweite_lesung_akku_fix FROM_SESSION Session_zweite_lesung_akku

# ingest-session 2026-09-19T14:37:17Z dsb-couverture-cerveau lang=de
V Session_dsb_couverture_cerveau kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dsb-couverture-cerveau.toon.md
V Sent_dsb_couverture_cerveau_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_dsb_couverture_cerveau_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_dsb_couverture_cerveau_fix FIXES Sent_dsb_couverture_cerveau_raw
E Sent_dsb_couverture_cerveau_raw FROM_SESSION Session_dsb_couverture_cerveau
E Sent_dsb_couverture_cerveau_fix FROM_SESSION Session_dsb_couverture_cerveau

# ingest-session 2026-09-19T14:42:29Z dsb-neudefinition lang=de
V Session_dsb_neudefinition kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dsb-neudefinition.toon.md
V Sent_dsb_neudefinition_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_dsb_neudefinition_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_dsb_neudefinition_fix FIXES Sent_dsb_neudefinition_raw
E Sent_dsb_neudefinition_raw FROM_SESSION Session_dsb_neudefinition
E Sent_dsb_neudefinition_fix FROM_SESSION Session_dsb_neudefinition

# ingest-session 2026-09-19T14:48:12Z dns-zurueck-lesen lang=de
V Session_dns_zurueck_lesen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dns-zurueck-lesen.toon.md
V Sent_dns_zurueck_lesen_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_dns_zurueck_lesen_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_dns_zurueck_lesen_fix FIXES Sent_dns_zurueck_lesen_raw
E Sent_dns_zurueck_lesen_raw FROM_SESSION Session_dns_zurueck_lesen
E Sent_dns_zurueck_lesen_fix FROM_SESSION Session_dns_zurueck_lesen

# ingest-session 2026-09-19T15:12:20Z news-url-verloren lang=de
V Session_news_url_verloren kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-news-url-verloren.toon.md
V Sent_news_url_verloren_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_news_url_verloren_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_news_url_verloren_fix FIXES Sent_news_url_verloren_raw
E Sent_news_url_verloren_raw FROM_SESSION Session_news_url_verloren
E Sent_news_url_verloren_fix FROM_SESSION Session_news_url_verloren

# ingest-session 2026-09-19T15:14:03Z oben-existiert-nicht lang=de
V Session_oben_existiert_nicht kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-oben-existiert-nicht.toon.md
V Sent_oben_existiert_nicht_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_oben_existiert_nicht_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_oben_existiert_nicht_fix FIXES Sent_oben_existiert_nicht_raw
E Sent_oben_existiert_nicht_raw FROM_SESSION Session_oben_existiert_nicht
E Sent_oben_existiert_nicht_fix FROM_SESSION Session_oben_existiert_nicht

# ingest-session 2026-09-19T16:01:44Z zusammenfassung-politik lang=de
V Session_zusammenfassung_politik kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-zusammenfassung-politik.toon.md
V Sent_zusammenfassung_politik_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_zusammenfassung_politik_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_zusammenfassung_politik_fix FIXES Sent_zusammenfassung_politik_raw
E Sent_zusammenfassung_politik_raw FROM_SESSION Session_zusammenfassung_politik
E Sent_zusammenfassung_politik_fix FROM_SESSION Session_zusammenfassung_politik

# ingest-session 2026-09-19T16:17:17Z exemplar-zusammenfassung lang=de
V Session_exemplar_zusammenfassung kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-exemplar-zusammenfassung.toon.md
V Sent_exemplar_zusammenfassung_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_exemplar_zusammenfassung_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_exemplar_zusammenfassung_fix FIXES Sent_exemplar_zusammenfassung_raw
E Sent_exemplar_zusammenfassung_raw FROM_SESSION Session_exemplar_zusammenfassung
E Sent_exemplar_zusammenfassung_fix FROM_SESSION Session_exemplar_zusammenfassung

# ingest-session 2026-09-19T16:31:06Z wortschatz-warten lang=de
V Session_wortschatz_warten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-wortschatz-warten.toon.md
V Sent_wortschatz_warten_raw kind=sentence date=2026-09-19 lang=de role=raw
V Sent_wortschatz_warten_fix kind=sentence date=2026-09-19 lang=de role=corrected
E Sent_wortschatz_warten_fix FIXES Sent_wortschatz_warten_raw
E Sent_wortschatz_warten_raw FROM_SESSION Session_wortschatz_warten
E Sent_wortschatz_warten_fix FROM_SESSION Session_wortschatz_warten

# ingest-session 2026-09-20T22:26:50Z setze-die-shenyou-fort lang=de
V Session_setze_die_shenyou_fort kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-setze-die-shenyou-fort.toon.md
V Sent_setze_die_shenyou_fort_raw kind=sentence date=2026-09-21 lang=de role=raw
V Sent_setze_die_shenyou_fort_fix kind=sentence date=2026-09-21 lang=de role=corrected
E Sent_setze_die_shenyou_fort_fix FIXES Sent_setze_die_shenyou_fort_raw
E Sent_setze_die_shenyou_fort_raw FROM_SESSION Session_setze_die_shenyou_fort
E Sent_setze_die_shenyou_fort_fix FROM_SESSION Session_setze_die_shenyou_fort

# ingest-session 2026-09-21T19:07:25Z wie-macht-man-das-noch-mal lang=de
V Session_wie_macht_man_das_noch_mal kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-wie-macht-man-das-noch-mal.toon.md
V Sent_wie_macht_man_das_noch_mal_raw kind=sentence date=2026-09-21 lang=de role=raw
V Sent_wie_macht_man_das_noch_mal_fix kind=sentence date=2026-09-21 lang=de role=corrected
E Sent_wie_macht_man_das_noch_mal_fix FIXES Sent_wie_macht_man_das_noch_mal_raw
E Sent_wie_macht_man_das_noch_mal_raw FROM_SESSION Session_wie_macht_man_das_noch_mal
E Sent_wie_macht_man_das_noch_mal_fix FROM_SESSION Session_wie_macht_man_das_noch_mal

# ingest-session 2026-09-21T19:20:23Z die-dateien-sind-bereit lang=de
V Session_die_dateien_sind_bereit kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-die-dateien-sind-bereit.toon.md
V Sent_die_dateien_sind_bereit_raw kind=sentence date=2026-09-21 lang=de role=raw
V Sent_die_dateien_sind_bereit_fix kind=sentence date=2026-09-21 lang=de role=corrected
E Sent_die_dateien_sind_bereit_fix FIXES Sent_die_dateien_sind_bereit_raw
E Sent_die_dateien_sind_bereit_raw FROM_SESSION Session_die_dateien_sind_bereit
E Sent_die_dateien_sind_bereit_fix FROM_SESSION Session_die_dateien_sind_bereit

# ingest-session 2026-09-21T19:32:47Z ersetze-huaqiang-durch-das-pummelige lang=de
V Session_ersetze_huaqiang_durch_das_pummelige kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-ersetze-huaqiang-durch-das-pummelige.toon.md
V Sent_ersetze_huaqiang_durch_das_pummelige_raw kind=sentence date=2026-09-21 lang=de role=raw
V Sent_ersetze_huaqiang_durch_das_pummelige_fix kind=sentence date=2026-09-21 lang=de role=corrected
E Sent_ersetze_huaqiang_durch_das_pummelige_fix FIXES Sent_ersetze_huaqiang_durch_das_pummelige_raw
E Sent_ersetze_huaqiang_durch_das_pummelige_raw FROM_SESSION Session_ersetze_huaqiang_durch_das_pummelige
E Sent_ersetze_huaqiang_durch_das_pummelige_fix FROM_SESSION Session_ersetze_huaqiang_durch_das_pummelige

# ingest-session 2026-09-22T09:05:32Z nimm-die-shenyou-in-den-takt lang=de
V Session_nimm_die_shenyou_in_den_takt kind=session date=2026-09-22 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-22-nimm-die-shenyou-in-den-takt.toon.md
V Sent_nimm_die_shenyou_in_den_takt_raw kind=sentence date=2026-09-22 lang=de role=raw
V Sent_nimm_die_shenyou_in_den_takt_fix kind=sentence date=2026-09-22 lang=de role=corrected
E Sent_nimm_die_shenyou_in_den_takt_fix FIXES Sent_nimm_die_shenyou_in_den_takt_raw
E Sent_nimm_die_shenyou_in_den_takt_raw FROM_SESSION Session_nimm_die_shenyou_in_den_takt
E Sent_nimm_die_shenyou_in_den_takt_fix FROM_SESSION Session_nimm_die_shenyou_in_den_takt

# ingest-session 2026-09-22T10:23:13Z die-gesangsstimme-ersetzen lang=de
V Session_die_gesangsstimme_ersetzen kind=session date=2026-09-22 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-22-die-gesangsstimme-ersetzen.toon.md
V Sent_die_gesangsstimme_ersetzen_raw kind=sentence date=2026-09-22 lang=de role=raw
V Sent_die_gesangsstimme_ersetzen_fix kind=sentence date=2026-09-22 lang=de role=corrected
E Sent_die_gesangsstimme_ersetzen_fix FIXES Sent_die_gesangsstimme_ersetzen_raw
E Sent_die_gesangsstimme_ersetzen_raw FROM_SESSION Session_die_gesangsstimme_ersetzen
E Sent_die_gesangsstimme_ersetzen_fix FROM_SESSION Session_die_gesangsstimme_ersetzen

# ingest-session 2026-09-23T14:08:56Z raeume-tmp-auf lang=de
V Session_raeume_tmp_auf kind=session date=2026-09-23 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-23-raeume-tmp-auf.toon.md
V Sent_raeume_tmp_auf_raw kind=sentence date=2026-09-23 lang=de role=raw
V Sent_raeume_tmp_auf_fix kind=sentence date=2026-09-23 lang=de role=corrected
E Sent_raeume_tmp_auf_fix FIXES Sent_raeume_tmp_auf_raw
E Sent_raeume_tmp_auf_raw FROM_SESSION Session_raeume_tmp_auf
E Sent_raeume_tmp_auf_fix FROM_SESSION Session_raeume_tmp_auf

# ingest-session 2026-09-23T14:13:29Z zuerst-fangen-wir-an lang=de
V Session_zuerst_fangen_wir_an kind=session date=2026-09-23 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-23-zuerst-fangen-wir-an.toon.md
V Sent_zuerst_fangen_wir_an_raw kind=sentence date=2026-09-23 lang=de role=raw
V Sent_zuerst_fangen_wir_an_fix kind=sentence date=2026-09-23 lang=de role=corrected
E Sent_zuerst_fangen_wir_an_fix FIXES Sent_zuerst_fangen_wir_an_raw
E Sent_zuerst_fangen_wir_an_raw FROM_SESSION Session_zuerst_fangen_wir_an
E Sent_zuerst_fangen_wir_an_fix FROM_SESSION Session_zuerst_fangen_wir_an

# ingest-session 2026-09-24T11:54:36Z mit-dem-neuen-tag lang=de
V Session_mit_dem_neuen_tag kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-mit-dem-neuen-tag.toon.md
V Sent_mit_dem_neuen_tag_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_mit_dem_neuen_tag_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_mit_dem_neuen_tag_fix FIXES Sent_mit_dem_neuen_tag_raw
E Sent_mit_dem_neuen_tag_raw FROM_SESSION Session_mit_dem_neuen_tag
E Sent_mit_dem_neuen_tag_fix FROM_SESSION Session_mit_dem_neuen_tag

# ingest-session 2026-09-24T11:56:59Z die-3d-hall-anschauen lang=de
V Session_die_3d_hall_anschauen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-die-3d-hall-anschauen.toon.md
V Sent_die_3d_hall_anschauen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_die_3d_hall_anschauen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_die_3d_hall_anschauen_fix FIXES Sent_die_3d_hall_anschauen_raw
E Sent_die_3d_hall_anschauen_raw FROM_SESSION Session_die_3d_hall_anschauen
E Sent_die_3d_hall_anschauen_fix FROM_SESSION Session_die_3d_hall_anschauen

# ingest-session 2026-09-24T12:05:01Z in-meiner-linken-skapula lang=de
V Session_in_meiner_linken_skapula kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-meiner-linken-skapula.toon.md
V Sent_in_meiner_linken_skapula_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_in_meiner_linken_skapula_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_in_meiner_linken_skapula_fix FIXES Sent_in_meiner_linken_skapula_raw
E Sent_in_meiner_linken_skapula_raw FROM_SESSION Session_in_meiner_linken_skapula
E Sent_in_meiner_linken_skapula_fix FROM_SESSION Session_in_meiner_linken_skapula

# ingest-session 2026-09-24T12:08:47Z warum-sind-apfelessig-und-betain lang=de
V Session_warum_sind_apfelessig_und_betain kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-warum-sind-apfelessig-und-betain.toon.md
V Sent_warum_sind_apfelessig_und_betain_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_warum_sind_apfelessig_und_betain_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_warum_sind_apfelessig_und_betain_fix FIXES Sent_warum_sind_apfelessig_und_betain_raw
E Sent_warum_sind_apfelessig_und_betain_raw FROM_SESSION Session_warum_sind_apfelessig_und_betain
E Sent_warum_sind_apfelessig_und_betain_fix FROM_SESSION Session_warum_sind_apfelessig_und_betain

# ingest-session 2026-09-24T12:12:28Z in-den-privaten-bereich lang=de
V Session_in_den_privaten_bereich kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-den-privaten-bereich.toon.md
V Sent_in_den_privaten_bereich_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_in_den_privaten_bereich_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_in_den_privaten_bereich_fix FIXES Sent_in_den_privaten_bereich_raw
E Sent_in_den_privaten_bereich_raw FROM_SESSION Session_in_den_privaten_bereich
E Sent_in_den_privaten_bereich_fix FROM_SESSION Session_in_den_privaten_bereich

# ingest-session 2026-09-24T12:16:31Z sondern-von-einem-wackelnden lang=de
V Session_sondern_von_einem_wackelnden kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-sondern-von-einem-wackelnden.toon.md
V Sent_sondern_von_einem_wackelnden_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_sondern_von_einem_wackelnden_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_sondern_von_einem_wackelnden_fix FIXES Sent_sondern_von_einem_wackelnden_raw
E Sent_sondern_von_einem_wackelnden_raw FROM_SESSION Session_sondern_von_einem_wackelnden
E Sent_sondern_von_einem_wackelnden_fix FROM_SESSION Session_sondern_von_einem_wackelnden

# ingest-session 2026-09-24T12:18:16Z kein-problem-mit-dem-weisheitszahn lang=de
V Session_kein_problem_mit_dem_weisheitszahn kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-kein-problem-mit-dem-weisheitszahn.toon.md
V Sent_kein_problem_mit_dem_weisheitszahn_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_kein_problem_mit_dem_weisheitszahn_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_kein_problem_mit_dem_weisheitszahn_fix FIXES Sent_kein_problem_mit_dem_weisheitszahn_raw
E Sent_kein_problem_mit_dem_weisheitszahn_raw FROM_SESSION Session_kein_problem_mit_dem_weisheitszahn
E Sent_kein_problem_mit_dem_weisheitszahn_fix FROM_SESSION Session_kein_problem_mit_dem_weisheitszahn

# ingest-session 2026-09-24T12:20:18Z meine-gesamten-emails lang=de
V Session_meine_gesamten_emails kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-meine-gesamten-emails.toon.md
V Sent_meine_gesamten_emails_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_meine_gesamten_emails_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_meine_gesamten_emails_fix FIXES Sent_meine_gesamten_emails_raw
E Sent_meine_gesamten_emails_raw FROM_SESSION Session_meine_gesamten_emails
E Sent_meine_gesamten_emails_fix FROM_SESSION Session_meine_gesamten_emails

# ingest-session 2026-09-24T12:23:24Z nachrichten-aus-der-ganzen-welt lang=de
V Session_nachrichten_aus_der_ganzen_welt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nachrichten-aus-der-ganzen-welt.toon.md
V Sent_nachrichten_aus_der_ganzen_welt_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_nachrichten_aus_der_ganzen_welt_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_nachrichten_aus_der_ganzen_welt_fix FIXES Sent_nachrichten_aus_der_ganzen_welt_raw
E Sent_nachrichten_aus_der_ganzen_welt_raw FROM_SESSION Session_nachrichten_aus_der_ganzen_welt
E Sent_nachrichten_aus_der_ganzen_welt_fix FROM_SESSION Session_nachrichten_aus_der_ganzen_welt

# ingest-session 2026-09-24T12:25:20Z nicht-so-langsam-beim-hoerverstehen lang=de
V Session_nicht_so_langsam_beim_hoerverstehen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nicht-so-langsam-beim-hoerverstehen.toon.md
V Sent_nicht_so_langsam_beim_hoerverstehen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_nicht_so_langsam_beim_hoerverstehen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_nicht_so_langsam_beim_hoerverstehen_fix FIXES Sent_nicht_so_langsam_beim_hoerverstehen_raw
E Sent_nicht_so_langsam_beim_hoerverstehen_raw FROM_SESSION Session_nicht_so_langsam_beim_hoerverstehen
E Sent_nicht_so_langsam_beim_hoerverstehen_fix FROM_SESSION Session_nicht_so_langsam_beim_hoerverstehen

# ingest-session 2026-09-24T12:31:11Z auswirkung-auf-meine-gesundheit lang=de
V Session_auswirkung_auf_meine_gesundheit kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-auswirkung-auf-meine-gesundheit.toon.md
V Sent_auswirkung_auf_meine_gesundheit_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_auswirkung_auf_meine_gesundheit_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_auswirkung_auf_meine_gesundheit_fix FIXES Sent_auswirkung_auf_meine_gesundheit_raw
E Sent_auswirkung_auf_meine_gesundheit_raw FROM_SESSION Session_auswirkung_auf_meine_gesundheit
E Sent_auswirkung_auf_meine_gesundheit_fix FROM_SESSION Session_auswirkung_auf_meine_gesundheit

# ingest-session 2026-09-24T12:36:05Z strengen-sie-sich-an lang=de
V Session_strengen_sie_sich_an kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-strengen-sie-sich-an.toon.md
V Sent_strengen_sie_sich_an_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_strengen_sie_sich_an_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_strengen_sie_sich_an_fix FIXES Sent_strengen_sie_sich_an_raw
E Sent_strengen_sie_sich_an_raw FROM_SESSION Session_strengen_sie_sich_an
E Sent_strengen_sie_sich_an_fix FROM_SESSION Session_strengen_sie_sich_an

# ingest-session 2026-09-24T12:46:32Z die-entropie-ein-bisschen-mehr lang=de
V Session_die_entropie_ein_bisschen_mehr kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-die-entropie-ein-bisschen-mehr.toon.md
V Sent_die_entropie_ein_bisschen_mehr_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_die_entropie_ein_bisschen_mehr_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_die_entropie_ein_bisschen_mehr_fix FIXES Sent_die_entropie_ein_bisschen_mehr_raw
E Sent_die_entropie_ein_bisschen_mehr_raw FROM_SESSION Session_die_entropie_ein_bisschen_mehr
E Sent_die_entropie_ein_bisschen_mehr_fix FROM_SESSION Session_die_entropie_ein_bisschen_mehr

# ingest-session 2026-09-24T13:18:04Z eine-beilage-zu-taetigkeiten lang=de
V Session_eine_beilage_zu_taetigkeiten kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-eine-beilage-zu-taetigkeiten.toon.md
V Sent_eine_beilage_zu_taetigkeiten_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_eine_beilage_zu_taetigkeiten_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_eine_beilage_zu_taetigkeiten_fix FIXES Sent_eine_beilage_zu_taetigkeiten_raw
E Sent_eine_beilage_zu_taetigkeiten_raw FROM_SESSION Session_eine_beilage_zu_taetigkeiten
E Sent_eine_beilage_zu_taetigkeiten_fix FROM_SESSION Session_eine_beilage_zu_taetigkeiten

# ingest-session 2026-09-24T13:18:27Z wechat-desktop-in-mein-system lang=de
V Session_wechat_desktop_in_mein_system kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-wechat-desktop-in-mein-system.toon.md
V Sent_wechat_desktop_in_mein_system_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_wechat_desktop_in_mein_system_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_wechat_desktop_in_mein_system_fix FIXES Sent_wechat_desktop_in_mein_system_raw
E Sent_wechat_desktop_in_mein_system_raw FROM_SESSION Session_wechat_desktop_in_mein_system
E Sent_wechat_desktop_in_mein_system_fix FROM_SESSION Session_wechat_desktop_in_mein_system

# ingest-session 2026-09-24T13:24:53Z oxs-in-die-planung lang=de
V Session_oxs_in_die_planung kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-oxs-in-die-planung.toon.md
V Sent_oxs_in_die_planung_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_oxs_in_die_planung_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_oxs_in_die_planung_fix FIXES Sent_oxs_in_die_planung_raw
E Sent_oxs_in_die_planung_raw FROM_SESSION Session_oxs_in_die_planung
E Sent_oxs_in_die_planung_fix FROM_SESSION Session_oxs_in_die_planung

# ingest-session 2026-09-24T13:31:28Z regelmaessiger-mynoise-benutzen lang=de
V Session_regelmaessiger_mynoise_benutzen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-regelmaessiger-mynoise-benutzen.toon.md
V Sent_regelmaessiger_mynoise_benutzen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_regelmaessiger_mynoise_benutzen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_regelmaessiger_mynoise_benutzen_fix FIXES Sent_regelmaessiger_mynoise_benutzen_raw
E Sent_regelmaessiger_mynoise_benutzen_raw FROM_SESSION Session_regelmaessiger_mynoise_benutzen
E Sent_regelmaessiger_mynoise_benutzen_fix FROM_SESSION Session_regelmaessiger_mynoise_benutzen

# ingest-session 2026-09-24T13:40:18Z antrag-aufenthaltserlaubnis lang=de
V Session_antrag_aufenthaltserlaubnis kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-antrag-aufenthaltserlaubnis.toon.md
V Sent_antrag_aufenthaltserlaubnis_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_antrag_aufenthaltserlaubnis_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_antrag_aufenthaltserlaubnis_fix FIXES Sent_antrag_aufenthaltserlaubnis_raw
E Sent_antrag_aufenthaltserlaubnis_raw FROM_SESSION Session_antrag_aufenthaltserlaubnis
E Sent_antrag_aufenthaltserlaubnis_fix FROM_SESSION Session_antrag_aufenthaltserlaubnis

# ingest-session 2026-09-24T13:42:25Z akten-sie-alle lang=de
V Session_akten_sie_alle kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-akten-sie-alle.toon.md
V Sent_akten_sie_alle_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_akten_sie_alle_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_akten_sie_alle_fix FIXES Sent_akten_sie_alle_raw
E Sent_akten_sie_alle_raw FROM_SESSION Session_akten_sie_alle
E Sent_akten_sie_alle_fix FROM_SESSION Session_akten_sie_alle

# ingest-session 2026-09-24T13:45:39Z ausreisefrist-verhandeln lang=de
V Session_ausreisefrist_verhandeln kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-ausreisefrist-verhandeln.toon.md
V Sent_ausreisefrist_verhandeln_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_ausreisefrist_verhandeln_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_ausreisefrist_verhandeln_fix FIXES Sent_ausreisefrist_verhandeln_raw
E Sent_ausreisefrist_verhandeln_raw FROM_SESSION Session_ausreisefrist_verhandeln
E Sent_ausreisefrist_verhandeln_fix FROM_SESSION Session_ausreisefrist_verhandeln

# ingest-session 2026-09-24T13:46:53Z gesicht-waschen-jetzt lang=de
V Session_gesicht_waschen_jetzt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gesicht-waschen-jetzt.toon.md
V Sent_gesicht_waschen_jetzt_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_gesicht_waschen_jetzt_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_gesicht_waschen_jetzt_fix FIXES Sent_gesicht_waschen_jetzt_raw
E Sent_gesicht_waschen_jetzt_raw FROM_SESSION Session_gesicht_waschen_jetzt
E Sent_gesicht_waschen_jetzt_fix FROM_SESSION Session_gesicht_waschen_jetzt

# ingest-session 2026-09-24T13:55:00Z ausserordentliche-kuendigung lang=de
V Session_ausserordentliche_kuendigung kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-ausserordentliche-kuendigung.toon.md
V Sent_ausserordentliche_kuendigung_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_ausserordentliche_kuendigung_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_ausserordentliche_kuendigung_fix FIXES Sent_ausserordentliche_kuendigung_raw
E Sent_ausserordentliche_kuendigung_raw FROM_SESSION Session_ausserordentliche_kuendigung
E Sent_ausserordentliche_kuendigung_fix FROM_SESSION Session_ausserordentliche_kuendigung

# ingest-session 2026-09-24T13:55:59Z jetzt-bin-ich-zurueck lang=de
V Session_jetzt_bin_ich_zurueck kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-jetzt-bin-ich-zurueck.toon.md
V Sent_jetzt_bin_ich_zurueck_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_jetzt_bin_ich_zurueck_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_jetzt_bin_ich_zurueck_fix FIXES Sent_jetzt_bin_ich_zurueck_raw
E Sent_jetzt_bin_ich_zurueck_raw FROM_SESSION Session_jetzt_bin_ich_zurueck
E Sent_jetzt_bin_ich_zurueck_fix FROM_SESSION Session_jetzt_bin_ich_zurueck

# ingest-session 2026-09-24T14:06:35Z nahrungsergaenzungsmittel-schon-genommen lang=de
V Session_nahrungsergaenzungsmittel_schon_genommen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nahrungsergaenzungsmittel-schon-genommen.toon.md
V Sent_nahrungsergaenzungsmittel_schon_genommen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_nahrungsergaenzungsmittel_schon_genommen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_nahrungsergaenzungsmittel_schon_genommen_fix FIXES Sent_nahrungsergaenzungsmittel_schon_genommen_raw
E Sent_nahrungsergaenzungsmittel_schon_genommen_raw FROM_SESSION Session_nahrungsergaenzungsmittel_schon_genommen
E Sent_nahrungsergaenzungsmittel_schon_genommen_fix FROM_SESSION Session_nahrungsergaenzungsmittel_schon_genommen

# ingest-session 2026-09-24T14:07:01Z zugang-zu-dieser-email lang=de
V Session_zugang_zu_dieser_email kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zugang-zu-dieser-email.toon.md
V Sent_zugang_zu_dieser_email_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_zugang_zu_dieser_email_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_zugang_zu_dieser_email_fix FIXES Sent_zugang_zu_dieser_email_raw
E Sent_zugang_zu_dieser_email_raw FROM_SESSION Session_zugang_zu_dieser_email
E Sent_zugang_zu_dieser_email_fix FROM_SESSION Session_zugang_zu_dieser_email

# ingest-session 2026-09-24T14:09:40Z zugang-zur-legal-email lang=de
V Session_zugang_zur_legal_email kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zugang-zur-legal-email.toon.md
V Sent_zugang_zur_legal_email_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_zugang_zur_legal_email_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_zugang_zur_legal_email_fix FIXES Sent_zugang_zur_legal_email_raw
E Sent_zugang_zur_legal_email_raw FROM_SESSION Session_zugang_zur_legal_email
E Sent_zugang_zur_legal_email_fix FROM_SESSION Session_zugang_zur_legal_email

# ingest-session 2026-09-24T14:15:37Z env-datei-hinzugefuegt lang=de
V Session_env_datei_hinzugefuegt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-env-datei-hinzugefuegt.toon.md
V Sent_env_datei_hinzugefuegt_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_env_datei_hinzugefuegt_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_env_datei_hinzugefuegt_fix FIXES Sent_env_datei_hinzugefuegt_raw
E Sent_env_datei_hinzugefuegt_raw FROM_SESSION Session_env_datei_hinzugefuegt
E Sent_env_datei_hinzugefuegt_fix FROM_SESSION Session_env_datei_hinzugefuegt

# ingest-session 2026-09-24T18:39:39Z todo-liste-einsehen lang=de
V Session_todo_liste_einsehen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-todo-liste-einsehen.toon.md
V Sent_todo_liste_einsehen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_todo_liste_einsehen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_todo_liste_einsehen_fix FIXES Sent_todo_liste_einsehen_raw
E Sent_todo_liste_einsehen_raw FROM_SESSION Session_todo_liste_einsehen
E Sent_todo_liste_einsehen_fix FROM_SESSION Session_todo_liste_einsehen

# ingest-session 2026-09-24T18:40:44Z kommunikation-mit-der-auslaenderbehoerde lang=de
V Session_kommunikation_mit_der_auslaenderbehoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-kommunikation-mit-der-auslaenderbehoerde.toon.md
V Sent_kommunikation_mit_der_auslaenderbehoerde_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_kommunikation_mit_der_auslaenderbehoerde_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_kommunikation_mit_der_auslaenderbehoerde_fix FIXES Sent_kommunikation_mit_der_auslaenderbehoerde_raw
E Sent_kommunikation_mit_der_auslaenderbehoerde_raw FROM_SESSION Session_kommunikation_mit_der_auslaenderbehoerde
E Sent_kommunikation_mit_der_auslaenderbehoerde_fix FROM_SESSION Session_kommunikation_mit_der_auslaenderbehoerde

# ingest-session 2026-09-24T18:42:32Z latex-pdf-die-ich-abschicken-will lang=de
V Session_latex_pdf_die_ich_abschicken_will kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-latex-pdf-die-ich-abschicken-will.toon.md
V Sent_latex_pdf_die_ich_abschicken_will_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_latex_pdf_die_ich_abschicken_will_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_latex_pdf_die_ich_abschicken_will_fix FIXES Sent_latex_pdf_die_ich_abschicken_will_raw
E Sent_latex_pdf_die_ich_abschicken_will_raw FROM_SESSION Session_latex_pdf_die_ich_abschicken_will
E Sent_latex_pdf_die_ich_abschicken_will_fix FROM_SESSION Session_latex_pdf_die_ich_abschicken_will

# ingest-session 2026-09-24T18:44:52Z mit-der-auslaenderbehoerde-kommunizieren lang=de
V Session_mit_der_auslaenderbehoerde_kommunizieren kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-mit-der-auslaenderbehoerde-kommunizieren.toon.md
V Sent_mit_der_auslaenderbehoerde_kommunizieren_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_mit_der_auslaenderbehoerde_kommunizieren_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_mit_der_auslaenderbehoerde_kommunizieren_fix FIXES Sent_mit_der_auslaenderbehoerde_kommunizieren_raw
E Sent_mit_der_auslaenderbehoerde_kommunizieren_raw FROM_SESSION Session_mit_der_auslaenderbehoerde_kommunizieren
E Sent_mit_der_auslaenderbehoerde_kommunizieren_fix FROM_SESSION Session_mit_der_auslaenderbehoerde_kommunizieren

# ingest-session 2026-09-24T18:49:47Z umgang-vier-wendungen lang=de
V Session_umgang_vier_wendungen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-umgang-vier-wendungen.toon.md
V Sent_umgang_vier_wendungen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_umgang_vier_wendungen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_umgang_vier_wendungen_fix FIXES Sent_umgang_vier_wendungen_raw
E Sent_umgang_vier_wendungen_raw FROM_SESSION Session_umgang_vier_wendungen
E Sent_umgang_vier_wendungen_fix FROM_SESSION Session_umgang_vier_wendungen

# ingest-session 2026-09-24T18:51:12Z erklaerung-von-der-fachhochschule lang=de
V Session_erklaerung_von_der_fachhochschule kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-erklaerung-von-der-fachhochschule.toon.md
V Sent_erklaerung_von_der_fachhochschule_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_erklaerung_von_der_fachhochschule_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_erklaerung_von_der_fachhochschule_fix FIXES Sent_erklaerung_von_der_fachhochschule_raw
E Sent_erklaerung_von_der_fachhochschule_raw FROM_SESSION Session_erklaerung_von_der_fachhochschule
E Sent_erklaerung_von_der_fachhochschule_fix FROM_SESSION Session_erklaerung_von_der_fachhochschule

# ingest-session 2026-09-24T18:59:27Z offene-gehaltschuld-anlagen lang=de
V Session_offene_gehaltschuld_anlagen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-offene-gehaltschuld-anlagen.toon.md
V Sent_offene_gehaltschuld_anlagen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_offene_gehaltschuld_anlagen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_offene_gehaltschuld_anlagen_fix FIXES Sent_offene_gehaltschuld_anlagen_raw
E Sent_offene_gehaltschuld_anlagen_raw FROM_SESSION Session_offene_gehaltschuld_anlagen
E Sent_offene_gehaltschuld_anlagen_fix FROM_SESSION Session_offene_gehaltschuld_anlagen

# ingest-session 2026-09-24T19:04:48Z forderungsformulare-ausfuellen lang=de
V Session_forderungsformulare_ausfuellen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformulare-ausfuellen.toon.md
V Sent_forderungsformulare_ausfuellen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_forderungsformulare_ausfuellen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_forderungsformulare_ausfuellen_fix FIXES Sent_forderungsformulare_ausfuellen_raw
E Sent_forderungsformulare_ausfuellen_raw FROM_SESSION Session_forderungsformulare_ausfuellen
E Sent_forderungsformulare_ausfuellen_fix FROM_SESSION Session_forderungsformulare_ausfuellen

# ingest-session 2026-09-24T19:07:56Z zuerst-verwalter-dann-behoerde lang=de
V Session_zuerst_verwalter_dann_behoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zuerst-verwalter-dann-behoerde.toon.md
V Sent_zuerst_verwalter_dann_behoerde_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_zuerst_verwalter_dann_behoerde_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_zuerst_verwalter_dann_behoerde_fix FIXES Sent_zuerst_verwalter_dann_behoerde_raw
E Sent_zuerst_verwalter_dann_behoerde_raw FROM_SESSION Session_zuerst_verwalter_dann_behoerde
E Sent_zuerst_verwalter_dann_behoerde_fix FROM_SESSION Session_zuerst_verwalter_dann_behoerde

# ingest-session 2026-09-24T19:11:21Z das-ist-fuer-owen lang=de
V Session_das_ist_fuer_owen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-fuer-owen.toon.md
V Sent_das_ist_fuer_owen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_das_ist_fuer_owen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_das_ist_fuer_owen_fix FIXES Sent_das_ist_fuer_owen_raw
E Sent_das_ist_fuer_owen_raw FROM_SESSION Session_das_ist_fuer_owen
E Sent_das_ist_fuer_owen_fix FROM_SESSION Session_das_ist_fuer_owen

# ingest-session 2026-09-24T19:12:27Z das-ist-fuer-yushu lang=de
V Session_das_ist_fuer_yushu kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-fuer-yushu.toon.md
V Sent_das_ist_fuer_yushu_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_das_ist_fuer_yushu_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_das_ist_fuer_yushu_fix FIXES Sent_das_ist_fuer_yushu_raw
E Sent_das_ist_fuer_yushu_raw FROM_SESSION Session_das_ist_fuer_yushu
E Sent_das_ist_fuer_yushu_fix FROM_SESSION Session_das_ist_fuer_yushu

# ingest-session 2026-09-24T19:15:32Z forderungsformular-ausfuellen lang=de
V Session_forderungsformular_ausfuellen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformular-ausfuellen.toon.md
V Sent_forderungsformular_ausfuellen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_forderungsformular_ausfuellen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_forderungsformular_ausfuellen_fix FIXES Sent_forderungsformular_ausfuellen_raw
E Sent_forderungsformular_ausfuellen_raw FROM_SESSION Session_forderungsformular_ausfuellen
E Sent_forderungsformular_ausfuellen_fix FROM_SESSION Session_forderungsformular_ausfuellen

# ingest-session 2026-09-24T19:19:24Z seien-sie-vorsichtiger lang=de
V Session_seien_sie_vorsichtiger kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-seien-sie-vorsichtiger.toon.md
V Sent_seien_sie_vorsichtiger_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_seien_sie_vorsichtiger_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_seien_sie_vorsichtiger_fix FIXES Sent_seien_sie_vorsichtiger_raw
E Sent_seien_sie_vorsichtiger_raw FROM_SESSION Session_seien_sie_vorsichtiger
E Sent_seien_sie_vorsichtiger_fix FROM_SESSION Session_seien_sie_vorsichtiger

# ingest-session 2026-09-24T19:26:38Z zinsen-schuldgrund-rote-schrift lang=de
V Session_zinsen_schuldgrund_rote_schrift kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zinsen-schuldgrund-rote-schrift.toon.md
V Sent_zinsen_schuldgrund_rote_schrift_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_zinsen_schuldgrund_rote_schrift_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_zinsen_schuldgrund_rote_schrift_fix FIXES Sent_zinsen_schuldgrund_rote_schrift_raw
E Sent_zinsen_schuldgrund_rote_schrift_raw FROM_SESSION Session_zinsen_schuldgrund_rote_schrift
E Sent_zinsen_schuldgrund_rote_schrift_fix FROM_SESSION Session_zinsen_schuldgrund_rote_schrift

# ingest-session 2026-09-24T19:31:09Z zentriert-ueber-den-unterzeilen lang=de
V Session_zentriert_ueber_den_unterzeilen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zentriert-ueber-den-unterzeilen.toon.md
V Sent_zentriert_ueber_den_unterzeilen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_zentriert_ueber_den_unterzeilen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_zentriert_ueber_den_unterzeilen_fix FIXES Sent_zentriert_ueber_den_unterzeilen_raw
E Sent_zentriert_ueber_den_unterzeilen_raw FROM_SESSION Session_zentriert_ueber_den_unterzeilen
E Sent_zentriert_ueber_den_unterzeilen_fix FROM_SESSION Session_zentriert_ueber_den_unterzeilen

# ingest-session 2026-09-24T19:34:07Z pdf-dateien-noch-einmal lang=de
V Session_pdf_dateien_noch_einmal kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-pdf-dateien-noch-einmal.toon.md
V Sent_pdf_dateien_noch_einmal_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_pdf_dateien_noch_einmal_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_pdf_dateien_noch_einmal_fix FIXES Sent_pdf_dateien_noch_einmal_raw
E Sent_pdf_dateien_noch_einmal_raw FROM_SESSION Session_pdf_dateien_noch_einmal
E Sent_pdf_dateien_noch_einmal_fix FROM_SESSION Session_pdf_dateien_noch_einmal

# ingest-session 2026-09-24T19:35:39Z gmail-konto-fuer-dieses-projekt lang=de
V Session_gmail_konto_fuer_dieses_projekt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gmail-konto-fuer-dieses-projekt.toon.md
V Sent_gmail_konto_fuer_dieses_projekt_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_gmail_konto_fuer_dieses_projekt_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_gmail_konto_fuer_dieses_projekt_fix FIXES Sent_gmail_konto_fuer_dieses_projekt_raw
E Sent_gmail_konto_fuer_dieses_projekt_raw FROM_SESSION Session_gmail_konto_fuer_dieses_projekt
E Sent_gmail_konto_fuer_dieses_projekt_fix FROM_SESSION Session_gmail_konto_fuer_dieses_projekt

# ingest-session 2026-09-24T19:40:40Z das-ist-falsch lang=de
V Session_das_ist_falsch kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-falsch.toon.md
V Sent_das_ist_falsch_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_das_ist_falsch_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_das_ist_falsch_fix FIXES Sent_das_ist_falsch_raw
E Sent_das_ist_falsch_raw FROM_SESSION Session_das_ist_falsch
E Sent_das_ist_falsch_fix FROM_SESSION Session_das_ist_falsch

# ingest-session 2026-09-24T19:49:07Z env-datei-falsches-format lang=de
V Session_env_datei_falsches_format kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-env-datei-falsches-format.toon.md
V Sent_env_datei_falsches_format_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_env_datei_falsches_format_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_env_datei_falsches_format_fix FIXES Sent_env_datei_falsches_format_raw
E Sent_env_datei_falsches_format_raw FROM_SESSION Session_env_datei_falsches_format
E Sent_env_datei_falsches_format_fix FROM_SESSION Session_env_datei_falsches_format

# ingest-session 2026-09-24T19:51:24Z was-soll-ich-ab-jetzt-tun lang=de
V Session_was_soll_ich_ab_jetzt_tun kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-was-soll-ich-ab-jetzt-tun.toon.md
V Sent_was_soll_ich_ab_jetzt_tun_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_was_soll_ich_ab_jetzt_tun_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_was_soll_ich_ab_jetzt_tun_fix FIXES Sent_was_soll_ich_ab_jetzt_tun_raw
E Sent_was_soll_ich_ab_jetzt_tun_raw FROM_SESSION Session_was_soll_ich_ab_jetzt_tun
E Sent_was_soll_ich_ab_jetzt_tun_fix FROM_SESSION Session_was_soll_ich_ab_jetzt_tun

# ingest-session 2026-09-24T19:51:37Z regelmaessige-zahlungen-zusammenfassen lang=de
V Session_regelmaessige_zahlungen_zusammenfassen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-regelmaessige-zahlungen-zusammenfassen.toon.md
V Sent_regelmaessige_zahlungen_zusammenfassen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_regelmaessige_zahlungen_zusammenfassen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_regelmaessige_zahlungen_zusammenfassen_fix FIXES Sent_regelmaessige_zahlungen_zusammenfassen_raw
E Sent_regelmaessige_zahlungen_zusammenfassen_raw FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen
E Sent_regelmaessige_zahlungen_zusammenfassen_fix FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen

# ingest-session 2026-09-24T19:53:06Z einschreiben-oder-email lang=de
V Session_einschreiben_oder_email kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-einschreiben-oder-email.toon.md
V Sent_einschreiben_oder_email_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_einschreiben_oder_email_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_einschreiben_oder_email_fix FIXES Sent_einschreiben_oder_email_raw
E Sent_einschreiben_oder_email_raw FROM_SESSION Session_einschreiben_oder_email
E Sent_einschreiben_oder_email_fix FROM_SESSION Session_einschreiben_oder_email

# ingest-session 2026-09-24T19:55:04Z zuerst-die-email-morgens-den-brief lang=de
V Session_zuerst_die_email_morgens_den_brief kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zuerst-die-email-morgens-den-brief.toon.md
V Sent_zuerst_die_email_morgens_den_brief_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_zuerst_die_email_morgens_den_brief_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_zuerst_die_email_morgens_den_brief_fix FIXES Sent_zuerst_die_email_morgens_den_brief_raw
E Sent_zuerst_die_email_morgens_den_brief_raw FROM_SESSION Session_zuerst_die_email_morgens_den_brief
E Sent_zuerst_die_email_morgens_den_brief_fix FROM_SESSION Session_zuerst_die_email_morgens_den_brief

# ingest-session 2026-09-24T19:57:42Z in-die-latex-pdf-datei lang=de
V Session_in_die_latex_pdf_datei kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-die-latex-pdf-datei.toon.md
V Sent_in_die_latex_pdf_datei_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_in_die_latex_pdf_datei_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_in_die_latex_pdf_datei_fix FIXES Sent_in_die_latex_pdf_datei_raw
E Sent_in_die_latex_pdf_datei_raw FROM_SESSION Session_in_die_latex_pdf_datei
E Sent_in_die_latex_pdf_datei_fix FROM_SESSION Session_in_die_latex_pdf_datei

# ingest-session 2026-09-24T19:58:14Z email-text-und-anlagenliste lang=de
V Session_email_text_und_anlagenliste kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-text-und-anlagenliste.toon.md
V Sent_email_text_und_anlagenliste_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_email_text_und_anlagenliste_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_email_text_und_anlagenliste_fix FIXES Sent_email_text_und_anlagenliste_raw
E Sent_email_text_und_anlagenliste_raw FROM_SESSION Session_email_text_und_anlagenliste
E Sent_email_text_und_anlagenliste_fix FROM_SESSION Session_email_text_und_anlagenliste

# ingest-session 2026-09-24T20:01:26Z xianyu-northdata-post lang=de
V Session_xianyu_northdata_post kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-xianyu-northdata-post.toon.md
V Sent_xianyu_northdata_post_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_xianyu_northdata_post_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_xianyu_northdata_post_fix FIXES Sent_xianyu_northdata_post_raw
E Sent_xianyu_northdata_post_raw FROM_SESSION Session_xianyu_northdata_post
E Sent_xianyu_northdata_post_fix FROM_SESSION Session_xianyu_northdata_post

# ingest-session 2026-09-24T20:09:44Z nachweisunterlagen-zu-den-anlagen lang=de
V Session_nachweisunterlagen_zu_den_anlagen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nachweisunterlagen-zu-den-anlagen.toon.md
V Sent_nachweisunterlagen_zu_den_anlagen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_nachweisunterlagen_zu_den_anlagen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_nachweisunterlagen_zu_den_anlagen_fix FIXES Sent_nachweisunterlagen_zu_den_anlagen_raw
E Sent_nachweisunterlagen_zu_den_anlagen_raw FROM_SESSION Session_nachweisunterlagen_zu_den_anlagen
E Sent_nachweisunterlagen_zu_den_anlagen_fix FROM_SESSION Session_nachweisunterlagen_zu_den_anlagen

# ingest-session 2026-09-24T20:16:51Z email-an-die-auslaenderbehoerde lang=de
V Session_email_an_die_auslaenderbehoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-an-die-auslaenderbehoerde.toon.md
V Sent_email_an_die_auslaenderbehoerde_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_email_an_die_auslaenderbehoerde_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_email_an_die_auslaenderbehoerde_fix FIXES Sent_email_an_die_auslaenderbehoerde_raw
E Sent_email_an_die_auslaenderbehoerde_raw FROM_SESSION Session_email_an_die_auslaenderbehoerde
E Sent_email_an_die_auslaenderbehoerde_fix FROM_SESSION Session_email_an_die_auslaenderbehoerde

# ingest-session 2026-09-24T20:25:29Z in-eine-zip-datei lang=de
V Session_in_eine_zip_datei kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-eine-zip-datei.toon.md
V Sent_in_eine_zip_datei_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_in_eine_zip_datei_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_in_eine_zip_datei_fix FIXES Sent_in_eine_zip_datei_raw
E Sent_in_eine_zip_datei_raw FROM_SESSION Session_in_eine_zip_datei
E Sent_in_eine_zip_datei_fix FROM_SESSION Session_in_eine_zip_datei

# ingest-session 2026-09-24T20:31:22Z forderungsformulare-an-den-verwalter lang=de
V Session_forderungsformulare_an_den_verwalter kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformulare-an-den-verwalter.toon.md
V Sent_forderungsformulare_an_den_verwalter_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_forderungsformulare_an_den_verwalter_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_forderungsformulare_an_den_verwalter_fix FIXES Sent_forderungsformulare_an_den_verwalter_raw
E Sent_forderungsformulare_an_den_verwalter_raw FROM_SESSION Session_forderungsformulare_an_den_verwalter
E Sent_forderungsformulare_an_den_verwalter_fix FROM_SESSION Session_forderungsformulare_an_den_verwalter

# ingest-session 2026-09-24T20:34:49Z das-forderungsformular lang=de
V Session_das_forderungsformular kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-forderungsformular.toon.md
V Sent_das_forderungsformular_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_das_forderungsformular_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_das_forderungsformular_fix FIXES Sent_das_forderungsformular_raw
E Sent_das_forderungsformular_raw FROM_SESSION Session_das_forderungsformular
E Sent_das_forderungsformular_fix FROM_SESSION Session_das_forderungsformular

# ingest-session 2026-09-24T20:38:15Z diese-beiden-forderungsanmeldungen lang=de
V Session_diese_beiden_forderungsanmeldungen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diese-beiden-forderungsanmeldungen.toon.md
V Sent_diese_beiden_forderungsanmeldungen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_diese_beiden_forderungsanmeldungen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_diese_beiden_forderungsanmeldungen_fix FIXES Sent_diese_beiden_forderungsanmeldungen_raw
E Sent_diese_beiden_forderungsanmeldungen_raw FROM_SESSION Session_diese_beiden_forderungsanmeldungen
E Sent_diese_beiden_forderungsanmeldungen_fix FROM_SESSION Session_diese_beiden_forderungsanmeldungen

# ingest-session 2026-09-24T20:40:15Z bereit-an-die-auslaenderbehoerde lang=de
V Session_bereit_an_die_auslaenderbehoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-bereit-an-die-auslaenderbehoerde.toon.md
V Sent_bereit_an_die_auslaenderbehoerde_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_bereit_an_die_auslaenderbehoerde_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_bereit_an_die_auslaenderbehoerde_fix FIXES Sent_bereit_an_die_auslaenderbehoerde_raw
E Sent_bereit_an_die_auslaenderbehoerde_raw FROM_SESSION Session_bereit_an_die_auslaenderbehoerde
E Sent_bereit_an_die_auslaenderbehoerde_fix FROM_SESSION Session_bereit_an_die_auslaenderbehoerde

# ingest-session 2026-09-24T20:42:58Z eine-ersatzdatei-zum-unterschreiben lang=de
V Session_eine_ersatzdatei_zum_unterschreiben kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-eine-ersatzdatei-zum-unterschreiben.toon.md
V Sent_eine_ersatzdatei_zum_unterschreiben_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_eine_ersatzdatei_zum_unterschreiben_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_eine_ersatzdatei_zum_unterschreiben_fix FIXES Sent_eine_ersatzdatei_zum_unterschreiben_raw
E Sent_eine_ersatzdatei_zum_unterschreiben_raw FROM_SESSION Session_eine_ersatzdatei_zum_unterschreiben
E Sent_eine_ersatzdatei_zum_unterschreiben_fix FROM_SESSION Session_eine_ersatzdatei_zum_unterschreiben

# ingest-session 2026-09-24T20:46:22Z schon-unterschrieben lang=de
V Session_schon_unterschrieben kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-schon-unterschrieben.toon.md
V Sent_schon_unterschrieben_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_schon_unterschrieben_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_schon_unterschrieben_fix FIXES Sent_schon_unterschrieben_raw
E Sent_schon_unterschrieben_raw FROM_SESSION Session_schon_unterschrieben
E Sent_schon_unterschrieben_fix FROM_SESSION Session_schon_unterschrieben

# ingest-session 2026-09-24T20:48:30Z bereit-eine-email-abzuschicken lang=de
V Session_bereit_eine_email_abzuschicken kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-bereit-eine-email-abzuschicken.toon.md
V Sent_bereit_eine_email_abzuschicken_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_bereit_eine_email_abzuschicken_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_bereit_eine_email_abzuschicken_fix FIXES Sent_bereit_eine_email_abzuschicken_raw
E Sent_bereit_eine_email_abzuschicken_raw FROM_SESSION Session_bereit_eine_email_abzuschicken
E Sent_bereit_eine_email_abzuschicken_fix FROM_SESSION Session_bereit_eine_email_abzuschicken

# ingest-session 2026-09-24T20:59:17Z offenlegung-zwischen-diesen-leuten lang=de
V Session_offenlegung_zwischen_diesen_leuten kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-offenlegung-zwischen-diesen-leuten.toon.md
V Sent_offenlegung_zwischen_diesen_leuten_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_offenlegung_zwischen_diesen_leuten_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_offenlegung_zwischen_diesen_leuten_fix FIXES Sent_offenlegung_zwischen_diesen_leuten_raw
E Sent_offenlegung_zwischen_diesen_leuten_raw FROM_SESSION Session_offenlegung_zwischen_diesen_leuten
E Sent_offenlegung_zwischen_diesen_leuten_fix FROM_SESSION Session_offenlegung_zwischen_diesen_leuten

# ingest-session 2026-09-24T21:13:52Z das-ende-tiefer lang=de
V Session_das_ende_tiefer kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ende-tiefer.toon.md
V Sent_das_ende_tiefer_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_das_ende_tiefer_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_das_ende_tiefer_fix FIXES Sent_das_ende_tiefer_raw
E Sent_das_ende_tiefer_raw FROM_SESSION Session_das_ende_tiefer
E Sent_das_ende_tiefer_fix FROM_SESSION Session_das_ende_tiefer

# ingest-session 2026-09-24T21:18:51Z moechte-die-reporterin lang=de
V Session_moechte_die_reporterin kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-moechte-die-reporterin.toon.md
V Sent_moechte_die_reporterin_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_moechte_die_reporterin_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_moechte_die_reporterin_fix FIXES Sent_moechte_die_reporterin_raw
E Sent_moechte_die_reporterin_raw FROM_SESSION Session_moechte_die_reporterin
E Sent_moechte_die_reporterin_fix FROM_SESSION Session_moechte_die_reporterin

# ingest-session 2026-09-24T21:21:55Z cybernaut-hinzufuegen lang=de
V Session_cybernaut_hinzufuegen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-cybernaut-hinzufuegen.toon.md
V Sent_cybernaut_hinzufuegen_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_cybernaut_hinzufuegen_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_cybernaut_hinzufuegen_fix FIXES Sent_cybernaut_hinzufuegen_raw
E Sent_cybernaut_hinzufuegen_raw FROM_SESSION Session_cybernaut_hinzufuegen
E Sent_cybernaut_hinzufuegen_fix FROM_SESSION Session_cybernaut_hinzufuegen

# ingest-session 2026-09-24T21:25:01Z beziehung-cybernaut-xu lang=de
V Session_beziehung_cybernaut_xu kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-beziehung-cybernaut-xu.toon.md
V Sent_beziehung_cybernaut_xu_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_beziehung_cybernaut_xu_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_beziehung_cybernaut_xu_fix FIXES Sent_beziehung_cybernaut_xu_raw
E Sent_beziehung_cybernaut_xu_raw FROM_SESSION Session_beziehung_cybernaut_xu
E Sent_beziehung_cybernaut_xu_fix FROM_SESSION Session_beziehung_cybernaut_xu

# ingest-session 2026-09-24T21:27:05Z email-von-name lang=de
V Session_email_von_name_slot kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-von-name.toon.md
V Sent_email_von_name_slot_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_email_von_name_slot_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_email_von_name_slot_fix FIXES Sent_email_von_name_slot_raw
E Sent_email_von_name_slot_raw FROM_SESSION Session_email_von_name_slot
E Sent_email_von_name_slot_fix FROM_SESSION Session_email_von_name_slot

# ingest-session 2026-09-24T21:30:40Z klageandrohung-cybernaut lang=de
V Session_klageandrohung_cybernaut kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-klageandrohung-cybernaut.toon.md
V Sent_klageandrohung_cybernaut_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_klageandrohung_cybernaut_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_klageandrohung_cybernaut_fix FIXES Sent_klageandrohung_cybernaut_raw
E Sent_klageandrohung_cybernaut_raw FROM_SESSION Session_klageandrohung_cybernaut
E Sent_klageandrohung_cybernaut_fix FROM_SESSION Session_klageandrohung_cybernaut

# ingest-session 2026-09-24T21:32:18Z antwort-an-die-reporterin lang=de
V Session_antwort_an_die_reporterin kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-antwort-an-die-reporterin.toon.md
V Sent_antwort_an_die_reporterin_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_antwort_an_die_reporterin_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_antwort_an_die_reporterin_fix FIXES Sent_antwort_an_die_reporterin_raw
E Sent_antwort_an_die_reporterin_raw FROM_SESSION Session_antwort_an_die_reporterin
E Sent_antwort_an_die_reporterin_fix FROM_SESSION Session_antwort_an_die_reporterin

# ingest-session 2026-09-24T21:34:54Z finanzfachkraft lang=de
V Session_finanzfachkraft kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-finanzfachkraft.toon.md
V Sent_finanzfachkraft_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_finanzfachkraft_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_finanzfachkraft_fix FIXES Sent_finanzfachkraft_raw
E Sent_finanzfachkraft_raw FROM_SESSION Session_finanzfachkraft
E Sent_finanzfachkraft_fix FROM_SESSION Session_finanzfachkraft

# ingest-session 2026-09-24T21:39:40Z pdf-zu-oxs lang=de
V Session_pdf_zu_oxs kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-pdf-zu-oxs.toon.md
V Sent_pdf_zu_oxs_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_pdf_zu_oxs_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_pdf_zu_oxs_fix FIXES Sent_pdf_zu_oxs_raw
E Sent_pdf_zu_oxs_raw FROM_SESSION Session_pdf_zu_oxs
E Sent_pdf_zu_oxs_fix FROM_SESSION Session_pdf_zu_oxs

# ingest-session 2026-09-24T21:42:41Z diesen-erlass lang=de
V Session_diesen_erlass kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diesen-erlass.toon.md
V Sent_diesen_erlass_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_diesen_erlass_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_diesen_erlass_fix FIXES Sent_diesen_erlass_raw
E Sent_diesen_erlass_raw FROM_SESSION Session_diesen_erlass
E Sent_diesen_erlass_fix FROM_SESSION Session_diesen_erlass

# ingest-session 2026-09-24T21:52:02Z diesen-vertrag lang=de
V Session_diesen_vertrag kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diesen-vertrag.toon.md
V Sent_diesen_vertrag_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_diesen_vertrag_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_diesen_vertrag_fix FIXES Sent_diesen_vertrag_raw
E Sent_diesen_vertrag_raw FROM_SESSION Session_diesen_vertrag
E Sent_diesen_vertrag_fix FROM_SESSION Session_diesen_vertrag

# ingest-session 2026-09-24T21:56:38Z in-der-richtigen-lage lang=de
V Session_in_der_richtigen_lage kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-der-richtigen-lage.toon.md
V Sent_in_der_richtigen_lage_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_in_der_richtigen_lage_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_in_der_richtigen_lage_fix FIXES Sent_in_der_richtigen_lage_raw
E Sent_in_der_richtigen_lage_raw FROM_SESSION Session_in_der_richtigen_lage
E Sent_in_der_richtigen_lage_fix FROM_SESSION Session_in_der_richtigen_lage

# ingest-session 2026-09-24T21:57:50Z gmail-jetzt-durchschauen-und-sortieren lang=de
V Session_gmail_jetzt_durchschauen_und_sortieren kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gmail-jetzt-durchschauen-und-sortieren.toon.md
V Sent_gmail_jetzt_durchschauen_und_sortieren_raw kind=sentence date=2026-09-24 lang=de role=raw
V Sent_gmail_jetzt_durchschauen_und_sortieren_fix kind=sentence date=2026-09-24 lang=de role=corrected
E Sent_gmail_jetzt_durchschauen_und_sortieren_fix FIXES Sent_gmail_jetzt_durchschauen_und_sortieren_raw
E Sent_gmail_jetzt_durchschauen_und_sortieren_raw FROM_SESSION Session_gmail_jetzt_durchschauen_und_sortieren
E Sent_gmail_jetzt_durchschauen_und_sortieren_fix FROM_SESSION Session_gmail_jetzt_durchschauen_und_sortieren

# ingest-session 2026-09-24T22:02:50Z xiaohongshu-angemeldet lang=de
V Session_xiaohongshu_angemeldet kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-xiaohongshu-angemeldet.toon.md
V Sent_xiaohongshu_angemeldet_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_xiaohongshu_angemeldet_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_xiaohongshu_angemeldet_fix FIXES Sent_xiaohongshu_angemeldet_raw
E Sent_xiaohongshu_angemeldet_raw FROM_SESSION Session_xiaohongshu_angemeldet
E Sent_xiaohongshu_angemeldet_fix FROM_SESSION Session_xiaohongshu_angemeldet

# ingest-session 2026-09-24T22:07:59Z mit-diesem-konto lang=de
V Session_mit_diesem_konto kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-mit-diesem-konto.toon.md
V Sent_mit_diesem_konto_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_mit_diesem_konto_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_mit_diesem_konto_fix FIXES Sent_mit_diesem_konto_raw
E Sent_mit_diesem_konto_raw FROM_SESSION Session_mit_diesem_konto
E Sent_mit_diesem_konto_fix FROM_SESSION Session_mit_diesem_konto

# ingest-session 2026-09-24T22:18:35Z einschliesslich-konto lang=de
V Session_einschliesslich_konto kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-einschliesslich-konto.toon.md
V Sent_einschliesslich_konto_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_einschliesslich_konto_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_einschliesslich_konto_fix FIXES Sent_einschliesslich_konto_raw
E Sent_einschliesslich_konto_raw FROM_SESSION Session_einschliesslich_konto
E Sent_einschliesslich_konto_fix FROM_SESSION Session_einschliesslich_konto

# ingest-session 2026-09-24T22:24:21Z mehr-konten lang=de
V Session_mehr_konten kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-mehr-konten.toon.md
V Sent_mehr_konten_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_mehr_konten_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_mehr_konten_fix FIXES Sent_mehr_konten_raw
E Sent_mehr_konten_raw FROM_SESSION Session_mehr_konten
E Sent_mehr_konten_fix FROM_SESSION Session_mehr_konten

# ingest-session 2026-09-24T22:28:58Z 2026-09-25-quantitative-investitionen-werkzeug lang=de
V Session_2026_09_25_quantitative_investitionen_we kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-quantitative-investitionen-werkzeug.toon.md
V Sent_2026_09_25_quantitative_investitionen_we_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_2026_09_25_quantitative_investitionen_we_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_2026_09_25_quantitative_investitionen_we_fix FIXES Sent_2026_09_25_quantitative_investitionen_we_raw
E Sent_2026_09_25_quantitative_investitionen_we_raw FROM_SESSION Session_2026_09_25_quantitative_investitionen_we
E Sent_2026_09_25_quantitative_investitionen_we_fix FROM_SESSION Session_2026_09_25_quantitative_investitionen_we

# ingest-session 2026-09-24T22:31:08Z untereinander lang=de
V Session_untereinander kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-untereinander.toon.md
V Sent_untereinander_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_untereinander_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_untereinander_fix FIXES Sent_untereinander_raw
E Sent_untereinander_raw FROM_SESSION Session_untereinander
E Sent_untereinander_fix FROM_SESSION Session_untereinander

# ingest-session 2026-09-24T22:34:58Z bcc-chinesische-studierende lang=de
V Session_bcc_chinesische_studierende kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bcc-chinesische-studierende.toon.md
V Sent_bcc_chinesische_studierende_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_bcc_chinesische_studierende_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_bcc_chinesische_studierende_fix FIXES Sent_bcc_chinesische_studierende_raw
E Sent_bcc_chinesische_studierende_raw FROM_SESSION Session_bcc_chinesische_studierende
E Sent_bcc_chinesische_studierende_fix FROM_SESSION Session_bcc_chinesische_studierende

# ingest-session 2026-09-24T22:40:33Z vollstaendiger-wortlaut lang=de
V Session_vollstaendiger_wortlaut kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-vollstaendiger-wortlaut.toon.md
V Sent_vollstaendiger_wortlaut_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_vollstaendiger_wortlaut_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_vollstaendiger_wortlaut_fix FIXES Sent_vollstaendiger_wortlaut_raw
E Sent_vollstaendiger_wortlaut_raw FROM_SESSION Session_vollstaendiger_wortlaut
E Sent_vollstaendiger_wortlaut_fix FROM_SESSION Session_vollstaendiger_wortlaut

# ingest-session 2026-09-24T22:44:44Z wie-einen-roman lang=de
V Session_wie_einen_roman kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-wie-einen-roman.toon.md
V Sent_wie_einen_roman_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_wie_einen_roman_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_wie_einen_roman_fix FIXES Sent_wie_einen_roman_raw
E Sent_wie_einen_roman_raw FROM_SESSION Session_wie_einen_roman
E Sent_wie_einen_roman_fix FROM_SESSION Session_wie_einen_roman

# ingest-session 2026-09-24T22:48:24Z alle-vorhandenen-dateien lang=de
V Session_alle_vorhandenen_dateien kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-alle-vorhandenen-dateien.toon.md
V Sent_alle_vorhandenen_dateien_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_alle_vorhandenen_dateien_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_alle_vorhandenen_dateien_fix FIXES Sent_alle_vorhandenen_dateien_raw
E Sent_alle_vorhandenen_dateien_raw FROM_SESSION Session_alle_vorhandenen_dateien
E Sent_alle_vorhandenen_dateien_fix FROM_SESSION Session_alle_vorhandenen_dateien

# ingest-session 2026-09-24T22:50:51Z chronik-mit-kommentaren lang=de
V Session_chronik_mit_kommentaren kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-chronik-mit-kommentaren.toon.md
V Sent_chronik_mit_kommentaren_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_chronik_mit_kommentaren_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_chronik_mit_kommentaren_fix FIXES Sent_chronik_mit_kommentaren_raw
E Sent_chronik_mit_kommentaren_raw FROM_SESSION Session_chronik_mit_kommentaren
E Sent_chronik_mit_kommentaren_fix FROM_SESSION Session_chronik_mit_kommentaren

# ingest-session 2026-09-24T22:58:18Z negativ-volltext lang=de
V Session_negativ_volltext kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-negativ-volltext.toon.md
V Sent_negativ_volltext_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_negativ_volltext_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_negativ_volltext_fix FIXES Sent_negativ_volltext_raw
E Sent_negativ_volltext_raw FROM_SESSION Session_negativ_volltext
E Sent_negativ_volltext_fix FROM_SESSION Session_negativ_volltext

# ingest-session 2026-09-24T23:20:38Z an-die-reporterin lang=de
V Session_an_die_reporterin kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-an-die-reporterin.toon.md
V Sent_an_die_reporterin_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_an_die_reporterin_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_an_die_reporterin_fix FIXES Sent_an_die_reporterin_raw
E Sent_an_die_reporterin_raw FROM_SESSION Session_an_die_reporterin
E Sent_an_die_reporterin_fix FROM_SESSION Session_an_die_reporterin

# ingest-session 2026-09-24T23:27:26Z zip-in-der lang=de
V Session_zip_in_der kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-zip-in-der.toon.md
V Sent_zip_in_der_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_zip_in_der_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_zip_in_der_fix FIXES Sent_zip_in_der_raw
E Sent_zip_in_der_raw FROM_SESSION Session_zip_in_der
E Sent_zip_in_der_fix FROM_SESSION Session_zip_in_der

# ingest-session 2026-09-25T08:06:21Z ein-neuer-tag lang=de
V Session_ein_neuer_tag kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-ein-neuer-tag.toon.md
V Sent_ein_neuer_tag_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_ein_neuer_tag_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_ein_neuer_tag_fix FIXES Sent_ein_neuer_tag_raw
E Sent_ein_neuer_tag_raw FROM_SESSION Session_ein_neuer_tag
E Sent_ein_neuer_tag_fix FROM_SESSION Session_ein_neuer_tag

# ingest-session 2026-09-25T08:08:08Z die-privaten-daten lang=de
V Session_die_privaten_daten kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-die-privaten-daten.toon.md
V Sent_die_privaten_daten_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_die_privaten_daten_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_die_privaten_daten_fix FIXES Sent_die_privaten_daten_raw
E Sent_die_privaten_daten_raw FROM_SESSION Session_die_privaten_daten
E Sent_die_privaten_daten_fix FROM_SESSION Session_die_privaten_daten

# ingest-session 2026-09-25T08:09:22Z leide-an-einer-krankheit lang=de
V Session_leide_an_einer_krankheit kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-leide-an-einer-krankheit.toon.md
V Sent_leide_an_einer_krankheit_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_leide_an_einer_krankheit_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_leide_an_einer_krankheit_fix FIXES Sent_leide_an_einer_krankheit_raw
E Sent_leide_an_einer_krankheit_raw FROM_SESSION Session_leide_an_einer_krankheit
E Sent_leide_an_einer_krankheit_fix FROM_SESSION Session_leide_an_einer_krankheit

# ingest-session 2026-09-25T08:22:36Z geht-mich-nichts-an lang=de
V Session_geht_mich_nichts_an kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-geht-mich-nichts-an.toon.md
V Sent_geht_mich_nichts_an_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_geht_mich_nichts_an_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_geht_mich_nichts_an_fix FIXES Sent_geht_mich_nichts_an_raw
E Sent_geht_mich_nichts_an_raw FROM_SESSION Session_geht_mich_nichts_an
E Sent_geht_mich_nichts_an_fix FROM_SESSION Session_geht_mich_nichts_an

# ingest-session 2026-09-25T08:24:36Z zwei-wichtigsten-ordner lang=de
V Session_zwei_wichtigsten_ordner kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-zwei-wichtigsten-ordner.toon.md
V Sent_zwei_wichtigsten_ordner_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_zwei_wichtigsten_ordner_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_zwei_wichtigsten_ordner_fix FIXES Sent_zwei_wichtigsten_ordner_raw
E Sent_zwei_wichtigsten_ordner_raw FROM_SESSION Session_zwei_wichtigsten_ordner
E Sent_zwei_wichtigsten_ordner_fix FROM_SESSION Session_zwei_wichtigsten_ordner

# ingest-session 2026-09-25T08:25:14Z einen-auftrag-gebe lang=de
V Session_einen_auftrag_gebe kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-einen-auftrag-gebe.toon.md
V Sent_einen_auftrag_gebe_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_einen_auftrag_gebe_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_einen_auftrag_gebe_fix FIXES Sent_einen_auftrag_gebe_raw
E Sent_einen_auftrag_gebe_raw FROM_SESSION Session_einen_auftrag_gebe
E Sent_einen_auftrag_gebe_fix FROM_SESSION Session_einen_auftrag_gebe

# ingest-session 2026-09-25T08:26:19Z nicht-nur-von-worldquant lang=de
V Session_nicht_nur_von_worldquant kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-nicht-nur-von-worldquant.toon.md
V Sent_nicht_nur_von_worldquant_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_nicht_nur_von_worldquant_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_nicht_nur_von_worldquant_fix FIXES Sent_nicht_nur_von_worldquant_raw
E Sent_nicht_nur_von_worldquant_raw FROM_SESSION Session_nicht_nur_von_worldquant
E Sent_nicht_nur_von_worldquant_fix FROM_SESSION Session_nicht_nur_von_worldquant

# ingest-session 2026-09-25T14:52:02Z setzen-sie-fort lang=de
V Session_setzen_sie_fort kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-setzen-sie-fort.toon.md
V Sent_setzen_sie_fort_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_setzen_sie_fort_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_setzen_sie_fort_fix FIXES Sent_setzen_sie_fort_raw
E Sent_setzen_sie_fort_raw FROM_SESSION Session_setzen_sie_fort
E Sent_setzen_sie_fort_fix FROM_SESSION Session_setzen_sie_fort

# ingest-session 2026-09-25T14:54:06Z sich-bewerben lang=de
V Session_sich_bewerben kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-sich-bewerben.toon.md
V Sent_sich_bewerben_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_sich_bewerben_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_sich_bewerben_fix FIXES Sent_sich_bewerben_raw
E Sent_sich_bewerben_raw FROM_SESSION Session_sich_bewerben
E Sent_sich_bewerben_fix FROM_SESSION Session_sich_bewerben

# ingest-session 2026-09-25T14:56:08Z was-fehlt lang=de
V Session_was_fehlt kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-was-fehlt.toon.md
V Sent_was_fehlt_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_was_fehlt_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_was_fehlt_fix FIXES Sent_was_fehlt_raw
E Sent_was_fehlt_raw FROM_SESSION Session_was_fehlt
E Sent_was_fehlt_fix FROM_SESSION Session_was_fehlt

# ingest-session 2026-09-25T15:00:22Z die-pagnos-stelle lang=de
V Session_die_pagnos_stelle kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-die-pagnos-stelle.toon.md
V Sent_die_pagnos_stelle_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_die_pagnos_stelle_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_die_pagnos_stelle_fix FIXES Sent_die_pagnos_stelle_raw
E Sent_die_pagnos_stelle_raw FROM_SESSION Session_die_pagnos_stelle
E Sent_die_pagnos_stelle_fix FROM_SESSION Session_die_pagnos_stelle

# ingest-session 2026-09-25T15:08:32Z abwechselnd-stellen lang=de
V Session_abwechselnd_stellen kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-abwechselnd-stellen.toon.md
V Sent_abwechselnd_stellen_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_abwechselnd_stellen_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_abwechselnd_stellen_fix FIXES Sent_abwechselnd_stellen_raw
E Sent_abwechselnd_stellen_raw FROM_SESSION Session_abwechselnd_stellen
E Sent_abwechselnd_stellen_fix FROM_SESSION Session_abwechselnd_stellen

# ingest-session 2026-09-25T15:14:01Z bewerbungsverfolgung lang=de
V Session_bewerbungsverfolgung kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bewerbungsverfolgung.toon.md
V Sent_bewerbungsverfolgung_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_bewerbungsverfolgung_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_bewerbungsverfolgung_fix FIXES Sent_bewerbungsverfolgung_raw
E Sent_bewerbungsverfolgung_raw FROM_SESSION Session_bewerbungsverfolgung
E Sent_bewerbungsverfolgung_fix FROM_SESSION Session_bewerbungsverfolgung

# ingest-session 2026-09-25T15:17:07Z bis-das-ziel lang=de
V Session_bis_das_ziel kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bis-das-ziel.toon.md
V Sent_bis_das_ziel_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_bis_das_ziel_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_bis_das_ziel_fix FIXES Sent_bis_das_ziel_raw
E Sent_bis_das_ziel_raw FROM_SESSION Session_bis_das_ziel
E Sent_bis_das_ziel_fix FROM_SESSION Session_bis_das_ziel

# ingest-session 2026-09-25T16:28:00Z lebenslauf-anpassen lang=de
V Session_lebenslauf_anpassen kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-lebenslauf-anpassen.toon.md
V Sent_lebenslauf_anpassen_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_lebenslauf_anpassen_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_lebenslauf_anpassen_fix FIXES Sent_lebenslauf_anpassen_raw
E Sent_lebenslauf_anpassen_raw FROM_SESSION Session_lebenslauf_anpassen
E Sent_lebenslauf_anpassen_fix FROM_SESSION Session_lebenslauf_anpassen

# ingest-session 2026-09-25T18:03:57Z jobbewerbung-fortsetzen lang=de
V Session_jobbewerbung_fortsetzen kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-jobbewerbung-fortsetzen.toon.md
V Sent_jobbewerbung_fortsetzen_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_jobbewerbung_fortsetzen_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_jobbewerbung_fortsetzen_fix FIXES Sent_jobbewerbung_fortsetzen_raw
E Sent_jobbewerbung_fortsetzen_raw FROM_SESSION Session_jobbewerbung_fortsetzen
E Sent_jobbewerbung_fortsetzen_fix FROM_SESSION Session_jobbewerbung_fortsetzen

# ingest-session 2026-09-25T18:15:30Z easy-apply-begrenzung lang=de
V Session_easy_apply_begrenzung kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-easy-apply-begrenzung.toon.md
V Sent_easy_apply_begrenzung_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_easy_apply_begrenzung_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_easy_apply_begrenzung_fix FIXES Sent_easy_apply_begrenzung_raw
E Sent_easy_apply_begrenzung_raw FROM_SESSION Session_easy_apply_begrenzung
E Sent_easy_apply_begrenzung_fix FROM_SESSION Session_easy_apply_begrenzung

# ingest-session 2026-09-25T18:24:32Z fuer-jede-stelle lang=de
V Session_fuer_jede_stelle kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-fuer-jede-stelle.toon.md
V Sent_fuer_jede_stelle_raw kind=sentence date=2026-09-25 lang=de role=raw
V Sent_fuer_jede_stelle_fix kind=sentence date=2026-09-25 lang=de role=corrected
E Sent_fuer_jede_stelle_fix FIXES Sent_fuer_jede_stelle_raw
E Sent_fuer_jede_stelle_raw FROM_SESSION Session_fuer_jede_stelle
E Sent_fuer_jede_stelle_fix FROM_SESSION Session_fuer_jede_stelle

# ingest-session 2026-09-27T08:43:43Z emails-bearbeiten lang=de
V Session_emails_bearbeiten kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-emails-bearbeiten.toon.md
V Sent_emails_bearbeiten_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_emails_bearbeiten_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_emails_bearbeiten_fix FIXES Sent_emails_bearbeiten_raw
E Sent_emails_bearbeiten_raw FROM_SESSION Session_emails_bearbeiten
E Sent_emails_bearbeiten_fix FROM_SESSION Session_emails_bearbeiten

# ingest-session 2026-09-27T08:57:06Z bewerbungsabsage lang=de
V Session_bewerbungsabsage kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-bewerbungsabsage.toon.md
V Sent_bewerbungsabsage_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_bewerbungsabsage_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_bewerbungsabsage_fix FIXES Sent_bewerbungsabsage_raw
E Sent_bewerbungsabsage_raw FROM_SESSION Session_bewerbungsabsage
E Sent_bewerbungsabsage_fix FROM_SESSION Session_bewerbungsabsage

# ingest-session 2026-09-27T09:00:04Z gmail-ordner lang=de
V Session_gmail_ordner kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-gmail-ordner.toon.md
V Sent_gmail_ordner_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_gmail_ordner_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_gmail_ordner_fix FIXES Sent_gmail_ordner_raw
E Sent_gmail_ordner_raw FROM_SESSION Session_gmail_ordner
E Sent_gmail_ordner_fix FROM_SESSION Session_gmail_ordner

# ingest-session 2026-09-27T09:04:39Z tag-starten-leiden lang=de
V Session_tag_starten_leiden kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tag-starten-leiden.toon.md
V Sent_tag_starten_leiden_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_tag_starten_leiden_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_tag_starten_leiden_fix FIXES Sent_tag_starten_leiden_raw
E Sent_tag_starten_leiden_raw FROM_SESSION Session_tag_starten_leiden
E Sent_tag_starten_leiden_fix FROM_SESSION Session_tag_starten_leiden

# ingest-session 2026-09-27T09:09:27Z meinen-tag-nachrichten lang=de
V Session_meinen_tag_nachrichten kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-meinen-tag-nachrichten.toon.md
V Sent_meinen_tag_nachrichten_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_meinen_tag_nachrichten_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_meinen_tag_nachrichten_fix FIXES Sent_meinen_tag_nachrichten_raw
E Sent_meinen_tag_nachrichten_raw FROM_SESSION Session_meinen_tag_nachrichten
E Sent_meinen_tag_nachrichten_fix FROM_SESSION Session_meinen_tag_nachrichten

# ingest-session 2026-09-27T09:10:19Z kanonischen-erholungszeitraum lang=de
V Session_kanonischen_erholungszeitraum kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-kanonischen-erholungszeitraum.toon.md
V Sent_kanonischen_erholungszeitraum_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_kanonischen_erholungszeitraum_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_kanonischen_erholungszeitraum_fix FIXES Sent_kanonischen_erholungszeitraum_raw
E Sent_kanonischen_erholungszeitraum_raw FROM_SESSION Session_kanonischen_erholungszeitraum
E Sent_kanonischen_erholungszeitraum_fix FROM_SESSION Session_kanonischen_erholungszeitraum

# ingest-session 2026-09-27T09:12:52Z tag-angefangen-putzen lang=de
V Session_tag_angefangen_putzen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tag-angefangen-putzen.toon.md
V Sent_tag_angefangen_putzen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_tag_angefangen_putzen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_tag_angefangen_putzen_fix FIXES Sent_tag_angefangen_putzen_raw
E Sent_tag_angefangen_putzen_raw FROM_SESSION Session_tag_angefangen_putzen
E Sent_tag_angefangen_putzen_fix FROM_SESSION Session_tag_angefangen_putzen

# ingest-session 2026-09-27T09:23:36Z boss-antworten-verfolgen lang=de
V Session_boss_antworten_verfolgen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-boss-antworten-verfolgen.toon.md
V Sent_boss_antworten_verfolgen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_boss_antworten_verfolgen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_boss_antworten_verfolgen_fix FIXES Sent_boss_antworten_verfolgen_raw
E Sent_boss_antworten_verfolgen_raw FROM_SESSION Session_boss_antworten_verfolgen
E Sent_boss_antworten_verfolgen_fix FROM_SESSION Session_boss_antworten_verfolgen

# ingest-session 2026-09-27T09:23:36Z eingeloggt-vorgaenge lang=de
V Session_eingeloggt_vorgaenge kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-eingeloggt-vorgaenge.toon.md
V Sent_eingeloggt_vorgaenge_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_eingeloggt_vorgaenge_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_eingeloggt_vorgaenge_fix FIXES Sent_eingeloggt_vorgaenge_raw
E Sent_eingeloggt_vorgaenge_raw FROM_SESSION Session_eingeloggt_vorgaenge
E Sent_eingeloggt_vorgaenge_fix FROM_SESSION Session_eingeloggt_vorgaenge

# ingest-session 2026-09-27T09:35:15Z fuer-jede-stelle-lebenslauf lang=de
V Session_fuer_jede_stelle_lebenslauf kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-fuer-jede-stelle-lebenslauf.toon.md
V Sent_fuer_jede_stelle_lebenslauf_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_fuer_jede_stelle_lebenslauf_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_fuer_jede_stelle_lebenslauf_fix FIXES Sent_fuer_jede_stelle_lebenslauf_raw
E Sent_fuer_jede_stelle_lebenslauf_raw FROM_SESSION Session_fuer_jede_stelle_lebenslauf
E Sent_fuer_jede_stelle_lebenslauf_fix FROM_SESSION Session_fuer_jede_stelle_lebenslauf

# ingest-session 2026-09-27T10:09:59Z apfelessig-auswirkungstabelle lang=de
V Session_apfelessig_auswirkungstabelle kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-apfelessig-auswirkungstabelle.toon.md
V Sent_apfelessig_auswirkungstabelle_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_apfelessig_auswirkungstabelle_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_apfelessig_auswirkungstabelle_fix FIXES Sent_apfelessig_auswirkungstabelle_raw
E Sent_apfelessig_auswirkungstabelle_raw FROM_SESSION Session_apfelessig_auswirkungstabelle
E Sent_apfelessig_auswirkungstabelle_fix FROM_SESSION Session_apfelessig_auswirkungstabelle

# ingest-session 2026-09-27T10:15:58Z tiefgreifende-analyse lang=de
V Session_tiefgreifende_analyse kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tiefgreifende-analyse.toon.md
V Sent_tiefgreifende_analyse_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_tiefgreifende_analyse_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_tiefgreifende_analyse_fix FIXES Sent_tiefgreifende_analyse_raw
E Sent_tiefgreifende_analyse_raw FROM_SESSION Session_tiefgreifende_analyse
E Sent_tiefgreifende_analyse_fix FROM_SESSION Session_tiefgreifende_analyse

# ingest-session 2026-09-27T10:22:56Z meinen-verlauf lang=de
V Session_meinen_verlauf kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-meinen-verlauf.toon.md
V Sent_meinen_verlauf_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_meinen_verlauf_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_meinen_verlauf_fix FIXES Sent_meinen_verlauf_raw
E Sent_meinen_verlauf_raw FROM_SESSION Session_meinen_verlauf
E Sent_meinen_verlauf_fix FROM_SESSION Session_meinen_verlauf

# ingest-session 2026-09-27T10:27:04Z vorhandenen-lebenslauf-ersetzen lang=de
V Session_vorhandenen_lebenslauf_ersetzen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-vorhandenen-lebenslauf-ersetzen.toon.md
V Sent_vorhandenen_lebenslauf_ersetzen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_vorhandenen_lebenslauf_ersetzen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_vorhandenen_lebenslauf_ersetzen_fix FIXES Sent_vorhandenen_lebenslauf_ersetzen_raw
E Sent_vorhandenen_lebenslauf_ersetzen_raw FROM_SESSION Session_vorhandenen_lebenslauf_ersetzen
E Sent_vorhandenen_lebenslauf_ersetzen_fix FROM_SESSION Session_vorhandenen_lebenslauf_ersetzen

# ingest-session 2026-09-27T10:38:17Z nicht-nur-sondern-auch-blogs lang=de
V Session_nicht_nur_sondern_auch_blogs kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-nicht-nur-sondern-auch-blogs.toon.md
V Sent_nicht_nur_sondern_auch_blogs_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_nicht_nur_sondern_auch_blogs_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_nicht_nur_sondern_auch_blogs_fix FIXES Sent_nicht_nur_sondern_auch_blogs_raw
E Sent_nicht_nur_sondern_auch_blogs_raw FROM_SESSION Session_nicht_nur_sondern_auch_blogs
E Sent_nicht_nur_sondern_auch_blogs_fix FROM_SESSION Session_nicht_nur_sondern_auch_blogs

# ingest-session 2026-09-27T10:47:52Z nach-china-reisen lang=de
V Session_nach_china_reisen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-nach-china-reisen.toon.md
V Sent_nach_china_reisen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_nach_china_reisen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_nach_china_reisen_fix FIXES Sent_nach_china_reisen_raw
E Sent_nach_china_reisen_raw FROM_SESSION Session_nach_china_reisen
E Sent_nach_china_reisen_fix FROM_SESSION Session_nach_china_reisen

# ingest-session 2026-09-27T10:51:58Z wechat-austausch-annehmen lang=de
V Session_wechat_austausch_annehmen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-wechat-austausch-annehmen.toon.md
V Sent_wechat_austausch_annehmen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_wechat_austausch_annehmen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_wechat_austausch_annehmen_fix FIXES Sent_wechat_austausch_annehmen_raw
E Sent_wechat_austausch_annehmen_raw FROM_SESSION Session_wechat_austausch_annehmen
E Sent_wechat_austausch_annehmen_fix FROM_SESSION Session_wechat_austausch_annehmen

# ingest-session 2026-09-27T11:44:36Z ueberblick-sprachenlernen lang=de
V Session_ueberblick_sprachenlernen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-ueberblick-sprachenlernen.toon.md
V Sent_ueberblick_sprachenlernen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_ueberblick_sprachenlernen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_ueberblick_sprachenlernen_fix FIXES Sent_ueberblick_sprachenlernen_raw
E Sent_ueberblick_sprachenlernen_raw FROM_SESSION Session_ueberblick_sprachenlernen
E Sent_ueberblick_sprachenlernen_fix FROM_SESSION Session_ueberblick_sprachenlernen

# ingest-session 2026-09-27T11:49:59Z visualisierung-sprachlernstand lang=de
V Session_visualisierung_sprachlernstand kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-visualisierung-sprachlernstand.toon.md
V Sent_visualisierung_sprachlernstand_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_visualisierung_sprachlernstand_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_visualisierung_sprachlernstand_fix FIXES Sent_visualisierung_sprachlernstand_raw
E Sent_visualisierung_sprachlernstand_raw FROM_SESSION Session_visualisierung_sprachlernstand
E Sent_visualisierung_sprachlernstand_fix FROM_SESSION Session_visualisierung_sprachlernstand

# ingest-session 2026-09-27T11:53:25Z oeffentlicher-link-sprachvisualisierung lang=de
V Session_oeffentlicher_link_sprachvisualisierung kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-oeffentlicher-link-sprachvisualisierung.toon.md
V Sent_oeffentlicher_link_sprachvisualisierung_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_oeffentlicher_link_sprachvisualisierung_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_oeffentlicher_link_sprachvisualisierung_fix FIXES Sent_oeffentlicher_link_sprachvisualisierung_raw
E Sent_oeffentlicher_link_sprachvisualisierung_raw FROM_SESSION Session_oeffentlicher_link_sprachvisualisierung
E Sent_oeffentlicher_link_sprachvisualisierung_fix FROM_SESSION Session_oeffentlicher_link_sprachvisualisierung

# ingest-session 2026-09-27T12:07:14Z tief-in-sprachlernstand-eintauchen lang=de
V Session_tief_in_sprachlernstand_eintauchen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tief-in-sprachlernstand-eintauchen.toon.md
V Sent_tief_in_sprachlernstand_eintauchen_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_tief_in_sprachlernstand_eintauchen_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_tief_in_sprachlernstand_eintauchen_fix FIXES Sent_tief_in_sprachlernstand_eintauchen_raw
E Sent_tief_in_sprachlernstand_eintauchen_raw FROM_SESSION Session_tief_in_sprachlernstand_eintauchen
E Sent_tief_in_sprachlernstand_eintauchen_fix FROM_SESSION Session_tief_in_sprachlernstand_eintauchen

# ingest-session 2026-09-27T12:20:10Z spanisch-uebungen-zuerst lang=de
V Session_spanisch_uebungen_zuerst kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-spanisch-uebungen-zuerst.toon.md
V Sent_spanisch_uebungen_zuerst_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_spanisch_uebungen_zuerst_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_spanisch_uebungen_zuerst_fix FIXES Sent_spanisch_uebungen_zuerst_raw
E Sent_spanisch_uebungen_zuerst_raw FROM_SESSION Session_spanisch_uebungen_zuerst
E Sent_spanisch_uebungen_zuerst_fix FROM_SESSION Session_spanisch_uebungen_zuerst

# ingest-session 2026-09-27T12:44:33Z cvc-primer-parrafo-demasiado lang=es
V Session_cvc_primer_parrafo_demasiado kind=session date=2026-09-27 lang=es body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-cvc-primer-parrafo-demasiado.toon.md
V Sent_cvc_primer_parrafo_demasiado_raw kind=sentence date=2026-09-27 lang=es role=raw
V Sent_cvc_primer_parrafo_demasiado_fix kind=sentence date=2026-09-27 lang=es role=corrected
E Sent_cvc_primer_parrafo_demasiado_fix FIXES Sent_cvc_primer_parrafo_demasiado_raw
E Sent_cvc_primer_parrafo_demasiado_raw FROM_SESSION Session_cvc_primer_parrafo_demasiado
E Sent_cvc_primer_parrafo_demasiado_fix FROM_SESSION Session_cvc_primer_parrafo_demasiado

# Russian opinion practice 2026-09-27
V Lemma_ru_mnenie kind=lemma lang=ru surface="мнение" gloss="opinion"
V Lemma_ru_schitat kind=lemma lang=ru surface="считать" gloss="consider-or-think"
V Lemma_ru_ponimat kind=lemma lang=ru surface="понимать" gloss="understand"
V Lemma_ru_kazatsja kind=lemma lang=ru surface="казаться" gloss="seem"
V Lemma_ru_povtorit kind=lemma lang=ru surface="повторить" gloss="repeat"
V Form_ru_ja_schitaju kind=form lang=ru surface="Я считаю" lemma=Lemma_ru_schitat
V Form_ru_mne_kazhetsja kind=form lang=ru surface="Мне кажется" lemma=Lemma_ru_kazatsja
V Form_ru_u_menja_drugoe_mnenie kind=form lang=ru surface="У меня другое мнение" lemma=Lemma_ru_mnenie
V Form_ru_ja_ponimaju kind=form lang=ru surface="Я пока не очень хорошо понимаю" lemma=Lemma_ru_ponimat
V Form_ru_ne_mogli_by_vy_povtorit kind=form lang=ru surface="Не могли бы вы повторить, пожалуйста?" lemma=Lemma_ru_povtorit
E Lemma_ru_schitat HAS_FORM Form_ru_ja_schitaju
E Lemma_ru_kazatsja HAS_FORM Form_ru_mne_kazhetsja
E Lemma_ru_mnenie HAS_FORM Form_ru_u_menja_drugoe_mnenie
E Lemma_ru_ponimat HAS_FORM Form_ru_ja_ponimaju
E Lemma_ru_povtorit HAS_FORM Form_ru_ne_mogli_by_vy_povtorit
V Chunk_ru_ja_schitaju_chto kind=chunk lang=ru surface="Я считаю, что это хороший способ учиться." frame=ja_schitaju_chto
V Chunk_ru_mne_kazhetsja_chto kind=chunk lang=ru surface="Мне кажется, что этот текст слишком сложный." frame=mne_kazhetsja_chto
V Chunk_ru_u_menja_drugoe_mnenie kind=chunk lang=ru surface="У меня другое мнение." frame=u_menja_N_nom
V Chunk_ru_ja_ponimaju kind=chunk lang=ru surface="Я пока не очень хорошо понимаю по-русски." frame=ja_poka_ne_ochen_ADV_V
V Chunk_ru_ne_mogli_by_vy_povtorit kind=chunk lang=ru surface="Не могли бы вы повторить, пожалуйста?" frame=ne_mogli_by_vy_inf
E Chunk_ru_ja_schitaju_chto USES Form_ru_ja_schitaju
E Chunk_ru_mne_kazhetsja_chto USES Form_ru_mne_kazhetsja
E Chunk_ru_u_menja_drugoe_mnenie USES Form_ru_u_menja_drugoe_mnenie
E Chunk_ru_ja_ponimaju USES Form_ru_ja_ponimaju
E Chunk_ru_ne_mogli_by_vy_povtorit USES Form_ru_ne_mogli_by_vy_povtorit

# ingest-session 2026-09-27T13:17:58Z wiktionary-deutsch-vokabelseiten lang=de
V Session_wiktionary_deutsch_vokabelseiten kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-wiktionary-deutsch-vokabelseiten.toon.md
V Sent_wiktionary_deutsch_vokabelseiten_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_wiktionary_deutsch_vokabelseiten_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_wiktionary_deutsch_vokabelseiten_fix FIXES Sent_wiktionary_deutsch_vokabelseiten_raw
E Sent_wiktionary_deutsch_vokabelseiten_raw FROM_SESSION Session_wiktionary_deutsch_vokabelseiten
E Sent_wiktionary_deutsch_vokabelseiten_fix FROM_SESSION Session_wiktionary_deutsch_vokabelseiten

# Russian expression practice 2026-09-27
V Lemma_ru_pytatsja kind=lemma lang=ru surface="пытаться" gloss="try" source=de-wiktionary-ru-pytatsja
V Lemma_ru_dumat kind=lemma lang=ru surface="думать" gloss="think" source=de-wiktionary-ru-dumat
V Form_ru_ja_pytajus_govorit kind=form lang=ru surface="Я пытаюсь говорить по-русски" lemma=Lemma_ru_pytatsja
V Form_ru_ja_dumaju kind=form lang=ru surface="я думаю по-немецки" lemma=Lemma_ru_dumat
E Lemma_ru_pytatsja HAS_FORM Form_ru_ja_pytajus_govorit
E Lemma_ru_dumat HAS_FORM Form_ru_ja_dumaju
V Chunk_ru_ja_pytajus_dumaju kind=chunk lang=ru surface="Я пытаюсь говорить по-русски, но пока думаю по-немецки." frame=ja_pytajus_inf
E Chunk_ru_ja_pytajus_dumaju USES Form_ru_ja_pytajus_govorit
E Chunk_ru_ja_pytajus_dumaju USES Form_ru_ja_dumaju

# ingest-session 2026-09-27T13:26:38Z russisch-gedanken-ausdruecken lang=de
V Session_russisch_gedanken_ausdruecken kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russisch-gedanken-ausdruecken.toon.md
V Sent_russisch_gedanken_ausdruecken_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_russisch_gedanken_ausdruecken_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_russisch_gedanken_ausdruecken_fix FIXES Sent_russisch_gedanken_ausdruecken_raw
E Sent_russisch_gedanken_ausdruecken_raw FROM_SESSION Session_russisch_gedanken_ausdruecken
E Sent_russisch_gedanken_ausdruecken_fix FROM_SESSION Session_russisch_gedanken_ausdruecken

# ingest-session 2026-09-27T13:36:14Z russischer-wortschatz-deutsche-erklaerung lang=de
V Session_russischer_wortschatz_deutsche_erklaerun kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russischer-wortschatz-deutsche-erklaerung.toon.md
V Sent_russischer_wortschatz_deutsche_erklaerun_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_russischer_wortschatz_deutsche_erklaerun_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_russischer_wortschatz_deutsche_erklaerun_fix FIXES Sent_russischer_wortschatz_deutsche_erklaerun_raw
E Sent_russischer_wortschatz_deutsche_erklaerun_raw FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun
E Sent_russischer_wortschatz_deutsche_erklaerun_fix FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun

# ingest-session 2026-09-27T13:40:49Z russische-lemma-links lang=de
V Session_russische_lemma_links kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russische-lemma-links.toon.md
V Sent_russische_lemma_links_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_russische_lemma_links_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_russische_lemma_links_fix FIXES Sent_russische_lemma_links_raw
E Sent_russische_lemma_links_raw FROM_SESSION Session_russische_lemma_links
E Sent_russische_lemma_links_fix FROM_SESSION Session_russische_lemma_links

# ingest-session 2026-09-27T13:42:26Z damit-zufrieden-fortschritt lang=de
V Session_damit_zufrieden_fortschritt kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-damit-zufrieden-fortschritt.toon.md
V Sent_damit_zufrieden_fortschritt_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_damit_zufrieden_fortschritt_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_damit_zufrieden_fortschritt_fix FIXES Sent_damit_zufrieden_fortschritt_raw
E Sent_damit_zufrieden_fortschritt_raw FROM_SESSION Session_damit_zufrieden_fortschritt
E Sent_damit_zufrieden_fortschritt_fix FROM_SESSION Session_damit_zufrieden_fortschritt

# ingest-session 2026-09-27T14:00:47Z auf-meine-emails lang=de
V Session_auf_meine_emails kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-auf-meine-emails.toon.md
V Sent_auf_meine_emails_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_auf_meine_emails_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_auf_meine_emails_fix FIXES Sent_auf_meine_emails_raw
E Sent_auf_meine_emails_raw FROM_SESSION Session_auf_meine_emails
E Sent_auf_meine_emails_fix FROM_SESSION Session_auf_meine_emails

# ingest-session 2026-09-27T14:02:05Z berlin-potsdam-ausflug lang=de
V Session_berlin_potsdam_ausflug kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-berlin-potsdam-ausflug.toon.md
V Sent_berlin_potsdam_ausflug_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_berlin_potsdam_ausflug_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_berlin_potsdam_ausflug_fix FIXES Sent_berlin_potsdam_ausflug_raw
E Sent_berlin_potsdam_ausflug_raw FROM_SESSION Session_berlin_potsdam_ausflug
E Sent_berlin_potsdam_ausflug_fix FROM_SESSION Session_berlin_potsdam_ausflug

# ingest-session 2026-09-27T20:45:48Z starte-die-shenyou-10m lang=de
V Session_starte_die_shenyou_10m kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-starte-die-shenyou.toon.md
V Sent_starte_die_shenyou_10m_raw kind=sentence date=2026-09-27 lang=de role=raw
V Sent_starte_die_shenyou_10m_fix kind=sentence date=2026-09-27 lang=de role=corrected
E Sent_starte_die_shenyou_10m_fix FIXES Sent_starte_die_shenyou_10m_raw
E Sent_starte_die_shenyou_10m_raw FROM_SESSION Session_starte_die_shenyou_10m
E Sent_starte_die_shenyou_10m_fix FROM_SESSION Session_starte_die_shenyou_10m

# ingest-session 2026-09-29T10:17:30Z meinen-tag-zustand lang=de
V Session_meinen_tag_zustand kind=session date=2026-09-29 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-29-meinen-tag-zustand.toon.md
V Sent_meinen_tag_zustand_raw kind=sentence date=2026-09-29 lang=de role=raw
V Sent_meinen_tag_zustand_fix kind=sentence date=2026-09-29 lang=de role=corrected
E Sent_meinen_tag_zustand_fix FIXES Sent_meinen_tag_zustand_raw
E Sent_meinen_tag_zustand_raw FROM_SESSION Session_meinen_tag_zustand
E Sent_meinen_tag_zustand_fix FROM_SESSION Session_meinen_tag_zustand

# ingest-session 2026-09-29T10:22:11Z anfang-des-tages lang=de
V Session_anfang_des_tages kind=session date=2026-09-29 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-29-anfang-des-tages.toon.md
V Sent_anfang_des_tages_raw kind=sentence date=2026-09-29 lang=de role=raw
V Sent_anfang_des_tages_fix kind=sentence date=2026-09-29 lang=de role=corrected
E Sent_anfang_des_tages_fix FIXES Sent_anfang_des_tages_raw
E Sent_anfang_des_tages_raw FROM_SESSION Session_anfang_des_tages
E Sent_anfang_des_tages_fix FROM_SESSION Session_anfang_des_tages
