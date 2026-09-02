# loop-slash · 全平台发布表单（复制即贴）

成片目录：`tmp/loop-slash/`
口播：德语 `de-DE-KatjaNeural` +38% · 画面烧录 DE（金）+ EN（青）字幕
AI 声明：口播与幻灯均为合成，各平台勾选「AI 生成」类开关。

渲染后先打开成片目录 `chapters.txt`，把时间轴覆盖到 YouTube / B 站简介里。Kit 在 `skills/loop-slash/`（PUBLISH.md、diagrams、render.py）。`tmp/ttl.toon.md` 记 last_run。五天后 janitor `--ttl` 清掉 tmp 里除 ttl 以外的文件。

---

## 0. 传哪个文件

| 文件 | 用途 |
| --- | --- |
| `loop-slash.mp4` | 横屏 16:9 全程 · YouTube 长视频、B 站投稿、LinkedIn、Facebook、X、Reddit、西瓜/头条横屏、Vimeo、Rumble |
| `loop-slash.9x16.mp4` | 竖屏 9:16 全程 · 抖音、快手、视频号、小红书、TikTok、B 站 Story、微博、知乎 |
| `loop-slash.hook.9x16.mp4` | 竖屏 ≤60 秒钩子 · YouTube Shorts、Reels 推荐流、Facebook Reels、Spotlight、Pinterest、Lemon8、Threads |
| `cover.16x9.png` | 横屏封面 |
| `cover.9x16.png` | 竖屏封面 |
| `cover.3x4.png` | 小红书封面 |
| `loop-slash.de-en.srt` | 有外挂字幕栏的平台（YouTube、B 站） |

不要把 9 分钟全程传到 Shorts / Reels 推荐架。钩子片末加评论：「全程在简介置顶」。

---

## 1. 母版文案（先复制这一份，下面各站是裁切版）

### 标题 DE

```
Slash Loop — der Wächter, nicht das Hörbuch
```

### 标题 EN

```
Slash Loop: stop hitting Enter. Hire a night watch for your agent.
```

### 标题 ZH

```
别再通宵按 Enter 了：Slash Loop 才是 Agent 的夜班门卫
```

### 简介 DE

```
Niemand sitzt fünf Stunden im Terminal und drückt Enter, nur damit der Agent denselben PR nochmal anschaut. Das ist kein Job. Das ist ein Wachdienst.

Slash Loop ist der Wecker am Handgelenk des Türstehers. Turn-basiert stehst du selbst an der Tür. /loop lässt die Uhr gucken. /schedule schickt dieselbe Uhr in die Cloud.

In diesem Talk:
• Vier Hebel: Turn, Goal, Loop, Schedule
• Inneres Agent-Loop (Herzschlag) vs. äußeres /loop (Wecker)
• Claude Code, Cursor lokal (PowerShell-Sentinel), Cursor Cloud
• Loop-Spezifikation (arXiv 2607.00038) und 217 Loops in Open Source (2608.21884)
• Labor: Parser aus Claude Code 2.1.71 gegen die Docs von 2026. Zwei Welten, ein Befehl.

Deutsch gesprochen, DE+EN Untertitel. Messung vor Mythos.

Kapitel: siehe die Zeitstempel oben.
```

### 简介 EN

```
Nobody sits five hours in a terminal hitting Enter so the agent re-checks the same PR. That is not a job. That is night watch.

Slash loop is the watch on the bouncer's wrist. Turn-based, you stand at the door. /loop lets the clock look. /schedule sends the same clock to the cloud.

This talk covers:
• Four levers: turn, goal, loop, schedule
• Inner agent loop (heartbeat) vs outer /loop (alarm)
• Claude Code, Cursor local (PowerShell sentinel), Cursor Cloud
• Loop specification (arXiv 2607.00038) and 217 loops mined in open source (2608.21884)
• Lab: parser from Claude Code 2.1.71 vs 2026 docs. Same command. Two worlds.

Spoken German, burnt-in DE+EN subs. Measure first. Then dance.

Chapters: timestamps at the top.
```

### 简介 ZH

