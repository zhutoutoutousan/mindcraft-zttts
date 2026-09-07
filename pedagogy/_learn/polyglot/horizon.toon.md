schema: learn/polyglot-horizon
kind: learner-horizon
vertex: PolyglotHorizon
created: 2026-09-07
as_of: 2026-09-07
age_now: 30
age_target: 35
years: 5
deadline_year: 2031
want: B2+ productive skill in 16 languages (raise limited/elementary toward B2+)
count: 16
status: open
slots_unnamed: 0

# Human self-rating 2026-09-07 (LinkedIn-style bands). Not invented CEFR.
# Prior CV/SPRACHEN notes kept separately where they differ.
langs[16]{code,name,band,script}:
  de,Deutsch,professional_working,Latn
  en,English,native_or_bilingual,Latn
  es,Español,limited_working,Latn
  fr,Français,limited_working,Latn
  it,Italiano,limited_working,Latn
  pt,Português,limited_working,Latn
  fi,Suomi,elementary,Latn
  vi,Tiếng Việt,elementary,Latn
  el,Ελληνικά,elementary,Grek
  ru,русский,limited_working,Cyrl
  ar,عربي,elementary,Arab
  hi,हिन्दी,elementary,Deva
  zh,中文,native_or_bilingual,Hans
  wuu,吴语,native_or_bilingual,Hans
  ja,日本語,limited_working,Jpan
  ko,한국어,elementary,Kore

native_or_bilingual[3]: en, zh, wuu
professional_working[1]: de
limited_working[6]: es, fr, it, pt, ru, ja
elementary[6]: fi, vi, el, ar, hi, ko

credential_note:
  en: prior IELTS 7.5 / C1 teaching attestation still in lebenslauf; self-rate today native_or_bilingual
  de: prior Goethe B2+ / Studium Beruf; self-rate today professional_working
  es: prior verhandlungssicher Avature; self-rate today limited_working — use today for polyglot pacing; do not invent which is "true"

default_arbitrage_target: de
rule: Do not invent CEFR numbers beyond these bands. Wu (吴语) is listed separately from 中文 as the human named it.

pace_hint:
  five_years: raise limited_working + elementary toward B2+ while maintaining native/professional; pacing only
  weekly: one targetLang coding-arbitrage focus (default de); Wordschatz apps remain separate load units

stores:
  method: pedagogy/_learn/polyglot/pairing.toon.md
  state: pedagogy/_learn/writing-accuracy/state.toon.md
  signal: pedagogy/_learn/polyglot/last-signal.toon.md
  lexicon_de: pedagogy/_learn/writing-accuracy/lexicon.graph.md
  frames_de: pedagogy/_learn/polyglot/frames/de.toon.md
  bridge: pedagogy/_learn/polyglot/bridge.graph.md

source: human 2026-09-07 named 16-language proficiency list
source: self/goals.toon.md
