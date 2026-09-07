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