```
没有人会在终端里坐五个小时狂按 Enter，就为了让 Agent 再看一遍同一个 PR。那不是工作，那是夜班门卫。

Slash Loop 是门卫手腕上的表。Turn 模式：你自己站门口。/loop：表替你看。/schedule：同一块表，接到云上。

这一讲：
• 四种杠杆：Turn / Goal / Loop / Schedule
• 内层 Agent Loop（心跳）vs 外层 /loop（闹钟）
• Claude Code、Cursor 本地 PowerShell 哨兵、Cursor Cloud
• 循环规格 arXiv 2607.00038；开源里确认过的 217 个自治循环 2608.21884
• 实验室：用 Claude Code 2.1.71 的解析器对 2026 文档。同一条命令，两个世界。

德语口播，画面烧录德英字幕。先测量，再跳舞。
```

### 标签母版

```
SlashLoop, ClaudeCode, Cursor, AgentLoop, PromptEngineering, AIAgents, DevTools, Anthropic, LLMOps, GermanTech
```

### 话题母版 ZH

```
#SlashLoop #ClaudeCode #Cursor #AIAgent #编程 #人工智能 #开发者 #AgentLoop
```

### 首评 / 置顶（各站通用，按语言贴一条）

ZH:

```
全程竖屏在本账号，横屏长版也在。别把 7 分钟切片当 Shorts 传。想复现：Parser 别信推文，信版本号。7m 有 4 分钟空隙，30s 会被 ceil 成 1 分钟。Cursor 哨兵：先 Sleep 再 Echo，正则必须带 ^。
```

EN:

```
Full cut on this account (landscape + portrait). Do not upload the 9 min file as a Short. Reproduce: trust the version, not the tweet. 7m wraps with a 4 min gap. 30s ceils to 1 minute. Cursor sentinel: sleep before echo, caret required.
```

DE:

```
Die ganze Cut ist hier (Quer + Hoch). Nicht die 9-Minuten-Datei als Short hochladen. Messen: Version lesen, nicht den Tweet. 7m hinkt über die Stunde. 30s wird zur Minute. Cursor: Sleep vor Echo, Dach-Regex.
```

---

## 2. 中国大陆

### 抖音

- 文件：`loop-slash.9x16.mp4`
- 封面：`cover.9x16.png`
- 勾选：内容由 AI 生成

标题（前 55 字）：

```
别再通宵按Enter了：Slash Loop才是Agent夜班门卫，4种循环+实测打脸谣言
```

正文：

```
没人会在终端里坐五个小时按 Enter，就为了让 Agent 再看一遍同一个 PR。那不是工作，那是夜班门卫。Slash Loop 是他手腕上的表。

这一讲把 Turn / Goal / Loop / Schedule 四根杠杆拆开，再把「内层心跳」和「外层闹钟」分开。Claude Code、Cursor 本地 PowerShell 哨兵、Cursor Cloud 对照着讲。

实验室部分：Claude Code 2.1.71 解析器对 2026 文档。同一条 /loop check the deploy，一边是固定 10 分钟，一边是 1 分钟到 1 小时动态。7m 跨小时会短一截。30s 会被 ceil 成 1 分钟。先测量，再跳舞。

德语口播，画面德英字幕。#SlashLoop #ClaudeCode #Cursor #AIAgent #编程
```

话题（≤5）：

```
#SlashLoop #ClaudeCode #Cursor #AIAgent #编程
```

后台：允许下载关 · 允许杜特/跟拍开 · 谁可以看=公开 · 位置不填或填 Berlin · 首评贴「首评 ZH」

---

### 快手

- 文件：`loop-slash.9x16.mp4`
- 封面：`cover.9x16.png`

标题（≤50 字）：

```
别再通宵按Enter：Slash Loop当夜班门卫，4种Agent循环讲清楚
```

作品描述：

```
Agent 循环不是把论文摘要读出来。你雇一个门卫，不是自己通宵盯门。Turn 你站门口，/loop 是腕表，/schedule 把表接到云上。实验室打脸：7m 有 4 分钟空隙，30s 不是 30 秒。德语口播+德英字幕。
```

话题（≤4）：

```
#人工智能 #编程 #Claude #Cursor
```

