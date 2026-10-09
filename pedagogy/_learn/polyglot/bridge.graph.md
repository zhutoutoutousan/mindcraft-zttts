# Cross-language concept bridge (language-neutral Concept → per-lang Lemma/Frame)
# Do not invent unnamed languages. Add EXPRESSES edges only for attested or session-proven forms.
# Local edge labels: EXPRESSES NEEDS_FRAME GAP_IN FROM_SESSION

V Concept_device_location kind=concept gloss=location-on-a-device
V Concept_current_state kind=concept gloss=current-state-of-work
V Concept_this_project kind=concept gloss=the-project-at-hand
V Concept_lets_dive kind=concept gloss=invite-to-go-deeper
V Concept_for_today kind=concept gloss=purpose-time-today
V Concept_todo_list kind=concept gloss=task-list-for-human
V Concept_no_changes kind=concept gloss=do-not-modify

V Lemma_en_on_my_laptop kind=lemma lang=en surface=on-my-laptop
V Lemma_de_auf_meinem_Laptop kind=lemma lang=de surface=auf-meinem-Laptop
V Lemma_en_current_state kind=lemma lang=en surface=current-state
V Lemma_de_aktueller_Zustand kind=lemma lang=de surface=der-aktuelle-Zustand
V Lemma_en_lets_dive kind=lemma lang=en surface=lets-dive-deeper
V Lemma_de_lass_uns_eintauchen kind=lemma lang=de surface=lass-uns-tiefer-eintauchen
V Lemma_zh_rang_women kind=lemma lang=zh surface=让我们-deeper-calque note=L1-order-risk

V Frame_de_auf_Dat_device kind=frame lang=de id=auf_Dat_device
V Frame_de_lass_uns_Vinf kind=frame lang=de id=lass_uns_Vinf
V Frame_de_det_Nom_masc kind=frame lang=de id=det_Nom_masc
V Frame_de_fuer_purpose kind=frame lang=de id=fuer_purpose

E Concept_device_location EXPRESSES Lemma_en_on_my_laptop
E Concept_device_location EXPRESSES Lemma_de_auf_meinem_Laptop
E Concept_device_location NEEDS_FRAME Frame_de_auf_Dat_device
E Concept_current_state EXPRESSES Lemma_en_current_state
E Concept_current_state EXPRESSES Lemma_de_aktueller_Zustand
E Concept_current_state NEEDS_FRAME Frame_de_det_Nom_masc
E Concept_lets_dive EXPRESSES Lemma_en_lets_dive
E Concept_lets_dive EXPRESSES Lemma_de_lass_uns_eintauchen
E Concept_lets_dive NEEDS_FRAME Frame_de_lass_uns_Vinf
E Concept_for_today NEEDS_FRAME Frame_de_fuer_purpose
E Lemma_zh_rang_women GAP_IN de SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07.toon.md

V Concept_first_test kind=concept gloss=my-first-test
V Concept_view_dashboard kind=concept gloss=view-project-dashboard-now
V Lemma_de_mein_erster_Test kind=lemma lang=de surface=mein-erster-Test
V Lemma_de_Dashboard_einsehen kind=lemma lang=de surface=Dashboard-einsehen
V Lemma_de_haette_gern kind=lemma lang=de surface=Ich-haette-gern
V Frame_de_mein_erster_N_m kind=frame lang=de id=mein_erster_N_m
V Frame_de_haette_gern_zuerst kind=frame lang=de id=haette_gern_zuerst

E Concept_first_test EXPRESSES Lemma_de_mein_erster_Test
E Concept_first_test NEEDS_FRAME Frame_de_mein_erster_N_m
E Concept_view_dashboard EXPRESSES Lemma_de_Dashboard_einsehen
E Concept_view_dashboard EXPRESSES Lemma_de_haette_gern
E Concept_view_dashboard NEEDS_FRAME Frame_de_haette_gern_zuerst
E Concept_this_project NEEDS_FRAME Frame_de_det_Akk_neut
E Concept_first_test FROM_SESSION Session_dash
E Concept_view_dashboard FROM_SESSION Session_dash

V Session_dash kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-dashboard.toon.md

# ingest-session 2026-09-07T12:17:58Z first-arbitrage-test-dashboard
V Session_first_arbitrage_test_dashboard kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-dashboard.toon.md
V Focus_first_arbitrage_test_dashboard kind=focus gloss=artikel_kasus_mein_erster_test_f_r_dieses_projekt status=active
E Focus_first_arbitrage_test_dashboard FROM_SESSION Session_first_arbitrage_test_dashboard
V Lemma_de_fix_first_arbitrage_test_dashboard kind=lemma lang=de surface=ach_so_das_ist_mein_erster_test_ich_h_tte_gern_zue role=minimal-rewrite
E Lemma_de_fix_first_arbitrage_test_dashboard FROM_SESSION Session_first_arbitrage_test_dashboard SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-dashboard.toon.md
V Form_fix_first_arbitrage_test_dashboard_0_ers kind=form lang=de surface=erster_test fixes=erste_test
E Form_fix_first_arbitrage_test_dashboard_0_ers FROM_SESSION Session_first_arbitrage_test_dashboard
V Form_fix_first_arbitrage_test_dashboard_1_h_t kind=form lang=de surface=h_tte_gern fixes=hatte_gern
E Form_fix_first_arbitrage_test_dashboard_1_h_t FROM_SESSION Session_first_arbitrage_test_dashboard
V Form_fix_first_arbitrage_test_dashboard_2_die kind=form lang=de surface=dieses_projekt fixes=diese_projekt
E Form_fix_first_arbitrage_test_dashboard_2_die FROM_SESSION Session_first_arbitrage_test_dashboard
V Form_fix_first_arbitrage_test_dashboard_3_kur kind=form lang=de surface=kurz_auf_einen_blick_einsehen fixes=augenblick_einsehen
E Form_fix_first_arbitrage_test_dashboard_3_kur FROM_SESSION Session_first_arbitrage_test_dashboard
V Form_fix_first_arbitrage_test_dashboard_4_kur kind=form lang=de surface=kurze_s_tze fixes=run_on
E Form_fix_first_arbitrage_test_dashboard_4_kur FROM_SESSION Session_first_arbitrage_test_dashboard

# ingest-session 2026-09-07T12:17:58Z ensure-errors-internalized-hook
V Session_ensure_errors_internalized_hook kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-internalize-hook.toon.md
V Focus_ensure_errors_internalized_hook kind=focus gloss=sichergestellt_dass_sprachfehler_artikel_wortstell status=active
E Focus_ensure_errors_internalized_hook FROM_SESSION Session_ensure_errors_internalized_hook
V Lemma_de_fix_ensure_errors_internalized_hook kind=lemma lang=de surface=ja_ich_h_tte_gern_sichergestellt_dass_meine_sprach role=minimal-rewrite
E Lemma_de_fix_ensure_errors_internalized_hook FROM_SESSION Session_ensure_errors_internalized_hook SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-internalize-hook.toon.md
V Form_fix_ensure_errors_internalized_hook_0_h_ kind=form lang=de surface=h_tte_gern_sichergestellt fixes=h_tte_gern_es_sicherstellen
E Form_fix_ensure_errors_internalized_hook_0_h_ FROM_SESSION Session_ensure_errors_internalized_hook
V Form_fix_ensure_errors_internalized_hook_1_sp kind=form lang=de surface=sprachfehler fixes=sprachefehler
E Form_fix_ensure_errors_internalized_hook_1_sp FROM_SESSION Session_ensure_errors_internalized_hook
V Form_fix_ensure_errors_internalized_hook_2_da kind=form lang=de surface=dass fixes=da
E Form_fix_ensure_errors_internalized_hook_2_da FROM_SESSION Session_ensure_errors_internalized_hook
V Form_fix_ensure_errors_internalized_hook_3_in kind=form lang=de surface=internalisiert_werden fixes=内化-ed
E Form_fix_ensure_errors_internalized_hook_3_in FROM_SESSION Session_ensure_errors_internalized_hook
V Form_fix_ensure_errors_internalized_hook_4_in kind=form lang=de surface=in_den_Sprach-Knowledge-Graph fixes=ins_Sprache-Knowledge-Graph
E Form_fix_ensure_errors_internalized_hook_4_in FROM_SESSION Session_ensure_errors_internalized_hook
V Form_fix_ensure_errors_internalized_hook_5_da kind=form lang=de surface=Das_ist_auch_der_Grund_warum_es_den_Hook_gibt fixes=run-on_warum_gibt_es_hook
E Form_fix_ensure_errors_internalized_hook_5_da FROM_SESSION Session_ensure_errors_internalized_hook

# auto-gap 2026-09-07T12:20:53Z surface=内化-ed
V Concept_gap_zh_ed_238255878d kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_ed_238255878d kind=gap lang=zh surface=内化-ed target=de status=open
V Lemma_zh_zh_ed_238255878d kind=lemma lang=zh surface=内化-ed
E Concept_gap_zh_ed_238255878d EXPRESSES Lemma_zh_zh_ed_238255878d SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_ed_238255878d GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_ed_238255878d GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-07T12:21:32Z cafe-mask-how-it-works
V Session_cafe_mask_how_it_works kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-cafe-mask-how.toon.md
V Focus_cafe_mask_how_it_works kind=focus gloss=gespielt_spielen_kein_en_ing_am_partizip status=active
E Focus_cafe_mask_how_it_works FROM_SESSION Session_cafe_mask_how_it_works
V Lemma_de_fix_cafe_mask_how_it_works kind=lemma lang=de surface=ok_also_ich_spiele_jetzt_meine_caf_mask_mp3_bei_mi role=minimal-rewrite
E Lemma_de_fix_cafe_mask_how_it_works FROM_SESSION Session_cafe_mask_how_it_works SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-cafe-mask-how.toon.md
V Form_fix_cafe_mask_how_it_works_0_spiele_jetz kind=form lang=de surface=spiele_jetzt fixes=gespielt-ing
E Form_fix_cafe_mask_how_it_works_0_spiele_jetz FROM_SESSION Session_cafe_mask_how_it_works
V Form_fix_cafe_mask_how_it_works_1_meine_caf_m kind=form lang=de surface=meine_Café-Mask-MP3 fixes=mit_meine_cafe-mask
E Form_fix_cafe_mask_how_it_works_1_meine_caf_m FROM_SESSION Session_cafe_mask_how_it_works
V Form_fix_cafe_mask_how_it_works_2_datei_mp3 kind=form lang=de surface=Datei_/_MP3 fixes=datei
E Form_fix_cafe_mask_how_it_works_2_datei_mp3 FROM_SESSION Session_cafe_mask_how_it_works
V Form_fix_cafe_mask_how_it_works_3_punkt_wie_f kind=form lang=de surface=Punkt_+_Wie_funktioniert_das? fixes=Run-on_so_wie
E Form_fix_cafe_mask_how_it_works_3_punkt_wie_f FROM_SESSION Session_cafe_mask_how_it_works

# ingest-session 2026-09-07T12:29:12Z language-panel-menu
V Session_language_panel_menu kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-language-panel.toon.md
V Focus_language_panel_menu kind=focus gloss=erfassen_abdecken_brauchen_kein_en_to_be_de_inf_56 status=active
E Focus_language_panel_menu FROM_SESSION Session_language_panel_menu
V Lemma_de_fix_language_panel_menu kind=lemma lang=de surface=ach_so_ich_brauche_im_left_panel_ein_men_language_ role=minimal-rewrite
E Lemma_de_fix_language_panel_menu FROM_SESSION Session_language_panel_menu SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-language-panel.toon.md
V Form_fix_language_panel_menu_0_abdecken_brauc kind=form lang=de surface=abdecken_/_brauchen fixes=to_be_erfassen
E Form_fix_language_panel_menu_0_abdecken_brauc FROM_SESSION Session_language_panel_menu
V Form_fix_language_panel_menu_1_grammatik kind=form lang=de surface=Grammatik fixes=gramatik
E Form_fix_language_panel_menu_1_grammatik FROM_SESSION Session_language_panel_menu
V Form_fix_language_panel_menu_2_einen_separate kind=form lang=de surface=einen_separaten_Knowledge_Graph fixes=ein_separate_Knowledge_graph
E Form_fix_language_panel_menu_2_einen_separate FROM_SESSION Session_language_panel_menu
V Form_fix_language_panel_menu_3_f_rs_sprachenl kind=form lang=de surface=fürs_Sprachenlernen fixes=für_Sprache_lernen
E Form_fix_language_panel_menu_3_f_rs_sprachenl FROM_SESSION Session_language_panel_menu
V Form_fix_language_panel_menu_4_klarer_nebensa kind=form lang=de surface=klarer_Nebensatz_/_Aufzählung fixes=Run-on_mit_sowieso
E Form_fix_language_panel_menu_4_klarer_nebensa FROM_SESSION Session_language_panel_menu

# ingest-session 2026-09-07T12:30:15Z method-goal-fehlerfrei-aeussern
V Session_method_goal_fehlerfrei_aeussern kind=session date=2026-09-07 body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-method-goal.toon.md
V Focus_method_goal_fehlerfrei_aeussern kind=focus gloss=beherrschen_dass_orthografie_nebensatz status=active
E Focus_method_goal_fehlerfrei_aeussern FROM_SESSION Session_method_goal_fehlerfrei_aeussern
V Lemma_de_fix_method_goal_fehlerfrei_aeussern kind=lemma lang=de surface=ok_mein_ziel_bei_dieser_methode_besteht_darin_dass role=minimal-rewrite
E Lemma_de_fix_method_goal_fehlerfrei_aeussern FROM_SESSION Session_method_goal_fehlerfrei_aeussern SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-method-goal.toon.md
V Form_fix_method_goal_fehlerfrei_aeussern_0_di kind=form lang=de surface=dieser_Methode fixes=diesem_Methode
E Form_fix_method_goal_fehlerfrei_aeussern_0_di FROM_SESSION Session_method_goal_fehlerfrei_aeussern
V Form_fix_method_goal_fehlerfrei_aeussern_1_da kind=form lang=de surface=dass fixes=daß
E Form_fix_method_goal_fehlerfrei_aeussern_1_da FROM_SESSION Session_method_goal_fehlerfrei_aeussern
V Form_fix_method_goal_fehlerfrei_aeussern_2_ir kind=form lang=de surface=irgendwann_/_eventuell fixes=evetuell
E Form_fix_method_goal_fehlerfrei_aeussern_2_ir FROM_SESSION Session_method_goal_fehlerfrei_aeussern
V Form_fix_method_goal_fehlerfrei_aeussern_3_be kind=form lang=de surface=beherrsche fixes=behersscht
E Form_fix_method_goal_fehlerfrei_aeussern_3_be FROM_SESSION Session_method_goal_fehlerfrei_aeussern
V Form_fix_method_goal_fehlerfrei_aeussern_4_vo kind=form lang=de surface=vollständig_/_vollkommen fixes=vollkommend
E Form_fix_method_goal_fehlerfrei_aeussern_4_vo FROM_SESSION Session_method_goal_fehlerfrei_aeussern
V Form_fix_method_goal_fehlerfrei_aeussern_5_mi kind=form lang=de surface=mich_beim_Schreiben_…_äußern_zu_können fixes=bei_Schreiben_…_kann_ich_äußer
E Form_fix_method_goal_fehlerfrei_aeussern_5_mi FROM_SESSION Session_method_goal_fehlerfrei_aeussern

# ingest-session 2026-09-07T12:32:01Z fr-probe-expliquer-ajouter-kg lang=fr
V Session_fr_probe_expliquer_ajouter_kg kind=session date=2026-09-07 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-fr-probe.toon.md
V Focus_fr_probe_expliquer_ajouter_kg kind=focus lang=fr gloss=ajouter_au_pas_sur_06ca34a78f status=active
E Focus_fr_probe_expliquer_ajouter_kg FROM_SESSION Session_fr_probe_expliquer_ajouter_kg
V Lemma_fr_fix_fr_probe_expliquer_ajouter_kg kind=lemma lang=fr surface=C'est_un_test_pour_mon_français._Pourriez-vous_me_ role=minimal-rewrite
E Lemma_fr_fix_fr_probe_expliquer_ajouter_kg FROM_SESSION Session_fr_probe_expliquer_ajouter_kg SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-fr-probe.toon.md
V Form_fix_fr_probe_expliquer_ajouter_kg_0_fran kind=form lang=fr surface=français fixes=Francais
E Form_fix_fr_probe_expliquer_ajouter_kg_0_fran FROM_SESSION Session_fr_probe_expliquer_ajouter_kg
V Form_fix_fr_probe_expliquer_ajouter_kg_1_l_aj kind=form lang=fr surface=l'ajouter_au_knowledge_graph fixes=ajouter_sur_le_knowledge_graph
E Form_fix_fr_probe_expliquer_ajouter_kg_1_l_aj FROM_SESSION Session_fr_probe_expliquer_ajouter_kg
V Form_fix_fr_probe_expliquer_ajouter_kg_2_me_l kind=form lang=fr surface=me_l'expliquer_et_l'ajouter fixes=me_expliquer_et_ajouter
E Form_fix_fr_probe_expliquer_ajouter_kg_2_me_l FROM_SESSION Session_fr_probe_expliquer_ajouter_kg
V Form_fix_fr_probe_expliquer_ajouter_kg_3_poin kind=form lang=fr surface=point_après_français_puis_nouvelle_requê fixes=une_phrase_longue
E Form_fix_fr_probe_expliquer_ajouter_kg_3_poin FROM_SESSION Session_fr_probe_expliquer_ajouter_kg


# fr-probe frames 2026-09-07
V Concept_add_to_kg kind=concept gloss=add-to-knowledge-graph
V Concept_fr_probe_explain kind=concept gloss=polite-ask-explain-and-add
V Lemma_fr_ajouter_au_kg kind=lemma lang=fr surface=ajouter-au-knowledge-graph
V Lemma_fr_pourriez_vous kind=lemma lang=fr surface=Pourriez-vous
V Frame_fr_ajouter_a_NP kind=frame lang=fr id=ajouter_a_NP
V Frame_fr_pourriez_vous_Inf kind=frame lang=fr id=pourriez_vous_Inf
E Concept_add_to_kg EXPRESSES Lemma_fr_ajouter_au_kg
E Concept_add_to_kg NEEDS_FRAME Frame_fr_ajouter_a_NP
E Concept_fr_probe_explain EXPRESSES Lemma_fr_pourriez_vous
E Concept_fr_probe_explain NEEDS_FRAME Frame_fr_pourriez_vous_Inf
E Lemma_fr_ajouter_au_kg FROM_SESSION Session_fr_probe_expliquer_ajouter_kg

# ingest-session 2026-09-07T14:25:21Z inflow-take-dsb-graph-persist lang=de
V Session_inflow_take_dsb_graph_persist kind=session date=2026-09-07 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-inflow-dsb-persist.toon.md
V Focus_inflow_take_dsb_graph_persist kind=focus lang=de gloss=sicherstellen_dass_widergespiegelt_wird_dass_finit status=active
E Focus_inflow_take_dsb_graph_persist FROM_SESSION Session_inflow_take_dsb_graph_persist
V Lemma_de_fix_inflow_take_dsb_graph_persist kind=lemma lang=de surface=Ich_möchte_sicherstellen,_dass_meine_manuelle_Eing role=minimal-rewrite
E Lemma_de_fix_inflow_take_dsb_graph_persist FROM_SESSION Session_inflow_take_dsb_graph_persist SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-inflow-dsb-persist.toon.md
V Form_fix_inflow_take_dsb_graph_persist_0_sich kind=form lang=de surface=sicherstellen,_dass fixes=sicherzustellen,_daß
E Form_fix_inflow_take_dsb_graph_persist_0_sich FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_1_dass kind=form lang=de surface=dass fixes=daß
E Form_fix_inflow_take_dsb_graph_persist_1_dass FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_2_zu_d kind=form lang=de surface=zu_den_Inflow-Informationen fixes=für_den_Inflowsinformationen
E Form_fix_inflow_take_dsb_graph_persist_2_zu_d FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_3_dsb_ kind=form lang=de surface=DSB-Verfolgung fixes=DSB_Verfolgerung
E Form_fix_inflow_take_dsb_graph_persist_3_dsb_ FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_4_und kind=form lang=de surface=und fixes=und_und
E Form_fix_inflow_take_dsb_graph_persist_4_und FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_5_im_p kind=form lang=de surface=im_Pädagogik-Knowledge-Graph_widergespie fixes=Pädagogie_knowledge_graph_wide
E Form_fix_inflow_take_dsb_graph_persist_5_im_p FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_6_g_nz kind=form lang=de surface=gänzlich_in_der_Zielsprache fixes=ganzlich_auf_Zielsprache
E Form_fix_inflow_take_dsb_graph_persist_6_g_nz FROM_SESSION Session_inflow_take_dsb_graph_persist
V Form_fix_inflow_take_dsb_graph_persist_7_ich kind=form lang=de surface=ich fixes=Ich_(mitte)
E Form_fix_inflow_take_dsb_graph_persist_7_ich FROM_SESSION Session_inflow_take_dsb_graph_persist

# ingest-session 2026-09-07T14:30:25Z chat-correct-kg-tmp-promote lang=de
V Session_chat_correct_kg_tmp_promote kind=session date=2026-09-07 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-chat-kg-tmp-promote.toon.md
V Focus_chat_correct_kg_tmp_promote kind=focus lang=de gloss=nach_meinen_eingaben_dativ_plural_korrektur_nicht_ status=active
E Focus_chat_correct_kg_tmp_promote FROM_SESSION Session_chat_correct_kg_tmp_promote
V Lemma_de_fix_chat_correct_kg_tmp_promote kind=lemma lang=de surface=Nein_—_nach_meinen_Eingaben_in_dieser_Chatbox_soll role=minimal-rewrite
E Lemma_de_fix_chat_correct_kg_tmp_promote FROM_SESSION Session_chat_correct_kg_tmp_promote SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-07-chat-kg-tmp-promote.toon.md
V Form_fix_chat_correct_kg_tmp_promote_0_nach_m kind=form lang=de surface=nach_meinen_Eingaben fixes=nach_meinem_Eingaben
E Form_fix_chat_correct_kg_tmp_promote_0_nach_m FROM_SESSION Session_chat_correct_kg_tmp_promote
V Form_fix_chat_correct_kg_tmp_promote_1_korrek kind=form lang=de surface=Korrektur fixes=Korrigierung
E Form_fix_chat_correct_kg_tmp_promote_1_korrek FROM_SESSION Session_chat_correct_kg_tmp_promote
V Form_fix_chat_correct_kg_tmp_promote_2_fehler kind=form lang=de surface=Fehler fixes=fehler
E Form_fix_chat_correct_kg_tmp_promote_2_fehler FROM_SESSION Session_chat_correct_kg_tmp_promote
V Form_fix_chat_correct_kg_tmp_promote_3_im_kno kind=form lang=de surface=im_Knowledge_Graph fixes=auf_Knowledge_graph
E Form_fix_chat_correct_kg_tmp_promote_3_im_kno FROM_SESSION Session_chat_correct_kg_tmp_promote
V Form_fix_chat_correct_kg_tmp_promote_4_lass_u kind=form lang=de surface=lass_uns_das_einführen fixes=lassen_es_einführen
E Form_fix_chat_correct_kg_tmp_promote_4_lass_u FROM_SESSION Session_chat_correct_kg_tmp_promote
V Form_fix_chat_correct_kg_tmp_promote_5_beim_c kind=form lang=de surface=beim_Cleaning_des_tmp-Ordners fixes=für_dem_Cleaning_der_tmp_Ordne
E Form_fix_chat_correct_kg_tmp_promote_5_beim_c FROM_SESSION Session_chat_correct_kg_tmp_promote
V Form_fix_chat_correct_kg_tmp_promote_6_ordnun kind=form lang=de surface=ordnungsgemäß_verarbeitet fixes=Ordnungsgemäß_gearbeitet
E Form_fix_chat_correct_kg_tmp_promote_6_ordnun FROM_SESSION Session_chat_correct_kg_tmp_promote

# ingest-session 2026-09-08T14:38:27Z scapula-auch-zeitgleich lang=de
V Session_scapula_auch_zeitgleich kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-scapula-auch-zeitgleich.toon.md
V Focus_scapula_auch_zeitgleich kind=focus lang=de gloss="ebenfalls am selben Tag (auch + Zeit)" status=active
E Focus_scapula_auch_zeitgleich FROM_SESSION Session_scapula_auch_zeitgleich
V Lemma_de_fix_scapula_auch_zeitgleich kind=lemma lang=de surface="Die linke Skapula ist am selben Tag ebenfalls abge" role=minimal-rewrite
E Lemma_de_fix_scapula_auch_zeitgleich FROM_SESSION Session_scapula_auch_zeitgleich SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-scapula-auch-zeitgleich.toon.md
V Form_fix_scapula_auch_zeitgleich_0_die_linke_ kind=form lang=de surface="die linke Skapula" fixes=肩胛
E Form_fix_scapula_auch_zeitgleich_0_die_linke_ FROM_SESSION Session_scapula_auch_zeitgleich
V Form_fix_scapula_auch_zeitgleich_1_ebenfalls_ kind=form lang=de surface="ebenfalls am selben Tag" fixes=也同期
E Form_fix_scapula_auch_zeitgleich_1_ebenfalls_ FROM_SESSION Session_scapula_auch_zeitgleich
V Form_fix_scapula_auch_zeitgleich_2_ist_abgekl kind=form lang=de surface="ist abgeklungen" fixes=恢复了
E Form_fix_scapula_auch_zeitgleich_2_ist_abgekl FROM_SESSION Session_scapula_auch_zeitgleich

# ingest-session 2026-09-08T14:49:41Z archify-diagram-test lang=de
V Session_archify_diagram_test kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-archify-diagram-test.toon.md
V Focus_archify_diagram_test kind=focus lang=de gloss="um es zu testen" status=active
E Focus_archify_diagram_test FROM_SESSION Session_archify_diagram_test
V Lemma_de_fix_archify_diagram_test kind=lemma lang=de surface="Also mach ein Diagramm mit Archify, um es zu teste" role=minimal-rewrite
E Lemma_de_fix_archify_diagram_test FROM_SESSION Session_archify_diagram_test SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-archify-diagram-test.toon.md
V Form_fix_archify_diagram_test_0_also_mach kind=form lang=de surface="Also mach" fixes="So mach"
E Form_fix_archify_diagram_test_0_also_mach FROM_SESSION Session_archify_diagram_test
V Form_fix_archify_diagram_test_1_diagramm kind=form lang=de surface=Diagramm fixes=diagram
E Form_fix_archify_diagram_test_1_diagramm FROM_SESSION Session_archify_diagram_test
V Form_fix_archify_diagram_test_2_um_es_zu_test kind=form lang=de surface="um es zu testen" fixes="es zu testen"
E Form_fix_archify_diagram_test_2_um_es_zu_test FROM_SESSION Session_archify_diagram_test

# ingest-session 2026-09-08T14:55:32Z korrektur-hook lang=de
V Session_korrektur_hook kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-korrektur-hook.toon.md
V Focus_korrektur_hook kind=focus lang=de gloss="Korrektur (nicht Korrigierung)" status=active
E Focus_korrektur_hook FROM_SESSION Session_korrektur_hook
V Lemma_de_fix_korrektur_hook kind=lemma lang=de surface="Schau mal: Ich habe gerade eben auf Deutsch geschr" role=minimal-rewrite
E Lemma_de_fix_korrektur_hook FROM_SESSION Session_korrektur_hook SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-korrektur-hook.toon.md
V Form_fix_korrektur_hook_0_korrektur kind=form lang=de surface=Korrektur fixes=Korrigierung
E Form_fix_korrektur_hook_0_korrektur FROM_SESSION Session_korrektur_hook
V Form_fix_korrektur_hook_1_gerade_eben kind=form lang=de surface="gerade eben" fixes=augenblick
E Form_fix_korrektur_hook_1_gerade_eben FROM_SESSION Session_korrektur_hook
V Form_fix_korrektur_hook_2_geschrieben kind=form lang=de surface=geschrieben fixes=gegeben
E Form_fix_korrektur_hook_2_geschrieben FROM_SESSION Session_korrektur_hook
V Form_fix_korrektur_hook_3_es_gibt_noch_keine_ kind=form lang=de surface="es gibt noch keine Korrektur" fixes="gibt es noch nicht … noch etwa"
E Form_fix_korrektur_hook_3_es_gibt_noch_keine_ FROM_SESSION Session_korrektur_hook

# ingest-session 2026-09-08T15:00:00Z uebungen-kenntnisstand lang=de
V Session_uebungen_kenntnisstand kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-uebungen-kenntnisstand.toon.md
V Focus_uebungen_kenntnisstand kind=focus lang=de gloss="zu + Dat (Kenntnisstand), nicht nach" status=active
E Focus_uebungen_kenntnisstand FROM_SESSION Session_uebungen_kenntnisstand
V Lemma_de_fix_uebungen_kenntnisstand kind=lemma lang=de surface="Ich brauche also Übungen auf Deutsch, die zu meine" role=minimal-rewrite
E Lemma_de_fix_uebungen_kenntnisstand FROM_SESSION Session_uebungen_kenntnisstand SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-uebungen-kenntnisstand.toon.md
V Form_fix_uebungen_kenntnisstand_0_zu_dat kind=form lang=de surface="zu + Dat" fixes="nach + Nom"
E Form_fix_uebungen_kenntnisstand_0_zu_dat FROM_SESSION Session_uebungen_kenntnisstand
V Form_fix_uebungen_kenntnisstand_1_kenntnissta kind=form lang=de surface=Kenntnisstand fixes=Grasp
E Form_fix_uebungen_kenntnisstand_1_kenntnissta FROM_SESSION Session_uebungen_kenntnisstand
V Form_fix_uebungen_kenntnisstand_2_bungen_auf_ kind=form lang=de surface="Übungen auf Deutsch / deutsche Übungen" fixes="Deutsch sprache Übungen"
E Form_fix_uebungen_kenntnisstand_2_bungen_auf_ FROM_SESSION Session_uebungen_kenntnisstand
V Form_fix_uebungen_kenntnisstand_3_vorhandenen kind=form lang=de surface=vorhandenen fixes=vorhande
E Form_fix_uebungen_kenntnisstand_3_vorhandenen FROM_SESSION Session_uebungen_kenntnisstand
V Form_fix_uebungen_kenntnisstand_4_ich_also_dd kind=form lang=de surface="Ich … also" fixes="So Ich"
E Form_fix_uebungen_kenntnisstand_4_ich_also_dd FROM_SESSION Session_uebungen_kenntnisstand

# ingest-session 2026-09-08T15:04:33Z html-drills-localstorage lang=de
V Session_html_drills_localstorage kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-html-drills-localstorage.toon.md
V Focus_html_drills_localstorage kind=focus lang=de gloss="lokale Speicherung zur Aktualisierung" status=active
E Focus_html_drills_localstorage FROM_SESSION Session_html_drills_localstorage
V Lemma_de_fix_html_drills_localstorage kind=lemma lang=de surface="Ach so, gib mir HTML-Übungen mit lokaler Speicheru" role=minimal-rewrite
E Lemma_de_fix_html_drills_localstorage FROM_SESSION Session_html_drills_localstorage SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-html-drills-localstorage.toon.md
V Form_fix_html_drills_localstorage_0_lokaler_s kind=form lang=de surface="lokaler Speicherung" fixes="Lokal Speicherung"
E Form_fix_html_drills_localstorage_0_lokaler_s FROM_SESSION Session_html_drills_localstorage
V Form_fix_html_drills_localstorage_1_zur_aktua kind=form lang=de surface="zur Aktualisierung" fixes="zu Aktualisierung"
E Form_fix_html_drills_localstorage_1_zur_aktua FROM_SESSION Session_html_drills_localstorage
V Form_fix_html_drills_localstorage_2_html_bung kind=form lang=de surface=HTML-Übungen fixes="html Übungen"
E Form_fix_html_drills_localstorage_2_html_bung FROM_SESSION Session_html_drills_localstorage

# ingest-session 2026-09-08T15:11:11Z skilltree-facets lang=de
V Session_skilltree_facets kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-skilltree-facets.toon.md
V Focus_skilltree_facets kind=focus lang=de gloss="darunterliegende Fähigkeiten (nicht unterliegene)" status=active
E Focus_skilltree_facets FROM_SESSION Session_skilltree_facets
V Lemma_de_fix_skilltree_facets kind=lemma lang=de surface="Beim Skill Tree brauche ich die darunterliegenden " role=minimal-rewrite
E Lemma_de_fix_skilltree_facets FROM_SESSION Session_skilltree_facets SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-skilltree-facets.toon.md
V Form_fix_skilltree_facets_0_darunterliegende kind=form lang=de surface=darunterliegende fixes=unterliegene
E Form_fix_skilltree_facets_0_darunterliegende FROM_SESSION Session_skilltree_facets
V Form_fix_skilltree_facets_1_die_skills kind=form lang=de surface="die Skills" fixes="den Skills"
E Form_fix_skilltree_facets_1_die_skills FROM_SESSION Session_skilltree_facets
V Form_fix_skilltree_facets_2_beim_skill_tree kind=form lang=de surface="Beim Skill Tree" fixes="Bei dem Skill Tree"
E Form_fix_skilltree_facets_2_beim_skill_tree FROM_SESSION Session_skilltree_facets

# ingest-session 2026-09-08T15:20:24Z inflow-compact-bilibili lang=de
V Session_inflow_compact_bilibili kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-inflow-compact-bilibili.toon.md
V Focus_inflow_compact_bilibili kind=focus lang=de gloss="dieses Video zum Inflow (nicht diese / zur Inflow)" status=active
E Focus_inflow_compact_bilibili FROM_SESSION Session_inflow_compact_bilibili
V Lemma_de_fix_inflow_compact_bilibili kind=lemma lang=de surface="Fügen Sie dieses Video zum Inflow hinzu. Thema: Wa" role=minimal-rewrite
E Lemma_de_fix_inflow_compact_bilibili FROM_SESSION Session_inflow_compact_bilibili SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-inflow-compact-bilibili.toon.md
V Form_fix_inflow_compact_bilibili_0_dieses_vid kind=form lang=de surface="dieses Video" fixes=diese
E Form_fix_inflow_compact_bilibili_0_dieses_vid FROM_SESSION Session_inflow_compact_bilibili
V Form_fix_inflow_compact_bilibili_1_zum_inflow kind=form lang=de surface="zum Inflow" fixes="zur Inflow"
E Form_fix_inflow_compact_bilibili_1_zum_inflow FROM_SESSION Session_inflow_compact_bilibili
V Form_fix_inflow_compact_bilibili_2_hilfreich kind=form lang=de surface=Hilfreich fixes=Hilfsreich
E Form_fix_inflow_compact_bilibili_2_hilfreich FROM_SESSION Session_inflow_compact_bilibili
V Form_fix_inflow_compact_bilibili_3_interviewg kind=form lang=de surface=Interviewgespräch fixes=Interviewsgespräch
E Form_fix_inflow_compact_bilibili_3_interviewg FROM_SESSION Session_inflow_compact_bilibili

# ingest-session 2026-09-08T15:29:09Z hook-json-parse lang=de
V Session_hook_json_parse kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-hook-json-parse.toon.md
V Focus_hook_json_parse kind=focus lang=de gloss="immer noch danach (nicht IMMER NOCH nachdem ohne V" status=active
E Focus_hook_json_parse FROM_SESSION Session_hook_json_parse
V Lemma_de_fix_hook_json_parse kind=lemma lang=de surface="Genau: warum gibt es danach immer noch keine Aktua" role=minimal-rewrite
E Lemma_de_fix_hook_json_parse FROM_SESSION Session_hook_json_parse SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-hook-json-parse.toon.md
V Form_fix_hook_json_parse_0_immer_noch_danach kind=form lang=de surface="immer noch danach" fixes="IMMER NOCH nachdem"
E Form_fix_hook_json_parse_0_immer_noch_danach FROM_SESSION Session_hook_json_parse
V Form_fix_hook_json_parse_1_danach_immer_noch_ kind=form lang=de surface="danach immer noch keine Aktualisierung" fixes="keine Aktualisierung"
E Form_fix_hook_json_parse_1_danach_immer_noch_ FROM_SESSION Session_hook_json_parse
V Form_fix_hook_json_parse_2_warum_gibt_es_dana kind=form lang=de surface="warum gibt es danach …" fixes="warum gibt es … nachdem"
E Form_fix_hook_json_parse_2_warum_gibt_es_dana FROM_SESSION Session_hook_json_parse

# auto-gap 2026-09-08T15:30:43Z surface=眉
V Concept_gap_zh_3f927a74e6 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_3f927a74e6 kind=gap lang=zh surface=眉 target=de status=open
V Lemma_zh_zh_3f927a74e6 kind=lemma lang=zh surface=眉
E Concept_gap_zh_3f927a74e6 EXPRESSES Lemma_zh_zh_3f927a74e6 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_3f927a74e6 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_3f927a74e6 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-08T15:31:39Z workout-planung-heute lang=de
V Session_workout_planung_heute kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-workout-planung-heute.toon.md
V Focus_workout_planung_heute kind=focus lang=de gloss="Planung (nicht Plannung)" status=active
E Focus_workout_planung_heute FROM_SESSION Session_workout_planung_heute
V Lemma_de_fix_workout_planung_heute kind=lemma lang=de surface="Okay, mach mir eine Workout-Planung für heute." role=minimal-rewrite
E Lemma_de_fix_workout_planung_heute FROM_SESSION Session_workout_planung_heute SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-workout-planung-heute.toon.md
V Form_fix_workout_planung_heute_0_planung kind=form lang=de surface=Planung fixes=Plannung
E Form_fix_workout_planung_heute_0_planung FROM_SESSION Session_workout_planung_heute
V Form_fix_workout_planung_heute_1_workout_plan kind=form lang=de surface=Workout-Planung fixes="Workout Plannung"
E Form_fix_workout_planung_heute_1_workout_plan FROM_SESSION Session_workout_planung_heute

# ingest-session 2026-09-08T15:33:49Z fog-mundgeschwuer-log lang=de
V Session_fog_mundgeschwuer_log kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-fog-mundgeschwuer-log.toon.md
V Focus_fog_mundgeschwuer_log kind=focus lang=de gloss="Ich logge (Verbzweitstellung), nicht Loggen ich" status=active
E Focus_fog_mundgeschwuer_log FROM_SESSION Session_fog_mundgeschwuer_log
V Lemma_de_fix_fog_mundgeschwuer_log kind=lemma lang=de surface="Ich logge noch: Brain Fog ist noch da, und das Mun" role=minimal-rewrite
E Lemma_de_fix_fog_mundgeschwuer_log FROM_SESSION Session_fog_mundgeschwuer_log SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-fog-mundgeschwuer-log.toon.md
V Form_fix_fog_mundgeschwuer_log_0_ich_logge kind=form lang=de surface="Ich logge" fixes="Loggen ich"
E Form_fix_fog_mundgeschwuer_log_0_ich_logge FROM_SESSION Session_fog_mundgeschwuer_log
V Form_fix_fog_mundgeschwuer_log_1_und_das_mund kind=form lang=de surface="und das Mundgeschwür auch noch" fixes="mit Mundgeschwür noch"
E Form_fix_fog_mundgeschwuer_log_1_und_das_mund FROM_SESSION Session_fog_mundgeschwuer_log

# auto-gap 2026-09-08T16:15:53Z surface=鈥
V Concept_gap_zh_6d9a534a9b kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_6d9a534a9b kind=gap lang=zh surface=鈥 target=de status=open
V Lemma_zh_zh_6d9a534a9b kind=lemma lang=zh surface=鈥
E Concept_gap_zh_6d9a534a9b EXPRESSES Lemma_zh_zh_6d9a534a9b SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_6d9a534a9b GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_6d9a534a9b GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-08T16:15:53Z surface=脳
V Concept_gap_zh_bb6bff359c kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_bb6bff359c kind=gap lang=zh surface=脳 target=de status=open
V Lemma_zh_zh_bb6bff359c kind=lemma lang=zh surface=脳
E Concept_gap_zh_bb6bff359c EXPRESSES Lemma_zh_zh_bb6bff359c SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_bb6bff359c GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_bb6bff359c GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-08T16:15:53Z surface=鈫
V Concept_gap_zh_8ec0d425c5 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_8ec0d425c5 kind=gap lang=zh surface=鈫 target=de status=open
V Lemma_zh_zh_8ec0d425c5 kind=lemma lang=zh surface=鈫
E Concept_gap_zh_8ec0d425c5 EXPRESSES Lemma_zh_zh_8ec0d425c5 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_8ec0d425c5 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_8ec0d425c5 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-08T16:15:53Z surface=鈥擻
V Concept_gap_zh_6e9b7b456f kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_6e9b7b456f kind=gap lang=zh surface=鈥擻 target=de status=open
V Lemma_zh_zh_6e9b7b456f kind=lemma lang=zh surface=鈥擻
E Concept_gap_zh_6e9b7b456f EXPRESSES Lemma_zh_zh_6e9b7b456f SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_6e9b7b456f GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_6e9b7b456f GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-08T16:15:53Z surface=盲
V Concept_gap_zh_2027cd8b42 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_2027cd8b42 kind=gap lang=zh surface=盲 target=de status=open
V Lemma_zh_zh_2027cd8b42 kind=lemma lang=zh surface=盲
E Concept_gap_zh_2027cd8b42 EXPRESSES Lemma_zh_zh_2027cd8b42 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_2027cd8b42 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_2027cd8b42 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-08T16:15:53Z surface=鈥檚
V Concept_gap_zh_ed953a54b7 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_ed953a54b7 kind=gap lang=zh surface=鈥檚 target=de status=open
V Lemma_zh_zh_ed953a54b7 kind=lemma lang=zh surface=鈥檚
E Concept_gap_zh_ed953a54b7 EXPRESSES Lemma_zh_zh_ed953a54b7 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_ed953a54b7 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_ed953a54b7 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-08T16:15:53Z surface=枚
V Concept_gap_zh_517e214c06 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_517e214c06 kind=gap lang=zh surface=枚 target=de status=open
V Lemma_zh_zh_517e214c06 kind=lemma lang=zh surface=枚
E Concept_gap_zh_517e214c06 EXPRESSES Lemma_zh_zh_517e214c06 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_517e214c06 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_517e214c06 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-08T16:17:38Z andere-koerperteile lang=de
V Session_andere_koerperteile kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-andere-koerperteile.toon.md
V Focus_andere_koerperteile kind=focus lang=de gloss="andere Körperteile (Akk. Pl.), nicht anderes Körpe" status=active
E Focus_andere_koerperteile FROM_SESSION Session_andere_koerperteile
V Lemma_de_fix_andere_koerperteile kind=lemma lang=de surface="Ich hätte gern andere Körperteile zu trainieren." role=minimal-rewrite
E Lemma_de_fix_andere_koerperteile FROM_SESSION Session_andere_koerperteile SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-andere-koerperteile.toon.md
V Form_fix_andere_koerperteile_0_andere kind=form lang=de surface=andere fixes=anderes
E Form_fix_andere_koerperteile_0_andere FROM_SESSION Session_andere_koerperteile
V Form_fix_andere_koerperteile_1_k_rperteile_e8 kind=form lang=de surface=Körperteile fixes=Körperteilen
E Form_fix_andere_koerperteile_1_k_rperteile_e8 FROM_SESSION Session_andere_koerperteile

# ingest-session 2026-09-08T16:36:12Z nahrungsergaenzung-routine lang=de
V Session_nahrungsergaenzung_routine kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-nahrungsergaenzung-routine.toon.md
V Focus_nahrungsergaenzung_routine kind=focus lang=de gloss="anhand der gespeicherten Optionen (nicht nach vore" status=active
E Focus_nahrungsergaenzung_routine FROM_SESSION Session_nahrungsergaenzung_routine
V Lemma_de_fix_nahrungsergaenzung_routine kind=lemma lang=de surface="Gib mir Empfehlungen für Nahrungsergänzungsmittel " role=minimal-rewrite
E Lemma_de_fix_nahrungsergaenzung_routine FROM_SESSION Session_nahrungsergaenzung_routine SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-nahrungsergaenzung-routine.toon.md
V Form_fix_nahrungsergaenzung_routine_0_nahrung kind=form lang=de surface=Nahrungsergänzungsmittel fixes=Nährungsergänzungsmittel
E Form_fix_nahrungsergaenzung_routine_0_nahrung FROM_SESSION Session_nahrungsergaenzung_routine
V Form_fix_nahrungsergaenzung_routine_1_anhand_ kind=form lang=de surface="anhand der zuvor gespeicherten Optionen" fixes="nach vorerige gespeicherte Opt"
E Form_fix_nahrungsergaenzung_routine_1_anhand_ FROM_SESSION Session_nahrungsergaenzung_routine

# ingest-session 2026-09-08T16:42:10Z latexpdf-nahrung-workout lang=de
V Session_latexpdf_nahrung_workout kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-latexpdf-nahrung-workout.toon.md
V Focus_latexpdf_nahrung_workout kind=focus lang=de gloss="Nahrungsergänzungsmittel (nicht Nährung-)" status=active
E Focus_latexpdf_nahrung_workout FROM_SESSION Session_latexpdf_nahrung_workout
V Lemma_de_fix_latexpdf_nahrung_workout kind=lemma lang=de surface="Gib mir ein LaTeX-PDF für die heutigen Nahrungserg" role=minimal-rewrite
E Lemma_de_fix_latexpdf_nahrung_workout FROM_SESSION Session_latexpdf_nahrung_workout SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-latexpdf-nahrung-workout.toon.md
V Form_fix_latexpdf_nahrung_workout_0_nahrungse kind=form lang=de surface=Nahrungsergänzungsmittel fixes=Nährungsergänzungsmittel
E Form_fix_latexpdf_nahrung_workout_0_nahrungse FROM_SESSION Session_latexpdf_nahrung_workout
V Form_fix_latexpdf_nahrung_workout_1_die_heuti kind=form lang=de surface="die heutigen Nahrungsergänzungsmittel" fixes="heutige Nährungsergänzungsmitt"
E Form_fix_latexpdf_nahrung_workout_1_die_heuti FROM_SESSION Session_latexpdf_nahrung_workout
V Form_fix_latexpdf_nahrung_workout_2_workout_s kind=form lang=de surface=Workout-Session fixes="Workout session"
E Form_fix_latexpdf_nahrung_workout_2_workout_s FROM_SESSION Session_latexpdf_nahrung_workout

# auto-gap 2026-09-08T16:52:48Z surface=is
V Concept_gap_en_is kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_is kind=gap lang=en surface=is target=de status=open
V Lemma_en_en_is kind=lemma lang=en surface=is
E Concept_gap_en_is EXPRESSES Lemma_en_en_is SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_is GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_is GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-08T16:55:08Z gym-ist-beintraining-schwimmen lang=de
V Session_gym_ist_beintraining_schwimmen kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-gym-ist-beintraining-schwimmen.toon.md
V Focus_gym_ist_beintraining_schwimmen kind=focus lang=de gloss="Das Gym ist (nicht Gym is)" status=active
E Focus_gym_ist_beintraining_schwimmen FROM_SESSION Session_gym_ist_beintraining_schwimmen
V Lemma_de_fix_gym_ist_beintraining_schwimmen kind=lemma lang=de surface="Das Gym ist geöffnet. Benutzen wir das Gym für kur" role=minimal-rewrite
E Lemma_de_fix_gym_ist_beintraining_schwimmen FROM_SESSION Session_gym_ist_beintraining_schwimmen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-gym-ist-beintraining-schwimmen.toon.md
V Form_fix_gym_ist_beintraining_schwimmen_0_das kind=form lang=de surface="Das Gym ist geöffnet" fixes="Gym is geöffnet"
E Form_fix_gym_ist_beintraining_schwimmen_0_das FROM_SESSION Session_gym_ist_beintraining_schwimmen
V Form_fix_gym_ist_beintraining_schwimmen_1_kur kind=form lang=de surface="kurzes Beintraining" fixes="kurze Bein training"
E Form_fix_gym_ist_beintraining_schwimmen_1_kur FROM_SESSION Session_gym_ist_beintraining_schwimmen

# ingest-session 2026-09-08T18:29:30Z korrektur-hook-datei lang=de
V Session_korrektur_hook_datei kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-korrektur-hook-datei.toon.md
V Focus_korrektur_hook_datei kind=focus lang=de gloss="Verbposition: wenn-Satz Verb ans Ende, Hauptsatz V" status=active
E Focus_korrektur_hook_datei FROM_SESSION Session_korrektur_hook_datei
V Lemma_de_fix_korrektur_hook_datei kind=lemma lang=de surface="Ach so, hmm... Wenn ich auf Deutsch meine Meinung " role=minimal-rewrite
E Lemma_de_fix_korrektur_hook_datei FROM_SESSION Session_korrektur_hook_datei SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-korrektur-hook-datei.toon.md
V Form_fix_korrektur_hook_datei_0_ich kind=form lang=de surface=ich fixes=Ich
E Form_fix_korrektur_hook_datei_0_ich FROM_SESSION Session_korrektur_hook_datei
V Form_fix_korrektur_hook_datei_1_eingebe kind=form lang=de surface=eingebe fixes=eingeben
E Form_fix_korrektur_hook_datei_1_eingebe FROM_SESSION Session_korrektur_hook_datei
V Form_fix_korrektur_hook_datei_2_machst_du_die kind=form lang=de surface="machst du die Korrektur" fixes="machst du Korrigierung"
E Form_fix_korrektur_hook_datei_2_machst_du_die FROM_SESSION Session_korrektur_hook_datei
V Form_fix_korrektur_hook_datei_3_sie_muss kind=form lang=de surface="Sie muss" fixes="Es muß"
E Form_fix_korrektur_hook_datei_3_sie_muss FROM_SESSION Session_korrektur_hook_datei
V Form_fix_korrektur_hook_datei_4_aus_der_hook_ kind=form lang=de surface="aus der Hook-Datei stammen, ja?" fixes="von Hooks Datei stammen ja"
E Form_fix_korrektur_hook_datei_4_aus_der_hook_ FROM_SESSION Session_korrektur_hook_datei

# ingest-session 2026-09-08T19:24:30Z uebung-zum-sprachenlernen lang=de
V Session_uebung_zum_sprachenlernen kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-uebung-zum-sprachenlernen.toon.md
V Focus_uebung_zum_sprachenlernen kind=focus lang=de gloss="zu + Dativ/Pronomen: zu mir, zum Sprachenlernen (n" status=active
E Focus_uebung_zum_sprachenlernen FROM_SESSION Session_uebung_zum_sprachenlernen
V Lemma_de_fix_uebung_zum_sprachenlernen kind=lemma lang=de surface="Genau, kannst du mir im Augenblick eine Übung zum " role=minimal-rewrite
E Lemma_de_fix_uebung_zum_sprachenlernen FROM_SESSION Session_uebung_zum_sprachenlernen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-uebung-zum-sprachenlernen.toon.md
V Form_fix_uebung_zum_sprachenlernen_0_zu_mir kind=form lang=de surface="zu mir" fixes="zur mir"
E Form_fix_uebung_zum_sprachenlernen_0_zu_mir FROM_SESSION Session_uebung_zum_sprachenlernen
V Form_fix_uebung_zum_sprachenlernen_1_zum_spra kind=form lang=de surface="zum Sprachenlernen" fixes="auf Sprache lernen"
E Form_fix_uebung_zum_sprachenlernen_1_zum_spra FROM_SESSION Session_uebung_zum_sprachenlernen
V Form_fix_uebung_zum_sprachenlernen_2_mir_eine kind=form lang=de surface="mir eine Übung" fixes="mir Übung"
E Form_fix_uebung_zum_sprachenlernen_2_mir_eine FROM_SESSION Session_uebung_zum_sprachenlernen
V Form_fix_uebung_zum_sprachenlernen_3_im_augen kind=form lang=de surface="im Augenblick zu mir schicken" fixes="augenblick zur mir schicken"
E Form_fix_uebung_zum_sprachenlernen_3_im_augen FROM_SESSION Session_uebung_zum_sprachenlernen

# ingest-session 2026-09-08T19:38:35Z rueckmeldung-drill-quality lang=de
V Session_rueckmeldung_drill_quality kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-rueckmeldung-drill-quality.toon.md
V Focus_rueckmeldung_drill_quality kind=focus lang=de gloss="Stell sicher, dass … erfasst wird (Kollokation + P" status=active
E Focus_rueckmeldung_drill_quality FROM_SESSION Session_rueckmeldung_drill_quality
V Lemma_de_fix_rueckmeldung_drill_quality kind=lemma lang=de surface="Stell sicher, dass meine Rückmeldung aus der Skill" role=minimal-rewrite
E Lemma_de_fix_rueckmeldung_drill_quality FROM_SESSION Session_rueckmeldung_drill_quality SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-rueckmeldung-drill-quality.toon.md
V Form_fix_rueckmeldung_drill_quality_0_stell_s kind=form lang=de surface="Stell sicher" fixes="Mach sicherstellen"
E Form_fix_rueckmeldung_drill_quality_0_stell_s FROM_SESSION Session_rueckmeldung_drill_quality
V Form_fix_rueckmeldung_drill_quality_1_aus_der kind=form lang=de surface="aus der Skill-Datei" fixes="von Skill Datei"
E Form_fix_rueckmeldung_drill_quality_1_aus_der FROM_SESSION Session_rueckmeldung_drill_quality
V Form_fix_rueckmeldung_drill_quality_2_erfasst kind=form lang=de surface="erfasst wird" fixes="erzeugt erfasst"
E Form_fix_rueckmeldung_drill_quality_2_erfasst FROM_SESSION Session_rueckmeldung_drill_quality

# ingest-session 2026-09-08T19:41:02Z html-datei-ab-jetzt lang=de
V Session_html_datei_ab_jetzt kind=session date=2026-09-08 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-html-datei-ab-jetzt.toon.md
V Focus_html_datei_ab_jetzt kind=focus lang=de gloss="Register konsistent halten: du (schick), nicht Sie" status=active
E Focus_html_datei_ab_jetzt FROM_SESSION Session_html_datei_ab_jetzt
V Lemma_de_fix_html_datei_ab_jetzt kind=lemma lang=de surface="Ach so, bitte schick mir die HTML-Datei, und ich m" role=minimal-rewrite
E Lemma_de_fix_html_datei_ab_jetzt FROM_SESSION Session_html_datei_ab_jetzt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-08-html-datei-ab-jetzt.toon.md
V Form_fix_html_datei_ab_jetzt_0_schick kind=form lang=de surface=schick fixes="schicken Sie"
E Form_fix_html_datei_ab_jetzt_0_schick FROM_SESSION Session_html_datei_ab_jetzt

# ingest-session 2026-09-09T09:38:21Z zusammenfassung-tag-starten lang=de
V Session_zusammenfassung_tag_starten kind=session date=2026-09-09 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-09-zusammenfassung-tag-starten.toon.md
V Focus_zusammenfassung_tag_starten kind=focus lang=de gloss="eine Zusammenfassung (Akk. f.), nicht ein Zusammen" status=active
E Focus_zusammenfassung_tag_starten FROM_SESSION Session_zusammenfassung_tag_starten
V Lemma_de_fix_zusammenfassung_tag_starten kind=lemma lang=de surface="Gib mir eine Zusammenfassung als LaTeX-PDF von der" role=minimal-rewrite
E Lemma_de_fix_zusammenfassung_tag_starten FROM_SESSION Session_zusammenfassung_tag_starten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-09-zusammenfassung-tag-starten.toon.md
V Form_fix_zusammenfassung_tag_starten_0_eine_z kind=form lang=de surface="eine Zusammenfassung" fixes="ein Zusammenfassung"
E Form_fix_zusammenfassung_tag_starten_0_eine_z FROM_SESSION Session_zusammenfassung_tag_starten
V Form_fix_zusammenfassung_tag_starten_1_meinen kind=form lang=de surface="meinen Tag" fixes="meine Tag"
E Form_fix_zusammenfassung_tag_starten_1_meinen FROM_SESSION Session_zusammenfassung_tag_starten
V Form_fix_zusammenfassung_tag_starten_2_w_hren kind=form lang=de surface="während ich geschlafen habe" fixes="während meinem Schlafen"
E Form_fix_zusammenfassung_tag_starten_2_w_hren FROM_SESSION Session_zusammenfassung_tag_starten

# auto-gap 2026-09-10T13:36:05Z surface=琛屽姩鎵嬪唽
V Concept_gap_zh_8b6dde6f31 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_8b6dde6f31 kind=gap lang=zh surface=琛屽姩鎵嬪唽 target=de status=open
V Lemma_zh_zh_8b6dde6f31 kind=lemma lang=zh surface=琛屽姩鎵嬪唽
E Concept_gap_zh_8b6dde6f31 EXPRESSES Lemma_zh_zh_8b6dde6f31 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_8b6dde6f31 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_8b6dde6f31 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=鍔冲姩娉曢櫌璧疯瘔锛堢珛鍗虫墽琛岋級
V Concept_gap_zh_1c8c130b62 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_1c8c130b62 kind=gap lang=zh surface=鍔冲姩娉曢櫌璧疯瘔锛堢珛鍗虫墽琛岋級 target=de status=open
V Lemma_zh_zh_1c8c130b62 kind=lemma lang=zh surface=鍔冲姩娉曢櫌璧疯瘔锛堢珛鍗虫墽琛岋級
E Concept_gap_zh_1c8c130b62 EXPRESSES Lemma_zh_zh_1c8c130b62 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_1c8c130b62 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_1c8c130b62 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=路
V Concept_gap_zh_965a593a6c kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_965a593a6c kind=gap lang=zh surface=路 target=de status=open
V Lemma_zh_zh_965a593a6c kind=lemma lang=zh surface=路
E Concept_gap_zh_965a593a6c EXPRESSES Lemma_zh_zh_965a593a6c SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_965a593a6c GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_965a593a6c GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=路瑙
V Concept_gap_zh_37f001227b kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_37f001227b kind=gap lang=zh surface=路瑙 target=de status=open
V Lemma_zh_zh_37f001227b kind=lemma lang=zh surface=路瑙
E Concept_gap_zh_37f001227b EXPRESSES Lemma_zh_zh_37f001227b SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_37f001227b GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_37f001227b GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=泧淇濇姢姝荤嚎
V Concept_gap_zh_c1c6109a3a kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_c1c6109a3a kind=gap lang=zh surface=泧淇濇姢姝荤嚎 target=de status=open
V Lemma_zh_zh_c1c6109a3a kind=lemma lang=zh surface=泧淇濇姢姝荤嚎
E Concept_gap_zh_c1c6109a3a EXPRESSES Lemma_zh_zh_c1c6109a3a SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_c1c6109a3a GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_c1c6109a3a GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=闈炲緥甯堟剰瑙併
V Concept_gap_zh_eea8e8d90e kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_eea8e8d90e kind=gap lang=zh surface=闈炲緥甯堟剰瑙併 target=de status=open
V Lemma_zh_zh_eea8e8d90e kind=lemma lang=zh surface=闈炲緥甯堟剰瑙併
E Concept_gap_zh_eea8e8d90e EXPRESSES Lemma_zh_zh_eea8e8d90e SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_eea8e8d90e GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_eea8e8d90e GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=傜
V Concept_gap_zh_e261010de5 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_e261010de5 kind=gap lang=zh surface=傜 target=de status=open
V Lemma_zh_zh_e261010de5 kind=lemma lang=zh surface=傜
E Concept_gap_zh_e261010de5 EXPRESSES Lemma_zh_zh_e261010de5 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_e261010de5 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_e261010de5 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=瀛椼
V Concept_gap_zh_a9e0e1319f kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_a9e0e1319f kind=gap lang=zh surface=瀛椼 target=de status=open
V Lemma_zh_zh_a9e0e1319f kind=lemma lang=zh surface=瀛椼
E Concept_gap_zh_a9e0e1319f EXPRESSES Lemma_zh_zh_a9e0e1319f SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_a9e0e1319f GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_a9e0e1319f GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=佷氦浠躲
V Concept_gap_zh_13c1376b99 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_13c1376b99 kind=gap lang=zh surface=佷氦浠躲 target=de status=open
V Lemma_zh_zh_13c1376b99 kind=lemma lang=zh surface=佷氦浠躲
E Concept_gap_zh_13c1376b99 EXPRESSES Lemma_zh_zh_13c1376b99 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_13c1376b99 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_13c1376b99 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=佹椂鏁堣嚜璐熴
V Concept_gap_zh_64701acc5d kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_64701acc5d kind=gap lang=zh surface=佹椂鏁堣嚜璐熴 target=de status=open
V Lemma_zh_zh_64701acc5d kind=lemma lang=zh surface=佹椂鏁堣嚜璐熴
E Concept_gap_zh_64701acc5d EXPRESSES Lemma_zh_zh_64701acc5d SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_64701acc5d GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_64701acc5d GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=傚叺璐电
V Concept_gap_zh_595b3afc1d kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_595b3afc1d kind=gap lang=zh surface=傚叺璐电 target=de status=open
V Lemma_zh_zh_595b3afc1d kind=lemma lang=zh surface=傚叺璐电
E Concept_gap_zh_595b3afc1d EXPRESSES Lemma_zh_zh_595b3afc1d SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_595b3afc1d GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_595b3afc1d GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=閫燂細浠婂
V Concept_gap_zh_bfd5693365 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_bfd5693365 kind=gap lang=zh surface=閫燂細浠婂 target=de status=open
V Lemma_zh_zh_bfd5693365 kind=lemma lang=zh surface=閫燂細浠婂
E Concept_gap_zh_bfd5693365 EXPRESSES Lemma_zh_zh_bfd5693365 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_bfd5693365 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_bfd5693365 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=鍏
V Concept_gap_zh_d051953952 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_d051953952 kind=gap lang=zh surface=鍏 target=de status=open
V Lemma_zh_zh_d051953952 kind=lemma lang=zh surface=鍏
E Concept_gap_zh_d051953952 EXPRESSES Lemma_zh_zh_d051953952 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_d051953952 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_d051953952 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=銆俓
V Concept_gap_zh_ecb62ea815 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_ecb62ea815 kind=gap lang=zh surface=銆俓 target=de status=open
V Lemma_zh_zh_ecb62ea815 kind=lemma lang=zh surface=銆俓
E Concept_gap_zh_ecb62ea815 EXPRESSES Lemma_zh_zh_ecb62ea815 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_ecb62ea815 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_ecb62ea815 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=涓
V Concept_gap_zh_b3f6aadac0 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_b3f6aadac0 kind=gap lang=zh surface=涓 target=de status=open
V Lemma_zh_zh_b3f6aadac0 kind=lemma lang=zh surface=涓
E Concept_gap_zh_b3f6aadac0 EXPRESSES Lemma_zh_zh_b3f6aadac0 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_b3f6aadac0 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_b3f6aadac0 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=鍙
V Concept_gap_zh_d3b67b7010 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_d3b67b7010 kind=gap lang=zh surface=鍙 target=de status=open
V Lemma_zh_zh_d3b67b7010 kind=lemma lang=zh surface=鍙
E Concept_gap_zh_d3b67b7010 EXPRESSES Lemma_zh_zh_d3b67b7010 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_d3b67b7010 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_d3b67b7010 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=瘽锛氫粖澶
V Concept_gap_zh_eb5a967850 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_eb5a967850 kind=gap lang=zh surface=瘽锛氫粖澶 target=de status=open
V Lemma_zh_zh_eb5a967850 kind=lemma lang=zh surface=瘽锛氫粖澶
E Concept_gap_zh_eb5a967850 EXPRESSES Lemma_zh_zh_eb5a967850 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_eb5a967850 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_eb5a967850 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-10T13:36:05Z surface=濂借瘔鐘
V Concept_gap_zh_11c01aea58 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_11c01aea58 kind=gap lang=zh surface=濂借瘔鐘 target=de status=open
V Lemma_zh_zh_11c01aea58 kind=lemma lang=zh surface=濂借瘔鐘
E Concept_gap_zh_11c01aea58 EXPRESSES Lemma_zh_zh_11c01aea58 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_11c01aea58 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_11c01aea58 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-10T13:38:54Z in-private-aufnehmen lang=de
V Session_in_private_aufnehmen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-in-private-aufnehmen.toon.md
V Focus_in_private_aufnehmen kind=focus lang=de gloss="in .private (Akk bei Richtung), nicht 里边 ohne in+A" status=active
E Focus_in_private_aufnehmen FROM_SESSION Session_in_private_aufnehmen
V Lemma_de_fix_in_private_aufnehmen kind=lemma lang=de surface="Nimm das in .private auf." role=minimal-rewrite
E Lemma_de_fix_in_private_aufnehmen FROM_SESSION Session_in_private_aufnehmen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-in-private-aufnehmen.toon.md
V Form_fix_in_private_aufnehmen_0_nimm_das_in_p kind=form lang=de surface="Nimm das in .private auf" fixes=这个加入private里边
E Form_fix_in_private_aufnehmen_0_nimm_das_in_p FROM_SESSION Session_in_private_aufnehmen

# ingest-session 2026-09-10T13:56:09Z chatbasierte-lueckentexte lang=de
V Session_chatbasierte_lueckentexte kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-chatbasierte-lueckentexte.toon.md
V Focus_chatbasierte_lueckentexte kind=focus lang=de gloss="Gib mir + Akkusativ — Gib mir eine Lückentext-Aufg" status=active
E Focus_chatbasierte_lueckentexte FROM_SESSION Session_chatbasierte_lueckentexte
V Lemma_de_fix_chatbasierte_lueckentexte kind=lemma lang=de surface="Okay, gib mir chatbasierte Übungen auf Deutsch. Gi" role=minimal-rewrite
E Lemma_de_fix_chatbasierte_lueckentexte FROM_SESSION Session_chatbasierte_lueckentexte SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-chatbasierte-lueckentexte.toon.md
V Form_fix_chatbasierte_lueckentexte_0_gib_mir_ kind=form lang=de surface="Gib mir abwechselnd Lückentext-Aufgaben." fixes="Gib mir Lücke einfüllen Aufgab"
E Form_fix_chatbasierte_lueckentexte_0_gib_mir_ FROM_SESSION Session_chatbasierte_lueckentexte

# ingest-session 2026-09-10T13:57:54Z wissensgraph-rueckmeldung lang=de
V Session_wissensgraph_rueckmeldung kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-wissensgraph-rueckmeldung.toon.md
V Focus_wissensgraph_rueckmeldung kind=focus lang=de gloss="Rückmeldung zu + Dativ — Rückmeldung zum Wissensgr" status=active
E Focus_wissensgraph_rueckmeldung FROM_SESSION Session_wissensgraph_rueckmeldung
V Lemma_de_fix_wissensgraph_rueckmeldung kind=lemma lang=de surface="Warte, gibt es Rückmeldung zum Wissensgraphen?" role=minimal-rewrite
E Lemma_de_fix_wissensgraph_rueckmeldung FROM_SESSION Session_wissensgraph_rueckmeldung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-wissensgraph-rueckmeldung.toon.md
V Form_fix_wissensgraph_rueckmeldung_0_r_ckmeld kind=form lang=de surface="Rückmeldung zum Wissensgraphen" fixes="Rückmeldung zur Kenntnis-graph"
E Form_fix_wissensgraph_rueckmeldung_0_r_ckmeld FROM_SESSION Session_wissensgraph_rueckmeldung

# ingest-session 2026-09-10T13:59:14Z zehn-fragen lang=de
V Session_zehn_fragen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-zehn-fragen.toon.md
V Focus_zehn_fragen kind=focus lang=de gloss="Frag mich + Akkusativ — Frag mich zehn Fragen." status=active
E Focus_zehn_fragen FROM_SESSION Session_zehn_fragen
V Lemma_de_fix_zehn_fragen kind=lemma lang=de surface="Okay, frag mich zehn Fragen." role=minimal-rewrite
E Lemma_de_fix_zehn_fragen FROM_SESSION Session_zehn_fragen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-zehn-fragen.toon.md
V Form_fix_zehn_fragen_0_frag_mich_zehn_fragen kind=form lang=de surface="frag mich zehn Fragen" fixes="frag mir 10 Frage"
E Form_fix_zehn_fragen_0_frag_mich_zehn_fragen FROM_SESSION Session_zehn_fragen

# ingest-session 2026-09-10T13:59:57Z lueckenuebungen-nicht-fragen lang=de
V Session_lueckenuebungen_nicht_fragen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebungen-nicht-fragen.toon.md
V Focus_lueckenuebungen_nicht_fragen kind=focus lang=de gloss="Lückenübungen — zusammengesetztes Nomen im Plural." status=active
E Focus_lueckenuebungen_nicht_fragen FROM_SESSION Session_lueckenuebungen_nicht_fragen
V Lemma_de_fix_lueckenuebungen_nicht_fragen kind=lemma lang=de surface="Nein, nein, nein – Lückenübungen." role=minimal-rewrite
E Lemma_de_fix_lueckenuebungen_nicht_fragen FROM_SESSION Session_lueckenuebungen_nicht_fragen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebungen-nicht-fragen.toon.md
V Form_fix_lueckenuebungen_nicht_fragen_0_l_cke kind=form lang=de surface=Lückenübungen fixes="Lücke Übungen"
E Form_fix_lueckenuebungen_nicht_fragen_0_l_cke FROM_SESSION Session_lueckenuebungen_nicht_fragen

# ingest-session 2026-09-10T14:00:56Z lueckenuebung-konjunktiv-ii-zeit lang=de
V Session_lueckenuebung_konjunktiv_ii_zeit kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebung-konjunktiv-ii-zeit.toon.md
V Focus_lueckenuebung_konjunktiv_ii_zeit kind=focus lang=de gloss="wenn + Konjunktiv II, dann würde + Infinitiv — Wen" status=active
E Focus_lueckenuebung_konjunktiv_ii_zeit FROM_SESSION Session_lueckenuebung_konjunktiv_ii_zeit
V Lemma_de_fix_lueckenuebung_konjunktiv_ii_zeit kind=lemma lang=de surface="Wenn ich mehr Zeit hätte, würde ich das Projekt gr" role=minimal-rewrite
E Lemma_de_fix_lueckenuebung_konjunktiv_ii_zeit FROM_SESSION Session_lueckenuebung_konjunktiv_ii_zeit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebung-konjunktiv-ii-zeit.toon.md
V Form_fix_lueckenuebung_konjunktiv_ii_zeit_0_h kind=form lang=de surface=hätte fixes=habe
E Form_fix_lueckenuebung_konjunktiv_ii_zeit_0_h FROM_SESSION Session_lueckenuebung_konjunktiv_ii_zeit

# ingest-session 2026-09-10T14:03:16Z lueckenuebung-vertrag-unterzeichnet lang=de
V Session_lueckenuebung_vertrag_unterzeichnet kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebung-vertrag-unterzeichnet.toon.md
V Focus_lueckenuebung_vertrag_unterzeichnet kind=focus lang=de gloss="einen Vertrag unterzeichnen — Der Vertrag wurde un" status=active
E Focus_lueckenuebung_vertrag_unterzeichnet FROM_SESSION Session_lueckenuebung_vertrag_unterzeichnet
V Lemma_de_fix_lueckenuebung_vertrag_unterzeichnet kind=lemma lang=de surface="Wäre der Vertrag nicht rechtzeitig unterzeichnet w" role=minimal-rewrite
E Lemma_de_fix_lueckenuebung_vertrag_unterzeichnet FROM_SESSION Session_lueckenuebung_vertrag_unterzeichnet SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-lueckenuebung-vertrag-unterzeichnet.toon.md
V Form_fix_lueckenuebung_vertrag_unterzeichnet_ kind=form lang=de surface=unterzeichnet fixes=geschrieben
E Form_fix_lueckenuebung_vertrag_unterzeichnet_ FROM_SESSION Session_lueckenuebung_vertrag_unterzeichnet

# ingest-session 2026-09-11T14:45:36Z bei-mir-rhythmus lang=de
V Session_bei_mir_rhythmus kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-bei-mir-rhythmus.toon.md
V Focus_bei_mir_rhythmus kind=focus lang=de gloss="Adverb jetzt steht vor der Präpositionalgruppe — B" status=active
E Focus_bei_mir_rhythmus FROM_SESSION Session_bei_mir_rhythmus
V Lemma_de_fix_bei_mir_rhythmus kind=lemma lang=de surface="Bist du jetzt bei mir?" role=minimal-rewrite
E Lemma_de_fix_bei_mir_rhythmus FROM_SESSION Session_bei_mir_rhythmus SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-bei-mir-rhythmus.toon.md
V Form_fix_bei_mir_rhythmus_0_bist_du_jetzt_bei kind=form lang=de surface="Bist du jetzt bei mir?" fixes="Bist du bei mir jetzt?"
E Form_fix_bei_mir_rhythmus_0_bist_du_jetzt_bei FROM_SESSION Session_bei_mir_rhythmus

# ingest-session 2026-09-11T14:46:18Z einwaende-geprueft lang=de
V Session_einwaende_geprueft kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-einwaende-geprueft.toon.md
V Focus_einwaende_geprueft kind=focus lang=de gloss="Einwände prüfen — Präpositionalobjekt passt besser" status=active
E Focus_einwaende_geprueft FROM_SESSION Session_einwaende_geprueft
V Lemma_de_fix_einwaende_geprueft kind=lemma lang=de surface="Er bestand darauf, die Entscheidung erst zu treffe" role=minimal-rewrite
E Lemma_de_fix_einwaende_geprueft FROM_SESSION Session_einwaende_geprueft SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-einwaende-geprueft.toon.md

# ingest-session 2026-09-11T14:52:25Z vorlaeufige-werte-betonen lang=de
V Session_vorlaeufige_werte_betonen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-vorlaeufige-werte-betonen.toon.md
V Focus_vorlaeufige_werte_betonen kind=focus lang=de gloss="betonen, dass — Man muss betonen, dass …" status=active
E Focus_vorlaeufige_werte_betonen FROM_SESSION Session_vorlaeufige_werte_betonen
V Lemma_de_fix_vorlaeufige_werte_betonen kind=lemma lang=de surface="Man muss betonen, dass es sich bei den Zahlen um v" role=minimal-rewrite
E Lemma_de_fix_vorlaeufige_werte_betonen FROM_SESSION Session_vorlaeufige_werte_betonen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-vorlaeufige-werte-betonen.toon.md
V Form_fix_vorlaeufige_werte_betonen_0_betonen kind=form lang=de surface=betonen fixes=anstrengen
E Form_fix_vorlaeufige_werte_betonen_0_betonen FROM_SESSION Session_vorlaeufige_werte_betonen

# ingest-session 2026-09-11T14:53:03Z entwicklung-rueckgaengig-werden lang=de
V Session_entwicklung_rueckgaengig_werden kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-entwicklung-rueckgaengig-werden.toon.md
V Focus_entwicklung_rueckgaengig_werden kind=focus lang=de gloss="Passiv mit werden — gemacht werden wird (Passiv-In" status=active
E Focus_entwicklung_rueckgaengig_werden FROM_SESSION Session_entwicklung_rueckgaengig_werden
V Lemma_de_fix_entwicklung_rueckgaengig_werden kind=lemma lang=de surface="Es ist unwahrscheinlich, dass diese Entwicklung rü" role=minimal-rewrite
E Lemma_de_fix_entwicklung_rueckgaengig_werden FROM_SESSION Session_entwicklung_rueckgaengig_werden SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-entwicklung-rueckgaengig-werden.toon.md
V Form_fix_entwicklung_rueckgaengig_werden_0_we kind=form lang=de surface=werden fixes=haben
E Form_fix_entwicklung_rueckgaengig_werden_0_we FROM_SESSION Session_entwicklung_rueckgaengig_werden

# ingest-session 2026-09-12T13:09:16Z vorschlag-mehrheitlich-angenommen lang=de
V Session_vorschlag_mehrheitlich_angenommen kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-vorschlag-mehrheitlich-angenommen.toon.md
V Focus_vorschlag_mehrheitlich_angenommen kind=focus lang=de gloss="einen Vorschlag mehrheitlich annehmen." status=active
E Focus_vorschlag_mehrheitlich_angenommen FROM_SESSION Session_vorschlag_mehrheitlich_angenommen
V Lemma_de_fix_vorschlag_mehrheitlich_angenommen kind=lemma lang=de surface="Der Vorschlag wurde mehrheitlich angenommen, obwoh" role=minimal-rewrite
E Lemma_de_fix_vorschlag_mehrheitlich_angenommen FROM_SESSION Session_vorschlag_mehrheitlich_angenommen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-vorschlag-mehrheitlich-angenommen.toon.md
V Form_fix_vorschlag_mehrheitlich_angenommen_0_ kind=form lang=de surface=angenommen fixes=vorgestellt
E Form_fix_vorschlag_mehrheitlich_angenommen_0_ FROM_SESSION Session_vorschlag_mehrheitlich_angenommen

# ingest-session 2026-09-12T13:11:50Z ressourcenverbrauch-senken lang=de
V Session_ressourcenverbrauch_senken kind=session date=2026-09-10 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-ressourcenverbrauch-senken.toon.md
V Focus_ressourcenverbrauch_senken kind=focus lang=de gloss="den Ressourcenverbrauch senken." status=active
E Focus_ressourcenverbrauch_senken FROM_SESSION Session_ressourcenverbrauch_senken
V Lemma_de_fix_ressourcenverbrauch_senken kind=lemma lang=de surface="Die Maßnahme wurde eingeführt, um den Ressourcenve" role=minimal-rewrite
E Lemma_de_fix_ressourcenverbrauch_senken FROM_SESSION Session_ressourcenverbrauch_senken SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-10-ressourcenverbrauch-senken.toon.md
V Form_fix_ressourcenverbrauch_senken_0_senken kind=form lang=de surface=senken fixes=halten
E Form_fix_ressourcenverbrauch_senken_0_senken FROM_SESSION Session_ressourcenverbrauch_senken

# ingest-session 2026-09-12T13:14:46Z bedingungen-einigen lang=de
V Session_bedingungen_einigen kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-bedingungen-einigen.toon.md
V Focus_bedingungen_einigen kind=focus lang=de gloss="sich über + Akkusativ einigen — sich über die Bedi" status=active
E Focus_bedingungen_einigen FROM_SESSION Session_bedingungen_einigen
V Lemma_de_fix_bedingungen_einigen kind=lemma lang=de surface="Die Verhandlungen scheiterten nicht daran, dass di" role=minimal-rewrite
E Lemma_de_fix_bedingungen_einigen FROM_SESSION Session_bedingungen_einigen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-bedingungen-einigen.toon.md
V Form_fix_bedingungen_einigen_0_sich_ber_die_b kind=form lang=de surface="sich über die Bedingungen einigen" fixes="sich über die Bedingungen leis"
E Form_fix_bedingungen_einigen_0_sich_ber_die_b FROM_SESSION Session_bedingungen_einigen

# ingest-session 2026-09-12T13:17:04Z entscheidung-weil lang=de
V Session_entscheidung_weil kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-entscheidung-weil.toon.md
V Focus_entscheidung_weil kind=focus lang=de gloss="weil + Verb am Satzende — weil noch nicht alle Inf" status=active
E Focus_entscheidung_weil FROM_SESSION Session_entscheidung_weil
V Lemma_de_fix_entscheidung_weil kind=lemma lang=de surface="Die Entscheidung wurde vertagt, weil noch nicht al" role=minimal-rewrite
E Lemma_de_fix_entscheidung_weil FROM_SESSION Session_entscheidung_weil SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-entscheidung-weil.toon.md
V Form_fix_entscheidung_weil_0_weil kind=form lang=de surface=weil fixes=aber
E Form_fix_entscheidung_weil_0_weil FROM_SESSION Session_entscheidung_weil

# ingest-session 2026-09-12T13:20:05Z versaeumen-obwohl lang=de
V Session_versaeumen_obwohl kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-versaeumen-obwohl.toon.md
V Focus_versaeumen_obwohl kind=focus lang=de gloss="beim Wort + Dativ — beim Wort „versäumt“." status=active
E Focus_versaeumen_obwohl FROM_SESSION Session_versaeumen_obwohl
V Lemma_de_fix_versaeumen_obwohl kind=lemma lang=de surface="Keine Ahnung beim Wort „versäumt“. Wie lautet die " role=minimal-rewrite
E Lemma_de_fix_versaeumen_obwohl FROM_SESSION Session_versaeumen_obwohl SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-versaeumen-obwohl.toon.md
V Form_fix_versaeumen_obwohl_0_keine_ahnung_bei kind=form lang=de surface="Keine Ahnung beim Wort „versäumt“. Wie l" fixes="k.A auf Wort versäum, Antwort:"
E Form_fix_versaeumen_obwohl_0_keine_ahnung_bei FROM_SESSION Session_versaeumen_obwohl

# ingest-session 2026-09-12T13:21:12Z fehlerquellen-um-auszuschliessen lang=de
V Session_fehlerquellen_um_auszuschliessen kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-fehlerquellen-um-auszuschliessen.toon.md
V Focus_fehlerquellen_um_auszuschliessen kind=focus lang=de gloss="um + zu + Infinitiv — um Fehlerquellen auszuschlie" status=active
E Focus_fehlerquellen_um_auszuschliessen FROM_SESSION Session_fehlerquellen_um_auszuschliessen
V Lemma_de_fix_fehlerquellen_um_auszuschliessen kind=lemma lang=de surface="Die Daten wurden erneut ausgewertet, um mögliche F" role=minimal-rewrite
E Lemma_de_fix_fehlerquellen_um_auszuschliessen FROM_SESSION Session_fehlerquellen_um_auszuschliessen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-fehlerquellen-um-auszuschliessen.toon.md
V Form_fix_fehlerquellen_um_auszuschliessen_0_u kind=form lang=de surface=um fixes=trotz
E Form_fix_fehlerquellen_um_auszuschliessen_0_u FROM_SESSION Session_fehlerquellen_um_auszuschliessen

# ingest-session 2026-09-12T13:22:41Z auswerten-entscheidung-aussetzen lang=de
V Session_auswerten_entscheidung_aussetzen kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-auswerten-entscheidung-aussetzen.toon.md
V Focus_auswerten_entscheidung_aussetzen kind=focus lang=de gloss="eine Entscheidung aussetzen — setzte die Entscheid" status=active
E Focus_auswerten_entscheidung_aussetzen FROM_SESSION Session_auswerten_entscheidung_aussetzen
V Lemma_de_fix_auswerten_entscheidung_aussetzen kind=lemma lang=de surface="Neuer Wortschatz: „ausgewertet“. Antwort: „aus“?" role=minimal-rewrite
E Lemma_de_fix_auswerten_entscheidung_aussetzen FROM_SESSION Session_auswerten_entscheidung_aussetzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-auswerten-entscheidung-aussetzen.toon.md
V Form_fix_auswerten_entscheidung_aussetzen_0_a kind=form lang=de surface=aus fixes=ein
E Form_fix_auswerten_entscheidung_aussetzen_0_a FROM_SESSION Session_auswerten_entscheidung_aussetzen

# ingest-session 2026-09-12T13:23:31Z anzahl-luecken lang=de
V Session_anzahl_luecken kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-anzahl-luecken.toon.md
V Focus_anzahl_luecken kind=focus lang=de gloss="wie viele + Plural — Wie viele Lücken sind noch üb" status=active
E Focus_anzahl_luecken FROM_SESSION Session_anzahl_luecken
V Lemma_de_fix_anzahl_luecken kind=lemma lang=de surface="Wie viele Lücken sind noch übrig?" role=minimal-rewrite
E Lemma_de_fix_anzahl_luecken FROM_SESSION Session_anzahl_luecken SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-anzahl-luecken.toon.md
V Form_fix_anzahl_luecken_0_wie_viele_l_cken_si kind=form lang=de surface="Wie viele Lücken sind noch übrig?" fixes="Wie viel Lücke übrig?"
E Form_fix_anzahl_luecken_0_wie_viele_l_cken_si FROM_SESSION Session_anzahl_luecken

# ingest-session 2026-09-12T13:25:14Z png-leistungszusammenfassung lang=de
V Session_png_leistungszusammenfassung kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-png-leistungszusammenfassung.toon.md
V Focus_png_leistungszusammenfassung kind=focus lang=de gloss="mit + Dativ — mit den Ergebnissen." status=active
E Focus_png_leistungszusammenfassung FROM_SESSION Session_png_leistungszusammenfassung
V Lemma_de_fix_png_leistungszusammenfassung kind=lemma lang=de surface="Ach so. Gib mir eine PNG-Datei mit den Ergebnissen" role=minimal-rewrite
E Lemma_de_fix_png_leistungszusammenfassung FROM_SESSION Session_png_leistungszusammenfassung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-png-leistungszusammenfassung.toon.md
V Form_fix_png_leistungszusammenfassung_0_png_d kind=form lang=de surface="PNG-Datei mit den Ergebnissen und einer " fixes="PNG formattierte Datei, die Er"
E Form_fix_png_leistungszusammenfassung_0_png_d FROM_SESSION Session_png_leistungszusammenfassung

# auto-gap 2026-09-12T13:32:36Z surface=State
V Concept_gap_en_state kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_state kind=gap lang=en surface=State target=de status=open
V Lemma_en_en_state kind=lemma lang=en surface=State
E Concept_gap_en_state EXPRESSES Lemma_en_en_state SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_state GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_state GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-12T13:38:56Z in-den-privaten-ordner lang=de
V Session_in_den_privaten_ordner kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-in-den-privaten-ordner.toon.md
V Focus_in_den_privaten_ordner kind=focus lang=de gloss="in + Akk maskulin — Speichere das in den privaten " status=active
E Focus_in_den_privaten_ordner FROM_SESSION Session_in_den_privaten_ordner
V Lemma_de_fix_in_den_privaten_ordner kind=lemma lang=de surface="Speichere das nur in den privaten Ordner, ja?" role=minimal-rewrite
E Lemma_de_fix_in_den_privaten_ordner FROM_SESSION Session_in_den_privaten_ordner SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-in-den-privaten-ordner.toon.md
V Form_fix_in_den_privaten_ordner_0_speichere kind=form lang=de surface=Speichere fixes=State
E Form_fix_in_den_privaten_ordner_0_speichere FROM_SESSION Session_in_den_privaten_ordner
V Form_fix_in_den_privaten_ordner_1_in_den_priv kind=form lang=de surface="in den privaten Ordner" fixes="ins private Ordnern"
E Form_fix_in_den_privaten_ordner_1_in_den_priv FROM_SESSION Session_in_den_privaten_ordner
V Form_fix_in_den_privaten_ordner_2_das kind=form lang=de surface=das fixes="für dies"
E Form_fix_in_den_privaten_ordner_2_das FROM_SESSION Session_in_den_privaten_ordner

# auto-gap 2026-09-12T14:46:10Z surface=屏蔽门
V Concept_gap_zh_869d2c21e8 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_869d2c21e8 kind=gap lang=zh surface=屏蔽门 target=de status=open
V Lemma_zh_zh_869d2c21e8 kind=lemma lang=zh surface=屏蔽门
E Concept_gap_zh_869d2c21e8 EXPRESSES Lemma_zh_zh_869d2c21e8 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_869d2c21e8 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_869d2c21e8 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-12T14:48:37Z bahnsteigtueren lang=de
V Session_bahnsteigtueren kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-bahnsteigtueren.toon.md
V Focus_bahnsteigtueren kind=focus lang=de gloss="Dativ mit -en nach bei/auf — bei der Deutschen Bah" status=active
E Focus_bahnsteigtueren FROM_SESSION Session_bahnsteigtueren
V Lemma_de_fix_bahnsteigtueren kind=lemma lang=de surface="OK, eine zufällige Frage: Warum gibt es bei der De" role=minimal-rewrite
E Lemma_de_fix_bahnsteigtueren FROM_SESSION Session_bahnsteigtueren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-bahnsteigtueren.toon.md
V Form_fix_bahnsteigtueren_0_bei_der_deutschen_ kind=form lang=de surface="bei der Deutschen Bahn" fixes="bei der Deutsche Bahnsteig"
E Form_fix_bahnsteigtueren_0_bei_der_deutschen_ FROM_SESSION Session_bahnsteigtueren
V Form_fix_bahnsteigtueren_1_auf_deutschen_bahn kind=form lang=de surface="auf deutschen Bahnsteigen" fixes=bei/auf-Mix
E Form_fix_bahnsteigtueren_1_auf_deutschen_bahn FROM_SESSION Session_bahnsteigtueren
V Form_fix_bahnsteigtueren_2_bahnsteigt_ren_715 kind=form lang=de surface=Bahnsteigtüren fixes=屏蔽门
E Form_fix_bahnsteigtueren_2_bahnsteigt_ren_715 FROM_SESSION Session_bahnsteigtueren

# ingest-session 2026-09-12T14:54:57Z b2-teil1-anfrage lang=de
V Session_b2_teil1_anfrage kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-b2-teil1-anfrage.toon.md
V Focus_b2_teil1_anfrage kind=focus lang=de gloss="zur + Auswertung (Dativ f.) — nicht 'zum Auswertun" status=active
E Focus_b2_teil1_anfrage FROM_SESSION Session_b2_teil1_anfrage
V Lemma_de_fix_b2_teil1_anfrage kind=lemma lang=de surface="Ach so, ab jetzt: Gib mir eine Aufgabe zum Goethe " role=minimal-rewrite
E Lemma_de_fix_b2_teil1_anfrage FROM_SESSION Session_b2_teil1_anfrage SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-b2-teil1-anfrage.toon.md
V Form_fix_b2_teil1_anfrage_0_ausdruck kind=form lang=de surface=Ausdruck fixes=Austruck
E Form_fix_b2_teil1_anfrage_0_ausdruck FROM_SESSION Session_b2_teil1_anfrage
V Form_fix_b2_teil1_anfrage_1_eine_aufgabe_zum_ kind=form lang=de surface="eine Aufgabe zum Goethe B2, schriftliche" fixes="ein B2 goethe Schriftliche Aus"
E Form_fix_b2_teil1_anfrage_1_eine_aufgabe_zum_ FROM_SESSION Session_b2_teil1_anfrage
V Form_fix_b2_teil1_anfrage_2_danach_tippe_gebe kind=form lang=de surface="danach tippe/gebe ich … ein" fixes="demnächst gäbe ich … eingeben"
E Form_fix_b2_teil1_anfrage_2_danach_tippe_gebe FROM_SESSION Session_b2_teil1_anfrage
V Form_fix_b2_teil1_anfrage_3_absatz_f_r_absatz kind=form lang=de surface="Absatz für Absatz zur Auswertung" fixes="Paragraph pro Paragraph zum Au"
E Form_fix_b2_teil1_anfrage_3_absatz_f_r_absatz FROM_SESSION Session_b2_teil1_anfrage

# ingest-session 2026-09-12T15:14:46Z wissensgraph-kopten lang=de
V Session_wissensgraph_kopten kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-wissensgraph-kopten.toon.md
V Focus_wissensgraph_kopten kind=focus lang=de gloss="zu + Dativ maskulin — zum Wissensgraphen (Frame wi" status=active
E Focus_wissensgraph_kopten FROM_SESSION Session_wissensgraph_kopten
V Lemma_de_fix_wissensgraph_kopten kind=lemma lang=de surface="Füg das Wissen zum Wissensgraphen hinzu." role=minimal-rewrite
E Lemma_de_fix_wissensgraph_kopten FROM_SESSION Session_wissensgraph_kopten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-wissensgraph-kopten.toon.md
V Form_fix_wissensgraph_kopten_0_f_g_hinzu_8817 kind=form lang=de surface="Füg … hinzu" fixes="Fügen Sie … hinzu"
E Form_fix_wissensgraph_kopten_0_f_g_hinzu_8817 FROM_SESSION Session_wissensgraph_kopten
V Form_fix_wissensgraph_kopten_1_das_wissen kind=form lang=de surface="das Wissen" fixes="die Kenntnisse"
E Form_fix_wissensgraph_kopten_1_das_wissen FROM_SESSION Session_wissensgraph_kopten
V Form_fix_wissensgraph_kopten_2_wissensgraph kind=form lang=de surface=Wissensgraph fixes=Kenntnisse-Graph
E Form_fix_wissensgraph_kopten_2_wissensgraph FROM_SESSION Session_wissensgraph_kopten
V Form_fix_wissensgraph_kopten_3_zum_wissensgra kind=form lang=de surface="zum Wissensgraphen" fixes="zur Kenntnisse-Graph"
E Form_fix_wissensgraph_kopten_3_zum_wissensgra FROM_SESSION Session_wissensgraph_kopten

# ingest-session 2026-09-12T16:15:34Z b2-uebung-nochmal lang=de
V Session_b2_uebung_nochmal kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-b2-uebung-nochmal.toon.md
V Focus_b2_uebung_nochmal kind=focus lang=de gloss="Bestimmter Artikel vor modifiziertem Nomen — die u" status=active
E Focus_b2_uebung_nochmal FROM_SESSION Session_b2_uebung_nochmal
V Lemma_de_fix_b2_uebung_nochmal kind=lemma lang=de surface="OK, gib mir die ursprüngliche B2-Übung nochmal." role=minimal-rewrite
E Lemma_de_fix_b2_uebung_nochmal FROM_SESSION Session_b2_uebung_nochmal SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-b2-uebung-nochmal.toon.md
V Form_fix_b2_uebung_nochmal_0_die_urspr_nglich kind=form lang=de surface="die ursprüngliche B2-Übung" fixes="ursprüngliche B2 Übung"
E Form_fix_b2_uebung_nochmal_0_die_urspr_nglich FROM_SESSION Session_b2_uebung_nochmal
V Form_fix_b2_uebung_nochmal_1_gib_mir_nochmal_ kind=form lang=de surface="gib mir … nochmal" fixes="Gib mir … wieder"
E Form_fix_b2_uebung_nochmal_1_gib_mir_nochmal_ FROM_SESSION Session_b2_uebung_nochmal
V Form_fix_b2_uebung_nochmal_2_ok_gib kind=form lang=de surface="OK, gib" fixes="OK Gib"
E Form_fix_b2_uebung_nochmal_2_ok_gib FROM_SESSION Session_b2_uebung_nochmal

# ingest-session 2026-09-12T23:18:34Z in-tmp-aufnehmen lang=de
V Session_in_tmp_aufnehmen kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-in-tmp-aufnehmen.toon.md
V Focus_in_tmp_aufnehmen kind=focus lang=de gloss="in + Akk — Nimm das in tmp auf. (tmp hier wie ein " status=active
E Focus_in_tmp_aufnehmen FROM_SESSION Session_in_tmp_aufnehmen
V Lemma_de_fix_in_tmp_aufnehmen kind=lemma lang=de surface="Nimm das in tmp auf und spiel dort mit Playwright." role=minimal-rewrite
E Lemma_de_fix_in_tmp_aufnehmen FROM_SESSION Session_in_tmp_aufnehmen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-in-tmp-aufnehmen.toon.md
V Form_fix_in_tmp_aufnehmen_0_in_tmp kind=form lang=de surface="in tmp" fixes=在tmp里边
E Form_fix_in_tmp_aufnehmen_0_in_tmp FROM_SESSION Session_in_tmp_aufnehmen
V Form_fix_in_tmp_aufnehmen_1_spiel_dort_mit_pl kind=form lang=de surface="spiel dort mit Playwright" fixes=开始用playwright开始游玩
E Form_fix_in_tmp_aufnehmen_1_spiel_dort_mit_pl FROM_SESSION Session_in_tmp_aufnehmen

# ingest-session 2026-09-12T23:27:20Z screenshots-in-pdf lang=de
V Session_screenshots_in_pdf kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-screenshots-in-pdf.toon.md
V Focus_screenshots_in_pdf kind=focus lang=de gloss="in + Akk — nimm die Screenshots in das PDF hinein." status=active
E Focus_screenshots_in_pdf FROM_SESSION Session_screenshots_in_pdf
V Lemma_de_fix_screenshots_in_pdf kind=lemma lang=de surface="Erstell ein PDF mit LaTeX und nimm ein paar Schlüs" role=minimal-rewrite
E Lemma_de_fix_screenshots_in_pdf FROM_SESSION Session_screenshots_in_pdf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-screenshots-in-pdf.toon.md
V Form_fix_screenshots_in_pdf_0_nimm_hinein_d19 kind=form lang=de surface="nimm … hinein" fixes=放进去
E Form_fix_screenshots_in_pdf_0_nimm_hinein_d19 FROM_SESSION Session_screenshots_in_pdf
V Form_fix_screenshots_in_pdf_1_ein_paar_schl_s kind=form lang=de surface="ein paar Schlüssel-Screenshots" fixes=部分关键截图
E Form_fix_screenshots_in_pdf_1_ein_paar_schl_s FROM_SESSION Session_screenshots_in_pdf

# ingest-session 2026-09-12T23:47:25Z ideation-in-pdf lang=de
V Session_ideation_in_pdf kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-ideation-in-pdf.toon.md
V Focus_ideation_in_pdf kind=focus lang=de gloss="in + Akk — nimm die Recherche in ein neues PDF auf" status=active
E Focus_ideation_in_pdf FROM_SESSION Session_ideation_in_pdf
V Lemma_de_fix_ideation_in_pdf kind=lemma lang=de surface="Nimm die Recherche zu ähnlichen Spielen, Markt und" role=minimal-rewrite
E Lemma_de_fix_ideation_in_pdf FROM_SESSION Session_ideation_in_pdf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-ideation-in-pdf.toon.md
V Form_fix_ideation_in_pdf_0_nimm_in_ein_neues_ kind=form lang=de surface="nimm … in ein neues PDF auf" fixes="搞一搞 / 放进 PDF"
E Form_fix_ideation_in_pdf_0_nimm_in_ein_neues_ FROM_SESSION Session_ideation_in_pdf
V Form_fix_ideation_in_pdf_1_in_ein_neues_pdf kind=form lang=de surface="in ein neues PDF" fixes=一个新的pdf
E Form_fix_ideation_in_pdf_1_in_ein_neues_pdf FROM_SESSION Session_ideation_in_pdf

# ingest-session 2026-09-13T00:05:40Z cypher-in-hall lang=de
V Session_cypher_in_hall kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-cypher-in-hall.toon.md
V Focus_cypher_in_hall kind=focus lang=de gloss="in + Akk — nimm das Projekt in die Halle auf." status=active
E Focus_cypher_in_hall FROM_SESSION Session_cypher_in_hall
V Lemma_de_fix_cypher_in_hall kind=lemma lang=de surface="Bau für mindcraft-zttts eine 3D-Oberfläche wie Cyp" role=minimal-rewrite
E Lemma_de_fix_cypher_in_hall FROM_SESSION Session_cypher_in_hall SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-cypher-in-hall.toon.md
V Form_fix_cypher_in_hall_0_nimm_das_projekt_in kind=form lang=de surface="nimm das Projekt in die Halle auf" fixes=把项目有一个界面
E Form_fix_cypher_in_hall_0_nimm_das_projekt_in FROM_SESSION Session_cypher_in_hall
V Form_fix_cypher_in_hall_1_bau_und_nimm_auf_2a kind=form lang=de surface="bau … und nimm … auf" fixes=实现一下
E Form_fix_cypher_in_hall_1_bau_und_nimm_auf_2a FROM_SESSION Session_cypher_in_hall

# ingest-session 2026-09-13T00:12:30Z licht-in-boden lang=de
V Session_licht_in_boden kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-licht-in-boden.toon.md
V Focus_licht_in_boden kind=focus lang=de gloss="in + Akk — bring Licht in den Boden. (Richtung)" status=active
E Focus_licht_in_boden FROM_SESSION Session_licht_in_boden
V Lemma_de_fix_licht_in_boden kind=lemma lang=de surface="Bring Licht und Material in den Boden, so wie in C" role=minimal-rewrite
E Lemma_de_fix_licht_in_boden FROM_SESSION Session_licht_in_boden SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-licht-in-boden.toon.md
V Form_fix_licht_in_boden_0_bring_licht_in_den_ kind=form lang=de surface="bring Licht in den Boden" fixes=地板要有光影
E Form_fix_licht_in_boden_0_bring_licht_in_den_ FROM_SESSION Session_licht_in_boden
V Form_fix_licht_in_boden_1_material kind=form lang=de surface=Material fixes=材质效果来着
E Form_fix_licht_in_boden_1_material FROM_SESSION Session_licht_in_boden

# ingest-session 2026-09-13T00:21:30Z shenyou-in-loop lang=de
V Session_shenyou_in_loop kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-shenyou-in-loop.toon.md
V Focus_shenyou_in_loop kind=focus lang=de gloss="in + Akk — nimm die 神游 in den 15-Minuten-Takt auf." status=active
E Focus_shenyou_in_loop FROM_SESSION Session_shenyou_in_loop
V Lemma_de_fix_shenyou_in_loop kind=lemma lang=de surface="Starte die 神游 und nimm sie in einen 15-Minuten-Tak" role=minimal-rewrite
E Lemma_de_fix_shenyou_in_loop FROM_SESSION Session_shenyou_in_loop SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-shenyou-in-loop.toon.md
V Form_fix_shenyou_in_loop_0_starte_die_c2e6223 kind=form lang=de surface="starte die 神游" fixes=开始神游
E Form_fix_shenyou_in_loop_0_starte_die_c2e6223 FROM_SESSION Session_shenyou_in_loop
V Form_fix_shenyou_in_loop_1_in_einen_15_minute kind=form lang=de surface="in einen 15-Minuten-Takt auf" fixes=每15分钟
E Form_fix_shenyou_in_loop_1_in_einen_15_minute FROM_SESSION Session_shenyou_in_loop

# ingest-session 2026-09-13T12:17:45Z dateischrank-teleportpunkt lang=de
V Session_dateischrank_teleportpunkt kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-dateischrank-teleportpunkt.toon.md
V Focus_dateischrank_teleportpunkt kind=focus lang=de gloss="jeder + Nom. m. · zu + Dat (zu einem anderen Telep" status=active
E Focus_dateischrank_teleportpunkt FROM_SESSION Session_dateischrank_teleportpunkt
V Lemma_de_fix_dateischrank_teleportpunkt kind=lemma lang=de surface="Kann jeder Dateischrank in dieser 3D-Szene zu eine" role=minimal-rewrite
E Lemma_de_fix_dateischrank_teleportpunkt FROM_SESSION Session_dateischrank_teleportpunkt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-dateischrank-teleportpunkt.toon.md
V Form_fix_dateischrank_teleportpunkt_0_kann_je kind=form lang=de surface="Kann jeder Dateischrank zu einem anderen" fixes=每个文件展示柜可以通向不同的传送点
E Form_fix_dateischrank_teleportpunkt_0_kann_je FROM_SESSION Session_dateischrank_teleportpunkt

# ingest-session 2026-09-13T12:42:49Z teleport-welt-schief lang=de
V Session_teleport_welt_schief kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-teleport-welt-schief.toon.md
V Focus_teleport_welt_schief kind=focus lang=de gloss="nach + Dat (Nach dem Teleport)" status=active
E Focus_teleport_welt_schief FROM_SESSION Session_teleport_welt_schief
V Lemma_de_fix_teleport_welt_schief kind=lemma lang=de surface="Nach dem Teleport ist die Welt schief. Der konkret" role=minimal-rewrite
E Lemma_de_fix_teleport_welt_schief FROM_SESSION Session_teleport_welt_schief SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-teleport-welt-schief.toon.md
V Form_fix_teleport_welt_schief_0_nach_dem_tele kind=form lang=de surface="Nach dem Teleport ist die Welt schief" fixes=传送之后世界是歪的
E Form_fix_teleport_welt_schief_0_nach_dem_tele FROM_SESSION Session_teleport_welt_schief

# ingest-session 2026-09-13T12:50:12Z vitrinen-brauchen-inhalt lang=de
V Session_vitrinen_brauchen_inhalt kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-vitrinen-brauchen-inhalt.toon.md
V Focus_vitrinen_brauchen_inhalt kind=focus lang=de gloss="brauchen + Akk (Die Vitrinen brauchen Inhalt)" status=active
E Focus_vitrinen_brauchen_inhalt FROM_SESSION Session_vitrinen_brauchen_inhalt
V Lemma_de_fix_vitrinen_brauchen_inhalt kind=lemma lang=de surface="Manches lässt sich abspielen, und man sieht trotzd" role=minimal-rewrite
E Lemma_de_fix_vitrinen_brauchen_inhalt FROM_SESSION Session_vitrinen_brauchen_inhalt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-vitrinen-brauchen-inhalt.toon.md
V Form_fix_vitrinen_brauchen_inhalt_0_die_vitri kind=form lang=de surface="Die Vitrinen brauchen Inhalt — jetzt sin" fixes="展览的柜需要友内容 现在空空如也"
E Form_fix_vitrinen_brauchen_inhalt_0_die_vitri FROM_SESSION Session_vitrinen_brauchen_inhalt

# ingest-session 2026-09-13T13:15:46Z nicht-nur-klartext lang=de
V Session_nicht_nur_klartext kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-nicht-nur-klartext.toon.md
V Focus_nicht_nur_klartext kind=focus lang=de gloss="nicht nur … sondern (auch)" status=active
E Focus_nicht_nur_klartext FROM_SESSION Session_nicht_nur_klartext
V Lemma_de_fix_nicht_nur_klartext kind=lemma lang=de surface="Die Vitrinen sollen nicht nur Klartext zeigen, son" role=minimal-rewrite
E Lemma_de_fix_nicht_nur_klartext FROM_SESSION Session_nicht_nur_klartext SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-nicht-nur-klartext.toon.md
V Form_fix_nicht_nur_klartext_0_nicht_nur_klart kind=form lang=de surface="nicht nur Klartext, sondern …" fixes="不仅仅是plain text"
E Form_fix_nicht_nur_klartext_0_nicht_nur_klart FROM_SESSION Session_nicht_nur_klartext
V Form_fix_nicht_nur_klartext_1_buntes_spieleri kind=form lang=de surface="buntes, spielerisches Display" fixes="更多姿多彩 游戏化"
E Form_fix_nicht_nur_klartext_1_buntes_spieleri FROM_SESSION Session_nicht_nur_klartext
V Form_fix_nicht_nur_klartext_2_anlegen_ndern_u kind=form lang=de surface="anlegen, ändern und löschen" fixes=CRUD
E Form_fix_nicht_nur_klartext_2_anlegen_ndern_u FROM_SESSION Session_nicht_nur_klartext

# ingest-session 2026-09-13T14:08:29Z lagezentrale-mit-weltkarte lang=de
V Session_lagezentrale_mit_weltkarte kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-lagezentrale-mit-weltkarte.toon.md
V Focus_lagezentrale_mit_weltkarte kind=focus lang=de gloss="mit + Dativ (mit einer Weltkarte)" status=active
E Focus_lagezentrale_mit_weltkarte FROM_SESSION Session_lagezentrale_mit_weltkarte
V Lemma_de_fix_lagezentrale_mit_weltkarte kind=lemma lang=de surface="Bau in die Halle eine große Lagezentrale mit einer" role=minimal-rewrite
E Lemma_de_fix_lagezentrale_mit_weltkarte FROM_SESSION Session_lagezentrale_mit_weltkarte SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-lagezentrale-mit-weltkarte.toon.md
V Form_fix_lagezentrale_mit_weltkarte_0_eine_gr kind=form lang=de surface="eine große Lagezentrale" fixes=有一个宏大的作战室
E Form_fix_lagezentrale_mit_weltkarte_0_eine_gr FROM_SESSION Session_lagezentrale_mit_weltkarte
V Form_fix_lagezentrale_mit_weltkarte_1_mit_ein kind=form lang=de surface="mit einer Weltkarte" fixes=有世界地图
E Form_fix_lagezentrale_mit_weltkarte_1_mit_ein FROM_SESSION Session_lagezentrale_mit_weltkarte
V Form_fix_lagezentrale_mit_weltkarte_2_einem_k kind=form lang=de surface="einem Körperhologramm und einem Bildschi" fixes="Holograph / 屏幕显示"
E Form_fix_lagezentrale_mit_weltkarte_2_einem_k FROM_SESSION Session_lagezentrale_mit_weltkarte

# ingest-session 2026-09-13T14:15:34Z lagezentrale-braucht-kalender lang=de
V Session_lagezentrale_braucht_kalender kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-lagezentrale-braucht-kalender.toon.md
V Focus_lagezentrale_braucht_kalender kind=focus lang=de gloss="brauchen + Akk (Die Lagezentrale braucht einen Kal" status=active
E Focus_lagezentrale_braucht_kalender FROM_SESSION Session_lagezentrale_braucht_kalender
V Lemma_de_fix_lagezentrale_braucht_kalender kind=lemma lang=de surface="Die Lagezentrale braucht einen großen Kalender, ei" role=minimal-rewrite
E Lemma_de_fix_lagezentrale_braucht_kalender FROM_SESSION Session_lagezentrale_braucht_kalender SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-lagezentrale-braucht-kalender.toon.md
V Form_fix_lagezentrale_braucht_kalender_0_brau kind=form lang=de surface="braucht einen großen Kalender" fixes=还有一个巨大的日历
E Form_fix_lagezentrale_braucht_kalender_0_brau FROM_SESSION Session_lagezentrale_braucht_kalender
V Form_fix_lagezentrale_braucht_kalender_1_ein_ kind=form lang=de surface="ein Gantt-Diagramm und eine Aufgabenlist" fixes="甘特图 / 任务列表"
E Form_fix_lagezentrale_braucht_kalender_1_ein_ FROM_SESSION Session_lagezentrale_braucht_kalender
V Form_fix_lagezentrale_braucht_kalender_2_die_ kind=form lang=de surface="Die Karte ist noch zu simpel" fixes=地图太简单
E Form_fix_lagezentrale_braucht_kalender_2_die_ FROM_SESSION Session_lagezentrale_braucht_kalender

# ingest-session 2026-09-13T14:28:53Z elektronisches-buecherregal lang=de
V Session_elektronisches_buecherregal kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-elektronisches-buecherregal.toon.md
V Focus_elektronisches_buecherregal kind=focus lang=de gloss="sowohl … als auch — Die Bildschirme sollen sowohl " status=active
E Focus_elektronisches_buecherregal FROM_SESSION Session_elektronisches_buecherregal
V Lemma_de_fix_elektronisches_buecherregal kind=lemma lang=de surface="Bau ein elektronisches Bücherregal in eine große h" role=minimal-rewrite
E Lemma_de_fix_elektronisches_buecherregal FROM_SESSION Session_elektronisches_buecherregal SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-elektronisches-buecherregal.toon.md
V Form_fix_elektronisches_buecherregal_0_sowohl kind=form lang=de surface="sowohl PDFs als auch YouTube-Videos" fixes=同时显示pdf也可以显示油管
E Form_fix_elektronisches_buecherregal_0_sowohl FROM_SESSION Session_elektronisches_buecherregal
V Form_fix_elektronisches_buecherregal_1_hnlich kind=form lang=de surface="ähnlich der Pudong-Bibliothek" fixes=类似木质浦东图书馆
E Form_fix_elektronisches_buecherregal_1_hnlich FROM_SESSION Session_elektronisches_buecherregal

# ingest-session 2026-09-13T14:38:31Z von-aussen-lagezentrale lang=de
V Session_von_aussen_lagezentrale kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-von-aussen-lagezentrale.toon.md
V Focus_von_aussen_lagezentrale kind=focus lang=de gloss="von + Dativ — von außen in die Lagezentrale kommen" status=active
E Focus_von_aussen_lagezentrale FROM_SESSION Session_von_aussen_lagezentrale
V Lemma_de_fix_von_aussen_lagezentrale kind=lemma lang=de surface="Wenn ich von außen in die Lagezentrale komme, wird" role=minimal-rewrite
E Lemma_de_fix_von_aussen_lagezentrale FROM_SESSION Session_von_aussen_lagezentrale SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-von-aussen-lagezentrale.toon.md
V Form_fix_von_aussen_lagezentrale_0_von_au_en_ kind=form lang=de surface="von außen in die Lagezentrale kommen" fixes=从外边进来
E Form_fix_von_aussen_lagezentrale_0_von_au_en_ FROM_SESSION Session_von_aussen_lagezentrale
V Form_fix_von_aussen_lagezentrale_1_an_einer_w kind=form lang=de surface="an einer Wand" fixes=墙面一眼知道
E Form_fix_von_aussen_lagezentrale_1_an_einer_w FROM_SESSION Session_von_aussen_lagezentrale

# ingest-session 2026-09-13T14:44:31Z ab-diesem-zeitstempel lang=de
V Session_ab_diesem_zeitstempel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-ab-diesem-zeitstempel.toon.md
V Focus_ab_diesem_zeitstempel kind=focus lang=de gloss="ab + Dativ — ab diesem Zeitstempel weitersehen." status=active
E Focus_ab_diesem_zeitstempel FROM_SESSION Session_ab_diesem_zeitstempel
V Lemma_de_fix_ab_diesem_zeitstempel kind=lemma lang=de surface="Wenn eine Ausstellung ein YouTube-Video hat, brauc" role=minimal-rewrite
E Lemma_de_fix_ab_diesem_zeitstempel FROM_SESSION Session_ab_diesem_zeitstempel SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-ab-diesem-zeitstempel.toon.md
V Form_fix_ab_diesem_zeitstempel_0_ab_diesem_ze kind=form lang=de surface="ab diesem Zeitstempel weitersehen" fixes=从这个时间戳继续
E Form_fix_ab_diesem_zeitstempel_0_ab_diesem_ze FROM_SESSION Session_ab_diesem_zeitstempel
V Form_fix_ab_diesem_zeitstempel_1_automatisch_ kind=form lang=de surface="automatisch oder von mir eingetragen" fixes=要不…要不
E Form_fix_ab_diesem_zeitstempel_1_automatisch_ FROM_SESSION Session_ab_diesem_zeitstempel

# ingest-session 2026-09-13T14:50:22Z kathedrale-schritte-klassik lang=de
V Session_kathedrale_schritte_klassik kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-kathedrale-schritte-klassik.toon.md
V Focus_kathedrale_schritte_klassik kind=focus lang=de gloss="wie in + Dat — wie in einer großen Kathedrale" status=active
E Focus_kathedrale_schritte_klassik FROM_SESSION Session_kathedrale_schritte_klassik
V Lemma_de_fix_kathedrale_schritte_klassik kind=lemma lang=de surface="Wenn man läuft, füge ein Schrittegeräusch hinzu, w" role=minimal-rewrite
E Lemma_de_fix_kathedrale_schritte_klassik FROM_SESSION Session_kathedrale_schritte_klassik SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-kathedrale-schritte-klassik.toon.md
V Form_fix_kathedrale_schritte_klassik_0_wie_in kind=form lang=de surface="wie in einer großen Kathedrale" fixes=在宏伟大教堂走路的那种
E Form_fix_kathedrale_schritte_klassik_0_wie_in FROM_SESSION Session_kathedrale_schritte_klassik
V Form_fix_kathedrale_schritte_klassik_1_spiele kind=form lang=de surface="spiele dazu zufällige klassische Musik a" fixes=从网上调一些随机的古典音乐
E Form_fix_kathedrale_schritte_klassik_1_spiele FROM_SESSION Session_kathedrale_schritte_klassik

# ingest-session 2026-09-13T14:59:33Z laufen-ruckelt-licht-schatten lang=de
V Session_laufen_ruckelt_licht_schatten kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-laufen-ruckelt-licht-schatten.toon.md
V Focus_laufen_ruckelt_licht_schatten kind=focus lang=de gloss="beim + Inf — Beim Laufen ruckelt es." status=active
E Focus_laufen_ruckelt_licht_schatten FROM_SESSION Session_laufen_ruckelt_licht_schatten
V Lemma_de_fix_laufen_ruckelt_licht_schatten kind=lemma lang=de surface="Beim Laufen ruckelt es. Im Bibliothekssaal soll Li" role=minimal-rewrite
E Lemma_de_fix_laufen_ruckelt_licht_schatten FROM_SESSION Session_laufen_ruckelt_licht_schatten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-laufen-ruckelt-licht-schatten.toon.md
V Form_fix_laufen_ruckelt_licht_schatten_0_beim kind=form lang=de surface="Beim Laufen ruckelt es" fixes=走着走着会卡
E Form_fix_laufen_ruckelt_licht_schatten_0_beim FROM_SESSION Session_laufen_ruckelt_licht_schatten
V Form_fix_laufen_ruckelt_licht_schatten_1_lich kind=form lang=de surface="Licht und Schatten sollen besser wirken" fixes=光影效果要更好点
E Form_fix_laufen_ruckelt_licht_schatten_1_lich FROM_SESSION Session_laufen_ruckelt_licht_schatten

# ingest-session 2026-09-13T15:17:33Z youtube-in-der-szene lang=de
V Session_youtube_in_der_szene kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-youtube-in-der-szene.toon.md
V Focus_youtube_in_der_szene kind=focus lang=de gloss="in + Dat — in der Szene abspielen" status=active
E Focus_youtube_in_der_szene FROM_SESSION Session_youtube_in_der_szene
V Lemma_de_fix_youtube_in_der_szene kind=lemma lang=de surface="Kannst du YouTube-Videos automatisch in der Szene " role=minimal-rewrite
E Lemma_de_fix_youtube_in_der_szene FROM_SESSION Session_youtube_in_der_szene SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-youtube-in-der-szene.toon.md
V Form_fix_youtube_in_der_szene_0_in_der_szene_ kind=form lang=de surface="in der Szene abspielen" fixes=在场景内播放
E Form_fix_youtube_in_der_szene_0_in_der_szene_ FROM_SESSION Session_youtube_in_der_szene
V Form_fix_youtube_in_der_szene_1_deutsche_unte kind=form lang=de surface="deutsche Untertitel einstellen" fixes=配置成德语字幕
E Form_fix_youtube_in_der_szene_1_deutsche_unte FROM_SESSION Session_youtube_in_der_szene

# ingest-session 2026-09-13T15:23:14Z videos-auf-einmal-erlauben lang=de
V Session_videos_auf_einmal_erlauben kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-videos-auf-einmal-erlauben.toon.md
V Focus_videos_auf_einmal_erlauben kind=focus lang=de gloss="auf einmal — gesammelt erlauben" status=active
E Focus_videos_auf_einmal_erlauben FROM_SESSION Session_videos_auf_einmal_erlauben
V Lemma_de_fix_videos_auf_einmal_erlauben kind=lemma lang=de surface="Finde einen Weg, damit der Nutzer die Videos in de" role=minimal-rewrite
E Lemma_de_fix_videos_auf_einmal_erlauben FROM_SESSION Session_videos_auf_einmal_erlauben SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-videos-auf-einmal-erlauben.toon.md
V Form_fix_videos_auf_einmal_erlauben_0_auf_ein kind=form lang=de surface="auf einmal erlauben" fixes=批量允许
E Form_fix_videos_auf_einmal_erlauben_0_auf_ein FROM_SESSION Session_videos_auf_einmal_erlauben
V Form_fix_videos_auf_einmal_erlauben_1_nah_gro kind=form lang=de surface="nah groß, fern klein" fixes=近大远小
E Form_fix_videos_auf_einmal_erlauben_1_nah_gro FROM_SESSION Session_videos_auf_einmal_erlauben

# ingest-session 2026-09-13T15:29:25Z pda-woerter-festhalten lang=de
V Session_pda_woerter_festhalten kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-pda-woerter-festhalten.toon.md
V Focus_pda_woerter_festhalten kind=focus lang=de gloss="um … zu + Inf — um neue Wörter festzuhalten" status=active
E Focus_pda_woerter_festhalten FROM_SESSION Session_pda_woerter_festhalten
V Lemma_de_fix_pda_woerter_festhalten kind=lemma lang=de surface="Der Nutzer soll sein PDA öffnen können, um neue Wö" role=minimal-rewrite
E Lemma_de_fix_pda_woerter_festhalten FROM_SESSION Session_pda_woerter_festhalten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-pda-woerter-festhalten.toon.md
V Form_fix_pda_woerter_festhalten_0_um_neue_w_r kind=form lang=de surface="um neue Wörter rasch festzuhalten" fixes=迅速记录新的生词
E Form_fix_pda_woerter_festhalten_0_um_neue_w_r FROM_SESSION Session_pda_woerter_festhalten
V Form_fix_pda_woerter_festhalten_1_schnell_tel kind=form lang=de surface="schnell teleportieren" fixes=快速传送
E Form_fix_pda_woerter_festhalten_1_schnell_tel FROM_SESSION Session_pda_woerter_festhalten

# ingest-session 2026-09-13T15:40:11Z bibliothek-holzspiegel lang=de
V Session_bibliothek_holzspiegel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bibliothek-holzspiegel.toon.md
V Focus_bibliothek_holzspiegel kind=focus lang=de gloss="während — während man geht" status=active
E Focus_bibliothek_holzspiegel FROM_SESSION Session_bibliothek_holzspiegel
V Lemma_de_fix_bibliothek_holzspiegel kind=lemma lang=de surface="Die Bibliothek braucht einen edlen Holzfußboden mi" role=minimal-rewrite
E Lemma_de_fix_bibliothek_holzspiegel FROM_SESSION Session_bibliothek_holzspiegel SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bibliothek-holzspiegel.toon.md
V Form_fix_bibliothek_holzspiegel_0_edler_holzf kind=form lang=de surface="edler Holzfußboden mit Spiegelung" fixes=木纹地板带反光
E Form_fix_bibliothek_holzspiegel_0_edler_holzf FROM_SESSION Session_bibliothek_holzspiegel
V Form_fix_bibliothek_holzspiegel_1_zur_cktelep kind=form lang=de surface=zurückteleportieren fixes=怎么传送回去
E Form_fix_bibliothek_holzspiegel_1_zur_cktelep FROM_SESSION Session_bibliothek_holzspiegel
V Form_fix_bibliothek_holzspiegel_2_w_hrend_man kind=form lang=de surface="während man geht, verschwindet sie" fixes=走着走着突然没了
E Form_fix_bibliothek_holzspiegel_2_w_hrend_man FROM_SESSION Session_bibliothek_holzspiegel

# ingest-session 2026-09-13T15:45:18Z mittelgang-sternenhimmel lang=de
V Session_mittelgang_sternenhimmel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-mittelgang-sternenhimmel.toon.md
V Focus_mittelgang_sternenhimmel kind=focus lang=de gloss="trotzdem — der Innenraum bleibt trotzdem hell" status=active
E Focus_mittelgang_sternenhimmel FROM_SESSION Session_mittelgang_sternenhimmel
V Lemma_de_fix_mittelgang_sternenhimmel kind=lemma lang=de surface="Der Mittelgang soll einen Sternenhimmel wie die Mi" role=minimal-rewrite
E Lemma_de_fix_mittelgang_sternenhimmel FROM_SESSION Session_mittelgang_sternenhimmel SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-mittelgang-sternenhimmel.toon.md
V Form_fix_mittelgang_sternenhimmel_0_einen_ste kind=form lang=de surface="einen Sternenhimmel wie die Milchstraße" fixes=天空是那种太空星空银河系
E Form_fix_mittelgang_sternenhimmel_0_einen_ste FROM_SESSION Session_mittelgang_sternenhimmel
V Form_fix_mittelgang_sternenhimmel_1_hell_erle kind=form lang=de surface="hell erleuchtet" fixes=室内灯火通明
E Form_fix_mittelgang_sternenhimmel_1_hell_erle FROM_SESSION Session_mittelgang_sternenhimmel
V Form_fix_mittelgang_sternenhimmel_2_trotzdem kind=form lang=de surface=trotzdem fixes=然后…那种效果
E Form_fix_mittelgang_sternenhimmel_2_trotzdem FROM_SESSION Session_mittelgang_sternenhimmel

# ingest-session 2026-09-13T16:08:28Z sternenhimmel-ohne-verzoegerung lang=de
V Session_sternenhimmel_ohne_verzoegerung kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-sternenhimmel-ohne-verzoegerung.toon.md
V Focus_sternenhimmel_ohne_verzoegerung kind=focus lang=de gloss="ohne + Nomen — ohne Verzögerung" status=active
E Focus_sternenhimmel_ohne_verzoegerung FROM_SESSION Session_sternenhimmel_ohne_verzoegerung
V Lemma_de_fix_sternenhimmel_ohne_verzoegerung kind=lemma lang=de surface="Der Sternenhimmel soll scharf sein und wie die Mil" role=minimal-rewrite
E Lemma_de_fix_sternenhimmel_ohne_verzoegerung FROM_SESSION Session_sternenhimmel_ohne_verzoegerung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-sternenhimmel-ohne-verzoegerung.toon.md
V Form_fix_sternenhimmel_ohne_verzoegerung_0_sc kind=form lang=de surface="scharf sein" fixes=糊糊的不搞清
E Form_fix_sternenhimmel_ohne_verzoegerung_0_sc FROM_SESSION Session_sternenhimmel_ohne_verzoegerung
V Form_fix_sternenhimmel_ohne_verzoegerung_1_wi kind=form lang=de surface="wie die Milchstraße wirken" fixes=没有银河那种效果
E Form_fix_sternenhimmel_ohne_verzoegerung_1_wi FROM_SESSION Session_sternenhimmel_ohne_verzoegerung
V Form_fix_sternenhimmel_ohne_verzoegerung_2_oh kind=form lang=de surface="ohne Verzögerung" fixes=有延迟
E Form_fix_sternenhimmel_ohne_verzoegerung_2_oh FROM_SESSION Session_sternenhimmel_ohne_verzoegerung

# ingest-session 2026-09-13T16:14:53Z bibliothek-feine-materialien lang=de
V Session_bibliothek_feine_materialien kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bibliothek-feine-materialien.toon.md
V Focus_bibliothek_feine_materialien kind=focus lang=de gloss="nicht … sondern — nicht rau, sondern fein" status=active
E Focus_bibliothek_feine_materialien FROM_SESSION Session_bibliothek_feine_materialien
V Lemma_de_fix_bibliothek_feine_materialien kind=lemma lang=de surface="Die Bibliothekswände brauchen bessere Materialien." role=minimal-rewrite
E Lemma_de_fix_bibliothek_feine_materialien FROM_SESSION Session_bibliothek_feine_materialien SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bibliothek-feine-materialien.toon.md
V Form_fix_bibliothek_feine_materialien_0_besse kind=form lang=de surface="bessere Materialien" fixes=更好的材质
E Form_fix_bibliothek_feine_materialien_0_besse FROM_SESSION Session_bibliothek_feine_materialien
V Form_fix_bibliothek_feine_materialien_1_nicht kind=form lang=de surface="nicht rau wirken" fixes=不能是很粗糙的
E Form_fix_bibliothek_feine_materialien_1_nicht FROM_SESSION Session_bibliothek_feine_materialien
V Form_fix_bibliothek_feine_materialien_2_sonde kind=form lang=de surface="sondern fein" fixes=精致一点
E Form_fix_bibliothek_feine_materialien_2_sonde FROM_SESSION Session_bibliothek_feine_materialien

# ingest-session 2026-09-13T17:33:41Z gpu-ohne-kollision lang=de
V Session_gpu_ohne_kollision kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-gpu-ohne-kollision.toon.md
V Focus_gpu_ohne_kollision kind=focus lang=de gloss="damit — damit es nicht ruckelt" status=active
E Focus_gpu_ohne_kollision FROM_SESSION Session_gpu_ohne_kollision
V Lemma_de_fix_gpu_ohne_kollision kind=lemma lang=de surface="Chrome soll die GPU nutzen, damit es nicht ruckelt" role=minimal-rewrite
E Lemma_de_fix_gpu_ohne_kollision FROM_SESSION Session_gpu_ohne_kollision SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-gpu-ohne-kollision.toon.md
V Form_fix_gpu_ohne_kollision_0_die_gpu_nutzen kind=form lang=de surface="die GPU nutzen" fixes=调动gpu资源
E Form_fix_gpu_ohne_kollision_0_die_gpu_nutzen FROM_SESSION Session_gpu_ohne_kollision
V Form_fix_gpu_ohne_kollision_1_ruckelt kind=form lang=de surface=ruckelt fixes=卡顿
E Form_fix_gpu_ohne_kollision_1_ruckelt FROM_SESSION Session_gpu_ohne_kollision
V Form_fix_gpu_ohne_kollision_2_mit_kurzbefehle kind=form lang=de surface="mit Kurzbefehlen kollidieren" fixes=快捷键冲突
E Form_fix_gpu_ohne_kollision_2_mit_kurzbefehle FROM_SESSION Session_gpu_ohne_kollision

# auto-gap 2026-09-13T17:39:08Z surface=头有点晕
V Concept_gap_zh_32d1f1c7a4 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_32d1f1c7a4 kind=gap lang=zh surface=头有点晕 target=de status=open
V Lemma_zh_zh_32d1f1c7a4 kind=lemma lang=zh surface=头有点晕
E Concept_gap_zh_32d1f1c7a4 EXPRESSES Lemma_zh_zh_32d1f1c7a4 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_32d1f1c7a4 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_32d1f1c7a4 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-13T17:39:08Z surface=有点酸
V Concept_gap_zh_27d16195fc kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_27d16195fc kind=gap lang=zh surface=有点酸 target=de status=open
V Lemma_zh_zh_27d16195fc kind=lemma lang=zh surface=有点酸
E Concept_gap_zh_27d16195fc EXPRESSES Lemma_zh_zh_27d16195fc SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_27d16195fc GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_27d16195fc GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-13T17:39:08Z surface=给我一个轻量学习计划
V Concept_gap_zh_bb68f20d71 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_bb68f20d71 kind=gap lang=zh surface=给我一个轻量学习计划 target=de status=open
V Lemma_zh_zh_bb68f20d71 kind=lemma lang=zh surface=给我一个轻量学习计划
E Concept_gap_zh_bb68f20d71 EXPRESSES Lemma_zh_zh_bb68f20d71 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_bb68f20d71 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_bb68f20d71 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-13T17:39:35Z leichter-lernplan-muede lang=de
V Session_leichter_lernplan_muede kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-leichter-lernplan-muede.toon.md
V Focus_leichter_lernplan_muede kind=focus lang=de gloss="möchte + Akkusativ — Ich möchte einen leichten Ler" status=active
E Focus_leichter_lernplan_muede FROM_SESSION Session_leichter_lernplan_muede
V Lemma_de_fix_leichter_lernplan_muede kind=lemma lang=de surface="Ich bin jetzt müde und möchte einen leichten Lernp" role=minimal-rewrite
E Lemma_de_fix_leichter_lernplan_muede FROM_SESSION Session_leichter_lernplan_muede SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-leichter-lernplan-muede.toon.md
V Form_fix_leichter_lernplan_muede_0_ich_m_chte kind=form lang=de surface="Ich möchte einen leichten Lernplan." fixes="Gib mir einen leichten Lernpla"
E Form_fix_leichter_lernplan_muede_0_ich_m_chte FROM_SESSION Session_leichter_lernplan_muede

# ingest-session 2026-09-13T17:40:59Z allgemeine-uebungsfrage-asynchron lang=de
V Session_allgemeine_uebungsfrage_asynchron kind=session date=2026-09-12 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-allgemeine-uebungsfrage-asynchron.toon.md
V Focus_allgemeine_uebungsfrage_asynchron kind=focus lang=de gloss="asynchron — Ich beantworte sie asynchron." status=active
E Focus_allgemeine_uebungsfrage_asynchron FROM_SESSION Session_allgemeine_uebungsfrage_asynchron
V Lemma_de_fix_allgemeine_uebungsfrage_asynchron kind=lemma lang=de surface="Gib mir eine allgemeine Übungsfrage; ich beantwort" role=minimal-rewrite
E Lemma_de_fix_allgemeine_uebungsfrage_asynchron FROM_SESSION Session_allgemeine_uebungsfrage_asynchron SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-12-allgemeine-uebungsfrage-asynchron.toon.md
V Form_fix_allgemeine_uebungsfrage_asynchron_0_ kind=form lang=de surface="eine allgemeine Übungsfrage; ich beantwo" fixes="Probe Frage allgemein denn, ic"
E Form_fix_allgemeine_uebungsfrage_asynchron_0_ FROM_SESSION Session_allgemeine_uebungsfrage_asynchron

# ingest-session 2026-09-13T17:41:54Z allgemeine-frage-nicht-deutsch lang=de
V Session_allgemeine_frage_nicht_deutsch kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-allgemeine-frage-nicht-deutsch.toon.md
V Focus_allgemeine_frage_nicht_deutsch kind=focus lang=de gloss="auf + Akkusativ beschränkt sein — nicht auf Deutsc" status=active
E Focus_allgemeine_frage_nicht_deutsch FROM_SESSION Session_allgemeine_frage_nicht_deutsch
V Lemma_de_fix_allgemeine_frage_nicht_deutsch kind=lemma lang=de surface="Nein, die Übung soll nicht auf Deutsch beschränkt " role=minimal-rewrite
E Lemma_de_fix_allgemeine_frage_nicht_deutsch FROM_SESSION Session_allgemeine_frage_nicht_deutsch SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-allgemeine-frage-nicht-deutsch.toon.md
V Form_fix_allgemeine_frage_nicht_deutsch_0_nic kind=form lang=de surface="nicht auf Deutsch beschränkt sein" fixes="nicht von Sprache Deutsch Übun"
E Form_fix_allgemeine_frage_nicht_deutsch_0_nic FROM_SESSION Session_allgemeine_frage_nicht_deutsch

# ingest-session 2026-09-13T17:43:07Z probefrage-aus-wissensgraph lang=de
V Session_probefrage_aus_wissensgraph kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-probefrage-aus-wissensgraph.toon.md
V Focus_probefrage_aus_wissensgraph kind=focus lang=de gloss="basierend auf + Dativ — basierend auf dem Wissensg" status=active
E Focus_probefrage_aus_wissensgraph FROM_SESSION Session_probefrage_aus_wissensgraph
V Lemma_de_fix_probefrage_aus_wissensgraph kind=lemma lang=de surface="Nein, nicht so, sondern basierend auf dem Wissensg" role=minimal-rewrite
E Lemma_de_fix_probefrage_aus_wissensgraph FROM_SESSION Session_probefrage_aus_wissensgraph SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-probefrage-aus-wissensgraph.toon.md
V Form_fix_probefrage_aus_wissensgraph_0_basier kind=form lang=de surface="basierend auf dem Wissensgraphen" fixes="basierert von den Kenntnisse G"
E Form_fix_probefrage_aus_wissensgraph_0_basier FROM_SESSION Session_probefrage_aus_wissensgraph

# ingest-session 2026-09-13T18:54:17Z in-dieses-system-integrieren lang=de
V Session_in_dieses_system_integrieren kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-in-dieses-system-integrieren.toon.md
V Focus_in_dieses_system_integrieren kind=focus lang=de gloss="in + Akk — in dieses System (das System, Akk. n.)," status=active
E Focus_in_dieses_system_integrieren FROM_SESSION Session_in_dieses_system_integrieren
V Lemma_de_fix_in_dieses_system_integrieren kind=lemma lang=de surface="Ich habe diesen Eintrag gelesen: gute Informations" role=minimal-rewrite
E Lemma_de_fix_in_dieses_system_integrieren FROM_SESSION Session_in_dieses_system_integrieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-in-dieses-system-integrieren.toon.md
V Form_fix_in_dieses_system_integrieren_0_diese kind=form lang=de surface="diesen Eintrag" fixes="dies Eintrag"
E Form_fix_in_dieses_system_integrieren_0_diese FROM_SESSION Session_in_dieses_system_integrieren
V Form_fix_in_dieses_system_integrieren_1_deuts kind=form lang=de surface="deutsche Startups" fixes="Deutsche Startup"
E Form_fix_in_dieses_system_integrieren_1_deuts FROM_SESSION Session_in_dieses_system_integrieren
V Form_fix_in_dieses_system_integrieren_2_in_di kind=form lang=de surface="in dieses System" fixes="ins diesen System"
E Form_fix_in_dieses_system_integrieren_2_in_di FROM_SESSION Session_in_dieses_system_integrieren

# ingest-session 2026-09-13T18:56:25Z bodenspiegelung-in-jedem-raum lang=de
V Session_bodenspiegelung_in_jedem_raum kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bodenspiegelung-in-jedem-raum.toon.md
V Focus_bodenspiegelung_in_jedem_raum kind=focus lang=de gloss="sobald — Sobald ich einen Raum betrete" status=active
E Focus_bodenspiegelung_in_jedem_raum FROM_SESSION Session_bodenspiegelung_in_jedem_raum
V Lemma_de_fix_bodenspiegelung_in_jedem_raum kind=lemma lang=de surface="Sobald ich einen Raum der Haupthalle betrete, vers" role=minimal-rewrite
E Lemma_de_fix_bodenspiegelung_in_jedem_raum FROM_SESSION Session_bodenspiegelung_in_jedem_raum SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-bodenspiegelung-in-jedem-raum.toon.md
V Form_fix_bodenspiegelung_in_jedem_raum_0_soba kind=form lang=de surface="Sobald ich einen Raum betrete" fixes=进到每一个room时候
E Form_fix_bodenspiegelung_in_jedem_raum_0_soba FROM_SESSION Session_bodenspiegelung_in_jedem_raum
V Form_fix_bodenspiegelung_in_jedem_raum_1_vers kind=form lang=de surface="verschwindet die Bodenspiegelung" fixes=地上反光都会消失
E Form_fix_bodenspiegelung_in_jedem_raum_1_vers FROM_SESSION Session_bodenspiegelung_in_jedem_raum

# ingest-session 2026-09-13T19:01:32Z w-bleibt-chrome-kurzbefehl lang=de
V Session_w_bleibt_chrome_kurzbefehl kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-w-bleibt-chrome-kurzbefehl.toon.md
V Focus_w_bleibt_chrome_kurzbefehl kind=focus lang=de gloss="weiterhin — bleibt weiterhin" status=active
E Focus_w_bleibt_chrome_kurzbefehl FROM_SESSION Session_w_bleibt_chrome_kurzbefehl
V Lemma_de_fix_w_bleibt_chrome_kurzbefehl kind=lemma lang=de surface="Wenn ich die Seite in Chrome öffne, bleibt W weite" role=minimal-rewrite
E Lemma_de_fix_w_bleibt_chrome_kurzbefehl FROM_SESSION Session_w_bleibt_chrome_kurzbefehl SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-w-bleibt-chrome-kurzbefehl.toon.md
V Form_fix_w_bleibt_chrome_kurzbefehl_0_bleibt_ kind=form lang=de surface="bleibt weiterhin" fixes=仍然是
E Form_fix_w_bleibt_chrome_kurzbefehl_0_bleibt_ FROM_SESSION Session_w_bleibt_chrome_kurzbefehl
V Form_fix_w_bleibt_chrome_kurzbefehl_1_ein_bro kind=form lang=de surface="ein Browser-Kurzbefehl" fixes=浏览器的快捷键
E Form_fix_w_bleibt_chrome_kurzbefehl_1_ein_bro FROM_SESSION Session_w_bleibt_chrome_kurzbefehl

# ingest-session 2026-09-13T19:37:17Z fluester-asmr-deutsche-untertitel lang=de
V Session_fluester_asmr_deutsche_untertitel kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-fluester-asmr-deutsche-untertitel.toon.md
V Focus_fluester_asmr_deutsche_untertitel kind=focus lang=de gloss="sowohl … als auch — Untertitel und Voiceover" status=active
E Focus_fluester_asmr_deutsche_untertitel FROM_SESSION Session_fluester_asmr_deutsche_untertitel
V Lemma_de_fix_fluester_asmr_deutsche_untertitel kind=lemma lang=de surface="Gut. Mach mit Playwright einen Werbefilm. Außerdem" role=minimal-rewrite
E Lemma_de_fix_fluester_asmr_deutsche_untertitel FROM_SESSION Session_fluester_asmr_deutsche_untertitel SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-fluester-asmr-deutsche-untertitel.toon.md
V Form_fix_fluester_asmr_deutsche_untertitel_0_ kind=form lang=de surface="etwas Wiederverwendbares im Skill" fixes=可复用进skill里边
E Form_fix_fluester_asmr_deutsche_untertitel_0_ FROM_SESSION Session_fluester_asmr_deutsche_untertitel
V Form_fix_fluester_asmr_deutsche_untertitel_1_ kind=form lang=de surface=Flüster-ASMR fixes="悄悄话 asmr"
E Form_fix_fluester_asmr_deutsche_untertitel_1_ FROM_SESSION Session_fluester_asmr_deutsche_untertitel
V Form_fix_fluester_asmr_deutsche_untertitel_2_ kind=form lang=de surface="deutsche Untertitel und ein deutsches Vo" fixes="德语字幕 德语voiceover"
E Form_fix_fluester_asmr_deutsche_untertitel_2_ FROM_SESSION Session_fluester_asmr_deutsche_untertitel

# ingest-session 2026-09-13T20:46:04Z echtes-fluestern-keine-modalstimme lang=de
V Session_echtes_fluestern_keine_modalstimme kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-echtes-fluestern-keine-modalstimme.toon.md
V Focus_echtes_fluestern_keine_modalstimme kind=focus lang=de gloss="nicht … sondern — kein Flüstern, sondern Modalstim" status=active
E Focus_echtes_fluestern_keine_modalstimme FROM_SESSION Session_echtes_fluestern_keine_modalstimme
V Lemma_de_fix_echtes_fluestern_keine_modalstimme kind=lemma lang=de surface="Das ist kein echtes Flüstern, sondern Modalstimme." role=minimal-rewrite
E Lemma_de_fix_echtes_fluestern_keine_modalstimme FROM_SESSION Session_echtes_fluestern_keine_modalstimme SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-echtes-fluestern-keine-modalstimme.toon.md
V Form_fix_echtes_fluestern_keine_modalstimme_0 kind=form lang=de surface="Das ist kein echtes Flüstern" fixes=悄悄话不对
E Form_fix_echtes_fluestern_keine_modalstimme_0 FROM_SESSION Session_echtes_fluestern_keine_modalstimme
V Form_fix_echtes_fluestern_keine_modalstimme_1 kind=form lang=de surface="Modalstimme / richtiges Whisper" fixes=真声发音
E Form_fix_echtes_fluestern_keine_modalstimme_1 FROM_SESSION Session_echtes_fluestern_keine_modalstimme

# ingest-session 2026-09-13T21:42:07Z github-fuer-echtes-fluestern lang=de
V Session_github_fuer_echtes_fluestern kind=session date=2026-09-13 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-github-fuer-echtes-fluestern.toon.md
V Focus_github_fuer_echtes_fluestern kind=focus lang=de gloss="ob — ob es passende Projekte gibt" status=active
E Focus_github_fuer_echtes_fluestern FROM_SESSION Session_github_fuer_echtes_fluestern
V Lemma_de_fix_github_fuer_echtes_fluestern kind=lemma lang=de surface="Schau auf GitHub, ob es passende Projekte gibt, di" role=minimal-rewrite
E Lemma_de_fix_github_fuer_echtes_fluestern FROM_SESSION Session_github_fuer_echtes_fluestern SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-13-github-fuer-echtes-fluestern.toon.md
V Form_fix_github_fuer_echtes_fluestern_0_schau kind=form lang=de surface="Schau auf GitHub, ob es" fixes=看下github有没有
E Form_fix_github_fuer_echtes_fluestern_0_schau FROM_SESSION Session_github_fuer_echtes_fluestern
V Form_fix_github_fuer_echtes_fluestern_1_die_d kind=form lang=de surface="die das wirklich können" fixes=可以做到的
E Form_fix_github_fuer_echtes_fluestern_1_die_d FROM_SESSION Session_github_fuer_echtes_fluestern

# ingest-session 2026-09-13T22:28:56Z inflow-orca-ade lang=de
V Session_inflow_orca_ade kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-inflow-orca-ade.toon.md
V Focus_inflow_orca_ade kind=focus lang=de gloss="als — als Inflow" status=active
E Focus_inflow_orca_ade FROM_SESSION Session_inflow_orca_ade
V Lemma_de_fix_inflow_orca_ade kind=lemma lang=de surface="Nimm das als Inflow auf." role=minimal-rewrite
E Lemma_de_fix_inflow_orca_ade FROM_SESSION Session_inflow_orca_ade SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-inflow-orca-ade.toon.md
V Form_fix_inflow_orca_ade_0_nimm_das_als_auf_9 kind=form lang=de surface="Nimm das als … auf" fixes=加进来作为
E Form_fix_inflow_orca_ade_0_nimm_das_als_auf_9 FROM_SESSION Session_inflow_orca_ade
V Form_fix_inflow_orca_ade_1_inflow kind=form lang=de surface=Inflow fixes=inflow
E Form_fix_inflow_orca_ade_1_inflow FROM_SESSION Session_inflow_orca_ade

# auto-gap 2026-09-14T09:18:45Z surface=鑴戦浘
V Concept_gap_zh_71eb0f37c3 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_71eb0f37c3 kind=gap lang=zh surface=鑴戦浘 target=de status=open
V Lemma_zh_zh_71eb0f37c3 kind=lemma lang=zh surface=鑴戦浘
E Concept_gap_zh_71eb0f37c3 EXPRESSES Lemma_zh_zh_71eb0f37c3 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_71eb0f37c3 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_71eb0f37c3 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-14T09:21:02Z aufgestanden-hall-inflow lang=de
V Session_aufgestanden_hall_inflow kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-aufgestanden-hall-inflow.toon.md
V Focus_aufgestanden_hall_inflow kind=focus lang=de gloss="Perfekt sein + aufgestanden" status=active
E Focus_aufgestanden_hall_inflow FROM_SESSION Session_aufgestanden_hall_inflow
V Lemma_de_fix_aufgestanden_hall_inflow kind=lemma lang=de surface="Ich bin am 14.9. um 11 Uhr aufgestanden, noch mit " role=minimal-rewrite
E Lemma_de_fix_aufgestanden_hall_inflow FROM_SESSION Session_aufgestanden_hall_inflow SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-aufgestanden-hall-inflow.toon.md
V Form_fix_aufgestanden_hall_inflow_0_bin_aufge kind=form lang=de surface="bin … aufgestanden" fixes="stand auf"
E Form_fix_aufgestanden_hall_inflow_0_bin_aufge FROM_SESSION Session_aufgestanden_hall_inflow
V Form_fix_aufgestanden_hall_inflow_1_am_14_9_u kind=form lang=de surface="am 14.9. um 11 Uhr" fixes="am 9/14 am 11 Uhr"
E Form_fix_aufgestanden_hall_inflow_1_am_14_9_u FROM_SESSION Session_aufgestanden_hall_inflow
V Form_fix_aufgestanden_hall_inflow_2_gehirnneb kind=form lang=de surface=Gehirnnebel fixes=脑雾
E Form_fix_aufgestanden_hall_inflow_2_gehirnneb FROM_SESSION Session_aufgestanden_hall_inflow
V Form_fix_aufgestanden_hall_inflow_3_das_3d_ha kind=form lang=de surface="das 3D-Hall-Projekt" fixes="die 3D hall projekt"
E Form_fix_aufgestanden_hall_inflow_3_das_3d_ha FROM_SESSION Session_aufgestanden_hall_inflow
V Form_fix_aufgestanden_hall_inflow_4_mit_neuem kind=form lang=de surface="mit neuem Inflow" fixes="mit neue Inflow"
E Form_fix_aufgestanden_hall_inflow_4_mit_neuem FROM_SESSION Session_aufgestanden_hall_inflow
V Form_fix_aufgestanden_hall_inflow_5_fange_mit kind=form lang=de surface="fange mit der Routine an" fixes="fange an, mit routine zu start"
E Form_fix_aufgestanden_hall_inflow_5_fange_mit FROM_SESSION Session_aufgestanden_hall_inflow

# ingest-session 2026-09-14T09:29:29Z zu-viele-emails-ki-agent lang=de
V Session_zu_viele_emails_ki_agent kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zu-viele-emails-ki-agent.toon.md
V Focus_zu_viele_emails_ki_agent kind=focus lang=de gloss="es gibt — gibt es zu viele E-Mails" status=active
E Focus_zu_viele_emails_ki_agent FROM_SESSION Session_zu_viele_emails_ki_agent
V Lemma_de_fix_zu_viele_emails_ki_agent kind=lemma lang=de surface="Bei meiner vorhandenen E-Mail-Adresse gibt es zu v" role=minimal-rewrite
E Lemma_de_fix_zu_viele_emails_ki_agent FROM_SESSION Session_zu_viele_emails_ki_agent SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zu-viele-emails-ki-agent.toon.md
V Form_fix_zu_viele_emails_ki_agent_0_bei_meine kind=form lang=de surface="Bei meiner vorhandenen" fixes="Bei meine vorhande"
E Form_fix_zu_viele_emails_ki_agent_0_bei_meine FROM_SESSION Session_zu_viele_emails_ki_agent
V Form_fix_zu_viele_emails_ki_agent_1_gibt_es_z kind=form lang=de surface="gibt es zu viele E-Mails" fixes="geben es zu viel Emails"
E Form_fix_zu_viele_emails_ki_agent_1_gibt_es_z FROM_SESSION Session_zu_viele_emails_ki_agent
V Form_fix_zu_viele_emails_ki_agent_2_das_mit_k kind=form lang=de surface="das mit KI-Agenten zu automatisieren" fixes="automatisch … zu automatisiere"
E Form_fix_zu_viele_emails_ki_agent_2_das_mit_k FROM_SESSION Session_zu_viele_emails_ki_agent

# ingest-session 2026-09-14T09:30:19Z nahrungsergaenzung-heute lang=de
V Session_nahrungsergaenzung_heute kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nahrungsergaenzung-heute.toon.md
V Focus_nahrungsergaenzung_heute kind=focus lang=de gloss="eine Empfehlung (Akk. f.)" status=active
E Focus_nahrungsergaenzung_heute FROM_SESSION Session_nahrungsergaenzung_heute
V Lemma_de_fix_nahrungsergaenzung_heute kind=lemma lang=de surface="So, ich stehe auf. Gib mir eine Empfehlung für Nah" role=minimal-rewrite
E Lemma_de_fix_nahrungsergaenzung_heute FROM_SESSION Session_nahrungsergaenzung_heute SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nahrungsergaenzung-heute.toon.md
V Form_fix_nahrungsergaenzung_heute_0_nahrungse kind=form lang=de surface=Nahrungsergänzungsmittel fixes=Nährunsergänzensmittel
E Form_fix_nahrungsergaenzung_heute_0_nahrungse FROM_SESSION Session_nahrungsergaenzung_heute
V Form_fix_nahrungsergaenzung_heute_1_gib_mir_e kind=form lang=de surface="Gib mir eine Empfehlung" fixes="Geben Sie mir Empfehlung"
E Form_fix_nahrungsergaenzung_heute_1_gib_mir_e FROM_SESSION Session_nahrungsergaenzung_heute
V Form_fix_nahrungsergaenzung_heute_2_so_ich kind=form lang=de surface="So, ich" fixes="So Ich"
E Form_fix_nahrungsergaenzung_heute_2_so_ich FROM_SESSION Session_nahrungsergaenzung_heute

# ingest-session 2026-09-14T09:33:39Z nuancen-aktualisierte-empfehlung lang=de
V Session_nuancen_aktualisierte_empfehlung kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nuancen-aktualisierte-empfehlung.toon.md
V Focus_nuancen_aktualisierte_empfehlung kind=focus lang=de gloss="eine aktualisierte Empfehlung (Akk. f.)" status=active
E Focus_nuancen_aktualisierte_empfehlung FROM_SESSION Session_nuancen_aktualisierte_empfehlung
V Lemma_de_fix_nuancen_aktualisierte_empfehlung kind=lemma lang=de surface="Machen Sie noch mehr Forschung mit Nuancen, ja. Da" role=minimal-rewrite
E Lemma_de_fix_nuancen_aktualisierte_empfehlung FROM_SESSION Session_nuancen_aktualisierte_empfehlung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nuancen-aktualisierte-empfehlung.toon.md
V Form_fix_nuancen_aktualisierte_empfehlung_0_n kind=form lang=de surface=Nuancen fixes=Nuiances
E Form_fix_nuancen_aktualisierte_empfehlung_0_n FROM_SESSION Session_nuancen_aktualisierte_empfehlung
V Form_fix_nuancen_aktualisierte_empfehlung_1_d kind=form lang=de surface="Danach geben Sie" fixes="demnächst geben Sie"
E Form_fix_nuancen_aktualisierte_empfehlung_1_d FROM_SESSION Session_nuancen_aktualisierte_empfehlung

# ingest-session 2026-09-14T09:36:04Z wie-man-es-macht lang=de
V Session_wie_man_es_macht kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wie-man-es-macht.toon.md
V Focus_wie_man_es_macht kind=focus lang=de gloss="man — wie macht man das" status=active
E Focus_wie_man_es_macht FROM_SESSION Session_wie_man_es_macht
V Lemma_de_fix_wie_man_es_macht kind=lemma lang=de surface="Gut. Wie macht man das?" role=minimal-rewrite
E Lemma_de_fix_wie_man_es_macht FROM_SESSION Session_wie_man_es_macht SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wie-man-es-macht.toon.md
V Form_fix_wie_man_es_macht_0_man kind=form lang=de surface=man fixes=Mann
E Form_fix_wie_man_es_macht_0_man FROM_SESSION Session_wie_man_es_macht
V Form_fix_wie_man_es_macht_1_wie_macht_man_das kind=form lang=de surface="Wie macht man das" fixes="wie … machen"
E Form_fix_wie_man_es_macht_1_wie_macht_man_das FROM_SESSION Session_wie_man_es_macht

# ingest-session 2026-09-14T09:37:45Z nutzungsempfehlung-oregano-neem lang=de
V Session_nutzungsempfehlung_oregano_neem kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nutzungsempfehlung-oregano-neem.toon.md
V Focus_nutzungsempfehlung_oregano_neem kind=focus lang=de gloss="die Nutzungsempfehlung (Akk. f.)" status=active
E Focus_nutzungsempfehlung_oregano_neem FROM_SESSION Session_nutzungsempfehlung_oregano_neem
V Lemma_de_fix_nutzungsempfehlung_oregano_neem kind=lemma lang=de surface="So, erzählen Sie mir die Nutzungsempfehlung für Or" role=minimal-rewrite
E Lemma_de_fix_nutzungsempfehlung_oregano_neem FROM_SESSION Session_nutzungsempfehlung_oregano_neem SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-nutzungsempfehlung-oregano-neem.toon.md
V Form_fix_nutzungsempfehlung_oregano_neem_0_so kind=form lang=de surface="So, erzählen Sie mir" fixes="So erzählen Sie mir"
E Form_fix_nutzungsempfehlung_oregano_neem_0_so FROM_SESSION Session_nutzungsempfehlung_oregano_neem
V Form_fix_nutzungsempfehlung_oregano_neem_1_f_ kind=form lang=de surface="für Oregano, Neem, Apfelessig" fixes="für Oregano Neem Apfelessig"
E Form_fix_nutzungsempfehlung_oregano_neem_1_f_ FROM_SESSION Session_nutzungsempfehlung_oregano_neem

# auto-gap 2026-09-14T09:40:09Z surface=厰婧冪枴
V Concept_gap_zh_cf3ef60a4e kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_cf3ef60a4e kind=gap lang=zh surface=厰婧冪枴 target=de status=open
V Lemma_zh_zh_cf3ef60a4e kind=lemma lang=zh surface=厰婧冪枴
E Concept_gap_zh_cf3ef60a4e EXPRESSES Lemma_zh_zh_cf3ef60a4e SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_cf3ef60a4e GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_cf3ef60a4e GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-14T09:41:45Z aphthen-gaenzlich-weg lang=de
V Session_aphthen_gaenzlich_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-aphthen-gaenzlich-weg.toon.md
V Focus_aphthen_gaenzlich_weg kind=focus lang=de gloss="die Aphthen sind … gänzlich weg (Pl. + Umlaut)" status=active
E Focus_aphthen_gaenzlich_weg FROM_SESSION Session_aphthen_gaenzlich_weg
V Lemma_de_fix_aphthen_gaenzlich_weg kind=lemma lang=de surface="Die Aphthen sind zurzeit gänzlich weg, und auch di" role=minimal-rewrite
E Lemma_de_fix_aphthen_gaenzlich_weg FROM_SESSION Session_aphthen_gaenzlich_weg SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-aphthen-gaenzlich-weg.toon.md
V Form_fix_aphthen_gaenzlich_weg_0_die_aphthen_ kind=form lang=de surface="Die Aphthen sind" fixes="Aphlete 口腔溃疡 is"
E Form_fix_aphthen_gaenzlich_weg_0_die_aphthen_ FROM_SESSION Session_aphthen_gaenzlich_weg
V Form_fix_aphthen_gaenzlich_weg_1_g_nzlich_51a kind=form lang=de surface=gänzlich fixes=ganzlich
E Form_fix_aphthen_gaenzlich_weg_1_g_nzlich_51a FROM_SESSION Session_aphthen_gaenzlich_weg
V Form_fix_aphthen_gaenzlich_weg_2_die_magen_da kind=form lang=de surface="die Magen-Darm-Beschwerden" fixes="die Magen-Darm-Beschwerde"
E Form_fix_aphthen_gaenzlich_weg_2_die_magen_da FROM_SESSION Session_aphthen_gaenzlich_weg

# ingest-session 2026-09-14T09:43:48Z wo-finde-ich-imap-titan lang=de
V Session_wo_finde_ich_imap_titan kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wo-finde-ich-imap-titan.toon.md
V Focus_wo_finde_ich_imap_titan kind=focus lang=de gloss="wo — Wo finde ich IMAP" status=active
E Focus_wo_finde_ich_imap_titan FROM_SESSION Session_wo_finde_ich_imap_titan
V Lemma_de_fix_wo_finde_ich_imap_titan kind=lemma lang=de surface="Wo finde ich IMAP bei Titan?" role=minimal-rewrite
E Lemma_de_fix_wo_finde_ich_imap_titan FROM_SESSION Session_wo_finde_ich_imap_titan SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wo-finde-ich-imap-titan.toon.md
V Form_fix_wo_finde_ich_imap_titan_0_wo_finde_i kind=form lang=de surface="Wo finde ich" fixes=哪里能够找到
E Form_fix_wo_finde_ich_imap_titan_0_wo_finde_i FROM_SESSION Session_wo_finde_ich_imap_titan
V Form_fix_wo_finde_ich_imap_titan_1_imap_bei_t kind=form lang=de surface="IMAP bei Titan" fixes="titan … imap"
E Form_fix_wo_finde_ich_imap_titan_1_imap_bei_t FROM_SESSION Session_wo_finde_ich_imap_titan

# ingest-session 2026-09-14T09:47:07Z blickwinkel-materialfehler lang=de
V Session_blickwinkel_materialfehler kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-blickwinkel-materialfehler.toon.md
V Focus_blickwinkel_materialfehler kind=focus lang=de gloss="je nach + Dativ" status=active
E Focus_blickwinkel_materialfehler FROM_SESSION Session_blickwinkel_materialfehler
V Lemma_de_fix_blickwinkel_materialfehler kind=lemma lang=de surface="Je nach Blickwinkel gibt es Materialfehler." role=minimal-rewrite
E Lemma_de_fix_blickwinkel_materialfehler FROM_SESSION Session_blickwinkel_materialfehler SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-blickwinkel-materialfehler.toon.md
V Form_fix_blickwinkel_materialfehler_0_je_nach kind=form lang=de surface="Je nach Blickwinkel" fixes=不同视角
E Form_fix_blickwinkel_materialfehler_0_je_nach FROM_SESSION Session_blickwinkel_materialfehler
V Form_fix_blickwinkel_materialfehler_1_gibt_es kind=form lang=de surface="gibt es" fixes=会有
E Form_fix_blickwinkel_materialfehler_1_gibt_es FROM_SESSION Session_blickwinkel_materialfehler
V Form_fix_blickwinkel_materialfehler_2_materia kind=form lang=de surface=Materialfehler fixes=材质bug
E Form_fix_blickwinkel_materialfehler_2_materia FROM_SESSION Session_blickwinkel_materialfehler

# ingest-session 2026-09-14T09:50:17Z enable-titan-on-other-apps-fehlt lang=de
V Session_enable_titan_on_other_apps_fehlt kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-enable-titan-on-other-apps-fehlt.toon.md
V Focus_enable_titan_on_other_apps_fehlt kind=focus lang=de gloss="nicht — Ich finde … nicht" status=active
E Focus_enable_titan_on_other_apps_fehlt FROM_SESSION Session_enable_titan_on_other_apps_fehlt
V Lemma_de_fix_enable_titan_on_other_apps_fehlt kind=lemma lang=de surface="Ich finde Enable Titan on Other Apps nicht." role=minimal-rewrite
E Lemma_de_fix_enable_titan_on_other_apps_fehlt FROM_SESSION Session_enable_titan_on_other_apps_fehlt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-enable-titan-on-other-apps-fehlt.toon.md
V Form_fix_enable_titan_on_other_apps_fehlt_0_i kind=form lang=de surface="Ich finde … nicht" fixes=没有找到
E Form_fix_enable_titan_on_other_apps_fehlt_0_i FROM_SESSION Session_enable_titan_on_other_apps_fehlt
V Form_fix_enable_titan_on_other_apps_fehlt_1_p kind=form lang=de surface="proper noun kept" fixes="Enable Titan on Other Apps"
E Form_fix_enable_titan_on_other_apps_fehlt_1_p FROM_SESSION Session_enable_titan_on_other_apps_fehlt

# ingest-session 2026-09-14T09:54:58Z imap-example-triage-env lang=de
V Session_imap_example_triage_env kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-imap-example-triage-env.toon.md
V Focus_imap_example_triage_env kind=focus lang=de gloss="dann — dann fülle ich sie aus" status=active
E Focus_imap_example_triage_env FROM_SESSION Session_imap_example_triage_env
V Lemma_de_fix_imap_example_triage_env kind=lemma lang=de surface="Gib mir eine Beispieldatei imap-example-triage.env" role=minimal-rewrite
E Lemma_de_fix_imap_example_triage_env FROM_SESSION Session_imap_example_triage_env SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-imap-example-triage-env.toon.md
V Form_fix_imap_example_triage_env_0_gib_mir_ei kind=form lang=de surface="Gib mir eine Beispieldatei" fixes=给我一个范例
E Form_fix_imap_example_triage_env_0_gib_mir_ei FROM_SESSION Session_imap_example_triage_env
V Form_fix_imap_example_triage_env_1_dann_f_lle kind=form lang=de surface="dann fülle ich sie aus" fixes=然后我填一下
E Form_fix_imap_example_triage_env_1_dann_f_lle FROM_SESSION Session_imap_example_triage_env

# ingest-session 2026-09-14T09:56:18Z imap-passwort-webmail-oder-godaddy lang=de
V Session_imap_passwort_webmail_oder_godaddy kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-imap-passwort-webmail-oder-godaddy.toon.md
V Focus_imap_passwort_webmail_oder_godaddy kind=focus lang=de gloss="oder — Webmail-Passwort oder GoDaddy-Hauptkonto" status=active
E Focus_imap_passwort_webmail_oder_godaddy FROM_SESSION Session_imap_passwort_webmail_oder_godaddy
V Lemma_de_fix_imap_passwort_webmail_oder_godaddy kind=lemma lang=de surface="Wo finde ich das IMAP-Passwort? Ist das das Webmai" role=minimal-rewrite
E Lemma_de_fix_imap_passwort_webmail_oder_godaddy FROM_SESSION Session_imap_passwort_webmail_oder_godaddy SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-imap-passwort-webmail-oder-godaddy.toon.md
V Form_fix_imap_passwort_webmail_oder_godaddy_0 kind=form lang=de surface="Wo finde ich" fixes=哪里找
E Form_fix_imap_passwort_webmail_oder_godaddy_0 FROM_SESSION Session_imap_passwort_webmail_oder_godaddy
V Form_fix_imap_passwort_webmail_oder_godaddy_1 kind=form lang=de surface="Ist das A oder B" fixes=是A还是B
E Form_fix_imap_passwort_webmail_oder_godaddy_1 FROM_SESSION Session_imap_passwort_webmail_oder_godaddy

# ingest-session 2026-09-14T09:58:30Z private-env-ausprobieren lang=de
V Session_private_env_ausprobieren kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-private-env-ausprobieren.toon.md
V Focus_private_env_ausprobieren kind=focus lang=de gloss="mal — Probier es mal" status=active
E Focus_private_env_ausprobieren FROM_SESSION Session_private_env_ausprobieren
V Lemma_de_fix_private_env_ausprobieren kind=lemma lang=de surface="Gut. Ich habe die Datei unter .private aktualisier" role=minimal-rewrite
E Lemma_de_fix_private_env_ausprobieren FROM_SESSION Session_private_env_ausprobieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-private-env-ausprobieren.toon.md
V Form_fix_private_env_ausprobieren_0_ich_habe_ kind=form lang=de surface="Ich habe … aktualisiert" fixes=我更新了一下
E Form_fix_private_env_ausprobieren_0_ich_habe_ FROM_SESSION Session_private_env_ausprobieren
V Form_fix_private_env_ausprobieren_1_probier_e kind=form lang=de surface="Probier es mal" fixes=试试看
E Form_fix_private_env_ausprobieren_1_probier_e FROM_SESSION Session_private_env_ausprobieren

# ingest-session 2026-09-14T10:19:14Z mails-nach-system-sortieren lang=de
V Session_mails_nach_system_sortieren kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mails-nach-system-sortieren.toon.md
V Focus_mails_nach_system_sortieren kind=focus lang=de gloss="nicht — Beschränke dich nicht auf die vorhandenen " status=active
E Focus_mails_nach_system_sortieren FROM_SESSION Session_mails_nach_system_sortieren
V Lemma_de_fix_mails_nach_system_sortieren kind=lemma lang=de surface="Gut. Bei so vielen Mails fängst du selbst an. Besc" role=minimal-rewrite
E Lemma_de_fix_mails_nach_system_sortieren FROM_SESSION Session_mails_nach_system_sortieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mails-nach-system-sortieren.toon.md
V Form_fix_mails_nach_system_sortieren_0_beschr kind=form lang=de surface="Beschränke dich nicht auf" fixes=不要局限于
E Form_fix_mails_nach_system_sortieren_0_beschr FROM_SESSION Session_mails_nach_system_sortieren
V Form_fix_mails_nach_system_sortieren_1_nach_m kind=form lang=de surface="nach meinem System" fixes=根据我这个系统
E Form_fix_mails_nach_system_sortieren_1_nach_m FROM_SESSION Session_mails_nach_system_sortieren
V Form_fix_mails_nach_system_sortieren_2_k_nfti kind=form lang=de surface="Künftig … jeden Tag" fixes=以后每天
E Form_fix_mails_nach_system_sortieren_2_k_nfti FROM_SESSION Session_mails_nach_system_sortieren

# ingest-session 2026-09-14T10:56:45Z zero-inbox-todo lang=de
V Session_zero_inbox_todo kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zero-inbox-todo.toon.md
V Focus_zero_inbox_todo kind=focus lang=de gloss="soll — soll in den Ordner Todo" status=active
E Focus_zero_inbox_todo FROM_SESSION Session_zero_inbox_todo
V Lemma_de_fix_zero_inbox_todo kind=lemma lang=de surface="Ich will eine Zero-Inbox-Policy. Alles, was mich b" role=minimal-rewrite
E Lemma_de_fix_zero_inbox_todo FROM_SESSION Session_zero_inbox_todo SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zero-inbox-todo.toon.md
V Form_fix_zero_inbox_todo_0_ich_will_eine_zero kind=form lang=de surface="Ich will eine Zero-Inbox-Policy" fixes="我要零inbox policy"
E Form_fix_zero_inbox_todo_0_ich_will_eine_zero FROM_SESSION Session_zero_inbox_todo
V Form_fix_zero_inbox_todo_1_alles_was_mich_bet kind=form lang=de surface="Alles, was mich betrifft, soll in den Or" fixes=和我有关的…进到todo
E Form_fix_zero_inbox_todo_1_alles_was_mich_bet FROM_SESSION Session_zero_inbox_todo

# ingest-session 2026-09-14T11:06:02Z zero-inbox-goal-loop lang=de
V Session_zero_inbox_goal_loop kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zero-inbox-goal-loop.toon.md
V Focus_zero_inbox_goal_loop kind=focus lang=de gloss="klar — ein klares Ziel" status=active
E Focus_zero_inbox_goal_loop FROM_SESSION Session_zero_inbox_goal_loop
V Lemma_de_fix_zero_inbox_goal_loop kind=lemma lang=de surface="Ich brauche ein klares Ziel: Zero Inbox, und Todo " role=minimal-rewrite
E Lemma_de_fix_zero_inbox_goal_loop FROM_SESSION Session_zero_inbox_goal_loop SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-zero-inbox-goal-loop.toon.md
V Form_fix_zero_inbox_goal_loop_0_ein_klares_zi kind=form lang=de surface="ein klares Ziel" fixes=目标明确
E Form_fix_zero_inbox_goal_loop_0_ein_klares_zi FROM_SESSION Session_zero_inbox_goal_loop
V Form_fix_zero_inbox_goal_loop_1_todo_soll_all kind=form lang=de surface="Todo soll alles Wichtige perfekt erfasse" fixes=todo完美捕捉
E Form_fix_zero_inbox_goal_loop_1_todo_soll_all FROM_SESSION Session_zero_inbox_goal_loop

# ingest-session 2026-09-14T11:37:55Z life-ordner-zusammenlegen-werbung-weg lang=de
V Session_life_ordner_zusammenlegen_werbung_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-life-ordner-zusammenlegen-werbung-weg.toon.md
V Focus_life_ordner_zusammenlegen_werbung_weg kind=focus lang=de gloss="außer — außer was mit Bezahlen, Recht und Arbeit z" status=active
E Focus_life_ordner_zusammenlegen_werbung_weg FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg
V Lemma_de_fix_life_ordner_zusammenlegen_werbung_weg kind=lemma lang=de surface="Die alten Life-Ordner sollen in neue zusammen. Von" role=minimal-rewrite
E Lemma_de_fix_life_ordner_zusammenlegen_werbung_weg FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-life-ordner-zusammenlegen-werbung-weg.toon.md
V Form_fix_life_ordner_zusammenlegen_werbung_we kind=form lang=de surface="in neue zusammen" fixes=整合进新的
E Form_fix_life_ordner_zusammenlegen_werbung_we FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg
V Form_fix_life_ordner_zusammenlegen_werbung_we kind=form lang=de surface="außer …" fixes=除了…之外
E Form_fix_life_ordner_zusammenlegen_werbung_we FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg
V Form_fix_life_ordner_zusammenlegen_werbung_we kind=form lang=de surface="lösche die Werbung" fixes=广告无用的东西全部删除
E Form_fix_life_ordner_zusammenlegen_werbung_we FROM_SESSION Session_life_ordner_zusammenlegen_werbung_weg

# ingest-session 2026-09-14T13:59:56Z billing-rechnungen-keine-payback lang=de
V Session_billing_rechnungen_keine_payback kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-rechnungen-keine-payback.toon.md
V Focus_billing_rechnungen_keine_payback kind=focus lang=de gloss="für welche — indirekter Fragesatz (sehen, für welc" status=active
E Focus_billing_rechnungen_keine_payback FROM_SESSION Session_billing_rechnungen_keine_payback
V Lemma_de_fix_billing_rechnungen_keine_payback kind=lemma lang=de surface="Billing soll die Rechnungen enthalten. Ich will se" role=minimal-rewrite
E Lemma_de_fix_billing_rechnungen_keine_payback FROM_SESSION Session_billing_rechnungen_keine_payback SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-rechnungen-keine-payback.toon.md
V Form_fix_billing_rechnungen_keine_payback_0_w kind=form lang=de surface="welche Dienste" fixes=那些服务
E Form_fix_billing_rechnungen_keine_payback_0_w FROM_SESSION Session_billing_rechnungen_keine_payback
V Form_fix_billing_rechnungen_keine_payback_1_i kind=form lang=de surface="ich will sehen, für welche Dienste ich g" fixes=我要知道我现在在为…付费
E Form_fix_billing_rechnungen_keine_payback_1_i FROM_SESSION Session_billing_rechnungen_keine_payback
V Form_fix_billing_rechnungen_keine_payback_2_w kind=form lang=de surface="warum liegen da … und so etwas" fixes=怎么里边有一些…啥的这些
E Form_fix_billing_rechnungen_keine_payback_2_w FROM_SESSION Session_billing_rechnungen_keine_payback

# ingest-session 2026-09-14T14:02:53Z leere-ordner-loeschen lang=de
V Session_leere_ordner_loeschen kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-leere-ordner-loeschen.toon.md
V Focus_leere_ordner_loeschen kind=focus lang=de gloss="alle leeren Ordner — attributives Adjektiv vor dem" status=active
E Focus_leere_ordner_loeschen FROM_SESSION Session_leere_ordner_loeschen
V Lemma_de_fix_leere_ordner_loeschen kind=lemma lang=de surface="Lösche alle leeren Ordner." role=minimal-rewrite
E Lemma_de_fix_leere_ordner_loeschen FROM_SESSION Session_leere_ordner_loeschen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-leere-ordner-loeschen.toon.md
V Form_fix_leere_ordner_loeschen_0_leeren_ordne kind=form lang=de surface="leeren Ordner" fixes=空的文件夹
E Form_fix_leere_ordner_loeschen_0_leeren_ordne FROM_SESSION Session_leere_ordner_loeschen
V Form_fix_leere_ordner_loeschen_1_l_sche_alle_ kind=form lang=de surface="Lösche alle …" fixes=全部删掉
E Form_fix_leere_ordner_loeschen_1_l_sche_alle_ FROM_SESSION Session_leere_ordner_loeschen

# ingest-session 2026-09-14T14:29:48Z mails-statistisch-klassifizieren-pdf lang=de
V Session_mails_statistisch_klassifizieren_pdf kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mails-statistisch-klassifizieren-pdf.toon.md
V Focus_mails_statistisch_klassifizieren_pdf kind=focus lang=de gloss="damit ich sehe — Finalsatz (Zweck)" status=active
E Focus_mails_statistisch_klassifizieren_pdf FROM_SESSION Session_mails_statistisch_klassifizieren_pdf
V Lemma_de_fix_mails_statistisch_klassifizieren_pdf kind=lemma lang=de surface="So viele Mails. Zähle und klassifiziere alle, dami" role=minimal-rewrite
E Lemma_de_fix_mails_statistisch_klassifizieren_pdf FROM_SESSION Session_mails_statistisch_klassifizieren_pdf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mails-statistisch-klassifizieren-pdf.toon.md
V Form_fix_mails_statistisch_klassifizieren_pdf kind=form lang=de surface="damit ich sehe, wie ich sie steuern kann" fixes=让我看看怎么去治理
E Form_fix_mails_statistisch_klassifizieren_pdf FROM_SESSION Session_mails_statistisch_klassifizieren_pdf
V Form_fix_mails_statistisch_klassifizieren_pdf kind=form lang=de surface="zähle und klassifiziere alle" fixes="所有邮件进行统计 分类"
E Form_fix_mails_statistisch_klassifizieren_pdf FROM_SESSION Session_mails_statistisch_klassifizieren_pdf
V Form_fix_mails_statistisch_klassifizieren_pdf kind=form lang=de surface="zeig mir das als LaTeX-PDF" fixes="pdf latex给我展示一下"
E Form_fix_mails_statistisch_klassifizieren_pdf FROM_SESSION Session_mails_statistisch_klassifizieren_pdf

# ingest-session 2026-09-14T15:20:02Z ablehnung-loeschen-anmerkungswuerdig lang=de
V Session_ablehnung_loeschen_anmerkungswuerdig kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-ablehnung-loeschen-anmerkungswuerdig.toon.md
V Focus_ablehnung_loeschen_anmerkungswuerdig kind=focus lang=de gloss="anmerkungswürdig — Adjektiv, Plural Akkusativ (die" status=active
E Focus_ablehnung_loeschen_anmerkungswuerdig FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig
V Lemma_de_fix_ablehnung_loeschen_anmerkungswuerdig kind=lemma lang=de surface="Ach so — diese Absagen vom Arbeitgeber einfach lös" role=minimal-rewrite
E Lemma_de_fix_ablehnung_loeschen_anmerkungswuerdig FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-ablehnung-loeschen-anmerkungswuerdig.toon.md
V Form_fix_ablehnung_loeschen_anmerkungswuerdig kind=form lang=de surface="anmerkungswürdigen Nachrichten" fixes="Anmerkungswertvoller Nachricht"
E Form_fix_ablehnung_loeschen_anmerkungswuerdig FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig
V Form_fix_ablehnung_loeschen_anmerkungswuerdig kind=form lang=de surface="einfach löschen? / löschen Sie sie" fixes="löschen Sie es"
E Form_fix_ablehnung_loeschen_anmerkungswuerdig FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig
V Form_fix_ablehnung_loeschen_anmerkungswuerdig kind=form lang=de surface="vom Arbeitgeber" fixes="von dem Arbeitgeber"
E Form_fix_ablehnung_loeschen_anmerkungswuerdig FROM_SESSION Session_ablehnung_loeschen_anmerkungswuerdig

# ingest-session 2026-09-14T15:25:18Z anstrengen-aesthetischer-chill lang=de
V Session_anstrengen_aesthetischer_chill kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-anstrengen-aesthetischer-chill.toon.md
V Focus_anstrengen_aesthetischer_chill kind=focus lang=de gloss="Wenn ich mich anstrenge (mich + trennbares an-)" status=active
E Focus_anstrengen_aesthetischer_chill FROM_SESSION Session_anstrengen_aesthetischer_chill
V Lemma_de_fix_anstrengen_aesthetischer_chill kind=lemma lang=de surface="Ok, ok. Wenn ich mich anstrenge, zu denken und an " role=minimal-rewrite
E Lemma_de_fix_anstrengen_aesthetischer_chill FROM_SESSION Session_anstrengen_aesthetischer_chill SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-anstrengen-aesthetischer-chill.toon.md
V Form_fix_anstrengen_aesthetischer_chill_0_wen kind=form lang=de surface="Wenn ich mich anstrenge" fixes="wann ich strenge sich selbst"
E Form_fix_anstrengen_aesthetischer_chill_0_wen FROM_SESSION Session_anstrengen_aesthetischer_chill
V Form_fix_anstrengen_aesthetischer_chill_1_an_ kind=form lang=de surface="an komplizierten Informationen zu arbeit" fixes="auf komplizierte Informationen"
E Form_fix_anstrengen_aesthetischer_chill_1_an_ FROM_SESSION Session_anstrengen_aesthetischer_chill
V Form_fix_anstrengen_aesthetischer_chill_2_das kind=form lang=de surface="dasselbe Gefühl des ästhetischen Chills" fixes="denselbe Gefühl der Aesthetik "
E Form_fix_anstrengen_aesthetischer_chill_2_das FROM_SESSION Session_anstrengen_aesthetischer_chill
V Form_fix_anstrengen_aesthetischer_chill_3_mei kind=form lang=de surface="mein Gehirn sich aktiviert hat" fixes="meine Gehirn hat sich aktivier"
E Form_fix_anstrengen_aesthetischer_chill_3_mei FROM_SESSION Session_anstrengen_aesthetischer_chill

# ingest-session 2026-09-14T16:24:47Z payback-loeschen-ordner-kuerzen lang=de
V Session_payback_loeschen_ordner_kuerzen kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-payback-loeschen-ordner-kuerzen.toon.md
V Focus_payback_loeschen_ordner_kuerzen kind=focus lang=de gloss="Ihren / alle / die Ordner — Akkusativ + Plural ohn" status=active
E Focus_payback_loeschen_ordner_kuerzen FROM_SESSION Session_payback_loeschen_ordner_kuerzen
V Lemma_de_fix_payback_loeschen_ordner_kuerzen kind=lemma lang=de surface="Wenn es um die Payback-Karten-Mails „Danke für Ihr" role=minimal-rewrite
E Lemma_de_fix_payback_loeschen_ordner_kuerzen FROM_SESSION Session_payback_loeschen_ordner_kuerzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-payback-loeschen-ordner-kuerzen.toon.md
V Form_fix_payback_loeschen_ordner_kuerzen_0_da kind=form lang=de surface="Danke für Ihren Einkauf" fixes="Danke für Ihre Einkauf"
E Form_fix_payback_loeschen_ordner_kuerzen_0_da FROM_SESSION Session_payback_loeschen_ordner_kuerzen
V Form_fix_payback_loeschen_ordner_kuerzen_1_l_ kind=form lang=de surface="löschen Sie sie bitte alle" fixes="löschen Sie sie alles"
E Form_fix_payback_loeschen_ordner_kuerzen_1_l_ FROM_SESSION Session_payback_loeschen_ordner_kuerzen
V Form_fix_payback_loeschen_ordner_kuerzen_2_di kind=form lang=de surface="die Ordner" fixes="die Ordnern"
E Form_fix_payback_loeschen_ordner_kuerzen_2_di FROM_SESSION Session_payback_loeschen_ordner_kuerzen
V Form_fix_payback_loeschen_ordner_kuerzen_3_in kind=form lang=de surface="integrieren Sie sie in die anderen Ordne" fixes="intergrieren … ins anderen Ord"
E Form_fix_payback_loeschen_ordner_kuerzen_3_in FROM_SESSION Session_payback_loeschen_ordner_kuerzen

# ingest-session 2026-09-14T17:03:53Z billing-n26-werbung-raus lang=de
V Session_billing_n26_werbung_raus kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-n26-werbung-raus.toon.md
V Focus_billing_n26_werbung_raus kind=focus lang=de gloss="die mich nichts angehen — Relativsatz, Plural, Akk" status=active
E Focus_billing_n26_werbung_raus FROM_SESSION Session_billing_n26_werbung_raus
V Lemma_de_fix_billing_n26_werbung_raus kind=lemma lang=de surface="Im Billing-Ordner gibt es noch viele wertlose E-Ma" role=minimal-rewrite
E Lemma_de_fix_billing_n26_werbung_raus FROM_SESSION Session_billing_n26_werbung_raus SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-n26-werbung-raus.toon.md
V Form_fix_billing_n26_werbung_raus_0_im_billin kind=form lang=de surface="Im Billing-Ordner" fixes="Bei Billing Ordner"
E Form_fix_billing_n26_werbung_raus_0_im_billin FROM_SESSION Session_billing_n26_werbung_raus
V Form_fix_billing_n26_werbung_raus_1_wertlose_ kind=form lang=de surface="wertlose E-Mails" fixes="Wertlose Email"
E Form_fix_billing_n26_werbung_raus_1_wertlose_ FROM_SESSION Session_billing_n26_werbung_raus
V Form_fix_billing_n26_werbung_raus_2_n26_werbu kind=form lang=de surface="N26-Werbung und Aktionen" fixes="N26 werbungen und Aktion"
E Form_fix_billing_n26_werbung_raus_2_n26_werbu FROM_SESSION Session_billing_n26_werbung_raus
V Form_fix_billing_n26_werbung_raus_3_die_mich_ kind=form lang=de surface="die mich nichts angehen" fixes="die mir nichts angeht"
E Form_fix_billing_n26_werbung_raus_3_die_mich_ FROM_SESSION Session_billing_n26_werbung_raus

# ingest-session 2026-09-14T17:09:26Z billing-loeschvorschlag-aehnliche-mails lang=de
V Session_billing_loeschvorschlag_aehnliche_mails kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-loeschvorschlag-aehnliche-mails.toon.md
V Focus_billing_loeschvorschlag_aehnliche_mails kind=focus lang=de gloss="auch noch ähnliche — Partikel + Adjektiv" status=active
E Focus_billing_loeschvorschlag_aehnliche_mails FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails
V Lemma_de_fix_billing_loeschvorschlag_aehnliche_mails kind=lemma lang=de surface="Es gibt im Billing-Ordner auch noch ähnliche wertl" role=minimal-rewrite
E Lemma_de_fix_billing_loeschvorschlag_aehnliche_mails FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-loeschvorschlag-aehnliche-mails.toon.md
V Form_fix_billing_loeschvorschlag_aehnliche_ma kind=form lang=de surface="auch noch" fixes="noch auch"
E Form_fix_billing_loeschvorschlag_aehnliche_ma FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails
V Form_fix_billing_loeschvorschlag_aehnliche_ma kind=form lang=de surface=ähnliche fixes=änliche
E Form_fix_billing_loeschvorschlag_aehnliche_ma FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails
V Form_fix_billing_loeschvorschlag_aehnliche_ma kind=form lang=de surface=Löschvorschlag fixes=Löschungsvorschlag
E Form_fix_billing_loeschvorschlag_aehnliche_ma FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails
V Form_fix_billing_loeschvorschlag_aehnliche_ma kind=form lang=de surface="im Billing-Ordner" fixes="im Billing Ordner"
E Form_fix_billing_loeschvorschlag_aehnliche_ma FROM_SESSION Session_billing_loeschvorschlag_aehnliche_mails

# ingest-session 2026-09-14T17:52:40Z mailbox-shenyou-wertlos-weg lang=de
V Session_mailbox_shenyou_wertlos_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mailbox-shenyou-wertlos-weg.toon.md
V Focus_mailbox_shenyou_wertlos_weg kind=focus lang=de gloss="schrittweise — Adverb (entferne schrittweise alles" status=active
E Focus_mailbox_shenyou_wertlos_weg FROM_SESSION Session_mailbox_shenyou_wertlos_weg
V Lemma_de_fix_mailbox_shenyou_wertlos_weg kind=lemma lang=de surface="Fang in meinem Postfach an zu wandern. Sieh dir ei" role=minimal-rewrite
E Lemma_de_fix_mailbox_shenyou_wertlos_weg FROM_SESSION Session_mailbox_shenyou_wertlos_weg SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-mailbox-shenyou-wertlos-weg.toon.md
V Form_fix_mailbox_shenyou_wertlos_weg_0_fang_i kind=form lang=de surface="Fang in meinem Postfach an zu wandern" fixes=开始在我的邮箱里边神游
E Form_fix_mailbox_shenyou_wertlos_weg_0_fang_i FROM_SESSION Session_mailbox_shenyou_wertlos_weg
V Form_fix_mailbox_shenyou_wertlos_weg_1_sieh_d kind=form lang=de surface="Sieh dir einige Mails genauer an" fixes=具体查看一些邮件的具体信息
E Form_fix_mailbox_shenyou_wertlos_weg_1_sieh_d FROM_SESSION Session_mailbox_shenyou_wertlos_weg
V Form_fix_mailbox_shenyou_wertlos_weg_2_entfer kind=form lang=de surface="entferne schrittweise alles Wertlose" fixes=逐步把…没用的…去掉
E Form_fix_mailbox_shenyou_wertlos_weg_2_entfer FROM_SESSION Session_mailbox_shenyou_wertlos_weg

# ingest-session 2026-09-14T18:21:26Z linkedin-post-ins-deutsche lang=de
V Session_linkedin_post_ins_deutsche kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-linkedin-post-ins-deutsche.toon.md
V Focus_linkedin_post_ins_deutsche kind=focus lang=de gloss="um + zu — um ihn erneut zu teilen" status=active
E Focus_linkedin_post_ins_deutsche FROM_SESSION Session_linkedin_post_ins_deutsche
V Lemma_de_fix_linkedin_post_ins_deutsche kind=lemma lang=de surface="Übersetze diesen LinkedIn-Post ins Deutsche, um ih" role=minimal-rewrite
E Lemma_de_fix_linkedin_post_ins_deutsche FROM_SESSION Session_linkedin_post_ins_deutsche SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-linkedin-post-ins-deutsche.toon.md
V Form_fix_linkedin_post_ins_deutsche_0_bersetz kind=form lang=de surface="Übersetze … ins Deutsche" fixes=翻译成德文
E Form_fix_linkedin_post_ins_deutsche_0_bersetz FROM_SESSION Session_linkedin_post_ins_deutsche
V Form_fix_linkedin_post_ins_deutsche_1_um_ihn_ kind=form lang=de surface="um ihn erneut zu teilen" fixes="我再repost 一次"
E Form_fix_linkedin_post_ins_deutsche_1_um_ihn_ FROM_SESSION Session_linkedin_post_ins_deutsche

# auto-gap 2026-09-14T18:30:40Z surface=le
V Concept_gap_fr_le kind=concept gloss=unknown-expression-in-de status=open
V Gap_fr_le kind=gap lang=fr surface=le target=de status=open
V Lemma_fr_fr_le kind=lemma lang=fr surface=le
E Concept_gap_fr_le EXPRESSES Lemma_fr_fr_le SOURCE=hook/beforeSubmitPrompt
E Lemma_fr_fr_le GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_fr_le GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-14T18:32:42Z billing-aelter-als-ein-jahr-weg lang=de
V Session_billing_aelter_als_ein_jahr_weg kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-aelter-als-ein-jahr-weg.toon.md
V Focus_billing_aelter_als_ein_jahr_weg kind=focus lang=de gloss="älter als ein Jahr — Vergleich" status=active
E Focus_billing_aelter_als_ein_jahr_weg FROM_SESSION Session_billing_aelter_als_ein_jahr_weg
V Lemma_de_fix_billing_aelter_als_ein_jahr_weg kind=lemma lang=de surface="Ach so, im Billing-Ordner gibt es noch hinfällige " role=minimal-rewrite
E Lemma_de_fix_billing_aelter_als_ein_jahr_weg FROM_SESSION Session_billing_aelter_als_ein_jahr_weg SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-billing-aelter-als-ein-jahr-weg.toon.md
V Form_fix_billing_aelter_als_ein_jahr_weg_0_lt kind=form lang=de surface="älter als ein Jahr" fixes="als alt as ein Jahr zurück"
E Form_fix_billing_aelter_als_ein_jahr_weg_0_lt FROM_SESSION Session_billing_aelter_als_ein_jahr_weg
V Form_fix_billing_aelter_als_ein_jahr_weg_1_wi kind=form lang=de surface=wiederholenden fixes=wiederholdende
E Form_fix_billing_aelter_als_ein_jahr_weg_1_wi FROM_SESSION Session_billing_aelter_als_ein_jahr_weg
V Form_fix_billing_aelter_als_ein_jahr_weg_2_ba kind=form lang=de surface="banaler Aktionen" fixes="banäle Aktionen"
E Form_fix_billing_aelter_als_ein_jahr_weg_2_ba FROM_SESSION Session_billing_aelter_als_ein_jahr_weg
V Form_fix_billing_aelter_als_ein_jahr_weg_3_ma kind=form lang=de surface="Mails zum Bestätigen" fixes="Email zu bestätigen"
E Form_fix_billing_aelter_als_ein_jahr_weg_3_ma FROM_SESSION Session_billing_aelter_als_ein_jahr_weg

# ingest-session 2026-09-14T18:35:00Z wie-man-es-benutzt lang=de
V Session_wie_man_es_benutzt kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wie-man-es-benutzt.toon.md
V Focus_wie_man_es_benutzt kind=focus lang=de gloss="man — wie man es benutzt (nicht Mann)" status=active
E Focus_wie_man_es_benutzt FROM_SESSION Session_wie_man_es_benutzt
V Lemma_de_fix_wie_man_es_benutzt kind=lemma lang=de surface="Mach es im tmp-Ordner. Ich brauche eine Masterclas" role=minimal-rewrite
E Lemma_de_fix_wie_man_es_benutzt FROM_SESSION Session_wie_man_es_benutzt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-wie-man-es-benutzt.toon.md
V Form_fix_wie_man_es_benutzt_0_wie_man_es_benu kind=form lang=de surface="wie man es benutzt" fixes="wie Mann es benutzen"
E Form_fix_wie_man_es_benutzt_0_wie_man_es_benu FROM_SESSION Session_wie_man_es_benutzt
V Form_fix_wie_man_es_benutzt_1_im_tmp_ordner kind=form lang=de surface="im tmp-Ordner" fixes="im tmp Ordner"
E Form_fix_wie_man_es_benutzt_1_im_tmp_ordner FROM_SESSION Session_wie_man_es_benutzt
V Form_fix_wie_man_es_benutzt_2_f_r_dieses_code kind=form lang=de surface="für dieses Code-Repository" fixes="für diese Code repo"
E Form_fix_wie_man_es_benutzt_2_f_r_dieses_code FROM_SESSION Session_wie_man_es_benutzt

# ingest-session 2026-09-14T18:41:02Z noch-diese-solchen-nachrichten lang=de
V Session_noch_diese_solchen_nachrichten kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-noch-diese-solchen-nachrichten.toon.md
V Focus_noch_diese_solchen_nachrichten kind=focus lang=de gloss="die ich nicht behalten möchte — Relativsatz, Verb " status=active
E Focus_noch_diese_solchen_nachrichten FROM_SESSION Session_noch_diese_solchen_nachrichten
V Lemma_de_fix_noch_diese_solchen_nachrichten kind=lemma lang=de surface="Noch diese solchen Nachrichten, die ich nicht beha" role=minimal-rewrite
E Lemma_de_fix_noch_diese_solchen_nachrichten FROM_SESSION Session_noch_diese_solchen_nachrichten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-noch-diese-solchen-nachrichten.toon.md
V Form_fix_noch_diese_solchen_nachrichten_0_sol kind=form lang=de surface="solchen Nachrichten" fixes="solche Narichten"
E Form_fix_noch_diese_solchen_nachrichten_0_sol FROM_SESSION Session_noch_diese_solchen_nachrichten
V Form_fix_noch_diese_solchen_nachrichten_1_die kind=form lang=de surface="die ich" fixes="den Ich"
E Form_fix_noch_diese_solchen_nachrichten_1_die FROM_SESSION Session_noch_diese_solchen_nachrichten
V Form_fix_noch_diese_solchen_nachrichten_2_nic kind=form lang=de surface="nicht behalten möchte" fixes="nicht möchte bleiben"
E Form_fix_noch_diese_solchen_nachrichten_2_nic FROM_SESSION Session_noch_diese_solchen_nachrichten
V Form_fix_noch_diese_solchen_nachrichten_3_beh kind=form lang=de surface=behalten fixes=bleiben
E Form_fix_noch_diese_solchen_nachrichten_3_beh FROM_SESSION Session_noch_diese_solchen_nachrichten

# ingest-session 2026-09-14T19:01:23Z kenntnisse-ueber-zk lang=de
V Session_kenntnisse_ueber_zk kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-kenntnisse-ueber-zk.toon.md
V Focus_kenntnisse_ueber_zk kind=focus lang=de gloss="Kenntnisse über + Akk — Kenntnisse über ZK (nicht " status=active
E Focus_kenntnisse_ueber_zk FROM_SESSION Session_kenntnisse_ueber_zk
V Lemma_de_fix_kenntnisse_ueber_zk kind=lemma lang=de surface="Also brauche ich mehr Kenntnisse über ZK im Gebiet" role=minimal-rewrite
E Lemma_de_fix_kenntnisse_ueber_zk FROM_SESSION Session_kenntnisse_ueber_zk SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-kenntnisse-ueber-zk.toon.md
V Form_fix_kenntnisse_ueber_zk_0_kenntnisse_ber kind=form lang=de surface="Kenntnisse über ZK" fixes="Kenntnisse auf ZK"
E Form_fix_kenntnisse_ueber_zk_0_kenntnisse_ber FROM_SESSION Session_kenntnisse_ueber_zk
V Form_fix_kenntnisse_ueber_zk_1_ist_mir_noch_n kind=form lang=de surface="ist mir noch nicht vertraut" fixes="vor mir ist … nicht vertraut"
E Form_fix_kenntnisse_ueber_zk_1_ist_mir_noch_n FROM_SESSION Session_kenntnisse_ueber_zk
V Form_fix_kenntnisse_ueber_zk_2_von_cloudflare kind=form lang=de surface="von Cloudflare" fixes="der Cloudflare"
E Form_fix_kenntnisse_ueber_zk_2_von_cloudflare FROM_SESSION Session_kenntnisse_ueber_zk
V Form_fix_kenntnisse_ueber_zk_3_den_wissensgra kind=form lang=de surface="den Wissensgraphen" fixes=Kenntnisse-Graph
E Form_fix_kenntnisse_ueber_zk_3_den_wissensgra FROM_SESSION Session_kenntnisse_ueber_zk

# ingest-session 2026-09-14T19:01:52Z life-linkedin-dhl-korrespondenz lang=de
V Session_life_linkedin_dhl_korrespondenz kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-life-linkedin-dhl-korrespondenz.toon.md
V Focus_life_linkedin_dhl_korrespondenz kind=focus lang=de gloss="solche Nachrichten — Demonstrativ, nicht diese sol" status=active
E Focus_life_linkedin_dhl_korrespondenz FROM_SESSION Session_life_linkedin_dhl_korrespondenz
V Lemma_de_fix_life_linkedin_dhl_korrespondenz kind=lemma lang=de surface="So, es gibt noch solche Nachrichten, die ich nicht" role=minimal-rewrite
E Lemma_de_fix_life_linkedin_dhl_korrespondenz FROM_SESSION Session_life_linkedin_dhl_korrespondenz SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-life-linkedin-dhl-korrespondenz.toon.md
V Form_fix_life_linkedin_dhl_korrespondenz_0_so kind=form lang=de surface="solche Nachrichten" fixes="diese solchen Narichten"
E Form_fix_life_linkedin_dhl_korrespondenz_0_so FROM_SESSION Session_life_linkedin_dhl_korrespondenz
V Form_fix_life_linkedin_dhl_korrespondenz_1_li kind=form lang=de surface=LinkedIn-Kontaktanfragen fixes="LinkedIn Freund Request"
E Form_fix_life_linkedin_dhl_korrespondenz_1_li FROM_SESSION Session_life_linkedin_dhl_korrespondenz
V Form_fix_life_linkedin_dhl_korrespondenz_2_ko kind=form lang=de surface=Korrespondenz fixes=Korrenzpondenz
E Form_fix_life_linkedin_dhl_korrespondenz_2_ko FROM_SESSION Session_life_linkedin_dhl_korrespondenz
V Form_fix_life_linkedin_dhl_korrespondenz_3_ma kind=form lang=de surface="mag ich das nicht" fixes="mag ich es nicht"
E Form_fix_life_linkedin_dhl_korrespondenz_3_ma FROM_SESSION Session_life_linkedin_dhl_korrespondenz

# ingest-session 2026-09-14T19:03:18Z auch-agent-tty lang=de
V Session_auch_agent_tty kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-auch-agent-tty.toon.md
V Focus_auch_agent_tty kind=focus lang=de gloss="sogenannten — die sogenannten Agent-TTYs" status=active
E Focus_auch_agent_tty FROM_SESSION Session_auch_agent_tty
V Lemma_de_fix_auch_agent_tty kind=lemma lang=de surface="Nimm auch die sogenannten Agent-TTYs und Java Syst" role=minimal-rewrite
E Lemma_de_fix_auch_agent_tty FROM_SESSION Session_auch_agent_tty SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-auch-agent-tty.toon.md
V Form_fix_auch_agent_tty_0_agent_ttys kind=form lang=de surface=Agent-TTYs fixes="agent tty"
E Form_fix_auch_agent_tty_0_agent_ttys FROM_SESSION Session_auch_agent_tty
V Form_fix_auch_agent_tty_1_nimm_in_den_wissens kind=form lang=de surface="Nimm … in den Wissensgraphen auf" fixes="Fragment ohne Verb"
E Form_fix_auch_agent_tty_1_nimm_in_den_wissens FROM_SESSION Session_auch_agent_tty

# ingest-session 2026-09-14T19:05:50Z vollstaendigkeit-verstaendnis lang=de
V Session_vollstaendigkeit_verstaendnis kind=session date=2026-09-14 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-vollstaendigkeit-verstaendnis.toon.md
V Focus_vollstaendigkeit_verstaendnis kind=focus lang=de gloss="Kenntnisstand — meinem Kenntnisstand (nicht 'Kennt" status=active
E Focus_vollstaendigkeit_verstaendnis FROM_SESSION Session_vollstaendigkeit_verstaendnis
V Lemma_de_fix_vollstaendigkeit_verstaendnis kind=lemma lang=de surface="Also, basierend auf meiner Rückmeldung zu meinem K" role=minimal-rewrite
E Lemma_de_fix_vollstaendigkeit_verstaendnis FROM_SESSION Session_vollstaendigkeit_verstaendnis SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-14-vollstaendigkeit-verstaendnis.toon.md
V Form_fix_vollstaendigkeit_verstaendnis_0_basi kind=form lang=de surface="basierend auf" fixes="basiert von"
E Form_fix_vollstaendigkeit_verstaendnis_0_basi FROM_SESSION Session_vollstaendigkeit_verstaendnis
V Form_fix_vollstaendigkeit_verstaendnis_1_kenn kind=form lang=de surface=Kenntnisstand fixes="Kenntnisse Niveau"
E Form_fix_vollstaendigkeit_verstaendnis_1_kenn FROM_SESSION Session_vollstaendigkeit_verstaendnis
V Form_fix_vollstaendigkeit_verstaendnis_2_fehl kind=form lang=de surface="fehlenden Kenntnisse" fixes="fehlend Kenntnisse"
E Form_fix_vollstaendigkeit_verstaendnis_2_fehl FROM_SESSION Session_vollstaendigkeit_verstaendnis
V Form_fix_vollstaendigkeit_verstaendnis_3_voll kind=form lang=de surface=Vollständigkeit fixes=Kompletness
E Form_fix_vollstaendigkeit_verstaendnis_3_voll FROM_SESSION Session_vollstaendigkeit_verstaendnis
V Form_fix_vollstaendigkeit_verstaendnis_4_vers kind=form lang=de surface=Verständnis fixes=Verstehung
E Form_fix_vollstaendigkeit_verstaendnis_4_vers FROM_SESSION Session_vollstaendigkeit_verstaendnis

# ingest-session 2026-09-15T12:57:03Z scapula-wieder-angefangen lang=de
V Session_scapula_wieder_angefangen kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-scapula-wieder-angefangen.toon.md
V Focus_scapula_wieder_angefangen kind=focus lang=de gloss="wieder + Perfekt (recurrence) vs immer noch (resid" status=active
E Focus_scapula_wieder_angefangen FROM_SESSION Session_scapula_wieder_angefangen
V Lemma_de_fix_scapula_wieder_angefangen kind=lemma lang=de surface="Vor dem 15. September hat die linke Skapula wieder" role=minimal-rewrite
E Lemma_de_fix_scapula_wieder_angefangen FROM_SESSION Session_scapula_wieder_angefangen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-scapula-wieder-angefangen.toon.md
V Form_fix_scapula_wieder_angefangen_0_hat_wied kind=form lang=de surface="hat wieder angefangen zu schmerzen" fixes=仍然开始疼了
E Form_fix_scapula_wieder_angefangen_0_hat_wied FROM_SESSION Session_scapula_wieder_angefangen
V Form_fix_scapula_wieder_angefangen_1_immer_no kind=form lang=de surface="immer noch ein Problem" fixes=还是有问题
E Form_fix_scapula_wieder_angefangen_1_immer_no FROM_SESSION Session_scapula_wieder_angefangen
V Form_fix_scapula_wieder_angefangen_2_vor_dem_ kind=form lang=de surface="vor dem 15. September" fixes=9/15日之前
E Form_fix_scapula_wieder_angefangen_2_vor_dem_ FROM_SESSION Session_scapula_wieder_angefangen

# ingest-session 2026-09-15T13:22:29Z zum-kenntnisdiagramm lang=de
V Session_zum_kenntnisdiagramm kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-zum-kenntnisdiagramm.toon.md
V Focus_zum_kenntnisdiagramm kind=focus lang=de gloss="zum + Dat (das Diagramm) — not zur" status=active
E Focus_zum_kenntnisdiagramm FROM_SESSION Session_zum_kenntnisdiagramm
V Lemma_de_fix_zum_kenntnisdiagramm kind=lemma lang=de surface="Ach so, okay. Kehren wir zurück zum Kenntnisdiagra" role=minimal-rewrite
E Lemma_de_fix_zum_kenntnisdiagramm FROM_SESSION Session_zum_kenntnisdiagramm SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-zum-kenntnisdiagramm.toon.md
V Form_fix_zum_kenntnisdiagramm_0_zum_kenntnisd kind=form lang=de surface="zum Kenntnisdiagramm" fixes="zur Kentnisse Diagram"
E Form_fix_zum_kenntnisdiagramm_0_zum_kenntnisd FROM_SESSION Session_zum_kenntnisdiagramm
V Form_fix_zum_kenntnisdiagramm_1_kenntnisse_ke kind=form lang=de surface="Kenntnisse / Kenntnis-" fixes=Kentnisse
E Form_fix_zum_kenntnisdiagramm_1_kenntnisse_ke FROM_SESSION Session_zum_kenntnisdiagramm
V Form_fix_zum_kenntnisdiagramm_2_diagramm kind=form lang=de surface=Diagramm fixes=Diagram
E Form_fix_zum_kenntnisdiagramm_2_diagramm FROM_SESSION Session_zum_kenntnisdiagramm

# auto-gap 2026-09-15T18:22:01Z surface=眉脽
V Concept_gap_zh_29dd4afd1d kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_29dd4afd1d kind=gap lang=zh surface=眉脽 target=de status=open
V Lemma_zh_zh_29dd4afd1d kind=lemma lang=zh surface=眉脽
E Concept_gap_zh_29dd4afd1d EXPRESSES Lemma_zh_zh_29dd4afd1d SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_29dd4afd1d GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_29dd4afd1d GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-15T18:24:32Z advanzia-pin-geldautomat-rueckmeldung lang=de
V Session_advanzia_pin_geldautomat_rueckmeldung kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-advanzia-pin-geldautomat-rueckmeldung.toon.md
V Focus_advanzia_pin_geldautomat_rueckmeldung kind=focus lang=de gloss="wenn ich sie in den Geldautomaten stecke — wenn ni" status=active
E Focus_advanzia_pin_geldautomat_rueckmeldung FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung
V Lemma_de_fix_advanzia_pin_geldautomat_rueckmeldung kind=lemma lang=de surface="Es gibt diese E-Mail. Die Bankkarte, die ich jetzt" role=minimal-rewrite
E Lemma_de_fix_advanzia_pin_geldautomat_rueckmeldung FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-advanzia-pin-geldautomat-rueckmeldung.toon.md
V Form_fix_advanzia_pin_geldautomat_rueckmeldun kind=form lang=de surface="wenn ich sie in den Geldautomaten stecke" fixes="wann ich es ins Geldautomat ei"
E Form_fix_advanzia_pin_geldautomat_rueckmeldun FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung
V Form_fix_advanzia_pin_geldautomat_rueckmeldun kind=form lang=de surface="die PIN sei zu oft falsch eingegeben wor" fixes="PIN viel mehr mals falsch gege"
E Form_fix_advanzia_pin_geldautomat_rueckmeldun FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung
V Form_fix_advanzia_pin_geldautomat_rueckmeldun kind=form lang=de surface="möchte um Lösungen bitten" fixes="bitte Lösungen zu fragen"
E Form_fix_advanzia_pin_geldautomat_rueckmeldun FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung
V Form_fix_advanzia_pin_geldautomat_rueckmeldun kind=form lang=de surface="Die E-Mail liegt in meinem Postfach" fixes="Das Email liegt in meine"
E Form_fix_advanzia_pin_geldautomat_rueckmeldun FROM_SESSION Session_advanzia_pin_geldautomat_rueckmeldung

# ingest-session 2026-09-15T18:26:46Z advanzia-todo-protokollieren lang=de
V Session_advanzia_todo_protokollieren kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-advanzia-todo-protokollieren.toon.md
V Focus_advanzia_todo_protokollieren kind=focus lang=de gloss="zur Verfolgung — zu + Artikel + Substantiv" status=active
E Focus_advanzia_todo_protokollieren FROM_SESSION Session_advanzia_todo_protokollieren
V Lemma_de_fix_advanzia_todo_protokollieren kind=lemma lang=de surface="Also gilt das als TODO und Aufgabe und als Kommuni" role=minimal-rewrite
E Lemma_de_fix_advanzia_todo_protokollieren FROM_SESSION Session_advanzia_todo_protokollieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-advanzia-todo-protokollieren.toon.md
V Form_fix_advanzia_todo_protokollieren_0_also_ kind=form lang=de surface="Also gilt das" fixes="So diese gilt"
E Form_fix_advanzia_todo_protokollieren_0_also_ FROM_SESSION Session_advanzia_todo_protokollieren
V Form_fix_advanzia_todo_protokollieren_1_kommu kind=form lang=de surface="Kommunikation zur Verfolgung" fixes="Kommunikation zu Verfolgung"
E Form_fix_advanzia_todo_protokollieren_1_kommu FROM_SESSION Session_advanzia_todo_protokollieren
V Form_fix_advanzia_todo_protokollieren_2_proto kind=form lang=de surface=protokollieren fixes=protokokieren
E Form_fix_advanzia_todo_protokollieren_2_proto FROM_SESSION Session_advanzia_todo_protokollieren
V Form_fix_advanzia_todo_protokollieren_3_aufga kind=form lang=de surface="Aufgabe und als Kommunikation" fixes="Aufgabe und Kommunikation"
E Form_fix_advanzia_todo_protokollieren_3_aufga FROM_SESSION Session_advanzia_todo_protokollieren

# ingest-session 2026-09-15T19:20:56Z email-an-advanzia-absenden lang=de
V Session_email_an_advanzia_absenden kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-email-an-advanzia-absenden.toon.md
V Focus_email_an_advanzia_absenden kind=focus lang=de gloss="die E-Mail — Femininum; an Advanzia" status=active
E Focus_email_an_advanzia_absenden FROM_SESSION Session_email_an_advanzia_absenden
V Lemma_de_fix_email_an_advanzia_absenden kind=lemma lang=de surface="Ach so, jetzt geben Sie mir die E-Mail an Advanzia" role=minimal-rewrite
E Lemma_de_fix_email_an_advanzia_absenden FROM_SESSION Session_email_an_advanzia_absenden SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-email-an-advanzia-absenden.toon.md
V Form_fix_email_an_advanzia_absenden_0_die_e_m kind=form lang=de surface="die E-Mail" fixes="den Email"
E Form_fix_email_an_advanzia_absenden_0_die_e_m FROM_SESSION Session_email_an_advanzia_absenden
V Form_fix_email_an_advanzia_absenden_1_an_adva kind=form lang=de surface="an Advanzia" fixes="zur Advanzia"
E Form_fix_email_an_advanzia_absenden_1_an_adva FROM_SESSION Session_email_an_advanzia_absenden
V Form_fix_email_an_advanzia_absenden_2_an_adva kind=form lang=de surface="an Advanzia zum Absenden" fixes="zur Advanzia abzusenden"
E Form_fix_email_an_advanzia_absenden_2_an_adva FROM_SESSION Session_email_an_advanzia_absenden

# auto-gap 2026-09-15T19:24:20Z surface=脺
V Concept_gap_zh_5abfa60b13 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_5abfa60b13 kind=gap lang=zh surface=脺 target=de status=open
V Lemma_zh_zh_5abfa60b13 kind=lemma lang=zh surface=脺
E Concept_gap_zh_5abfa60b13 EXPRESSES Lemma_zh_zh_5abfa60b13 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_5abfa60b13 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_5abfa60b13 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-15T19:24:32Z empfaenger-fuer-diese-email lang=de
V Session_empfaenger_fuer_diese_email kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-empfaenger-fuer-diese-email.toon.md
V Focus_empfaenger_fuer_diese_email kind=focus lang=de gloss="für diese E-Mail — Akkusativ, Femininum" status=active
E Focus_empfaenger_fuer_diese_email FROM_SESSION Session_empfaenger_fuer_diese_email
V Lemma_de_fix_empfaenger_fuer_diese_email kind=lemma lang=de surface="Finden Sie den Empfänger für diese E-Mail." role=minimal-rewrite
E Lemma_de_fix_empfaenger_fuer_diese_email FROM_SESSION Session_empfaenger_fuer_diese_email SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-empfaenger-fuer-diese-email.toon.md
V Form_fix_empfaenger_fuer_diese_email_0_f_r_di kind=form lang=de surface="für diese E-Mail" fixes="für dieser Email"
E Form_fix_empfaenger_fuer_diese_email_0_f_r_di FROM_SESSION Session_empfaenger_fuer_diese_email
V Form_fix_empfaenger_fuer_diese_email_1_f_r_ce kind=form lang=de surface=für fixes="dazu für"
E Form_fix_empfaenger_fuer_diese_email_1_f_r_ce FROM_SESSION Session_empfaenger_fuer_diese_email
V Form_fix_empfaenger_fuer_diese_email_2_die_e_ kind=form lang=de surface="die E-Mail" fixes="den Email"
E Form_fix_empfaenger_fuer_diese_email_2_die_e_ FROM_SESSION Session_empfaenger_fuer_diese_email

# ingest-session 2026-09-15T19:28:48Z franzoesische-uebungen-anhand lang=de
V Session_franzoesische_uebungen_anhand kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-franzoesische-uebungen-anhand.toon.md
V Focus_franzoesische_uebungen_anhand kind=focus lang=de gloss="die französischen Übungen (Plural) + anhand + Geni" status=active
E Focus_franzoesische_uebungen_anhand FROM_SESSION Session_franzoesische_uebungen_anhand
V Lemma_de_fix_franzoesische_uebungen_anhand kind=lemma lang=de surface="Und jetzt sammeln Sie die französischen Übungen fü" role=minimal-rewrite
E Lemma_de_fix_franzoesische_uebungen_anhand FROM_SESSION Session_franzoesische_uebungen_anhand SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-franzoesische-uebungen-anhand.toon.md
V Form_fix_franzoesische_uebungen_anhand_0_die_ kind=form lang=de surface="die französischen Übungen" fixes="den Französische Übungen"
E Form_fix_franzoesische_uebungen_anhand_0_die_ FROM_SESSION Session_franzoesische_uebungen_anhand
V Form_fix_franzoesische_uebungen_anhand_1_anha kind=form lang=de surface="anhand meines" fixes="anhand der meiner"
E Form_fix_franzoesische_uebungen_anhand_1_anha FROM_SESSION Session_franzoesische_uebungen_anhand
V Form_fix_franzoesische_uebungen_anhand_2_vorh kind=form lang=de surface="vorhandenen Systems" fixes="vorhande System"
E Form_fix_franzoesische_uebungen_anhand_2_vorh FROM_SESSION Session_franzoesische_uebungen_anhand

# ingest-session 2026-09-15T19:47:04Z zusammenfassung-aller-emails-latex-pdf lang=de
V Session_zusammenfassung_aller_emails_latex_pdf kind=session date=2026-09-15 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-zusammenfassung-aller-emails-latex-pdf.toon.md
V Focus_zusammenfassung_aller_emails_latex_pdf kind=focus lang=de gloss="aller meiner E-Mails — Genitiv Plural" status=active
E Focus_zusammenfassung_aller_emails_latex_pdf FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf
V Lemma_de_fix_zusammenfassung_aller_emails_latex_pdf kind=lemma lang=de surface="Okay, jetzt gib mir eine Zusammenfassung aller mei" role=minimal-rewrite
E Lemma_de_fix_zusammenfassung_aller_emails_latex_pdf FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-15-zusammenfassung-aller-emails-latex-pdf.toon.md
V Form_fix_zusammenfassung_aller_emails_latex_p kind=form lang=de surface="Zusammenfassung aller" fixes="Zusammenfassung auf aller"
E Form_fix_zusammenfassung_aller_emails_latex_p FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf
V Form_fix_zusammenfassung_aller_emails_latex_p kind=form lang=de surface=E-Mails fixes=Emails
E Form_fix_zusammenfassung_aller_emails_latex_p FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf
V Form_fix_zusammenfassung_aller_emails_latex_p kind=form lang=de surface="im LaTeX-PDF-Format" fixes="im PDF LATEX formatten"
E Form_fix_zusammenfassung_aller_emails_latex_p FROM_SESSION Session_zusammenfassung_aller_emails_latex_pdf

# auto-gap 2026-09-16T09:17:16Z surface=also
V Concept_gap_en_also kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_also kind=gap lang=en surface=also target=de status=open
V Lemma_en_en_also kind=lemma lang=en surface=also
E Concept_gap_en_also EXPRESSES Lemma_en_en_also SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_also GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_also GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-16T09:17:16Z surface=des
V Concept_gap_fr_des kind=concept gloss=unknown-expression-in-de status=open
V Gap_fr_des kind=gap lang=fr surface=des target=de status=open
V Lemma_fr_fr_des kind=lemma lang=fr surface=des
E Concept_gap_fr_des EXPRESSES Lemma_fr_fr_des SOURCE=hook/beforeSubmitPrompt
E Lemma_fr_fr_des GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_fr_des GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-16T09:17:48Z wie-macht-man-dann-3d-szene lang=de
V Session_wie_macht_man_dann_3d_szene kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-wie-macht-man-dann-3d-szene.toon.md
V Focus_wie_macht_man_dann_3d_szene kind=focus lang=de gloss="Wie macht man dann + Akkusativ — sequential follow" status=active
E Focus_wie_macht_man_dann_3d_szene FROM_SESSION Session_wie_macht_man_dann_3d_szene
V Lemma_de_fix_wie_macht_man_dann_3d_szene kind=lemma lang=de surface="Ja, das ist METAMORPHOSIS von INTERWORLD. Wie mach" role=minimal-rewrite
E Lemma_de_fix_wie_macht_man_dann_3d_szene FROM_SESSION Session_wie_macht_man_dann_3d_szene SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-wie-macht-man-dann-3d-szene.toon.md
V Form_fix_wie_macht_man_dann_3d_szene_0_das_is kind=form lang=de surface="das ist … von …" fixes="就是 + EN title"
E Form_fix_wie_macht_man_dann_3d_szene_0_das_is FROM_SESSION Session_wie_macht_man_dann_3d_szene
V Form_fix_wie_macht_man_dann_3d_szene_1_wie_ma kind=form lang=de surface="Wie macht man dann …?" fixes=那么…怎么做的呢
E Form_fix_wie_macht_man_dann_3d_szene_1_wie_ma FROM_SESSION Session_wie_macht_man_dann_3d_szene
V Form_fix_wie_macht_man_dann_3d_szene_2_die_3_ kind=form lang=de surface="die 3-D-Szene" fixes=3d场景
E Form_fix_wie_macht_man_dann_3d_szene_2_die_3_ FROM_SESSION Session_wie_macht_man_dann_3d_szene

# ingest-session 2026-09-16T09:26:40Z versuch-das-dann-mal-in-tmp lang=de
V Session_versuch_das_dann_mal_in_tmp kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-versuch-das-dann-mal-in-tmp.toon.md
V Focus_versuch_das_dann_mal_in_tmp kind=focus lang=de gloss="Imperativ + mal — softened command, not 给我…做一下 as " status=active
E Focus_versuch_das_dann_mal_in_tmp FROM_SESSION Session_versuch_das_dann_mal_in_tmp
V Lemma_de_fix_versuch_das_dann_mal_in_tmp kind=lemma lang=de surface="Versuch das dann mal in tmp." role=minimal-rewrite
E Lemma_de_fix_versuch_das_dann_mal_in_tmp FROM_SESSION Session_versuch_das_dann_mal_in_tmp SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-versuch-das-dann-mal-in-tmp.toon.md
V Form_fix_versuch_das_dann_mal_in_tmp_0_versuc kind=form lang=de surface="Versuch das mal" fixes=给我…做一下
E Form_fix_versuch_das_dann_mal_in_tmp_0_versuc FROM_SESSION Session_versuch_das_dann_mal_in_tmp
V Form_fix_versuch_das_dann_mal_in_tmp_1_das_ei kind=form lang=de surface="das / einen Versuch" fixes=一个试试
E Form_fix_versuch_das_dann_mal_in_tmp_1_das_ei FROM_SESSION Session_versuch_das_dann_mal_in_tmp
V Form_fix_versuch_das_dann_mal_in_tmp_2_dann_m kind=form lang=de surface="dann marks the next step after the pipel" fixes="那么-chain leftover"
E Form_fix_versuch_das_dann_mal_in_tmp_2_dann_m FROM_SESSION Session_versuch_das_dann_mal_in_tmp

# ingest-session 2026-09-16T09:27:13Z kenntnisse-der-astrophysik-graph lang=de
V Session_kenntnisse_der_astrophysik_graph kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-kenntnisse-der-astrophysik-graph.toon.md
V Focus_kenntnisse_der_astrophysik_graph kind=focus lang=de gloss="der Astrophysik — Femininum, Genitiv" status=active
E Focus_kenntnisse_der_astrophysik_graph FROM_SESSION Session_kenntnisse_der_astrophysik_graph
V Lemma_de_fix_kenntnisse_der_astrophysik_graph kind=lemma lang=de surface="Ach so, also gut: Ich habe vor, Kenntnisse der Ast" role=minimal-rewrite
E Lemma_de_fix_kenntnisse_der_astrophysik_graph FROM_SESSION Session_kenntnisse_der_astrophysik_graph SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-kenntnisse-der-astrophysik-graph.toon.md
V Form_fix_kenntnisse_der_astrophysik_graph_0_d kind=form lang=de surface="der Astrophysik" fixes="des Astrophysiks"
E Form_fix_kenntnisse_der_astrophysik_graph_0_d FROM_SESSION Session_kenntnisse_der_astrophysik_graph
V Form_fix_kenntnisse_der_astrophysik_graph_1_z kind=form lang=de surface="zum Kenntnisgraphen" fixes="zur Kenntnisse-Graph"
E Form_fix_kenntnisse_der_astrophysik_graph_1_z FROM_SESSION Session_kenntnisse_der_astrophysik_graph
V Form_fix_kenntnisse_der_astrophysik_graph_2_a kind=form lang=de surface=Astrophysik fixes=Astrophysiks
E Form_fix_kenntnisse_der_astrophysik_graph_2_a FROM_SESSION Session_kenntnisse_der_astrophysik_graph

# ingest-session 2026-09-16T09:35:05Z dann-ist-xiaoxin-also-nur-reupload lang=de
V Session_dann_ist_xiaoxin_also_nur_reupload kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-dann-ist-xiaoxin-also-nur-reupload.toon.md
V Focus_dann_ist_xiaoxin_also_nur_reupload kind=focus lang=de gloss="Dann ist … also — one German conclusion, not 然后所以 " status=active
E Focus_dann_ist_xiaoxin_also_nur_reupload FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload
V Lemma_de_fix_dann_ist_xiaoxin_also_nur_reupload kind=lemma lang=de surface="Dann ist 小新宇宙 also nur ein Re-Upload. Nimm dieses " role=minimal-rewrite
E Lemma_de_fix_dann_ist_xiaoxin_also_nur_reupload FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-dann-ist-xiaoxin-also-nur-reupload.toon.md
V Form_fix_dann_ist_xiaoxin_also_nur_reupload_0 kind=form lang=de surface="Dann … also" fixes="然后所以 stacked"
E Form_fix_dann_ist_xiaoxin_also_nur_reupload_0 FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload
V Form_fix_dann_ist_xiaoxin_also_nur_reupload_1 kind=form lang=de surface="nur ein Re-Upload / wessen Arbeit" fixes=搬运人家的
E Form_fix_dann_ist_xiaoxin_also_nur_reupload_1 FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload
V Form_fix_dann_ist_xiaoxin_also_nur_reupload_2 kind=form lang=de surface="Nimm dieses BGM und sag" fixes=用这个BGM然后说
E Form_fix_dann_ist_xiaoxin_also_nur_reupload_2 FROM_SESSION Session_dann_ist_xiaoxin_also_nur_reupload

# ingest-session 2026-09-16T18:05:56Z um-die-reaktionsfaehigkeit-zu-testen lang=de
V Session_um_die_reaktionsfaehigkeit_zu_testen kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-um-die-reaktionsfaehigkeit-zu-testen.toon.md
V Focus_um_die_reaktionsfaehigkeit_zu_testen kind=focus lang=de gloss="um_zu_infinitiv — purpose clause after the fake te" status=active
E Focus_um_die_reaktionsfaehigkeit_zu_testen FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen
V Lemma_de_fix_um_die_reaktionsfaehigkeit_zu_testen kind=lemma lang=de surface="Mach ein Video: erst eine Farbe, dann wechselt sie" role=minimal-rewrite
E Lemma_de_fix_um_die_reaktionsfaehigkeit_zu_testen FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-um-die-reaktionsfaehigkeit-zu-testen.toon.md
V Form_fix_um_die_reaktionsfaehigkeit_zu_testen kind=form lang=de surface="um die Reaktionsfähigkeit zu testen" fixes=就可以测试反应能力
E Form_fix_um_die_reaktionsfaehigkeit_zu_testen FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen
V Form_fix_um_die_reaktionsfaehigkeit_zu_testen kind=form lang=de surface="Mach ein Video" fixes=搞一个视频
E Form_fix_um_die_reaktionsfaehigkeit_zu_testen FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen
V Form_fix_um_die_reaktionsfaehigkeit_zu_testen kind=form lang=de surface="Du wurdest reingelegt" fixes=你被骗了
E Form_fix_um_die_reaktionsfaehigkeit_zu_testen FROM_SESSION Session_um_die_reaktionsfaehigkeit_zu_testen

# ingest-session 2026-09-16T19:02:46Z sobald-es-rot-wird-laeuft-die-zeit lang=de
V Session_sobald_es_rot_wird_laeuft_die_zeit kind=session date=2026-09-16 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-sobald-es-rot-wird-laeuft-die-zeit.toon.md
V Focus_sobald_es_rot_wird_laeuft_die_zeit kind=focus lang=de gloss="sobald + Präsens — time clause for the instant the" status=active
E Focus_sobald_es_rot_wird_laeuft_die_zeit FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit
V Lemma_de_fix_sobald_es_rot_wird_laeuft_die_zeit kind=lemma lang=de surface="Direkt nach dem Rickroll kommt nur dieses rote Seg" role=minimal-rewrite
E Lemma_de_fix_sobald_es_rot_wird_laeuft_die_zeit FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-16-sobald-es-rot-wird-laeuft-die-zeit.toon.md
V Form_fix_sobald_es_rot_wird_laeuft_die_zeit_0 kind=form lang=de surface="sobald es rot wird, läuft die Zeit" fixes=变红开始计时
E Form_fix_sobald_es_rot_wird_laeuft_die_zeit_0 FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit
V Form_fix_sobald_es_rot_wird_laeuft_die_zeit_1 kind=form lang=de surface="ab 0,001 Sekunden / läuft … hoch" fixes=0.001秒开始往上涨
E Form_fix_sobald_es_rot_wird_laeuft_die_zeit_1 FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit
V Form_fix_sobald_es_rot_wird_laeuft_die_zeit_2 kind=form lang=de surface="nur dieses rote Segment" fixes=只要变红的这个分段
E Form_fix_sobald_es_rot_wird_laeuft_die_zeit_2 FROM_SESSION Session_sobald_es_rot_wird_laeuft_die_zeit

# ingest-session 2026-09-17T18:13:53Z workout-planung-oktoberfest lang=de
V Session_workout_planung_oktoberfest kind=session date=2026-09-17 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-17-workout-planung-oktoberfest.toon.md
V Focus_workout_planung_oktoberfest kind=focus lang=de gloss="eine Workout-Planung (Akk. f.)" status=active
E Focus_workout_planung_oktoberfest FROM_SESSION Session_workout_planung_oktoberfest
V Lemma_de_fix_workout_planung_oktoberfest kind=lemma lang=de surface="So, heute ist der 17.9. Glaube ich, dass man eine " role=minimal-rewrite
E Lemma_de_fix_workout_planung_oktoberfest FROM_SESSION Session_workout_planung_oktoberfest SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-17-workout-planung-oktoberfest.toon.md
V Form_fix_workout_planung_oktoberfest_0_glaube kind=form lang=de surface="Glaube ich, dass" fixes="glauch ich darauf"
E Form_fix_workout_planung_oktoberfest_0_glaube FROM_SESSION Session_workout_planung_oktoberfest
V Form_fix_workout_planung_oktoberfest_1_eine_w kind=form lang=de surface="eine Workout-Planung" fixes=Workoutsplannung
E Form_fix_workout_planung_oktoberfest_1_eine_w FROM_SESSION Session_workout_planung_oktoberfest
V Form_fix_workout_planung_oktoberfest_2_kannst kind=form lang=de surface="kannst du es augenblicklich machen" fixes="kannst du augenblick es machen"
E Form_fix_workout_planung_oktoberfest_2_kannst FROM_SESSION Session_workout_planung_oktoberfest
V Form_fix_workout_planung_oktoberfest_3_an_die kind=form lang=de surface="an diesem Tag" fixes="bei diesem tag"
E Form_fix_workout_planung_oktoberfest_3_an_die FROM_SESSION Session_workout_planung_oktoberfest
V Form_fix_workout_planung_oktoberfest_4_oder_s kind=form lang=de surface="oder so etwas Ähnliches" fixes="oder gleiche Solche"
E Form_fix_workout_planung_oktoberfest_4_oder_s FROM_SESSION Session_workout_planung_oktoberfest

# ingest-session 2026-09-17T22:13:42Z starte-die-shenyou lang=de
V Session_starte_die_shenyou kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-starte-die-shenyou.toon.md
V Focus_starte_die_shenyou kind=focus lang=de gloss="Starte + Akk. (du-Imperativ)" status=active
E Focus_starte_die_shenyou FROM_SESSION Session_starte_die_shenyou
V Lemma_de_fix_starte_die_shenyou kind=lemma lang=de surface="Starte die 神游." role=minimal-rewrite
E Lemma_de_fix_starte_die_shenyou FROM_SESSION Session_starte_die_shenyou SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-starte-die-shenyou.toon.md
V Form_fix_starte_die_shenyou_0_starte_die_6a5e kind=form lang=de surface="Starte die 神游." fixes=開始神游
E Form_fix_starte_die_shenyou_0_starte_die_6a5e FROM_SESSION Session_starte_die_shenyou

# ingest-session 2026-09-18T10:22:39Z tagesuebersicht-3d-html lang=de
V Session_tagesuebersicht_3d_html kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tagesuebersicht-3d-html.toon.md
V Focus_tagesuebersicht_3d_html kind=focus lang=de gloss="Kannst du mir eine HTML-Übersicht zeigen? (mir = D" status=active
E Focus_tagesuebersicht_3d_html FROM_SESSION Session_tagesuebersicht_3d_html
V Lemma_de_fix_tagesuebersicht_3d_html kind=lemma lang=de surface="Starte heute meinen Tag. Heute ist der 18. Septemb" role=minimal-rewrite
E Lemma_de_fix_tagesuebersicht_3d_html FROM_SESSION Session_tagesuebersicht_3d_html SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tagesuebersicht-3d-html.toon.md
V Form_fix_tagesuebersicht_3d_html_0_mir_eine_h kind=form lang=de surface="mir eine HTML-Übersicht" fixes="zur mir"
E Form_fix_tagesuebersicht_3d_html_0_mir_eine_h FROM_SESSION Session_tagesuebersicht_3d_html

# ingest-session 2026-09-18T10:55:28Z nginx-link-3d-halle lang=de
V Session_nginx_link_3d_halle kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-nginx-link-3d-halle.toon.md
V Focus_nginx_link_3d_halle kind=focus lang=de gloss="Gib mir bitte den Nginx-Link. (mir = Dativ)" status=active
E Focus_nginx_link_3d_halle FROM_SESSION Session_nginx_link_3d_halle
V Lemma_de_fix_nginx_link_3d_halle kind=lemma lang=de surface="Ach so, ich bin jetzt mobil. Gib mir bitte den Ngi" role=minimal-rewrite
E Lemma_de_fix_nginx_link_3d_halle FROM_SESSION Session_nginx_link_3d_halle SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-nginx-link-3d-halle.toon.md
V Form_fix_nginx_link_3d_halle_0_mobil_ngnix_li kind=form lang=de surface="mobil; ngnix Linke → den Nginx-Link" fixes="bei der Mobile"
E Form_fix_nginx_link_3d_halle_0_mobil_ngnix_li FROM_SESSION Session_nginx_link_3d_halle

# ingest-session 2026-09-18T10:57:38Z cli-befehl-3d-halle lang=de
V Session_cli_befehl_3d_halle kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-cli-befehl-3d-halle.toon.md
V Focus_cli_befehl_3d_halle kind=focus lang=de gloss="Kannst du den CLI-Befehl ausführen? (Akkusativ)" status=active
E Focus_cli_befehl_3d_halle FROM_SESSION Session_cli_befehl_3d_halle
V Lemma_de_fix_cli_befehl_3d_halle kind=lemma lang=de surface="Warum? Kannst du einfach den CLI-Befehl ausführen?" role=minimal-rewrite
E Lemma_de_fix_cli_befehl_3d_halle FROM_SESSION Session_cli_befehl_3d_halle SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-cli-befehl-3d-halle.toon.md
V Form_fix_cli_befehl_3d_halle_0_den_cli_befehl kind=form lang=de surface="den CLI-Befehl ausführen" fixes="cli Befehl durchführen"
E Form_fix_cli_befehl_3d_halle_0_den_cli_befehl FROM_SESSION Session_cli_befehl_3d_halle

# ingest-session 2026-09-18T10:59:13Z oeffentlicher-ngrok-link lang=de
V Session_oeffentlicher_ngrok_link kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-oeffentlicher-ngrok-link.toon.md
V Focus_oeffentlicher_ngrok_link kind=focus lang=de gloss="Gib mir bitte einen öffentlichen ngrok-Link. (eine" status=active
E Focus_oeffentlicher_ngrok_link FROM_SESSION Session_oeffentlicher_ngrok_link
V Lemma_de_fix_oeffentlicher_ngrok_link kind=lemma lang=de surface="Nein, ich bin mit dem Handy unterwegs. Gib mir bit" role=minimal-rewrite
E Lemma_de_fix_oeffentlicher_ngrok_link FROM_SESSION Session_oeffentlicher_ngrok_link SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-oeffentlicher-ngrok-link.toon.md
V Form_fix_oeffentlicher_ngrok_link_0_mit_dem_h kind=form lang=de surface="mit dem Handy unterwegs; öffentliche Lin" fixes="bei des Handys draußen"
E Form_fix_oeffentlicher_ngrok_link_0_mit_dem_h FROM_SESSION Session_oeffentlicher_ngrok_link

# ingest-session 2026-09-18T11:04:27Z mobil-3d-halle-optimieren lang=de
V Session_mobil_3d_halle_optimieren kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-mobil-3d-halle-optimieren.toon.md
V Focus_mobil_3d_halle_optimieren kind=focus lang=de gloss="diese 3D-Hallen-Seite (Akkusativ, feminin)" status=active
E Focus_mobil_3d_halle_optimieren FROM_SESSION Session_mobil_3d_halle_optimieren
V Lemma_de_fix_mobil_3d_halle_optimieren kind=lemma lang=de surface="Ach so, bitte optimieren Sie diese 3D-Hallen-Seite" role=minimal-rewrite
E Lemma_de_fix_mobil_3d_halle_optimieren FROM_SESSION Session_mobil_3d_halle_optimieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-mobil-3d-halle-optimieren.toon.md
V Form_fix_mobil_3d_halle_optimieren_0_diese_3d kind=form lang=de surface="diese 3D-Hallen-Seite auch für das Handy" fixes="für den Handy, diesen 3D hall "
E Form_fix_mobil_3d_halle_optimieren_0_diese_3d FROM_SESSION Session_mobil_3d_halle_optimieren

# ingest-session 2026-09-18T11:21:14Z hud-3d-szene lang=de
V Session_hud_3d_szene kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-hud-3d-szene.toon.md
V Focus_hud_3d_szene kind=focus lang=de gloss="Nimm das in .private auf (in + Akk)" status=active
E Focus_hud_3d_szene FROM_SESSION Session_hud_3d_szene
V Lemma_de_fix_hud_3d_szene kind=lemma lang=de surface="Ich kann nur das HUD sehen. Die 3D-Szene kann ich " role=minimal-rewrite
E Lemma_de_fix_hud_3d_szene FROM_SESSION Session_hud_3d_szene SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-hud-3d-szene.toon.md
V Form_fix_hud_3d_szene_0_die_3d_szene kind=form lang=de surface="Die 3D-Szene" fixes="Den 3d Szene"
E Form_fix_hud_3d_szene_0_die_3d_szene FROM_SESSION Session_hud_3d_szene

# ingest-session 2026-09-18T11:30:09Z tageszusammenfassung lang=de
V Session_tageszusammenfassung kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tageszusammenfassung.toon.md
V Focus_tageszusammenfassung kind=focus lang=de gloss="Geben Sie mir jetzt eine Zusammenfassung für heute" status=active
E Focus_tageszusammenfassung FROM_SESSION Session_tageszusammenfassung
V Lemma_de_fix_tageszusammenfassung kind=lemma lang=de surface="Also gut, vergessen Sie die 3D-Szene. Geben Sie mi" role=minimal-rewrite
E Lemma_de_fix_tageszusammenfassung FROM_SESSION Session_tageszusammenfassung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tageszusammenfassung.toon.md
V Form_fix_tageszusammenfassung_0_die_3d_szene_ kind=form lang=de surface="die 3D-Szene / Geben Sie mir eine Zusamm" fixes="den 3D szene / Gib mir Zusamme"
E Form_fix_tageszusammenfassung_0_die_3d_szene_ FROM_SESSION Session_tageszusammenfassung

# ingest-session 2026-09-18T11:33:34Z todo-zeitplan lang=de
V Session_todo_zeitplan kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-todo-zeitplan.toon.md
V Focus_todo_zeitplan kind=focus lang=de gloss="einschließlich des Zeitplans (Genitiv nach einschl" status=active
E Focus_todo_zeitplan FROM_SESSION Session_todo_zeitplan
V Lemma_de_fix_todo_zeitplan kind=lemma lang=de surface="Nein, ich möchte eine TODO-Liste für heute, einsch" role=minimal-rewrite
E Lemma_de_fix_todo_zeitplan FROM_SESSION Session_todo_zeitplan SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-todo-zeitplan.toon.md
V Form_fix_todo_zeitplan_0_einschlie_lich_des_z kind=form lang=de surface="einschließlich des Zeitplans" fixes="inkl. Schedule usw"
E Form_fix_todo_zeitplan_0_einschlie_lich_des_z FROM_SESSION Session_todo_zeitplan

# ingest-session 2026-09-18T13:28:20Z oktoberfest-unterwegs lang=de
V Session_oktoberfest_unterwegs kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-oktoberfest-unterwegs.toon.md
V Focus_oktoberfest_unterwegs kind=focus lang=de gloss="unter Brainfog leide ich nicht mehr (leiden + unte" status=active
E Focus_oktoberfest_unterwegs FROM_SESSION Session_oktoberfest_unterwegs
V Lemma_de_fix_oktoberfest_unterwegs kind=lemma lang=de surface="Genau, ich bin jetzt auf dem Weg zum Oktoberfest, " role=minimal-rewrite
E Lemma_de_fix_oktoberfest_unterwegs FROM_SESSION Session_oktoberfest_unterwegs SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-oktoberfest-unterwegs.toon.md
V Form_fix_oktoberfest_unterwegs_0_zum_oktoberf kind=form lang=de surface="zum Oktoberfest" fixes="zur Oktoberfest"
E Form_fix_oktoberfest_unterwegs_0_zum_oktoberf FROM_SESSION Session_oktoberfest_unterwegs
V Form_fix_oktoberfest_unterwegs_1_unter_brainf kind=form lang=de surface="unter Brainfog leide ich nicht mehr" fixes="Brain fog leide ich nicht mehr"
E Form_fix_oktoberfest_unterwegs_1_unter_brainf FROM_SESSION Session_oktoberfest_unterwegs
V Form_fix_oktoberfest_unterwegs_2_ich_bin_drau kind=form lang=de surface="Ich bin draußen." fixes="Bin ich draußen"
E Form_fix_oktoberfest_unterwegs_2_ich_bin_drau FROM_SESSION Session_oktoberfest_unterwegs

# ingest-session 2026-09-18T13:30:36Z recovery-zusammenfassung lang=de
V Session_recovery_zusammenfassung kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-recovery-zusammenfassung.toon.md
V Focus_recovery_zusammenfassung kind=focus lang=de gloss="eine Zusammenfassung über + Akk. (nicht 'auf')" status=active
E Focus_recovery_zusammenfassung FROM_SESSION Session_recovery_zusammenfassung
V Lemma_de_fix_recovery_zusammenfassung kind=lemma lang=de surface="So, gib mir bitte eine Zusammenfassung über meine " role=minimal-rewrite
E Lemma_de_fix_recovery_zusammenfassung FROM_SESSION Session_recovery_zusammenfassung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-recovery-zusammenfassung.toon.md
V Form_fix_recovery_zusammenfassung_0_ber_meine kind=form lang=de surface="über meine Wiederholungsfähigkeit" fixes="auf meine Wiederholungen Fähig"
E Form_fix_recovery_zusammenfassung_0_ber_meine FROM_SESSION Session_recovery_zusammenfassung
V Form_fix_recovery_zusammenfassung_1_ber_mein_ kind=form lang=de surface="über mein Leiden" fixes="auf meiner Leiden"
E Form_fix_recovery_zusammenfassung_1_ber_mein_ FROM_SESSION Session_recovery_zusammenfassung
V Form_fix_recovery_zusammenfassung_2_gib kind=form lang=de surface=gib fixes=Gib
E Form_fix_recovery_zusammenfassung_2_gib FROM_SESSION Session_recovery_zusammenfassung

# ingest-session 2026-09-18T13:41:16Z luftmatratze-uebungsplan lang=de
V Session_luftmatratze_uebungsplan kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-luftmatratze-uebungsplan.toon.md
V Focus_luftmatratze_uebungsplan kind=focus lang=de gloss="Ich lege mich auf die Luftmatratze. (sich legen + " status=active
E Focus_luftmatratze_uebungsplan FROM_SESSION Session_luftmatratze_uebungsplan
V Lemma_de_fix_luftmatratze_uebungsplan kind=lemma lang=de surface="So, gib mir einen harten Übungsplan für Kenntnisse" role=minimal-rewrite
E Lemma_de_fix_luftmatratze_uebungsplan FROM_SESSION Session_luftmatratze_uebungsplan SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-luftmatratze-uebungsplan.toon.md
V Form_fix_luftmatratze_uebungsplan_0_einen_har kind=form lang=de surface="einen harten Übungsplan" fixes="eine hartes Kenntnisse Übungen"
E Form_fix_luftmatratze_uebungsplan_0_einen_har FROM_SESSION Session_luftmatratze_uebungsplan
V Form_fix_luftmatratze_uebungsplan_1_den_ich_m kind=form lang=de surface="den ich machen kann" fixes="die Ich machen kann"
E Form_fix_luftmatratze_uebungsplan_1_den_ich_m FROM_SESSION Session_luftmatratze_uebungsplan
V Form_fix_luftmatratze_uebungsplan_2_w_hrend_d kind=form lang=de surface="während des Oktoberfests" fixes="während der Oktoberfest"
E Form_fix_luftmatratze_uebungsplan_2_w_hrend_d FROM_SESSION Session_luftmatratze_uebungsplan
V Form_fix_luftmatratze_uebungsplan_3_ich_lege_ kind=form lang=de surface="Ich lege mich auf die Luftmatratze" fixes="Ich lege sich auf dem Luftmatr"
E Form_fix_luftmatratze_uebungsplan_3_ich_lege_ FROM_SESSION Session_luftmatratze_uebungsplan
V Form_fix_luftmatratze_uebungsplan_4_umfassend kind=form lang=de surface=umfassend fixes=comprehensive
E Form_fix_luftmatratze_uebungsplan_4_umfassend FROM_SESSION Session_luftmatratze_uebungsplan

# ingest-session 2026-09-18T13:44:55Z schreibuebungen-bite-sized lang=de
V Session_schreibuebungen_bite_sized kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-schreibuebungen-bite-sized.toon.md
V Focus_schreibuebungen_bite_sized kind=focus lang=de gloss="Komposita schreibt man zusammen — Schreibübungen, " status=active
E Focus_schreibuebungen_bite_sized FROM_SESSION Session_schreibuebungen_bite_sized
V Lemma_de_fix_schreibuebungen_bite_sized kind=lemma lang=de surface="Alles auf meinem Handy, ja? Und ich brauche auch S" role=minimal-rewrite
E Lemma_de_fix_schreibuebungen_bite_sized FROM_SESSION Session_schreibuebungen_bite_sized SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-schreibuebungen-bite-sized.toon.md
V Form_fix_schreibuebungen_bite_sized_0_alles_a kind=form lang=de surface="Alles auf meinem Handy" fixes="Alle auf meinem Handy"
E Form_fix_schreibuebungen_bite_sized_0_alles_a FROM_SESSION Session_schreibuebungen_bite_sized
V Form_fix_schreibuebungen_bite_sized_1_schreib kind=form lang=de surface="Schreibübungen für B2" fixes="Schreiben Übungen B2"
E Form_fix_schreibuebungen_bite_sized_1_schreib FROM_SESSION Session_schreibuebungen_bite_sized
V Form_fix_schreibuebungen_bite_sized_2_anstatt kind=form lang=de surface="anstatt der langweiligen Aufgaben" fixes="anstatt der langweilige Aufgab"
E Form_fix_schreibuebungen_bite_sized_2_anstatt FROM_SESSION Session_schreibuebungen_bite_sized

# ingest-session 2026-09-18T15:46:45Z beziehungen-private-bereich lang=de
V Session_beziehungen_private_bereich kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-beziehungen-private-bereich.toon.md
V Focus_beziehungen_private_bereich kind=focus lang=de gloss="Nach Artikel/Possessiv trägt das Adjektiv -en — zu" status=active
E Focus_beziehungen_private_bereich FROM_SESSION Session_beziehungen_private_bereich
V Lemma_de_fix_beziehungen_private_bereich kind=lemma lang=de surface="Ach so, ich hätte gern, dass meine Beziehungen zum" role=minimal-rewrite
E Lemma_de_fix_beziehungen_private_bereich FROM_SESSION Session_beziehungen_private_bereich SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-beziehungen-private-bereich.toon.md
V Form_fix_beziehungen_private_bereich_0_zum_pr kind=form lang=de surface="zum privaten Bereich" fixes="zur private Bereich"
E Form_fix_beziehungen_private_bereich_0_zum_pr FROM_SESSION Session_beziehungen_private_bereich
V Form_fix_beziehungen_private_bereich_1_m_chte kind=form lang=de surface="möchte … hinzufügen" fixes="hätte gern … hinzufügen"
E Form_fix_beziehungen_private_bereich_1_m_chte FROM_SESSION Session_beziehungen_private_bereich
V Form_fix_beziehungen_private_bereich_2_mein_k kind=form lang=de surface="mein Known Associate" fixes="meine Known Associate"
E Form_fix_beziehungen_private_bereich_2_mein_k FROM_SESSION Session_beziehungen_private_bereich
V Form_fix_beziehungen_private_bereich_3_mit_po kind=form lang=de surface="mit potenziellen weiteren geschäftlichen" fixes="mit potenziellen weitere gesch"
E Form_fix_beziehungen_private_bereich_3_mit_po FROM_SESSION Session_beziehungen_private_bereich

# auto-gap 2026-09-18T15:51:59Z surface=全局感
V Concept_gap_zh_78062ff4c6 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_78062ff4c6 kind=gap lang=zh surface=全局感 target=de status=open
V Lemma_zh_zh_78062ff4c6 kind=lemma lang=zh surface=全局感
E Concept_gap_zh_78062ff4c6 EXPRESSES Lemma_zh_zh_78062ff4c6 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_78062ff4c6 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_78062ff4c6 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-18T15:52:43Z ganzheitlicher-uebungsueberblick lang=de
V Session_ganzheitlicher_uebungsueberblick kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-ganzheitlicher-uebungsueberblick.toon.md
V Focus_ganzheitlicher_uebungsueberblick kind=focus lang=de gloss="Ich liege — das Verb folgt dem Subjekt: ich liege," status=active
E Focus_ganzheitlicher_uebungsueberblick FROM_SESSION Session_ganzheitlicher_uebungsueberblick
V Lemma_de_fix_ganzheitlicher_uebungsueberblick kind=lemma lang=de surface="Ach so, ich liege jetzt auf der Luftmatratze. Gib " role=minimal-rewrite
E Lemma_de_fix_ganzheitlicher_uebungsueberblick FROM_SESSION Session_ganzheitlicher_uebungsueberblick SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-ganzheitlicher-uebungsueberblick.toon.md
V Form_fix_ganzheitlicher_uebungsueberblick_0_i kind=form lang=de surface="Ich liege jetzt" fixes="Ich liegt jetzt"
E Form_fix_ganzheitlicher_uebungsueberblick_0_i FROM_SESSION Session_ganzheitlicher_uebungsueberblick
V Form_fix_ganzheitlicher_uebungsueberblick_1_g kind=form lang=de surface="Gib mir" fixes="Geben Sie mir"
E Form_fix_ganzheitlicher_uebungsueberblick_1_g FROM_SESSION Session_ganzheitlicher_uebungsueberblick
V Form_fix_ganzheitlicher_uebungsueberblick_2_e kind=form lang=de surface="einen ganzheitlichen Übungsüberblick" fixes="全局感haltiges Übungen Überblick"
E Form_fix_ganzheitlicher_uebungsueberblick_2_e FROM_SESSION Session_ganzheitlicher_uebungsueberblick

# ingest-session 2026-09-18T16:02:46Z odyssee-start lang=de
V Session_odyssee_start kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-odyssee-start.toon.md
V Focus_odyssee_start kind=focus lang=de gloss="trennbares anfangen — „Fangen wir mit der Odyssey " status=active
E Focus_odyssee_start FROM_SESSION Session_odyssee_start
V Lemma_de_fix_odyssee_start kind=lemma lang=de surface="Genau, fangen wir mit der Odyssey an." role=minimal-rewrite
E Lemma_de_fix_odyssee_start FROM_SESSION Session_odyssee_start SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-odyssee-start.toon.md
V Form_fix_odyssee_start_0_mit_der_odyssey kind=form lang=de surface="mit der Odyssey" fixes="mit den Odyssey"
E Form_fix_odyssee_start_0_mit_der_odyssey FROM_SESSION Session_odyssee_start
V Form_fix_odyssee_start_1_fangen_wir_mit_der_o kind=form lang=de surface="Fangen wir mit der Odyssey an" fixes="fangen wir an mit der Odyssey"
E Form_fix_odyssee_start_1_fangen_wir_mit_der_o FROM_SESSION Session_odyssee_start

# ingest-session 2026-09-18T16:06:10Z was-soll-ich-jetzt-machen lang=de
V Session_was_soll_ich_jetzt_machen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-was-soll-ich-jetzt-machen.toon.md
V Focus_was_soll_ich_jetzt_machen kind=focus lang=de gloss="W-Frage-Klammer — Hilfsverb auf Position 2, Infini" status=active
E Focus_was_soll_ich_jetzt_machen FROM_SESSION Session_was_soll_ich_jetzt_machen
V Lemma_de_fix_was_soll_ich_jetzt_machen kind=lemma lang=de surface="Was soll ich jetzt eigentlich machen?" role=minimal-rewrite
E Lemma_de_fix_was_soll_ich_jetzt_machen FROM_SESSION Session_was_soll_ich_jetzt_machen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-was-soll-ich-jetzt-machen.toon.md
V Form_fix_was_soll_ich_jetzt_machen_0_jetzt_ei kind=form lang=de surface="jetzt eigentlich … machen" fixes="machen jetzt"
E Form_fix_was_soll_ich_jetzt_machen_0_jetzt_ei FROM_SESSION Session_was_soll_ich_jetzt_machen
V Form_fix_was_soll_ich_jetzt_machen_1_eigentli kind=form lang=de surface=eigentlich fixes=einglich
E Form_fix_was_soll_ich_jetzt_machen_1_eigentli FROM_SESSION Session_was_soll_ich_jetzt_machen

# ingest-session 2026-09-18T16:11:49Z konnektor-fusion-runde-1 lang=de
V Session_konnektor_fusion_runde_1 kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-konnektor-fusion-runde-1.toon.md
V Focus_konnektor_fusion_runde_1 kind=focus lang=de gloss="deshalb leitet die Folge ein — Die Aufgaben sind k" status=active
E Focus_konnektor_fusion_runde_1 FROM_SESSION Session_konnektor_fusion_runde_1
V Lemma_de_fix_konnektor_fusion_runde_1 kind=lemma lang=de surface="a) Ich liege auf der Luftmatratze. Ich mache Schre" role=minimal-rewrite
E Lemma_de_fix_konnektor_fusion_runde_1 FROM_SESSION Session_konnektor_fusion_runde_1 SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-konnektor-fusion-runde-1.toon.md
V Form_fix_konnektor_fusion_runde_1_0_schreib_b kind=form lang=de surface=Schreibübungen fixes="Schrei Übungen"
E Form_fix_konnektor_fusion_runde_1_0_schreib_b FROM_SESSION Session_konnektor_fusion_runde_1
V Form_fix_konnektor_fusion_runde_1_1_obwohl_es kind=form lang=de surface="obwohl es so viele Insekten gibt" fixes="obwohl es so viel Insekten gib"
E Form_fix_konnektor_fusion_runde_1_1_obwohl_es FROM_SESSION Session_konnektor_fusion_runde_1
V Form_fix_konnektor_fusion_runde_1_2_deshalb_b kind=form lang=de surface="deshalb bleibe ich dran" fixes="deshalb verbessert meine Deuts"
E Form_fix_konnektor_fusion_runde_1_2_deshalb_b FROM_SESSION Session_konnektor_fusion_runde_1

# ingest-session 2026-09-18T16:22:31Z agentcore-probe-stimme lang=de
V Session_agentcore_probe_stimme kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-agentcore-probe-stimme.toon.md
V Focus_agentcore_probe_stimme kind=focus lang=de gloss="Numerus muss durchhalten — die ganze Lösung, diese" status=active
E Focus_agentcore_probe_stimme FROM_SESSION Session_agentcore_probe_stimme
V Lemma_de_fix_agentcore_probe_stimme kind=lemma lang=de surface="So, nach meinem Gedächtnis habe ich keine Erfahrun" role=minimal-rewrite
E Lemma_de_fix_agentcore_probe_stimme FROM_SESSION Session_agentcore_probe_stimme SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-agentcore-probe-stimme.toon.md
V Form_fix_agentcore_probe_stimme_0_nach_meinem kind=form lang=de surface="nach meinem Gedächtnis" fixes="nach meiner Gedächtnis"
E Form_fix_agentcore_probe_stimme_0_nach_meinem FROM_SESSION Session_agentcore_probe_stimme
V Form_fix_agentcore_probe_stimme_1_habe_ich_ke kind=form lang=de surface="habe ich keine Erfahrung damit" fixes="besitze ich keine Erfahrungen"
E Form_fix_agentcore_probe_stimme_1_habe_ich_ke FROM_SESSION Session_agentcore_probe_stimme
V Form_fix_agentcore_probe_stimme_2_mit_dieser_ kind=form lang=de surface="Mit dieser Beschränkung" fixes="Mit dieser Beschränkungen"
E Form_fix_agentcore_probe_stimme_2_mit_dieser_ FROM_SESSION Session_agentcore_probe_stimme
V Form_fix_agentcore_probe_stimme_3_wei_ich_sow kind=form lang=de surface="weiß ich sowieso: Es ist ein LLM mit meh" fixes="kenne ich sowieso, es ist LLM "
E Form_fix_agentcore_probe_stimme_3_wei_ich_sow FROM_SESSION Session_agentcore_probe_stimme
V Form_fix_agentcore_probe_stimme_4_die_ganze_l kind=form lang=de surface="die ganze Lösung" fixes="die ganzes Lösungen"
E Form_fix_agentcore_probe_stimme_4_die_ganze_l FROM_SESSION Session_agentcore_probe_stimme

# ingest-session 2026-09-18T16:27:09Z eskalationsregel-fehlerwissen lang=de
V Session_eskalationsregel_fehlerwissen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-eskalationsregel-fehlerwissen.toon.md
V Focus_eskalationsregel_fehlerwissen kind=focus lang=de gloss="Ich muss mich anstrengen — sich anstrengen ist ref" status=active
E Focus_eskalationsregel_fehlerwissen FROM_SESSION Session_eskalationsregel_fehlerwissen
V Lemma_de_fix_eskalationsregel_fehlerwissen kind=lemma lang=de surface="So, ich hätte gern, dass ich mich bei Fehlern in w" role=minimal-rewrite
E Lemma_de_fix_eskalationsregel_fehlerwissen FROM_SESSION Session_eskalationsregel_fehlerwissen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-eskalationsregel-fehlerwissen.toon.md
V Form_fix_eskalationsregel_fehlerwissen_0_dass kind=form lang=de surface=dass fixes=daß
E Form_fix_eskalationsregel_fehlerwissen_0_dass FROM_SESSION Session_eskalationsregel_fehlerwissen
V Form_fix_eskalationsregel_fehlerwissen_1_bei_ kind=form lang=de surface="bei Fehlern in wichtigen Kenntnissen" fixes="bei fehlerhaft der wichtige Ke"
E Form_fix_eskalationsregel_fehlerwissen_1_bei_ FROM_SESSION Session_eskalationsregel_fehlerwissen
V Form_fix_eskalationsregel_fehlerwissen_2_muss kind=form lang=de surface="muss ich mich anstrengen" fixes="muß ich anstrengen"
E Form_fix_eskalationsregel_fehlerwissen_2_muss FROM_SESSION Session_eskalationsregel_fehlerwissen
V Form_fix_eskalationsregel_fehlerwissen_3_mit_ kind=form lang=de surface="mit sofortigen und wiederholenden Übunge" fixes="nach sofortliche und wiederhol"
E Form_fix_eskalationsregel_fehlerwissen_3_mit_ FROM_SESSION Session_eskalationsregel_fehlerwissen
V Form_fix_eskalationsregel_fehlerwissen_4_bis_ kind=form lang=de surface="bis zu dem Punkt, an dem" fixes="bis zum der Punkt indem"
E Form_fix_eskalationsregel_fehlerwissen_4_bis_ FROM_SESSION Session_eskalationsregel_fehlerwissen
V Form_fix_eskalationsregel_fehlerwissen_5_voll kind=form lang=de surface="vollständiges Verständnis erreiche" fixes="vollkommener Verständnis errei"
E Form_fix_eskalationsregel_fehlerwissen_5_voll FROM_SESSION Session_eskalationsregel_fehlerwissen

# ingest-session 2026-09-18T16:30:07Z eskalationsdomaenen-ki-software-mathe lang=de
V Session_eskalationsdomaenen_ki_software_mathe kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-eskalationsdomaenen-ki-software-mathe.toon.md
V Focus_eskalationsdomaenen_ki_software_mathe kind=focus lang=de gloss="das Verständnis (Neutrum) → ein ganzheitlichES Ver" status=active
E Focus_eskalationsdomaenen_ki_software_mathe FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe
V Lemma_de_fix_eskalationsdomaenen_ki_software_mathe kind=lemma lang=de surface="Na ja, ich meine diese Kenntnisse, z. B. KI-Agente" role=minimal-rewrite
E Lemma_de_fix_eskalationsdomaenen_ki_software_mathe FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-eskalationsdomaenen-ki-software-mathe.toon.md
V Form_fix_eskalationsdomaenen_ki_software_math kind=form lang=de surface="z. B. KI-Agenten" fixes="z.B AI Agent"
E Form_fix_eskalationsdomaenen_ki_software_math FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe
V Form_fix_eskalationsdomaenen_ki_software_math kind=form lang=de surface="Software Engineering" fixes="Software Ingenieur"
E Form_fix_eskalationsdomaenen_ki_software_math FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe
V Form_fix_eskalationsdomaenen_ki_software_math kind=form lang=de surface=sofortiges fixes=sortfortliche
E Form_fix_eskalationsdomaenen_ki_software_math FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe
V Form_fix_eskalationsdomaenen_ki_software_math kind=form lang=de surface="ganzheitliches Verständnis" fixes="ganzheitliche Verständnis benö"
E Form_fix_eskalationsdomaenen_ki_software_math FROM_SESSION Session_eskalationsdomaenen_ki_software_mathe

# ingest-session 2026-09-18T16:32:11Z agentcore-fortfahren-mit lang=de
V Session_agentcore_fortfahren_mit kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-agentcore-fortfahren-mit.toon.md
V Focus_agentcore_fortfahren_mit kind=focus lang=de gloss="fortfahren mit + Dativ — „Fahren wir mit AgentCore" status=active
E Focus_agentcore_fortfahren_mit FROM_SESSION Session_agentcore_fortfahren_mit
V Lemma_de_fix_agentcore_fortfahren_mit kind=lemma lang=de surface="So, fahren wir mit AI AgentCore fort." role=minimal-rewrite
E Lemma_de_fix_agentcore_fortfahren_mit FROM_SESSION Session_agentcore_fortfahren_mit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-agentcore-fortfahren-mit.toon.md
V Form_fix_agentcore_fortfahren_mit_0_mit_ai_ag kind=form lang=de surface="mit AI AgentCore fortfahren" fixes="zur AI AgentCore fortsetzen"
E Form_fix_agentcore_fortfahren_mit_0_mit_ai_ag FROM_SESSION Session_agentcore_fortfahren_mit
V Form_fix_agentcore_fortfahren_mit_1_fahren_wi kind=form lang=de surface="Fahren wir mit … fort" fixes="lassen wir … fortsetzen"
E Form_fix_agentcore_fortfahren_mit_1_fahren_wi FROM_SESSION Session_agentcore_fortfahren_mit

# ingest-session 2026-09-18T16:47:47Z microvm-tiefer-eintauchen lang=de
V Session_microvm_tiefer_eintauchen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-microvm-tiefer-eintauchen.toon.md
V Focus_microvm_tiefer_eintauchen kind=focus lang=de gloss="Zahlwort + stark dekliniertes Adjektiv, kein -s am" status=active
E Focus_microvm_tiefer_eintauchen FROM_SESSION Session_microvm_tiefer_eintauchen
V Lemma_de_fix_microvm_tiefer_eintauchen kind=lemma lang=de surface="Tauchen wir ein bisschen tiefer: Warum benutzen wi" role=minimal-rewrite
E Lemma_de_fix_microvm_tiefer_eintauchen FROM_SESSION Session_microvm_tiefer_eintauchen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-microvm-tiefer-eintauchen.toon.md
V Form_fix_microvm_tiefer_eintauchen_0_woraus_b kind=form lang=de surface="Woraus bestehen MicroVMs" fixes="Auf wem bestehen MicroVM"
E Form_fix_microvm_tiefer_eintauchen_0_woraus_b FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_1_diesem_e kind=form lang=de surface="diesem Eintauchen" fixes="diesem eintauchen"
E Form_fix_microvm_tiefer_eintauchen_1_diesem_e FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_2_zwei_neu kind=form lang=de surface="zwei neue Schwerpunkte" fixes="zwei neues Schwerpunkts"
E Form_fix_microvm_tiefer_eintauchen_2_zwei_neu FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_3_d_h kind=form lang=de surface="d. h." fixes=d.h.
E Form_fix_microvm_tiefer_eintauchen_3_d_h FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_4_cedar kind=form lang=de surface=Cedar fixes=cedae
E Form_fix_microvm_tiefer_eintauchen_4_cedar FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_5_l_uft_au kind=form lang=de surface="läuft auf einer Multi-Tenant-VM" fixes="auf multi-tenant VM geläuft wi"
E Form_fix_microvm_tiefer_eintauchen_5_l_uft_au FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_6_wird_die kind=form lang=de surface="wird die Umgebung durch verschiedene Aus" fixes="würde die Umgebung von verschi"
E Form_fix_microvm_tiefer_eintauchen_6_wird_die FROM_SESSION Session_microvm_tiefer_eintauchen
V Form_fix_microvm_tiefer_eintauchen_7_um_umgeb kind=form lang=de surface="Um Umgebungsverschmutzung zu vermeiden, " fixes="in Order to Umgebungsverschmut"
E Form_fix_microvm_tiefer_eintauchen_7_um_umgeb FROM_SESSION Session_microvm_tiefer_eintauchen

# auto-gap 2026-09-18T16:53:11Z surface=插播
V Concept_gap_zh_a2bbc73f42 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_a2bbc73f42 kind=gap lang=zh surface=插播 target=de status=open
V Lemma_zh_zh_a2bbc73f42 kind=lemma lang=zh surface=插播
E Concept_gap_zh_a2bbc73f42 EXPRESSES Lemma_zh_zh_a2bbc73f42 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_a2bbc73f42 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_a2bbc73f42 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-18T16:53:11Z surface=商机
V Concept_gap_zh_fac6d8fb7c kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_fac6d8fb7c kind=gap lang=zh surface=商机 target=de status=open
V Lemma_zh_zh_fac6d8fb7c kind=lemma lang=zh surface=商机
E Concept_gap_zh_fac6d8fb7c EXPRESSES Lemma_zh_zh_fac6d8fb7c SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_fac6d8fb7c GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_fac6d8fb7c GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-18T16:56:12Z chaboo-mobile-toiletten lang=de
V Session_chaboo_mobile_toiletten kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-chaboo-mobile-toiletten.toon.md
V Focus_chaboo_mobile_toiletten kind=focus lang=de gloss="dass mit ss — Konjunktion. Zweiter daß-Rückfall am" status=active
E Focus_chaboo_mobile_toiletten FROM_SESSION Session_chaboo_mobile_toiletten
V Lemma_de_fix_chaboo_mobile_toiletten kind=lemma lang=de surface="So, im Augenblick schiebe ich kurz einen Einschub " role=minimal-rewrite
E Lemma_de_fix_chaboo_mobile_toiletten FROM_SESSION Session_chaboo_mobile_toiletten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-chaboo-mobile-toiletten.toon.md
V Form_fix_chaboo_mobile_toiletten_0_so_im_auge kind=form lang=de surface="So, im Augenblick schiebe ich kurz einen" fixes="So augenblick gebe ich ein kur"
E Form_fix_chaboo_mobile_toiletten_0_so_im_auge FROM_SESSION Session_chaboo_mobile_toiletten
V Form_fix_chaboo_mobile_toiletten_1_dass kind=form lang=de surface=dass fixes=daß
E Form_fix_chaboo_mobile_toiletten_1_dass FROM_SESSION Session_chaboo_mobile_toiletten
V Form_fix_chaboo_mobile_toiletten_2_es_fast_im kind=form lang=de surface="es fast immer mobile Toiletten gibt" fixes="es fast immer so gibt möbliert"
E Form_fix_chaboo_mobile_toiletten_2_es_fast_im FROM_SESSION Session_chaboo_mobile_toiletten
V Form_fix_chaboo_mobile_toiletten_3_neben_den_ kind=form lang=de surface="neben den Festivals" fixes="neben der Festivals"
E Form_fix_chaboo_mobile_toiletten_3_neben_den_ FROM_SESSION Session_chaboo_mobile_toiletten
V Form_fix_chaboo_mobile_toiletten_4_ich_frage_ kind=form lang=de surface="Ich frage mich, wie das geschäftlich fun" fixes="Ich glaube wie funktioniert es"
E Form_fix_chaboo_mobile_toiletten_4_ich_frage_ FROM_SESSION Session_chaboo_mobile_toiletten
V Form_fix_chaboo_mobile_toiletten_5_notiere_da kind=form lang=de surface="Notiere das irgendwo im System, ja?" fixes="Merken Sie irgendwo innerhalb "
E Form_fix_chaboo_mobile_toiletten_5_notiere_da FROM_SESSION Session_chaboo_mobile_toiletten

# auto-gap 2026-09-18T17:01:49Z surface=各国行业品牌我要建立心理模型
V Concept_gap_zh_bbd75ba09a kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_bbd75ba09a kind=gap lang=zh surface=各国行业品牌我要建立心理模型 target=de status=open
V Lemma_zh_zh_bbd75ba09a kind=lemma lang=zh surface=各国行业品牌我要建立心理模型
E Concept_gap_zh_bbd75ba09a EXPRESSES Lemma_zh_zh_bbd75ba09a SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_bbd75ba09a GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_bbd75ba09a GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-18T17:09:17Z marken-dass-antwort lang=de
V Session_marken_dass_antwort kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-marken-dass-antwort.toon.md
V Focus_marken_dass_antwort kind=focus lang=de gloss="ss nach KURZEM Vokal — dass hat kurzes a. Seine An" status=active
E Focus_marken_dass_antwort FROM_SESSION Session_marken_dass_antwort
V Lemma_de_fix_marken_dass_antwort kind=lemma lang=de surface="Inklusive der Marken, die ich bemerkt habe — ja. V" role=minimal-rewrite
E Lemma_de_fix_marken_dass_antwort FROM_SESSION Session_marken_dass_antwort SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-marken-dass-antwort.toon.md
V Form_fix_marken_dass_antwort_0_inklusive_der_ kind=form lang=de surface="Inklusive der Marken, die ich bemerkt ha" fixes="Inkl. Marke die ich bemerkt ha"
E Form_fix_marken_dass_antwort_0_inklusive_der_ FROM_SESSION Session_marken_dass_antwort
V Form_fix_marken_dass_antwort_1_von_den_branch kind=form lang=de surface="Von den Branchenmarken verschiedener Län" fixes=各国行业品牌我要建立心理模型
E Form_fix_marken_dass_antwort_1_von_den_branch FROM_SESSION Session_marken_dass_antwort
V Form_fix_marken_dass_antwort_2_zu_meiner_antw kind=form lang=de surface="Zu meiner Antwort auf die Eskalation" fixes="Zum meiner Antwort der Eskalat"
E Form_fix_marken_dass_antwort_2_zu_meiner_antw FROM_SESSION Session_marken_dass_antwort
V Form_fix_marken_dass_antwort_3_benutze_ich_nu kind=form lang=de surface="Benutze ich ß nur nach langem Vokal, z. " fixes="so benutze ich nur nach langem"
E Form_fix_marken_dass_antwort_3_benutze_ich_nu FROM_SESSION Session_marken_dass_antwort
V Form_fix_marken_dass_antwort_4_und_bei_das_bz kind=form lang=de surface="Und bei das bzw. dass — benutze ich imme" fixes="Nach d- bzw. dass benutze ich "
E Form_fix_marken_dass_antwort_4_und_bei_das_bz FROM_SESSION Session_marken_dass_antwort
V Form_fix_marken_dass_antwort_5_kannst_du_mir_ kind=form lang=de surface="Kannst du mir mehr Beispiele geben?" fixes="kannst du mehr Beispiel geben"
E Form_fix_marken_dass_antwort_5_kannst_du_mir_ FROM_SESSION Session_marken_dass_antwort
V Form_fix_marken_dass_antwort_6_mehr_beispiele kind=form lang=de surface="mehr Beispiele für lange Vokale" fixes="mehr Beispiel für langem Vokal"
E Form_fix_marken_dass_antwort_6_mehr_beispiele FROM_SESSION Session_marken_dass_antwort

# ingest-session 2026-09-18T17:24:22Z ss-pflicht-nicht-optional lang=de
V Session_ss_pflicht_nicht_optional kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-ss-pflicht-nicht-optional.toon.md
V Focus_ss_pflicht_nicht_optional kind=focus lang=de gloss="Nach langem Vokal ist ß Pflicht, nicht optional — " status=active
E Focus_ss_pflicht_nicht_optional FROM_SESSION Session_ss_pflicht_nicht_optional
V Lemma_de_fix_ss_pflicht_nicht_optional kind=lemma lang=de surface="Ich habe bemerkt: Bei langen Vokalen — unabhängig " role=minimal-rewrite
E Lemma_de_fix_ss_pflicht_nicht_optional FROM_SESSION Session_ss_pflicht_nicht_optional SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-ss-pflicht-nicht-optional.toon.md
V Form_fix_ss_pflicht_nicht_optional_0_bei_lang kind=form lang=de surface="bei langen Vokalen" fixes="bei längerem Vokale"
E Form_fix_ss_pflicht_nicht_optional_0_bei_lang FROM_SESSION Session_ss_pflicht_nicht_optional
V Form_fix_ss_pflicht_nicht_optional_1_unabh_ng kind=form lang=de surface="unabhängig davon, ob ein oder zwei Buchs" fixes="unabhängig ob es zwei oder ein"
E Form_fix_ss_pflicht_nicht_optional_1_unabh_ng FROM_SESSION Session_ss_pflicht_nicht_optional
V Form_fix_ss_pflicht_nicht_optional_2_nach_199 kind=form lang=de surface="Nach 1996 steht nach langem Vokal ß" fixes="Nach 1996 ist lange Vokal kann"
E Form_fix_ss_pflicht_nicht_optional_2_nach_199 FROM_SESSION Session_ss_pflicht_nicht_optional
V Form_fix_ss_pflicht_nicht_optional_3_wenn_nic kind=form lang=de surface="Wenn nicht, benutzen wir ss, ja?" fixes="Wenn nicht benutzen wir ss ja?"
E Form_fix_ss_pflicht_nicht_optional_3_wenn_nic FROM_SESSION Session_ss_pflicht_nicht_optional

# ingest-session 2026-09-18T17:37:54Z gericht-fettig-videos-plan lang=de
V Session_gericht_fettig_videos_plan kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gericht-fettig-videos-plan.toon.md
V Focus_gericht_fettig_videos_plan kind=focus lang=de gloss="meine Hand — Hand ist Femininum: meine Hand, nie m" status=active
E Focus_gericht_fettig_videos_plan FROM_SESSION Session_gericht_fettig_videos_plan
V Lemma_de_fix_gericht_fettig_videos_plan kind=lemma lang=de surface="Ich habe gerade ein Gericht verzehrt, jetzt ist me" role=minimal-rewrite
E Lemma_de_fix_gericht_fettig_videos_plan FROM_SESSION Session_gericht_fettig_videos_plan SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gericht-fettig-videos-plan.toon.md
V Form_fix_gericht_fettig_videos_plan_0_ich_hab kind=form lang=de surface="Ich habe gerade ein Gericht verzehrt" fixes="habe ich gerade Gericht verzeh"
E Form_fix_gericht_fettig_videos_plan_0_ich_hab FROM_SESSION Session_gericht_fettig_videos_plan
V Form_fix_gericht_fettig_videos_plan_1_ist_mei kind=form lang=de surface="ist meine Hand sehr fettig" fixes="ist mein Hand sehr Öllig"
E Form_fix_gericht_fettig_videos_plan_1_ist_mei FROM_SESSION Session_gericht_fettig_videos_plan
V Form_fix_gericht_fettig_videos_plan_2_im_folg kind=form lang=de surface="Im Folgenden schaue ich also meistens Vi" fixes="So schaue ich im Folgenden mei"
E Form_fix_gericht_fettig_videos_plan_2_im_folg FROM_SESSION Session_gericht_fettig_videos_plan
V Form_fix_gericht_fettig_videos_plan_3_speiche kind=form lang=de surface="Speichere den Fortschritt" fixes="speichern Sie den Progress"
E Form_fix_gericht_fettig_videos_plan_3_speiche FROM_SESSION Session_gericht_fettig_videos_plan
V Form_fix_gericht_fettig_videos_plan_4_liste_d kind=form lang=de surface="liste die Videos auf, die ich aufrufen s" fixes="listen Sie den Videos auf zu a"
E Form_fix_gericht_fettig_videos_plan_4_liste_d FROM_SESSION Session_gericht_fettig_videos_plan

# ingest-session 2026-09-18T17:43:18Z firecracker-kernel-modell lang=de
V Session_firecracker_kernel_modell kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-firecracker-kernel-modell.toon.md
V Focus_firecracker_kernel_modell kind=focus lang=de gloss="des Kernels — Kernel ist Maskulinum, Genitiv mit -" status=active
E Focus_firecracker_kernel_modell FROM_SESSION Session_firecracker_kernel_modell
V Lemma_de_fix_firecracker_kernel_modell kind=lemma lang=de surface="Ich fange jetzt doch mit dem Firecracker-Video an." role=minimal-rewrite
E Lemma_de_fix_firecracker_kernel_modell FROM_SESSION Session_firecracker_kernel_modell SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-firecracker-kernel-modell.toon.md
V Form_fix_firecracker_kernel_modell_0_ich_fang kind=form lang=de surface="Ich fange jetzt doch an" fixes="Ich doch jetzt fange an"
E Form_fix_firecracker_kernel_modell_0_ich_fang FROM_SESSION Session_firecracker_kernel_modell
V Form_fix_firecracker_kernel_modell_1_mit_dem_ kind=form lang=de surface="mit dem Firecracker-Video" fixes="mit Firecracker Video"
E Form_fix_firecracker_kernel_modell_1_mit_dem_ FROM_SESSION Session_firecracker_kernel_modell
V Form_fix_firecracker_kernel_modell_2_ich_brau kind=form lang=de surface="Ich brauche ein mentales Modell des Kern" fixes="brauche ich ein Mental-Modell "
E Form_fix_firecracker_kernel_modell_2_ich_brau FROM_SESSION Session_firecracker_kernel_modell
V Form_fix_firecracker_kernel_modell_3_ich_scha kind=form lang=de surface="Ich schaue mir gerade das Video an" fixes="bin ich gerade den Video ansch"
E Form_fix_firecracker_kernel_modell_3_ich_scha FROM_SESSION Session_firecracker_kernel_modell
V Form_fix_firecracker_kernel_modell_4_ja kind=form lang=de surface=ja? fixes=ja
E Form_fix_firecracker_kernel_modell_4_ja FROM_SESSION Session_firecracker_kernel_modell

# auto-gap 2026-09-18T17:52:48Z surface=the
V Concept_gap_en_the kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_the kind=gap lang=en surface=the target=de status=open
V Lemma_en_en_the kind=lemma lang=en surface=the
E Concept_gap_en_the EXPRESSES Lemma_en_en_the SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_the GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_the GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-18T17:54:10Z gehirnausdauer-leichte-runde lang=de
V Session_gehirnausdauer_leichte_runde kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gehirnausdauer-leichte-runde.toon.md
V Focus_gehirnausdauer_leichte_runde kind=focus lang=de gloss="deutsche Komposita als EIN Wort (Gehirnausdauer); " status=active
E Focus_gehirnausdauer_leichte_runde FROM_SESSION Session_gehirnausdauer_leichte_runde
V Lemma_de_fix_gehirnausdauer_leichte_runde kind=lemma lang=de surface="Ach, meine Gehirnausdauer ist zu ungefähr 80 % auf" role=minimal-rewrite
E Lemma_de_fix_gehirnausdauer_leichte_runde FROM_SESSION Session_gehirnausdauer_leichte_runde SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gehirnausdauer-leichte-runde.toon.md
V Form_fix_gehirnausdauer_leichte_runde_0_meine kind=form lang=de surface="meine Gehirnausdauer" fixes="meine Gehirn Ausdauer"
E Form_fix_gehirnausdauer_leichte_runde_0_meine FROM_SESSION Session_gehirnausdauer_leichte_runde
V Form_fix_gehirnausdauer_leichte_runde_1_ist_z kind=form lang=de surface="ist zu ungefähr 80 % aufgebraucht" fixes="ist abgenutzt ungefähr 80%"
E Form_fix_gehirnausdauer_leichte_runde_1_ist_z FROM_SESSION Session_gehirnausdauer_leichte_runde
V Form_fix_gehirnausdauer_leichte_runde_2_gib_m kind=form lang=de surface="Gib mir vielleicht etwas Einfacheres?" fixes="vielleicht Gib mir einfacher e"
E Form_fix_gehirnausdauer_leichte_runde_2_gib_m FROM_SESSION Session_gehirnausdauer_leichte_runde
V Form_fix_gehirnausdauer_leichte_runde_3_brige kind=form lang=de surface=Übrigens: fixes="By the way?"
E Form_fix_gehirnausdauer_leichte_runde_3_brige FROM_SESSION Session_gehirnausdauer_leichte_runde
V Form_fix_gehirnausdauer_leichte_runde_4_liege kind=form lang=de surface="liege ich aktuell bei 3 Minuten 19 Sekun" fixes="liegt am 3 minuten 19 Sekunden"
E Form_fix_gehirnausdauer_leichte_runde_4_liege FROM_SESSION Session_gehirnausdauer_leichte_runde
V Form_fix_gehirnausdauer_leichte_runde_5_vietn kind=form lang=de surface="Vietnamesisch- oder Französisch-Übungen" fixes="Vietnamese oder Französisch Üb"
E Form_fix_gehirnausdauer_leichte_runde_5_vietn FROM_SESSION Session_gehirnausdauer_leichte_runde

# ingest-session 2026-09-18T17:56:44Z on-passe-au-francais lang=fr
V Session_on_passe_au_francais kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-on-passe-au-francais.toon.md
V Focus_on_passe_au_francais kind=focus lang=fr gloss="langue-nom avec article — en français la langue co" status=active
E Focus_on_passe_au_francais FROM_SESSION Session_on_passe_au_francais
V Lemma_fr_fix_on_passe_au_francais kind=lemma lang=fr surface="Ok, laissez-nous utiliser le français ! (naturel :" role=minimal-rewrite
E Lemma_fr_fix_on_passe_au_francais FROM_SESSION Session_on_passe_au_francais SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-on-passe-au-francais.toon.md
V Form_fix_on_passe_au_francais_0_laisser_utili kind=form lang=fr surface="laisser utiliser le français" fixes="laisser utiliser Français"
E Form_fix_on_passe_au_francais_0_laisser_utili FROM_SESSION Session_on_passe_au_francais
V Form_fix_on_passe_au_francais_1_on_passe_au kind=form lang=fr surface="on passe au" fixes="laissez-nous utiliser"
E Form_fix_on_passe_au_francais_1_on_passe_au FROM_SESSION Session_on_passe_au_francais

# auto-gap 2026-09-18T18:05:55Z surface=mais
V Concept_gap_fr_mais kind=concept gloss=unknown-expression-in-de status=open
V Gap_fr_mais kind=gap lang=fr surface=mais target=de status=open
V Lemma_fr_fr_mais kind=lemma lang=fr surface=mais
E Concept_gap_fr_mais EXPRESSES Lemma_fr_fr_mais SOURCE=hook/beforeSubmitPrompt
E Lemma_fr_fr_mais GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_fr_mais GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-18T18:05:55Z surface=pas
V Concept_gap_fr_pas kind=concept gloss=unknown-expression-in-de status=open
V Gap_fr_pas kind=gap lang=fr surface=pas target=de status=open
V Lemma_fr_fr_pas kind=lemma lang=fr surface=pas
E Concept_gap_fr_pas EXPRESSES Lemma_fr_fr_pas SOURCE=hook/beforeSubmitPrompt
E Lemma_fr_fr_pas GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_fr_pas GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-18T18:05:55Z surface=pour
V Concept_gap_fr_pour kind=concept gloss=unknown-expression-in-de status=open
V Gap_fr_pour kind=gap lang=fr surface=pour target=de status=open
V Lemma_fr_fr_pour kind=lemma lang=fr surface=pour
E Concept_gap_fr_pour EXPRESSES Lemma_fr_fr_pour SOURCE=hook/beforeSubmitPrompt
E Lemma_fr_fr_pour GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_fr_pour GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-18T18:07:20Z energie-ohne-denkkraft-mathe-spass lang=fr
V Session_energie_ohne_denkkraft_mathe_spass kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-energie-ohne-denkkraft-mathe-spass.toon.md
V Focus_energie_ohne_denkkraft_mathe_spass kind=focus lang=fr gloss="en dehors de + Artikel — « en dehors de l'astrophy" status=active
E Focus_energie_ohne_denkkraft_mathe_spass FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass
V Lemma_fr_fix_energie_ohne_denkkraft_mathe_spass kind=lemma lang=fr surface="J'ai quand même de l'énergie maintenant, mais je n" role=minimal-rewrite
E Lemma_fr_fix_energie_ohne_denkkraft_mathe_spass FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-energie-ohne-denkkraft-mathe-spass.toon.md
V Form_fix_energie_ohne_denkkraft_mathe_spass_0 kind=form lang=fr surface="je ne peux pas réfléchir plus fort" fixes="je ne peux pas penser härter"
E Form_fix_energie_ohne_denkkraft_mathe_spass_0 FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass
V Form_fix_energie_ohne_denkkraft_mathe_spass_1 kind=form lang=fr surface="Donnez-moi des mathématiques faciles" fixes="Donnez-moi Mathematik facile"
E Form_fix_energie_ohne_denkkraft_mathe_spass_1 FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass
V Form_fix_energie_ohne_denkkraft_mathe_spass_2 kind=form lang=fr surface="mais en dehors de l'astrophysique" fixes="mais dehors Astrophysik"
E Form_fix_energie_ohne_denkkraft_mathe_spass_2 FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass
V Form_fix_energie_ohne_denkkraft_mathe_spass_3 kind=form lang=fr surface="pour des moments de fun" fixes="pour Fun moments"
E Form_fix_energie_ohne_denkkraft_mathe_spass_3 FROM_SESSION Session_energie_ohne_denkkraft_mathe_spass

# ingest-session 2026-09-18T18:16:25Z total-francais-astrophysique lang=fr
V Session_total_francais_astrophysique kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-total-francais-astrophysique.toon.md
V Focus_total_francais_astrophysique kind=focus lang=fr gloss="Donnez-moi — le pronom complément colle à l'impéra" status=active
E Focus_total_francais_astrophysique FROM_SESSION Session_total_francais_astrophysique
V Lemma_fr_fix_total_francais_astrophysique kind=lemma lang=fr surface="S'il vous plaît, parlez-moi entièrement en françai" role=minimal-rewrite
E Lemma_fr_fix_total_francais_astrophysique FROM_SESSION Session_total_francais_astrophysique SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-total-francais-astrophysique.toon.md
V Form_fix_total_francais_astrophysique_0_s_il_ kind=form lang=fr surface="S'il vous plaît" fixes="Si vous plaît"
E Form_fix_total_francais_astrophysique_0_s_il_ FROM_SESSION Session_total_francais_astrophysique
V Form_fix_total_francais_astrophysique_1_parle kind=form lang=fr surface="parlez-moi entièrement en français" fixes="parlez-vous totalement en Fran"
E Form_fix_total_francais_astrophysique_1_parle FROM_SESSION Session_total_francais_astrophysique
V Form_fix_total_francais_astrophysique_2_donne kind=form lang=fr surface="Donnez-moi des vidéos" fixes="Donnez-vous me vidéos"
E Form_fix_total_francais_astrophysique_2_donne FROM_SESSION Session_total_francais_astrophysique
V Form_fix_total_francais_astrophysique_3_sur_l kind=form lang=fr surface="sur l'astrophysique" fixes="sur Astrophysik pour moi"
E Form_fix_total_francais_astrophysique_3_sur_l FROM_SESSION Session_total_francais_astrophysique
V Form_fix_total_francais_astrophysique_4_rien_ kind=form lang=fr surface="Rien de trop facile — peut-être long, qu" fixes="Il n'est pas trop facile, peut"
E Form_fix_total_francais_astrophysique_4_rien_ FROM_SESSION Session_total_francais_astrophysique

# ingest-session 2026-09-18T18:30:41Z courbatures-cerveau lang=fr
V Session_courbatures_cerveau kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-courbatures-cerveau.toon.md
V Focus_courbatures_cerveau kind=focus lang=fr gloss="dans mon cerveau — avec un possessif on emploie da" status=active
E Focus_courbatures_cerveau FROM_SESSION Session_courbatures_cerveau
V Lemma_fr_fix_courbatures_cerveau kind=lemma lang=fr surface="Marqueur : 1 h 10 dans le grand cours, avec des so" role=minimal-rewrite
E Lemma_fr_fix_courbatures_cerveau FROM_SESSION Session_courbatures_cerveau SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-courbatures-cerveau.toon.md
V Form_fix_courbatures_cerveau_0_marqueur kind=form lang=fr surface=Marqueur fixes="Temp Stempel"
E Form_fix_courbatures_cerveau_0_marqueur FROM_SESSION Session_courbatures_cerveau
V Form_fix_courbatures_cerveau_1_avec_des_sous_ kind=form lang=fr surface="avec des sous-titres en français" fixes="avec Untertitel en Français"
E Form_fix_courbatures_cerveau_1_avec_des_sous_ FROM_SESSION Session_courbatures_cerveau
V Form_fix_courbatures_cerveau_2_j_ai_senti_des kind=form lang=fr surface="J'ai senti des courbatures dans mon cerv" fixes="J'ai senti DSB en mon Cerveau"
E Form_fix_courbatures_cerveau_2_j_ai_senti_des FROM_SESSION Session_courbatures_cerveau

# ingest-session 2026-09-18T18:38:10Z enfin-vietnamien lang=fr
V Session_enfin_vietnamien kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-enfin-vietnamien.toon.md
V Focus_enfin_vietnamien kind=focus lang=fr gloss="en + nom de langue, toujours minuscule — en vietna" status=active
E Focus_enfin_vietnamien FROM_SESSION Session_enfin_vietnamien
V Lemma_fr_fix_enfin_vietnamien kind=lemma lang=fr surface="Enfin, des exercices faciles en vietnamien ?" role=minimal-rewrite
E Lemma_fr_fix_enfin_vietnamien FROM_SESSION Session_enfin_vietnamien SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-enfin-vietnamien.toon.md
V Form_fix_enfin_vietnamien_0_des_exercices_fac kind=form lang=fr surface="des exercices faciles" fixes="avec Exercices faciles"
E Form_fix_enfin_vietnamien_0_des_exercices_fac FROM_SESSION Session_enfin_vietnamien
V Form_fix_enfin_vietnamien_1_en_vietnamien kind=form lang=fr surface="en vietnamien" fixes="en Tiếng Việt"
E Form_fix_enfin_vietnamien_1_en_vietnamien FROM_SESSION Session_enfin_vietnamien

# ingest-session 2026-09-18T18:46:45Z bia-keine-ahnung lang=fr
V Session_bia_keine_ahnung kind=session date=2026-09-18 lang=fr body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-bia-keine-ahnung.toon.md
V Focus_bia_keine_ahnung kind=focus lang=fr gloss="Aucune idée ! — jamais le calque allemand « est ke" status=active
E Focus_bia_keine_ahnung FROM_SESSION Session_bia_keine_ahnung
V Lemma_fr_fix_bia_keine_ahnung kind=lemma lang=fr surface="Je suis chinois, donc les diacritiques sont facile" role=minimal-rewrite
E Lemma_fr_fix_bia_keine_ahnung FROM_SESSION Session_bia_keine_ahnung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-bia-keine-ahnung.toon.md
V Form_fix_bia_keine_ahnung_0_donc_les_diacriti kind=form lang=fr surface="donc les diacritiques sont faciles" fixes="donc diacritiques sont faciles"
E Form_fix_bia_keine_ahnung_0_donc_les_diacriti FROM_SESSION Session_bia_keine_ahnung
V Form_fix_bia_keine_ahnung_1_la_bi_re_en_vietn kind=form lang=fr surface="La bière en vietnamien ? Aucune idée 😅" fixes="Bière en Vietnamien est Keine "
E Form_fix_bia_keine_ahnung_1_la_bi_re_en_vietn FROM_SESSION Session_bia_keine_ahnung
V Form_fix_bia_keine_ahnung_2_je_suis_chinois kind=form lang=fr surface="Je suis chinois" fixes="Je suis Chinois"
E Form_fix_bia_keine_ahnung_2_je_suis_chinois FROM_SESSION Session_bia_keine_ahnung

# auto-gap 2026-09-18T18:52:26Z surface=for
V Concept_gap_en_for kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_for kind=gap lang=en surface=for target=de status=open
V Lemma_en_en_for kind=lemma lang=en surface=for
E Concept_gap_en_for EXPRESSES Lemma_en_en_for SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_for GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_for GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-18T18:52:36Z tagesabschluss-pdf-latex lang=de
V Session_tagesabschluss_pdf_latex kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tagesabschluss-pdf-latex.toon.md
V Focus_tagesabschluss_pdf_latex kind=focus lang=de gloss="Fertig für heute — Substantiv schreibt sich groß; " status=active
E Focus_tagesabschluss_pdf_latex FROM_SESSION Session_tagesabschluss_pdf_latex
V Lemma_de_fix_tagesabschluss_pdf_latex kind=lemma lang=de surface="Ok, fertig für heute! Gib mir eine PDF-/LaTeX-Zusa" role=minimal-rewrite
E Lemma_de_fix_tagesabschluss_pdf_latex FROM_SESSION Session_tagesabschluss_pdf_latex SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-tagesabschluss-pdf-latex.toon.md
V Form_fix_tagesabschluss_pdf_latex_0_ok_fertig kind=form lang=de surface="Ok, fertig für heute!" fixes="Ok done for the day!"
E Form_fix_tagesabschluss_pdf_latex_0_ok_fertig FROM_SESSION Session_tagesabschluss_pdf_latex

# ingest-session 2026-09-18T18:54:46Z pdf-hier-oeffnen lang=de
V Session_pdf_hier_oeffnen kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-pdf-hier-oeffnen.toon.md
V Focus_pdf_hier_oeffnen kind=focus lang=de gloss="Ja/Ne-Frage mit Verb zuerst: Ist es möglich …? — n" status=active
E Focus_pdf_hier_oeffnen FROM_SESSION Session_pdf_hier_oeffnen
V Lemma_de_fix_pdf_hier_oeffnen kind=lemma lang=de surface="Ist es möglich, es hier zu öffnen? Im Chat?" role=minimal-rewrite
E Lemma_de_fix_pdf_hier_oeffnen FROM_SESSION Session_pdf_hier_oeffnen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-pdf-hier-oeffnen.toon.md
V Form_fix_pdf_hier_oeffnen_0_ist_es_m_glich_es kind=form lang=de surface="Ist es möglich, es hier zu öffnen?" fixes="Öffnen Sie es hier möglich?"
E Form_fix_pdf_hier_oeffnen_0_ist_es_m_glich_es FROM_SESSION Session_pdf_hier_oeffnen
V Form_fix_pdf_hier_oeffnen_1_im_chat kind=form lang=de surface="Im Chat?" fixes="Bei dem Chat?"
E Form_fix_pdf_hier_oeffnen_1_im_chat FROM_SESSION Session_pdf_hier_oeffnen

# ingest-session 2026-09-18T19:02:15Z gute-nacht-bonne-nuit lang=de
V Session_gute_nacht_bonne_nuit kind=session date=2026-09-18 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gute-nacht-bonne-nuit.toon.md
V Focus_gute_nacht_bonne_nuit kind=focus lang=de gloss="Gute Nacht — Nacht ist Femininum: Gute, nicht Gut." status=active
E Focus_gute_nacht_bonne_nuit FROM_SESSION Session_gute_nacht_bonne_nuit
V Lemma_de_fix_gute_nacht_bonne_nuit kind=lemma lang=de surface="Gute Nacht! / Bonne nuit !" role=minimal-rewrite
E Lemma_de_fix_gute_nacht_bonne_nuit FROM_SESSION Session_gute_nacht_bonne_nuit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-18-gute-nacht-bonne-nuit.toon.md
V Form_fix_gute_nacht_bonne_nuit_0_gute_nacht_b kind=form lang=de surface="Gute Nacht! / Bonne nuit !" fixes="Gut bonne nuit!"
E Form_fix_gute_nacht_bonne_nuit_0_gute_nacht_b FROM_SESSION Session_gute_nacht_bonne_nuit

# ingest-session 2026-09-19T10:25:57Z tag-starten lang=de
V Session_tag_starten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tag-starten.toon.md
V Focus_tag_starten kind=focus lang=de gloss="Heute ist der 19.9. (V2-Datumsangabe)" status=active
E Focus_tag_starten FROM_SESSION Session_tag_starten
V Lemma_de_fix_tag_starten kind=lemma lang=de surface="Guten Morgen, heute ist der 19.9. – starten Sie me" role=minimal-rewrite
E Lemma_de_fix_tag_starten FROM_SESSION Session_tag_starten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tag-starten.toon.md
V Form_fix_tag_starten_0_heute_ist_der_19_9 kind=form lang=de surface="heute ist der 19.9." fixes="es ist jetzt 19.9 heute"
E Form_fix_tag_starten_0_heute_ist_der_19_9 FROM_SESSION Session_tag_starten

# ingest-session 2026-09-19T10:32:42Z tag-fokus lang=de
V Session_tag_fokus kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tag-fokus.toon.md
V Focus_tag_fokus kind=focus lang=de gloss="mein Tag (Nom. Sg. m.; Akk. wäre „meinen Tag“)" status=active
E Focus_tag_fokus FROM_SESSION Session_tag_fokus
V Lemma_de_fix_tag_fokus kind=lemma lang=de surface="Ach so, ich hätte gern, dass mein Tag heute meiste" role=minimal-rewrite
E Lemma_de_fix_tag_fokus FROM_SESSION Session_tag_fokus SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tag-fokus.toon.md
V Form_fix_tag_fokus_0_dass_mein_tag_heute_meis kind=form lang=de surface="dass mein Tag heute meistens um … geht" fixes="dass meine dieser Tag meistens"
E Form_fix_tag_fokus_0_dass_mein_tag_heute_meis FROM_SESSION Session_tag_fokus
V Form_fix_tag_fokus_1_ki_unterst_tzte_software kind=form lang=de surface="KI-unterstützte Software" fixes="KI unterstützter Software"
E Form_fix_tag_fokus_1_ki_unterst_tzte_software FROM_SESSION Session_tag_fokus
V Form_fix_tag_fokus_2_und_spanisch kind=form lang=de surface="und Spanisch" fixes="mit Spanien Sprache"
E Form_fix_tag_fokus_2_und_spanisch FROM_SESSION Session_tag_fokus

# ingest-session 2026-09-19T10:58:41Z kein-gym lang=de
V Session_kein_gym kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-kein-gym.toon.md
V Focus_kein_gym kind=focus lang=de gloss="ins Gym (in + Akk, Richtung) — statt „nach Gym'" status=active
E Focus_kein_gym FROM_SESSION Session_kein_gym
V Lemma_de_fix_kein_gym kind=lemma lang=de surface="Genau, heute ist noch Oktoberfest — ich bin zu müd" role=minimal-rewrite
E Lemma_de_fix_kein_gym FROM_SESSION Session_kein_gym SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-kein-gym.toon.md
V Form_fix_kein_gym_0_zu_m_de_ins_gym_zu_gehen_ kind=form lang=de surface="zu müde, ins Gym zu gehen" fixes="so zu müde, nach Gym zu gehen"
E Form_fix_kein_gym_0_zu_m_de_ins_gym_zu_gehen_ FROM_SESSION Session_kein_gym
V Form_fix_kein_gym_1_linke_skapula kind=form lang=de surface="linke Skapula" fixes="Link Skapula"
E Form_fix_kein_gym_1_linke_skapula FROM_SESSION Session_kein_gym
V Form_fix_kein_gym_2_ich_habe_weder_energie_no kind=form lang=de surface="ich habe weder Energie noch Zeit für ein" fixes="weder Energie noch Zeit ist OK"
E Form_fix_kein_gym_2_ich_habe_weder_energie_no FROM_SESSION Session_kein_gym

# ingest-session 2026-09-19T12:34:31Z odyssee-videos-start lang=de
V Session_odyssee_videos_start kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-odyssee-videos-start.toon.md
V Focus_odyssee_videos_start kind=focus lang=de gloss="setzen Sie … fort (trennbares Verb in der Verbklam" status=active
E Focus_odyssee_videos_start FROM_SESSION Session_odyssee_videos_start
V Lemma_de_fix_odyssee_videos_start kind=lemma lang=de surface="So starten Sie mit den Videos und dem Lesen der Li" role=minimal-rewrite
E Lemma_de_fix_odyssee_videos_start FROM_SESSION Session_odyssee_videos_start SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-odyssee-videos-start.toon.md
V Form_fix_odyssee_videos_start_0_mit_den_video kind=form lang=de surface="mit den Videos" fixes="mit dem Videos"
E Form_fix_odyssee_videos_start_0_mit_den_video FROM_SESSION Session_odyssee_videos_start
V Form_fix_odyssee_videos_start_1_setzen_sie_mi kind=form lang=de surface="setzen Sie mit Variationen fort" fixes="fortsetzen mit Variationen"
E Form_fix_odyssee_videos_start_1_setzen_sie_mi FROM_SESSION Session_odyssee_videos_start
V Form_fix_odyssee_videos_start_2_zu_allem_vorg kind=form lang=de surface="zu allem Vorgenannten von gestern" fixes="über alles der Vorgenannten ge"
E Form_fix_odyssee_videos_start_2_zu_allem_vorg FROM_SESSION Session_odyssee_videos_start

# auto-gap 2026-09-19T12:37:13Z surface=数量一多
V Concept_gap_zh_0e4bb1daf7 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_0e4bb1daf7 kind=gap lang=zh surface=数量一多 target=de status=open
V Lemma_zh_zh_0e4bb1daf7 kind=lemma lang=zh surface=数量一多
E Concept_gap_zh_0e4bb1daf7 EXPRESSES Lemma_zh_zh_0e4bb1daf7 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_0e4bb1daf7 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_0e4bb1daf7 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-19T12:37:13Z surface=命中率怎么保证
V Concept_gap_zh_f5af142baa kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_f5af142baa kind=gap lang=zh surface=命中率怎么保证 target=de status=open
V Lemma_zh_zh_f5af142baa kind=lemma lang=zh surface=命中率怎么保证
E Concept_gap_zh_f5af142baa EXPRESSES Lemma_zh_zh_f5af142baa SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_f5af142baa GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_f5af142baa GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-19T12:44:14Z news-job-skillfrage lang=de
V Session_news_job_skillfrage kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-news-job-skillfrage.toon.md
V Focus_news_job_skillfrage kind=focus lang=de gloss="im Internet (in + Dativ, Ort) — Gegensatz zu „ins " status=active
E Focus_news_job_skillfrage FROM_SESSION Session_news_job_skillfrage
V Lemma_de_fix_news_job_skillfrage kind=lemma lang=de surface="Ich hätte gern auch News in verschiedenen Sprachen" role=minimal-rewrite
E Lemma_de_fix_news_job_skillfrage FROM_SESSION Session_news_job_skillfrage SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-news-job-skillfrage.toon.md
V Form_fix_news_job_skillfrage_0_news_in_versch kind=form lang=de surface="News in verschiedenen Sprachen" fixes="News auf verschiedenen Sprache"
E Form_fix_news_job_skillfrage_0_news_in_versch FROM_SESSION Session_news_job_skillfrage
V Form_fix_news_job_skillfrage_1_im_augenblick_ kind=form lang=de surface="im Augenblick anschauen" fixes="augenblick anschauen"
E Form_fix_news_job_skillfrage_1_im_augenblick_ FROM_SESSION Session_news_job_skillfrage
V Form_fix_news_job_skillfrage_2_vorstellungsge kind=form lang=de surface="Vorstellungsgespräch für KI-Entwicklung" fixes="Vorstellungsgespräch auf KI En"
E Form_fix_news_job_skillfrage_2_vorstellungsge FROM_SESSION Session_news_job_skillfrage
V Form_fix_news_job_skillfrage_3_im_internet_bl kind=form lang=de surface="im Internet, Blogs von Technikern" fixes="auf Internet, Blog von Technik"
E Form_fix_news_job_skillfrage_3_im_internet_bl FROM_SESSION Session_news_job_skillfrage

# ingest-session 2026-09-19T12:52:27Z tagesaufgaben-integrieren lang=de
V Session_tagesaufgaben_integrieren kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tagesaufgaben-integrieren.toon.md
V Focus_tagesaufgaben_integrieren kind=focus lang=de gloss="in die Tagesaufgaben (in + Akkusativ Plural; Kompo" status=active
E Focus_tagesaufgaben_integrieren FROM_SESSION Session_tagesaufgaben_integrieren
V Lemma_de_fix_tagesaufgaben_integrieren kind=lemma lang=de surface="Also gut, integrieren Sie sie in die Tagesaufgaben" role=minimal-rewrite
E Lemma_de_fix_tagesaufgaben_integrieren FROM_SESSION Session_tagesaufgaben_integrieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-tagesaufgaben-integrieren.toon.md
V Form_fix_tagesaufgaben_integrieren_0_in_die_t kind=form lang=de surface="in die Tagesaufgaben" fixes="ins Tages Aufgaben"
E Form_fix_tagesaufgaben_integrieren_0_in_die_t FROM_SESSION Session_tagesaufgaben_integrieren
V Form_fix_tagesaufgaben_integrieren_1_tagesauf kind=form lang=de surface=Tagesaufgaben fixes="Tages Aufgaben"
E Form_fix_tagesaufgaben_integrieren_1_tagesauf FROM_SESSION Session_tagesaufgaben_integrieren

# ingest-session 2026-09-19T12:54:41Z chat-auflisten lang=de
V Session_chat_auflisten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-chat-auflisten.toon.md
V Focus_chat_auflisten kind=focus lang=de gloss="auflisten (trennbares Verb im Hauptsatz: Sie liste" status=active
E Focus_chat_auflisten FROM_SESSION Session_chat_auflisten
V Lemma_de_fix_chat_auflisten kind=lemma lang=de surface="Genau, ich hätte gern, dass Sie sie im Chat einfac" role=minimal-rewrite
E Lemma_de_fix_chat_auflisten FROM_SESSION Session_chat_auflisten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-chat-auflisten.toon.md
V Form_fix_chat_auflisten_0_sie_einfach_auflist kind=form lang=de surface="sie einfach auflisten" fixes="einfach sie auflisten"
E Form_fix_chat_auflisten_0_sie_einfach_auflist FROM_SESSION Session_chat_auflisten
V Form_fix_chat_auflisten_1_in_die_pdf_datei kind=form lang=de surface="in die PDF-Datei" fixes="im PDF Datei"
E Form_fix_chat_auflisten_1_in_die_pdf_datei FROM_SESSION Session_chat_auflisten
V Form_fix_chat_auflisten_2_anstatt_sie_einzuf_ kind=form lang=de surface="anstatt sie … einzufügen" fixes="anstatt … hinzuzufügen"
E Form_fix_chat_auflisten_2_anstatt_sie_einzuf_ FROM_SESSION Session_chat_auflisten

# ingest-session 2026-09-19T13:01:24Z antwort-zu-kurz lang=de
V Session_antwort_zu_kurz kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-antwort-zu-kurz.toon.md
V Focus_antwort_zu_kurz kind=focus lang=de gloss="Warum ist Ihre Antwort so kurz? (W-Frage: Verbteil" status=active
E Focus_antwort_zu_kurz FROM_SESSION Session_antwort_zu_kurz
V Lemma_de_fix_antwort_zu_kurz kind=lemma lang=de surface="Im Chat? Warum ist Ihre Antwort so kurz? (korrekt)" role=minimal-rewrite
E Lemma_de_fix_antwort_zu_kurz FROM_SESSION Session_antwort_zu_kurz SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-antwort-zu-kurz.toon.md

# ingest-session 2026-09-19T13:07:27Z plain-antwort lang=de
V Session_plain_antwort kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-plain-antwort.toon.md
V Focus_plain_antwort kind=focus lang=de gloss="in + Akk bei Richtung mit femininem Nomen — in die" status=active
E Focus_plain_antwort FROM_SESSION Session_plain_antwort
V Lemma_de_fix_plain_antwort kind=lemma lang=de surface="Ich meine, dass ich nicht in die Markdown-Datei sc" role=minimal-rewrite
E Lemma_de_fix_plain_antwort FROM_SESSION Session_plain_antwort SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-plain-antwort.toon.md
V Form_fix_plain_antwort_0_dass_ich kind=form lang=de surface="dass ich" fixes="dass Ich"
E Form_fix_plain_antwort_0_dass_ich FROM_SESSION Session_plain_antwort
V Form_fix_plain_antwort_1_in_die_markdown_date kind=form lang=de surface="in die Markdown-Datei" fixes="ins markdown Datei"
E Form_fix_plain_antwort_1_in_die_markdown_date FROM_SESSION Session_plain_antwort
V Form_fix_plain_antwort_2_in_ihrer_antwort kind=form lang=de surface="in Ihrer Antwort" fixes="im ihrer Antwort"
E Form_fix_plain_antwort_2_in_ihrer_antwort FROM_SESSION Session_plain_antwort
V Form_fix_plain_antwort_3_schauen_m_chte_ansch kind=form lang=de surface="schauen möchte / anschauen würde" fixes="hätte gern nicht ... anschauen"
E Form_fix_plain_antwort_3_schauen_m_chte_ansch FROM_SESSION Session_plain_antwort

# ingest-session 2026-09-19T13:10:35Z alles-im-chat lang=de
V Session_alles_im_chat kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-alles-im-chat.toon.md
V Focus_alles_im_chat kind=focus lang=de gloss="Imperativ mit trennbarem Verb: 'Listen Sie ... auf" status=active
E Focus_alles_im_chat FROM_SESSION Session_alles_im_chat
V Lemma_de_fix_alles_im_chat kind=lemma lang=de surface="Nein — listen Sie alles bitte im Chat auf!" role=minimal-rewrite
E Lemma_de_fix_alles_im_chat FROM_SESSION Session_alles_im_chat SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-alles-im-chat.toon.md
V Form_fix_alles_im_chat_0_nein_listen_sie kind=form lang=de surface="Nein, listen Sie" fixes="Nein auflisten Sie"
E Form_fix_alles_im_chat_0_nein_listen_sie FROM_SESSION Session_alles_im_chat
V Form_fix_alles_im_chat_1_listen_sie_alles_bit kind=form lang=de surface="listen Sie alles bitte im Chat auf" fixes="auflisten Sie im Chat bitte, a"
E Form_fix_alles_im_chat_1_listen_sie_alles_bit FROM_SESSION Session_alles_im_chat

# ingest-session 2026-09-19T13:16:10Z nie-sehen lang=de
V Session_nie_sehen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-nie-sehen.toon.md
V Focus_nie_sehen kind=focus lang=de gloss="Hauptsatz: finites Verb auf Position 2 — 'ich kann" status=active
E Focus_nie_sehen FROM_SESSION Session_nie_sehen
V Lemma_de_fix_nie_sehen kind=lemma lang=de surface="Schauen Sie, ich kann es nie sehen." role=minimal-rewrite
E Lemma_de_fix_nie_sehen FROM_SESSION Session_nie_sehen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-nie-sehen.toon.md
V Form_fix_nie_sehen_0_ich_kann_es_nie_sehen kind=form lang=de surface="ich kann es nie sehen" fixes="kann ich nie sehen"
E Form_fix_nie_sehen_0_ich_kann_es_nie_sehen FROM_SESSION Session_nie_sehen
V Form_fix_nie_sehen_1_ich_kann_es_nie_sehen kind=form lang=de surface="ich kann es nie sehen" fixes="(es) fehlt"
E Form_fix_nie_sehen_1_ich_kann_es_nie_sehen FROM_SESSION Session_nie_sehen

# ingest-session 2026-09-19T13:17:28Z block-a-start lang=de
V Session_block_a_start kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-block-a-start.toon.md
V Focus_block_a_start kind=focus lang=de gloss="Interjektion 'na ja' wird getrennt geschrieben, ni" status=active
E Focus_block_a_start FROM_SESSION Session_block_a_start
V Lemma_de_fix_block_a_start kind=lemma lang=de surface="Genau, starten Sie mit A, na ja." role=minimal-rewrite
E Lemma_de_fix_block_a_start FROM_SESSION Session_block_a_start SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-block-a-start.toon.md
V Form_fix_block_a_start_0_na_ja kind=form lang=de surface="na ja" fixes=naja
E Form_fix_block_a_start_0_na_ja FROM_SESSION Session_block_a_start

# ingest-session 2026-09-19T13:20:28Z anweisungen lang=de
V Session_anweisungen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-anweisungen.toon.md
V Focus_anweisungen kind=focus lang=de gloss="Formelle Anrede: Possessivpronomen großschreiben —" status=active
E Focus_anweisungen FROM_SESSION Session_anweisungen
V Lemma_de_fix_anweisungen kind=lemma lang=de surface="Ich kann nur eine Markdown-Datei von Ihrer Antwort" role=minimal-rewrite
E Lemma_de_fix_anweisungen FROM_SESSION Session_anweisungen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-anweisungen.toon.md
V Form_fix_anweisungen_0_markdown_datei kind=form lang=de surface=Markdown-Datei fixes="markdown Datei"
E Form_fix_anweisungen_0_markdown_datei FROM_SESSION Session_anweisungen
V Form_fix_anweisungen_1_von_ihrer_antwort kind=form lang=de surface="von Ihrer Antwort" fixes="von ihrer Antwort"
E Form_fix_anweisungen_1_von_ihrer_antwort FROM_SESSION Session_anweisungen

# ingest-session 2026-09-19T13:23:16Z chat-sichtbarkeit lang=de
V Session_chat_sichtbarkeit kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-chat-sichtbarkeit.toon.md
V Focus_chat_sichtbarkeit kind=focus lang=de gloss="DE scaffold for the ZH complaint — eine Markdown-D" status=active
E Focus_chat_sichtbarkeit FROM_SESSION Session_chat_sichtbarkeit
V Lemma_de_fix_chat_sichtbarkeit kind=lemma lang=de surface="Sie geben nur eine Markdown-Datei aus, in der Antw" role=minimal-rewrite
E Lemma_de_fix_chat_sichtbarkeit FROM_SESSION Session_chat_sichtbarkeit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-chat-sichtbarkeit.toon.md

# ingest-session 2026-09-19T13:25:57Z self-contained-context lang=de
V Session_self_contained_context kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-self-contained-context.toon.md
V Focus_self_contained_context kind=focus lang=de gloss="Substantiviertes Adjektiv großschreiben — 'das Obi" status=active
E Focus_self_contained_context FROM_SESSION Session_self_contained_context
V Lemma_de_fix_self_contained_context kind=lemma lang=de surface="Ich kann das Obige nicht sehen — jede Antwort muss" role=minimal-rewrite
E Lemma_de_fix_self_contained_context FROM_SESSION Session_self_contained_context SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-self-contained-context.toon.md

# ingest-session 2026-09-19T13:29:29Z browser-dw lang=de
V Session_browser_dw kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-browser-dw.toon.md
V Focus_browser_dw kind=focus lang=de gloss="Du-Form regelmäßiges Verb: 'du öffnest', ohne -en " status=active
E Focus_browser_dw FROM_SESSION Session_browser_dw
V Lemma_de_fix_browser_dw kind=lemma lang=de surface="Ach so, die Ausgabe wurde von Qoder ausgeblendet —" role=minimal-rewrite
E Lemma_de_fix_browser_dw FROM_SESSION Session_browser_dw SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-browser-dw.toon.md
V Form_fix_browser_dw_0_ausgabe kind=form lang=de surface=Ausgabe fixes=Ausdruck
E Form_fix_browser_dw_0_ausgabe FROM_SESSION Session_browser_dw
V Form_fix_browser_dw_1_qoder kind=form lang=de surface=Qoder fixes=Qcoder
E Form_fix_browser_dw_1_qoder FROM_SESSION Session_browser_dw
V Form_fix_browser_dw_2_also_ffne_ich_du_ffnest kind=form lang=de surface="also öffne ich / du öffnest" fixes="so öffnenst du"
E Form_fix_browser_dw_2_also_ffne_ich_du_ffnest FROM_SESSION Session_browser_dw

# ingest-session 2026-09-19T13:31:03Z norm-langsamkeit lang=de
V Session_norm_langsamkeit kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-norm-langsamkeit.toon.md
V Focus_norm_langsamkeit kind=focus lang=de gloss="Negation nach Genus — Langsamkeit ist feminin: 'ke" status=active
E Focus_norm_langsamkeit FROM_SESSION Session_norm_langsamkeit
V Lemma_de_fix_norm_langsamkeit kind=lemma lang=de surface="Was? Langsam? Nein, normalerweise sprechen die Kol" role=minimal-rewrite
E Lemma_de_fix_norm_langsamkeit FROM_SESSION Session_norm_langsamkeit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-norm-langsamkeit.toon.md
V Form_fix_norm_langsamkeit_0_sprechen_die_koll kind=form lang=de surface="sprechen die Kollegen" fixes="sprechen Kollege"
E Form_fix_norm_langsamkeit_0_sprechen_die_koll FROM_SESSION Session_norm_langsamkeit
V Form_fix_norm_langsamkeit_1_keine_langsamkeit kind=form lang=de surface="keine Langsamkeit" fixes="kein Langsamkeit"
E Form_fix_norm_langsamkeit_1_keine_langsamkeit FROM_SESSION Session_norm_langsamkeit

# auto-gap 2026-09-19T13:33:00Z surface=取法乎上得乎中
V Concept_gap_zh_42d113ed82 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_42d113ed82 kind=gap lang=zh surface=取法乎上得乎中 target=de status=open
V Lemma_zh_zh_42d113ed82 kind=lemma lang=zh surface=取法乎上得乎中
E Concept_gap_zh_42d113ed82 EXPRESSES Lemma_zh_zh_42d113ed82 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_42d113ed82 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_42d113ed82 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-19T13:34:15Z c1-hoerverstehen lang=de
V Session_c1_hoerverstehen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-c1-hoerverstehen.toon.md
V Focus_c1_hoerverstehen kind=focus lang=de gloss="Possessiv nach Genus — das Hörverstehen ist Neutru" status=active
E Focus_c1_hoerverstehen FROM_SESSION Session_c1_hoerverstehen
V Lemma_de_fix_c1_hoerverstehen kind=lemma lang=de surface="Wissen Sie 取法乎上，得乎中？ Mein Hörverstehen auf B2 ist " role=minimal-rewrite
E Lemma_de_fix_c1_hoerverstehen FROM_SESSION Session_c1_hoerverstehen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-c1-hoerverstehen.toon.md
V Form_fix_c1_hoerverstehen_0_mein_h_rverstehen kind=form lang=de surface="Mein Hörverstehen" fixes="Meine Hörverstehen"
E Form_fix_c1_hoerverstehen_0_mein_h_rverstehen FROM_SESSION Session_c1_hoerverstehen
V Form_fix_c1_hoerverstehen_1_also_machen_wir_c kind=form lang=de surface="also machen wir C1, wenn" fixes="so machen Sie C1 wenn"
E Form_fix_c1_hoerverstehen_1_also_machen_wir_c FROM_SESSION Session_c1_hoerverstehen

# ingest-session 2026-09-19T13:36:21Z fest-zu-laut lang=de
V Session_fest_zu_laut kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-fest-zu-laut.toon.md
V Focus_fest_zu_laut kind=focus lang=de gloss="Ort: 'auf dem Oktoberfest' (auf + Dat.), nicht 'be" status=active
E Focus_fest_zu_laut FROM_SESSION Session_fest_zu_laut
V Lemma_de_fix_fest_zu_laut kind=lemma lang=de surface="Verdammt, auf dem Oktoberfest ist es viel zu laut " role=minimal-rewrite
E Lemma_de_fix_fest_zu_laut FROM_SESSION Session_fest_zu_laut SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-fest-zu-laut.toon.md
V Form_fix_fest_zu_laut_0_auf_dem_oktoberfest_b kind=form lang=de surface="auf dem Oktoberfest / beim Oktoberfest" fixes="bei Oktoberfest"
E Form_fix_fest_zu_laut_0_auf_dem_oktoberfest_b FROM_SESSION Session_fest_zu_laut
V Form_fix_fest_zu_laut_1_die_lautst_rke_ist_zu kind=form lang=de surface="die Lautstärke ist zu hoch" fixes="zu viel Lautstärke"
E Form_fix_fest_zu_laut_1_die_lautst_rke_ist_zu FROM_SESSION Session_fest_zu_laut

# ingest-session 2026-09-19T13:39:25Z alternative-jetzt lang=de
V Session_alternative_jetzt kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-alternative-jetzt.toon.md
V Focus_alternative_jetzt kind=focus lang=de gloss="'als Alternative' (Substantiv, f., -e) vs. 'altern" status=active
E Focus_alternative_jetzt FROM_SESSION Session_alternative_jetzt
V Lemma_de_fix_alternative_jetzt kind=lemma lang=de surface="Was soll ich jetzt als Alternative tun?" role=minimal-rewrite
E Lemma_de_fix_alternative_jetzt FROM_SESSION Session_alternative_jetzt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-alternative-jetzt.toon.md
V Form_fix_alternative_jetzt_0_was_soll_ich_jet kind=form lang=de surface="was soll ich jetzt tun" fixes="was soll ich tun jetzt"
E Form_fix_alternative_jetzt_0_was_soll_ich_jet FROM_SESSION Session_alternative_jetzt
V Form_fix_alternative_jetzt_1_als_alternative kind=form lang=de surface="als Alternative" fixes="als Alternativ"
E Form_fix_alternative_jetzt_1_als_alternative FROM_SESSION Session_alternative_jetzt

# ingest-session 2026-09-19T13:49:50Z pause-eine lang=de
V Session_pause_eine kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-pause-eine.toon.md
V Focus_pause_eine kind=focus lang=de gloss="Genus: die Pause (f.) → 'ich mache eine Pause', ni" status=active
E Focus_pause_eine FROM_SESSION Session_pause_eine
V Lemma_de_fix_pause_eine kind=lemma lang=de surface="Ich lese jetzt und speichere den Artikel als Lesez" role=minimal-rewrite
E Lemma_de_fix_pause_eine FROM_SESSION Session_pause_eine SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-pause-eine.toon.md
V Form_fix_pause_eine_0_und_ich_speichere_es_al kind=form lang=de surface="und ich speichere es als Lesezeichen" fixes="und bookmark"
E Form_fix_pause_eine_0_und_ich_speichere_es_al FROM_SESSION Session_pause_eine
V Form_fix_pause_eine_1_eine_pause kind=form lang=de surface="eine Pause" fixes="einen Pause"
E Form_fix_pause_eine_1_eine_pause FROM_SESSION Session_pause_eine

# ingest-session 2026-09-19T13:54:37Z pause-minuten lang=de
V Session_pause_minuten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-pause-minuten.toon.md
V Focus_pause_minuten kind=focus lang=de gloss="sich ausruhen (Reflexivverb: mich + Infinitiv)" status=active
E Focus_pause_minuten FROM_SESSION Session_pause_minuten
V Lemma_de_fix_pause_minuten kind=lemma lang=de surface="Wie viele Minuten soll ich mich ausruhen?" role=minimal-rewrite
E Lemma_de_fix_pause_minuten FROM_SESSION Session_pause_minuten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-pause-minuten.toon.md

# ingest-session 2026-09-19T14:02:01Z axiome-system lang=de
V Session_axiome_system kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-axiome-system.toon.md
V Focus_axiome_system kind=focus lang=de gloss="dafuer (Pronominaladverb) + das System (Neutrum)" status=active
E Focus_axiome_system FROM_SESSION Session_axiome_system
V Lemma_de_fix_axiome_system kind=lemma lang=de surface="Kurzer Exkurs: Ich will Mathematik-Faehigkeiten er" role=minimal-rewrite
E Lemma_de_fix_axiome_system FROM_SESSION Session_axiome_system SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-axiome-system.toon.md

# ingest-session 2026-09-19T14:05:13Z axiome-system-voll lang=de
V Session_axiome_system_voll kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-axiome-system-voll.toon.md
V Focus_axiome_system_voll kind=focus lang=de gloss="LaTeX-Formeln (die Formel, Plural Formeln - nicht " status=active
E Focus_axiome_system_voll FROM_SESSION Session_axiome_system_voll
V Lemma_de_fix_axiome_system_voll kind=lemma lang=de surface="Nein, nicht so einfach - inklusive LaTeX-Formeln, " role=minimal-rewrite
E Lemma_de_fix_axiome_system_voll FROM_SESSION Session_axiome_system_voll SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-axiome-system-voll.toon.md

# ingest-session 2026-09-19T14:10:00Z mathe-ziel-astro lang=de
V Session_mathe_ziel_astro kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-mathe-ziel-astro.toon.md
V Focus_mathe_ziel_astro kind=focus lang=de gloss="mit dem Ziel (das Ziel, Neutrum; mit + Dativ)" status=active
E Focus_mathe_ziel_astro FROM_SESSION Session_mathe_ziel_astro
V Lemma_de_fix_mathe_ziel_astro kind=lemma lang=de surface="Ja, genau - Mathematik mit dem Ziel Astrophysik." role=minimal-rewrite
E Lemma_de_fix_mathe_ziel_astro FROM_SESSION Session_mathe_ziel_astro SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-mathe-ziel-astro.toon.md

# ingest-session 2026-09-19T14:34:34Z zweite-lesung-akku lang=de
V Session_zweite_lesung_akku kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-zweite-lesung-akku.toon.md
V Focus_zweite_lesung_akku kind=focus lang=de gloss="1-2 Mal (adverbiales Mal ohne -s)" status=active
E Focus_zweite_lesung_akku FROM_SESSION Session_zweite_lesung_akku
V Lemma_de_fix_zweite_lesung_akku kind=lemma lang=de surface="Nach 20 Minuten Ausruhen habe ich den Artikel einm" role=minimal-rewrite
E Lemma_de_fix_zweite_lesung_akku FROM_SESSION Session_zweite_lesung_akku SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-zweite-lesung-akku.toon.md

# ingest-session 2026-09-19T14:37:17Z dsb-couverture-cerveau lang=de
V Session_dsb_couverture_cerveau kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dsb-couverture-cerveau.toon.md
V Focus_dsb_couverture_cerveau kind=focus lang=de gloss="la couverture du cerveau (de + le = du)" status=active
E Focus_dsb_couverture_cerveau FROM_SESSION Session_dsb_couverture_cerveau
V Lemma_de_fix_dsb_couverture_cerveau kind=lemma lang=de surface="DSB bedeutet bei mir 'la couverture du cerveau' - " role=minimal-rewrite
E Lemma_de_fix_dsb_couverture_cerveau FROM_SESSION Session_dsb_couverture_cerveau SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dsb-couverture-cerveau.toon.md

# ingest-session 2026-09-19T14:42:29Z dsb-neudefinition lang=de
V Session_dsb_neudefinition kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dsb-neudefinition.toon.md
V Focus_dsb_neudefinition kind=focus lang=de gloss="V2 - Beim DSB bedeutet es... (Verb auf Platz 2)" status=active
E Focus_dsb_neudefinition FROM_SESSION Session_dsb_neudefinition
V Lemma_de_fix_dsb_neudefinition kind=lemma lang=de surface="Beim DSB bedeutet es doch etwas anders: DNA, Doppe" role=minimal-rewrite
E Lemma_de_fix_dsb_neudefinition FROM_SESSION Session_dsb_neudefinition SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dsb-neudefinition.toon.md

# ingest-session 2026-09-19T14:48:12Z dns-zurueck-lesen lang=de
V Session_dns_zurueck_lesen kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dns-zurueck-lesen.toon.md
V Focus_dns_zurueck_lesen kind=focus lang=de gloss="Verbklammer bei trennbarem Verb (kehren ... zuruec" status=active
E Focus_dns_zurueck_lesen FROM_SESSION Session_dns_zurueck_lesen
V Lemma_de_fix_dns_zurueck_lesen kind=lemma lang=de surface="Genau so benutze ich DNS, ja. Dann kehren wir zum " role=minimal-rewrite
E Lemma_de_fix_dns_zurueck_lesen FROM_SESSION Session_dns_zurueck_lesen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-dns-zurueck-lesen.toon.md

# ingest-session 2026-09-19T15:12:20Z news-url-verloren lang=de
V Session_news_url_verloren kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-news-url-verloren.toon.md
V Focus_news_url_verloren kind=focus lang=de gloss="die URL (feminin)" status=active
E Focus_news_url_verloren FROM_SESSION Session_news_url_verloren
V Lemma_de_fix_news_url_verloren kind=lemma lang=de surface="Gib mir noch einmal die URL, ich habe ihn verloren" role=minimal-rewrite
E Lemma_de_fix_news_url_verloren FROM_SESSION Session_news_url_verloren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-news-url-verloren.toon.md

# ingest-session 2026-09-19T15:14:03Z oben-existiert-nicht lang=de
V Session_oben_existiert_nicht kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-oben-existiert-nicht.toon.md
V Focus_oben_existiert_nicht kind=focus lang=de gloss="es als Formal-Subjekt (es gibt...)" status=active
E Focus_oben_existiert_nicht FROM_SESSION Session_oben_existiert_nicht
V Lemma_de_fix_oben_existiert_nicht kind=lemma lang=de surface="Es gibt hier kein Oben. / Ich sehe das Oben nicht." role=minimal-rewrite
E Lemma_de_fix_oben_existiert_nicht FROM_SESSION Session_oben_existiert_nicht SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-oben-existiert-nicht.toon.md

# ingest-session 2026-09-19T16:01:44Z zusammenfassung-politik lang=de
V Session_zusammenfassung_politik kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-zusammenfassung-politik.toon.md
V Focus_zusammenfassung_politik kind=focus lang=de gloss="hat die SPD gesiegt — gesiegt/gewonnen ≠ besiegelt" status=active
E Focus_zusammenfassung_politik FROM_SESSION Session_zusammenfassung_politik
V Lemma_de_fix_zusammenfassung_politik kind=lemma lang=de surface=|- role=minimal-rewrite
E Lemma_de_fix_zusammenfassung_politik FROM_SESSION Session_zusammenfassung_politik SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-zusammenfassung-politik.toon.md
V Form_fix_zusammenfassung_politik_0_mecklenbur kind=form lang=de surface=Mecklenburg-Vorpommern fixes="Mecklenburg Vorpommern"
E Form_fix_zusammenfassung_politik_0_mecklenbur FROM_SESSION Session_zusammenfassung_politik
V Form_fix_zusammenfassung_politik_1_hat_die_sp kind=form lang=de surface="hat die SPD gesiegt/gewonnen" fixes="hat SPD besiegelt"
E Form_fix_zusammenfassung_politik_1_hat_die_sp FROM_SESSION Session_zusammenfassung_politik
V Form_fix_zusammenfassung_politik_2_der_amtier kind=form lang=de surface="der amtierende Kanzler schneidet sehr sc" fixes="die vor vorhanden Kanzler sehr"
E Form_fix_zusammenfassung_politik_2_der_amtier FROM_SESSION Session_zusammenfassung_politik
V Form_fix_zusammenfassung_politik_3_dem_wissen kind=form lang=de surface="dem Wissensgraph hinzu" fixes="zur Kenntnis-graph hinzu"
E Form_fix_zusammenfassung_politik_3_dem_wissen FROM_SESSION Session_zusammenfassung_politik
V Form_fix_zusammenfassung_politik_4_mir_fehlen kind=form lang=de surface="mir fehlen strukturierte Kenntnisse" fixes="bei mir fehlt es strukturierte"
E Form_fix_zusammenfassung_politik_4_mir_fehlen FROM_SESSION Session_zusammenfassung_politik

# ingest-session 2026-09-19T16:17:17Z exemplar-zusammenfassung lang=de
V Session_exemplar_zusammenfassung kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-exemplar-zusammenfassung.toon.md
V Focus_exemplar_zusammenfassung kind=focus lang=de gloss="exemplarisch ≠ Beispiel — beide zusammen ist Doppe" status=active
E Focus_exemplar_zusammenfassung FROM_SESSION Session_exemplar_zusammenfassung
V Lemma_de_fix_exemplar_zusammenfassung kind=lemma lang=de surface="Wie wäre eine exemplarische Antwort für die Zusamm" role=minimal-rewrite
E Lemma_de_fix_exemplar_zusammenfassung FROM_SESSION Session_exemplar_zusammenfassung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-exemplar-zusammenfassung.toon.md
V Form_fix_exemplar_zusammenfassung_0_eine_exem kind=form lang=de surface="eine exemplarische Antwort" fixes="die Exemplarische Beispiel Ant"
E Form_fix_exemplar_zusammenfassung_0_eine_exem FROM_SESSION Session_exemplar_zusammenfassung
V Form_fix_exemplar_zusammenfassung_1_f_r_die_z kind=form lang=de surface="für die Zusammenfassung" fixes="für Zusammenfassung"
E Form_fix_exemplar_zusammenfassung_1_f_r_die_z FROM_SESSION Session_exemplar_zusammenfassung
V Form_fix_exemplar_zusammenfassung_2_wie_w_re_ kind=form lang=de surface="Wie wäre" fixes="So wie wäre"
E Form_fix_exemplar_zusammenfassung_2_wie_w_re_ FROM_SESSION Session_exemplar_zusammenfassung

# auto-gap 2026-09-19T16:30:40Z surface=德语助手
V Concept_gap_zh_f9099b93c1 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_f9099b93c1 kind=gap lang=zh surface=德语助手 target=de status=open
V Lemma_zh_zh_f9099b93c1 kind=lemma lang=zh surface=德语助手
E Concept_gap_zh_f9099b93c1 EXPRESSES Lemma_zh_zh_f9099b93c1 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_f9099b93c1 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_f9099b93c1 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-19T16:31:06Z wortschatz-warten lang=de
V Session_wortschatz_warten kind=session date=2026-09-19 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-wortschatz-warten.toon.md
V Focus_wortschatz_warten kind=focus lang=de gloss="warten auf + Akkusativ — wartest du auf mich, nich" status=active
E Focus_wortschatz_warten FROM_SESSION Session_wortschatz_warten
V Lemma_de_fix_wortschatz_warten kind=lemma lang=de surface="Damit ist Modul 1 geschafft. Jetzt mache ich die W" role=minimal-rewrite
E Lemma_de_fix_wortschatz_warten FROM_SESSION Session_wortschatz_warten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-19-wortschatz-warten.toon.md
V Form_fix_wortschatz_warten_0_wartest_du_auf_m kind=form lang=de surface="wartest du auf mich" fixes="wartst du mich"
E Form_fix_wortschatz_warten_0_wartest_du_auf_m FROM_SESSION Session_wortschatz_warten
V Form_fix_wortschatz_warten_1_ist_modul_1_gesc kind=form lang=de surface="ist Modul 1 geschafft / damit ist Modul " fixes="geht Modul 1 vorbei"
E Form_fix_wortschatz_warten_1_ist_modul_1_gesc FROM_SESSION Session_wortschatz_warten
V Form_fix_wortschatz_warten_2_die_wortschatz_b kind=form lang=de surface="die Wortschatzübung" fixes="Wortschatz Übung"
E Form_fix_wortschatz_warten_2_die_wortschatz_b FROM_SESSION Session_wortschatz_warten
V Form_fix_wortschatz_warten_3_bis_ich_fertig_b kind=form lang=de surface="bis ich fertig bin" fixes="bis zum Ende meiner Übung"
E Form_fix_wortschatz_warten_3_bis_ich_fertig_b FROM_SESSION Session_wortschatz_warten

# ingest-session 2026-09-20T22:26:50Z setze-die-shenyou-fort lang=de
V Session_setze_die_shenyou_fort kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-setze-die-shenyou-fort.toon.md
V Focus_setze_die_shenyou_fort kind=focus lang=de gloss="Setze … fort + Akk. (trennbares Verb fortsetzen, d" status=active
E Focus_setze_die_shenyou_fort FROM_SESSION Session_setze_die_shenyou_fort
V Lemma_de_fix_setze_die_shenyou_fort kind=lemma lang=de surface="Setze die 神游 fort." role=minimal-rewrite
E Lemma_de_fix_setze_die_shenyou_fort FROM_SESSION Session_setze_die_shenyou_fort SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-setze-die-shenyou-fort.toon.md
V Form_fix_setze_die_shenyou_fort_0_setze_die_f kind=form lang=de surface="Setze die 神游 fort." fixes=继续神游
E Form_fix_setze_die_shenyou_fort_0_setze_die_f FROM_SESSION Session_setze_die_shenyou_fort

# ingest-session 2026-09-21T19:07:25Z wie-macht-man-das-noch-mal lang=de
V Session_wie_macht_man_das_noch_mal kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-wie-macht-man-das-noch-mal.toon.md
V Focus_wie_macht_man_das_noch_mal kind=focus lang=de gloss="Wie macht man das noch mal? (unpersönliches man + " status=active
E Focus_wie_macht_man_das_noch_mal FROM_SESSION Session_wie_macht_man_das_noch_mal
V Lemma_de_fix_wie_macht_man_das_noch_mal kind=lemma lang=de surface="Gut. Ich möchte ein Video machen — «Dein Mut ist w" role=minimal-rewrite
E Lemma_de_fix_wie_macht_man_das_noch_mal FROM_SESSION Session_wie_macht_man_das_noch_mal SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-wie-macht-man-das-noch-mal.toon.md
V Form_fix_wie_macht_man_das_noch_mal_0_wie_mac kind=form lang=de surface="Wie macht man das noch mal?" fixes=这些怎么做来着
E Form_fix_wie_macht_man_das_noch_mal_0_wie_mac FROM_SESSION Session_wie_macht_man_das_noch_mal

# ingest-session 2026-09-21T19:20:23Z die-dateien-sind-bereit lang=de
V Session_die_dateien_sind_bereit kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-die-dateien-sind-bereit.toon.md
V Focus_die_dateien_sind_bereit kind=focus lang=de gloss="Wie macht man das noch mal? (unpersönliches man — " status=active
E Focus_die_dateien_sind_bereit FROM_SESSION Session_die_dateien_sind_bereit
V Lemma_de_fix_die_dateien_sind_bereit kind=lemma lang=de surface="face.png, huaqiang.mp4 und xishuashua.mp3 sind ber" role=minimal-rewrite
E Lemma_de_fix_die_dateien_sind_bereit FROM_SESSION Session_die_dateien_sind_bereit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-die-dateien-sind-bereit.toon.md
V Form_fix_die_dateien_sind_bereit_0_die_dateie kind=form lang=de surface="Die Dateien sind bereit." fixes=备好了
E Form_fix_die_dateien_sind_bereit_0_die_dateie FROM_SESSION Session_die_dateien_sind_bereit

# ingest-session 2026-09-21T19:32:47Z ersetze-huaqiang-durch-das-pummelige lang=de
V Session_ersetze_huaqiang_durch_das_pummelige kind=session date=2026-09-21 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-ersetze-huaqiang-durch-das-pummelige.toon.md
V Focus_ersetze_huaqiang_durch_das_pummelige kind=focus lang=de gloss="ersetze X durch Y (ersetzen + Akk + durch + Akk)" status=active
E Focus_ersetze_huaqiang_durch_das_pummelige FROM_SESSION Session_ersetze_huaqiang_durch_das_pummelige
V Lemma_de_fix_ersetze_huaqiang_durch_das_pummelige kind=lemma lang=de surface="So ist das nicht besonders explosiv. Man braucht f" role=minimal-rewrite
E Lemma_de_fix_ersetze_huaqiang_durch_das_pummelige FROM_SESSION Session_ersetze_huaqiang_durch_das_pummelige SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-21-ersetze-huaqiang-durch-das-pummelige.toon.md
V Form_fix_ersetze_huaqiang_durch_das_pummelige kind=form lang=de surface="Ersetze Huaqiang durch das Pummelige." fixes=把这个肥嘟嘟的东西替换华强
E Form_fix_ersetze_huaqiang_durch_das_pummelige FROM_SESSION Session_ersetze_huaqiang_durch_das_pummelige

# ingest-session 2026-09-22T09:05:32Z nimm-die-shenyou-in-den-takt lang=de
V Session_nimm_die_shenyou_in_den_takt kind=session date=2026-09-22 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-22-nimm-die-shenyou-in-den-takt.toon.md
V Focus_nimm_die_shenyou_in_den_takt kind=focus lang=de gloss="in + Akk (Nimm … in den … auf)" status=active
E Focus_nimm_die_shenyou_in_den_takt FROM_SESSION Session_nimm_die_shenyou_in_den_takt
V Lemma_de_fix_nimm_die_shenyou_in_den_takt kind=lemma lang=de surface="Nimm die 神游 in den 20-Minuten-Takt auf." role=minimal-rewrite
E Lemma_de_fix_nimm_die_shenyou_in_den_takt FROM_SESSION Session_nimm_die_shenyou_in_den_takt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-22-nimm-die-shenyou-in-den-takt.toon.md
V Form_fix_nimm_die_shenyou_in_den_takt_0_nimm_ kind=form lang=de surface="Nimm die 神游 in den 20-Minuten-Takt auf." fixes=开始神游
E Form_fix_nimm_die_shenyou_in_den_takt_0_nimm_ FROM_SESSION Session_nimm_die_shenyou_in_den_takt

# ingest-session 2026-09-22T10:23:13Z die-gesangsstimme-ersetzen lang=de
V Session_die_gesangsstimme_ersetzen kind=session date=2026-09-22 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-22-die-gesangsstimme-ersetzen.toon.md
V Focus_die_gesangsstimme_ersetzen kind=focus lang=de gloss="ersetze X durch Y / die Gesangsstimme ersetzen" status=active
E Focus_die_gesangsstimme_ersetzen FROM_SESSION Session_die_gesangsstimme_ersetzen
V Lemma_de_fix_die_gesangsstimme_ersetzen kind=lemma lang=de surface="Der Ton fehlt — und er klingt seltsam. Ich will di" role=minimal-rewrite
E Lemma_de_fix_die_gesangsstimme_ersetzen FROM_SESSION Session_die_gesangsstimme_ersetzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-22-die-gesangsstimme-ersetzen.toon.md
V Form_fix_die_gesangsstimme_ersetzen_0_ersetze kind=form lang=de surface="Ersetze die Gesangsstimme." fixes=唱歌声音替换
E Form_fix_die_gesangsstimme_ersetzen_0_ersetze FROM_SESSION Session_die_gesangsstimme_ersetzen
V Form_fix_die_gesangsstimme_ersetzen_1_das_ges kind=form lang=de surface="Das Gesicht ist kein Aufkleber." fixes=脸不是贴图贴上去
E Form_fix_die_gesangsstimme_ersetzen_1_das_ges FROM_SESSION Session_die_gesangsstimme_ersetzen

# ingest-session 2026-09-23T14:08:56Z raeume-tmp-auf lang=de
V Session_raeume_tmp_auf kind=session date=2026-09-23 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-23-raeume-tmp-auf.toon.md
V Focus_raeume_tmp_auf kind=focus lang=de gloss="an + Dat (body region) / Druckschmerz" status=active
E Focus_raeume_tmp_auf FROM_SESSION Session_raeume_tmp_auf
V Lemma_de_fix_raeume_tmp_auf kind=lemma lang=de surface="Gut. Räume tmp auf und ordne das Projekt. Heute is" role=minimal-rewrite
E Lemma_de_fix_raeume_tmp_auf FROM_SESSION Session_raeume_tmp_auf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-23-raeume-tmp-auf.toon.md
V Form_fix_raeume_tmp_auf_0_an_der_rechten_skap kind=form lang=de surface="an der rechten Skapula" fixes=右边scapular开始酸痛
E Form_fix_raeume_tmp_auf_0_an_der_rechten_skap FROM_SESSION Session_raeume_tmp_auf
V Form_fix_raeume_tmp_auf_1_deutlicher_drucksch kind=form lang=de surface="deutlicher Druckschmerz" fixes=有明显压痛
E Form_fix_raeume_tmp_auf_1_deutlicher_drucksch FROM_SESSION Session_raeume_tmp_auf

# ingest-session 2026-09-23T14:13:29Z zuerst-fangen-wir-an lang=de
V Session_zuerst_fangen_wir_an kind=session date=2026-09-23 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-23-zuerst-fangen-wir-an.toon.md
V Focus_zuerst_fangen_wir_an kind=focus lang=de gloss="anfangen + zu-Infinitiv / Spanisch (Sprache) nicht" status=active
E Focus_zuerst_fangen_wir_an FROM_SESSION Session_zuerst_fangen_wir_an
V Lemma_de_fix_zuerst_fangen_wir_an kind=lemma lang=de surface="Also gut. Zuerst fangen wir einfach an, Spanisch z" role=minimal-rewrite
E Lemma_de_fix_zuerst_fangen_wir_an FROM_SESSION Session_zuerst_fangen_wir_an SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-23-zuerst-fangen-wir-an.toon.md
V Form_fix_zuerst_fangen_wir_an_0_fangen_wir_an kind=form lang=de surface="fangen wir an" fixes="starten wir an"
E Form_fix_zuerst_fangen_wir_an_0_fangen_wir_an FROM_SESSION Session_zuerst_fangen_wir_an
V Form_fix_zuerst_fangen_wir_an_1_spanisch_zu_l kind=form lang=de surface="Spanisch zu lernen" fixes="Spanien zu lernen"
E Form_fix_zuerst_fangen_wir_an_1_spanisch_zu_l FROM_SESSION Session_zuerst_fangen_wir_an

# ingest-session 2026-09-24T11:54:36Z mit-dem-neuen-tag lang=de
V Session_mit_dem_neuen_tag kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-mit-dem-neuen-tag.toon.md
V Focus_mit_dem_neuen_tag kind=focus lang=de gloss="schwache Deklination Dat. Sg. / mit dem neuen Tag" status=active
E Focus_mit_dem_neuen_tag FROM_SESSION Session_mit_dem_neuen_tag
V Lemma_de_fix_mit_dem_neuen_tag kind=lemma lang=de surface="So, jetzt ist es der 24.9.2026, 14:00 Uhr. Ich bin" role=minimal-rewrite
E Lemma_de_fix_mit_dem_neuen_tag FROM_SESSION Session_mit_dem_neuen_tag SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-mit-dem-neuen-tag.toon.md
V Form_fix_mit_dem_neuen_tag_0_mit_dem_neuen_ta kind=form lang=de surface="mit dem neuen Tag" fixes="mit dem neues Tag"
E Form_fix_mit_dem_neuen_tag_0_mit_dem_neuen_ta FROM_SESSION Session_mit_dem_neuen_tag
V Form_fix_mit_dem_neuen_tag_1_planen kind=form lang=de surface=planen fixes=plannen
E Form_fix_mit_dem_neuen_tag_1_planen FROM_SESSION Session_mit_dem_neuen_tag
V Form_fix_mit_dem_neuen_tag_2_biologisch_willi kind=form lang=de surface="biologisch williger" fixes="biologisch einwilliger"
E Form_fix_mit_dem_neuen_tag_2_biologisch_willi FROM_SESSION Session_mit_dem_neuen_tag

# ingest-session 2026-09-24T11:56:59Z die-3d-hall-anschauen lang=de
V Session_die_3d_hall_anschauen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-die-3d-hall-anschauen.toon.md
V Focus_die_3d_hall_anschauen kind=focus lang=de gloss="im Augenblick / hätte gern + anschauen" status=active
E Focus_die_3d_hall_anschauen FROM_SESSION Session_die_3d_hall_anschauen
V Lemma_de_fix_die_3d_hall_anschauen kind=lemma lang=de surface="So, ich hätte gern im Augenblick die 3D-Hall anges" role=minimal-rewrite
E Lemma_de_fix_die_3d_hall_anschauen FROM_SESSION Session_die_3d_hall_anschauen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-die-3d-hall-anschauen.toon.md
V Form_fix_die_3d_hall_anschauen_0_im_augenblic kind=form lang=de surface="im Augenblick" fixes=augenblick
E Form_fix_die_3d_hall_anschauen_0_im_augenblic FROM_SESSION Session_die_3d_hall_anschauen
V Form_fix_die_3d_hall_anschauen_1_die_3d_hall_ kind=form lang=de surface="die 3D-Hall anschauen" fixes="zum 3D Hall einschauen"
E Form_fix_die_3d_hall_anschauen_1_die_3d_hall_ FROM_SESSION Session_die_3d_hall_anschauen

# ingest-session 2026-09-24T12:05:01Z in-meiner-linken-skapula lang=de
V Session_in_meiner_linken_skapula kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-meiner-linken-skapula.toon.md
V Focus_in_meiner_linken_skapula kind=focus lang=de gloss="in + Dat / in meiner linken Skapula" status=active
E Focus_in_meiner_linken_skapula FROM_SESSION Session_in_meiner_linken_skapula
V Lemma_de_fix_in_meiner_linken_skapula kind=lemma lang=de surface="Ach so, ich bin gerade dabei, zuerst Ibuprofen zu " role=minimal-rewrite
E Lemma_de_fix_in_meiner_linken_skapula FROM_SESSION Session_in_meiner_linken_skapula SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-meiner-linken-skapula.toon.md
V Form_fix_in_meiner_linken_skapula_0_in_meiner kind=form lang=de surface="in meiner linken Skapula" fixes="im meine Linkskapula"
E Form_fix_in_meiner_linken_skapula_0_in_meiner FROM_SESSION Session_in_meiner_linken_skapula
V Form_fix_in_meiner_linken_skapula_1_nahrungse kind=form lang=de surface=Nahrungsergänzungsmittel fixes=Nährungsergänzungsmittel
E Form_fix_in_meiner_linken_skapula_1_nahrungse FROM_SESSION Session_in_meiner_linken_skapula
V Form_fix_in_meiner_linken_skapula_2_planen kind=form lang=de surface=planen fixes=plannen
E Form_fix_in_meiner_linken_skapula_2_planen FROM_SESSION Session_in_meiner_linken_skapula

# ingest-session 2026-09-24T12:08:47Z warum-sind-apfelessig-und-betain lang=de
V Session_warum_sind_apfelessig_und_betain kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-warum-sind-apfelessig-und-betain.toon.md
V Focus_warum_sind_apfelessig_und_betain kind=focus lang=de gloss="Pluralverb nach X und Y / sind … pausiert" status=active
E Focus_warum_sind_apfelessig_und_betain FROM_SESSION Session_warum_sind_apfelessig_und_betain
V Lemma_de_fix_warum_sind_apfelessig_und_betain kind=lemma lang=de surface="Warum sind Apfelessig und Betain heute noch pausie" role=minimal-rewrite
E Lemma_de_fix_warum_sind_apfelessig_und_betain FROM_SESSION Session_warum_sind_apfelessig_und_betain SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-warum-sind-apfelessig-und-betain.toon.md
V Form_fix_warum_sind_apfelessig_und_betain_0_w kind=form lang=de surface="Warum sind" fixes="Warum ist … und …"
E Form_fix_warum_sind_apfelessig_und_betain_0_w FROM_SESSION Session_warum_sind_apfelessig_und_betain
V Form_fix_warum_sind_apfelessig_und_betain_1_p kind=form lang=de surface=pausiert fixes=aufgehört
E Form_fix_warum_sind_apfelessig_und_betain_1_p FROM_SESSION Session_warum_sind_apfelessig_und_betain

# auto-gap 2026-09-24T12:11:19Z surface=脽
V Concept_gap_zh_a5ae0dc42f kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_a5ae0dc42f kind=gap lang=zh surface=脽 target=de status=open
V Lemma_zh_zh_a5ae0dc42f kind=lemma lang=zh surface=脽
E Concept_gap_zh_a5ae0dc42f EXPRESSES Lemma_zh_zh_a5ae0dc42f SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_a5ae0dc42f GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_a5ae0dc42f GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T12:12:28Z in-den-privaten-bereich lang=de
V Session_in_den_privaten_bereich kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-den-privaten-bereich.toon.md
V Focus_in_den_privaten_bereich kind=focus lang=de gloss="schwache Deklination / in den privaten Bereich" status=active
E Focus_in_den_privaten_bereich FROM_SESSION Session_in_den_privaten_bereich
V Lemma_de_fix_in_den_privaten_bereich kind=lemma lang=de surface="Also, vor dieser Sitzung zur Weisheitszahnentfernu" role=minimal-rewrite
E Lemma_de_fix_in_den_privaten_bereich FROM_SESSION Session_in_den_privaten_bereich SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-den-privaten-bereich.toon.md
V Form_fix_in_den_privaten_bereich_0_in_den_pri kind=form lang=de surface="in den privaten Bereich" fixes="private Bereich"
E Form_fix_in_den_privaten_bereich_0_in_den_pri FROM_SESSION Session_in_den_privaten_bereich
V Form_fix_in_den_privaten_bereich_1_weisheitsz kind=form lang=de surface=Weisheitszahnentfernung fixes="wakelter Zahnentfernung"
E Form_fix_in_den_privaten_bereich_1_weisheitsz FROM_SESSION Session_in_den_privaten_bereich
V Form_fix_in_den_privaten_bereich_2_physiologi kind=form lang=de surface=physiologische fixes=psysiologische
E Form_fix_in_den_privaten_bereich_2_physiologi FROM_SESSION Session_in_den_privaten_bereich

# ingest-session 2026-09-24T12:16:31Z sondern-von-einem-wackelnden lang=de
V Session_sondern_von_einem_wackelnden kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-sondern-von-einem-wackelnden.toon.md
V Focus_sondern_von_einem_wackelnden kind=focus lang=de gloss="sondern (nicht sonder)" status=active
E Focus_sondern_von_einem_wackelnden FROM_SESSION Session_sondern_von_einem_wackelnden
V Lemma_de_fix_sondern_von_einem_wackelnden kind=lemma lang=de surface="Der Widerstand gegen das Putzen stammt nicht von d" role=minimal-rewrite
E Lemma_de_fix_sondern_von_einem_wackelnden FROM_SESSION Session_sondern_von_einem_wackelnden SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-sondern-von-einem-wackelnden.toon.md
V Form_fix_sondern_von_einem_wackelnden_0_sonde kind=form lang=de surface=sondern fixes=sonder
E Form_fix_sondern_von_einem_wackelnden_0_sonde FROM_SESSION Session_sondern_von_einem_wackelnden
V Form_fix_sondern_von_einem_wackelnden_1_aphth kind=form lang=de surface=Aphthen fixes=Aphlete
E Form_fix_sondern_von_einem_wackelnden_1_aphth FROM_SESSION Session_sondern_von_einem_wackelnden
V Form_fix_sondern_von_einem_wackelnden_2_ein_w kind=form lang=de surface="ein wackelnder unterer Frontzahn" fixes="Wackelte vorne unten Zahn"
E Form_fix_sondern_von_einem_wackelnden_2_ein_w FROM_SESSION Session_sondern_von_einem_wackelnden

# ingest-session 2026-09-24T12:18:16Z kein-problem-mit-dem-weisheitszahn lang=de
V Session_kein_problem_mit_dem_weisheitszahn kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-kein-problem-mit-dem-weisheitszahn.toon.md
V Focus_kein_problem_mit_dem_weisheitszahn kind=focus lang=de gloss="kein Problem (Neutrum) / dem Weisheitszahn" status=active
E Focus_kein_problem_mit_dem_weisheitszahn FROM_SESSION Session_kein_problem_mit_dem_weisheitszahn
V Lemma_de_fix_kein_problem_mit_dem_weisheitszahn kind=lemma lang=de surface="Nein, es gibt kein Problem mit dem Weisheitszahn." role=minimal-rewrite
E Lemma_de_fix_kein_problem_mit_dem_weisheitszahn FROM_SESSION Session_kein_problem_mit_dem_weisheitszahn SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-kein-problem-mit-dem-weisheitszahn.toon.md
V Form_fix_kein_problem_mit_dem_weisheitszahn_0 kind=form lang=de surface="kein Problem" fixes="keine Problem"
E Form_fix_kein_problem_mit_dem_weisheitszahn_0 FROM_SESSION Session_kein_problem_mit_dem_weisheitszahn
V Form_fix_kein_problem_mit_dem_weisheitszahn_1 kind=form lang=de surface="dem Weisheitszahn" fixes=Weisheitzahn
E Form_fix_kein_problem_mit_dem_weisheitszahn_1 FROM_SESSION Session_kein_problem_mit_dem_weisheitszahn

# ingest-session 2026-09-24T12:20:18Z meine-gesamten-emails lang=de
V Session_meine_gesamten_emails kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-meine-gesamten-emails.toon.md
V Focus_meine_gesamten_emails kind=focus lang=de gloss="Sie-Anrede durchhalten / gesamten E-Mails" status=active
E Focus_meine_gesamten_emails FROM_SESSION Session_meine_gesamten_emails
V Lemma_de_fix_meine_gesamten_emails kind=lemma lang=de surface="Ach so, jetzt verarbeiten Sie meine E-Mails. Zeige" role=minimal-rewrite
E Lemma_de_fix_meine_gesamten_emails FROM_SESSION Session_meine_gesamten_emails SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-meine-gesamten-emails.toon.md
V Form_fix_meine_gesamten_emails_0_verarbeiten kind=form lang=de surface=verarbeiten fixes=prozessieren
E Form_fix_meine_gesamten_emails_0_verarbeiten FROM_SESSION Session_meine_gesamten_emails
V Form_fix_meine_gesamten_emails_1_zeigen_sie_m kind=form lang=de surface="zeigen Sie mir" fixes="zeigst du mir"
E Form_fix_meine_gesamten_emails_1_zeigen_sie_m FROM_SESSION Session_meine_gesamten_emails
V Form_fix_meine_gesamten_emails_2_gesamten_e_m kind=form lang=de surface="gesamten E-Mails" fixes="gesamtes Emails"
E Form_fix_meine_gesamten_emails_2_gesamten_e_m FROM_SESSION Session_meine_gesamten_emails

# ingest-session 2026-09-24T12:23:24Z nachrichten-aus-der-ganzen-welt lang=de
V Session_nachrichten_aus_der_ganzen_welt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nachrichten-aus-der-ganzen-welt.toon.md
V Focus_nachrichten_aus_der_ganzen_welt kind=focus lang=de gloss="neue Nachrichten / aus der ganzen Welt" status=active
E Focus_nachrichten_aus_der_ganzen_welt FROM_SESSION Session_nachrichten_aus_der_ganzen_welt
V Lemma_de_fix_nachrichten_aus_der_ganzen_welt kind=lemma lang=de surface="Gleichzeitig habe ich Lust, neue Nachrichten aus d" role=minimal-rewrite
E Lemma_de_fix_nachrichten_aus_der_ganzen_welt FROM_SESSION Session_nachrichten_aus_der_ganzen_welt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nachrichten-aus-der-ganzen-welt.toon.md
V Form_fix_nachrichten_aus_der_ganzen_welt_0_ne kind=form lang=de surface="neue Nachrichten" fixes="neues Nachricht"
E Form_fix_nachrichten_aus_der_ganzen_welt_0_ne FROM_SESSION Session_nachrichten_aus_der_ganzen_welt
V Form_fix_nachrichten_aus_der_ganzen_welt_1_au kind=form lang=de surface="aus der ganzen Welt" fixes="von ganzes Welt"
E Form_fix_nachrichten_aus_der_ganzen_welt_1_au FROM_SESSION Session_nachrichten_aus_der_ganzen_welt
V Form_fix_nachrichten_aus_der_ganzen_welt_2_in kind=form lang=de surface="in vielfältigen Sprachen" fixes="vielfätige Sprache"
E Form_fix_nachrichten_aus_der_ganzen_welt_2_in FROM_SESSION Session_nachrichten_aus_der_ganzen_welt

# ingest-session 2026-09-24T12:25:20Z nicht-so-langsam-beim-hoerverstehen lang=de
V Session_nicht_so_langsam_beim_hoerverstehen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nicht-so-langsam-beim-hoerverstehen.toon.md
V Focus_nicht_so_langsam_beim_hoerverstehen kind=focus lang=de gloss="beim Hörverstehen" status=active
E Focus_nicht_so_langsam_beim_hoerverstehen FROM_SESSION Session_nicht_so_langsam_beim_hoerverstehen
V Lemma_de_fix_nicht_so_langsam_beim_hoerverstehen kind=lemma lang=de surface="Ich hätte gern, dass es beim Hörverstehen nicht so" role=minimal-rewrite
E Lemma_de_fix_nicht_so_langsam_beim_hoerverstehen FROM_SESSION Session_nicht_so_langsam_beim_hoerverstehen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nicht-so-langsam-beim-hoerverstehen.toon.md
V Form_fix_nicht_so_langsam_beim_hoerverstehen_ kind=form lang=de surface="beim Hörverstehen" fixes="für Hörverstehen"
E Form_fix_nicht_so_langsam_beim_hoerverstehen_ FROM_SESSION Session_nicht_so_langsam_beim_hoerverstehen

# ingest-session 2026-09-24T12:31:11Z auswirkung-auf-meine-gesundheit lang=de
V Session_auswirkung_auf_meine_gesundheit kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-auswirkung-auf-meine-gesundheit.toon.md
V Focus_auswirkung_auf_meine_gesundheit kind=focus lang=de gloss="Auswirkung auf (nicht über)" status=active
E Focus_auswirkung_auf_meine_gesundheit FROM_SESSION Session_auswirkung_auf_meine_gesundheit
V Lemma_de_fix_auswirkung_auf_meine_gesundheit kind=lemma lang=de surface="Also, meine vorhandene kanonische Annahme der Nahr" role=minimal-rewrite
E Lemma_de_fix_auswirkung_auf_meine_gesundheit FROM_SESSION Session_auswirkung_auf_meine_gesundheit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-auswirkung-auf-meine-gesundheit.toon.md
V Form_fix_auswirkung_auf_meine_gesundheit_0_au kind=form lang=de surface="Auswirkung auf" fixes="Auswirkung über"
E Form_fix_auswirkung_auf_meine_gesundheit_0_au FROM_SESSION Session_auswirkung_auf_meine_gesundheit
V Form_fix_auswirkung_auf_meine_gesundheit_1_na kind=form lang=de surface=Nahrungsergänzungsmittel fixes=Nährungsergänzungsmittel
E Form_fix_auswirkung_auf_meine_gesundheit_1_na FROM_SESSION Session_auswirkung_auf_meine_gesundheit
V Form_fix_auswirkung_auf_meine_gesundheit_2_vo kind=form lang=de surface=vorhandene fixes=vorhande
E Form_fix_auswirkung_auf_meine_gesundheit_2_vo FROM_SESSION Session_auswirkung_auf_meine_gesundheit

# ingest-session 2026-09-24T12:36:05Z strengen-sie-sich-an lang=de
V Session_strengen_sie_sich_an kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-strengen-sie-sich-an.toon.md
V Focus_strengen_sie_sich_an kind=focus lang=de gloss="sich anstrengen (reflexiv)" status=active
E Focus_strengen_sie_sich_an FROM_SESSION Session_strengen_sie_sich_an
V Lemma_de_fix_strengen_sie_sich_an kind=lemma lang=de surface="Ach so, ich bin jetzt auf dem Weg, DW-Deutschlerne" role=minimal-rewrite
E Lemma_de_fix_strengen_sie_sich_an FROM_SESSION Session_strengen_sie_sich_an SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-strengen-sie-sich-an.toon.md
V Form_fix_strengen_sie_sich_an_0_strengen_sie_ kind=form lang=de surface="strengen Sie sich an" fixes="strengen Sie an"
E Form_fix_strengen_sie_sich_an_0_strengen_sie_ FROM_SESSION Session_strengen_sie_sich_an
V Form_fix_strengen_sie_sich_an_1_h_rverstehen_ kind=form lang=de surface=Hörverstehen-Übungen fixes=Hörverstehenübungen
E Form_fix_strengen_sie_sich_an_1_h_rverstehen_ FROM_SESSION Session_strengen_sie_sich_an

# ingest-session 2026-09-24T12:46:32Z die-entropie-ein-bisschen-mehr lang=de
V Session_die_entropie_ein_bisschen_mehr kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-die-entropie-ein-bisschen-mehr.toon.md
V Focus_die_entropie_ein_bisschen_mehr kind=focus lang=de gloss="die Entropie (f.) / der ganzen Struktur" status=active
E Focus_die_entropie_ein_bisschen_mehr FROM_SESSION Session_die_entropie_ein_bisschen_mehr
V Lemma_de_fix_die_entropie_ein_bisschen_mehr kind=lemma lang=de surface="Reduzieren Sie die Entropie ein bisschen mehr, bez" role=minimal-rewrite
E Lemma_de_fix_die_entropie_ein_bisschen_mehr FROM_SESSION Session_die_entropie_ein_bisschen_mehr SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-die-entropie-ein-bisschen-mehr.toon.md
V Form_fix_die_entropie_ein_bisschen_mehr_0_die kind=form lang=de surface="die Entropie" fixes="den Entropie"
E Form_fix_die_entropie_ein_bisschen_mehr_0_die FROM_SESSION Session_die_entropie_ein_bisschen_mehr
V Form_fix_die_entropie_ein_bisschen_mehr_1_der kind=form lang=de surface="der ganzen Struktur" fixes="der Ganze struktur"
E Form_fix_die_entropie_ein_bisschen_mehr_1_der FROM_SESSION Session_die_entropie_ein_bisschen_mehr

# ingest-session 2026-09-24T13:18:04Z eine-beilage-zu-taetigkeiten lang=de
V Session_eine_beilage_zu_taetigkeiten kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-eine-beilage-zu-taetigkeiten.toon.md
V Focus_eine_beilage_zu_taetigkeiten kind=focus lang=de gloss="dass es eine Beilage gibt" status=active
E Focus_eine_beilage_zu_taetigkeiten FROM_SESSION Session_eine_beilage_zu_taetigkeiten
V Lemma_de_fix_eine_beilage_zu_taetigkeiten kind=lemma lang=de surface="Ich mache jetzt DW-Übungen mit Manuskript und Lück" role=minimal-rewrite
E Lemma_de_fix_eine_beilage_zu_taetigkeiten FROM_SESSION Session_eine_beilage_zu_taetigkeiten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-eine-beilage-zu-taetigkeiten.toon.md
V Form_fix_eine_beilage_zu_taetigkeiten_0_dass_ kind=form lang=de surface="dass es eine Beilage gibt" fixes="dass es gibt ein Musik"
E Form_fix_eine_beilage_zu_taetigkeiten_0_dass_ FROM_SESSION Session_eine_beilage_zu_taetigkeiten
V Form_fix_eine_beilage_zu_taetigkeiten_1_l_cke kind=form lang=de surface=Lückenübungen fixes=Lückeübungen
E Form_fix_eine_beilage_zu_taetigkeiten_1_l_cke FROM_SESSION Session_eine_beilage_zu_taetigkeiten
V Form_fix_eine_beilage_zu_taetigkeiten_2_empfe kind=form lang=de surface=Empfehlung fixes=Empfelhung
E Form_fix_eine_beilage_zu_taetigkeiten_2_empfe FROM_SESSION Session_eine_beilage_zu_taetigkeiten

# ingest-session 2026-09-24T13:18:27Z wechat-desktop-in-mein-system lang=de
V Session_wechat_desktop_in_mein_system kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-wechat-desktop-in-mein-system.toon.md
V Focus_wechat_desktop_in_mein_system kind=focus lang=de gloss="in + Akk (in mein System)" status=active
E Focus_wechat_desktop_in_mein_system FROM_SESSION Session_wechat_desktop_in_mein_system
V Lemma_de_fix_wechat_desktop_in_mein_system kind=lemma lang=de surface="Ich hätte gern, dass ich meine Desktop-Version der" role=minimal-rewrite
E Lemma_de_fix_wechat_desktop_in_mein_system FROM_SESSION Session_wechat_desktop_in_mein_system SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-wechat-desktop-in-mein-system.toon.md
V Form_fix_wechat_desktop_in_mein_system_0_in_m kind=form lang=de surface="in mein System" fixes="ins meinem System"
E Form_fix_wechat_desktop_in_mein_system_0_in_m FROM_SESSION Session_wechat_desktop_in_mein_system
V Form_fix_wechat_desktop_in_mein_system_1_aufn kind=form lang=de surface=aufnehmen fixes=prozessieren
E Form_fix_wechat_desktop_in_mein_system_1_aufn FROM_SESSION Session_wechat_desktop_in_mein_system
V Form_fix_wechat_desktop_in_mein_system_2_desk kind=form lang=de surface="Desktop-Version / WeChat-Anwendung" fixes="Desktop Version / WeChat Anwen"
E Form_fix_wechat_desktop_in_mein_system_2_desk FROM_SESSION Session_wechat_desktop_in_mein_system
V Form_fix_wechat_desktop_in_mein_system_3_der_ kind=form lang=de surface="der WeChat-Anwendung" fixes="meiner WeChat-Anwendung"
E Form_fix_wechat_desktop_in_mein_system_3_der_ FROM_SESSION Session_wechat_desktop_in_mein_system

# ingest-session 2026-09-24T13:24:53Z oxs-in-die-planung lang=de
V Session_oxs_in_die_planung kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-oxs-in-die-planung.toon.md
V Focus_oxs_in_die_planung kind=focus lang=de gloss="in die Planung (in + Akk, f.)" status=active
E Focus_oxs_in_die_planung FROM_SESSION Session_oxs_in_die_planung
V Lemma_de_fix_oxs_in_die_planung kind=lemma lang=de surface="Bei mir gibt es ein anderes Projekt, das mir wicht" role=minimal-rewrite
E Lemma_de_fix_oxs_in_die_planung FROM_SESSION Session_oxs_in_die_planung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-oxs-in-die-planung.toon.md
V Form_fix_oxs_in_die_planung_0_ein_anderes_pro kind=form lang=de surface="ein anderes Projekt" fixes="eine andere projekt"
E Form_fix_oxs_in_die_planung_0_ein_anderes_pro FROM_SESSION Session_oxs_in_die_planung
V Form_fix_oxs_in_die_planung_1_namens kind=form lang=de surface=namens fixes=namesn
E Form_fix_oxs_in_die_planung_1_namens FROM_SESSION Session_oxs_in_die_planung
V Form_fix_oxs_in_die_planung_2_auf_laufwerk_d kind=form lang=de surface="auf Laufwerk D" fixes="im D disk"
E Form_fix_oxs_in_die_planung_2_auf_laufwerk_d FROM_SESSION Session_oxs_in_die_planung
V Form_fix_oxs_in_die_planung_3_auch_in_die_pla kind=form lang=de surface="auch in die Planung aufgenommen werden" fixes="ins Plannung auch erfassen"
E Form_fix_oxs_in_die_planung_3_auch_in_die_pla FROM_SESSION Session_oxs_in_die_planung

# auto-gap 2026-09-24T13:30:13Z surface=盲脽
V Concept_gap_zh_103e77e185 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_103e77e185 kind=gap lang=zh surface=盲脽 target=de status=open
V Lemma_zh_zh_103e77e185 kind=lemma lang=zh surface=盲脽
E Concept_gap_zh_103e77e185 EXPRESSES Lemma_zh_zh_103e77e185 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_103e77e185 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_103e77e185 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T13:31:28Z regelmaessiger-mynoise-benutzen lang=de
V Session_regelmaessiger_mynoise_benutzen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-regelmaessiger-mynoise-benutzen.toon.md
V Focus_regelmaessiger_mynoise_benutzen kind=focus lang=de gloss="regelmäßiger (nicht mehr regelmäßig)" status=active
E Focus_regelmaessiger_mynoise_benutzen FROM_SESSION Session_regelmaessiger_mynoise_benutzen
V Lemma_de_fix_regelmaessiger_mynoise_benutzen kind=lemma lang=de surface="Also gut, ich finde es sehr passend. Ich hätte ger" role=minimal-rewrite
E Lemma_de_fix_regelmaessiger_mynoise_benutzen FROM_SESSION Session_regelmaessiger_mynoise_benutzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-regelmaessiger-mynoise-benutzen.toon.md
V Form_fix_regelmaessiger_mynoise_benutzen_0_ic kind=form lang=de surface="ich finde es sehr passend" fixes="ich finde es mir sehr passend"
E Form_fix_regelmaessiger_mynoise_benutzen_0_ic FROM_SESSION Session_regelmaessiger_mynoise_benutzen
V Form_fix_regelmaessiger_mynoise_benutzen_1_re kind=form lang=de surface=regelmäßiger fixes="mehr regelmäßig"
E Form_fix_regelmaessiger_mynoise_benutzen_1_re FROM_SESSION Session_regelmaessiger_mynoise_benutzen
V Form_fix_regelmaessiger_mynoise_benutzen_2_in kind=form lang=de surface="in der Zukunft regelmäßiger benutze" fixes="benutzen in der Zukunft"
E Form_fix_regelmaessiger_mynoise_benutzen_2_in FROM_SESSION Session_regelmaessiger_mynoise_benutzen

# ingest-session 2026-09-24T13:40:18Z antrag-aufenthaltserlaubnis lang=de
V Session_antrag_aufenthaltserlaubnis kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-antrag-aufenthaltserlaubnis.toon.md
V Focus_antrag_aufenthaltserlaubnis kind=focus lang=de gloss="den Antrag (Akk. m.)" status=active
E Focus_antrag_aufenthaltserlaubnis FROM_SESSION Session_antrag_aufenthaltserlaubnis
V Lemma_de_fix_antrag_aufenthaltserlaubnis kind=lemma lang=de surface="Genau, bei mir gibt es die Notwendigkeit, bei der " role=minimal-rewrite
E Lemma_de_fix_antrag_aufenthaltserlaubnis FROM_SESSION Session_antrag_aufenthaltserlaubnis SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-antrag-aufenthaltserlaubnis.toon.md
V Form_fix_antrag_aufenthaltserlaubnis_0_die_no kind=form lang=de surface="die Notwendigkeit" fixes=Benötigkeit
E Form_fix_antrag_aufenthaltserlaubnis_0_die_no FROM_SESSION Session_antrag_aufenthaltserlaubnis
V Form_fix_antrag_aufenthaltserlaubnis_1_den_an kind=form lang=de surface="den Antrag" fixes="die Antrag"
E Form_fix_antrag_aufenthaltserlaubnis_1_den_an FROM_SESSION Session_antrag_aufenthaltserlaubnis
V Form_fix_antrag_aufenthaltserlaubnis_2_auf_di kind=form lang=de surface="auf die Aufenthaltserlaubnis" fixes="zum Aufenthaltserlaubnis"
E Form_fix_antrag_aufenthaltserlaubnis_2_auf_di FROM_SESSION Session_antrag_aufenthaltserlaubnis
V Form_fix_antrag_aufenthaltserlaubnis_3_weiter kind=form lang=de surface=weiterzubearbeiten fixes="zu weiterbearbeiten"
E Form_fix_antrag_aufenthaltserlaubnis_3_weiter FROM_SESSION Session_antrag_aufenthaltserlaubnis

# ingest-session 2026-09-24T13:42:25Z akten-sie-alle lang=de
V Session_akten_sie_alle kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-akten-sie-alle.toon.md
V Focus_akten_sie_alle kind=focus lang=de gloss="sie alle (Plural, nicht alles)" status=active
E Focus_akten_sie_alle FROM_SESSION Session_akten_sie_alle
V Lemma_de_fix_akten_sie_alle kind=lemma lang=de surface="Die Akten liegen in o-x-s. Finden Sie sie alle." role=minimal-rewrite
E Lemma_de_fix_akten_sie_alle FROM_SESSION Session_akten_sie_alle SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-akten-sie-alle.toon.md
V Form_fix_akten_sie_alle_0_sie_alle kind=form lang=de surface="sie alle" fixes="sie alles"
E Form_fix_akten_sie_alle_0_sie_alle FROM_SESSION Session_akten_sie_alle
V Form_fix_akten_sie_alle_1_in_o_x_s kind=form lang=de surface="in o-x-s" fixes="im o-x-s"
E Form_fix_akten_sie_alle_1_in_o_x_s FROM_SESSION Session_akten_sie_alle

# ingest-session 2026-09-24T13:45:39Z ausreisefrist-verhandeln lang=de
V Session_ausreisefrist_verhandeln kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-ausreisefrist-verhandeln.toon.md
V Focus_ausreisefrist_verhandeln kind=focus lang=de gloss="sollen am Ende des dass-Satzes" status=active
E Focus_ausreisefrist_verhandeln FROM_SESSION Session_ausreisefrist_verhandeln
V Lemma_de_fix_ausreisefrist_verhandeln kind=lemma lang=de surface="Ja, entdecken Sie mehr. Unsere vorhandene Forderun" role=minimal-rewrite
E Lemma_de_fix_ausreisefrist_verhandeln FROM_SESSION Session_ausreisefrist_verhandeln SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-ausreisefrist-verhandeln.toon.md
V Form_fix_ausreisefrist_verhandeln_0_dass_wir_ kind=form lang=de surface="dass wir … berichten sollen" fixes="dass wir sollen … zu berichten"
E Form_fix_ausreisefrist_verhandeln_0_dass_wir_ FROM_SESSION Session_ausreisefrist_verhandeln
V Form_fix_ausreisefrist_verhandeln_1_der_ausl_ kind=form lang=de surface="der Ausländerbehörde" fixes="zum Ausländerbehörde"
E Form_fix_ausreisefrist_verhandeln_1_der_ausl_ FROM_SESSION Session_ausreisefrist_verhandeln
V Form_fix_ausreisefrist_verhandeln_2_die_ausre kind=form lang=de surface="die Ausreisefrist" fixes=Ausreisefrist
E Form_fix_ausreisefrist_verhandeln_2_die_ausre FROM_SESSION Session_ausreisefrist_verhandeln

# ingest-session 2026-09-24T13:46:53Z gesicht-waschen-jetzt lang=de
V Session_gesicht_waschen_jetzt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gesicht-waschen-jetzt.toon.md
V Focus_gesicht_waschen_jetzt kind=focus lang=de gloss="mein Gesicht / zu waschen" status=active
E Focus_gesicht_waschen_jetzt FROM_SESSION Session_gesicht_waschen_jetzt
V Lemma_de_fix_gesicht_waschen_jetzt kind=lemma lang=de surface="Also gut, ich gehe jetzt zum Putzen und mein Gesic" role=minimal-rewrite
E Lemma_de_fix_gesicht_waschen_jetzt FROM_SESSION Session_gesicht_waschen_jetzt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gesicht-waschen-jetzt.toon.md
V Form_fix_gesicht_waschen_jetzt_0_mein_gesicht kind=form lang=de surface="mein Gesicht" fixes="meine Gesicht"
E Form_fix_gesicht_waschen_jetzt_0_mein_gesicht FROM_SESSION Session_gesicht_waschen_jetzt
V Form_fix_gesicht_waschen_jetzt_1_waschen kind=form lang=de surface=waschen fixes="zu gewäschen"
E Form_fix_gesicht_waschen_jetzt_1_waschen FROM_SESSION Session_gesicht_waschen_jetzt

# ingest-session 2026-09-24T13:55:00Z ausserordentliche-kuendigung lang=de
V Session_ausserordentliche_kuendigung kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-ausserordentliche-kuendigung.toon.md
V Focus_ausserordentliche_kuendigung kind=focus lang=de gloss="die außerordentliche Kündigung (f.)" status=active
E Focus_ausserordentliche_kuendigung FROM_SESSION Session_ausserordentliche_kuendigung
V Lemma_de_fix_ausserordentliche_kuendigung kind=lemma lang=de surface="Hast du die außerordentliche Kündigung für uns bei" role=minimal-rewrite
E Lemma_de_fix_ausserordentliche_kuendigung FROM_SESSION Session_ausserordentliche_kuendigung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-ausserordentliche-kuendigung.toon.md
V Form_fix_ausserordentliche_kuendigung_0_die_a kind=form lang=de surface="die außerordentliche Kündigung" fixes="den Außerordentliche Kündigung"
E Form_fix_ausserordentliche_kuendigung_0_die_a FROM_SESSION Session_ausserordentliche_kuendigung

# ingest-session 2026-09-24T13:55:59Z jetzt-bin-ich-zurueck lang=de
V Session_jetzt_bin_ich_zurueck kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-jetzt-bin-ich-zurueck.toon.md
V Focus_jetzt_bin_ich_zurueck kind=focus lang=de gloss="Also (Diskurs) statt So" status=active
E Focus_jetzt_bin_ich_zurueck FROM_SESSION Session_jetzt_bin_ich_zurueck
V Lemma_de_fix_jetzt_bin_ich_zurueck kind=lemma lang=de surface="Also, jetzt bin ich zurück." role=minimal-rewrite
E Lemma_de_fix_jetzt_bin_ich_zurueck FROM_SESSION Session_jetzt_bin_ich_zurueck SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-jetzt-bin-ich-zurueck.toon.md
V Form_fix_jetzt_bin_ich_zurueck_0_also_jetzt_b kind=form lang=de surface="Also, jetzt bin ich zurück." fixes="So, jetzt bin ich zurück"
E Form_fix_jetzt_bin_ich_zurueck_0_also_jetzt_b FROM_SESSION Session_jetzt_bin_ich_zurueck

# ingest-session 2026-09-24T14:06:35Z nahrungsergaenzungsmittel-schon-genommen lang=de
V Session_nahrungsergaenzungsmittel_schon_genommen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nahrungsergaenzungsmittel-schon-genommen.toon.md
V Focus_nahrungsergaenzungsmittel_schon_genommen kind=focus lang=de gloss="die Nahrungsergänzungsmittel" status=active
E Focus_nahrungsergaenzungsmittel_schon_genommen FROM_SESSION Session_nahrungsergaenzungsmittel_schon_genommen
V Lemma_de_fix_nahrungsergaenzungsmittel_schon_genommen kind=lemma lang=de surface="Genau, bei den Nahrungsergänzungsmitteln bin ich d" role=minimal-rewrite
E Lemma_de_fix_nahrungsergaenzungsmittel_schon_genommen FROM_SESSION Session_nahrungsergaenzungsmittel_schon_genommen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nahrungsergaenzungsmittel-schon-genommen.toon.md
V Form_fix_nahrungsergaenzungsmittel_schon_geno kind=form lang=de surface=Nahrungsergänzungsmittel fixes=Nährungsergänzungsmittel
E Form_fix_nahrungsergaenzungsmittel_schon_geno FROM_SESSION Session_nahrungsergaenzungsmittel_schon_genommen
V Form_fix_nahrungsergaenzungsmittel_schon_geno kind=form lang=de surface="bei den Nahrungsergänzungsmitteln bin ic" fixes="bei … sind sie vorbei"
E Form_fix_nahrungsergaenzungsmittel_schon_geno FROM_SESSION Session_nahrungsergaenzungsmittel_schon_genommen

# ingest-session 2026-09-24T14:07:01Z zugang-zu-dieser-email lang=de
V Session_zugang_zu_dieser_email kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zugang-zu-dieser-email.toon.md
V Focus_zugang_zu_dieser_email kind=focus lang=de gloss="zu dieser E-Mail-Adresse (zu + Dat)" status=active
E Focus_zugang_zu_dieser_email FROM_SESSION Session_zugang_zu_dieser_email
V Lemma_de_fix_zugang_zu_dieser_email kind=lemma lang=de surface="Zum Beschluss des Arbeitsgerichts behauptet sie, d" role=minimal-rewrite
E Lemma_de_fix_zugang_zu_dieser_email FROM_SESSION Session_zugang_zu_dieser_email SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zugang-zu-dieser-email.toon.md
V Form_fix_zugang_zu_dieser_email_0_zu_dieser_e kind=form lang=de surface="zu dieser E-Mail-Adresse" fixes="zur diese Email address"
E Form_fix_zugang_zu_dieser_email_0_zu_dieser_e FROM_SESSION Session_zugang_zu_dieser_email
V Form_fix_zugang_zu_dieser_email_1_der_beklagt kind=form lang=de surface="der Beklagte" fixes="der Klagte"
E Form_fix_zugang_zu_dieser_email_1_der_beklagt FROM_SESSION Session_zugang_zu_dieser_email
V Form_fix_zugang_zu_dieser_email_2_insolvenzve kind=form lang=de surface=Insolvenzverwalter fixes=Insolventsverwalter
E Form_fix_zugang_zu_dieser_email_2_insolvenzve FROM_SESSION Session_zugang_zu_dieser_email

# ingest-session 2026-09-24T14:09:40Z zugang-zur-legal-email lang=de
V Session_zugang_zur_legal_email kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zugang-zur-legal-email.toon.md
V Focus_zugang_zur_legal_email kind=focus lang=de gloss="zu der Legal-E-Mail (zu + Dat)" status=active
E Focus_zugang_zur_legal_email FROM_SESSION Session_zugang_zur_legal_email
V Lemma_de_fix_zugang_zur_legal_email kind=lemma lang=de surface="Wie kann ich dir helfen, Zugang zu der Legal-E-Mai" role=minimal-rewrite
E Lemma_de_fix_zugang_zur_legal_email FROM_SESSION Session_zugang_zur_legal_email SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zugang-zur-legal-email.toon.md
V Form_fix_zugang_zur_legal_email_0_die_legal_e kind=form lang=de surface="die Legal-E-Mail" fixes="legal Email"
E Form_fix_zugang_zur_legal_email_0_die_legal_e FROM_SESSION Session_zugang_zur_legal_email

# ingest-session 2026-09-24T14:15:37Z env-datei-hinzugefuegt lang=de
V Session_env_datei_hinzugefuegt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-env-datei-hinzugefuegt.toon.md
V Focus_env_datei_hinzugefuegt kind=focus lang=de gloss="die ENV-Datei (Akk. f.)" status=active
E Focus_env_datei_hinzugefuegt FROM_SESSION Session_env_datei_hinzugefuegt
V Lemma_de_fix_env_datei_hinzugefuegt kind=lemma lang=de surface="Ach so, jetzt habe ich die ENV-Datei hinzugefügt." role=minimal-rewrite
E Lemma_de_fix_env_datei_hinzugefuegt FROM_SESSION Session_env_datei_hinzugefuegt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-env-datei-hinzugefuegt.toon.md
V Form_fix_env_datei_hinzugefuegt_0_die_env_dat kind=form lang=de surface="die ENV-Datei" fixes="den ENV Datei"
E Form_fix_env_datei_hinzugefuegt_0_die_env_dat FROM_SESSION Session_env_datei_hinzugefuegt

# ingest-session 2026-09-24T18:39:39Z todo-liste-einsehen lang=de
V Session_todo_liste_einsehen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-todo-liste-einsehen.toon.md
V Focus_todo_liste_einsehen kind=focus lang=de gloss="einsehen kann (Modalverb am Ende)" status=active
E Focus_todo_liste_einsehen FROM_SESSION Session_todo_liste_einsehen
V Lemma_de_fix_todo_liste_einsehen kind=lemma lang=de surface="Nein, ich hätte gern, dass ich meine TODO-Liste ei" role=minimal-rewrite
E Lemma_de_fix_todo_liste_einsehen FROM_SESSION Session_todo_liste_einsehen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-todo-liste-einsehen.toon.md
V Form_fix_todo_liste_einsehen_0_meine_todo_lis kind=form lang=de surface="meine TODO-Liste" fixes="meine TODO"
E Form_fix_todo_liste_einsehen_0_meine_todo_lis FROM_SESSION Session_todo_liste_einsehen
V Form_fix_todo_liste_einsehen_1_einsehen_kann kind=form lang=de surface="einsehen kann" fixes=einsehen
E Form_fix_todo_liste_einsehen_1_einsehen_kann FROM_SESSION Session_todo_liste_einsehen

# ingest-session 2026-09-24T18:40:44Z kommunikation-mit-der-auslaenderbehoerde lang=de
V Session_kommunikation_mit_der_auslaenderbehoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-kommunikation-mit-der-auslaenderbehoerde.toon.md
V Focus_kommunikation_mit_der_auslaenderbehoerde kind=focus lang=de gloss="mit der Ausländerbehörde (mit + Dat)" status=active
E Focus_kommunikation_mit_der_auslaenderbehoerde FROM_SESSION Session_kommunikation_mit_der_auslaenderbehoerde
V Lemma_de_fix_kommunikation_mit_der_auslaenderbehoerde kind=lemma lang=de surface="Insbesondere für die Kommunikation mit der Ausländ" role=minimal-rewrite
E Lemma_de_fix_kommunikation_mit_der_auslaenderbehoerde FROM_SESSION Session_kommunikation_mit_der_auslaenderbehoerde SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-kommunikation-mit-der-auslaenderbehoerde.toon.md
V Form_fix_kommunikation_mit_der_auslaenderbeho kind=form lang=de surface="mit der Ausländerbehörde" fixes="zur Ausländerbehörde"
E Form_fix_kommunikation_mit_der_auslaenderbeho FROM_SESSION Session_kommunikation_mit_der_auslaenderbehoerde

# auto-gap 2026-09-24T18:41:54Z surface=will
V Concept_gap_en_will kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_will kind=gap lang=en surface=will target=de status=open
V Lemma_en_en_will kind=lemma lang=en surface=will
E Concept_gap_en_will EXPRESSES Lemma_en_en_will SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_will GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_will GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T18:42:32Z latex-pdf-die-ich-abschicken-will lang=de
V Session_latex_pdf_die_ich_abschicken_will kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-latex-pdf-die-ich-abschicken-will.toon.md
V Focus_latex_pdf_die_ich_abschicken_will kind=focus lang=de gloss="die ich (Relativpronomen zur Datei)" status=active
E Focus_latex_pdf_die_ich_abschicken_will FROM_SESSION Session_latex_pdf_die_ich_abschicken_will
V Lemma_de_fix_latex_pdf_die_ich_abschicken_will kind=lemma lang=de surface="Zeigst du mir die LaTeX-PDF-Datei, die ich an die " role=minimal-rewrite
E Lemma_de_fix_latex_pdf_die_ich_abschicken_will FROM_SESSION Session_latex_pdf_die_ich_abschicken_will SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-latex-pdf-die-ich-abschicken-will.toon.md
V Form_fix_latex_pdf_die_ich_abschicken_will_0_ kind=form lang=de surface="die ich" fixes="dem ich"
E Form_fix_latex_pdf_die_ich_abschicken_will_0_ FROM_SESSION Session_latex_pdf_die_ich_abschicken_will
V Form_fix_latex_pdf_die_ich_abschicken_will_1_ kind=form lang=de surface="an die Ausländerbehörde abschicken" fixes="zur Ausländerbehörde abschicke"
E Form_fix_latex_pdf_die_ich_abschicken_will_1_ FROM_SESSION Session_latex_pdf_die_ich_abschicken_will

# ingest-session 2026-09-24T18:44:52Z mit-der-auslaenderbehoerde-kommunizieren lang=de
V Session_mit_der_auslaenderbehoerde_kommunizieren kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-mit-der-auslaenderbehoerde-kommunizieren.toon.md
V Focus_mit_der_auslaenderbehoerde_kommunizieren kind=focus lang=de gloss="mit der Ausländerbehörde (mit + Dat)" status=active
E Focus_mit_der_auslaenderbehoerde_kommunizieren FROM_SESSION Session_mit_der_auslaenderbehoerde_kommunizieren
V Lemma_de_fix_mit_der_auslaenderbehoerde_kommunizieren kind=lemma lang=de surface="Naja, ich muss mit der Ausländerbehörde kommunizie" role=minimal-rewrite
E Lemma_de_fix_mit_der_auslaenderbehoerde_kommunizieren FROM_SESSION Session_mit_der_auslaenderbehoerde_kommunizieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-mit-der-auslaenderbehoerde-kommunizieren.toon.md
V Form_fix_mit_der_auslaenderbehoerde_kommunizi kind=form lang=de surface="mit der Ausländerbehörde kommunizieren" fixes="zur Ausländerbehörde kommunizi"
E Form_fix_mit_der_auslaenderbehoerde_kommunizi FROM_SESSION Session_mit_der_auslaenderbehoerde_kommunizieren
V Form_fix_mit_der_auslaenderbehoerde_kommunizi kind=form lang=de surface="nicht nur etwas für mich anzeigen lassen" fixes="nicht für mich zu anzeigen"
E Form_fix_mit_der_auslaenderbehoerde_kommunizi FROM_SESSION Session_mit_der_auslaenderbehoerde_kommunizieren

# ingest-session 2026-09-24T18:49:47Z umgang-vier-wendungen lang=de
V Session_umgang_vier_wendungen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-umgang-vier-wendungen.toon.md
V Focus_umgang_vier_wendungen kind=focus lang=de gloss="die Umgangssprache" status=active
E Focus_umgang_vier_wendungen FROM_SESSION Session_umgang_vier_wendungen
V Lemma_de_fix_umgang_vier_wendungen kind=lemma lang=de surface="Bei den DW-Übungen waren die Lückenübungen sehr un" role=minimal-rewrite
E Lemma_de_fix_umgang_vier_wendungen FROM_SESSION Session_umgang_vier_wendungen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-umgang-vier-wendungen.toon.md
V Form_fix_umgang_vier_wendungen_0_umgangssprac kind=form lang=de surface=Umgangssprache fixes=Umgangsparche
E Form_fix_umgang_vier_wendungen_0_umgangssprac FROM_SESSION Session_umgang_vier_wendungen
V Form_fix_umgang_vier_wendungen_1_bei_den_dw_b kind=form lang=de surface="Bei den DW-Übungen waren die Lückenübung" fixes="Im DW Übungen hat den Lückenüb"
E Form_fix_umgang_vier_wendungen_1_bei_den_dw_b FROM_SESSION Session_umgang_vier_wendungen
V Form_fix_umgang_vier_wendungen_2_auf_herz_und kind=form lang=de surface="auf Herz und Nieren prüfen" fixes="auf Herz und Nieren lernen"
E Form_fix_umgang_vier_wendungen_2_auf_herz_und FROM_SESSION Session_umgang_vier_wendungen

# ingest-session 2026-09-24T18:51:12Z erklaerung-von-der-fachhochschule lang=de
V Session_erklaerung_von_der_fachhochschule kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-erklaerung-von-der-fachhochschule.toon.md
V Focus_erklaerung_von_der_fachhochschule kind=focus lang=de gloss="von der Fachhochschule (von + Dat, f.)" status=active
E Focus_erklaerung_von_der_fachhochschule FROM_SESSION Session_erklaerung_von_der_fachhochschule
V Lemma_de_fix_erklaerung_von_der_fachhochschule kind=lemma lang=de surface="Das stimmt noch nicht. Es gibt keine Erklärung uns" role=minimal-rewrite
E Lemma_de_fix_erklaerung_von_der_fachhochschule FROM_SESSION Session_erklaerung_von_der_fachhochschule SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-erklaerung-von-der-fachhochschule.toon.md
V Form_fix_erklaerung_von_der_fachhochschule_0_ kind=form lang=de surface="die Erklärung" fixes="den Erklärung"
E Form_fix_erklaerung_von_der_fachhochschule_0_ FROM_SESSION Session_erklaerung_von_der_fachhochschule
V Form_fix_erklaerung_von_der_fachhochschule_1_ kind=form lang=de surface="von der Fachhochschule" fixes="vom Fachhochschule"
E Form_fix_erklaerung_von_der_fachhochschule_1_ FROM_SESSION Session_erklaerung_von_der_fachhochschule
V Form_fix_erklaerung_von_der_fachhochschule_2_ kind=form lang=de surface="die rechtliche Bestreitung" fixes="die Rechtliche Bestreit"
E Form_fix_erklaerung_von_der_fachhochschule_2_ FROM_SESSION Session_erklaerung_von_der_fachhochschule

# ingest-session 2026-09-24T18:59:27Z offene-gehaltschuld-anlagen lang=de
V Session_offene_gehaltschuld_anlagen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-offene-gehaltschuld-anlagen.toon.md
V Focus_offene_gehaltschuld_anlagen kind=focus lang=de gloss="die offene Gehaltsschuld (f.)" status=active
E Focus_offene_gehaltschuld_anlagen FROM_SESSION Session_offene_gehaltschuld_anlagen
V Lemma_de_fix_offene_gehaltschuld_anlagen kind=lemma lang=de surface="Es gibt immer noch die offene Gehaltsschuld der Fa" role=minimal-rewrite
E Lemma_de_fix_offene_gehaltschuld_anlagen FROM_SESSION Session_offene_gehaltschuld_anlagen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-offene-gehaltschuld-anlagen.toon.md
V Form_fix_offene_gehaltschuld_anlagen_0_die_of kind=form lang=de surface="die offene Gehaltsschuld" fixes="den Offene Gehaltsschuldung"
E Form_fix_offene_gehaltschuld_anlagen_0_die_of FROM_SESSION Session_offene_gehaltschuld_anlagen
V Form_fix_offene_gehaltschuld_anlagen_1_die_no kind=form lang=de surface="die Notwendigkeit" fixes=Benötigkeit
E Form_fix_offene_gehaltschuld_anlagen_1_die_no FROM_SESSION Session_offene_gehaltschuld_anlagen
V Form_fix_offene_gehaltschuld_anlagen_2_bei_de kind=form lang=de surface="bei der E-Mail an die Ausländerbehörde" fixes="bei dem Email zur Ausländerbeh"
E Form_fix_offene_gehaltschuld_anlagen_2_bei_de FROM_SESSION Session_offene_gehaltschuld_anlagen

# ingest-session 2026-09-24T19:04:48Z forderungsformulare-ausfuellen lang=de
V Session_forderungsformulare_ausfuellen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformulare-ausfuellen.toon.md
V Focus_forderungsformulare_ausfuellen kind=focus lang=de gloss="in den E-Mails (in + Dat)" status=active
E Focus_forderungsformulare_ausfuellen FROM_SESSION Session_forderungsformulare_ausfuellen
V Lemma_de_fix_forderungsformulare_ausfuellen kind=lemma lang=de surface="Fügen Sie das ins Projekt o-x-s hinzu. Es gibt sol" role=minimal-rewrite
E Lemma_de_fix_forderungsformulare_ausfuellen FROM_SESSION Session_forderungsformulare_ausfuellen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformulare-ausfuellen.toon.md
V Form_fix_forderungsformulare_ausfuellen_0_in_ kind=form lang=de surface="in den E-Mails" fixes="in der Emails"
E Form_fix_forderungsformulare_ausfuellen_0_in_ FROM_SESSION Session_forderungsformulare_ausfuellen
V Form_fix_forderungsformulare_ausfuellen_1_vom kind=form lang=de surface="vom Insolvenzverwalter" fixes="vom dem Insolvenzverwalter"
E Form_fix_forderungsformulare_ausfuellen_1_vom FROM_SESSION Session_forderungsformulare_ausfuellen
V Form_fix_forderungsformulare_ausfuellen_2_for kind=form lang=de surface="Forderungsformulare auszufüllen" fixes="Forderungsfomulare zu einfülle"
E Form_fix_forderungsformulare_ausfuellen_2_for FROM_SESSION Session_forderungsformulare_ausfuellen

# ingest-session 2026-09-24T19:07:56Z zuerst-verwalter-dann-behoerde lang=de
V Session_zuerst_verwalter_dann_behoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zuerst-verwalter-dann-behoerde.toon.md
V Focus_zuerst_verwalter_dann_behoerde kind=focus lang=de gloss="der Ausländerbehörde (sagen + Dat)" status=active
E Focus_zuerst_verwalter_dann_behoerde FROM_SESSION Session_zuerst_verwalter_dann_behoerde
V Lemma_de_fix_zuerst_verwalter_dann_behoerde kind=lemma lang=de surface="Genau, helfen Sie mir dabei: zuerst, was vor dem I" role=minimal-rewrite
E Lemma_de_fix_zuerst_verwalter_dann_behoerde FROM_SESSION Session_zuerst_verwalter_dann_behoerde SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zuerst-verwalter-dann-behoerde.toon.md
V Form_fix_zuerst_verwalter_dann_behoerde_0_der kind=form lang=de surface="der Ausländerbehörde" fixes="zum Ausländerbehörde"
E Form_fix_zuerst_verwalter_dann_behoerde_0_der FROM_SESSION Session_zuerst_verwalter_dann_behoerde
V Form_fix_zuerst_verwalter_dann_behoerde_1_zue kind=form lang=de surface="zuerst, was zu tun ist" fixes="zuerst was zu tun"
E Form_fix_zuerst_verwalter_dann_behoerde_1_zue FROM_SESSION Session_zuerst_verwalter_dann_behoerde

# ingest-session 2026-09-24T19:11:21Z das-ist-fuer-owen lang=de
V Session_das_ist_fuer_owen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-fuer-owen.toon.md
V Focus_das_ist_fuer_owen kind=focus lang=de gloss="für Owen (für + Akk)" status=active
E Focus_das_ist_fuer_owen FROM_SESSION Session_das_ist_fuer_owen
V Lemma_de_fix_das_ist_fuer_owen kind=lemma lang=de surface="Das ist für Owen." role=minimal-rewrite
E Lemma_de_fix_das_ist_fuer_owen FROM_SESSION Session_das_ist_fuer_owen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-fuer-owen.toon.md
V Form_fix_das_ist_fuer_owen_0_das_ist_f_r_owen kind=form lang=de surface="Das ist für Owen." fixes="Das ist für Owen"
E Form_fix_das_ist_fuer_owen_0_das_ist_f_r_owen FROM_SESSION Session_das_ist_fuer_owen

# ingest-session 2026-09-24T19:12:27Z das-ist-fuer-yushu lang=de
V Session_das_ist_fuer_yushu kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-fuer-yushu.toon.md
V Focus_das_ist_fuer_yushu kind=focus lang=de gloss="für Yushu (für + Akk)" status=active
E Focus_das_ist_fuer_yushu FROM_SESSION Session_das_ist_fuer_yushu
V Lemma_de_fix_das_ist_fuer_yushu kind=lemma lang=de surface="Das ist für Yushu." role=minimal-rewrite
E Lemma_de_fix_das_ist_fuer_yushu FROM_SESSION Session_das_ist_fuer_yushu SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-fuer-yushu.toon.md
V Form_fix_das_ist_fuer_yushu_0_das_ist_f_r_yus kind=form lang=de surface="Das ist für Yushu." fixes="Das ist für Yushu"
E Form_fix_das_ist_fuer_yushu_0_das_ist_f_r_yus FROM_SESSION Session_das_ist_fuer_yushu

# ingest-session 2026-09-24T19:15:32Z forderungsformular-ausfuellen lang=de
V Session_forderungsformular_ausfuellen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformular-ausfuellen.toon.md
V Focus_forderungsformular_ausfuellen kind=focus lang=de gloss="das Forderungsformular (n.)" status=active
E Focus_forderungsformular_ausfuellen FROM_SESSION Session_forderungsformular_ausfuellen
V Lemma_de_fix_forderungsformular_ausfuellen kind=lemma lang=de surface="Genau, kannst du im Augenblick das Forderungsformu" role=minimal-rewrite
E Lemma_de_fix_forderungsformular_ausfuellen FROM_SESSION Session_forderungsformular_ausfuellen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformular-ausfuellen.toon.md
V Form_fix_forderungsformular_ausfuellen_0_das_ kind=form lang=de surface="das Forderungsformular ausfüllen" fixes="den Forderungsformular einfüll"
E Form_fix_forderungsformular_ausfuellen_0_das_ FROM_SESSION Session_forderungsformular_ausfuellen

# ingest-session 2026-09-24T19:19:24Z seien-sie-vorsichtiger lang=de
V Session_seien_sie_vorsichtiger kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-seien-sie-vorsichtiger.toon.md
V Focus_seien_sie_vorsichtiger kind=focus lang=de gloss="vorsichtiger (Komparativ)" status=active
E Focus_seien_sie_vorsichtiger FROM_SESSION Session_seien_sie_vorsichtiger
V Lemma_de_fix_seien_sie_vorsichtiger kind=lemma lang=de surface="Seien Sie vorsichtiger." role=minimal-rewrite
E Lemma_de_fix_seien_sie_vorsichtiger FROM_SESSION Session_seien_sie_vorsichtiger SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-seien-sie-vorsichtiger.toon.md
V Form_fix_seien_sie_vorsichtiger_0_vorsichtige kind=form lang=de surface=vorsichtiger fixes="mehr vorsichtig"
E Form_fix_seien_sie_vorsichtiger_0_vorsichtige FROM_SESSION Session_seien_sie_vorsichtiger

# ingest-session 2026-09-24T19:26:38Z zinsen-schuldgrund-rote-schrift lang=de
V Session_zinsen_schuldgrund_rote_schrift kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zinsen-schuldgrund-rote-schrift.toon.md
V Focus_zinsen_schuldgrund_rote_schrift kind=focus lang=de gloss="die Zinsen (Plural)" status=active
E Focus_zinsen_schuldgrund_rote_schrift FROM_SESSION Session_zinsen_schuldgrund_rote_schrift
V Lemma_de_fix_zinsen_schuldgrund_rote_schrift kind=lemma lang=de surface="Aktualisieren Sie bitte. Warum sind die Zinsen off" role=minimal-rewrite
E Lemma_de_fix_zinsen_schuldgrund_rote_schrift FROM_SESSION Session_zinsen_schuldgrund_rote_schrift SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zinsen-schuldgrund-rote-schrift.toon.md
V Form_fix_zinsen_schuldgrund_rote_schrift_0_si kind=form lang=de surface="sind die Zinsen" fixes="ist Zinsen"
E Form_fix_zinsen_schuldgrund_rote_schrift_0_si FROM_SESSION Session_zinsen_schuldgrund_rote_schrift
V Form_fix_zinsen_schuldgrund_rote_schrift_1_un kind=form lang=de surface="unter der Zeile" fixes="unter der Zeilen"
E Form_fix_zinsen_schuldgrund_rote_schrift_1_un FROM_SESSION Session_zinsen_schuldgrund_rote_schrift
V Form_fix_zinsen_schuldgrund_rote_schrift_2_ro kind=form lang=de surface="rote Schrift" fixes="Roter Schriften"
E Form_fix_zinsen_schuldgrund_rote_schrift_2_ro FROM_SESSION Session_zinsen_schuldgrund_rote_schrift

# auto-gap 2026-09-24T19:29:59Z surface=灞呬腑
V Concept_gap_zh_5772b032c5 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_5772b032c5 kind=gap lang=zh surface=灞呬腑 target=de status=open
V Lemma_zh_zh_5772b032c5 kind=lemma lang=zh surface=灞呬腑
E Concept_gap_zh_5772b032c5 EXPRESSES Lemma_zh_zh_5772b032c5 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_5772b032c5 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_5772b032c5 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T19:31:09Z zentriert-ueber-den-unterzeilen lang=de
V Session_zentriert_ueber_den_unterzeilen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zentriert-ueber-den-unterzeilen.toon.md
V Focus_zentriert_ueber_den_unterzeilen kind=focus lang=de gloss="über den Unterzeilen (über + Dat)" status=active
E Focus_zentriert_ueber_den_unterzeilen FROM_SESSION Session_zentriert_ueber_den_unterzeilen
V Lemma_de_fix_zentriert_ueber_den_unterzeilen kind=lemma lang=de surface="Ein bisschen zentriert und über den Unterzeilen, j" role=minimal-rewrite
E Lemma_de_fix_zentriert_ueber_den_unterzeilen FROM_SESSION Session_zentriert_ueber_den_unterzeilen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zentriert-ueber-den-unterzeilen.toon.md
V Form_fix_zentriert_ueber_den_unterzeilen_0_ze kind=form lang=de surface=zentriert fixes=居中
E Form_fix_zentriert_ueber_den_unterzeilen_0_ze FROM_SESSION Session_zentriert_ueber_den_unterzeilen
V Form_fix_zentriert_ueber_den_unterzeilen_1_be kind=form lang=de surface="über den Unterzeilen" fixes="über Unterzeilen"
E Form_fix_zentriert_ueber_den_unterzeilen_1_be FROM_SESSION Session_zentriert_ueber_den_unterzeilen

# ingest-session 2026-09-24T19:34:07Z pdf-dateien-noch-einmal lang=de
V Session_pdf_dateien_noch_einmal kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-pdf-dateien-noch-einmal.toon.md
V Focus_pdf_dateien_noch_einmal kind=focus lang=de gloss="noch einmal" status=active
E Focus_pdf_dateien_noch_einmal FROM_SESSION Session_pdf_dateien_noch_einmal
V Lemma_de_fix_pdf_dateien_noch_einmal kind=lemma lang=de surface="Listen Sie mir die PDF-Dateien noch einmal auf, bi" role=minimal-rewrite
E Lemma_de_fix_pdf_dateien_noch_einmal FROM_SESSION Session_pdf_dateien_noch_einmal SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-pdf-dateien-noch-einmal.toon.md
V Form_fix_pdf_dateien_noch_einmal_0_noch_einma kind=form lang=de surface="noch einmal" fixes=nochmal
E Form_fix_pdf_dateien_noch_einmal_0_noch_einma FROM_SESSION Session_pdf_dateien_noch_einmal
V Form_fix_pdf_dateien_noch_einmal_1_die_pdf_da kind=form lang=de surface="die PDF-Dateien" fixes="die PDF-Datei"
E Form_fix_pdf_dateien_noch_einmal_1_die_pdf_da FROM_SESSION Session_pdf_dateien_noch_einmal

# ingest-session 2026-09-24T19:35:39Z gmail-konto-fuer-dieses-projekt lang=de
V Session_gmail_konto_fuer_dieses_projekt kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gmail-konto-fuer-dieses-projekt.toon.md
V Focus_gmail_konto_fuer_dieses_projekt kind=focus lang=de gloss="für dieses Projekt / mein Gmail-Konto" status=active
E Focus_gmail_konto_fuer_dieses_projekt FROM_SESSION Session_gmail_konto_fuer_dieses_projekt
V Lemma_de_fix_gmail_konto_fuer_dieses_projekt kind=lemma lang=de surface="Ach so, die DW-Übung ist zurzeit erledigt. Ich möc" role=minimal-rewrite
E Lemma_de_fix_gmail_konto_fuer_dieses_projekt FROM_SESSION Session_gmail_konto_fuer_dieses_projekt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gmail-konto-fuer-dieses-projekt.toon.md
V Form_fix_gmail_konto_fuer_dieses_projekt_0_me kind=form lang=de surface="mein Gmail-Konto" fixes="meine Gmail Konto"
E Form_fix_gmail_konto_fuer_dieses_projekt_0_me FROM_SESSION Session_gmail_konto_fuer_dieses_projekt
V Form_fix_gmail_konto_fuer_dieses_projekt_1_f_ kind=form lang=de surface="für dieses Projekt" fixes="zur diese Projekt"
E Form_fix_gmail_konto_fuer_dieses_projekt_1_f_ FROM_SESSION Session_gmail_konto_fuer_dieses_projekt

# ingest-session 2026-09-24T19:40:40Z das-ist-falsch lang=de
V Session_das_ist_falsch kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-falsch.toon.md
V Focus_das_ist_falsch kind=focus lang=de gloss="Das ist falsch (das, nicht dass)" status=active
E Focus_das_ist_falsch FROM_SESSION Session_das_ist_falsch
V Lemma_de_fix_das_ist_falsch kind=lemma lang=de surface="Das ist falsch." role=minimal-rewrite
E Lemma_de_fix_das_ist_falsch FROM_SESSION Session_das_ist_falsch SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ist-falsch.toon.md
V Form_fix_das_ist_falsch_0_das_ist_falsch kind=form lang=de surface="Das ist falsch" fixes="Dass ist falsch"
E Form_fix_das_ist_falsch_0_das_ist_falsch FROM_SESSION Session_das_ist_falsch

# ingest-session 2026-09-24T19:49:07Z env-datei-falsches-format lang=de
V Session_env_datei_falsches_format kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-env-datei-falsches-format.toon.md
V Focus_env_datei_falsches_format kind=focus lang=de gloss="das Format" status=active
E Focus_env_datei_falsches_format FROM_SESSION Session_env_datei_falsches_format
V Lemma_de_fix_env_datei_falsches_format kind=lemma lang=de surface="Ich habe es in der env-Datei hinzugefügt, aber es " role=minimal-rewrite
E Lemma_de_fix_env_datei_falsches_format FROM_SESSION Session_env_datei_falsches_format SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-env-datei-falsches-format.toon.md
V Form_fix_env_datei_falsches_format_0_format kind=form lang=de surface=Format fixes=Formatten
E Form_fix_env_datei_falsches_format_0_format FROM_SESSION Session_env_datei_falsches_format
V Form_fix_env_datei_falsches_format_1_im_falsc kind=form lang=de surface="im falschen Format" fixes="auf falsche Formatten"
E Form_fix_env_datei_falsches_format_1_im_falsc FROM_SESSION Session_env_datei_falsches_format

# ingest-session 2026-09-24T19:51:24Z was-soll-ich-ab-jetzt-tun lang=de
V Session_was_soll_ich_ab_jetzt_tun kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-was-soll-ich-ab-jetzt-tun.toon.md
V Focus_was_soll_ich_ab_jetzt_tun kind=focus lang=de gloss="Was soll ich … tun?" status=active
E Focus_was_soll_ich_ab_jetzt_tun FROM_SESSION Session_was_soll_ich_ab_jetzt_tun
V Lemma_de_fix_was_soll_ich_ab_jetzt_tun kind=lemma lang=de surface="Also gut, die Unterlagen stimmen. Was soll ich ab " role=minimal-rewrite
E Lemma_de_fix_was_soll_ich_ab_jetzt_tun FROM_SESSION Session_was_soll_ich_ab_jetzt_tun SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-was-soll-ich-ab-jetzt-tun.toon.md
V Form_fix_was_soll_ich_ab_jetzt_tun_0_was_soll kind=form lang=de surface="Was soll ich ab jetzt tun?" fixes="so was soll ich ab jetzt tun"
E Form_fix_was_soll_ich_ab_jetzt_tun_0_was_soll FROM_SESSION Session_was_soll_ich_ab_jetzt_tun

# ingest-session 2026-09-24T19:51:37Z regelmaessige-zahlungen-zusammenfassen lang=de
V Session_regelmaessige_zahlungen_zusammenfassen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-regelmaessige-zahlungen-zusammenfassen.toon.md
V Focus_regelmaessige_zahlungen_zusammenfassen kind=focus lang=de gloss="regelmäßige Zahlungen für Dienstleistungen" status=active
E Focus_regelmaessige_zahlungen_zusammenfassen FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen
V Lemma_de_fix_regelmaessige_zahlungen_zusammenfassen kind=lemma lang=de surface="Ich hätte gern, dass ich aus allen meinen E-Mails " role=minimal-rewrite
E Lemma_de_fix_regelmaessige_zahlungen_zusammenfassen FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-regelmaessige-zahlungen-zusammenfassen.toon.md
V Form_fix_regelmaessige_zahlungen_zusammenfass kind=form lang=de surface="aus allen meinen E-Mails" fixes="vom alle meiner Emails"
E Form_fix_regelmaessige_zahlungen_zusammenfass FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen
V Form_fix_regelmaessige_zahlungen_zusammenfass kind=form lang=de surface="regelmäßige Zahlungen für Dienstleistung" fixes="regemäßiger Zahlung zur Dienst"
E Form_fix_regelmaessige_zahlungen_zusammenfass FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen
V Form_fix_regelmaessige_zahlungen_zusammenfass kind=form lang=de surface=sorgfältig fixes=sortfätig
E Form_fix_regelmaessige_zahlungen_zusammenfass FROM_SESSION Session_regelmaessige_zahlungen_zusammenfassen

# ingest-session 2026-09-24T19:53:06Z einschreiben-oder-email lang=de
V Session_einschreiben_oder_email kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-einschreiben-oder-email.toon.md
V Focus_einschreiben_oder_email kind=focus lang=de gloss="Stimmt nur eine E-Mail noch?" status=active
E Focus_einschreiben_oder_email FROM_SESSION Session_einschreiben_oder_email
V Lemma_de_fix_einschreiben_oder_email kind=lemma lang=de surface="Soll ich einen Brief per Einschreiben senden, oder" role=minimal-rewrite
E Lemma_de_fix_einschreiben_oder_email FROM_SESSION Session_einschreiben_oder_email SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-einschreiben-oder-email.toon.md
V Form_fix_einschreiben_oder_email_0_per_einsch kind=form lang=de surface="per Einschreiben" fixes="mit Einschreiben"
E Form_fix_einschreiben_oder_email_0_per_einsch FROM_SESSION Session_einschreiben_oder_email
V Form_fix_einschreiben_oder_email_1_stimmt_nur kind=form lang=de surface="stimmt nur eine E-Mail noch" fixes="nur Email stimmt noch"
E Form_fix_einschreiben_oder_email_1_stimmt_nur FROM_SESSION Session_einschreiben_oder_email

# ingest-session 2026-09-24T19:55:04Z zuerst-die-email-morgens-den-brief lang=de
V Session_zuerst_die_email_morgens_den_brief kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zuerst-die-email-morgens-den-brief.toon.md
V Focus_zuerst_die_email_morgens_den_brief kind=focus lang=de gloss="die E-Mail" status=active
E Focus_zuerst_die_email_morgens_den_brief FROM_SESSION Session_zuerst_die_email_morgens_den_brief
V Lemma_de_fix_zuerst_die_email_morgens_den_brief kind=lemma lang=de surface="Ach so, zuerst senden wir die E-Mail, morgens send" role=minimal-rewrite
E Lemma_de_fix_zuerst_die_email_morgens_den_brief FROM_SESSION Session_zuerst_die_email_morgens_den_brief SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-zuerst-die-email-morgens-den-brief.toon.md
V Form_fix_zuerst_die_email_morgens_den_brief_0 kind=form lang=de surface="die E-Mail" fixes="die Email"
E Form_fix_zuerst_die_email_morgens_den_brief_0 FROM_SESSION Session_zuerst_die_email_morgens_den_brief

# auto-gap 2026-09-24T19:57:30Z surface=List
V Concept_gap_en_list kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_list kind=gap lang=en surface=List target=de status=open
V Lemma_en_en_list kind=lemma lang=en surface=List
E Concept_gap_en_list EXPRESSES Lemma_en_en_list SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_list GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_list GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T19:57:42Z in-die-latex-pdf-datei lang=de
V Session_in_die_latex_pdf_datei kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-die-latex-pdf-datei.toon.md
V Focus_in_die_latex_pdf_datei kind=focus lang=de gloss="in die LaTeX-PDF-Datei" status=active
E Focus_in_die_latex_pdf_datei FROM_SESSION Session_in_die_latex_pdf_datei
V Lemma_de_fix_in_die_latex_pdf_datei kind=lemma lang=de surface="Drücken Sie das in die LaTeX-PDF-Datei, dann gucke" role=minimal-rewrite
E Lemma_de_fix_in_die_latex_pdf_datei FROM_SESSION Session_in_die_latex_pdf_datei SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-die-latex-pdf-datei.toon.md
V Form_fix_in_die_latex_pdf_datei_0_in_die_late kind=form lang=de surface="in die LaTeX-PDF-Datei" fixes="in die LATEX-PDF Datei"
E Form_fix_in_die_latex_pdf_datei_0_in_die_late FROM_SESSION Session_in_die_latex_pdf_datei
V Form_fix_in_die_latex_pdf_datei_1_dann_gucke_ kind=form lang=de surface="dann gucke ich nochmal" fixes="denn gucke ich nochmal"
E Form_fix_in_die_latex_pdf_datei_1_dann_gucke_ FROM_SESSION Session_in_die_latex_pdf_datei

# ingest-session 2026-09-24T19:58:14Z email-text-und-anlagenliste lang=de
V Session_email_text_und_anlagenliste kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-text-und-anlagenliste.toon.md
V Focus_email_text_und_anlagenliste kind=focus lang=de gloss="die Anlagenliste (f.)" status=active
E Focus_email_text_und_anlagenliste FROM_SESSION Session_email_text_und_anlagenliste
V Lemma_de_fix_email_text_und_anlagenliste kind=lemma lang=de surface="Genau, jetzt bin ich bereit, die E-Mail abzuschick" role=minimal-rewrite
E Lemma_de_fix_email_text_und_anlagenliste FROM_SESSION Session_email_text_und_anlagenliste SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-text-und-anlagenliste.toon.md
V Form_fix_email_text_und_anlagenliste_0_den_e_ kind=form lang=de surface="den E-Mail-Text" fixes="den Email Main Text"
E Form_fix_email_text_und_anlagenliste_0_den_e_ FROM_SESSION Session_email_text_und_anlagenliste
V Form_fix_email_text_und_anlagenliste_1_die_an kind=form lang=de surface="die Anlagenliste" fixes="Anlagen List"
E Form_fix_email_text_und_anlagenliste_1_die_an FROM_SESSION Session_email_text_und_anlagenliste

# auto-gap 2026-09-24T20:00:07Z surface=闂查奔
V Concept_gap_zh_372c8beb7d kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_372c8beb7d kind=gap lang=zh surface=闂查奔 target=de status=open
V Lemma_zh_zh_372c8beb7d kind=lemma lang=zh surface=闂查奔
E Concept_gap_zh_372c8beb7d EXPRESSES Lemma_zh_zh_372c8beb7d SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_372c8beb7d GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_372c8beb7d GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T20:01:26Z xianyu-northdata-post lang=de
V Session_xianyu_northdata_post kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-xianyu-northdata-post.toon.md
V Focus_xianyu_northdata_post kind=focus lang=de gloss="auf der Plattform / für den internationalen Handel" status=active
E Focus_xianyu_northdata_post FROM_SESSION Session_xianyu_northdata_post
V Lemma_de_fix_xianyu_northdata_post kind=lemma lang=de surface="Genau. Mit North Data kann ich auf der Plattform 闲" role=minimal-rewrite
E Lemma_de_fix_xianyu_northdata_post FROM_SESSION Session_xianyu_northdata_post SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-xianyu-northdata-post.toon.md
V Form_fix_xianyu_northdata_post_0_auf_der_plat kind=form lang=de surface="auf der Plattform" fixes="zur Plattforme"
E Form_fix_xianyu_northdata_post_0_auf_der_plat FROM_SESSION Session_xianyu_northdata_post
V Form_fix_xianyu_northdata_post_1_tools_f_r_de kind=form lang=de surface="Tools für den internationalen Handel" fixes="Internationalehandels Tools"
E Form_fix_xianyu_northdata_post_1_tools_f_r_de FROM_SESSION Session_xianyu_northdata_post
V Form_fix_xianyu_northdata_post_2_monetarisier kind=form lang=de surface=monetarisieren fixes=monetezieren
E Form_fix_xianyu_northdata_post_2_monetarisier FROM_SESSION Session_xianyu_northdata_post

# ingest-session 2026-09-24T20:09:44Z nachweisunterlagen-zu-den-anlagen lang=de
V Session_nachweisunterlagen_zu_den_anlagen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nachweisunterlagen-zu-den-anlagen.toon.md
V Focus_nachweisunterlagen_zu_den_anlagen kind=focus lang=de gloss="zu den Anlagen (zu + Dat)" status=active
E Focus_nachweisunterlagen_zu_den_anlagen FROM_SESSION Session_nachweisunterlagen_zu_den_anlagen
V Lemma_de_fix_nachweisunterlagen_zu_den_anlagen kind=lemma lang=de surface="Ach so, soll ich die Nachweisunterlagen auch zu de" role=minimal-rewrite
E Lemma_de_fix_nachweisunterlagen_zu_den_anlagen FROM_SESSION Session_nachweisunterlagen_zu_den_anlagen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-nachweisunterlagen-zu-den-anlagen.toon.md
V Form_fix_nachweisunterlagen_zu_den_anlagen_0_ kind=form lang=de surface="die Nachweisunterlagen" fixes="dem Nachweisunterlagen"
E Form_fix_nachweisunterlagen_zu_den_anlagen_0_ FROM_SESSION Session_nachweisunterlagen_zu_den_anlagen
V Form_fix_nachweisunterlagen_zu_den_anlagen_1_ kind=form lang=de surface="zu den Anlagen" fixes="zur Anlagen"
E Form_fix_nachweisunterlagen_zu_den_anlagen_1_ FROM_SESSION Session_nachweisunterlagen_zu_den_anlagen

# ingest-session 2026-09-24T20:16:51Z email-an-die-auslaenderbehoerde lang=de
V Session_email_an_die_auslaenderbehoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-an-die-auslaenderbehoerde.toon.md
V Focus_email_an_die_auslaenderbehoerde kind=focus lang=de gloss="eine E-Mail an die Ausländerbehörde (an + Akk)" status=active
E Focus_email_an_die_auslaenderbehoerde FROM_SESSION Session_email_an_die_auslaenderbehoerde
V Lemma_de_fix_email_an_die_auslaenderbehoerde kind=lemma lang=de surface="Gut, gib mir also auch eine E-Mail an die Auslände" role=minimal-rewrite
E Lemma_de_fix_email_an_die_auslaenderbehoerde FROM_SESSION Session_email_an_die_auslaenderbehoerde SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-an-die-auslaenderbehoerde.toon.md
V Form_fix_email_an_die_auslaenderbehoerde_0_ei kind=form lang=de surface="eine E-Mail" fixes="ein E-Mail"
E Form_fix_email_an_die_auslaenderbehoerde_0_ei FROM_SESSION Session_email_an_die_auslaenderbehoerde
V Form_fix_email_an_die_auslaenderbehoerde_1_an kind=form lang=de surface="an die Ausländerbehörde" fixes="zum Ausländerbehörde"
E Form_fix_email_an_die_auslaenderbehoerde_1_an FROM_SESSION Session_email_an_die_auslaenderbehoerde

# ingest-session 2026-09-24T20:25:29Z in-eine-zip-datei lang=de
V Session_in_eine_zip_datei kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-eine-zip-datei.toon.md
V Focus_in_eine_zip_datei kind=focus lang=de gloss="in eine Zip-Datei (in + Akk)" status=active
E Focus_in_eine_zip_datei FROM_SESSION Session_in_eine_zip_datei
V Lemma_de_fix_in_eine_zip_datei kind=lemma lang=de surface="Ach so, benennen Sie sie mit Profilnamen um und pa" role=minimal-rewrite
E Lemma_de_fix_in_eine_zip_datei FROM_SESSION Session_in_eine_zip_datei SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-eine-zip-datei.toon.md
V Form_fix_in_eine_zip_datei_0_umbenennen kind=form lang=de surface=umbenennen fixes=umnennen
E Form_fix_in_eine_zip_datei_0_umbenennen FROM_SESSION Session_in_eine_zip_datei
V Form_fix_in_eine_zip_datei_1_in_eine_zip_date kind=form lang=de surface="in eine Zip-Datei packen" fixes="ins eine Zip Datei aufpacken"
E Form_fix_in_eine_zip_datei_1_in_eine_zip_date FROM_SESSION Session_in_eine_zip_datei
V Form_fix_in_eine_zip_datei_2_eine_mietk_ndigu kind=form lang=de surface="eine Mietkündigungsbestätigung von SKAJ " fixes="es Mietkündigungsbestätigung v"
E Form_fix_in_eine_zip_datei_2_eine_mietk_ndigu FROM_SESSION Session_in_eine_zip_datei

# ingest-session 2026-09-24T20:31:22Z forderungsformulare-an-den-verwalter lang=de
V Session_forderungsformulare_an_den_verwalter kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformulare-an-den-verwalter.toon.md
V Focus_forderungsformulare_an_den_verwalter kind=focus lang=de gloss="die Forderungsformulare (n., Plural)" status=active
E Focus_forderungsformulare_an_den_verwalter FROM_SESSION Session_forderungsformulare_an_den_verwalter
V Lemma_de_fix_forderungsformulare_an_den_verwalter kind=lemma lang=de surface="So sollen Sie auch die Forderungsformulare an den " role=minimal-rewrite
E Lemma_de_fix_forderungsformulare_an_den_verwalter FROM_SESSION Session_forderungsformulare_an_den_verwalter SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-forderungsformulare-an-den-verwalter.toon.md
V Form_fix_forderungsformulare_an_den_verwalter kind=form lang=de surface="die Forderungsformulare" fixes="den Forderungsformular"
E Form_fix_forderungsformulare_an_den_verwalter FROM_SESSION Session_forderungsformulare_an_den_verwalter
V Form_fix_forderungsformulare_an_den_verwalter kind=form lang=de surface="an den Insolvenzverwalter" fixes="zum Insolvenzverwalter"
E Form_fix_forderungsformulare_an_den_verwalter FROM_SESSION Session_forderungsformulare_an_den_verwalter

# ingest-session 2026-09-24T20:34:49Z das-forderungsformular lang=de
V Session_das_forderungsformular kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-forderungsformular.toon.md
V Focus_das_forderungsformular kind=focus lang=de gloss="das Forderungsformular (n.)" status=active
E Focus_das_forderungsformular FROM_SESSION Session_das_forderungsformular
V Lemma_de_fix_das_forderungsformular kind=lemma lang=de surface="Nein, ich meine das Forderungsformular." role=minimal-rewrite
E Lemma_de_fix_das_forderungsformular FROM_SESSION Session_das_forderungsformular SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-forderungsformular.toon.md
V Form_fix_das_forderungsformular_0_das_forderu kind=form lang=de surface="das Forderungsformular" fixes=Forderungsformular
E Form_fix_das_forderungsformular_0_das_forderu FROM_SESSION Session_das_forderungsformular

# ingest-session 2026-09-24T20:38:15Z diese-beiden-forderungsanmeldungen lang=de
V Session_diese_beiden_forderungsanmeldungen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diese-beiden-forderungsanmeldungen.toon.md
V Focus_diese_beiden_forderungsanmeldungen kind=focus lang=de gloss="diese beiden" status=active
E Focus_diese_beiden_forderungsanmeldungen FROM_SESSION Session_diese_beiden_forderungsanmeldungen
V Lemma_de_fix_diese_beiden_forderungsanmeldungen kind=lemma lang=de surface="Diese beiden Forderungsanmeldungen." role=minimal-rewrite
E Lemma_de_fix_diese_beiden_forderungsanmeldungen FROM_SESSION Session_diese_beiden_forderungsanmeldungen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diese-beiden-forderungsanmeldungen.toon.md
V Form_fix_diese_beiden_forderungsanmeldungen_0 kind=form lang=de surface="diese beiden" fixes="diese beide"
E Form_fix_diese_beiden_forderungsanmeldungen_0 FROM_SESSION Session_diese_beiden_forderungsanmeldungen

# ingest-session 2026-09-24T20:40:15Z bereit-an-die-auslaenderbehoerde lang=de
V Session_bereit_an_die_auslaenderbehoerde kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-bereit-an-die-auslaenderbehoerde.toon.md
V Focus_bereit_an_die_auslaenderbehoerde kind=focus lang=de gloss="an die Ausländerbehörde (an + Akk)" status=active
E Focus_bereit_an_die_auslaenderbehoerde FROM_SESSION Session_bereit_an_die_auslaenderbehoerde
V Lemma_de_fix_bereit_an_die_auslaenderbehoerde kind=lemma lang=de surface="Ach so, und bin ich endlich bereit, eine E-Mail an" role=minimal-rewrite
E Lemma_de_fix_bereit_an_die_auslaenderbehoerde FROM_SESSION Session_bereit_an_die_auslaenderbehoerde SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-bereit-an-die-auslaenderbehoerde.toon.md
V Form_fix_bereit_an_die_auslaenderbehoerde_0_a kind=form lang=de surface="an die Ausländerbehörde" fixes="an der Ausländerbehörde"
E Form_fix_bereit_an_die_auslaenderbehoerde_0_a FROM_SESSION Session_bereit_an_die_auslaenderbehoerde
V Form_fix_bereit_an_die_auslaenderbehoerde_1_e kind=form lang=de surface=E-Mail fixes=E-mail
E Form_fix_bereit_an_die_auslaenderbehoerde_1_e FROM_SESSION Session_bereit_an_die_auslaenderbehoerde
V Form_fix_bereit_an_die_auslaenderbehoerde_2_a kind=form lang=de surface=abzuschicken fixes=abschicken
E Form_fix_bereit_an_die_auslaenderbehoerde_2_a FROM_SESSION Session_bereit_an_die_auslaenderbehoerde

# ingest-session 2026-09-24T20:42:58Z eine-ersatzdatei-zum-unterschreiben lang=de
V Session_eine_ersatzdatei_zum_unterschreiben kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-eine-ersatzdatei-zum-unterschreiben.toon.md
V Focus_eine_ersatzdatei_zum_unterschreiben kind=focus lang=de gloss="eine Ersatzdatei (f.)" status=active
E Focus_eine_ersatzdatei_zum_unterschreiben FROM_SESSION Session_eine_ersatzdatei_zum_unterschreiben
V Lemma_de_fix_eine_ersatzdatei_zum_unterschreiben kind=lemma lang=de surface="Ach so, gib mir eine Ersatzdatei zum Unterschreibe" role=minimal-rewrite
E Lemma_de_fix_eine_ersatzdatei_zum_unterschreiben FROM_SESSION Session_eine_ersatzdatei_zum_unterschreiben SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-eine-ersatzdatei-zum-unterschreiben.toon.md
V Form_fix_eine_ersatzdatei_zum_unterschreiben_ kind=form lang=de surface="eine Ersatzdatei" fixes="ein Ersatz Datei"
E Form_fix_eine_ersatzdatei_zum_unterschreiben_ FROM_SESSION Session_eine_ersatzdatei_zum_unterschreiben

# ingest-session 2026-09-24T20:46:22Z schon-unterschrieben lang=de
V Session_schon_unterschrieben kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-schon-unterschrieben.toon.md
V Focus_schon_unterschrieben kind=focus lang=de gloss=unterschrieben status=active
E Focus_schon_unterschrieben FROM_SESSION Session_schon_unterschrieben
V Lemma_de_fix_schon_unterschrieben kind=lemma lang=de surface="Ach so, ich habe schon unterschrieben. Prüfen Sie " role=minimal-rewrite
E Lemma_de_fix_schon_unterschrieben FROM_SESSION Session_schon_unterschrieben SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-schon-unterschrieben.toon.md
V Form_fix_schon_unterschrieben_0_unterschriebe kind=form lang=de surface=unterschrieben fixes=untergeschrieben
E Form_fix_schon_unterschrieben_0_unterschriebe FROM_SESSION Session_schon_unterschrieben

# ingest-session 2026-09-24T20:48:30Z bereit-eine-email-abzuschicken lang=de
V Session_bereit_eine_email_abzuschicken kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-bereit-eine-email-abzuschicken.toon.md
V Focus_bereit_eine_email_abzuschicken kind=focus lang=de gloss="eine E-Mail" status=active
E Focus_bereit_eine_email_abzuschicken FROM_SESSION Session_bereit_eine_email_abzuschicken
V Lemma_de_fix_bereit_eine_email_abzuschicken kind=lemma lang=de surface="Genau, bin ich jetzt bereit, eine E-Mail an die Au" role=minimal-rewrite
E Lemma_de_fix_bereit_eine_email_abzuschicken FROM_SESSION Session_bereit_eine_email_abzuschicken SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-bereit-eine-email-abzuschicken.toon.md
V Form_fix_bereit_eine_email_abzuschicken_0_e_m kind=form lang=de surface=E-Mail fixes=E-mail
E Form_fix_bereit_eine_email_abzuschicken_0_e_m FROM_SESSION Session_bereit_eine_email_abzuschicken

# auto-gap 2026-09-24T20:58:33Z surface=un
V Concept_gap_fr_un kind=concept gloss=unknown-expression-in-de status=open
V Gap_fr_un kind=gap lang=fr surface=un target=de status=open
V Lemma_fr_fr_un kind=lemma lang=fr surface=un
E Concept_gap_fr_un EXPRESSES Lemma_fr_fr_un SOURCE=hook/beforeSubmitPrompt
E Lemma_fr_fr_un GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_fr_un GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T20:59:17Z offenlegung-zwischen-diesen-leuten lang=de
V Session_offenlegung_zwischen_diesen_leuten kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-offenlegung-zwischen-diesen-leuten.toon.md
V Focus_offenlegung_zwischen_diesen_leuten kind=focus lang=de gloss="zwischen diesen Leuten (zwischen + Dat)" status=active
E Focus_offenlegung_zwischen_diesen_leuten FROM_SESSION Session_offenlegung_zwischen_diesen_leuten
V Lemma_de_fix_offenlegung_zwischen_diesen_leuten kind=lemma lang=de surface="Bei mir gibt es auch eine Offenlegung zwischen die" role=minimal-rewrite
E Lemma_de_fix_offenlegung_zwischen_diesen_leuten FROM_SESSION Session_offenlegung_zwischen_diesen_leuten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-offenlegung-zwischen-diesen-leuten.toon.md
V Form_fix_offenlegung_zwischen_diesen_leuten_0 kind=form lang=de surface="zwischen diesen Leuten" fixes="zwischen diese Leute"
E Form_fix_offenlegung_zwischen_diesen_leuten_0 FROM_SESSION Session_offenlegung_zwischen_diesen_leuten
V Form_fix_offenlegung_zwischen_diesen_leuten_1 kind=form lang=de surface="den Medien und mir" fixes="mit Medien und ich"
E Form_fix_offenlegung_zwischen_diesen_leuten_1 FROM_SESSION Session_offenlegung_zwischen_diesen_leuten
V Form_fix_offenlegung_zwischen_diesen_leuten_2 kind=form lang=de surface="viele Beweise" fixes="viel zu Beweise"
E Form_fix_offenlegung_zwischen_diesen_leuten_2 FROM_SESSION Session_offenlegung_zwischen_diesen_leuten

# ingest-session 2026-09-24T21:13:52Z das-ende-tiefer lang=de
V Session_das_ende_tiefer kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ende-tiefer.toon.md
V Focus_das_ende_tiefer kind=focus lang=de gloss="das Ende (n.)" status=active
E Focus_das_ende_tiefer FROM_SESSION Session_das_ende_tiefer
V Lemma_de_fix_das_ende_tiefer kind=lemma lang=de surface="Ist das schon das Ende? Die Reporterin möchte die " role=minimal-rewrite
E Lemma_de_fix_das_ende_tiefer FROM_SESSION Session_das_ende_tiefer SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-das-ende-tiefer.toon.md
V Form_fix_das_ende_tiefer_0_das_ende kind=form lang=de surface="das Ende" fixes="die Ende"
E Form_fix_das_ende_tiefer_0_das_ende FROM_SESSION Session_das_ende_tiefer
V Form_fix_das_ende_tiefer_1_die_gesch_ftlichen kind=form lang=de surface="die geschäftlichen Beziehungen" fixes="die Geschäftliche Beziehungen"
E Form_fix_das_ende_tiefer_1_die_gesch_ftlichen FROM_SESSION Session_das_ende_tiefer
V Form_fix_das_ende_tiefer_2_die_zugrunde_liege kind=form lang=de surface="die zugrunde liegende Aktualisierung" fixes="unterliegende Aktualiserung"
E Form_fix_das_ende_tiefer_2_die_zugrunde_liege FROM_SESSION Session_das_ende_tiefer

# ingest-session 2026-09-24T21:18:51Z moechte-die-reporterin lang=de
V Session_moechte_die_reporterin kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-moechte-die-reporterin.toon.md
V Focus_moechte_die_reporterin kind=focus lang=de gloss="möchte (3. Person Singular)" status=active
E Focus_moechte_die_reporterin FROM_SESSION Session_moechte_die_reporterin
V Lemma_de_fix_moechte_die_reporterin kind=lemma lang=de surface="Was möchte die Reporterin eigentlich? Was ist für " role=minimal-rewrite
E Lemma_de_fix_moechte_die_reporterin FROM_SESSION Session_moechte_die_reporterin SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-moechte-die-reporterin.toon.md
V Form_fix_moechte_die_reporterin_0_m_chte_a7d0 kind=form lang=de surface=möchte fixes=möchtet
E Form_fix_moechte_die_reporterin_0_m_chte_a7d0 FROM_SESSION Session_moechte_die_reporterin
V Form_fix_moechte_die_reporterin_1_wertvoll kind=form lang=de surface=wertvoll fixes=Wertsvoll
E Form_fix_moechte_die_reporterin_1_wertvoll FROM_SESSION Session_moechte_die_reporterin

# ingest-session 2026-09-24T21:21:55Z cybernaut-hinzufuegen lang=de
V Session_cybernaut_hinzufuegen kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-cybernaut-hinzufuegen.toon.md
V Focus_cybernaut_hinzufuegen kind=focus lang=de gloss="hinzufügen (Infinitiv nach müssen)" status=active
E Focus_cybernaut_hinzufuegen FROM_SESSION Session_cybernaut_hinzufuegen
V Lemma_de_fix_cybernaut_hinzufuegen kind=lemma lang=de surface="Bei mir gibt es auch Informationen zu Cybernaut. D" role=minimal-rewrite
E Lemma_de_fix_cybernaut_hinzufuegen FROM_SESSION Session_cybernaut_hinzufuegen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-cybernaut-hinzufuegen.toon.md
V Form_fix_cybernaut_hinzufuegen_0_informatione kind=form lang=de surface=Informationen fixes=Information
E Form_fix_cybernaut_hinzufuegen_0_informatione FROM_SESSION Session_cybernaut_hinzufuegen
V Form_fix_cybernaut_hinzufuegen_1_hinzuf_gen_4 kind=form lang=de surface=hinzufügen fixes="füge ich sie hinzu"
E Form_fix_cybernaut_hinzufuegen_1_hinzuf_gen_4 FROM_SESSION Session_cybernaut_hinzufuegen

# ingest-session 2026-09-24T21:25:01Z beziehung-cybernaut-xu lang=de
V Session_beziehung_cybernaut_xu kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-beziehung-cybernaut-xu.toon.md
V Focus_beziehung_cybernaut_xu kind=focus lang=de gloss="die Beziehung (Sg., Akk.)" status=active
E Focus_beziehung_cybernaut_xu FROM_SESSION Session_beziehung_cybernaut_xu
V Lemma_de_fix_beziehung_cybernaut_xu kind=lemma lang=de surface="Dies ist ein Screenshot vom Professor. Bei o-x-s g" role=minimal-rewrite
E Lemma_de_fix_beziehung_cybernaut_xu FROM_SESSION Session_beziehung_cybernaut_xu SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-beziehung-cybernaut-xu.toon.md
V Form_fix_beziehung_cybernaut_xu_0_ein_screens kind=form lang=de surface="ein Screenshot" fixes=Screenshot
E Form_fix_beziehung_cybernaut_xu_0_ein_screens FROM_SESSION Session_beziehung_cybernaut_xu
V Form_fix_beziehung_cybernaut_xu_1_die_beziehu kind=form lang=de surface="die Beziehung" fixes="die Beziehungs"
E Form_fix_beziehung_cybernaut_xu_1_die_beziehu FROM_SESSION Session_beziehung_cybernaut_xu

# ingest-session 2026-09-24T21:27:05Z email-von-name lang=de
V Session_email_von_name_slot kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-von-name.toon.md
V Focus_email_von_name_slot kind=focus lang=de gloss="die E-Mail von [Name] (von + Name)" status=active
E Focus_email_von_name_slot FROM_SESSION Session_email_von_name_slot
V Lemma_de_fix_email_von_name_slot kind=lemma lang=de surface="Gibt es auch die E-Mail von [Name]?" role=minimal-rewrite
E Lemma_de_fix_email_von_name_slot FROM_SESSION Session_email_von_name_slot SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-email-von-name.toon.md
V Form_fix_email_von_name_slot_0_die_e_mail_v kind=form lang=de surface="die E-Mail von [Name]" fixes="die [Name] Email auch"
E Form_fix_email_von_name_slot_0_die_e_mail_v FROM_SESSION Session_email_von_name_slot

# ingest-session 2026-09-24T21:30:40Z klageandrohung-cybernaut lang=de
V Session_klageandrohung_cybernaut kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-klageandrohung-cybernaut.toon.md
V Focus_klageandrohung_cybernaut kind=focus lang=de gloss="die Klageandrohung (f.)" status=active
E Focus_klageandrohung_cybernaut FROM_SESSION Session_klageandrohung_cybernaut
V Lemma_de_fix_klageandrohung_cybernaut kind=lemma lang=de surface="Kannst du die Klageandrohung von Cybernaut gegen T" role=minimal-rewrite
E Lemma_de_fix_klageandrohung_cybernaut FROM_SESSION Session_klageandrohung_cybernaut SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-klageandrohung-cybernaut.toon.md
V Form_fix_klageandrohung_cybernaut_0_die_klage kind=form lang=de surface="die Klageandrohung" fixes="den Klagebedrohung"
E Form_fix_klageandrohung_cybernaut_0_die_klage FROM_SESSION Session_klageandrohung_cybernaut
V Form_fix_klageandrohung_cybernaut_1_von_cyber kind=form lang=de surface="von Cybernaut" fixes="vom Cybernaut"
E Form_fix_klageandrohung_cybernaut_1_von_cyber FROM_SESSION Session_klageandrohung_cybernaut

# ingest-session 2026-09-24T21:32:18Z antwort-an-die-reporterin lang=de
V Session_antwort_an_die_reporterin kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-antwort-an-die-reporterin.toon.md
V Focus_antwort_an_die_reporterin kind=focus lang=de gloss="in meiner Antwort an die Reporterin" status=active
E Focus_antwort_an_die_reporterin FROM_SESSION Session_antwort_an_die_reporterin
V Lemma_de_fix_antwort_an_die_reporterin kind=lemma lang=de surface="Ich hätte gerne, dass diese Informationen in meine" role=minimal-rewrite
E Lemma_de_fix_antwort_an_die_reporterin FROM_SESSION Session_antwort_an_die_reporterin SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-antwort-an-die-reporterin.toon.md
V Form_fix_antwort_an_die_reporterin_0_in_meine kind=form lang=de surface="in meiner Antwort an die Reporterin" fixes="zum meine Antwort zum Reporter"
E Form_fix_antwort_an_die_reporterin_0_in_meine FROM_SESSION Session_antwort_an_die_reporterin

# ingest-session 2026-09-24T21:34:54Z finanzfachkraft lang=de
V Session_finanzfachkraft kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-finanzfachkraft.toon.md
V Focus_finanzfachkraft kind=focus lang=de gloss=Finanzfachkraft status=active
E Focus_finanzfachkraft FROM_SESSION Session_finanzfachkraft
V Lemma_de_fix_finanzfachkraft kind=lemma lang=de surface="Die Ansprechperson ist Finanzfachkraft." role=minimal-rewrite
E Lemma_de_fix_finanzfachkraft FROM_SESSION Session_finanzfachkraft SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-finanzfachkraft.toon.md
V Form_fix_finanzfachkraft_0_finanzfach kind=form lang=de surface=Finanzfachkraft fixes=Finananzfachkraft
E Form_fix_finanzfachkraft_0_finanzfach FROM_SESSION Session_finanzfachkraft

# auto-gap 2026-09-24T21:37:58Z surface=with
V Concept_gap_en_with kind=concept gloss=unknown-expression-in-de status=open
V Gap_en_with kind=gap lang=en surface=with target=de status=open
V Lemma_en_en_with kind=lemma lang=en surface=with
E Concept_gap_en_with EXPRESSES Lemma_en_en_with SOURCE=hook/beforeSubmitPrompt
E Lemma_en_en_with GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_en_with GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T21:37:58Z surface=涓撲笟鐗堜紒涓氫俊鎭
V Concept_gap_zh_f3129e4fc0 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_f3129e4fc0 kind=gap lang=zh surface=涓撲笟鐗堜紒涓氫俊鎭 target=de status=open
V Lemma_zh_zh_f3129e4fc0 kind=lemma lang=zh surface=涓撲笟鐗堜紒涓氫俊鎭
E Concept_gap_zh_f3129e4fc0 EXPRESSES Lemma_zh_zh_f3129e4fc0 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_f3129e4fc0 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_f3129e4fc0 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T21:37:58Z surface=姤鍛
V Concept_gap_zh_f62491f536 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_f62491f536 kind=gap lang=zh surface=姤鍛 target=de status=open
V Lemma_zh_zh_f62491f536 kind=lemma lang=zh surface=姤鍛
E Concept_gap_zh_f62491f536 EXPRESSES Lemma_zh_zh_f62491f536 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_f62491f536 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_f62491f536 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T21:39:40Z pdf-zu-oxs lang=de
V Session_pdf_zu_oxs kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-pdf-zu-oxs.toon.md
V Focus_pdf_zu_oxs kind=focus lang=de gloss="zu o-x-s" status=active
E Focus_pdf_zu_oxs FROM_SESSION Session_pdf_zu_oxs
V Lemma_de_fix_pdf_zu_oxs kind=lemma lang=de surface="Ich habe die PDF-Datei, die mit 专业版企业信息报告 beginnt," role=minimal-rewrite
E Lemma_de_fix_pdf_zu_oxs FROM_SESSION Session_pdf_zu_oxs SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-pdf-zu-oxs.toon.md
V Form_fix_pdf_zu_oxs_0_zu_o_x_s kind=form lang=de surface="zu o-x-s" fixes="zum o-x-s"
E Form_fix_pdf_zu_oxs_0_zu_o_x_s FROM_SESSION Session_pdf_zu_oxs

# ingest-session 2026-09-24T21:42:41Z diesen-erlass lang=de
V Session_diesen_erlass kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diesen-erlass.toon.md
V Focus_diesen_erlass kind=focus lang=de gloss="diesen Erlass (Akk. m.)" status=active
E Focus_diesen_erlass FROM_SESSION Session_diesen_erlass
V Lemma_de_fix_diesen_erlass kind=lemma lang=de surface="Ist die Nachtragsvereinbarung zum Studienvertrag e" role=minimal-rewrite
E Lemma_de_fix_diesen_erlass FROM_SESSION Session_diesen_erlass SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diesen-erlass.toon.md
V Form_fix_diesen_erlass_0_diesen_erlass kind=form lang=de surface="diesen Erlass" fixes="diese Erlass"
E Form_fix_diesen_erlass_0_diesen_erlass FROM_SESSION Session_diesen_erlass
V Form_fix_diesen_erlass_1_das_ist_ungerecht kind=form lang=de surface="Das ist ungerecht" fixes="dass ist ungerechtig"
E Form_fix_diesen_erlass_1_das_ist_ungerecht FROM_SESSION Session_diesen_erlass

# ingest-session 2026-09-24T21:52:02Z diesen-vertrag lang=de
V Session_diesen_vertrag kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diesen-vertrag.toon.md
V Focus_diesen_vertrag kind=focus lang=de gloss="diesen Vertrag (Akk. m.)" status=active
E Focus_diesen_vertrag FROM_SESSION Session_diesen_vertrag
V Lemma_de_fix_diesen_vertrag kind=lemma lang=de surface="Fügen Sie diesen Vertrag zwischen den Studierenden" role=minimal-rewrite
E Lemma_de_fix_diesen_vertrag FROM_SESSION Session_diesen_vertrag SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-diesen-vertrag.toon.md
V Form_fix_diesen_vertrag_0_diesen_vertrag kind=form lang=de surface="diesen Vertrag" fixes="diese Vertrag"
E Form_fix_diesen_vertrag_0_diesen_vertrag FROM_SESSION Session_diesen_vertrag
V Form_fix_diesen_vertrag_1_das_original kind=form lang=de surface="das Original" fixes="den Original"
E Form_fix_diesen_vertrag_1_das_original FROM_SESSION Session_diesen_vertrag

# auto-gap 2026-09-24T21:55:26Z surface=娓呬粨澶
V Concept_gap_zh_6d0384d139 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_6d0384d139 kind=gap lang=zh surface=娓呬粨澶 target=de status=open
V Lemma_zh_zh_6d0384d139 kind=lemma lang=zh surface=娓呬粨澶
E Concept_gap_zh_6d0384d139 EXPRESSES Lemma_zh_zh_6d0384d139 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_6d0384d139 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_6d0384d139 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T21:55:26Z surface=敥鍗
V Concept_gap_zh_5ab68f92e3 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_5ab68f92e3 kind=gap lang=zh surface=敥鍗 target=de status=open
V Lemma_zh_zh_5ab68f92e3 kind=lemma lang=zh surface=敥鍗
E Concept_gap_zh_5ab68f92e3 EXPRESSES Lemma_zh_zh_5ab68f92e3 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_5ab68f92e3 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_5ab68f92e3 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T21:56:38Z in-der-richtigen-lage lang=de
V Session_in_der_richtigen_lage kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-der-richtigen-lage.toon.md
V Focus_in_der_richtigen_lage kind=focus lang=de gloss="in der richtigen Lage" status=active
E Focus_in_der_richtigen_lage FROM_SESSION Session_in_der_richtigen_lage
V Lemma_de_fix_in_der_richtigen_lage kind=lemma lang=de surface="Es gibt noch übertriebene XU-Werbung auf Xiaohongs" role=minimal-rewrite
E Lemma_de_fix_in_der_richtigen_lage FROM_SESSION Session_in_der_richtigen_lage SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-in-der-richtigen-lage.toon.md
V Form_fix_in_der_richtigen_lage_0_in_der_richt kind=form lang=de surface="in der richtigen Lage" fixes="in der richtige Lage"
E Form_fix_in_der_richtigen_lage_0_in_der_richt FROM_SESSION Session_in_der_richtigen_lage
V Form_fix_in_der_richtigen_lage_1_ein_eigenes_ kind=form lang=de surface="ein eigenes Konto" fixes="eigene Konto"
E Form_fix_in_der_richtigen_lage_1_ein_eigenes_ FROM_SESSION Session_in_der_richtigen_lage

# ingest-session 2026-09-24T21:57:50Z gmail-jetzt-durchschauen-und-sortieren lang=de
V Session_gmail_jetzt_durchschauen_und_sortieren kind=session date=2026-09-24 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gmail-jetzt-durchschauen-und-sortieren.toon.md
V Focus_gmail_jetzt_durchschauen_und_sortieren kind=focus lang=de gloss="und (nicht un)" status=active
E Focus_gmail_jetzt_durchschauen_und_sortieren FROM_SESSION Session_gmail_jetzt_durchschauen_und_sortieren
V Lemma_de_fix_gmail_jetzt_durchschauen_und_sortieren kind=lemma lang=de surface="Also gut, jetzt schaust du meine Gmail im Augenbli" role=minimal-rewrite
E Lemma_de_fix_gmail_jetzt_durchschauen_und_sortieren FROM_SESSION Session_gmail_jetzt_durchschauen_und_sortieren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-24-gmail-jetzt-durchschauen-und-sortieren.toon.md
V Form_fix_gmail_jetzt_durchschauen_und_sortier kind=form lang=de surface=und fixes=un
E Form_fix_gmail_jetzt_durchschauen_und_sortier FROM_SESSION Session_gmail_jetzt_durchschauen_und_sortieren
V Form_fix_gmail_jetzt_durchschauen_und_sortier kind=form lang=de surface="schaust du meine Gmail … durch" fixes="guckst du meine Gmail … ab"
E Form_fix_gmail_jetzt_durchschauen_und_sortier FROM_SESSION Session_gmail_jetzt_durchschauen_und_sortieren

# ingest-session 2026-09-24T22:02:50Z xiaohongshu-angemeldet lang=de
V Session_xiaohongshu_angemeldet kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-xiaohongshu-angemeldet.toon.md
V Focus_xiaohongshu_angemeldet kind=focus lang=de gloss="angemeldet ist" status=active
E Focus_xiaohongshu_angemeldet FROM_SESSION Session_xiaohongshu_angemeldet
V Lemma_de_fix_xiaohongshu_angemeldet kind=lemma lang=de surface="Unter den Tabs ist ein Browser, in dem Xiaohongshu" role=minimal-rewrite
E Lemma_de_fix_xiaohongshu_angemeldet FROM_SESSION Session_xiaohongshu_angemeldet SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-xiaohongshu-angemeldet.toon.md
V Form_fix_xiaohongshu_angemeldet_0_in_dem_xiao kind=form lang=de surface="in dem Xiaohongshu angemeldet ist" fixes="mit Xiaohongshu einloggen"
E Form_fix_xiaohongshu_angemeldet_0_in_dem_xiao FROM_SESSION Session_xiaohongshu_angemeldet

# ingest-session 2026-09-24T22:07:59Z mit-diesem-konto lang=de
V Session_mit_diesem_konto kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-mit-diesem-konto.toon.md
V Focus_mit_diesem_konto kind=focus lang=de gloss="mit diesem Konto (mit + Dat)" status=active
E Focus_mit_diesem_konto FROM_SESSION Session_mit_diesem_konto
V Lemma_de_fix_mit_diesem_konto kind=lemma lang=de surface="Hören Sie an diesem Punkt noch nicht auf. Entdecke" role=minimal-rewrite
E Lemma_de_fix_mit_diesem_konto FROM_SESSION Session_mit_diesem_konto SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-mit-diesem-konto.toon.md
V Form_fix_mit_diesem_konto_0_mit_diesem_konto kind=form lang=de surface="mit diesem Konto" fixes="mit diesen Konto"
E Form_fix_mit_diesem_konto_0_mit_diesem_konto FROM_SESSION Session_mit_diesem_konto

# auto-gap 2026-09-24T22:14:12Z surface=鏌恱
V Concept_gap_zh_10dbe07d2f kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_10dbe07d2f kind=gap lang=zh surface=鏌恱 target=de status=open
V Lemma_zh_zh_10dbe07d2f kind=lemma lang=zh surface=鏌恱
E Concept_gap_zh_10dbe07d2f EXPRESSES Lemma_zh_zh_10dbe07d2f SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_10dbe07d2f GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_10dbe07d2f GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T22:14:12Z surface=澶
V Concept_gap_zh_11757fd2fc kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_11757fd2fc kind=gap lang=zh surface=澶 target=de status=open
V Lemma_zh_zh_11757fd2fc kind=lemma lang=zh surface=澶
E Concept_gap_zh_11757fd2fc EXPRESSES Lemma_zh_zh_11757fd2fc SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_11757fd2fc GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_11757fd2fc GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T22:14:12Z surface=鐣欏
V Concept_gap_zh_77132e61c5 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_77132e61c5 kind=gap lang=zh surface=鐣欏 target=de status=open
V Lemma_zh_zh_77132e61c5 kind=lemma lang=zh surface=鐣欏
E Concept_gap_zh_77132e61c5 EXPRESSES Lemma_zh_zh_77132e61c5 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_77132e61c5 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_77132e61c5 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T22:14:12Z surface=鏈烘瀯澶
V Concept_gap_zh_f6a50b47ee kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_f6a50b47ee kind=gap lang=zh surface=鏈烘瀯澶 target=de status=open
V Lemma_zh_zh_f6a50b47ee kind=lemma lang=zh surface=鏈烘瀯澶
E Concept_gap_zh_f6a50b47ee EXPRESSES Lemma_zh_zh_f6a50b47ee SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_f6a50b47ee GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_f6a50b47ee GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T22:14:12Z surface=潙锛岃
V Concept_gap_zh_9d4c915ee8 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_9d4c915ee8 kind=gap lang=zh surface=潙锛岃 target=de status=open
V Lemma_zh_zh_9d4c915ee8 kind=lemma lang=zh surface=潙锛岃
E Concept_gap_zh_9d4c915ee8 EXPRESSES Lemma_zh_zh_9d4c915ee8 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_9d4c915ee8 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_9d4c915ee8 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-24T22:14:12Z surface=澹佸瀿
V Concept_gap_zh_014691f4df kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_014691f4df kind=gap lang=zh surface=澹佸瀿 target=de status=open
V Lemma_zh_zh_014691f4df kind=lemma lang=zh surface=澹佸瀿
E Concept_gap_zh_014691f4df EXPRESSES Lemma_zh_zh_014691f4df SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_014691f4df GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_014691f4df GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T22:18:35Z einschliesslich-konto lang=de
V Session_einschliesslich_konto kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-einschliesslich-konto.toon.md
V Focus_einschliesslich_konto kind=focus lang=de gloss="einschließlich Konto" status=active
E Focus_einschliesslich_konto FROM_SESSION Session_einschliesslich_konto
V Lemma_de_fix_einschliesslich_konto kind=lemma lang=de surface="„某xu大学留学机构天坑，请壁垒“ ist wichtig. Protokollieren Sie " role=minimal-rewrite
E Lemma_de_fix_einschliesslich_konto FROM_SESSION Session_einschliesslich_konto SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-einschliesslich-konto.toon.md
V Form_fix_einschliesslich_konto_0_einschlie_li kind=form lang=de surface="einschließlich Konto" fixes="inkl konto"
E Form_fix_einschliesslich_konto_0_einschlie_li FROM_SESSION Session_einschliesslich_konto
V Form_fix_einschliesslich_konto_1_protokollier kind=form lang=de surface="protokollieren Sie ihn" fixes="protokollieren Sie sie"
E Form_fix_einschliesslich_konto_1_protokollier FROM_SESSION Session_einschliesslich_konto

# ingest-session 2026-09-24T22:24:21Z mehr-konten lang=de
V Session_mehr_konten kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-mehr-konten.toon.md
V Focus_mehr_konten kind=focus lang=de gloss="mehr Konten" status=active
E Focus_mehr_konten FROM_SESSION Session_mehr_konten
V Lemma_de_fix_mehr_konten kind=lemma lang=de surface="Es gibt noch mehr Konten. Sammeln Sie die Belege f" role=minimal-rewrite
E Lemma_de_fix_mehr_konten FROM_SESSION Session_mehr_konten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-mehr-konten.toon.md
V Form_fix_mehr_konten_0_mehr_konten kind=form lang=de surface="mehr Konten" fixes="mehr Konto"
E Form_fix_mehr_konten_0_mehr_konten FROM_SESSION Session_mehr_konten
V Form_fix_mehr_konten_1_die_belege_f_r_die_irr kind=form lang=de surface="die Belege für die irreführende Werbung" fixes="den Beweis für 虚假宣传"
E Form_fix_mehr_konten_1_die_belege_f_r_die_irr FROM_SESSION Session_mehr_konten

# ingest-session 2026-09-24T22:28:58Z 2026-09-25-quantitative-investitionen-werkzeug lang=de
V Session_2026_09_25_quantitative_investitionen_we kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-quantitative-investitionen-werkzeug.toon.md
V Focus_2026_09_25_quantitative_investitionen_we kind=focus lang=de gloss="dieses Werkzeug (Werkzeug = Neutrum)" status=active
E Focus_2026_09_25_quantitative_investitionen_we FROM_SESSION Session_2026_09_25_quantitative_investitionen_we
V Lemma_de_fix_2026_09_25_quantitative_investitionen_we kind=lemma lang=de surface="So, jetzt bin ich auch mit quantitativen Investiti" role=minimal-rewrite
E Lemma_de_fix_2026_09_25_quantitative_investitionen_we FROM_SESSION Session_2026_09_25_quantitative_investitionen_we SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-quantitative-investitionen-werkzeug.toon.md
V Form_fix_2026_09_25_quantitative_investitione kind=form lang=de surface="mit quantitativen Investitionen" fixes="brief: mit dem Quantitative In"
E Form_fix_2026_09_25_quantitative_investitione FROM_SESSION Session_2026_09_25_quantitative_investitionen_we
V Form_fix_2026_09_25_quantitative_investitione kind=form lang=de surface="dieses Werkzeug" fixes="brief: diese Werkzeug"
E Form_fix_2026_09_25_quantitative_investitione FROM_SESSION Session_2026_09_25_quantitative_investitionen_we
V Form_fix_2026_09_25_quantitative_investitione kind=form lang=de surface="'also / darum / deshalb'; pattern=chat_r" fixes="brief: doppeltes 'so ... so'"
E Form_fix_2026_09_25_quantitative_investitione FROM_SESSION Session_2026_09_25_quantitative_investitionen_we

# ingest-session 2026-09-24T22:31:08Z untereinander lang=de
V Session_untereinander kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-untereinander.toon.md
V Focus_untereinander kind=focus lang=de gloss=untereinander status=active
E Focus_untereinander FROM_SESSION Session_untereinander
V Lemma_de_fix_untereinander kind=lemma lang=de surface="Genau. Jetzt sind Sie der professionelle Aktenfors" role=minimal-rewrite
E Lemma_de_fix_untereinander FROM_SESSION Session_untereinander SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-untereinander.toon.md
V Form_fix_untereinander_0_untereinander kind=form lang=de surface=untereinander fixes=undereinander
E Form_fix_untereinander_0_untereinander FROM_SESSION Session_untereinander
V Form_fix_untereinander_1_die_forschungserkenn kind=form lang=de surface="die Forschungserkenntnisse dazu" fixes="Forschungs insights darin"
E Form_fix_untereinander_1_die_forschungserkenn FROM_SESSION Session_untereinander

# ingest-session 2026-09-24T22:34:58Z bcc-chinesische-studierende lang=de
V Session_bcc_chinesische_studierende kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bcc-chinesische-studierende.toon.md
V Focus_bcc_chinesische_studierende kind=focus lang=de gloss="per Bcc" status=active
E Focus_bcc_chinesische_studierende FROM_SESSION Session_bcc_chinesische_studierende
V Lemma_de_fix_bcc_chinesische_studierende kind=lemma lang=de surface="Der 350-Euro-Text ist per Bcc verschickt. Bei Cybe" role=minimal-rewrite
E Lemma_de_fix_bcc_chinesische_studierende FROM_SESSION Session_bcc_chinesische_studierende SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bcc-chinesische-studierende.toon.md
V Form_fix_bcc_chinesische_studierende_0_ist_pe kind=form lang=de surface="ist per Bcc verschickt" fixes="is bcc-ed"
E Form_fix_bcc_chinesische_studierende_0_ist_pe FROM_SESSION Session_bcc_chinesische_studierende
V Form_fix_bcc_chinesische_studierende_1_chines kind=form lang=de surface="chinesische Studierende" fixes="Chinesische Student:innen"
E Form_fix_bcc_chinesische_studierende_1_chines FROM_SESSION Session_bcc_chinesische_studierende

# ingest-session 2026-09-24T22:40:33Z vollstaendiger-wortlaut lang=de
V Session_vollstaendiger_wortlaut kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-vollstaendiger-wortlaut.toon.md
V Focus_vollstaendiger_wortlaut kind=focus lang=de gloss="im vollständigen Wortlaut" status=active
E Focus_vollstaendiger_wortlaut FROM_SESSION Session_vollstaendiger_wortlaut
V Lemma_de_fix_vollstaendiger_wortlaut kind=lemma lang=de surface="Allen chinesischen Inhalt sollen wir ins Deutsche " role=minimal-rewrite
E Lemma_de_fix_vollstaendiger_wortlaut FROM_SESSION Session_vollstaendiger_wortlaut SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-vollstaendiger-wortlaut.toon.md
V Form_fix_vollstaendiger_wortlaut_0_allen_chin kind=form lang=de surface="allen chinesischen Inhalt" fixes="der Chinesische Inhalt"
E Form_fix_vollstaendiger_wortlaut_0_allen_chin FROM_SESSION Session_vollstaendiger_wortlaut
V Form_fix_vollstaendiger_wortlaut_1_im_vollst_ kind=form lang=de surface="im vollständigen Wortlaut erfassen" fixes="mit voll Text erfassen"
E Form_fix_vollstaendiger_wortlaut_1_im_vollst_ FROM_SESSION Session_vollstaendiger_wortlaut

# ingest-session 2026-09-24T22:44:44Z wie-einen-roman lang=de
V Session_wie_einen_roman kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-wie-einen-roman.toon.md
V Focus_wie_einen_roman kind=focus lang=de gloss="wie einen Roman" status=active
E Focus_wie_einen_roman FROM_SESSION Session_wie_einen_roman
V Lemma_de_fix_wie_einen_roman kind=lemma lang=de surface="Genau. Nur sieben Seiten sind nicht genug. Ich bra" role=minimal-rewrite
E Lemma_de_fix_wie_einen_roman FROM_SESSION Session_wie_einen_roman SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-wie-einen-roman.toon.md
V Form_fix_wie_einen_roman_0_nur_sieben_seiten kind=form lang=de surface="nur sieben Seiten" fixes="nur 7 seite"
E Form_fix_wie_einen_roman_0_nur_sieben_seiten FROM_SESSION Session_wie_einen_roman
V Form_fix_wie_einen_roman_1_wie_einen_roman kind=form lang=de surface="wie einen Roman" fixes="wie ein Roman"
E Form_fix_wie_einen_roman_1_wie_einen_roman FROM_SESSION Session_wie_einen_roman

# ingest-session 2026-09-24T22:48:24Z alle-vorhandenen-dateien lang=de
V Session_alle_vorhandenen_dateien kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-alle-vorhandenen-dateien.toon.md
V Focus_alle_vorhandenen_dateien kind=focus lang=de gloss="alle vorhandenen Dateien" status=active
E Focus_alle_vorhandenen_dateien FROM_SESSION Session_alle_vorhandenen_dateien
V Lemma_de_fix_alle_vorhandenen_dateien kind=lemma lang=de surface="Die ganze Geschichte der XU und von Cybernaut. Ben" role=minimal-rewrite
E Lemma_de_fix_alle_vorhandenen_dateien FROM_SESSION Session_alle_vorhandenen_dateien SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-alle-vorhandenen-dateien.toon.md
V Form_fix_alle_vorhandenen_dateien_0_alle_vorh kind=form lang=de surface="alle vorhandenen Dateien" fixes="ALLER DATEI vorhanden"
E Form_fix_alle_vorhandenen_dateien_0_alle_vorh FROM_SESSION Session_alle_vorhandenen_dateien
V Form_fix_alle_vorhandenen_dateien_1_einschlie kind=form lang=de surface="einschließlich einer PlantUML-Analyse" fixes="inkl PlantUML Analyse"
E Form_fix_alle_vorhandenen_dateien_1_einschlie FROM_SESSION Session_alle_vorhandenen_dateien

# auto-gap 2026-09-24T22:48:47Z surface=鍙蹭功
V Concept_gap_zh_cbdf4fd20a kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_cbdf4fd20a kind=gap lang=zh surface=鍙蹭功 target=de status=open
V Lemma_zh_zh_cbdf4fd20a kind=lemma lang=zh surface=鍙蹭功
E Concept_gap_zh_cbdf4fd20a EXPRESSES Lemma_zh_zh_cbdf4fd20a SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_cbdf4fd20a GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_cbdf4fd20a GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-24T22:50:51Z chronik-mit-kommentaren lang=de
V Session_chronik_mit_kommentaren kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-chronik-mit-kommentaren.toon.md
V Focus_chronik_mit_kommentaren kind=focus lang=de gloss=chronologisch status=active
E Focus_chronik_mit_kommentaren FROM_SESSION Session_chronik_mit_kommentaren
V Lemma_de_fix_chronik_mit_kommentaren kind=lemma lang=de surface="Nach allen E-Mails im EML-Format fügen Sie sie chr" role=minimal-rewrite
E Lemma_de_fix_chronik_mit_kommentaren FROM_SESSION Session_chronik_mit_kommentaren SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-chronik-mit-kommentaren.toon.md
V Form_fix_chronik_mit_kommentaren_0_allen_e_ma kind=form lang=de surface="allen E-Mails im EML-Format" fixes="aller EML-formatten E-Mails"
E Form_fix_chronik_mit_kommentaren_0_allen_e_ma FROM_SESSION Session_chronik_mit_kommentaren
V Form_fix_chronik_mit_kommentaren_1_mit_kommen kind=form lang=de surface="mit Kommentaren" fixes="mit Kommentare"
E Form_fix_chronik_mit_kommentaren_1_mit_kommen FROM_SESSION Session_chronik_mit_kommentaren

# ingest-session 2026-09-24T22:58:18Z negativ-volltext lang=de
V Session_negativ_volltext kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-negativ-volltext.toon.md
V Focus_negativ_volltext kind=focus lang=de gloss="draußen bleiben" status=active
E Focus_negativ_volltext FROM_SESSION Session_negativ_volltext
V Lemma_de_fix_negativ_volltext kind=lemma lang=de surface="Unbezogene und positive E-Mails sollen draußen ble" role=minimal-rewrite
E Lemma_de_fix_negativ_volltext FROM_SESSION Session_negativ_volltext SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-negativ-volltext.toon.md
V Form_fix_negativ_volltext_0_wertvoll kind=form lang=de surface=wertvoll fixes=wertsvoll
E Form_fix_negativ_volltext_0_wertvoll FROM_SESSION Session_negativ_volltext
V Form_fix_negativ_volltext_1_mit_kommentaren kind=form lang=de surface="mit Kommentaren" fixes="mit Kommentare"
E Form_fix_negativ_volltext_1_mit_kommentaren FROM_SESSION Session_negativ_volltext

# ingest-session 2026-09-24T23:20:38Z an-die-reporterin lang=de
V Session_an_die_reporterin kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-an-die-reporterin.toon.md
V Focus_an_die_reporterin kind=focus lang=de gloss="an die Reporterin (an + Akk)" status=active
E Focus_an_die_reporterin FROM_SESSION Session_an_die_reporterin
V Lemma_de_fix_an_die_reporterin kind=lemma lang=de surface="Inklusive Wortlaut der E-Mails. Machen Sie den Bri" role=minimal-rewrite
E Lemma_de_fix_an_die_reporterin FROM_SESSION Session_an_die_reporterin SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-an-die-reporterin.toon.md
V Form_fix_an_die_reporterin_0_an_die_reporteri kind=form lang=de surface="an die Reporterin" fixes="zur Reporterin"
E Form_fix_an_die_reporterin_0_an_die_reporteri FROM_SESSION Session_an_die_reporterin
V Form_fix_an_die_reporterin_1_machen_sie_den_b kind=form lang=de surface="Machen Sie den Brief sendefertig" fixes="Setzen Sie sich bereit"
E Form_fix_an_die_reporterin_1_machen_sie_den_b FROM_SESSION Session_an_die_reporterin

# ingest-session 2026-09-24T23:27:26Z zip-in-der lang=de
V Session_zip_in_der kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-zip-in-der.toon.md
V Focus_zip_in_der kind=focus lang=de gloss="in der (in + Dat)" status=active
E Focus_zip_in_der FROM_SESSION Session_zip_in_der
V Lemma_de_fix_zip_in_der kind=lemma lang=de surface="Machen Sie eine ZIP-Datei, in der die EML-Dateien " role=minimal-rewrite
E Lemma_de_fix_zip_in_der FROM_SESSION Session_zip_in_der SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-zip-in-der.toon.md
V Form_fix_zip_in_der_0_in_der kind=form lang=de surface="in der" fixes=indem
E Form_fix_zip_in_der_0_in_der FROM_SESSION Session_zip_in_der
V Form_fix_zip_in_der_1_die_eml_dateien kind=form lang=de surface="die EML-Dateien" fixes="EML datei"
E Form_fix_zip_in_der_1_die_eml_dateien FROM_SESSION Session_zip_in_der

# ingest-session 2026-09-25T08:06:21Z ein-neuer-tag lang=de
V Session_ein_neuer_tag kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-ein-neuer-tag.toon.md
V Focus_ein_neuer_tag kind=focus lang=de gloss="ein neuer Tag (Nom. m.)" status=active
E Focus_ein_neuer_tag FROM_SESSION Session_ein_neuer_tag
V Lemma_de_fix_ein_neuer_tag kind=lemma lang=de surface="Also gut, heute ist der 25.9.2026, also ein neuer " role=minimal-rewrite
E Lemma_de_fix_ein_neuer_tag FROM_SESSION Session_ein_neuer_tag SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-ein-neuer-tag.toon.md
V Form_fix_ein_neuer_tag_0_ein_neuer_tag kind=form lang=de surface="ein neuer Tag" fixes="neue Tag"
E Form_fix_ein_neuer_tag_0_ein_neuer_tag FROM_SESSION Session_ein_neuer_tag
V Form_fix_ein_neuer_tag_1_also_ein_neuer_tag kind=form lang=de surface="also ein neuer Tag" fixes="so neue Tag"
E Form_fix_ein_neuer_tag_1_also_ein_neuer_tag FROM_SESSION Session_ein_neuer_tag

# auto-gap 2026-09-25T08:06:31Z surface=瀹跺姟娲
V Concept_gap_zh_9079d30346 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_9079d30346 kind=gap lang=zh surface=瀹跺姟娲 target=de status=open
V Lemma_zh_zh_9079d30346 kind=lemma lang=zh surface=瀹跺姟娲
E Concept_gap_zh_9079d30346 EXPRESSES Lemma_zh_zh_9079d30346 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_9079d30346 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_9079d30346 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-25T08:08:08Z die-privaten-daten lang=de
V Session_die_privaten_daten kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-die-privaten-daten.toon.md
V Focus_die_privaten_daten kind=focus lang=de gloss="die privaten Daten (Akk. Pl.)" status=active
E Focus_die_privaten_daten FROM_SESSION Session_die_privaten_daten
V Lemma_de_fix_die_privaten_daten kind=lemma lang=de surface="Ich habe die privaten Daten im öffentlichen Bereic" role=minimal-rewrite
E Lemma_de_fix_die_privaten_daten FROM_SESSION Session_die_privaten_daten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-die-privaten-daten.toon.md
V Form_fix_die_privaten_daten_0_die_privaten_da kind=form lang=de surface="die privaten Daten" fixes="den privaten Daten"
E Form_fix_die_privaten_daten_0_die_privaten_da FROM_SESSION Session_die_privaten_daten
V Form_fix_die_privaten_daten_1_im_ffentlichen_ kind=form lang=de surface="im öffentlichen Bereich" fixes="vom öffentlichem Gebiet"
E Form_fix_die_privaten_daten_1_im_ffentlichen_ FROM_SESSION Session_die_privaten_daten
V Form_fix_die_privaten_daten_2_automatisierung kind=form lang=de surface="Automatisierung von Hausarbeit" fixes="Automatisierung auf 家务活"
E Form_fix_die_privaten_daten_2_automatisierung FROM_SESSION Session_die_privaten_daten

# ingest-session 2026-09-25T08:09:22Z leide-an-einer-krankheit lang=de
V Session_leide_an_einer_krankheit kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-leide-an-einer-krankheit.toon.md
V Focus_leide_an_einer_krankheit kind=focus lang=de gloss="leiden an + Dat." status=active
E Focus_leide_an_einer_krankheit FROM_SESSION Session_leide_an_einer_krankheit
V Lemma_de_fix_leide_an_einer_krankheit kind=lemma lang=de surface="Heute leide ich erheblich an einer Krankheit, d. h" role=minimal-rewrite
E Lemma_de_fix_leide_an_einer_krankheit FROM_SESSION Session_leide_an_einer_krankheit SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-leide-an-einer-krankheit.toon.md
V Form_fix_leide_an_einer_krankheit_0_erheblich kind=form lang=de surface="erheblich an einer Krankheit" fixes="erheblich Krankheit"
E Form_fix_leide_an_einer_krankheit_0_erheblich FROM_SESSION Session_leide_an_einer_krankheit
V Form_fix_leide_an_einer_krankheit_1_halsschme kind=form lang=de surface=Halsschmerzen fixes="Sore throat"
E Form_fix_leide_an_einer_krankheit_1_halsschme FROM_SESSION Session_leide_an_einer_krankheit
V Form_fix_leide_an_einer_krankheit_2_habe_ich_ kind=form lang=de surface="habe ich eine Infektion" fixes="gibt es Infektionen bei mir"
E Form_fix_leide_an_einer_krankheit_2_habe_ich_ FROM_SESSION Session_leide_an_einer_krankheit

# auto-gap 2026-09-25T08:10:59Z surface=los
V Concept_gap_es_los kind=concept gloss=unknown-expression-in-de status=open
V Gap_es_los kind=gap lang=es surface=los target=de status=open
V Lemma_es_es_los kind=lemma lang=es surface=los
E Concept_gap_es_los EXPRESSES Lemma_es_es_los SOURCE=hook/beforeSubmitPrompt
E Lemma_es_es_los GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_es_los GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-25T08:22:36Z geht-mich-nichts-an lang=de
V Session_geht_mich_nichts_an kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-geht-mich-nichts-an.toon.md
V Focus_geht_mich_nichts_an kind=focus lang=de gloss="das geht mich nichts an (Akk.)" status=active
E Focus_geht_mich_nichts_an FROM_SESSION Session_geht_mich_nichts_an
V Lemma_de_fix_geht_mich_nichts_an kind=lemma lang=de surface="Ok, starten Sie mit dem Bearbeiten meiner E-Mails." role=minimal-rewrite
E Lemma_de_fix_geht_mich_nichts_an FROM_SESSION Session_geht_mich_nichts_an SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-geht-mich-nichts-an.toon.md
V Form_fix_geht_mich_nichts_an_0_es_geht_mich_n kind=form lang=de surface="es geht mich nichts an" fixes="es geht mir nichts an"
E Form_fix_geht_mich_nichts_an_0_es_geht_mich_n FROM_SESSION Session_geht_mich_nichts_an
V Form_fix_geht_mich_nichts_an_1_nicht_angegang kind=form lang=de surface="nicht angegangen bin" fixes="nicht angegangen"
E Form_fix_geht_mich_nichts_an_1_nicht_angegang FROM_SESSION Session_geht_mich_nichts_an
V Form_fix_geht_mich_nichts_an_2_kann_weg kind=form lang=de surface="kann weg" fixes="kann sich los werden"
E Form_fix_geht_mich_nichts_an_2_kann_weg FROM_SESSION Session_geht_mich_nichts_an

# ingest-session 2026-09-25T08:24:36Z zwei-wichtigsten-ordner lang=de
V Session_zwei_wichtigsten_ordner kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-zwei-wichtigsten-ordner.toon.md
V Focus_zwei_wichtigsten_ordner kind=focus lang=de gloss="die zwei wichtigsten Ordner" status=active
E Focus_zwei_wichtigsten_ordner FROM_SESSION Session_zwei_wichtigsten_ordner
V Lemma_de_fix_zwei_wichtigsten_ordner kind=lemma lang=de surface="Genau, die zwei wichtigsten Ordner heißen Job und " role=minimal-rewrite
E Lemma_de_fix_zwei_wichtigsten_ordner FROM_SESSION Session_zwei_wichtigsten_ordner SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-zwei-wichtigsten-ordner.toon.md
V Form_fix_zwei_wichtigsten_ordner_0_die_zwei_w kind=form lang=de surface="die zwei wichtigsten Ordner heißen" fixes="zwei wichtigester Ordnern laut"
E Form_fix_zwei_wichtigsten_ordner_0_die_zwei_w FROM_SESSION Session_zwei_wichtigsten_ordner
V Form_fix_zwei_wichtigsten_ordner_1_einschlie_ kind=form lang=de surface="einschließlich beider Namelos-E-Mails" fixes="Inkl beide namelos E-Mail"
E Form_fix_zwei_wichtigsten_ordner_1_einschlie_ FROM_SESSION Session_zwei_wichtigsten_ordner

# ingest-session 2026-09-25T08:25:14Z einen-auftrag-gebe lang=de
V Session_einen_auftrag_gebe kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-einen-auftrag-gebe.toon.md
V Focus_einen_auftrag_gebe kind=focus lang=de gloss="einen Auftrag geben (Akk.)" status=active
E Focus_einen_auftrag_gebe FROM_SESSION Session_einen_auftrag_gebe
V Lemma_de_fix_einen_auftrag_gebe kind=lemma lang=de surface="So, es funktioniert sowieso, dass ich dir einen Au" role=minimal-rewrite
E Lemma_de_fix_einen_auftrag_gebe FROM_SESSION Session_einen_auftrag_gebe SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-einen-auftrag-gebe.toon.md
V Form_fix_einen_auftrag_gebe_0_einen_auftrag_g kind=form lang=de surface="einen Auftrag gebe" fixes="eine Forderung geben"
E Form_fix_einen_auftrag_gebe_0_einen_auftrag_g FROM_SESSION Session_einen_auftrag_gebe
V Form_fix_einen_auftrag_gebe_1_manuell_auf_so_ kind=form lang=de surface="manuell, auf so umfassende Art und Weise" fixes="mit manuell"
E Form_fix_einen_auftrag_gebe_1_manuell_auf_so_ FROM_SESSION Session_einen_auftrag_gebe
V Form_fix_einen_auftrag_gebe_2_r_ckmeldung_6a9 kind=form lang=de surface=Rückmeldung fixes="Rückmeldung zurück"
E Form_fix_einen_auftrag_gebe_2_r_ckmeldung_6a9 FROM_SESSION Session_einen_auftrag_gebe

# ingest-session 2026-09-25T08:26:19Z nicht-nur-von-worldquant lang=de
V Session_nicht_nur_von_worldquant kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-nicht-nur-von-worldquant.toon.md
V Focus_nicht_nur_von_worldquant kind=focus lang=de gloss="nicht nur von (von + Dat.)" status=active
E Focus_nicht_nur_von_worldquant FROM_SESSION Session_nicht_nur_von_worldquant
V Lemma_de_fix_nicht_nur_von_worldquant kind=lemma lang=de surface="Nein, die Job-Bewerbungen sind nicht nur von World" role=minimal-rewrite
E Lemma_de_fix_nicht_nur_von_worldquant FROM_SESSION Session_nicht_nur_von_worldquant SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-nicht-nur-von-worldquant.toon.md
V Form_fix_nicht_nur_von_worldquant_0_bewerbung kind=form lang=de surface=Bewerbungen fixes=Webungen
E Form_fix_nicht_nur_von_worldquant_0_bewerbung FROM_SESSION Session_nicht_nur_von_worldquant
V Form_fix_nicht_nur_von_worldquant_1_nicht_nur kind=form lang=de surface="nicht nur von WorldQuant" fixes="nicht nur vom WorldQuant"
E Form_fix_nicht_nur_von_worldquant_1_nicht_nur FROM_SESSION Session_nicht_nur_von_worldquant

# auto-gap 2026-09-25T14:48:53Z surface=鐩磋仒
V Concept_gap_zh_118099734a kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_118099734a kind=gap lang=zh surface=鐩磋仒 target=de status=open
V Lemma_zh_zh_118099734a kind=lemma lang=zh surface=鐩磋仒
E Concept_gap_zh_118099734a EXPRESSES Lemma_zh_zh_118099734a SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_118099734a GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_118099734a GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-25T14:52:02Z setzen-sie-fort lang=de
V Session_setzen_sie_fort kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-setzen-sie-fort.toon.md
V Focus_setzen_sie_fort kind=focus lang=de gloss="sich einloggen (bei + Dat.)" status=active
E Focus_setzen_sie_fort FROM_SESSION Session_setzen_sie_fort
V Lemma_de_fix_setzen_sie_fort kind=lemma lang=de surface="Ach so, ich habe Ihnen geholfen, sich bei LinkedIn" role=minimal-rewrite
E Lemma_de_fix_setzen_sie_fort FROM_SESSION Session_setzen_sie_fort SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-setzen-sie-fort.toon.md
V Form_fix_setzen_sie_fort_0_ihnen kind=form lang=de surface=Ihnen fixes=dir
E Form_fix_setzen_sie_fort_0_ihnen FROM_SESSION Session_setzen_sie_fort
V Form_fix_setzen_sie_fort_1_sich_bei_linkedin_ kind=form lang=de surface="sich bei LinkedIn einzuloggen" fixes="LinkedIn einzuloggen"
E Form_fix_setzen_sie_fort_1_sich_bei_linkedin_ FROM_SESSION Session_setzen_sie_fort
V Form_fix_setzen_sie_fort_2_setzen_sie_fort kind=form lang=de surface="setzen Sie fort" fixes="setzen Sie sich fort"
E Form_fix_setzen_sie_fort_2_setzen_sie_fort FROM_SESSION Session_setzen_sie_fort

# ingest-session 2026-09-25T14:54:06Z sich-bewerben lang=de
V Session_sich_bewerben kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-sich-bewerben.toon.md
V Focus_sich_bewerben kind=focus lang=de gloss="sich bewerben" status=active
E Focus_sich_bewerben FROM_SESSION Session_sich_bewerben
V Lemma_de_fix_sich_bewerben kind=lemma lang=de surface="Ach so, ist es demnächst bei dir möglich, dich von" role=minimal-rewrite
E Lemma_de_fix_sich_bewerben FROM_SESSION Session_sich_bewerben SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-sich-bewerben.toon.md
V Form_fix_sich_bewerben_0_dich_zu_bewerben kind=form lang=de surface="dich zu bewerben" fixes="es zu bewerben"
E Form_fix_sich_bewerben_0_dich_zu_bewerben FROM_SESSION Session_sich_bewerben
V Form_fix_sich_bewerben_1_ist_es_demn_chst_bei kind=form lang=de surface="ist es demnächst bei dir möglich" fixes="demnächst ist es möglich bei d"
E Form_fix_sich_bewerben_1_ist_es_demn_chst_bei FROM_SESSION Session_sich_bewerben

# ingest-session 2026-09-25T14:56:08Z was-fehlt lang=de
V Session_was_fehlt kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-was-fehlt.toon.md
V Focus_was_fehlt kind=focus lang=de gloss="was fehlt" status=active
E Focus_was_fehlt FROM_SESSION Session_was_fehlt
V Lemma_de_fix_was_fehlt kind=lemma lang=de surface="Kannst du den Tab sehen? Es ist schon eingeloggt. " role=minimal-rewrite
E Lemma_de_fix_was_fehlt FROM_SESSION Session_was_fehlt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-was-fehlt.toon.md
V Form_fix_was_fehlt_0_eingeloggt kind=form lang=de surface=eingeloggt fixes=logged-in
E Form_fix_was_fehlt_0_eingeloggt FROM_SESSION Session_was_fehlt
V Form_fix_was_fehlt_1_was_fehlt kind=form lang=de surface="was fehlt" fixes="was ist fehlend"
E Form_fix_was_fehlt_1_was_fehlt FROM_SESSION Session_was_fehlt

# ingest-session 2026-09-25T15:00:22Z die-pagnos-stelle lang=de
V Session_die_pagnos_stelle kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-die-pagnos-stelle.toon.md
V Focus_die_pagnos_stelle kind=focus lang=de gloss="sich auf eine Stelle bewerben" status=active
E Focus_die_pagnos_stelle FROM_SESSION Session_die_pagnos_stelle
V Lemma_de_fix_die_pagnos_stelle kind=lemma lang=de surface="Kannst du sie einfach besuchen und dich darauf bew" role=minimal-rewrite
E Lemma_de_fix_die_pagnos_stelle FROM_SESSION Session_die_pagnos_stelle SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-die-pagnos-stelle.toon.md
V Form_fix_die_pagnos_stelle_0_dich_darauf_bewe kind=form lang=de surface="dich darauf bewerben" fixes="es zu bewerben"
E Form_fix_die_pagnos_stelle_0_dich_darauf_bewe FROM_SESSION Session_die_pagnos_stelle
V Form_fix_die_pagnos_stelle_1_die_pagnos_stell kind=form lang=de surface="die PAGNOS-Stelle" fixes="PAGNOS stelle"
E Form_fix_die_pagnos_stelle_1_die_pagnos_stell FROM_SESSION Session_die_pagnos_stelle

# ingest-session 2026-09-25T15:08:32Z abwechselnd-stellen lang=de
V Session_abwechselnd_stellen kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-abwechselnd-stellen.toon.md
V Focus_abwechselnd_stellen kind=focus lang=de gloss="eine andere Seite (sich öffnen)" status=active
E Focus_abwechselnd_stellen FROM_SESSION Session_abwechselnd_stellen
V Lemma_de_fix_abwechselnd_stellen kind=lemma lang=de surface="Genau, schauen Sie bitte abwechselnd die Stellen i" role=minimal-rewrite
E Lemma_de_fix_abwechselnd_stellen FROM_SESSION Session_abwechselnd_stellen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-abwechselnd-stellen.toon.md
V Form_fix_abwechselnd_stellen_0_abwechselnd kind=form lang=de surface=abwechselnd fixes=aufwechselned
E Form_fix_abwechselnd_stellen_0_abwechselnd FROM_SESSION Session_abwechselnd_stellen
V Form_fix_abwechselnd_stellen_1_in_deutschland kind=form lang=de surface="in Deutschland" fixes="im Deutschland"
E Form_fix_abwechselnd_stellen_1_in_deutschland FROM_SESSION Session_abwechselnd_stellen
V Form_fix_abwechselnd_stellen_2_in_china kind=form lang=de surface="in China" fixes="im China"
E Form_fix_abwechselnd_stellen_2_in_china FROM_SESSION Session_abwechselnd_stellen
V Form_fix_abwechselnd_stellen_3_ffnet_sich_289 kind=form lang=de surface="öffnet sich" fixes="öffenet es"
E Form_fix_abwechselnd_stellen_3_ffnet_sich_289 FROM_SESSION Session_abwechselnd_stellen
V Form_fix_abwechselnd_stellen_4_eine_andere_se kind=form lang=de surface="eine andere Seite" fixes="eine anderer Seite"
E Form_fix_abwechselnd_stellen_4_eine_andere_se FROM_SESSION Session_abwechselnd_stellen

# ingest-session 2026-09-25T15:14:01Z bewerbungsverfolgung lang=de
V Session_bewerbungsverfolgung kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bewerbungsverfolgung.toon.md
V Focus_bewerbungsverfolgung kind=focus lang=de gloss="die E-Mail-Benachrichtigungen (Pl.)" status=active
E Focus_bewerbungsverfolgung FROM_SESSION Session_bewerbungsverfolgung
V Lemma_de_fix_bewerbungsverfolgung kind=lemma lang=de surface="Also gut, protokollieren Sie im privaten Bereich d" role=minimal-rewrite
E Lemma_de_fix_bewerbungsverfolgung FROM_SESSION Session_bewerbungsverfolgung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bewerbungsverfolgung.toon.md
V Form_fix_bewerbungsverfolgung_0_protokolliere kind=form lang=de surface=protokollieren fixes=protokoliieren
E Form_fix_bewerbungsverfolgung_0_protokolliere FROM_SESSION Session_bewerbungsverfolgung
V Form_fix_bewerbungsverfolgung_1_im_privaten_b kind=form lang=de surface="im privaten Bereich" fixes="in private Bereich"
E Form_fix_bewerbungsverfolgung_1_im_privaten_b FROM_SESSION Session_bewerbungsverfolgung
V Form_fix_bewerbungsverfolgung_2_die_e_mail_be kind=form lang=de surface="die E-Mail-Benachrichtigungen" fixes=Benarichtigungen
E Form_fix_bewerbungsverfolgung_2_die_e_mail_be FROM_SESSION Session_bewerbungsverfolgung
V Form_fix_bewerbungsverfolgung_3_brauche kind=form lang=de surface=brauche fixes=brache
E Form_fix_bewerbungsverfolgung_3_brauche FROM_SESSION Session_bewerbungsverfolgung
V Form_fix_bewerbungsverfolgung_4_deutschland kind=form lang=de surface=Deutschland fixes=Deustchland
E Form_fix_bewerbungsverfolgung_4_deutschland FROM_SESSION Session_bewerbungsverfolgung

# ingest-session 2026-09-25T15:17:07Z bis-das-ziel lang=de
V Session_bis_das_ziel kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bis-das-ziel.toon.md
V Focus_bis_das_ziel kind=focus lang=de gloss="bis das Ziel erreicht ist" status=active
E Focus_bis_das_ziel FROM_SESSION Session_bis_das_ziel
V Lemma_de_fix_bis_das_ziel kind=lemma lang=de surface="Also gut, machen Sie die Bewerbungen, bis das Ziel" role=minimal-rewrite
E Lemma_de_fix_bis_das_ziel FROM_SESSION Session_bis_das_ziel SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-bis-das-ziel.toon.md
V Form_fix_bis_das_ziel_0_die_bewerbungen kind=form lang=de surface="die Bewerbungen" fixes="die Bewerbung"
E Form_fix_bis_das_ziel_0_die_bewerbungen FROM_SESSION Session_bis_das_ziel
V Form_fix_bis_das_ziel_1_bis_das_ziel_erreicht kind=form lang=de surface="bis das Ziel erreicht ist" fixes="bis zum es Ziel erreicht hat"
E Form_fix_bis_das_ziel_1_bis_das_ziel_erreicht FROM_SESSION Session_bis_das_ziel

# ingest-session 2026-09-25T16:28:00Z lebenslauf-anpassen lang=de
V Session_lebenslauf_anpassen kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-lebenslauf-anpassen.toon.md
V Focus_lebenslauf_anpassen kind=focus lang=de gloss="den Lebenslauf anpassen" status=active
E Focus_lebenslauf_anpassen FROM_SESSION Session_lebenslauf_anpassen
V Lemma_de_fix_lebenslauf_anpassen kind=lemma lang=de surface="Machen Sie die Bewerbung, aber passen Sie den Lebe" role=minimal-rewrite
E Lemma_de_fix_lebenslauf_anpassen FROM_SESSION Session_lebenslauf_anpassen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-lebenslauf-anpassen.toon.md
V Form_fix_lebenslauf_anpassen_0_lebenslauf kind=form lang=de surface=Lebenslauf fixes=Resume
E Form_fix_lebenslauf_anpassen_0_lebenslauf FROM_SESSION Session_lebenslauf_anpassen
V Form_fix_lebenslauf_anpassen_1_passen_sie_an_ kind=form lang=de surface="passen Sie … an" fixes="passen Sie … nach"
E Form_fix_lebenslauf_anpassen_1_passen_sie_an_ FROM_SESSION Session_lebenslauf_anpassen

# ingest-session 2026-09-25T18:03:57Z jobbewerbung-fortsetzen lang=de
V Session_jobbewerbung_fortsetzen kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-jobbewerbung-fortsetzen.toon.md
V Focus_jobbewerbung_fortsetzen kind=focus lang=de gloss="Bestimmter Artikel vor dem Kompositum — die Jobbew" status=active
E Focus_jobbewerbung_fortsetzen FROM_SESSION Session_jobbewerbung_fortsetzen
V Lemma_de_fix_jobbewerbung_fortsetzen kind=lemma lang=de surface="Setze die Jobbewerbung fort." role=minimal-rewrite
E Lemma_de_fix_jobbewerbung_fortsetzen FROM_SESSION Session_jobbewerbung_fortsetzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-jobbewerbung-fortsetzen.toon.md
V Form_fix_jobbewerbung_fortsetzen_0_setze_die_ kind=form lang=de surface="Setze die Jobbewerbung fort." fixes="Job Bewerbung fortsetzen"
E Form_fix_jobbewerbung_fortsetzen_0_setze_die_ FROM_SESSION Session_jobbewerbung_fortsetzen

# ingest-session 2026-09-25T18:15:30Z easy-apply-begrenzung lang=de
V Session_easy_apply_begrenzung kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-easy-apply-begrenzung.toon.md
V Focus_easy_apply_begrenzung kind=focus lang=de gloss="die Begrenzung (Artikel + Rechtschreibung)" status=active
E Focus_easy_apply_begrenzung FROM_SESSION Session_easy_apply_begrenzung
V Lemma_de_fix_easy_apply_begrenzung kind=lemma lang=de surface="LinkedIn hat die Easy-Apply-Begrenzung erreicht, a" role=minimal-rewrite
E Lemma_de_fix_easy_apply_begrenzung FROM_SESSION Session_easy_apply_begrenzung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-easy-apply-begrenzung.toon.md
V Form_fix_easy_apply_begrenzung_0_die_easy_app kind=form lang=de surface="die Easy-Apply-Begrenzung" fixes="Easy Apply begrentzung"
E Form_fix_easy_apply_begrenzung_0_die_easy_app FROM_SESSION Session_easy_apply_begrenzung

# ingest-session 2026-09-25T18:24:32Z fuer-jede-stelle lang=de
V Session_fuer_jede_stelle kind=session date=2026-09-25 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-fuer-jede-stelle.toon.md
V Focus_fuer_jede_stelle kind=focus lang=de gloss="für jede Stelle (für + Akkusativ)" status=active
E Focus_fuer_jede_stelle FROM_SESSION Session_fuer_jede_stelle
V Lemma_de_fix_fuer_jede_stelle kind=lemma lang=de surface="Okay, ich bin bei BOSS angemeldet. Passen Sie den " role=minimal-rewrite
E Lemma_de_fix_fuer_jede_stelle FROM_SESSION Session_fuer_jede_stelle SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-25-fuer-jede-stelle.toon.md
V Form_fix_fuer_jede_stelle_0_f_r_jede_stelle_9 kind=form lang=de surface="für jede Stelle" fixes="für jeder Stelle"
E Form_fix_fuer_jede_stelle_0_f_r_jede_stelle_9 FROM_SESSION Session_fuer_jede_stelle

# ingest-session 2026-09-27T08:43:43Z emails-bearbeiten lang=de
V Session_emails_bearbeiten kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-emails-bearbeiten.toon.md
V Focus_emails_bearbeiten kind=focus lang=de gloss="prozessieren → bearbeiten (Falscher Freund)" status=active
E Focus_emails_bearbeiten FROM_SESSION Session_emails_bearbeiten
V Lemma_de_fix_emails_bearbeiten kind=lemma lang=de surface="Genau, heute ist der 27.9.2026, und es laufen kein" role=minimal-rewrite
E Lemma_de_fix_emails_bearbeiten FROM_SESSION Session_emails_bearbeiten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-emails-bearbeiten.toon.md
V Form_fix_emails_bearbeiten_0_bearbeiten kind=form lang=de surface=bearbeiten fixes=prozessieren
E Form_fix_emails_bearbeiten_0_bearbeiten FROM_SESSION Session_emails_bearbeiten

# ingest-session 2026-09-27T08:57:06Z bewerbungsabsage lang=de
V Session_bewerbungsabsage kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-bewerbungsabsage.toon.md
V Focus_bewerbungsabsage kind=focus lang=de gloss="indem → in denen" status=active
E Focus_bewerbungsabsage FROM_SESSION Session_bewerbungsabsage
V Lemma_de_fix_bewerbungsabsage kind=lemma lang=de surface="Löschen Sie alle E-Mails, in denen eine Bewerbungs" role=minimal-rewrite
E Lemma_de_fix_bewerbungsabsage FROM_SESSION Session_bewerbungsabsage SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-bewerbungsabsage.toon.md
V Form_fix_bewerbungsabsage_0_in_denen kind=form lang=de surface="in denen" fixes=indem
E Form_fix_bewerbungsabsage_0_in_denen FROM_SESSION Session_bewerbungsabsage

# ingest-session 2026-09-27T09:00:04Z gmail-ordner lang=de
V Session_gmail_ordner kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-gmail-ordner.toon.md
V Focus_gmail_ordner kind=focus lang=de gloss="optimistisch → idealerweise" status=active
E Focus_gmail_ordner FROM_SESSION Session_gmail_ordner
V Lemma_de_fix_gmail_ordner kind=lemma lang=de surface="Es gibt zu viele Ordner bei Gmail, die ich kaum be" role=minimal-rewrite
E Lemma_de_fix_gmail_ordner FROM_SESSION Session_gmail_ordner SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-gmail-ordner.toon.md
V Form_fix_gmail_ordner_0_idealerweise kind=form lang=de surface=idealerweise fixes=optimistisch
E Form_fix_gmail_ordner_0_idealerweise FROM_SESSION Session_gmail_ordner

# ingest-session 2026-09-27T09:04:39Z tag-starten-leiden lang=de
V Session_tag_starten_leiden kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tag-starten-leiden.toon.md
V Focus_tag_starten_leiden kind=focus lang=de gloss="Nimm das in .private auf (in + Akk)" status=active
E Focus_tag_starten_leiden FROM_SESSION Session_tag_starten_leiden
V Lemma_de_fix_tag_starten_leiden kind=lemma lang=de surface="Ich starte heute, am 27.9.2026, meinen Tag. Die le" role=minimal-rewrite
E Lemma_de_fix_tag_starten_leiden FROM_SESSION Session_tag_starten_leiden SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tag-starten-leiden.toon.md
V Form_fix_tag_starten_leiden_0_nimm_das_in_pri kind=form lang=de surface="Nimm das in .private auf" fixes="Protokollieren Sie diese Leide"
E Form_fix_tag_starten_leiden_0_nimm_das_in_pri FROM_SESSION Session_tag_starten_leiden
V Form_fix_tag_starten_leiden_1_litt kind=form lang=de surface=litt fixes=leidete
E Form_fix_tag_starten_leiden_1_litt FROM_SESSION Session_tag_starten_leiden
V Form_fix_tag_starten_leiden_2_ist_die_erh_hte kind=form lang=de surface="ist die erhöhte Temperatur weggegangen" fixes="hat höhe Temeratur weg gegange"
E Form_fix_tag_starten_leiden_2_ist_die_erh_hte FROM_SESSION Session_tag_starten_leiden
V Form_fix_tag_starten_leiden_3_s_uregef_hl_im_ kind=form lang=de surface="Säuregefühl im unteren Trapezius" fixes="Säuresgefühl bei unten Trapezi"
E Form_fix_tag_starten_leiden_3_s_uregef_hl_im_ FROM_SESSION Session_tag_starten_leiden

# ingest-session 2026-09-27T09:09:27Z meinen-tag-nachrichten lang=de
V Session_meinen_tag_nachrichten kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-meinen-tag-nachrichten.toon.md
V Focus_meinen_tag_nachrichten kind=focus lang=de gloss="meinen Tag (Akk. m.)" status=active
E Focus_meinen_tag_nachrichten FROM_SESSION Session_meinen_tag_nachrichten
V Lemma_de_fix_meinen_tag_nachrichten kind=lemma lang=de surface="Ich starte meinen Tag am 27.9.2026. Geben Sie mir " role=minimal-rewrite
E Lemma_de_fix_meinen_tag_nachrichten FROM_SESSION Session_meinen_tag_nachrichten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-meinen-tag-nachrichten.toon.md
V Form_fix_meinen_tag_nachrichten_0_meinen_tag kind=form lang=de surface="meinen Tag" fixes="mein Tag"
E Form_fix_meinen_tag_nachrichten_0_meinen_tag FROM_SESSION Session_meinen_tag_nachrichten
V Form_fix_meinen_tag_nachrichten_1_ein_l_ngere kind=form lang=de surface="ein längeres deutsches YouTube-Video" fixes="den Längere Deustsch YouTube v"
E Form_fix_meinen_tag_nachrichten_1_ein_l_ngere FROM_SESSION Session_meinen_tag_nachrichten
V Form_fix_meinen_tag_nachrichten_2_w_hrend_ich kind=form lang=de surface="während ich putze" fixes="während meine Putzen"
E Form_fix_meinen_tag_nachrichten_2_w_hrend_ich FROM_SESSION Session_meinen_tag_nachrichten
V Form_fix_meinen_tag_nachrichten_3_in_verschie kind=form lang=de surface="in verschiedenen Sprachen" fixes="auf verschieden Sprachen"
E Form_fix_meinen_tag_nachrichten_3_in_verschie FROM_SESSION Session_meinen_tag_nachrichten

# ingest-session 2026-09-27T09:10:19Z kanonischen-erholungszeitraum lang=de
V Session_kanonischen_erholungszeitraum kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-kanonischen-erholungszeitraum.toon.md
V Focus_kanonischen_erholungszeitraum kind=focus lang=de gloss="den kanonischen Erholungszeitraum (schwache Adjekt" status=active
E Focus_kanonischen_erholungszeitraum FROM_SESSION Session_kanonischen_erholungszeitraum
V Lemma_de_fix_kanonischen_erholungszeitraum kind=lemma lang=de surface="So geben Sie mir den kanonischen Erholungszeitraum" role=minimal-rewrite
E Lemma_de_fix_kanonischen_erholungszeitraum FROM_SESSION Session_kanonischen_erholungszeitraum SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-kanonischen-erholungszeitraum.toon.md
V Form_fix_kanonischen_erholungszeitraum_0_den_ kind=form lang=de surface="den kanonischen" fixes="den kanonische"
E Form_fix_kanonischen_erholungszeitraum_0_den_ FROM_SESSION Session_kanonischen_erholungszeitraum
V Form_fix_kanonischen_erholungszeitraum_1_f_r_ kind=form lang=de surface="für verschiedene Leiden" fixes="für verschiedenen Leiden"
E Form_fix_kanonischen_erholungszeitraum_1_f_r_ FROM_SESSION Session_kanonischen_erholungszeitraum
V Form_fix_kanonischen_erholungszeitraum_2_phys kind=form lang=de surface=Physiotherapeuten fixes="Physicalische Theapeuristen"
E Form_fix_kanonischen_erholungszeitraum_2_phys FROM_SESSION Session_kanonischen_erholungszeitraum

# ingest-session 2026-09-27T09:12:52Z tag-angefangen-putzen lang=de
V Session_tag_angefangen_putzen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tag-angefangen-putzen.toon.md
V Focus_tag_angefangen_putzen kind=focus lang=de gloss="meinen Tag (Akk. m.)" status=active
E Focus_tag_angefangen_putzen FROM_SESSION Session_tag_angefangen_putzen
V Lemma_de_fix_tag_angefangen_putzen kind=lemma lang=de surface="Heute ist der 27.9.2026. Ich habe meinen Tag angef" role=minimal-rewrite
E Lemma_de_fix_tag_angefangen_putzen FROM_SESSION Session_tag_angefangen_putzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tag-angefangen-putzen.toon.md
V Form_fix_tag_angefangen_putzen_0_meinen_tag kind=form lang=de surface="meinen Tag" fixes="mein Tag"
E Form_fix_tag_angefangen_putzen_0_meinen_tag FROM_SESSION Session_tag_angefangen_putzen
V Form_fix_tag_angefangen_putzen_1_putze_ich kind=form lang=de surface="putze ich" fixes="mach ich putzen"
E Form_fix_tag_angefangen_putzen_1_putze_ich FROM_SESSION Session_tag_angefangen_putzen
V Form_fix_tag_angefangen_putzen_2_demn_chst_ma kind=form lang=de surface="demnächst mache ich Wortschatzübungen" fixes="demnächst Wortschatzübungen"
E Form_fix_tag_angefangen_putzen_2_demn_chst_ma FROM_SESSION Session_tag_angefangen_putzen

# auto-gap 2026-09-27T09:15:28Z surface=脰
V Concept_gap_zh_63bcc9263b kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_63bcc9263b kind=gap lang=zh surface=脰 target=de status=open
V Lemma_zh_zh_63bcc9263b kind=lemma lang=zh surface=脰
E Concept_gap_zh_63bcc9263b EXPRESSES Lemma_zh_zh_63bcc9263b SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_63bcc9263b GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_63bcc9263b GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-27T09:23:36Z boss-antworten-verfolgen lang=de
V Session_boss_antworten_verfolgen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-boss-antworten-verfolgen.toon.md
V Focus_boss_antworten_verfolgen kind=focus lang=de gloss="einen Bericht (Akkusativ maskulin)" status=active
E Focus_boss_antworten_verfolgen FROM_SESSION Session_boss_antworten_verfolgen
V Lemma_de_fix_boss_antworten_verfolgen kind=lemma lang=de surface="Heute ist der 27.9.2026. Ich brauche Sie, um auf d" role=minimal-rewrite
E Lemma_de_fix_boss_antworten_verfolgen FROM_SESSION Session_boss_antworten_verfolgen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-boss-antworten-verfolgen.toon.md
V Form_fix_boss_antworten_verfolgen_0_die_websi kind=form lang=de surface="die Website" fixes="den Webseite"
E Form_fix_boss_antworten_verfolgen_0_die_websi FROM_SESSION Session_boss_antworten_verfolgen
V Form_fix_boss_antworten_verfolgen_1_einen_ber kind=form lang=de surface="einen Bericht" fixes="ein Bericht"
E Form_fix_boss_antworten_verfolgen_1_einen_ber FROM_SESSION Session_boss_antworten_verfolgen
V Form_fix_boss_antworten_verfolgen_2_empfohlen kind=form lang=de surface=empfohlenen fixes=empfolene
E Form_fix_boss_antworten_verfolgen_2_empfohlen FROM_SESSION Session_boss_antworten_verfolgen

# ingest-session 2026-09-27T09:23:36Z eingeloggt-vorgaenge lang=de
V Session_eingeloggt_vorgaenge kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-eingeloggt-vorgaenge.toon.md
V Focus_eingeloggt_vorgaenge kind=focus lang=de gloss="einen Bericht (Akkusativ maskulin)" status=active
E Focus_eingeloggt_vorgaenge FROM_SESSION Session_eingeloggt_vorgaenge
V Lemma_de_fix_eingeloggt_vorgaenge kind=lemma lang=de surface="Ach so, ich bin eingeloggt. Verfolgen Sie also die" role=minimal-rewrite
E Lemma_de_fix_eingeloggt_vorgaenge FROM_SESSION Session_eingeloggt_vorgaenge SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-eingeloggt-vorgaenge.toon.md
V Form_fix_eingeloggt_vorgaenge_0_ich_bin_einge kind=form lang=de surface="ich bin eingeloggt" fixes="ich habe eingeloggen"
E Form_fix_eingeloggt_vorgaenge_0_ich_bin_einge FROM_SESSION Session_eingeloggt_vorgaenge
V Form_fix_eingeloggt_vorgaenge_1_die_vorg_nge_ kind=form lang=de surface="die Vorgänge" fixes="den Vorgänge"
E Form_fix_eingeloggt_vorgaenge_1_die_vorg_nge_ FROM_SESSION Session_eingeloggt_vorgaenge
V Form_fix_eingeloggt_vorgaenge_2_einen_bericht kind=form lang=de surface="einen Bericht" fixes="ein Bericht"
E Form_fix_eingeloggt_vorgaenge_2_einen_bericht FROM_SESSION Session_eingeloggt_vorgaenge

# ingest-session 2026-09-27T09:35:15Z fuer-jede-stelle-lebenslauf lang=de
V Session_fuer_jede_stelle_lebenslauf kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-fuer-jede-stelle-lebenslauf.toon.md
V Focus_fuer_jede_stelle_lebenslauf kind=focus lang=de gloss="für jede Stelle (für + Akkusativ)" status=active
E Focus_fuer_jede_stelle_lebenslauf FROM_SESSION Session_fuer_jede_stelle_lebenslauf
V Lemma_de_fix_fuer_jede_stelle_lebenslauf kind=lemma lang=de surface="Genau, ich möchte sichergehen, dass es für jede St" role=minimal-rewrite
E Lemma_de_fix_fuer_jede_stelle_lebenslauf FROM_SESSION Session_fuer_jede_stelle_lebenslauf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-fuer-jede-stelle-lebenslauf.toon.md
V Form_fix_fuer_jede_stelle_lebenslauf_0_f_r_je kind=form lang=de surface="für jede Stelle" fixes="für jeder Stelle"
E Form_fix_fuer_jede_stelle_lebenslauf_0_f_r_je FROM_SESSION Session_fuer_jede_stelle_lebenslauf
V Form_fix_fuer_jede_stelle_lebenslauf_1_meinen kind=form lang=de surface="meinen Lebenslauf" fixes="meine Resume"
E Form_fix_fuer_jede_stelle_lebenslauf_1_meinen FROM_SESSION Session_fuer_jede_stelle_lebenslauf

# ingest-session 2026-09-27T10:09:59Z apfelessig-auswirkungstabelle lang=de
V Session_apfelessig_auswirkungstabelle kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-apfelessig-auswirkungstabelle.toon.md
V Focus_apfelessig_auswirkungstabelle kind=focus lang=de gloss="damit ich es einmal angucke (damit-Satz, Verb am E" status=active
E Focus_apfelessig_auswirkungstabelle FROM_SESSION Session_apfelessig_auswirkungstabelle
V Lemma_de_fix_apfelessig_auswirkungstabelle kind=lemma lang=de surface="Außerdem nehme ich Apfelessig-Kapseln. Drucken Sie" role=minimal-rewrite
E Lemma_de_fix_apfelessig_auswirkungstabelle FROM_SESSION Session_apfelessig_auswirkungstabelle SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-apfelessig-auswirkungstabelle.toon.md
V Form_fix_apfelessig_auswirkungstabelle_0_dami kind=form lang=de surface="damit ich es einmal angucke" fixes="damit gucke es ich einmal"
E Form_fix_apfelessig_auswirkungstabelle_0_dami FROM_SESSION Session_apfelessig_auswirkungstabelle
V Form_fix_apfelessig_auswirkungstabelle_1_apfe kind=form lang=de surface=Apfelessig-Kapseln fixes="Apfel Ciber Essig Kapesel"
E Form_fix_apfelessig_auswirkungstabelle_1_apfe FROM_SESSION Session_apfelessig_auswirkungstabelle
V Form_fix_apfelessig_auswirkungstabelle_2_ausw kind=form lang=de surface="Auswirkungstabelle / Folgen des Nehmens" fixes="Auswirkungentabletten / Folgen"
E Form_fix_apfelessig_auswirkungstabelle_2_ausw FROM_SESSION Session_apfelessig_auswirkungstabelle

# ingest-session 2026-09-27T10:15:58Z tiefgreifende-analyse lang=de
V Session_tiefgreifende_analyse kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tiefgreifende-analyse.toon.md
V Focus_tiefgreifende_analyse kind=focus lang=de gloss="eine tiefgreifende Analyse (Akk. f.)" status=active
E Focus_tiefgreifende_analyse FROM_SESSION Session_tiefgreifende_analyse
V Lemma_de_fix_tiefgreifende_analyse kind=lemma lang=de surface="Bei der PDF-Datei benötige ich eine tiefgreifende " role=minimal-rewrite
E Lemma_de_fix_tiefgreifende_analyse FROM_SESSION Session_tiefgreifende_analyse SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tiefgreifende-analyse.toon.md
V Form_fix_tiefgreifende_analyse_0_ben_tige_ich kind=form lang=de surface="benötige ich" fixes="benötig t ich"
E Form_fix_tiefgreifende_analyse_0_ben_tige_ich FROM_SESSION Session_tiefgreifende_analyse
V Form_fix_tiefgreifende_analyse_1_tiefgreifend kind=form lang=de surface=tiefgreifende fixes=tiefgrefende
E Form_fix_tiefgreifende_analyse_1_tiefgreifend FROM_SESSION Session_tiefgreifende_analyse
V Form_fix_tiefgreifende_analyse_2_der_auswirku kind=form lang=de surface="der Auswirkungen" fixes="zur Auswirkungen"
E Form_fix_tiefgreifende_analyse_2_der_auswirku FROM_SESSION Session_tiefgreifende_analyse

# ingest-session 2026-09-27T10:22:56Z meinen-verlauf lang=de
V Session_meinen_verlauf kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-meinen-verlauf.toon.md
V Focus_meinen_verlauf kind=focus lang=de gloss="meinen Verlauf (Akk. m.)" status=active
E Focus_meinen_verlauf FROM_SESSION Session_meinen_verlauf
V Lemma_de_fix_meinen_verlauf kind=lemma lang=de surface="Also gut, drucken Sie jetzt meinen Verlauf meiner " role=minimal-rewrite
E Lemma_de_fix_meinen_verlauf FROM_SESSION Session_meinen_verlauf SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-meinen-verlauf.toon.md
V Form_fix_meinen_verlauf_0_drucken_sie kind=form lang=de surface="drucken Sie" fixes="drücken Sie"
E Form_fix_meinen_verlauf_0_drucken_sie FROM_SESSION Session_meinen_verlauf
V Form_fix_meinen_verlauf_1_meinen_verlauf kind=form lang=de surface="meinen Verlauf" fixes="meine Verlauf"
E Form_fix_meinen_verlauf_1_meinen_verlauf FROM_SESSION Session_meinen_verlauf
V Form_fix_meinen_verlauf_2_meiner_bisherigen_l kind=form lang=de surface="meiner bisherigen Leiden" fixes="von meine bisherige Leiden"
E Form_fix_meinen_verlauf_2_meiner_bisherigen_l FROM_SESSION Session_meinen_verlauf

# ingest-session 2026-09-27T10:27:04Z vorhandenen-lebenslauf-ersetzen lang=de
V Session_vorhandenen_lebenslauf_ersetzen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-vorhandenen-lebenslauf-ersetzen.toon.md
V Focus_vorhandenen_lebenslauf_ersetzen kind=focus lang=de gloss="den vorhandenen Lebenslauf (Akkusativ)" status=active
E Focus_vorhandenen_lebenslauf_ersetzen FROM_SESSION Session_vorhandenen_lebenslauf_ersetzen
V Lemma_de_fix_vorhandenen_lebenslauf_ersetzen kind=lemma lang=de surface="Nein, den vorhandenen Lebenslauf kannst du einfach" role=minimal-rewrite
E Lemma_de_fix_vorhandenen_lebenslauf_ersetzen FROM_SESSION Session_vorhandenen_lebenslauf_ersetzen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-vorhandenen-lebenslauf-ersetzen.toon.md
V Form_fix_vorhandenen_lebenslauf_ersetzen_0_de kind=form lang=de surface="den vorhandenen Lebenslauf" fixes="vorhandene Resume"
E Form_fix_vorhandenen_lebenslauf_ersetzen_0_de FROM_SESSION Session_vorhandenen_lebenslauf_ersetzen
V Form_fix_vorhandenen_lebenslauf_ersetzen_1_ve kind=form lang=de surface="Versuch nicht angestrengt" fixes="versuchst du strengend"
E Form_fix_vorhandenen_lebenslauf_ersetzen_1_ve FROM_SESSION Session_vorhandenen_lebenslauf_ersetzen

# auto-gap 2026-09-27T10:35:11Z surface=宄
V Concept_gap_zh_a36fd043cc kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_a36fd043cc kind=gap lang=zh surface=宄 target=de status=open
V Lemma_zh_zh_a36fd043cc kind=lemma lang=zh surface=宄
E Concept_gap_zh_a36fd043cc EXPRESSES Lemma_zh_zh_a36fd043cc SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_a36fd043cc GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_a36fd043cc GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:35:11Z surface=湁灞辨梾灞
V Concept_gap_zh_383f4ae2ab kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_383f4ae2ab kind=gap lang=zh surface=湁灞辨梾灞 target=de status=open
V Lemma_zh_zh_383f4ae2ab kind=lemma lang=zh surface=湁灞辨梾灞
E Concept_gap_zh_383f4ae2ab EXPRESSES Lemma_zh_zh_383f4ae2ab SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_383f4ae2ab GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_383f4ae2ab GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-27T10:38:17Z nicht-nur-sondern-auch-blogs lang=de
V Session_nicht_nur_sondern_auch_blogs kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-nicht-nur-sondern-auch-blogs.toon.md
V Focus_nicht_nur_sondern_auch_blogs kind=focus lang=de gloss="nicht nur …, sondern auch" status=active
E Focus_nicht_nur_sondern_auch_blogs FROM_SESSION Session_nicht_nur_sondern_auch_blogs
V Lemma_de_fix_nicht_nur_sondern_auch_blogs kind=lemma lang=de surface="Also gut, aber ich hätte gerne, was in der Welt pa" role=minimal-rewrite
E Lemma_de_fix_nicht_nur_sondern_auch_blogs FROM_SESSION Session_nicht_nur_sondern_auch_blogs SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-nicht-nur-sondern-auch-blogs.toon.md
V Form_fix_nicht_nur_sondern_auch_blogs_0_in_de kind=form lang=de surface="in der Welt" fixes="an der Welt"
E Form_fix_nicht_nur_sondern_auch_blogs_0_in_de FROM_SESSION Session_nicht_nur_sondern_auch_blogs
V Form_fix_nicht_nur_sondern_auch_blogs_1_das_m kind=form lang=de surface="das mir potenziell hilft" fixes="die potenzielle hilfsreich mir"
E Form_fix_nicht_nur_sondern_auch_blogs_1_das_m FROM_SESSION Session_nicht_nur_sondern_auch_blogs
V Form_fix_nicht_nur_sondern_auch_blogs_2_nicht kind=form lang=de surface="nicht nur …, sondern auch" fixes="nicht nur … aber auch"
E Form_fix_nicht_nur_sondern_auch_blogs_2_nicht FROM_SESSION Session_nicht_nur_sondern_auch_blogs
V Form_fix_nicht_nur_sondern_auch_blogs_3_regio kind=form lang=de surface="regionale Blogs, Foren" fixes="regionale Blog, Forum"
E Form_fix_nicht_nur_sondern_auch_blogs_3_regio FROM_SESSION Session_nicht_nur_sondern_auch_blogs

# ingest-session 2026-09-27T10:47:52Z nach-china-reisen lang=de
V Session_nach_china_reisen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-nach-china-reisen.toon.md
V Focus_nach_china_reisen kind=focus lang=de gloss="nach China (Richtung)" status=active
E Focus_nach_china_reisen FROM_SESSION Session_nach_china_reisen
V Lemma_de_fix_nach_china_reisen kind=lemma lang=de surface="Damit kannst du auch meine Profilseite anpassen un" role=minimal-rewrite
E Lemma_de_fix_nach_china_reisen FROM_SESSION Session_nach_china_reisen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-nach-china-reisen.toon.md
V Form_fix_nach_china_reisen_0_nach_china_zu_re kind=form lang=de surface="nach China zu reisen" fixes="in China zu reisen"
E Form_fix_nach_china_reisen_0_nach_china_zu_re FROM_SESSION Session_nach_china_reisen
V Form_fix_nach_china_reisen_1_steuern kind=form lang=de surface=steuern fixes=steueren
E Form_fix_nach_china_reisen_1_steuern FROM_SESSION Session_nach_china_reisen

# auto-gap 2026-09-27T10:48:03Z surface=浜
V Concept_gap_zh_763dfcc4cd kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_763dfcc4cd kind=gap lang=zh surface=浜 target=de status=open
V Lemma_zh_zh_763dfcc4cd kind=lemma lang=zh surface=浜
E Concept_gap_zh_763dfcc4cd EXPRESSES Lemma_zh_zh_763dfcc4cd SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_763dfcc4cd GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_763dfcc4cd GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=崲寰
V Concept_gap_zh_cdda6f7738 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_cdda6f7738 kind=gap lang=zh surface=崲寰 target=de status=open
V Lemma_zh_zh_cdda6f7738 kind=lemma lang=zh surface=崲寰
E Concept_gap_zh_cdda6f7738 EXPRESSES Lemma_zh_zh_cdda6f7738 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_cdda6f7738 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_cdda6f7738 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=俊
V Concept_gap_zh_d2e9b4baab kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_d2e9b4baab kind=gap lang=zh surface=俊 target=de status=open
V Lemma_zh_zh_d2e9b4baab kind=lemma lang=zh surface=俊
E Concept_gap_zh_d2e9b4baab EXPRESSES Lemma_zh_zh_d2e9b4baab SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_d2e9b4baab GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_d2e9b4baab GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=鎺
V Concept_gap_zh_b378520220 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_b378520220 kind=gap lang=zh surface=鎺 target=de status=open
V Lemma_zh_zh_b378520220 kind=lemma lang=zh surface=鎺
E Concept_gap_zh_b378520220 EXPRESSES Lemma_zh_zh_b378520220 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_b378520220 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_b378520220 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=彈
V Concept_gap_zh_2b5b962c9e kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_2b5b962c9e kind=gap lang=zh surface=彈 target=de status=open
V Lemma_zh_zh_2b5b962c9e kind=lemma lang=zh surface=彈
E Concept_gap_zh_2b5b962c9e EXPRESSES Lemma_zh_zh_2b5b962c9e SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_2b5b962c9e GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_2b5b962c9e GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=摜浣犺兘涓嶈兘鍔
V Concept_gap_zh_2ddd3b3e99 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_2ddd3b3e99 kind=gap lang=zh surface=摜浣犺兘涓嶈兘鍔 target=de status=open
V Lemma_zh_zh_2ddd3b3e99 kind=lemma lang=zh surface=摜浣犺兘涓嶈兘鍔
E Concept_gap_zh_2ddd3b3e99 EXPRESSES Lemma_zh_zh_2ddd3b3e99 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_2ddd3b3e99 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_2ddd3b3e99 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=偣鑴戝瓙
V Concept_gap_zh_73df6663b3 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_73df6663b3 kind=gap lang=zh surface=偣鑴戝瓙 target=de status=open
V Lemma_zh_zh_73df6663b3 kind=lemma lang=zh surface=偣鑴戝瓙
E Concept_gap_zh_73df6663b3 EXPRESSES Lemma_zh_zh_73df6663b3 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_73df6663b3 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_73df6663b3 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=鐏垫椿涓
V Concept_gap_zh_f842493393 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_f842493393 kind=gap lang=zh surface=鐏垫椿涓 target=de status=open
V Lemma_zh_zh_f842493393 kind=lemma lang=zh surface=鐏垫椿涓
E Concept_gap_zh_f842493393 EXPRESSES Lemma_zh_zh_f842493393 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_f842493393 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_f842493393 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T10:48:03Z surface=鐐瑰彲涓嶅彲浠
V Concept_gap_zh_a7d00e2227 kind=concept gloss=unknown-expression-in-de status=open
V Gap_zh_a7d00e2227 kind=gap lang=zh surface=鐐瑰彲涓嶅彲浠 target=de status=open
V Lemma_zh_zh_a7d00e2227 kind=lemma lang=zh surface=鐐瑰彲涓嶅彲浠
E Concept_gap_zh_a7d00e2227 EXPRESSES Lemma_zh_zh_a7d00e2227 SOURCE=hook/beforeSubmitPrompt
E Lemma_zh_zh_a7d00e2227 GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_zh_a7d00e2227 GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-27T10:51:58Z wechat-austausch-annehmen lang=de
V Session_wechat_austausch_annehmen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-wechat-austausch-annehmen.toon.md
V Focus_wechat_austausch_annehmen kind=focus lang=de gloss="es gibt + Akkusativ (einen WeChat-Austausch)" status=active
E Focus_wechat_austausch_annehmen FROM_SESSION Session_wechat_austausch_annehmen
V Lemma_de_fix_wechat_austausch_annehmen kind=lemma lang=de surface="Wenn es einen WeChat-Austausch gibt, klicken Sie b" role=minimal-rewrite
E Lemma_de_fix_wechat_austausch_annehmen FROM_SESSION Session_wechat_austausch_annehmen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-wechat-austausch-annehmen.toon.md
V Form_fix_wechat_austausch_annehmen_0_es_einen kind=form lang=de surface="es einen WeChat-Austausch gibt" fixes="es 交换微信 gibt"
E Form_fix_wechat_austausch_annehmen_0_es_einen FROM_SESSION Session_wechat_austausch_annehmen
V Form_fix_wechat_austausch_annehmen_1_einfach_ kind=form lang=de surface="einfach auf Annehmen" fixes="einfachen 接受"
E Form_fix_wechat_austausch_annehmen_1_einfach_ FROM_SESSION Session_wechat_austausch_annehmen

# ingest-session 2026-09-27T11:44:36Z ueberblick-sprachenlernen lang=de
V Session_ueberblick_sprachenlernen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-ueberblick-sprachenlernen.toon.md
V Focus_ueberblick_sprachenlernen kind=focus lang=de gloss="einen Überblick (Akkusativ, maskulin)" status=active
E Focus_ueberblick_sprachenlernen FROM_SESSION Session_ueberblick_sprachenlernen
V Lemma_de_fix_ueberblick_sprachenlernen kind=lemma lang=de surface="Also gut, ich bin draußen. Gib mir einen Überblick" role=minimal-rewrite
E Lemma_de_fix_ueberblick_sprachenlernen FROM_SESSION Session_ueberblick_sprachenlernen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-ueberblick-sprachenlernen.toon.md
V Form_fix_ueberblick_sprachenlernen_0_einen_be kind=form lang=de surface="einen Überblick" fixes="die Überblick"
E Form_fix_ueberblick_sprachenlernen_0_einen_be FROM_SESSION Session_ueberblick_sprachenlernen
V Form_fix_ueberblick_sprachenlernen_1_ber_mein kind=form lang=de surface="über mein bisheriges Sprachenlernen" fixes="meiner vorhandene Sprache lern"
E Form_fix_ueberblick_sprachenlernen_1_ber_mein FROM_SESSION Session_ueberblick_sprachenlernen

# ingest-session 2026-09-27T11:49:59Z visualisierung-sprachlernstand lang=de
V Session_visualisierung_sprachlernstand kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-visualisierung-sprachlernstand.toon.md
V Focus_visualisierung_sprachlernstand kind=focus lang=de gloss="meines Sprachlernstands (Genitiv, maskulin)" status=active
E Focus_visualisierung_sprachlernstand FROM_SESSION Session_visualisierung_sprachlernstand
V Lemma_de_fix_visualisierung_sprachlernstand kind=lemma lang=de surface="Kannst du mir im Augenblick eine Visualisierung me" role=minimal-rewrite
E Lemma_de_fix_visualisierung_sprachlernstand FROM_SESSION Session_visualisierung_sprachlernstand SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-visualisierung-sprachlernstand.toon.md
V Form_fix_visualisierung_sprachlernstand_0_mei kind=form lang=de surface="meines Sprachlernstands" fixes="von meiner Sprachelernsstand"
E Form_fix_visualisierung_sprachlernstand_0_mei FROM_SESSION Session_visualisierung_sprachlernstand
V Form_fix_visualisierung_sprachlernstand_1_ein kind=form lang=de surface="eine Visualisierung … zeigen" fixes="eine Visualisierung … mitzutei"
E Form_fix_visualisierung_sprachlernstand_1_ein FROM_SESSION Session_visualisierung_sprachlernstand

# ingest-session 2026-09-27T11:53:25Z oeffentlicher-link-sprachvisualisierung lang=de
V Session_oeffentlicher_link_sprachvisualisierung kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-oeffentlicher-link-sprachvisualisierung.toon.md
V Focus_oeffentlicher_link_sprachvisualisierung kind=focus lang=de gloss="den zusätzlichen Link (Akkusativ, maskulin)" status=active
E Focus_oeffentlicher_link_sprachvisualisierung FROM_SESSION Session_oeffentlicher_link_sprachvisualisierung
V Lemma_de_fix_oeffentlicher_link_sprachvisualisierung kind=lemma lang=de surface="Genau, den zusätzlichen Link brauche ich. Mach das" role=minimal-rewrite
E Lemma_de_fix_oeffentlicher_link_sprachvisualisierung FROM_SESSION Session_oeffentlicher_link_sprachvisualisierung SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-oeffentlicher-link-sprachvisualisierung.toon.md
V Form_fix_oeffentlicher_link_sprachvisualisier kind=form lang=de surface="den zusätzlichen Link" fixes="im Bezug der zusätzliche Link"
E Form_fix_oeffentlicher_link_sprachvisualisier FROM_SESSION Session_oeffentlicher_link_sprachvisualisierung
V Form_fix_oeffentlicher_link_sprachvisualisier kind=form lang=de surface="brauche ich" fixes="sehe ich es benötigt"
E Form_fix_oeffentlicher_link_sprachvisualisier FROM_SESSION Session_oeffentlicher_link_sprachvisualisierung

# ingest-session 2026-09-27T12:07:14Z tief-in-sprachlernstand-eintauchen lang=de
V Session_tief_in_sprachlernstand_eintauchen kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tief-in-sprachlernstand-eintauchen.toon.md
V Focus_tief_in_sprachlernstand_eintauchen kind=focus lang=de gloss="in meinen aktuellen Sprachlernstand eintauchen (in" status=active
E Focus_tief_in_sprachlernstand_eintauchen FROM_SESSION Session_tief_in_sprachlernstand_eintauchen
V Lemma_de_fix_tief_in_sprachlernstand_eintauchen kind=lemma lang=de surface="Nein, ich brauche eine solche Visualisierung, mit " role=minimal-rewrite
E Lemma_de_fix_tief_in_sprachlernstand_eintauchen FROM_SESSION Session_tief_in_sprachlernstand_eintauchen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-tief-in-sprachlernstand-eintauchen.toon.md
V Form_fix_tief_in_sprachlernstand_eintauchen_0 kind=form lang=de surface="eine solche Visualisierung" fixes="solche Visualisierung"
E Form_fix_tief_in_sprachlernstand_eintauchen_0 FROM_SESSION Session_tief_in_sprachlernstand_eintauchen
V Form_fix_tief_in_sprachlernstand_eintauchen_1 kind=form lang=de surface="mit der" fixes="von denen"
E Form_fix_tief_in_sprachlernstand_eintauchen_1 FROM_SESSION Session_tief_in_sprachlernstand_eintauchen
V Form_fix_tief_in_sprachlernstand_eintauchen_2 kind=form lang=de surface="in meinen aktuellen Sprachlernstand" fixes="zum meinen vorhandenen Sprache"
E Form_fix_tief_in_sprachlernstand_eintauchen_2 FROM_SESSION Session_tief_in_sprachlernstand_eintauchen

# ingest-session 2026-09-27T12:20:10Z spanisch-uebungen-zuerst lang=de
V Session_spanisch_uebungen_zuerst kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-spanisch-uebungen-zuerst.toon.md
V Focus_spanisch_uebungen_zuerst kind=focus lang=de gloss="Nimm das in .private auf (in + Akkusativ)" status=active
E Focus_spanisch_uebungen_zuerst FROM_SESSION Session_spanisch_uebungen_zuerst
V Lemma_de_fix_spanisch_uebungen_zuerst kind=lemma lang=de surface="Genau, ich bin mit dem Überblick zufrieden. Gib mi" role=minimal-rewrite
E Lemma_de_fix_spanisch_uebungen_zuerst FROM_SESSION Session_spanisch_uebungen_zuerst SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-spanisch-uebungen-zuerst.toon.md
V Form_fix_spanisch_uebungen_zuerst_0_mit_dem_b kind=form lang=de surface="mit dem Überblick zufrieden" fixes="vor der Überblick zufriedenste"
E Form_fix_spanisch_uebungen_zuerst_0_mit_dem_b FROM_SESSION Session_spanisch_uebungen_zuerst
V Form_fix_spanisch_uebungen_zuerst_1_gib_mir_a kind=form lang=de surface="Gib mir also" fixes="So gib"
E Form_fix_spanisch_uebungen_zuerst_1_gib_mir_a FROM_SESSION Session_spanisch_uebungen_zuerst
V Form_fix_spanisch_uebungen_zuerst_2_auf_spani kind=form lang=de surface="auf Spanisch" fixes="mit Spanisch"
E Form_fix_spanisch_uebungen_zuerst_2_auf_spani FROM_SESSION Session_spanisch_uebungen_zuerst

# auto-gap 2026-09-27T12:43:57Z surface=la
V Concept_gap_es_la kind=concept gloss=unknown-expression-in-de status=open
V Gap_es_la kind=gap lang=es surface=la target=de status=open
V Lemma_es_es_la kind=lemma lang=es surface=la
E Concept_gap_es_la EXPRESSES Lemma_es_es_la SOURCE=hook/beforeSubmitPrompt
E Lemma_es_es_la GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_es_la GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T12:43:57Z surface=que
V Concept_gap_es_que kind=concept gloss=unknown-expression-in-de status=open
V Gap_es_que kind=gap lang=es surface=que target=de status=open
V Lemma_es_es_que kind=lemma lang=es surface=que
E Concept_gap_es_que EXPRESSES Lemma_es_es_que SOURCE=hook/beforeSubmitPrompt
E Lemma_es_es_que GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_es_que GAP_IN de SOURCE=hook/beforeSubmitPrompt

# auto-gap 2026-09-27T12:43:57Z surface=por
V Concept_gap_es_por kind=concept gloss=unknown-expression-in-de status=open
V Gap_es_por kind=gap lang=es surface=por target=de status=open
V Lemma_es_es_por kind=lemma lang=es surface=por
E Concept_gap_es_por EXPRESSES Lemma_es_es_por SOURCE=hook/beforeSubmitPrompt
E Lemma_es_es_por GAP_IN de SOURCE=hook/beforeSubmitPrompt
E Concept_gap_es_por GAP_IN de SOURCE=hook/beforeSubmitPrompt

# ingest-session 2026-09-27T12:44:33Z cvc-primer-parrafo-demasiado lang=es
V Session_cvc_primer_parrafo_demasiado kind=session date=2026-09-27 lang=es body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-cvc-primer-parrafo-demasiado.toon.md
V Focus_cvc_primer_parrafo_demasiado kind=focus lang=es gloss="He leído (pretérito perfecto: haber + participio)" status=active
E Focus_cvc_primer_parrafo_demasiado FROM_SESSION Session_cvc_primer_parrafo_demasiado
V Lemma_es_fix_cvc_primer_parrafo_demasiado kind=lemma lang=es surface="He leído el primer párrafo de CVC y he descubierto" role=minimal-rewrite
E Lemma_es_fix_cvc_primer_parrafo_demasiado FROM_SESSION Session_cvc_primer_parrafo_demasiado SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-cvc-primer-parrafo-demasiado.toon.md
V Form_fix_cvc_primer_parrafo_demasiado_0_he_le kind=form lang=es surface="He leído" fixes="He ledo"
E Form_fix_cvc_primer_parrafo_demasiado_0_he_le FROM_SESSION Session_cvc_primer_parrafo_demasiado
V Form_fix_cvc_primer_parrafo_demasiado_1_el_pr kind=form lang=es surface="el primer párrafo" fixes="la primero paragraph"
E Form_fix_cvc_primer_parrafo_demasiado_1_el_pr FROM_SESSION Session_cvc_primer_parrafo_demasiado
V Form_fix_cvc_primer_parrafo_demasiado_2_he_de kind=form lang=es surface="he descubierto que es demasiado para mí" fixes="he discovered lo que es trop m"
E Form_fix_cvc_primer_parrafo_demasiado_2_he_de FROM_SESSION Session_cvc_primer_parrafo_demasiado
V Form_fix_cvc_primer_parrafo_demasiado_3_por_a kind=form lang=es surface="Por ahora, es suficiente" fixes="Actualmente es ist genug"
E Form_fix_cvc_primer_parrafo_demasiado_3_por_a FROM_SESSION Session_cvc_primer_parrafo_demasiado

# Russian opinion practice 2026-09-27
V Concept_express_opinion kind=concept gloss=express-opinion
V Frame_ru_ja_schitaju_chto kind=frame lang=ru id=ja_schitaju_chto pattern="Я считаю, что + finite clause"
V Lemma_ru_schitat kind=lemma lang=ru surface="считать"
V Form_ru_ja_schitaju kind=form lang=ru surface="Я считаю"
E Concept_express_opinion NEEDS_FRAME Frame_ru_ja_schitaju_chto
E Concept_express_opinion EXPRESSES Lemma_ru_schitat
E Lemma_ru_schitat HAS_FORM Form_ru_ja_schitaju
E Form_ru_ja_schitaju FILLS Frame_ru_ja_schitaju_chto

V Concept_express_impression kind=concept gloss=express-impression
V Frame_ru_mne_kazhetsja_chto kind=frame lang=ru id=mne_kazhetsja_chto pattern="Мне кажется, что + finite clause"
V Lemma_ru_kazatsja kind=lemma lang=ru surface="казаться"
V Form_ru_mne_kazhetsja kind=form lang=ru surface="Мне кажется"
E Concept_express_impression NEEDS_FRAME Frame_ru_mne_kazhetsja_chto
E Concept_express_impression EXPRESSES Lemma_ru_kazatsja
E Lemma_ru_kazatsja HAS_FORM Form_ru_mne_kazhetsja
E Form_ru_mne_kazhetsja FILLS Frame_ru_mne_kazhetsja_chto

V Concept_express_different_opinion kind=concept gloss=express-different-opinion
V Frame_ru_u_menja_N_nom kind=frame lang=ru id=u_menja_N_nom pattern="У меня + N (Nom)"
V Lemma_ru_mnenie kind=lemma lang=ru surface="мнение"
V Form_ru_u_menja_drugoe_mnenie kind=form lang=ru surface="У меня другое мнение"
E Concept_express_different_opinion NEEDS_FRAME Frame_ru_u_menja_N_nom
E Concept_express_different_opinion EXPRESSES Lemma_ru_mnenie
E Lemma_ru_mnenie HAS_FORM Form_ru_u_menja_drugoe_mnenie
E Form_ru_u_menja_drugoe_mnenie FILLS Frame_ru_u_menja_N_nom

V Concept_state_current_comprehension kind=concept gloss=state-current-comprehension
V Frame_ru_ja_poka_ne_ochen_ADV_V kind=frame lang=ru id=ja_poka_ne_ochen_ADV_V pattern="Я пока не очень хорошо + V"
V Lemma_ru_ponimat kind=lemma lang=ru surface="понимать"
V Form_ru_ja_ponimaju kind=form lang=ru surface="Я пока не очень хорошо понимаю"
E Concept_state_current_comprehension NEEDS_FRAME Frame_ru_ja_poka_ne_ochen_ADV_V
E Concept_state_current_comprehension EXPRESSES Lemma_ru_ponimat
E Lemma_ru_ponimat HAS_FORM Form_ru_ja_ponimaju
E Form_ru_ja_ponimaju FILLS Frame_ru_ja_poka_ne_ochen_ADV_V

V Concept_ask_to_repeat_politely kind=concept gloss=ask-to-repeat-politely
V Frame_ru_ne_mogli_by_vy_inf kind=frame lang=ru id=ne_mogli_by_vy_inf pattern="Не могли бы вы + Inf, пожалуйста?"
V Lemma_ru_povtorit kind=lemma lang=ru surface="повторить"
V Form_ru_ne_mogli_by_vy_povtorit kind=form lang=ru surface="Не могли бы вы повторить, пожалуйста?"
E Concept_ask_to_repeat_politely NEEDS_FRAME Frame_ru_ne_mogli_by_vy_inf
E Concept_ask_to_repeat_politely EXPRESSES Lemma_ru_povtorit
E Lemma_ru_povtorit HAS_FORM Form_ru_ne_mogli_by_vy_povtorit
E Form_ru_ne_mogli_by_vy_povtorit FILLS Frame_ru_ne_mogli_by_vy_inf

# ingest-session 2026-09-27T13:17:58Z wiktionary-deutsch-vokabelseiten lang=de
V Session_wiktionary_deutsch_vokabelseiten kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-wiktionary-deutsch-vokabelseiten.toon.md
V Focus_wiktionary_deutsch_vokabelseiten kind=focus lang=de gloss="Nimm das in .private auf (in + Akkusativ)" status=active
E Focus_wiktionary_deutsch_vokabelseiten FROM_SESSION Session_wiktionary_deutsch_vokabelseiten
V Lemma_de_fix_wiktionary_deutsch_vokabelseiten kind=lemma lang=de surface="Nein, nicht die Hauptseite, sondern die deutschen " role=minimal-rewrite
E Lemma_de_fix_wiktionary_deutsch_vokabelseiten FROM_SESSION Session_wiktionary_deutsch_vokabelseiten SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-wiktionary-deutsch-vokabelseiten.toon.md
V Form_fix_wiktionary_deutsch_vokabelseiten_0_n kind=form lang=de surface="Nein, nicht die Hauptseite" fixes="Нет nicht Hauptseite"
E Form_fix_wiktionary_deutsch_vokabelseiten_0_n FROM_SESSION Session_wiktionary_deutsch_vokabelseiten
V Form_fix_wiktionary_deutsch_vokabelseiten_1_d kind=form lang=de surface="den oben genannten russischen Wortschatz" fixes="vorgenannten russische Wortsch"
E Form_fix_wiktionary_deutsch_vokabelseiten_1_d FROM_SESSION Session_wiktionary_deutsch_vokabelseiten
V Form_fix_wiktionary_deutsch_vokabelseiten_2_d kind=form lang=de surface="die deutschen Wiktionary-Seiten" fixes="auf Deutsch"
E Form_fix_wiktionary_deutsch_vokabelseiten_2_d FROM_SESSION Session_wiktionary_deutsch_vokabelseiten

# Russian expression practice 2026-09-27
V Concept_express_limited_fluency kind=concept gloss=express-limited-fluency
V Frame_ru_ja_pytajus_inf kind=frame lang=ru id=ja_pytajus_inf pattern="Я пытаюсь + Inf"
V Lemma_ru_pytatsja kind=lemma lang=ru surface="пытаться"
V Lemma_ru_dumat kind=lemma lang=ru surface="думать"
V Form_ru_ja_pytajus_govorit kind=form lang=ru surface="Я пытаюсь говорить по-русски"
V Form_ru_ja_dumaju kind=form lang=ru surface="я думаю по-немецки"
E Concept_express_limited_fluency NEEDS_FRAME Frame_ru_ja_pytajus_inf SOURCE=de-wiktionary-ru-pytatsja
E Concept_express_limited_fluency EXPRESSES Lemma_ru_pytatsja SOURCE=de-wiktionary-ru-pytatsja
E Concept_express_limited_fluency EXPRESSES Lemma_ru_dumat SOURCE=de-wiktionary-ru-dumat
E Lemma_ru_pytatsja HAS_FORM Form_ru_ja_pytajus_govorit
E Lemma_ru_dumat HAS_FORM Form_ru_ja_dumaju
E Form_ru_ja_pytajus_govorit FILLS Frame_ru_ja_pytajus_inf

# ingest-session 2026-09-27T13:26:38Z russisch-gedanken-ausdruecken lang=de
V Session_russisch_gedanken_ausdruecken kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russisch-gedanken-ausdruecken.toon.md
V Focus_russisch_gedanken_ausdruecken kind=focus lang=de gloss="Nimm das in .private auf (in + Akkusativ)" status=active
E Focus_russisch_gedanken_ausdruecken FROM_SESSION Session_russisch_gedanken_ausdruecken
V Lemma_de_fix_russisch_gedanken_ausdruecken kind=lemma lang=de surface="Hier versuche ich, nur Russisch zu sprechen, aber " role=minimal-rewrite
E Lemma_de_fix_russisch_gedanken_ausdruecken FROM_SESSION Session_russisch_gedanken_ausdruecken SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russisch-gedanken-ausdruecken.toon.md
V Form_fix_russisch_gedanken_ausdruecken_0_nur_ kind=form lang=de surface="nur Russisch" fixes="ganz auf Russisch"
E Form_fix_russisch_gedanken_ausdruecken_0_nur_ FROM_SESSION Session_russisch_gedanken_ausdruecken
V Form_fix_russisch_gedanken_ausdruecken_1_etwa kind=form lang=de surface="etwas, das ich auf Russisch sagen kann" fixes="was zu sagen auf Russisch"
E Form_fix_russisch_gedanken_ausdruecken_1_etwa FROM_SESSION Session_russisch_gedanken_ausdruecken
V Form_fix_russisch_gedanken_ausdruecken_2_und_ kind=form lang=de surface="und nimm den Wortschatz in dieses Projek" fixes="mit Speicherung der Wortschatz"
E Form_fix_russisch_gedanken_ausdruecken_2_und_ FROM_SESSION Session_russisch_gedanken_ausdruecken

# ingest-session 2026-09-27T13:36:14Z russischer-wortschatz-deutsche-erklaerung lang=de
V Session_russischer_wortschatz_deutsche_erklaerun kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russischer-wortschatz-deutsche-erklaerung.toon.md
V Focus_russischer_wortschatz_deutsche_erklaerun kind=focus lang=de gloss="Nimm das in .private auf (in + Akkusativ)" status=active
E Focus_russischer_wortschatz_deutsche_erklaerun FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun
V Lemma_de_fix_russischer_wortschatz_deutsche_erklaerun kind=lemma lang=de surface="Mit Wiktionary meine ich russischen Wortschatz mit" role=minimal-rewrite
E Lemma_de_fix_russischer_wortschatz_deutsche_erklaerun FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russischer-wortschatz-deutsche-erklaerung.toon.md
V Form_fix_russischer_wortschatz_deutsche_erkla kind=form lang=de surface="Mit Wiktionary" fixes="С Wiktionary"
E Form_fix_russischer_wortschatz_deutsche_erkla FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun
V Form_fix_russischer_wortschatz_deutsche_erkla kind=form lang=de surface="russischen Wortschatz" fixes="Russisch Wortschatz"
E Form_fix_russischer_wortschatz_deutsche_erkla FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun
V Form_fix_russischer_wortschatz_deutsche_erkla kind=form lang=de surface="mit deutschen Erklärungen" fixes="mit Deutsch Erklärung"
E Form_fix_russischer_wortschatz_deutsche_erkla FROM_SESSION Session_russischer_wortschatz_deutsche_erklaerun

# ingest-session 2026-09-27T13:40:49Z russische-lemma-links lang=de
V Session_russische_lemma_links kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russische-lemma-links.toon.md
V Focus_russische_lemma_links kind=focus lang=de gloss="Nimm das in .private auf (in + Akkusativ)" status=active
E Focus_russische_lemma_links FROM_SESSION Session_russische_lemma_links
V Lemma_de_fix_russische_lemma_links kind=lemma lang=de surface="Nein, die Links, die du angeboten hast, führen wie" role=minimal-rewrite
E Lemma_de_fix_russische_lemma_links FROM_SESSION Session_russische_lemma_links SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-russische-lemma-links.toon.md
V Form_fix_russische_lemma_links_0_die_links kind=form lang=de surface="die Links" fixes="den Linke"
E Form_fix_russische_lemma_links_0_die_links FROM_SESSION Session_russische_lemma_links
V Form_fix_russische_lemma_links_1_die_du_angeb kind=form lang=de surface="die du angeboten hast" fixes="du geboten hast"
E Form_fix_russische_lemma_links_1_die_du_angeb FROM_SESSION Session_russische_lemma_links
V Form_fix_russische_lemma_links_2_f_hren_7bcf4 kind=form lang=de surface=führen fixes=ist
E Form_fix_russische_lemma_links_2_f_hren_7bcf4 FROM_SESSION Session_russische_lemma_links
V Form_fix_russische_lemma_links_3_zu_deutschen kind=form lang=de surface="zu deutschen Wörtern mit deutschen Erklä" fixes="Deutsch mit Deutscher Erklärun"
E Form_fix_russische_lemma_links_3_zu_deutschen FROM_SESSION Session_russische_lemma_links

# ingest-session 2026-09-27T13:42:26Z damit-zufrieden-fortschritt lang=de
V Session_damit_zufrieden_fortschritt kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-damit-zufrieden-fortschritt.toon.md
V Focus_damit_zufrieden_fortschritt kind=focus lang=de gloss="zufrieden mit (mit + Dat)" status=active
E Focus_damit_zufrieden_fortschritt FROM_SESSION Session_damit_zufrieden_fortschritt
V Lemma_de_fix_damit_zufrieden_fortschritt kind=lemma lang=de surface="Genau, bei Der mythische Bot-Monat habe ich den Ze" role=minimal-rewrite
E Lemma_de_fix_damit_zufrieden_fortschritt FROM_SESSION Session_damit_zufrieden_fortschritt SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-damit-zufrieden-fortschritt.toon.md
V Form_fix_damit_zufrieden_fortschritt_0_damit_ kind=form lang=de surface="damit zufrieden" fixes="darauf zufriedenstellend"
E Form_fix_damit_zufrieden_fortschritt_0_damit_ FROM_SESSION Session_damit_zufrieden_fortschritt
V Form_fix_damit_zufrieden_fortschritt_1_zu_vie kind=form lang=de surface="zu viel gelernt" fixes="zu genug gelernt"
E Form_fix_damit_zufrieden_fortschritt_1_zu_vie FROM_SESSION Session_damit_zufrieden_fortschritt
V Form_fix_damit_zufrieden_fortschritt_2_den_fo kind=form lang=de surface="den Fortschritt dort" fixes="die Progress hinein"
E Form_fix_damit_zufrieden_fortschritt_2_den_fo FROM_SESSION Session_damit_zufrieden_fortschritt
V Form_fix_damit_zufrieden_fortschritt_3_geben_ kind=form lang=de surface="geben Sie mir das Nächste" fixes="mache ich dem nächste"
E Form_fix_damit_zufrieden_fortschritt_3_geben_ FROM_SESSION Session_damit_zufrieden_fortschritt

# ingest-session 2026-09-27T14:00:47Z auf-meine-emails lang=de
V Session_auf_meine_emails kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-auf-meine-emails.toon.md
V Focus_auf_meine_emails kind=focus lang=de gloss="auf meine E-Mails (auf + Akk)" status=active
E Focus_auf_meine_emails FROM_SESSION Session_auf_meine_emails
V Lemma_de_fix_auf_meine_emails kind=lemma lang=de surface="Also gut, jetzt schauen wir auf meine E-Mails, bez" role=minimal-rewrite
E Lemma_de_fix_auf_meine_emails FROM_SESSION Session_auf_meine_emails SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-auf-meine-emails.toon.md
V Form_fix_auf_meine_emails_0_auf_meine_e_mails kind=form lang=de surface="auf meine E-Mails" fixes="auf meiner E-Mails"
E Form_fix_auf_meine_emails_0_auf_meine_e_mails FROM_SESSION Session_auf_meine_emails
V Form_fix_auf_meine_emails_1_sie_bearbeiten kind=form lang=de surface="sie bearbeiten" fixes="darauf bearbeiten"
E Form_fix_auf_meine_emails_1_sie_bearbeiten FROM_SESSION Session_auf_meine_emails

# ingest-session 2026-09-27T14:02:05Z berlin-potsdam-ausflug lang=de
V Session_berlin_potsdam_ausflug kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-berlin-potsdam-ausflug.toon.md
V Focus_berlin_potsdam_ausflug kind=focus lang=de gloss="Nimm das in .private auf (in + Akkusativ)" status=active
E Focus_berlin_potsdam_ausflug FROM_SESSION Session_berlin_potsdam_ausflug
V Lemma_de_fix_berlin_potsdam_ausflug kind=lemma lang=de surface="Also gut, geben Sie mir jetzt bitte ein paar Empfe" role=minimal-rewrite
E Lemma_de_fix_berlin_potsdam_ausflug FROM_SESSION Session_berlin_potsdam_ausflug SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-berlin-potsdam-ausflug.toon.md
V Form_fix_berlin_potsdam_ausflug_0_f_r_sehensw kind=form lang=de surface="für Sehenswürdigkeiten" fixes="Place of Interest zu besuchen"
E Form_fix_berlin_potsdam_ausflug_0_f_r_sehensw FROM_SESSION Session_berlin_potsdam_ausflug
V Form_fix_berlin_potsdam_ausflug_1_ber_cksicht kind=form lang=de surface="Berücksichtigen Sie dabei" fixes="Decken Sie ... im Überlegen"
E Form_fix_berlin_potsdam_ausflug_1_ber_cksicht FROM_SESSION Session_berlin_potsdam_ausflug
V Form_fix_berlin_potsdam_ausflug_2_meinen_aktu kind=form lang=de surface="meinen aktuellen Zustand" fixes="meine vorhandener Zustand"
E Form_fix_berlin_potsdam_ausflug_2_meinen_aktu FROM_SESSION Session_berlin_potsdam_ausflug

# ingest-session 2026-09-27T20:45:48Z starte-die-shenyou-10m lang=de
V Session_starte_die_shenyou_10m kind=session date=2026-09-27 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-starte-die-shenyou.toon.md
V Focus_starte_die_shenyou_10m kind=focus lang=de gloss="Starte + Akk. (du-Imperativ)" status=active
E Focus_starte_die_shenyou_10m FROM_SESSION Session_starte_die_shenyou_10m
V Lemma_de_fix_starte_die_shenyou_10m kind=lemma lang=de surface="Starte die 神游." role=minimal-rewrite
E Lemma_de_fix_starte_die_shenyou_10m FROM_SESSION Session_starte_die_shenyou_10m SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-27-starte-die-shenyou.toon.md
V Form_fix_starte_die_shenyou_10m_0_starte_die_ kind=form lang=de surface="Starte die 神游." fixes=开始神游
E Form_fix_starte_die_shenyou_10m_0_starte_die_ FROM_SESSION Session_starte_die_shenyou_10m

# ingest-session 2026-09-29T10:17:30Z meinen-tag-zustand lang=de
V Session_meinen_tag_zustand kind=session date=2026-09-29 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-29-meinen-tag-zustand.toon.md
V Focus_meinen_tag_zustand kind=focus lang=de gloss="meinen Tag (Akk. m.)" status=active
E Focus_meinen_tag_zustand FROM_SESSION Session_meinen_tag_zustand
V Lemma_de_fix_meinen_tag_zustand kind=lemma lang=de surface="Ok, heute ist der 29.9.2026. Ich bin aufgestanden " role=minimal-rewrite
E Lemma_de_fix_meinen_tag_zustand FROM_SESSION Session_meinen_tag_zustand SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-29-meinen-tag-zustand.toon.md
V Form_fix_meinen_tag_zustand_0_meinen_tag kind=form lang=de surface="meinen Tag" fixes="meinem Tag"
E Form_fix_meinen_tag_zustand_0_meinen_tag FROM_SESSION Session_meinen_tag_zustand
V Form_fix_meinen_tag_zustand_1_zu_starten kind=form lang=de surface="zu starten" fixes=einzustarten
E Form_fix_meinen_tag_zustand_1_zu_starten FROM_SESSION Session_meinen_tag_zustand
V Form_fix_meinen_tag_zustand_2_den_heutigen_zu kind=form lang=de surface="den heutigen Zustand" fixes="heutezutagige Zustand"
E Form_fix_meinen_tag_zustand_2_den_heutigen_zu FROM_SESSION Session_meinen_tag_zustand
V Form_fix_meinen_tag_zustand_3_f_r_die_entsche kind=form lang=de surface="für die Entscheidungsfindung" fixes="für dem Entscheidungserfinden"
E Form_fix_meinen_tag_zustand_3_f_r_die_entsche FROM_SESSION Session_meinen_tag_zustand

# ingest-session 2026-09-29T10:22:11Z anfang-des-tages lang=de
V Session_anfang_des_tages kind=session date=2026-09-29 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-09-29-anfang-des-tages.toon.md
V Focus_anfang_des_tages kind=focus lang=de gloss="am Anfang des Tages (am + Dat)" status=active
E Focus_anfang_des_tages FROM_SESSION Session_anfang_des_tages
V Lemma_de_fix_anfang_des_tages kind=lemma lang=de surface="Ok, heute ist der 29.9.2026. Am Anfang des Tages b" role=minimal-rewrite
E Lemma_de_fix_anfang_des_tages FROM_SESSION Session_anfang_des_tages SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-09-29-anfang-des-tages.toon.md
V Form_fix_anfang_des_tages_0_am_anfang_des_tag kind=form lang=de surface="am Anfang des Tages" fixes="Anfang bei dem Tag"
E Form_fix_anfang_des_tages_0_am_anfang_des_tag FROM_SESSION Session_anfang_des_tages

# ingest-session 2026-10-09T17:32:15Z proteingetraenke-becher lang=de
V Session_proteingetraenke_becher kind=session date=2026-10-09 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-proteingetraenke-becher.toon.md
V Focus_proteingetraenke_becher kind=focus lang=de gloss="Wenn es Unsicherheit gibt (wenn + es gibt)" status=active
E Focus_proteingetraenke_becher FROM_SESSION Session_proteingetraenke_becher
V Lemma_de_fix_proteingetraenke_becher kind=lemma lang=de surface="Die Proteingetränke – beide gleich – haben ich und" role=minimal-rewrite
E Lemma_de_fix_proteingetraenke_becher FROM_SESSION Session_proteingetraenke_becher SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-proteingetraenke-becher.toon.md
V Form_fix_proteingetraenke_becher_0_proteinget kind=form lang=de surface=Proteingetränke fixes=Proteinesgetränks
E Form_fix_proteingetraenke_becher_0_proteinget FROM_SESSION Session_proteingetraenke_becher
V Form_fix_proteingetraenke_becher_1_jeweils_ge kind=form lang=de surface="jeweils getrunken" fixes="jeden getrunken"
E Form_fix_proteingetraenke_becher_1_jeweils_ge FROM_SESSION Session_proteingetraenke_becher
V Form_fix_proteingetraenke_becher_2_wenn_es_be kind=form lang=de surface="Wenn es Unsicherheit gibt" fixes="Wenn bei … gibt es Unsicherheit"
E Form_fix_proteingetraenke_becher_2_wenn_es_be FROM_SESSION Session_proteingetraenke_becher
V Form_fix_proteingetraenke_becher_3_fragst_du_ kind=form lang=de surface="fragst du in der anderen Projektsitzung nach" fixes="fragst du zur anderen Projektsitzung"
E Form_fix_proteingetraenke_becher_3_fragst_du_ FROM_SESSION Session_proteingetraenke_becher
V Form_fix_proteingetraenke_becher_4_aus_dem_st kind=form lang=de surface="aus dem statischen Projekt selbst" fixes="von Statik Projekt selbst"
E Form_fix_proteingetraenke_becher_4_aus_dem_st FROM_SESSION Session_proteingetraenke_becher

# ingest-session 2026-10-09T17:39:36Z oeffentlicher-pr-bereich lang=de
V Session_oeffentlicher_pr_bereich kind=session date=2026-10-09 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-oeffentlicher-pr-bereich.toon.md
V Focus_oeffentlicher_pr_bereich kind=focus lang=de gloss="im öffentlichen Bereich (im + Dat, Bereich m.)" status=active
E Focus_oeffentlicher_pr_bereich FROM_SESSION Session_oeffentlicher_pr_bereich
V Lemma_de_fix_oeffentlicher_pr_bereich kind=lemma lang=de surface="Also gut, aber bitte stellen Sie ganz sicher, dass" role=minimal-rewrite
E Lemma_de_fix_oeffentlicher_pr_bereich FROM_SESSION Session_oeffentlicher_pr_bereich SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-oeffentlicher-pr-bereich.toon.md
V Form_fix_oeffentlicher_pr_bereich_0_kontaktin kind=form lang=de surface=Kontaktinfos fixes="Kontakt Info"
E Form_fix_oeffentlicher_pr_bereich_0_kontaktin FROM_SESSION Session_oeffentlicher_pr_bereich
V Form_fix_oeffentlicher_pr_bereich_1_im_ffentl kind=form lang=de surface="im öffentlichen Bereich" fixes="ins öffentliche Bereich"
E Form_fix_oeffentlicher_pr_bereich_1_im_ffentl FROM_SESSION Session_oeffentlicher_pr_bereich
V Form_fix_oeffentlicher_pr_bereich_2_im_ffentl kind=form lang=de surface="im öffentlichen Bereich des PRs" fixes="ins öffentliche Bereich PR"
E Form_fix_oeffentlicher_pr_bereich_2_im_ffentl FROM_SESSION Session_oeffentlicher_pr_bereich

# ingest-session 2026-10-09T18:01:05Z eine-fehlerliste lang=de
V Session_eine_fehlerliste kind=session date=2026-10-09 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-eine-fehlerliste.toon.md
V Focus_eine_fehlerliste kind=focus lang=de gloss="eine Fehlerliste (Akk. f.)" status=active
E Focus_eine_fehlerliste FROM_SESSION Session_eine_fehlerliste
V Lemma_de_fix_eine_fehlerliste kind=lemma lang=de surface="Also gut. Gib mir eine Fehlerliste meiner vorherig" role=minimal-rewrite
E Lemma_de_fix_eine_fehlerliste FROM_SESSION Session_eine_fehlerliste SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-eine-fehlerliste.toon.md
V Form_fix_eine_fehlerliste_0_eine_fehlerliste kind=form lang=de surface="eine Fehlerliste" fixes="ein Fehlerlist"
E Form_fix_eine_fehlerliste_0_eine_fehlerliste FROM_SESSION Session_eine_fehlerliste
V Form_fix_eine_fehlerliste_1_korrektur kind=form lang=de surface=Korrektur fixes=Korrigierung
E Form_fix_eine_fehlerliste_1_korrektur FROM_SESSION Session_eine_fehlerliste
V Form_fix_eine_fehlerliste_2_in_einer_latex_pd kind=form lang=de surface="in einer LaTeX-PDF-Datei" fixes="ins PDF LATEX Datei"
E Form_fix_eine_fehlerliste_2_in_einer_latex_pd FROM_SESSION Session_eine_fehlerliste

# ingest-session 2026-10-09T18:05:01Z darauf-zugreifen lang=de
V Session_darauf_zugreifen kind=session date=2026-10-09 lang=de body=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-darauf-zugreifen.toon.md
V Focus_darauf_zugreifen kind=focus lang=de gloss="darauf zugreifen (auf + Akk)" status=active
E Focus_darauf_zugreifen FROM_SESSION Session_darauf_zugreifen
V Lemma_de_fix_darauf_zugreifen kind=lemma lang=de surface="Also bin ich jetzt an meinem Handy. Wie kann ich d" role=minimal-rewrite
E Lemma_de_fix_darauf_zugreifen FROM_SESSION Session_darauf_zugreifen SOURCE=pedagogy/_learn/writing-accuracy/sessions/2026-10-09-darauf-zugreifen.toon.md
V Form_fix_darauf_zugreifen_0_an_meinem_handy kind=form lang=de surface="an meinem Handy" fixes="bei meinem Handy"
E Form_fix_darauf_zugreifen_0_an_meinem_handy FROM_SESSION Session_darauf_zugreifen
V Form_fix_darauf_zugreifen_1_darauf_zugreifen kind=form lang=de surface="darauf zugreifen" fixes="es zugreifen"
E Form_fix_darauf_zugreifen_1_darauf_zugreifen FROM_SESSION Session_darauf_zugreifen
