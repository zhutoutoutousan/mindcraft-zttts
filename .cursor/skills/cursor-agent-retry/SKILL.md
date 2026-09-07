---
name: cursor-agent-retry
description: Diagnoses Cursor Agent stream drops (Agent stopped retrying, Connection failed, HTTP/2 vs HTTP/1.1, Clash TUN, proxySupport override) and Agent-side load rules that amplify drops (huge parallel tool batches, GenerateImage storms). Rebuilds tmp/cursor-agent-retry.pdf and the Bilibili/LinkedIn summary MP4 with PlantUML. Use when the human names Agent stopped retrying, 连接中断, Connection failed, HTTP Compatibility Mode, Clash/Mihomo/v2rayN TUN, 土方法, CSDN 代理, retry bug, or asks for a Cursor network PDF or retry prevention video.
---

# Cursor Agent stream drop

This error is a **client stream drop before progress is saved**, not a server abort. Retry continues from the last saved state. Full folk-method table and sources: [reference.md](reference.md). Rebuild the card with [template.tex](template.tex). Publish summary video kit: [video/](video/).

`tmp/` expires in 5 days. Lasting notes stay in this skill, not in CPU.md.

Two halves: **network ladder** (human settings) and **Agent-side load** (what this agent must not do). Fixing only Clash while still firing 7× image APIs in one turn will keep dropping.

## Rebuild PDF

Copy [template.tex](template.tex) to `tmp/cursor-agent-retry.tex`, then:

```
python .cursor/skills/daily-brief/scripts/compile.py tmp/cursor-agent-retry.tex
```

Body language is **Chinese**. Do not invent a working proxy port. Do not paste private Clash nodes, PAC URLs, or credentials into the PDF or this skill. Regenerate PDF only when the human asks.

## Rebuild summary MP4 (Bilibili + LinkedIn)

Kit: [video/make_memes.py](video/make_memes.py), [video/build_mp4.py](video/build_mp4.py), [video/diagrams/*.puml](video/diagrams/), [video/PUBLISH.md](video/PUBLISH.md).

```
python .cursor/skills/cursor-agent-retry/video/make_memes.py
python .cursor/skills/cursor-agent-retry/video/build_mp4.py
python cron/janitor.py --touch
```

- Spoken German `de-DE-KatjaNeural` +38%; burnt-in DE+ZH; 16:9 master → `tmp/cursor-agent-retry-video/cursor-retry.mp4`
- PlantUML via Kroki with dark contrast skin (same family as `skills/video-generation.fu.md`)
- Local PIL memes only; Mixkit b-roll muted (reuse fog-kit CDN copies when present)
- Obey Agent-side load below while building (no GenerateImage storms)

## Agent-side load (controllable here)

When the human already names retry / 连接中断 / fog, or a prior turn in this chat was interrupted: default to **small turns**.

| Rule | Do | Do not |
|---|---|---|
| Tools per turn | ≤3–4 independent tools | One megabatch of 6+ long network tools |
| Images | Local script / PIL first (`make_memes.py`) | Default `GenerateImage` storms; max **2** GenerateImage only if human asked |
| Web | Known CDN URL + Shell download; ≤2 `WebFetch` | Parallel scrape of many HTML gallery pages to hunt clips |
| Heavy jobs | Write scripts/assets first turn; encode/compile **next** turn | Stack XeLaTeX + full mp4 encode + multi-Fetch in one turn |
| After interrupt | Inventory on-disk `_memes/` `_broll/` `_audio/` / partial files; resume missing steps only | Replay the exact failed megabatch |
| Retry UI | Click **Retry** | Open a new chat unless the session itself is corrupt |

Evidence (this repo, 2026-09-06 partner cut): a turn with 7×`GenerateImage` + multi-`WebFetch` was interrupted twice; local PIL + Mixkit CDN finished in one short shell chain.

Cross-link: playful video kit obeys the same hard rules in `skills/video-generation.fu.md`. Fog weeks: `.cursor/skills/fog-rest/SKILL.md` Load rule skips long media batches unless named.

## Ladder (Windows standalone first)

Do in order. After any Network or `settings.json` change: **kill every `Cursor.exe`**, then relaunch. Reload Window is not enough.

1. **Cursor Settings → Network → Run Diagnostics.** Keep the output.
2. **HTTP Compatibility Mode → HTTP/1.1** (same as `cursor.general.disableHttp2: true`). If it still drops after a full quit, try **HTTP/1.0**.
3. **Hotspot 对照.** If Agent holds on phone data and dies on LAN/VPN, the current path is the fault.
4. Align proxy + HTTP mode with the VS Code Cursor extension. They are two apps.
5. If Clash/Mihomo/v2rayN is on: **规则模式 + mixed/HTTP 端口** into `http.proxy`. Do not mix SOCKS port. Prefer **no TUN / no 系统全局** unless IDE settings never see the proxy.
6. `http.proxySupport` default `override` + empty `http.proxy` = 裸连. Either fill `http.proxy` or switch Support to `on` / `fallback`.
7. DNS `1.1.1.1` or `8.8.8.8` if diagnostics show SSL handshake / bad edge.
8. Click **Retry** rather than opening a new chat unless the session itself is corrupt.

## Do not lead with

These were tried for *Agent stopped retrying* and did not fix the standalone app: clear `workspaceStorage`, `.cursorignore`, disable hardware acceleration. They fix other bugs (stuck terminal, laggy index).

Do not recommend `cursor.general.disableHttp1SSE: true` as a first step. Official fallback **is** HTTP/1.1 SSE. That CSDN/博客园 key is cargo-cult.

`http.proxyStrictSSL: false` and `--ignore-certificate-errors` are last-resort MITM bypasses, not defaults.

## settings.json skeleton

Port is an example. Read the local mixed/HTTP port from the proxy app.

```json
{
  "http.proxy": "http://127.0.0.1:7890",
  "https.proxy": "http://127.0.0.1:7890",
  "http.proxySupport": "override",
  "http.proxyStrictSSL": false,
  "cursor.general.disableHttp2": true
}
```

CLI equivalent: `%USERPROFILE%/.cursor/cli-config.json` → `"network": { "useHttp1ForAgent": true }`.

## Write-back

New generic evidence → [reference.md](reference.md) and regenerate the PDF if asked. Video script / PlantUML changes → [video/](video/) then rebuild MP4 if asked. Do not log a person's proxy host into the skill.