---

### 微信视频号

- 文件：`loop-slash.9x16.mp4`
- 封面：`cover.9x16.png`

描述（≤60 字展示，可更长）：

```
别再通宵按 Enter 盯 Agent。Slash Loop 是夜班门卫手腕上的表。四种循环 + 实测谣言。德语口播，德英字幕。#AIAgent #编程 #Claude
```

位置：原创 · 公开 · 声明 AI 生成（若有该开关）

---

### 小红书

- 文件：`loop-slash.9x16.mp4`
- 封面：`cover.3x4.png`（标题硬上限 20 字）

标题：

```
别再通宵按Enter盯PR
```

正文：

```
没有人会在终端坐五个小时狂按 Enter，只为让 Agent 再看同一条 PR。那不是工作，是夜班门卫。

Slash Loop 是门卫手腕上的表。
Turn：你自己站门口。
/loop：表替你看。
/schedule：同一块表，接到云上。

容易混的一点：内层 Agent Loop 是心跳（prompt → tool → 结果，直到模型空手说话）。外层 /loop 是闹钟（每隔 N 分钟同一份差事再来一遍）。一个心跳不是 Slash Loop。

实验室（本机跑过）：
· /loop check the deploy：2.1.71 固定 10 分钟；2026 文档改成 1 分钟–1 小时动态
· 30s 会被 ceil 成 1 分钟，cron 没有秒
· 7m 跨小时那一格只有 4 分钟
· Cursor 哨兵必须 Sleep 再 Echo，正则带 ^，否则会双响

德语口播，画面德英字幕。先测量，再跳舞。

#SlashLoop #ClaudeCode #Cursor #AIAgent #编程 #开发者 #人工智能 #Agent
```

标签（≤10，已写在正文末）

---

### 哔哩哔哩 · 投稿（横屏）

- 文件：`loop-slash.mp4`
- 封面：`cover.16x9.png`
- 字幕：上传 `loop-slash.de-en.srt`（类型：字幕稿 / 软字幕）
- 分区：科技 → 计算机技术（或极客）
- 类型：自制
- 标签（≤10，每个≤20 字）：`Claude` `Cursor` `AIAgent` `编程` `人工智能` `开发工具` `LLM` `SlashLoop` `Prompt` `德语`

标题：

```
Slash Loop：别再当 Agent 的夜班门卫【4种循环+实测谣言】
```

简介（前两行会被折叠，先放钩子；章节从 `chapters.txt` 粘到最上面）：

```
没人会在终端坐五个小时按 Enter，就为了让 Agent 再看同一条 PR。Slash Loop 是门卫手腕上的表。

【这一讲】
Turn / Goal / Loop / Schedule 四根杠杆
内层心跳 vs 外层闹钟
Claude Code · Cursor 本地 PowerShell 哨兵 · Cursor Cloud
arXiv 2607.00038 循环规格 · 2608.21884 开源 217 个自治循环
实验室：Claude Code 2.1.71 解析器 vs 2026 文档

德语口播，画面烧录德英字幕。测量先于神话。

来源：Claude Blog Getting started with loops · Docs Commands / Scheduled Tasks · Cursor SKILL loop
```

活动/专栏：不参加 · 开启弹幕 · 关闭充电直到你确认版权 · 声明 AI 生成（若有）

---

### 哔哩哔哩 · 竖屏 Story

- 文件：`loop-slash.9x16.mp4`
- 封面：`cover.9x16.png`
- 网页端若弹出「是否发布为竖屏」：选是

标题：

```
别再通宵按 Enter，Slash Loop 才是夜班门卫
```

---

### 微博

- 文件：`loop-slash.9x16.mp4`

正文：

```
别再通宵按 Enter 盯 Agent 了。Slash Loop 是夜班门卫手腕上的表：Turn 你站门口，/loop 表替你看，/schedule 把表接到云上。实验室打脸：7m 跨小时会短一截，30s 不是 30 秒。德语口播+德英字幕。#SlashLoop# #ClaudeCode# #人工智能#
```

---

### 西瓜视频 / 今日头条

