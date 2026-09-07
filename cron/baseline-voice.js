/* 摸底 Speak. Filter console: [baseline-voice]
 * Chrome SpeechRecognition is Google-cloud. error=network + onaudiostart→onaudioend
 * usually means the mic was still held by getUserMedia, or Google STT is unreachable.
 * We release the permission stream before rec.start(), then fall back to local whisper.
 */
const boot = window.BASELINE_BOOT || {};
const PROBES = boot.probes || [];
const LANGS = boot.langs || ["en", "zh", "fr", "de"];
const BCP47 = boot.bcp47 || { en: "en-GB", zh: "zh-CN", fr: "fr-FR", de: "de-DE" };
const KEY = boot.key || "baseline-lang4-voice-2026-09-02";
const WHISPER_LANG = { en: "english", zh: "chinese", fr: "french", de: "german" };
const SpeechAPI = window.SpeechRecognition || window.webkitSpeechRecognition;
const total = PROBES.length * LANGS.length;
const areas = [...document.querySelectorAll("article[data-id]")];

let live = null;
let seq = 0;
let asrPromise = null;
let saveTimer = null;
let micTest = null;

function setMeter(rms) {
  const fill = document.getElementById("meter-fill");
  const num = document.getElementById("meter-num");
  const pct = Math.min(100, Math.round(rms * 220));
  if (fill) fill.style.width = pct + "%";
  if (num) num.textContent = rms < 0.012 ? "silent" : rms.toFixed(2);
}

function vlog(step, extra) {
  const row = Object.assign(
    {
      t: Date.now(),
      seq,
      step,
      href: String(location.href),
      ua: navigator.userAgent.slice(0, 88),
      secure: !!window.isSecureContext,
      speechCtor: SpeechAPI ? SpeechAPI.name : "none",
      live: !!live,
      mode: live && live.mode,
      keep: !!(live && live.keep),
      lang: live && live.lang,
      boxLen: live && live.box ? (live.box.value || "").length : null,
    },
    extra || {}
  );
  console.log("%c[baseline-voice]", "color:#69f0ae;font-weight:700", step, row);
}

function setStatus(msg) {
  document.getElementById("status").textContent = msg;
  vlog("status", { msg });
}

function stopTracks(stream) {
  if (!stream) return;
  stream.getTracks().forEach((t) => {
    vlog("track-stop", { kind: t.kind, ready: t.readyState, label: t.label });
    try {
      t.stop();
    } catch (e) {}
  });
}

function clearLiveUi() {
  document.querySelectorAll("button.mic").forEach((b) => {
    b.classList.remove("live");
    b.textContent = "Speak";
  });
  document.querySelectorAll("textarea.listening").forEach((el) => el.classList.remove("listening"));
}

function stopLive(why) {
  vlog("stopLive", { why: why || "" });
  if (!live) {
    clearLiveUi();
    return;
  }
  live.keep = false;
  const rec = live.rec;
  const recoder = live.recorder;
  const stream = live.stream;
  const pending = live.stopResolve;
  live = null;
  try {
    rec && rec.stop();
  } catch (e) {
    vlog("rec.stop-throw", { err: String(e) });
  }
  try {
    if (recoder && recoder.state === "recording") recoder.stop();
  } catch (e) {
    vlog("recorder.stop-throw", { err: String(e) });
  }
  stopTracks(stream);
  clearLiveUi();
  if (pending) pending();
}

function collect() {
  const out = {};
  areas.forEach((el) => {
    const id = el.getAttribute("data-id");
    const row = {};
    LANGS.forEach((lang) => {
      const box = el.querySelector('textarea[data-lang="' + lang + '"]');
      row[lang] = ((box && box.value) || "").trim();
    });
    out[id] = row;
  });
  return out;
}

function restore(data) {
  areas.forEach((el) => {
    const id = el.getAttribute("data-id");
    let row = data[id];
    if (typeof row === "string") row = { en: row, zh: "", fr: "", de: "" };
    if (!row) return;
    LANGS.forEach((lang) => {
      const box = el.querySelector('textarea[data-lang="' + lang + '"]');
      if (box && row[lang]) box.value = row[lang];
    });
  });
}

function filledCount(data) {
  let n = 0;
  Object.values(data).forEach((row) => {
    LANGS.forEach((lang) => {
      if ((row[lang] || "").trim()) n += 1;
    });
  });
  return n;
}

