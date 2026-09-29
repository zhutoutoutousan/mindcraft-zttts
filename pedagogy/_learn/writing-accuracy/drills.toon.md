schema: learn/writing-accuracy-drills
lang: de
storageKey: mindcraft-de-drills-v2
updated: 2026-09-24
note: Substitution from attested Frames only. Not a CEFR workbook. Do not invent ANSWER. point: names the 考点 and must make the blank derivable — never a blind guess.

item:
  id: zu-1
  frame: zu_Dat_kenntnisstand
  kind: cloze
  point: zu + Dativ（三格）· Kenntnisstand 单数 → meinem
  prompt: Ich brauche Übungen, die ___ Kenntnisstand passen.
  accept: zu meinem | zu meinem vorhandenen
  hint: zu + Dativ, nicht nach

item:
  id: zu-2
  frame: zu_Dat_kenntnisstand
  kind: cloze
  point: zu + Dativ Plural → meinen
  prompt: Die Korrektur passt ___ Deutschkenntnissen.
  accept: zu meinen | zu meinen vorhandenen
  hint: Dat. Plural: meinen

item:
  id: zu-3
  frame: zu_Dat_kenntnisstand
  kind: cloze
  point: zu + Dativ · der Stand 是阳性 → diesem
  prompt: Der Plan passt ___ Stand.
  accept: zu diesem
  hint: Stand ist maskulin; Dat. Maskulinum = diesem

item:
  id: prep-fuer
  frame: fuer_purpose
  kind: choice
  point: 介词三选一 · 目的/当天时间点 = für
  prompt: Zweck oder Zeit — ___ heute
  choices: für | nach | zu
  answer: für
  hint: für = purpose/time today; nach = after

item:
  id: prep-nach
  frame: fuer_purpose
  kind: choice
  point: nach + Dativ = 时间上之后
  prompt: Zeitlich danach — ___ dem Training
  choices: für | nach | zu
  answer: nach
  hint: nach + Dat = after

item:
  id: prep-zu
  frame: zu_Dat_kenntnisstand
  kind: choice
  point: zu = 按、符合（Niveau/Ebene）
  prompt: Gemäß Niveau — ___ meinem Kenntnisstand
  choices: für | nach | zu
  answer: zu
  hint: zu + Dat = according to the level

item:
  id: auf-laptop
  frame: auf_Dat_device
  kind: cloze
  point: auf + Dativ · 位置在设备上
  prompt: Der aktuelle Zustand liegt jetzt ___ Laptop.
  accept: auf meinem
  hint: Lage auf Gerät = auf + Dat, nicht in

item:
  id: dieses-projekt
  frame: det_Akk_neut
  kind: cloze
  point: Akkusativ Neutrum → dieses
  prompt: Gib mir eine TODO-Liste für ___ Projekt.
  accept: dieses
  hint: Projekt ist Neutrum → dieses

item:
  id: aktueller-zustand
  frame: det_Nom_masc
  kind: cloze
  point: Nominativ Maskulinum · 定冠词 + 形容词 -e
  prompt: ___ Zustand liegt auf meinem Laptop.
  accept: Der aktuelle | der aktuelle
  hint: aktuell = current, nicht aktualisiert; mask. braucht Artikel

item:
  id: lass-uns
  frame: lass_uns_Vinf
  kind: cloze
  point: lass uns + 副词 + 动词（副词在动词前）
  prompt: Okay, lass uns ___ eintauchen.
  accept: tiefer
  hint: Adverb vor dem Verb: tiefer eintauchen

item:
  id: korrektur
  frame: korrektur_nicht_korrigierung
  kind: choice
  point: Nomen-Wahl · die Korrektur（Korrigierung 不存在）
  prompt: Es gibt noch keine ___ .
  choices: Korrektur | Korrigierung
  answer: Korrektur
  hint: die Korrektur, nicht Korrigierung

item:
  id: um-zu
  frame: um_zu_infinitiv
  kind: cloze
  point: um … zu + Infinitiv = 目的
  prompt: Mach ein Diagramm mit Archify, ___ es zu testen.
  accept: um
  hint: Zweck = um … zu + Inf

item:
  id: erster-test
  frame: mein_erster_N_m
  kind: cloze
  point: Possessiv + Ordinalzahl: mein erster（阳性）
  prompt: Das ist ___ Test.
  accept: mein erster | mein erster.
  hint: mask. Nom. mein + -er, nicht Erste

item:
  id: haette-gern
  frame: haette_gern_zuerst
  kind: choice
  point: Konjunktiv II · 客气愿望 = hätte
  prompt: Höflicher Wunsch — Ich ___ gern zuerst mein Dashboard einzusehen.
  choices: hätte | hatte | hatte gehabt
  answer: hätte
  hint: Konjunktiv II, nicht Präteritum hatte

item:
  id: grasp-rewrite
  frame: zu_Dat_kenntnisstand
  kind: rewrite
  point: 英语词 Grasp → Kenntnisstand
  prompt: Ersetze die englische Insel Grasp. Ein Satz.
  stem: Ich brauche Übungen nach meine vorhande Grasp.
  mustInclude: kenntnisstand
  accept: Ich brauche Übungen, die zu meinen vorhandenen Deutschkenntnissen passen.
  hint: Kenntnisstand, nicht Grasp

