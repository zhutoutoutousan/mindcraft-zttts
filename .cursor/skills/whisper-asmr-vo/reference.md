# Whisper ASMR VO — true whisper

## What failed before

edge-tts Katja at `-24%` plus a dark EQ is still **modal voice** (真声). The free Edge endpoint rejects `<mstts:express-as style="whispering">` (`NoAudioReceived`).

## Pipeline that is actually whisper

1. German TTS (Katja) at about `-10%` — keep formants.
2. **WORLD** (`pyworld`): harvest F0 → CheapTrick envelope → D4C → synthesize with **F0 = 0** and **aperiodicity = 1**. Glottal pulse gone; breath noise carries the words.
3. Light close-mic: highpass, air boost around 5.5 kHz, Haas. Do **not** low-pass at 4 kHz.

`pip install pyworld`

## Captions

ASS `PlayResX=1920 PlayResY=1080`. Style DE: Segoe UI 44, primary `&H00D4E0E8`, outline 2.2, margin v=72. Wrap ~40 characters. German only. SRT sidecar; ASS is burnt.