async function save(status) {
  if (live && status !== "done") {
    vlog("save-skipped-while-live", { status });
    return;
  }
  const data = collect();
  localStorage.setItem(KEY, JSON.stringify(data));
  const n = filledCount(data);
  document.getElementById("status").textContent = "saving " + n + "/" + total;
  try {
    const res = await fetch(status === "done" ? "/done" : "/save", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ status: status || "open", answers: data }),
    });
    if (!res.ok) throw new Error("http " + res.status);
    document.getElementById("status").textContent =
      (status === "done" ? "done · " : "saved · ") + n + "/" + total + " boxes · " + new Date().toLocaleTimeString();
  } catch (e) {
    document.getElementById("status").textContent = "local only · " + n + "/" + total + " · use Download backup";
  }
}

function armUi(btn, box) {
  btn.classList.add("live");
  btn.textContent = "Stop";
  box.classList.add("listening");
  box.focus();
}

async function openMic() {
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    throw new Error("no-mic-api");
  }
  vlog("getUserMedia-call", {});
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  vlog("getUserMedia-ok", {
    tracks: stream.getAudioTracks().map((t) => ({
      label: t.label,
      muted: t.muted,
      enabled: t.enabled,
      ready: t.readyState,
    })),
  });
  return stream;
}

function downsampleMono(channel, fromRate, toRate) {
  if (fromRate === toRate) return channel;
  const ratio = fromRate / toRate;
  const n = Math.max(1, Math.round(channel.length / ratio));
  const out = new Float32Array(n);
  for (let i = 0; i < n; i++) {
    const x = i * ratio;
    const i0 = Math.floor(x);
    const i1 = Math.min(channel.length - 1, i0 + 1);
    const f = x - i0;
    out[i] = channel[i0] * (1 - f) + channel[i1] * f;
  }
  return out;
}

function attachMeter(stream) {
  const ctx = new AudioContext();
  const src = ctx.createMediaStreamSource(stream);
  const analyser = ctx.createAnalyser();
  analyser.fftSize = 2048;
  src.connect(analyser);
  const wave = new Uint8Array(analyser.fftSize);
  const state = { peak: 0, raf: 0, ctx, keep: true };
  let lastLog = 0;
  function tick() {
    if (!state.keep) return;
    analyser.getByteTimeDomainData(wave);
    let sum = 0;
    for (let i = 0; i < wave.length; i++) {
      const v = (wave[i] - 128) / 128;
      sum += v * v;
    }
    const rms = Math.sqrt(sum / wave.length);
    if (rms > state.peak) state.peak = rms;
    setMeter(rms);
    if (Date.now() - lastLog > 400) {
      vlog("meter", { rms, peak: state.peak });
      lastLog = Date.now();
    }
    state.raf = requestAnimationFrame(tick);
  }
  ctx.resume().then(() => tick());
  state.stop = () => {
    state.keep = false;
    if (state.raf) cancelAnimationFrame(state.raf);
    try {
      ctx.close();
    } catch (e) {}
    setMeter(state.peak);
  };
  return state;
}

function collapseRepeats(text) {
  let t = (text || "").replace(/\s+/g, " ").trim();
  if (!t) return "";
  const parts = t.split(/(?<=[.!?])\s+/).map((s) => s.trim()).filter(Boolean);
  if (!parts.length) return t;
  const first = parts[0];
  if (parts.length >= 2 && parts.every((p) => p.toLowerCase() === first.toLowerCase())) return first;
  const out = [];
  for (const p of parts) {
    if (!out.length || out[out.length - 1].toLowerCase() !== p.toLowerCase()) out.push(p);
  }
  t = out.join(" ");
  const compact = t.replace(/\s+/g, " ");
  for (let n = Math.min(80, Math.floor(compact.length / 2)); n >= 8; n--) {
    const unit = compact.slice(0, n).trim();
    if (!unit) continue;
    const esc = unit.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const re = new RegExp("^(?:" + esc + "[\\s.?!]*)+$", "i");
    if (re.test(compact) && compact.length >= unit.length * 2) return unit.replace(/[.!?]+$/, "").trim() + (unit.endsWith(".") ? "." : "");
  }
  return t;
}

function mergeUtterance(prev, next) {
  const a = collapseRepeats(prev);
  const b = collapseRepeats(next);
  if (!b) return a;
  if (!a) return b;
  if (a.toLowerCase().includes(b.toLowerCase())) return a;
  if (b.toLowerCase().includes(a.toLowerCase())) return b;
  return collapseRepeats(a + " " + b);
}