- 文件：`loop-slash.mp4`（西瓜横屏）或 `loop-slash.9x16.mp4`（头条中视频优先竖屏）
- 封面：对应画幅
- 分类：科技 / 互联网

标题：

```
Slash Loop：别再当 Agent 的夜班门卫，四种循环一次讲清
```

正文：用「简介 ZH」。声明原创。同步到头条号（若绑定）。

---

### 知乎视频

- 文件：`loop-slash.9x16.mp4` 或横屏 `loop-slash.mp4`
- 话题：人工智能、编程、Claude、Cursor

标题：

```
Slash Loop 不是把论文读给你听：四种 Agent 循环 + 一次解析器实测
```

想法/回答导语：用「简介 ZH」。

---

### 百家号 · 企鹅号 · 搜狐号 · 网易号

四个后台字段几乎一样。

标题：

```
Slash Loop：别再通宵按 Enter，给 Agent 雇一个夜班门卫
```

导语：

```
Turn、Goal、Loop、Schedule 四根杠杆，内层心跳和外层闹钟不是一回事。Claude Code 2.1.71 解析器对 2026 文档：同一条命令，两个世界。
```

正文：用「简介 ZH」+ 来源列表。分类：科技。原发声明。封面横屏用 `cover.16x9.png`。

---

### AcFun

- 文件：`loop-slash.mp4`
- 分区：科技 · 文章标签 `AI` `编程`

标题：

```
Slash Loop：夜班门卫，不是有声书【Claude / Cursor 循环实测】
```

简介：用「简介 ZH」。

---

### 豆瓣

- 文件通常只能贴链接。发广播：

```
做了一条关于 Slash Loop 的德语技术口播（德英字幕）：别再通宵按 Enter 给 Agent 守夜。四种循环 + 解析器实测。长版见 B 站 / YouTube。
```

---

## 3. 全球主流

### YouTube · 长视频

- 文件：`loop-slash.mp4`
- 封面：`cover.16x9.png`
- 字幕：上传 `loop-slash.de-en.srt`，语言 German + English
- 语言：German (Germany)
- 字幕烧录：已在画面里，软字幕仍传（无障碍 + 翻译）
- 类别：Science & Technology
- 观众：No, it's not made for kids
- 改动内容：Yes, altered / AI generated
- 评论：On · 可见性 Public
- 获利：先关，版权清完再开
- 投放：先不要付费

标题（≤100）：

```
Slash Loop — der Wächter, nicht das Hörbuch | Claude Code /loop vs Cursor
```

描述（先贴 `chapters.txt` 全文，再贴下面）：

```
Niemand sitzt fünf Stunden im Terminal und drückt Enter. Slash Loop ist der Wecker am Handgelenk des Türstehers.

Four levers: Turn · Goal · Loop · Schedule
Heartbeat (inner agent loop) ≠ alarm (slash loop)
Claude Code · Cursor local PowerShell sentinel · Cursor Cloud
arXiv 2607.00038 loop specification · 2608.21884 (217 autonomous loops)
Lab: Claude Code 2.1.71 parser vs 2026 docs. Same command. Two worlds.

Spoken German. Burnt-in DE+EN subs.

Sources:
• Claude blog: Getting started with loops
• Claude docs: Commands, Scheduled Tasks
• Cursor SKILL loop
• arXiv 2607.00038, 2608.21884

#SlashLoop #ClaudeCode #Cursor #AIAgents #LLMOps
```

Tags（最多 500 字符）：

```
slash loop, claude code, cursor ide, ai agents, agent loop, prompt engineering, anthropic, llmops, scheduled tasks, powershell, german, deutsch, coding, developer tools
```

End screen：订阅 + 本片章节。卡片：无。

---

### YouTube Shorts

- 文件：`loop-slash.hook.9x16.mp4`（必须 ≤60s/≤180s 视账号，本钩子按 ≤59.9s 切）
- 封面：`cover.9x16.png`

标题：

```
Stop hitting Enter. Hire a night watch. #Shorts
```

描述：

```
Slash Loop is the watch on the bouncer's wrist. Full German talk on the channel (DE+EN subs). #SlashLoop #ClaudeCode #Cursor #AIAgents #Shorts
```

