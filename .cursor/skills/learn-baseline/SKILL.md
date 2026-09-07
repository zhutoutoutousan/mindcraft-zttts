---
name: learn-baseline
description: Serves the 摸底 baseline HTML with per-language Speak-to-text, ingests answers, and must not invent ANSWER. Use when the human asks for the probe HTML, voice answers, baseline, 摸底, Speak button, or python cron/learn-enrich.py --baseline-serve.
---

# Learn baseline 摸底

## Serve

```
python cron/learn-enrich.py --baseline-serve
```

Binds `127.0.0.1:8765`, then `8777`, then `8778` if busy. Print the URL it actually bound. Do not tell the human 8765 if the log says 8777.

Open in **Chrome or Edge**. Not the Cursor Simple Browser. SpeechRecognition and getUserMedia fail there, so Speak never fills the box.

## Voice

Collapse Whisper loops (`It's a bit wrong` repeated). Mute onnxruntime unused-initializer warnings. Each Stop merges one cleaned utterance, does not append the same sentence.

Test mic: bar `#meter` plus 4s record and playback. Console `mic-test-level` / `mic-test-done`. If peak stays `silent`, the device never reached the page. Parenthesis-only Whisper output like `(whistling)` is discarded.

## After Save   

```
python cron/learn-enrich.py --ingest-baseline
```

`--apply-study` only when asked. English wins for STUDY ANSWER else first filled language. Expression samples stay in `pedagogy/_learn/baseline.toon.md`. Empty skip. Never invent ANSWER. Do not add Chinese as native. Stop if sore. Not DAY LOAD.

## Store

- probes: `pedagogy/_learn/baseline-probes.toon.md`
- html: `tmp/pedagogy/baseline.html`
- live answers: `tmp/pedagogy/baseline-answers.toon.md`
- renderer: `cron/learn-enrich.py` `render_baseline_html`
