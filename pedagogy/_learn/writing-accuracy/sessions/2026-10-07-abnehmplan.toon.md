schema: learn/writing-accuracy-session
date: 2026-10-07
id: abnehmplan-2026-10-07
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: [Name] im Abnahmemodus; Pulver-Mengen + Rest-Tagesplan.
original: "Also gut Ich [Name] will abnehmen, so brauche ich kalorie Defizit. Also Gib mir solche sowieso nach für [Name] vielleicht 3-4 Löffel Protein Pulver, und 2 Löffel für Partnerin was mehr zu nehmen heute?"
corrected: "Also gut, ich, [Name], will abnehmen — ich brauche also ein Kaloriendefizit. Geben Sie mir die Empfehlung trotzdem: für [Name] vielleicht 3–4 Löffel Proteinpulver und für Partnerin 2 Löffel — was sollen wir heute noch essen?"
oneFocus: "W-Frage mit Modalverb: [was] + V2 + Subjekt + noch + Infinitiv"
reuseNextSession: "Was sollen wir heute noch essen?"
errorTypes: [wortstellung, kompositum, modalverb]
gaps:
  - gap: "was mehr zu nehmen heute"
    hit: "was sollen wir heute noch zu uns nehmen"
    frame: "[Fragewort] + [Modalverb] + [Subjekt] + [Zeit] + [noch] + [Infinitiv]"
confidence: high

errors_brief:
  - "was mehr zu nehmen heute? -> was sollen wir heute noch essen?: Modalverb fehlt; V2 in der Frage; 'noch' vor dem Infinitiv."
  - "kalorie Defizit -> Kaloriendefizit: Nomen-Kompositum als ein Wort, gross geschrieben."
  - "Ich [Name] will -> ich, [Name], will: Apposition mit Kommas; 'Gib mir solche sowieso nach' -> 'Geben Sie mir die trotzdem'."
