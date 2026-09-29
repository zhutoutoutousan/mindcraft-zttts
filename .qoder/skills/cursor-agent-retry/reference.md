# Sources and folk methods

Official meaning of *Agent stopped retrying*: the Agent stream to Cursor dropped before progress was saved. Retry resumes last saved state. Staff diagnosis: client went quiet on the path to the servers, not a server abort.

## Official / staff

| Source | Claim |
|---|---|
| [forum 169376/5](https://forum.cursor.com/t/bug-agent-stopped-retrying-repeatedly-on-windows-standalone-desktop-app/169376/5) | Drop is on the network path. Standalone app and VS Code extension have separate proxy/HTTP settings. Diagnostics + hotspot. |
| [forum 170410](https://forum.cursor.com/t/why-has-cursor-been-reporting-errors-these-past-few-days-for-b2c1d4e1-2230-4c7a-b698-37726c70f7b/170410) | HTTP/1.0 (short requests) + VPN node switch cleared repeated drops. Staff: avoid HTTP/1.0 unless 1.1 still dies. |
| [Network troubleshooting](https://cursor.com/help/troubleshooting/network) | Diagnostics; HTTP/1.1 for proxies that block HTTP/2; full restart after VPN DNS. JA: [ネットワーク](https://cursor.com/ja/help/troubleshooting/network). |
| [Enterprise network](https://cursor.com/docs/enterprise/network-configuration) | HTTP/2 bidi default; auto-fallback to HTTP/1.1 SSE; proxies must not buffer SSE; allow `*.cursor.sh`, `*.cursor-cdn.com`, `*.cursorapi.com`. |
| [forum 164455](https://forum.cursor.com/t/cursor-agent-fails-with-connecterror-unavailable/164455) | From 3.9.16 Agent uses a separate HTTP/2 transport that may ignore proxy; HTTP/1.1 path honors `http.proxy`. `--no-proxy-server` tests cached system proxy. |

## Chinese / non-English folk (土方法)

| Source | Method | Grade |
|---|---|---|
| [CSDN 排坑 HTTP Compatibility](https://blog.csdn.net/weixin_41496173/article/details/149153599) | Network → HTTP/1.1. Claims no restart. | **Use HTTP/1.1.** Restart anyway. |
| [DeepSeek 社区 / CSDN 国内模型](https://deepseek.csdn.net/6a2a195a662f9a54cb7cab21.html) | Same HTTP/1.1 switch unlocked models behind 魔法. | Use. |
| [CSDN 内置代理 无需 TUN](https://blog.csdn.net/weixin_66397563/article/details/155617027) · [博客园同文](https://www.cnblogs.com/jzssuanfa/p/19503708) | Clash **规则模式**, fill `http.proxy` mixed/HTTP port, `disableHttp2`, no 全局/TUN. Also `disableHttp1SSE` + `connectionTimeout`. | **Use 规则模式 + HTTP port + disableHttp2.** Do not copy `disableHttp1SSE`. Timeout 30s is optional. |
| [掘金 锁区 7897](https://juejin.cn/post/7529020018618695730) | IDE proxy only; 海外节点; HK may still geo-block; HTTP/1.1 in Network. | Use; pick a real overseas node. |
| [Easton 中文排查](https://eastondev.com/blog/zh/posts/dev/20260119-cursor-network-fix/) | `proxySupport` default `override` + empty proxy = 裸连 → `on`/`fallback`. DNS 1.1.1.1. Clash `http-version: "1.1"`. Logs `%APPDATA%\Cursor\logs`. Launch `--disable-http2`. | Use in that order. `--ignore-certificate-errors` last. |
| [Easton 企业代理](https://eastondev.com/blog/zh/posts/ai/20260529-cursor-proxy-config/) | `disableHttp2` for Zscaler/Netskope; import corp root; `--disable-http2` wins over settings. | Use. |
| [Clash 开源文](https://clashopen.com/zh-CN/blog/articles/cursor-clash-proxy-ai-ide-2026.html) | TUN for stubborn processes; FakeIP/DoH; long-lived Agent drops = bad node. | TUN only if IDE proxy never takes effect. |
| [少华 Mac 残留代理](https://www.shaohualee.com/article/1049) | Stale system proxy to dead 7897; PAC 直连 `cursor.sh` → geo-block. Force `\|\|cursor.sh` through proxy. | Use when login/region fails. |
| [CSDN Codex/WSL](https://blog.csdn.net/gr6661/article/details/154729056) | WSL NAT cannot see Windows `127.0.0.1` Clash. | Only for Codex-in-WSL, not this toast. |
| [CLI HTTP/1](https://forum.cursor.com/t/agent-feature-unusable-due-to-continuous-reconnecting-and-failed-requests/162009/14) | `cli-config.json` `network.useHttp1ForAgent: true`. | CLI only. |

## Tried and not for this toast

Original Windows report already: kill processes, HTTP/1.1 alone, clear `workspaceStorage`, `.cursorignore`, disable GPU. Bug remained on standalone. Those steps belong to **other** failures (empty terminal, sticky index).

## Port mixups (common 土坑)

| App | Typical mixed/HTTP | Typical SOCKS | Do not put SOCKS in `http.proxy` |
|---|---|---|---|
| Clash / Mihomo | 7890 | 7891 | yes |
| Clash Verge | 7897 | — | check Mixed Port |
| v2rayN / V2Ray | 10809 HTTP | 10808 SOCKS | 10808 in `http.proxy` fails |

## Allowlist if a firewall is in the way

`*.cursor.sh` (incl. `api2.cursor.sh`, `agent.api5.cursor.sh`), `*.cursor-cdn.com`, `*.cursorapi.com`. Disable SSL inspection / SSE buffering on those hosts.

## Agent-side load (amplifies drops)

Network fix alone is not enough when the Agent turn itself is a long parallel storm. Drop = unsaved progress; Retry resumes last disk/chat checkpoint.

| Pattern | Grade | Note |
|---|---|---|
| ≤3–4 tools / turn when retry or fog is named | Use | Default small turn |
| Local PIL / `make_memes.py` for stickers | Use | Partner cut 2026-09-06 |
| Mixkit CDN `assets.mixkit.co/videos/<id>/<id>-720.mp4` via Shell | Use | Mute b-roll |
| ≤2 `WebFetch` or ≤2 `GenerateImage` only if human asked | Cap | Never batch 7 images |
| Encode/compile in a separate turn after scripts land | Use | Do not stack with Fetch storms |
| After interrupt: inventory `_memes/` `_broll/` `_audio/`; resume gaps | Use | Do not replay megabatch |
| Parallel gallery HTML scrape to pick stock clips | Avoid | CDN id first |
| Default `GenerateImage` for every slide | Avoid | Skill: `skills/video-generation.fu.md` |
