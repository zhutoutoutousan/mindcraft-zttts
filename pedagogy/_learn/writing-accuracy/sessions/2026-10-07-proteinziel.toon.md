schema: learn/writing-accuracy-session
date: 2026-10-07
id: proteinziel-2026-10-07
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Pro-Person-Makrotabelle (Halb-Halb) + Proteinpulver-Menge je Ziel.
original: "[Name] wiegt [Gewicht], Größe [Groesse]. Partnerin wiegt [Gewicht], Größe 168cm. Kalkulieren Sie jeder Tabellen, als ob halb halb gegessen. Und wie viel Gram oder Löffel von Protein Pulver zu nehmen, um Ziel zu erreichen. [Name] macht Gewichtheben, Muskelvoll, normalerweise 150g Proteine pro Tag. Partnerin zum ihrer Empfehlung"
corrected: "[Name] wiegt [Gewicht] bei [Groesse], Partnerin [Gewicht] bei 168 cm. Berechnen Sie für jede(n) eine Tabelle, als ob beide die Hälfte gegessen hätten. Und wie viele Gramm bzw. Messlöffel Proteinpulver sollten sie nehmen, um das Ziel zu erreichen? [Name] trainiert Gewichtheben und macht Muskelaufbau — normalerweise 150 g Protein pro Tag. Partnerin: nach Ihrer Empfehlung."
oneFocus: "Mengenfrage: wie viele + zaehlbare Einheit (Gramm, Messlöffel); wie viel nur bei Unzaehlbarem"
reuseNextSession: "Wie viele Gramm Proteinpulver soll ich nehmen, um mein Proteinziel zu erreichen?"
errorTypes: [grammatik_quantor, lexik_wortwahl, praeposition, kollokation]
gaps:
  - gap: "wie viel Gram oder Löffel"
    hit: "wie viele Gramm bzw. Messlöffel"
    frame: "[wie viel/wie viele] + Mengeneinheit"
confidence: high

errors_brief:
  - "wie viel Gram oder Löffel -> wie viele Gramm bzw. Messlöffel: zaehlbare Einheiten nehmen 'wie viele'; 'Gramm' bleibt bei Zahlen pluralisch."
  - "Kalkulieren Sie jeder Tabellen -> Berechnen Sie für jede(n) eine Tabelle: wieder kalkulieren statt berechnen; 'jeder' + Akkusativ-Plural passt nicht."
  - "Muskelvoll -> Muskelaufbau; 'Partnerin zum ihrer Empfehlung' -> 'Partnerin: nach Ihrer Empfehlung' (zum->nach, ihrer->Ihrer)."
