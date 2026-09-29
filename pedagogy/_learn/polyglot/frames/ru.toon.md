schema: learn/grammar-frames
lang: ru
updated: 2026-09-27
note: Frames own slots. Lemmas fill slots. Only verified direct Russian lemma pages with German explanations are linked; frames without one remain source-free.

frame:
  id: ja_schitaju_chto
  gloss: state-an-opinion
  pattern: Я считаю, что + finite clause
  slots[1]: CLAUSE
  fillers[1]: это-хороший-способ-учиться
  anti: Я считаю это хороший способ учиться
  concept: express-opinion

frame:
  id: mne_kazhetsja_chto
  gloss: state-an-impression
  pattern: Мне кажется, что + finite clause
  slots[1]: CLAUSE
  fillers[1]: этот-текст-слишком-сложный
  anti: Мне кажется этот текст слишком сложный
  concept: express-impression

frame:
  id: u_menja_N_nom
  gloss: have-an-opinion
  pattern: У меня + N (Nom)
  slots[1]: N_nom
  fillers[1]: другое-мнение
  anti: Я имею другое мнение
  concept: express-different-opinion

frame:
  id: ja_poka_ne_ochen_ADV_V
  gloss: limited-understanding-so-far
  pattern: Я пока не очень хорошо + V
  slots[1]: V_1sg
  fillers[1]: понимаю
  anti: Я не понимаю пока очень хорошо
  concept: state-current-comprehension

frame:
  id: ne_mogli_by_vy_inf
  gloss: polite-request-conditional
  pattern: Не могли бы вы + Inf, пожалуйста?
  slots[1]: V_inf
  fillers[1]: повторить
  anti: Вы можете повторить, пожалуйста? when formal politeness is intended
  concept: ask-to-repeat-politely

frame:
  id: ja_pytajus_inf
  gloss: attempt-to-speak
  pattern: Я пытаюсь + Inf
  slots[1]: V_inf
  fillers[1]: говорить-по-русски
  anti: Я пытаюсь, говорить по-русски
  concept: express-effort-to-speak
  source: de-wiktionary-ru-pytatsja