---

### TikTok

- 文件：`loop-slash.9x16.mp4`（网页 TikTok Studio 上传，避免手机 287 MB 上限）
- 封面：`cover.9x16.png`
- 勾选：AI-generated content
- 允许评论 / 允许 Stitch / 允许 Duet：开
- 谁可以看：Everyone

字幕栏（钩子在前）：

```
Nobody sits 5 hours hitting Enter so the agent re-checks the same PR. Slash loop is the night watch.

Four levers. Heartbeat ≠ alarm. Claude Code vs Cursor. We ran the 2.1.71 parser against the 2026 docs.

German audio, DE+EN subs. Full sources in bio.

#ai #claude #cursor #coding #developer #llm #anthropic #tech #learnontiktok #programming
```

---

### Instagram Reels（推荐流）

- 文件：`loop-slash.hook.9x16.mp4`
- 封面：`cover.9x16.png`
- 分享到 Feed：开 · 分享到 Facebook：按你号

说明：

```
Stop hitting Enter. Hire a night watch for your agent.

Slash loop = the watch on the bouncer’s wrist. Full talk (DE audio, DE+EN subs) on YouTube / TikTok.

#ai #claude #cursor #coding #developer #tech #programming #llm
```

位置：Berlin（可选）· 改动内容：AI 生成

---

### Instagram 帖子 / 长视频

- 文件：`loop-slash.9x16.mp4`（Feed 可长，推荐会弱）
- 说明：用上面 Reels 文案，去掉时长暗示，补一句 “full ~10 min”

---

### Facebook 视频

- 文件：`loop-slash.mp4`
- 标题：`Slash Loop: hire a night watch for your agent`
- 说明：用「简介 EN」
- 观众：Public · 不是儿童内容

### Facebook Reels

- 文件：`loop-slash.hook.9x16.mp4`
- 说明：同 Instagram Reels

---

### X (Twitter)

- 文件：优先 `loop-slash.hook.9x16.mp4`（帖内视频更吃完播）；长版只发链接
- 帖文（≤280，下面 277 字）：

```
Nobody sits 5h hitting Enter so the agent re-checks the same PR. Slash loop is the night watch.

Heartbeat ≠ alarm. We ran Claude Code 2.1.71’s parser vs 2026 docs. Same command. Two worlds.

German audio, DE+EN subs.
```

---

### LinkedIn

- 文件：`loop-slash.mp4`（信息流更吃横屏；9:16 会被裁）
- 分类：Professional · 谁可以看：Anyone
- 改动内容：AI generated（若有）

文案：

```
You are not the night watch. You hire one.

Turn-based agents still need you at the door. /loop is the watch on the bouncer’s wrist. /schedule sends that watch to the cloud.

I walked the four levers (turn, goal, loop, schedule), split the inner heartbeat from the outer alarm, and ran the Claude Code 2.1.71 parser against the 2026 docs. Same command. Two worlds. 7m wraps with a 4-minute gap. 30s is not 30 seconds.

Spoken German, burnt-in DE+EN subtitles. Measure first.

#AIAgents #ClaudeCode #Cursor #LLMOps #SoftwareEngineering
```

---

### Threads

- 文件：`loop-slash.hook.9x16.mp4`

```
Stop hitting Enter. Hire a night watch. Slash loop = wristwatch for your agent. Full German talk (DE+EN subs) on YT/TikTok.
```

---

### Reddit

发帖，不要只丢视频无正文。建议：

- r/ClaudeAI · r/cursor · r/LocalLLaMA · r/programming · r/MachineLearning（后者更挑质量）

Title：

```
Slash Loop is not the inner agent loop: we ran Claude Code 2.1.71’s parser against the 2026 docs
```

Body：

