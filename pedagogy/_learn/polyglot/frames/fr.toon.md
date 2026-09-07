schema: learn/grammar-frames
lang: fr
updated: 2026-09-07
note: Frames own slots. First FR seed from writing-accuracy probe.

frame:
  id: ajouter_a_NP
  gloss: add-something-to-a-store
  pattern: ajouter + NP + à / au / à la / aux + NP
  slots[2]: NP_obj, NP_destination
  fillers[2]: ceci, au-knowledge-graph
  anti: ajouter sur + NP (calque EN/DE "on/auf")
  concept: add-to-knowledge-graph
  from_session: 2026-09-07-fr-probe

frame:
  id: pourriez_vous_Inf
  gloss: polite-request-conditional
  pattern: Pourriez-vous + Inf (+ complement)
  slots[1]: V_inf_chain
  fillers[1]: m-expliquer-et-ajouter
  anti: tu peux / can you calque without vous-form when register is formal
  concept: polite-ask-explain-and-add
  from_session: 2026-09-07-fr-probe