function quietOnnx() {
  if (console.__onnxQuiet) return;
  console.__onnxQuiet = true;
  const warn = console.warn.bind(console);
  console.warn = (...args) => {
    const s = args.map((a) => String(a)).join(" ");
    if (s.includes("onnxruntime") || s.includes("CleanUnusedInitializers")) return;
    warn(...args);
  };
}

function getAsr() {
  if (!asrPromise) {
    vlog("whisper-load", {});
    quietOnnx();
    asrPromise = import("https://cdn.jsdelivr.net/npm/@xenova/transformers@2.17.2").then(({ env, pipeline }) => {
      env.allowLocalModels = false;
      return pipeline("automatic-speech-recognition", "Xenova/whisper-tiny");
    });
  }
  return asrPromise;
}

async function transcribeBlob(blob, lang) {
  vlog("whisper-decode", { bytes: blob.size, type: blob.type, lang });
  const ctx = new AudioContext();
  const buf = await blob.arrayBuffer();
  const audio = await ctx.decodeAudioData(buf.slice(0));
  const data = downsampleMono(audio.getChannelData(0), audio.sampleRate, 16000);
  vlog("whisper-audio", { sampleRate: audio.sampleRate, samples: data.length, duration: audio.duration, out16k: data.length });
  const asr = await getAsr();
  const out = await asr(data, {
    sampling_rate: 16000,
    language: WHISPER_LANG[lang] || "english",
    task: "transcribe",
    chunk_length_s: 20,
    stride_length_s: 3,
  });
  const raw = (out && (out.text || out[0]?.text) || "").trim();
  const text = collapseRepeats(raw);
  vlog("whisper-out", { raw, text });
  if (/^\([^)]+\)(\s+\([^)]+\))*$/.test(text)) {
    vlog("whisper-sfx-discard", { text });
    return "";
  }
  return text;
}

async function startLocal(btn, lang, box, prefix) {
  setStatus("recording · speak now · bar must move · Stop when done");
  const stream = await openMic();
  const meter = attachMeter(stream);
  const mime = MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
    ? "audio/webm;codecs=opus"
    : MediaRecorder.isTypeSupported("audio/webm")
      ? "audio/webm"
      : "";
  const chunks = [];
  const recorder = mime ? new MediaRecorder(stream, { mimeType: mime }) : new MediaRecorder(stream);
  vlog("recorder-start", { mime: recorder.mimeType, skipChrome: true });
  recorder.ondataavailable = (ev) => {
    if (ev.data && ev.data.size) chunks.push(ev.data);
    vlog("recorder-chunk", { bytes: ev.data && ev.data.size, peak: meter.peak });
  };
  let stopResolve = null;
  const stopped = new Promise((resolve) => {
    stopResolve = resolve;
  });
  recorder.onstop = () => {
    vlog("recorder-stop", { chunks: chunks.length, peak: meter.peak });
    if (stopResolve) stopResolve();
  };
  live = { mode: "local", rec: null, recorder, stream, btn, box, keep: true, lang, stopResolve };
  armUi(btn, box);
  recorder.start(250);
  await stopped;
  meter.stop();
  stopTracks(stream);
  const blob = new Blob(chunks, { type: recorder.mimeType || "audio/webm" });
  vlog("record-done", { bytes: blob.size, peak: meter.peak, durationHint: chunks.length });
  if (meter.peak < 0.02) {
    setStatus("bar stayed silent — Test mic first. Chrome → site settings → mic for 127.0.0.1.");
    return;
  }
  if (!blob.size) {
    setStatus("local recording empty. Type the answer, or try Speak again.");
    return;
  }
  setStatus("transcribing locally… peak " + meter.peak.toFixed(2));
  try {
    const text = await transcribeBlob(blob, lang);
    if (!text) {
      setStatus("mic had signal (peak " + meter.peak.toFixed(2) + ") but model returned noise. Type the answer.");
      return;
    }
    box.value = mergeUtterance(prefix, text);
    setStatus("heard (local): " + box.value.slice(-80));
    save("open");
  } catch (e) {
    vlog("whisper-fail", { err: String(e) });
    setStatus("local transcribe failed: " + e + " · type the answer");
  }
}

