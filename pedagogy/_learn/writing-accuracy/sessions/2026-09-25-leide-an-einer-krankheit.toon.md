schema: learn/writing-accuracy-session
date: 2026-09-25
id: leide-an-einer-krankheit
lang: de
meta:
  task: written_expression
  methodHit: true
  method: writing-accuracy-base-arbitrage
  note: Job was log named illness and stop DAY load. DE report. Not a diagnosis.

original: Heute leide ich erheblich Krankheit, d.h. Sore throat, erhöhte körperliche Temperatur usw. Vielleicht gibt es Infektionen bei mir

corrected: Heute leide ich erheblich an einer Krankheit, d. h. Halsschmerzen, erhöhte Körpertemperatur usw. Vielleicht habe ich eine Infektion.

oneFocus: leiden an + Dat.
reuseNextSession: Heute leide ich erheblich an einer Krankheit.
errorTypes: leiden_an_dat,lexis
gaps: leide ich erheblich Krankheit → leide ich erheblich an einer Krankheit; Sore throat → Halsschmerzen; körperliche Temperatur → Körpertemperatur; gibt es Infektionen bei mir → habe ich eine Infektion
confidence: high

errors_brief[3]:
  erheblich Krankheit → erheblich an einer Krankheit (leiden an + Dat.)
  Sore throat → Halsschmerzen
  gibt es Infektionen bei mir → habe ich eine Infektion