```
German presentation (DE+EN subs) on hiring a night watch instead of sitting in the terminal.

Main claims, all measured or cited:
- Inner heartbeat (prompt/tool/result until no tools) ≠ outer /loop (same job every N minutes)
- 2.1.71 default for ` /loop check the deploy ` is a fixed 10m; current docs say dynamic 1m–1h (except Bedrock/Foundry)
- `30s` ceils to 1 minute (cron has no seconds)
- `*/7` wraps the hour with a 4-minute gap
- Cursor local: sleep then echo, caret regex; echo-before-sleep + run-now double-ticks

Video: <PASTE URL AFTER UPLOAD>
Sources in the description: arXiv 2607.00038, 2608.21884, Claude docs, Cursor SKILL loop.
```

Flair：Video / Resource。遵守各板自宣规则，必要时标 OC。

---

### Snapchat Spotlight

- 文件：`loop-slash.hook.9x16.mp4`
- 标题：`Hire a night watch`

---

### Pinterest Idea Pin

- 文件：`loop-slash.hook.9x16.mp4`
- 标题：`Slash Loop: agent night watch`
- 描述：用「简介 EN」前两句 + `#AI #Coding #Claude #Cursor`
- 画板：AI / Developer tools

---

### VK

- 文件：`loop-slash.mp4` 或 `loop-slash.9x16.mp4`
- 标题：`Slash Loop — night watch for your agent (DE+EN)`
- 描述：用「简介 EN」

---

### Dailymotion

- 文件：`loop-slash.mp4`
- 频道分类：Tech
- 标题 / 描述：同 YouTube 长视频（无章节也行）
- 语言：German
- 标签：`ai, claude, cursor, programming, deutsch`

---

### Rumble

- 文件：`loop-slash.mp4`
- 类别：Science & Technology
- 标题 / 描述：同 YouTube EN 标题 + 简介 EN
- 年龄：Everyone

---

### Vimeo

- 文件：`loop-slash.mp4`
- 隐私：Public 或 Hide from vimeo.com（若只当母带）
- 标题：YouTube DE 标题
- 描述：简介 EN
- 语言：German
- 内容分级：Safe

---

### Odysee

- 文件：`loop-slash.mp4`
- 标题 / 描述 / 标签：同 YouTube 长视频
- 频道语言：de

---

### Bluesky

```
Nobody sits 5 hours hitting Enter so the agent re-checks the same PR. Slash loop is the night watch.

Heartbeat ≠ alarm. Parser 2.1.71 vs 2026 docs. German audio, DE+EN subs.
<URL>
```

---

### Mastodon

内容警告：不必。语言 `de`。

```
Slash Loop — der Wächter, nicht das Hörbuch.

Turn = du stehst an der Tür. /loop = die Uhr am Handgelenk. Messung: Parser 2.1.71 gegen Docs 2026.

Deutsch gesprochen, DE+EN Untertitel.
<URL>

#ClaudeCode #Cursor #AIAgents #Fediverse
```

---

### Lemon8

- 文件：`loop-slash.hook.9x16.mp4`
- 标题：`Stop being your agent’s night watch`
- 正文：Instagram Reels 说明

---

### Tumblr

```
Slash Loop: hire a night watch, stop hitting Enter. German talk, DE+EN subs. Full cut: <URL>
#ai #coding #claude #cursor
```

---

## 4. 统一后台选项（各站能勾就勾）

- 公开 / Public
- 允许评论
- 关闭「作品允许他人下载」（抖音/快手）除非你想开
- 声明 AI 生成 / Altered content
- 不是儿童内容 / Not made for kids
- 关闭付费推广直到你看完首日数据
- 首评贴第 1 节「首评」对应语言
- 上传完成后把 URL 回写到 `skills/video-generation.fu.md` 的 `ARCHIVE_URL`
- 全部满意后再：`python skills/loop-slash/render.py --cleanup --confirmed-uploaded`

## 5. 上传顺序（减少重复劳动）

1. YouTube 长视频（拿稳定 URL，供 Reddit / X / Bluesky / Mastodon / 豆瓣引用）
2. B 站横屏投稿（国内引用）
3. 抖音 + TikTok + 快手 + 视频号 + 小红书（竖屏全程）
4. Shorts / Reels / Spotlight / Lemon8 / Threads（钩子）
5. LinkedIn / Facebook / 西瓜 / 知乎 / 其余长尾
6. 把所有 URL 贴进 `ARCHIVE_URL`（可多行）