function startChromeSpeech(btn, lang, box) {
  const rec = new SpeechAPI();
  rec.lang = BCP47[lang] || "en-GB";
  rec.continuous = true;
  rec.interimResults = true;
  rec.maxAlternatives = 1;
  const committed = (box.value || "").replace(/\s+$/, "");
  const prefix = committed ? committed + " " : "";
  let sawResult = false;
  let fellBack = false;
  live = { mode: "chrome", rec, recorder: null, stream: null, btn, box, keep: true, lang };
  rec.onstart = () => {
    vlog("onstart", {});
    setStatus("listening " + lang + " · " + rec.lang + " · speak, then Stop");
  };
  rec.onaudiostart = () => vlog("onaudiostart", {});
  rec.onaudioend = () => vlog("onaudioend", { sawResult });
  rec.onsoundstart = () => vlog("onsoundstart", {});
  rec.onsoundend = () => vlog("onsoundend", {});
  rec.onspeechstart = () => {
    vlog("onspeechstart", {});
    setStatus("speech detected " + lang);
  };
  rec.onspeechend = () => vlog("onspeechend", {});
  rec.onnomatch = () => vlog("onnomatch", {});
  rec.onresult = (ev) => {
    sawResult = true;
    let acc = "";
    let interim = "";
    const parts = [];
    for (let i = 0; i < ev.results.length; i++) {
      const t = ev.results[i][0].transcript;
      parts.push({ i, final: ev.results[i].isFinal, t });
      if (ev.results[i].isFinal) acc += t + " ";
      else interim += t;
    }
    box.value = (prefix + acc + interim).replace(/ +/g, " ").replace(/^ /, "");
    vlog("onresult", { resultIndex: ev.resultIndex, n: ev.results.length, parts, box: box.value });
    setStatus("heard: " + box.value.slice(-80));
  };
  rec.onerror = (ev) => {
    vlog("onerror", { error: ev.error, message: ev.message || "", sawResult });
    if (fellBack) return;
    if (ev.error === "network" || ev.error === "service-not-allowed") {
      fellBack = true;
      live.keep = false;
      try {
        rec.stop();
      } catch (e) {}
      setTimeout(() => {
        startLocal(btn, lang, box, box.value).catch((e) => {
          vlog("fallback-throw", { err: String(e) });
          setStatus("fallback failed · type the answer");
        });
      }, 50);
      return;
    }
    setStatus("voice: " + ev.error + " · see console [baseline-voice]");
    if (ev.error === "not-allowed") stopLive(ev.error);
  };
  rec.onend = () => {
    vlog("onend", { sawResult, fellBack, keep: !!(live && live.keep && live.rec === rec) });
    if (fellBack) return;
    if (live && live.rec === rec) {
      live = null;
      clearLiveUi();
      if (sawResult) save("open");
      else setStatus("Chrome speech ended with no words (often network). Click Speak to use local model.");
    }
  };
  vlog("rec.start", { lang: rec.lang, continuous: rec.continuous, micHeld: false });
  rec.start();
  armUi(btn, box);
}

async function startLive(btn) {
  const lang = btn.getAttribute("data-lang");
  const box = btn.closest(".lang").querySelector("textarea");
  seq += 1;
  vlog("click", { lang, SpeechAPI: !!SpeechAPI, MediaRecorder: typeof MediaRecorder });
  if (live && live.btn === btn) {
    stopLive("toggle");
    return;
  }
  stopLive("replace");
  setStatus("asking microphone…");
  try {
    await startLocal(btn, lang, box, box.value);
  } catch (e) {
    vlog("startLocal-throw", { err: String(e) });
    setStatus("record failed: " + e);
  }
}