item:
  id: koerperteile-1
  frame: andere_koerperteile_akk_pl
  kind: cloze
  point: Akkusativ Plural 无词尾 → andere
  prompt: Ich möchte heute ___ Körperteile trainieren.
  accept: andere
  hint: Körperteile ist Akk. Plural ohne Endung: andere, nicht anderes

item:
  id: koerperteile-2
  frame: andere_koerperteile_akk_pl
  kind: choice
  point: Akkusativ Plural → andere（不是 anderes/anderen）
  prompt: Akk. Plural — Ich trainiere ___ Körperteile.
  choices: andere | anderes | anderen
  answer: andere
  hint: Plural ohne -s-Endung am Artikelwort: andere

item:
  id: ich-logge-1
  frame: verbzweitstellung_ich_logge
  kind: cloze
  point: Verbzweitstellung · Heute + 动词 + ich
  prompt: Heute ___ ich mein Training in die Datei.
  accept: logge
  hint: Verbzweitstellung: Heute + Verb + ich

item:
  id: planung-1
  frame: planung_spelling
  kind: choice
  point: 拼写 · Plan + ung = Planung（单 n）
  prompt: Richtig geschrieben — die ___ für morgen
  choices: Planung | Plannung
  answer: Planung
  hint: Plan mit einem n: Planung

item:
  id: zu-mir-1
  frame: zu_pronomen_akk
  kind: cloze
  point: zu + 人称代词 → zu mir（zur = zu der，不接人称代词）
  prompt: Kannst du die Übung ___ schicken?
  accept: zu mir
  hint: zu + Personalpronomen: zu mir, nie zur mir

item:
  id: uebung-zum-1
  frame: uebung_zum_sprachenlernen
  kind: cloze
  point: zum (= zu dem) + 名词化 = 目的
  prompt: Ich brauche eine Übung ___ Sprachenlernen.
  accept: zum | fürs
  hint: Zweck/Substantiv: zum (zu dem) Sprachenlernen, nicht auf

item:
  id: dass-rueckfall
  frame: orth_dass
  kind: choice
  point: Konjunktion dass · seit 1996 immer ss, nie ß
  prompt: Ich hätte gern, ___ alles im privaten Bereich bleibt.
  choices: daß | dass
  answer: dass
  hint: Rückfall-Fehler seit 2026-09-12; alte Schreibung ß ist falsch

item:
  id: adj-en-dat-plural
  frame: schwache_dekl_en
  kind: cloze
  point: schwache Deklination · nach Artikel im Dat. Plural = -en → wiederholenden
  prompt: Ich übe mit sofortigen und ___ Übungen.
  accept: wiederholenden
  hint: parallel zu sofortigen: -en

item:
  id: ss-kurzer-vokal
  frame: orth_dass
  kind: cloze
  point: ß/ss-Regel · ss nach KURZEM Vokal — dass hat kurzes a, also ss
  prompt: Ich weiß, ___ alles gut läuft. (Konjunktion; der Vokal ist kurz)
  accept: dass
  hint: Konjunktion heißt immer dass (ss); das wäre Artikel/Pronomen

item:
  id: ss-diphthong-aussen
  frame: orth_dass
  kind: cloze
  point: ß nach Diphthong au — außen, nicht aussen; ss nur nach kurzem Vokal
  prompt: Das Haus ist ___ grün und innen weiß. (Diphthong au)
  accept: außen
  hint: au ist ein Diphthong (lang) → ß; Wasser und nass sind kurz → ss

item:
  id: umgang-laden
  frame: laden_schmeissen
  kind: cloze
  point: den Laden schmeißen · Akk. den Laden · Präteritum schmiss
  prompt: Nach der Einarbeitung ___ sie den ___ ganz allein.
  accept: schmiss den Laden | schmiss den Laden
  hint: schmeißen → schmiss; den Laden (Akk.)

item:
  id: umgang-faust
  frame: faust_tasche
  kind: cloze
  point: eine Faust in der Tasche machen · Dativ in der Tasche · Verb machen
  prompt: Der Vater ___ öfter die Faust in der ___, ohne laut zu protestieren.
  accept: machte Tasche
  hint: machen, nicht haben; in der Tasche = Dativ

item:
  id: umgang-rolle
  frame: sich_in_rolle_sehen
  kind: cloze
  point: sich in einer Rolle sehen · Reflexiv + in + Dativ
  prompt: Sie ___ schon früh in der ___ einer Chefin.
  accept: sah sich Rolle
  hint: sich sehen; in der Rolle (Dat.)

item:
  id: umgang-nacken
  frame: im_nacken_sitzen
  kind: cloze
  point: jemanden im Nacken sitzen haben · Akk. Person + haben
  prompt: Sie wollte ihn nicht im Nacken sitzen ___.
  accept: haben
  hint: feste Klammer: sitzen haben, nicht sitzen wollen allein