async function testMic() {
  if (micTest) {
    vlog("mic-test-stop", {});
    micTest.keep = false;
    stopTracks(micTest.stream);
    if (micTest.raf) cancelAnimationFrame(micTest.raf);
    try {
      micTest.ctx && micTest.ctx.close();
    } catch (e) {}
    micTest = null;
    document.getElementById("test-mic").textContent = "Test mic";
    setMeter(0);
    setStatus("mic test stopped");
    return;
  }
  stopLive("mic-test");
  setStatus("test mic: allow, then speak — bar should jump. 4s then playback.");
  let stream;
  try {
    stream = await openMic();
  } catch (e) {
    setStatus("mic blocked. Allow microphone for 127.0.0.1.");
    return;
  }
  const ctx = new AudioContext();
  if (ctx.state === "suspended") await ctx.resume();
  const src = ctx.createMediaStreamSource(stream);
  const analyser = ctx.createAnalyser();
  analyser.fftSize = 2048;
  src.connect(analyser);
  const wave = new Uint8Array(analyser.fftSize);
  const chunks = [];
  const mime = MediaRecorder.isTypeSupported("audio/webm;codecs=opus") ? "audio/webm;codecs=opus" : "";
  const recorder = mime ? new MediaRecorder(stream, { mimeType: mime }) : new MediaRecorder(stream);
  recorder.ondataavailable = (ev) => {
    if (ev.data && ev.data.size) chunks.push(ev.data);
  };
  recorder.start(200);
  const btn = document.getElementById("test-mic");
  btn.textContent = "Stop test";
  micTest = { keep: true, stream, ctx, raf: 0 };
  const t0 = Date.now();
  let peak = 0;
  let lastLog = 0;
  function tick() {
    if (!micTest || !micTest.keep) return;
    analyser.getByteTimeDomainData(wave);
    let sum = 0;
    for (let i = 0; i < wave.length; i++) {
      const v = (wave[i] - 128) / 128;
      sum += v * v;
    }
    const rms = Math.sqrt(sum / wave.length);
    if (rms > peak) peak = rms;
    setMeter(rms);
    if (Date.now() - lastLog > 400) {
      vlog("mic-test-level", { rms, peak, ms: Date.now() - t0 });
      lastLog = Date.now();
    }
    micTest.raf = requestAnimationFrame(tick);
  }
  tick();
  await new Promise((r) => setTimeout(r, 4000));
  if (!micTest || !micTest.keep) return;
  micTest.keep = false;
  if (micTest.raf) cancelAnimationFrame(micTest.raf);
  try {
    if (recorder.state === "recording") recorder.stop();
  } catch (e) {}
  await new Promise((r) => {
    recorder.onstop = r;
    setTimeout(r, 800);
  });
  const blob = new Blob(chunks, { type: recorder.mimeType || "audio/webm" });
  vlog("mic-test-done", { bytes: blob.size, peak, tracks: stream.getAudioTracks().map((t) => t.label) });
  stopTracks(stream);
  try {
    await ctx.close();
  } catch (e) {}
  micTest = null;
  btn.textContent = "Test mic";
  setMeter(peak);
  if (peak < 0.02 || blob.size < 200) {
    setStatus("mic silent. Chrome site settings → Microphone → 127.0.0.1 Allow. Check the input device.");
    return;
  }
  setStatus("playing you back · peak " + peak.toFixed(2) + " · if you hear yourself, mic is fine");
  const audio = new Audio(URL.createObjectURL(blob));
  try {
    await audio.play();
  } catch (e) {
    vlog("mic-test-play-fail", { err: String(e) });
    setStatus("recorded (peak " + peak.toFixed(2) + ") but playback blocked · mic still got signal");
  }
}

try {
  const cached = JSON.parse(localStorage.getItem(KEY) || "{}");
  restore(cached);
  const old = JSON.parse(localStorage.getItem("baseline-2026-09-02") || "{}");
  areas.forEach((el) => {
    const id = el.getAttribute("data-id");
    const box = el.querySelector('textarea[data-lang="en"]');
    if (box && !box.value && typeof old[id] === "string") box.value = old[id];
  });
} catch (e) {}

areas.forEach((el) => {
  el.querySelectorAll("textarea").forEach((box) => {
    box.addEventListener("input", () => {
      if (box.classList.contains("listening")) return;
      clearTimeout(saveTimer);
      saveTimer = setTimeout(() => save("open"), 1200);
    });
  });
});
document.getElementById("save").onclick = () => save("open");
document.getElementById("done").onclick = () => save("done");
document.getElementById("dl").onclick = () => {
  const data = collect();
  localStorage.setItem(KEY, JSON.stringify(data));
  const blob = new Blob(
    [JSON.stringify({ schema: "learn/baseline-answers", langs: LANGS, answers: data }, null, 2)],
    { type: "application/json" }
  );
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "baseline-answers.json";
  a.click();
};
document.getElementById("test-mic").onclick = () => testMic();
document.querySelectorAll("button.mic").forEach((btn) => {
  btn.addEventListener("click", () => startLive(btn));
});
vlog("boot", { probes: PROBES.length, langs: LANGS, speech: !!SpeechAPI });
setStatus("idle · Speak asks mic, then Chrome speech; network error falls back to local whisper");
