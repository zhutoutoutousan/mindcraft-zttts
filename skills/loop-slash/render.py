#!/usr/bin/env python3
"""Presentation cut: faster German, analogies, PlantUML. Not 照本宣读.

    python skills/loop-slash/render.py
    python skills/loop-slash/render.py --force
    python skills/loop-slash/render.py --aspect 9x16
    python skills/loop-slash/render.py --cleanup --confirmed-uploaded

Masters land in tmp/loop-slash/. Kit stays in skills/loop-slash/.
"""
from __future__ import annotations

import argparse
import asyncio
import io
import re
import shutil
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
import zlib
from dataclasses import dataclass
from pathlib import Path

import edge_tts
import imageio_ffmpeg
import matplotlib
import numpy as np
from PIL import Image as PILImage

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def repo_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "ROOT.md").exists():
            return p
    raise SystemExit("ROOT.md not found")


SRC = Path(__file__).resolve().parent
REPO = repo_root(SRC)
WORK = REPO / "tmp" / "loop-slash"
DIAG = SRC / "diagrams"
AUDIO = WORK / "_audio"
SLIDES = WORK / "_slides"
SLIDES_P = WORK / "_slides_9x16"
PUML_PNG = WORK / "_puml"
OUT = WORK / "loop-slash.mp4"
OUT_P = WORK / "loop-slash.9x16.mp4"
OUT_HOOK = WORK / "loop-slash.hook.9x16.mp4"
SRT = WORK / "loop-slash.de-en.srt"
ASS = WORK / "loop-slash.de-en.ass"
ASS_P = WORK / "loop-slash.9x16.de-en.ass"
COVER_L = WORK / "cover.16x9.png"
COVER_P = WORK / "cover.9x16.png"
COVER_34 = WORK / "cover.3x4.png"
CHAPTERS = WORK / "chapters.txt"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
VOICE = "de-DE-KatjaNeural"
RATE = "+38%"
PAUSE = 0.22
W, H, DPI = 1920, 1080, 100
WP, HP = 1080, 1920
HOOK_MIN, HOOK_CAP = 58.0, 59.85

CHAPTER_LABELS = {
    "01": "Hook — you are not the night watch",
    "04": "Four levers",
    "06": "What you actually type",
    "09": "Alarm vs heartbeat",
    "11": "Claude Code vs Cursor",
    "13": "Walkthrough Claude Code",
    "16": "Walkthrough Cursor Windows",
    "18": "SDK heartbeat",
    "19": "Loop specification",
    "22": "How loops die",
    "25": "Hand off one lever",
    "29": "Lab / mythbusters",
    "38": "Close",
}

C_BG = "#0a0e14"
C_DE = "#ffcc80"
C_EN = "#90caf9"
C_ACC = "#69f0ae"
C_LINE = "#2a3544"

# visual: puml filename stem or builtin key
SEGMENTS: list[tuple[str, str, str, str, str]] = [
    (
        "01", "intro", "hook",
        "Okay, ehrlich: niemand bleibt fünf Stunden im Terminal sitzen und drückt Enter, nur damit der Agent nochmal denselben PR anschaut. Das ist kein Job. Das ist ein Wachdienst. Und genau dafür ist Slash Loop da.",
        "Nobody sits five hours in a terminal hitting Enter so the agent re-checks the same PR. That is not a job. That is night watch. Slash loop is the night watch.",
    ),
    (
        "02", "intro", "hook",
        "Stell dir einen Türsteher vor. Turn-basiert bist du der Türsteher. Jede Minute fragst du: noch jemand? Slash Loop ist der Wecker an seinem Handgelenk. Alle fünf Minuten guckt er. Du gehst tanzen.",
        "Picture a bouncer. Turn-based, you are the bouncer. Every minute you ask: anyone else? Slash loop is the watch on his wrist. Every five minutes he looks. You go dancing.",
    ),
    (
        "03", "intro", "types",
        "Anthropic sagt das nüchtern: Loops sind Agenten, die Zyklen wiederholen, bis eine Stoppbedingung greift. Poetisch: du baust eine Maschine, die das Nachhaken für dich übernimmt. Prompt engineering stirbt nicht. Es zieht nur eine Schicht höher.",
        "Anthropic, dry: loops repeat cycles until a stop condition hits. Poetic: you build a machine that nags for you. Prompt engineering does not die. It just moves one layer up.",
    ),
    (
        "04", "core", "types",
        "Vier Hebel. Turn: du hältst den Takt. Goal: der Coach lässt dich nicht aus der Halle, bis Lighthouse neunzig ist. Loop: die Uhr hält den Takt. Schedule: dieselbe Uhr, aber in der Cloud, auch wenn dein Laptop klappt.",
        "Four levers. Turn: you keep time. Goal: the coach will not let you leave until Lighthouse is ninety. Loop: the clock keeps time. Schedule: same clock, in the cloud, even if the laptop folds.",
    ),
    (
        "05", "core", "types",
        "Proaktiv ist, wenn du den ganzen Zettel abgibst. Nicht nur den Wecker. Auch das Rezept, den Coach, und drei Azubis, die parallel kochen. Das ist kein Anfänger-Move. Pilotier das an einem Kanal, nicht an der ganzen Firma.",
        "Proactive is handing over the whole scrap of paper. Not just the alarm. The recipe, the coach, and three apprentices cooking in parallel. Not a beginner move. Pilot one channel, not the whole company.",
    ),
    (
        "06", "core", "syntax",
        "Was tippst du wirklich? Slash Loop, fünf m, Leerzeichen, dann der Satz. Check den Deploy. Punkt. Intervall plus Prompt. Das ist der Wecker mit Ansage. Laptop zu, Wecker tot. Alias übrigens: Slash Proactive.",
        "What do you actually type? Slash loop, five m, space, then the sentence. Check the deploy. Period. Interval plus prompt. Alarm with a voice note. Laptop shut, alarm dead. Alias: slash proactive.",
    ),
    (
        "07", "core", "syntax",
        "Lässt du das Intervall weg, wählt Claude die Pause selbst. Eine Minute bis eine Stunde. Kurz, wenn CI brennt. Lang, wenn die Queue gähnt. Am Ende des Ticks druckt er die Pause und das Warum. Das ist kein Magier. Das ist ein Metronom mit Augen.",
        "Drop the interval and Claude picks the pause. One minute to one hour. Short when CI is on fire. Long when the queue yawns. End of tick, it prints the delay and the why. Not a magician. A metronome with eyes.",
    ),
    (
        "08", "core", "syntax",
        "Nur Slash Loop, gar nichts dahinter? Dann nimmt er loop.md, oder den eingebauten Hausmeister-Prompt. Esc löscht den nächsten Weckruf. Nicht den ganzen Agenten. Nur den nächsten Gong.",
        "Bare slash loop, nothing after it? Then loop.md, or the built-in janitor prompt. Esc kills the next wakeup. Not the whole agent. Just the next gong.",
    ),
    (
        "09", "core", "inner",
        "Pass auf, das verwechselt jeder. Slash Loop ist der Wecker. Das innere Agent-Loop ist der Herzschlag. Wecker: alle fünf Minuten nochmal derselbe Auftrag. Herzschlag: Prompt, Tool, Ergebnis, Tool, bis das Modell ohne Werkzeug antwortet.",
        "Careful, everyone mixes this up. Slash loop is the alarm clock. The inner agent loop is the heartbeat. Alarm: same job again every five minutes. Heartbeat: prompt, tool, result, tool, until the model answers with no tools.",
    ),
    (
        "10", "core", "inner",
        "Im SDK heißt der Herzschlag max Turns und max Budget. Turns zählen nur Tool-Runden. Ohne Tools redet das Modell nur. Mit Tools handelt es. Slash Loop startet viele Herzschläge. Ein Herzschlag ist noch kein Slash Loop.",
        "In the SDK the heartbeat is max turns and max budget. Turns count tool round-trips only. No tools, it only talks. With tools, it acts. Slash loop starts many heartbeats. One heartbeat is not a slash loop.",
    ),
    (
        "11", "core", "platforms",
        "Zwei Gebäude, gleicher Job. Claude Code: Slash Loop lebt in der Session. Slash Schedule ist die Nachtschicht in der Cloud. Cursor lokal: eine PowerShell, die alle dreihundert Sekunden einen Sentinel schreit. Cursor Cloud: Subscription Timer.",
        "Two buildings, same job. Claude Code: slash loop lives in the session. Slash schedule is the cloud night shift. Cursor local: PowerShell that yells a sentinel every three hundred seconds. Cursor cloud: subscription timer.",
    ),
    (
        "12", "core", "platforms",
        "Cursor-Falle, merkt euch die. Gleicher Timer-Name, ohne Unsubscribe, ist ein stilles Nein. Du klebst einen neuen Zettel auf den Thermostat. Der Kessel unten ändert sich nicht. Erst abmelden, dann neu anmelden. Sonst denkst du, du hättest retuned.",
        "Cursor trap, remember it. Same timer name, no unsubscribe, is a silent no. You stick a new note on the thermostat. The boiler downstairs does not change. Unsubscribe first, then subscribe. Else you think you retuned.",
    ),
    (
        "13", "demo", "code_cc",
        "Walkthrough, Claude Code, der Klassiker. Slash Loop fünf m: schau meinen PR an, beiss dich durch Review-Kommentare, flick kaputtes CI. Das ist Boris Chernys Babysitter. Du gehst Kaffee holen. Der Wächter bleibt.",
        "Walkthrough, Claude Code, the classic. Slash loop five m: look at my PR, chew review comments, patch broken CI. Boris Cherny's babysitter. You get coffee. The watch stays.",
    ),
    (
        "14", "demo", "code_cc",
        "Zweite Taste: Slash Goal. Homepage Lighthouse auf neunzig, Schluss nach fünf Versuchen. Der Coach pfeift nicht ab, weil das Modell müde ist. Er pfeift ab, weil die Zahl stimmt, oder die Kappe greift. Zahlen, nicht Vibes.",
        "Second key: slash goal. Homepage Lighthouse to ninety, stop after five tries. The coach does not blow the whistle because the model is tired. He blows it because the number holds, or the cap hits. Numbers, not vibes.",
    ),
    (
        "15", "demo", "code_cc",
        "Die Kombi, wenn du mutig bist. Schedule jede Stunde: guck in den Feedback-Kanal. Goal: jeder neue Bug in diesem Lauf ist triagiert, angefasst, beantwortet. Parallel drei Worktrees, ein Richter, der böse liest. Das ist keine Demo mehr. Das ist eine Schicht.",
        "The combo if you are brave. Schedule every hour: peek at the feedback channel. Goal: every new bug this run is triaged, touched, answered. Three worktrees in parallel, a judge who reads mean. That is not a demo. That is a shift.",
    ),
    (
        "16", "demo", "code_ps",
        "Cursor auf Windows. While true. Sleep dreihundert. Echo AGENT LOOP TICK deploy, und daneben ein JSON mit dem Prompt. Notify on output, Regex mit Dach. Einmal sofort ausführen. Der erste Sentinel darf erst nach dem Schlaf kommen. Sonst doppelst du den Tick.",
        "Cursor on Windows. While true. Sleep three hundred. Echo AGENT LOOP TICK deploy, plus JSON with the prompt. Notify on output, caret regex. Run once now. First sentinel only after the sleep. Else you double the tick.",
    ),
    (
        "17", "demo", "code_ps",
        "Titel die Shell: Loop every five m, check deploy. Ein Name pro Loop, sonst weckt fremder Lärm den Agenten. Stopp heißt: PID tot, keinen neuen Heartbeat armieren. Und den Completion-Ping verbrauchen, sonst steht er nachts wieder auf.",
        "Title the shell: loop every five m, check deploy. One name per loop, or stray noise wakes the agent. Stop means: PID dead, do not arm another heartbeat. And consume the completion ping, or it rises at night again.",
    ),
    (
        "18", "demo", "code_sdk",
        "SDK-Walkthrough, ganz kurz. Claude Agent Options: max Turns acht, max Budget zwei Dollar fünfzig. Der Loop im SDK ist der Herzschlag. Wenn du das mit Slash Loop verwechselst, baust du zwei Wecker und wunderst dich, warum die Küche brennt.",
        "SDK walkthrough, short. Claude agent options: max turns eight, max budget two fifty. The SDK loop is the heartbeat. Mix it with slash loop and you build two alarms, then wonder why the kitchen is on fire.",
    ),
    (
        "19", "core", "spec",
        "Forscher haben dem Ding einen Namen gegeben. Archiv 2607.00038: Loop-Spezifikation. Trigger, Goal, Arbeit, Verifikation, Stopp plus Gedächtnis auf der Disk. Nicht im Chat. Im Chat vergisst der Agent, dass er gestern schon dreimal gescheitert ist.",
        "Researchers named the object. arXiv 2607.00038: loop specification. Trigger, goal, work, verify, stop plus memory on disk. Not in chat. In chat the agent forgets it already failed three times yesterday.",
    ),
    (
        "20", "core", "spec",
        "Fünf Endzustände, merkt euch die wie Ampeln. Success. No-op, nichts zu tun. Blocked, Mensch braucht. Stalled, keine Bewegung. Exhausted, Kappe leer. Ein Fehler darf niemals Success heißen. Sonst tanzt ihr auf einer grünen Lüge.",
        "Five terminals, learn them like lights. Success. No-op, nothing to do. Blocked, human needed. Stalled, no motion. Exhausted, cap empty. An error must never be named success. Else you dance on a green lie.",
    ),
    (
        "21", "core", "spec",
        "Zweites Paper, 2608.21884. Sie haben Open Source durchsucht. 217 autonome Loops bestätigt. Die Config liegt im Repo. Die State-Datei fast nie. Runtime lebt neben Git, wie Suppe im Kühlschrank, während das Rezept im Kochbuch steht. Plant das ein, oder eure Loops lügen im Daily.",
        "Second paper, 2608.21884. They mined open source. 217 autonomous loops confirmed. Config lives in the repo. State files almost never. Runtime lives beside git, soup in the fridge, recipe in the cookbook. Design for that, or your loops lie in standup.",
    ),
    (
        "22", "core", "fail",
        "Wie Loops sterben, Küchenversion. Infinite Fix: dieselbe Soße fünfmal nachsalzen. Verifier Theater: der Kritiker nickt, der Gast spuckt. Token Burn: der Herd läuft, obwohl niemand bestellt. Parallel Collision: zwei Köche, ein Messer.",
        "How loops die, kitchen version. Infinite fix: salt the same sauce five times. Verifier theater: the critic nods, the guest spits. Token burn: the stove runs with no orders. Parallel collision: two cooks, one knife.",
    ),
    (
        "23", "core", "fail",
        "Pflaster. Drei Versuche, dann Mensch. Tests als Orakel, nicht Modell-Meinung. Erst billige Triage, dann fette Subagents. Worktree-Isolation plus Schloss. Und bei Cursor: Unsubscribe, bevor du den Takt änderst. Sonst klebt ihr weiter den Thermostat-Zettel.",
        "Patches. Three tries, then a human. Tests as oracle, not model opinion. Cheap triage first, then fat subagents. Worktree isolation plus a lock. And on Cursor: unsubscribe before you change the beat. Else you keep sticking thermostat notes.",
    ),
    (
        "24", "core", "fail",
        "Tokens. Fünf-Minuten-Loop, der jedes Mal das ganze Monorepo liest, ist kein Loop. Das ist eine Heizung im August. Intervall an die Änderungsrate koppeln. Kleines Modell für den Rundgang. Großes Modell nur, wenn geurteilt wird.",
        "Tokens. A five-minute loop that rereads the whole monorepo every tick is not a loop. It is a heater in August. Match the interval to how fast the world changes. Small model for the walk. Big model only when judging.",
    ),
    (
        "25", "summary", "close",
        "Die Übung von Anthropic ist fies und gut. Wo bist du der Flaschenhals? Kannst du den Check abgeben? Die Stoppbedingung? Den Trigger? Oder den ganzen Prompt? Fang mit einem Hebel an. Nicht mit einer Fabrik.",
        "Anthropic's drill is mean and good. Where are you the bottleneck? Can you hand off the check? The stop? The trigger? Or the whole prompt? Start with one lever. Not a factory.",
    ),
    (
        "26", "summary", "close",
        "Lauf, schau wo er stallt oder übergreift, dann härte den Harness. Skill, Verifier, State-Datei. Nicht den Prompt um drei Adjektive. Und wenn der Wächter schläft, weck ihn nicht mit mehr Poesie. Weck ihn mit einer messbaren Ampel.",
        "Run it, watch where it stalls or overreaches, then harden the harness. Skill, verifier, state file. Not three more adjectives on the prompt. If the watch sleeps, do not wake it with more poetry. Wake it with a measurable light.",
    ),
    (
        "27", "summary", "close",
        "Quellen, falls ihr nachlesen wollt: Claude Blog Getting started with loops. Docs Commands und Scheduled Tasks. Explainx hat die Taxonomie schön aufgeräumt. Zwei Archiv-Papers, 2607 und 2608. Cursor SKILL loop für die lokale Variante.",
        "Sources if you want to read: Claude blog getting started with loops. Docs commands and scheduled tasks. Explainx cleaned the taxonomy. Two arXiv papers, 2607 and 2608. Cursor SKILL loop for the local variant.",
    ),
    (
        "28", "summary", "close",
        "Also. Baut keinen Wächter, der Romane vorliest. Baut einen, der auf die Tür starrt, die Zahl kennt, und um Hilfe schreit, wenn die Soße fünfmal versalzen ist. Das war die Theorie. Jetzt das Labor.",
        "So. Do not build a watch that recites novels. Build one that stares at the door, knows the number, and yells when the sauce is salted five times. That was theory. Now the lab.",
    ),
    (
        "29", "demo", "myths",
        "Mythbusters-Regel. Blogposts sind Zeugen. Quelltext und Messungen sind Beweise. Wir haben den Parser aus Claude Code 2.1.71 gegen die Docs von 2026 laufen lassen. Gleicher Befehl. Zwei Welten.",
        "Mythbusters rule. Blog posts are witnesses. Source and measurements are evidence. We ran the parser from Claude Code 2.1.71 against the 2026 docs. Same command. Two worlds.",
    ),
    (
        "30", "demo", "code_parse",
        "Schaut den Parser an. Führendes Token, Ziffer plus s m h d. Sonst trailing every, aber nur wenn danach eine Zeit steht. Check every PR? Every ist nicht die Uhr. Das ist ein Substantiv in Uniform.",
        "Look at the parser. Leading token, digit plus s m h d. Else trailing every, only if a time follows. Check every PR? Every is not the clock. It is a noun in uniform.",
    ),
    (
        "31", "demo", "code_parse",
        "Mythos eins, gesprengt. Slash Loop check the deploy ist nicht immer Self-Pace. In 2.1.71 ist der Default zehn Minuten fest. In den aktuellen Docs: dynamisch, eine Minute bis eine Stunde. Außer Bedrock und Foundry, da bleibt die Zehn. Version lesen, nicht den Tweet.",
        "Myth one, busted. Slash loop check the deploy is not always self-pace. In 2.1.71 the default is a fixed ten minutes. Current docs: dynamic, one minute to one hour. Except Bedrock and Foundry, they stay at ten. Read the version, not the tweet.",
    ),
    (
        "32", "demo", "code_gaps",
        "Mythos drei und vier, Labor. Dreißig s wird nicht dreißig Sekunden. Cron kennt keine Sekunden. Ceil auf eine Minute. Sieben m: die Treffer sind null, sieben, vierzehn, bis sechsundfünfzig. Der Sprung über die Stunde ist vier Minuten, nicht sieben. Der Wecker hinkt.",
        "Myths three and four, lab. Thirty s is not thirty seconds. Cron has no seconds. Ceil to one minute. Seven m: hits zero, seven, fourteen, through fifty-six. The wrap across the hour is four minutes, not seven. The alarm limps.",
    ),
    (
        "33", "demo", "code_gaps",
        "Mythos sechs. Fünf-Minuten-Job feuert nicht auf die Sekunde. Jitter bis zur Hälfte des Intervalls, also einhundertfünfzig Sekunden. Kein Nachholen, wenn Claude beschäftigt ist. Einmal, wenn er frei wird. Pünktlichkeit ist Marketing.",
        "Myth six. A five-minute job does not fire on the second. Jitter up to half the interval, one hundred fifty seconds. No catch-up if Claude is busy. Once, when idle. Punctuality is marketing.",
    ),
    (
        "34", "demo", "code_sent",
        "Cursor ist kein Cron. Der Skill sagt Sleep, dann Echo AGENT LOOP TICK, Dach-Regex. Wir haben Start-Sleep gemessen. Auf null komma vier Sekunden: siebzehn Millisekunden Mittel-Fehler. Auf fünf Minuten ist das Rauschen. Der Jitter von Claude frisst euch lebendig. Der Sleep nicht.",
        "Cursor is not cron. The skill says sleep, then echo AGENT LOOP TICK, caret regex. We measured Start-Sleep. On zero point four seconds: seventeen milliseconds mean error. At five minutes that is noise. Claude jitter eats you alive. Sleep does not.",
    ),
    (
        "35", "demo", "code_sent",
        "Mythos neun, Double Tick. Wenn du Echo vor den Sleep stellst, und den Prompt sofort ausführst, knallt es zweimal in einer Sekunde. Der Skill ist da gnadenlos: Prompt jetzt, Sentinel erst nach dem Schlaf. Reihenfolge ist der Test, nicht die Absicht.",
        "Myth nine, double tick. Echo before sleep, plus run the prompt now, and you fire twice in one second. The skill is ruthless: prompt now, sentinel only after sleep. Order is the test, not intent.",
    ),
    (
        "36", "demo", "bench",
        "Noch zwei Sprengungen. Drei Tage Expiry? Der Skill von März sagt drei. Die Docs jetzt sagen sieben, letzter Schuss, dann tot. Und Slash Loop zwanzig m Slash Permissions startet nicht die Permissions-UI. Built-ins kommen als Klartext an. Sie laufen nicht.",
        "Two more blasts. Three day expiry? The March skill says three. Docs now say seven, one last fire, then dead. And slash loop twenty m slash permissions does not open the permissions UI. Built-ins arrive as plain text. They do not run.",
    ),
    (
        "37", "demo", "bench",
        "Die Tabelle aus unserem Lauf. Elf Inputs. Nur zwei Streitfälle: check the deploy, und check every PR. Alles mit führender Zeit oder every 20 m ist einig. Der Streit sitzt genau dort, wo Blogs am lautesten sind. Deshalb messen.",
        "The table from our run. Eleven inputs. Only two fights: check the deploy, and check every PR. Everything with a leading time or every 20 m agrees. The fight sits exactly where blogs shout loudest. That is why we measure.",
    ),
    (
        "38", "summary", "close",
        "Also wirklich Schluss. Parser committen. 7 m nicht anfassen. 30 s nicht glauben. Sentinel mit Dach. Sleep vor Echo. Version der Docs neben den Skill legen. Dann darfst du tanzen. Der Wächter hat jetzt ein Laborprotokoll, nicht nur Charme.",
        "So, really the end. Commit the parser. Do not touch 7 m. Do not believe 30 s. Sentinel with a caret. Sleep before echo. Put the docs version next to the skill. Then you may dance. The watch now has a lab notebook, not just charm.",
    ),
]


@dataclass
class Cue:
    sid: str
    section: str
    de: str
    en: str
    start: float
    end: float


def tts_clean(text: str) -> str:
    t = text.replace("Slash Loop", "Slash-Loop").replace("Slash Goal", "Slash-Goal")
    t = t.replace("Slash Schedule", "Slash-Schedule")
    t = t.replace("/", " ")
    t = t.replace("CI", " C I ")
    t = t.replace("PR", " P R ")
    t = t.replace("SDK", " S D K ")
    t = t.replace("JSON", " Jason ")
    t = t.replace("Lighthouse", " Lait-Haus ")
    t = t.replace("arXiv", " Archiv ")
    return re.sub(r"\s+", " ", t).strip()


def wrap(text: str, width: int = 88, max_lines: int = 3) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False)[:max_lines])


def wrap_code(code: str, width: int) -> str:
    out: list[str] = []
    for line in code.splitlines():
        if len(line) <= width:
            out.append(line)
            continue
        out.extend(
            textwrap.wrap(line, width=width, break_long_words=False, replace_whitespace=False)
            or [line]
        )
    return "\n".join(out[:20])


def audio_duration(path: Path) -> float:
    proc = subprocess.run(
        [FFMPEG, "-i", str(path)], capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.?\d*)", proc.stderr)
    if not m:
        return 5.0
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


async def tts_save(text: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(tts_clean(text), VOICE, rate=RATE).save(str(path))


def png_wh(blob: bytes) -> tuple[int, int]:
    if blob[:8] != b"\x89PNG\r\n\x1a\n" or len(blob) < 24:
        return 0, 0
    import struct
    w, h = struct.unpack(">II", blob[16:24])
    return w, h


def png_is_dark_diagram(blob: bytes) -> bool:
    w, h = png_wh(blob)
    if h < 80:
        return False
    arr = np.asarray(PILImage.open(io.BytesIO(blob)).convert("RGB").resize((32, 32)))
    return float(arr.mean()) < 140


def _plantuml_encode(src: str) -> str:
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    data = zlib.compress(src.encode("utf-8"))[2:-4]
    out = []
    for i in range(0, len(data), 3):
        b1 = data[i]
        b2 = data[i + 1] if i + 1 < len(data) else 0
        b3 = data[i + 2] if i + 2 < len(data) else 0
        n = (b1 << 16) + (b2 << 8) + b3
        out.append(alphabet[(n >> 18) & 63])
        out.append(alphabet[(n >> 12) & 63])
        out.append(alphabet[(n >> 6) & 63])
        out.append(alphabet[n & 63])
    return "".join(out)


PUML_CONTRAST = r"""
<style>
root {
  FontColor #e8eef5
  LineColor #69f0ae
  LineThickness 2.5
  BackgroundColor #0a0e14
}
arrow {
  LineColor #69f0ae
  LineThickness 2.5
  FontColor #e8eef5
}
lifeLine {
  LineColor #90caf9
  LineThickness 2
}
group {
  LineColor #90caf9
  LineThickness 2.5
  BackgroundColor #1a2530
  FontColor #ffcc80
}
.participant {
  BackgroundColor #121a24
  FontColor #e8eef5
  LineColor #69f0ae
}
</style>
skinparam ArrowColor #69f0ae
skinparam ArrowThickness 3
skinparam titleFontColor #e8eef5
skinparam titleBackgroundColor #121a24
skinparam titleBorderColor #69f0ae
skinparam sequenceLifeLineBorderColor #90caf9
skinparam sequenceGroupBorderColor #90caf9
skinparam sequenceGroupBackgroundColor #1a2530
skinparam sequenceGroupHeaderFontColor #ffcc80
skinparam actorBorderColor #69f0ae
skinparam actorBackgroundColor #121a24
skinparam actorFontColor #e8eef5
skinparam participantBorderColor #69f0ae
skinparam participantBackgroundColor #121a24
skinparam participantFontColor #e8eef5
skinparam rectangleBorderColor #90caf9
skinparam packageBorderColor #90caf9
skinparam cardBorderColor #69f0ae
skinparam noteBorderColor #ffcc80
skinparam noteBackgroundColor #1a2530
skinparam noteFontColor #e8eef5
skinparam activityBorderColor #69f0ae
skinparam activityArrowColor #69f0ae
skinparam componentBorderColor #69f0ae
"""


def with_puml_contrast(src: str) -> str:
    block = PUML_CONTRAST.strip()
    if "@enduml" in src:
        return src.replace("@enduml", block + "\n@enduml", 1)
    return src + "\n" + block


def render_puml(puml_path: Path, out_png: Path) -> None:
    src = with_puml_contrast(puml_path.read_text(encoding="utf-8"))
    out_png.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        "https://kroki.io/plantuml/png",
        data=src.encode("utf-8"),
        headers={"Content-Type": "text/plain", "User-Agent": "mindcraft-zttts/1.0", "Accept": "image/png"},
        method="POST",
    )
    blob = b""
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            blob = resp.read()
    except urllib.error.HTTPError as e:
        blob = e.read() or b""
    except (urllib.error.URLError, TimeoutError):
        blob = b""
    if png_is_dark_diagram(blob):
        out_png.write_bytes(blob)
        return
    encoded = _plantuml_encode(src)
    last_err: Exception | None = None
    for url in (
        "https://www.plantuml.com/plantuml/png/" + encoded,
        "https://www.plantuml.com/plantuml/png/~1" + encoded,
    ):
        req2 = urllib.request.Request(url, headers={"User-Agent": "mindcraft-zttts/1.0"})
        try:
            with urllib.request.urlopen(req2, timeout=90) as resp:
                fb = resp.read()
            if png_is_dark_diagram(fb):
                out_png.write_bytes(fb)
                return
        except urllib.error.HTTPError as e:
            last_err = e
            continue
    raise RuntimeError(f"PlantUML render failed for {puml_path.name}: {last_err}")


def header(fig, section: str, sid: str, *, tall: bool = False) -> None:
    if tall:
        ax = fig.add_axes([0.05, 0.845, 0.90, 0.10])
        ax.axis("off")
        ax.text(0, 0.68, "Slash Loop", fontsize=34, color="white", fontweight="bold", va="center")
        ax.text(0, 0.22, "der Wächter, nicht das Hörbuch", fontsize=18, color=C_ACC, va="center")
        ax.text(1, 0.68, "f-university", fontsize=16, color="#667788", ha="right", va="center")
        ax.text(1, 0.22, f"{sid} · {section.upper()}", fontsize=16, color="#8899aa", ha="right", va="center")
        return
    ax = fig.add_axes([0.04, 0.905, 0.92, 0.07])
    ax.axis("off")
    ax.text(0, 0.58, "Slash Loop  ·  der Wächter, nicht das Hörbuch", fontsize=24, color="white", fontweight="bold", va="center")
    ax.text(0, 0.08, f"{sid}  ·  {section.upper()}  ·  DE playback +38%  ·  DE+EN", fontsize=13, color="#8899aa", va="center")
    ax.text(1, 0.58, "f-university", fontsize=13, color="#667788", ha="right", va="center")


def sub_bar(fig, de: str, en: str, *, tall: bool = False) -> None:
    if tall:
        ax = fig.add_axes([0.03, 0.150, 0.94, 0.33])
        ax.axis("off")
        ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.008", facecolor="#0a1018", edgecolor=C_EN, lw=3, transform=ax.transAxes))
        ax.text(0.04, 0.97, wrap(de, 32, 5), fontsize=30, color=C_DE, fontweight="bold", va="top", transform=ax.transAxes, linespacing=1.12)
        ax.text(0.04, 0.44, wrap(en, 34, 4), fontsize=24, color=C_EN, va="top", transform=ax.transAxes, linespacing=1.12)
        return
    ax = fig.add_axes([0.035, 0.035, 0.93, 0.175])
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.012", facecolor="#0a1018", edgecolor=C_EN, lw=2, transform=ax.transAxes))
    ax.text(0.02, 0.70, wrap(de, 96), fontsize=14, color=C_DE, fontweight="bold", va="center", transform=ax.transAxes)
    ax.text(0.02, 0.26, wrap(en, 100), fontsize=13, color=C_EN, va="center", transform=ax.transAxes)


def show_puml(ax, stem: str, *, box_px: tuple[int, int] | None = None) -> None:
    png = PUML_PNG / f"{stem}.png"
    if box_px:
        bw, bh = box_px
        im = PILImage.open(png).convert("RGB")
        canvas = PILImage.new("RGB", (bw, bh), C_BG)
        im.thumbnail((max(1, bw - 16), max(1, bh - 16)), PILImage.Resampling.LANCZOS)
        canvas.paste(im, ((bw - im.width) // 2, (bh - im.height) // 2))
        ax.imshow(np.asarray(canvas))
    else:
        ax.imshow(plt.imread(png))
    ax.axis("off")
    ax.set_facecolor(C_BG)


def code_box(ax, title: str, code: str, color: str, *, tall: bool = False) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_facecolor(C_BG)
    body = wrap_code(code, 30 if tall else 88)
    ax.text(0.3, 9.38, wrap(title, 24 if tall else 60, 2), fontsize=24 if tall else 18, color="white", fontweight="bold")
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 9.6, 8.6 if tall else 8.4, boxstyle="round,pad=0.05", facecolor="#101820", edgecolor=C_LINE, lw=1.5))
    ax.text(0.4, 8.55 if tall else 4.6, body, fontsize=20 if tall else 14, color=color, family="DejaVu Sans Mono", va="top" if tall else "center", linespacing=1.18)


def slide_hook(ax, *, tall: bool = False) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_facecolor(C_BG)
    if tall:
        ax.text(5, 7.75, "You are not\nthe night watch.", ha="center", fontsize=44, color="white", fontweight="bold", linespacing=1.12)
        ax.text(5, 5.15, "You hire one.", ha="center", fontsize=36, color=C_ACC)
        ax.text(5, 2.95, "Turn = you stand at the door\n/loop = the watch on his wrist", ha="center", fontsize=22, color="#99aabb", linespacing=1.3)
        return
    ax.text(5, 6.6, "You are not the night watch.", ha="center", fontsize=32, color="white", fontweight="bold")
    ax.text(5, 4.9, "You hire one.", ha="center", fontsize=28, color=C_ACC)
    ax.text(5, 3.0, "Turn = you stand at the door\n/loop = the watch on his wrist", ha="center", fontsize=16, color="#99aabb")


def slide_close(ax, *, tall: bool = False) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_facecolor(C_BG)
    if tall:
        ax.text(5, 7.75, "Hand off\nONE lever.", ha="center", fontsize=44, color="white", fontweight="bold", linespacing=1.12)
        ax.text(5, 5.15, "check  ·  stop\ntrigger  ·  prompt", ha="center", fontsize=24, color=C_ACC, linespacing=1.28)
        ax.text(5, 2.8, "Measure it.\nThen go dancing.", ha="center", fontsize=24, color=C_DE, linespacing=1.28)
        return
    ax.text(5, 7.2, "Hand off ONE lever.", ha="center", fontsize=30, color="white", fontweight="bold")
    ax.text(5, 5.2, "check   ·   stop   ·   trigger   ·   prompt", ha="center", fontsize=18, color=C_ACC)
    ax.text(5, 3.2, "Measure it. Then go dancing.", ha="center", fontsize=18, color=C_DE)


def slide_bench(ax, *, tall: bool = False) -> None:
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_facecolor(C_BG)
    ax.text(0.3, 9.45, "Lab · bench_loop.py", fontsize=20 if tall else 16, color="white", fontweight="bold")
    rows = [
        ("input", "2.1.71", "2026 docs"),
        ("5m /babysit-prs", "5m leading", "5m fixed"),
        ("deploy every 20m", "20m trailing", "20m fixed"),
        ("check the deploy", "10m DEFAULT", "DYNAMIC 1m-1h"),
        ("check every PR", "10m kept", "DYNAMIC kept"),
        ("30s check status", "30s -> 1m", "30s -> 1m"),
        ("7m check ci", "wrap=4min", "round step"),
        ("PS Sleep 0.4s", "err 17ms", "jitter 150s"),
        ("3d vs 7d expiry", "skill: 3d", "docs: 7d"),
    ]
    step = 0.86 if tall else 0.85
    fs = 18 if tall else 13
    for i, (a, b, c) in enumerate(rows):
        y = 8.55 - i * step
        col = C_ACC if i == 0 else ("#ff8a80" if "DEFAULT" in b or "DYNAMIC" in c or "4min" in b else "#e8eef5")
        if tall:
            ax.text(0.35, y + 0.22, a, fontsize=fs, color=col, family="DejaVu Sans Mono", va="center")
            ax.text(0.35, y - 0.18, f"{b}  |  {c}", fontsize=fs, color=col, family="DejaVu Sans Mono", va="center")
        else:
            ax.text(0.35, y, a, fontsize=fs, color=col, family="DejaVu Sans Mono", va="center")
            ax.text(3.7, y, b, fontsize=fs, color=col, family="DejaVu Sans Mono", va="center")
            ax.text(6.7, y, c, fontsize=fs, color=col, family="DejaVu Sans Mono", va="center")



PUML = {
    "types": "01-types",
    "syntax": "02-syntax",
    "inner": "03-inner-outer",
    "platforms": "04-platforms",
    "spec": "05-spec",
    "fail": "06-failures",
    "myths": "07-myths",
}


def draw_slide(sid: str, section: str, visual: str, de: str, en: str, path: Path, *, tall: bool = False) -> None:
    w, h = (WP, HP) if tall else (W, H)
    fig = plt.figure(figsize=(w / DPI, h / DPI), dpi=DPI, facecolor=C_BG)
    header(fig, section, sid, tall=tall)
    if tall:
        ax = fig.add_axes([0.04, 0.50, 0.92, 0.33])
        box_px = (int(0.92 * WP), int(0.33 * HP))
    else:
        ax = fig.add_axes([0.04, 0.23, 0.92, 0.66])
        box_px = None
    if visual in PUML:
        show_puml(ax, PUML[visual], box_px=box_px)
    elif visual == "hook":
        slide_hook(ax, tall=tall)
    elif visual == "close":
        slide_close(ax, tall=tall)
    elif visual == "code_cc":
        code_box(ax, "Walkthrough · Claude Code — type this", """/loop 5m check my PR, address review comments,
        and fix failing CI

/goal get homepage Lighthouse >= 90, stop after 5 tries

/schedule every hour: check #project-feedback
  /goal: triage + action + reply every new report
  explore 3 fixes in worktrees, judge them mean""", C_EN, tall=tall)
    elif visual == "code_ps":
        code_box(ax, "Walkthrough · Cursor local · PowerShell", r"""while ($true) {
  Start-Sleep -Seconds 300
  echo 'AGENT_LOOP_TICK_deploy {"prompt":"check deploy"}'
}
# notify_on_output   ^AGENT_LOOP_TICK_deploy
# run the prompt ONCE now
# first sentinel AFTER sleep — no double tick
# stop = kill PID, do not re-arm""", C_DE, tall=tall)
    elif visual == "code_sdk":
        code_box(ax, "Walkthrough · SDK heartbeat  !=  /loop alarm", """options = ClaudeAgentOptions(
    max_turns=8,          # tool round-trips only
    max_budget_usd=2.50,  # hard cost stop
)
# prompt -> tool_use -> results -> repeat
# ends when the model replies with NO tools
# that cycle is the heartbeat
# /loop is the alarm that starts many heartbeats""", "#e8eef5", tall=tall)
    elif visual == "code_parse":
        code_box(ax, "Lab · parser we actually ran (2.1.71 skill)", r"""INTERVAL = r'^(\d+)([smhd])$'          # leading 5m / 30s
EVERY = r'^(.*) every (\d+)\s*(s|m|h|d|minutes?)\s*$'

# 5m /babysit-prs     -> 5m, prompt=/babysit-prs
# check deploy every 20m -> 20m, prompt=check deploy
# check every PR      -> NOT an interval ('every' + noun)
# check the deploy    -> 2.1.71: 10m FIXED
#                      -> 2026 docs: DYNAMIC 1m-1h""", C_ACC, tall=tall)
    elif visual == "code_gaps":
        code_box(ax, "Lab · cron math, measured on this machine", """seconds_ceil(30) = 1 minute     # 30s is a lie
*/7 hits  0 7 14 21 28 35 42 49 56
gaps      7 7  7  7  7  7  7  7  4   # wrap = 4 min
5m jitter bound = min(30min, interval/2) = 150s
busy session: NO catch-up, fire once when idle
PS Start-Sleep 0.4s  mean error 17ms   # noise vs jitter""", C_DE, tall=tall)
    elif visual == "code_sent":
        code_box(ax, "Lab · Cursor sentinel + no double-tick", r"""# GOOD
run_prompt_now()
while ($true) {
  Start-Sleep -Seconds 300
  echo 'AGENT_LOOP_TICK_deploy {"prompt":"check deploy"}'
}
# notify_on_output  ^AGENT_LOOP_TICK_deploy

# BAD: echo then sleep + run_now  => 2 fires in <1s
# ^ is required: 'noise AGENT_LOOP_TICK_deploy later' must NOT match""", C_EN, tall=tall)
    elif visual == "bench":
        slide_bench(ax, tall=tall)
    else:
        ax.axis("off")
    sub_bar(fig, de, en, tall=tall)
    fig.savefig(path, facecolor=C_BG)
    plt.close(fig)


def fmt_srt(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, rem = divmod(ms, 3600000)
    m, rem = divmod(rem, 60000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def fmt_ass(sec: float) -> str:
    cs = int(round(sec * 100))
    h, rem = divmod(cs, 360000)
    m, rem = divmod(rem, 6000)
    s, cs = divmod(rem, 100)
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


def write_ass(cues: list[Cue], path: Path, *, px: int, py: int, de_size: int, en_size: int, de_m: int, en_m: int) -> None:
    header_ass = f"""[Script Info]
Title: loop-slash DE+EN
ScriptType: v4.00+
PlayResX: {px}
PlayResY: {py}

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, OutlineColour, BackColour, Bold, Alignment, MarginL, MarginR, MarginV, BorderStyle, Outline, Encoding
Style: DE,Microsoft YaHei,{de_size},&H80CCFF,&H00101010,&H80000000,-1,2,48,48,{de_m},1,2,1
Style: EN,Microsoft YaHei,{en_size},&H9FC90,&H00101010,&H80000000,0,2,48,48,{en_m},1,2,1

[Events]
Format: Layer, Start, End, Style, Text
"""
    ev = []
    for c in cues:
        ev.append(f"Dialogue: 0,{fmt_ass(c.start)},{fmt_ass(c.end)},DE,{c.de}")
        ev.append(f"Dialogue: 0,{fmt_ass(c.start)},{fmt_ass(c.end)},EN,{c.en}")
    path.write_text(header_ass + "\n".join(ev) + "\n", encoding="utf-8")


def write_subs(cues: list[Cue]) -> None:
    lines: list[str] = []
    for i, c in enumerate(cues, 1):
        lines += [str(i), f"{fmt_srt(c.start)} --> {fmt_srt(c.end)}", f"DE: {c.de}", f"EN: {c.en}", ""]
    SRT.write_text("\n".join(lines), encoding="utf-8")
    write_ass(cues, ASS, px=1920, py=1080, de_size=32, en_size=28, de_m=72, en_m=30)
    write_ass(cues, ASS_P, px=1080, py=1920, de_size=42, en_size=34, de_m=360, en_m=280)


def write_chapters(cues: list[Cue]) -> None:
    by_id = {c.sid: c for c in cues}

    def stamp(sec: float) -> str:
        m, s = divmod(int(sec), 60)
        return f"{m}:{s:02d}"

    rows = ["YouTube / Bilibili chapters (paste as first lines of description)", ""]
    for sid, label in CHAPTER_LABELS.items():
        if sid in by_id:
            rows.append(f"{stamp(by_id[sid].start)} {label}")
    CHAPTERS.write_text("\n".join(rows) + "\n", encoding="utf-8")


def make_silence(path: Path, sec: float) -> None:
    subprocess.run(
        [FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(sec), "-q:a", "9", str(path)],
        check=True, capture_output=True,
    )


def ffmpeg_concat(paths: list[Path], out: Path) -> None:
    lst = out.with_suffix(".concat.txt")
    lst.write_text("\n".join(f"file '{p.resolve().as_posix()}'" for p in paths), encoding="utf-8")
    subprocess.run(
        [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(out)],
        check=True, capture_output=True,
    )


def ffmpeg_ok(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0:
        err = (proc.stderr or b"").decode("utf-8", errors="replace")[-4000:]
        raise RuntimeError(f"ffmpeg failed ({proc.returncode}):\n{err}")


def encode_video(concat_txt: Path, full_audio: Path, out: Path) -> None:
    silent = out.with_name(out.stem + "._silent.mp4")
    ffmpeg_ok(
        [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat_txt),
         "-vsync", "vfr", "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", str(silent)]
    )
    ffmpeg_ok(
        [FFMPEG, "-y", "-i", str(silent), "-i", str(full_audio),
         "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-shortest", str(out)]
    )
    silent.unlink(missing_ok=True)


def build_slides(durs: list[float], *, tall: bool) -> tuple[Path, list[Cue]]:
    slides = SLIDES_P if tall else SLIDES
    slides.mkdir(parents=True, exist_ok=True)
    tag = "9x16" if tall else "16x9"
    print(f"Slides {tag}…")
    cues: list[Cue] = []
    lines: list[str] = []
    t = 0.0
    for i, ((sid, section, visual, de, en), dur) in enumerate(zip(SEGMENTS, durs)):
        png = slides / f"{sid}.png"
        draw_slide(sid, section, visual, de, en, png, tall=tall)
        hold = dur + (PAUSE if i < len(SEGMENTS) - 1 else 0.0)
        cues.append(Cue(sid, section, de, en, t, t + dur))
        lines.append(f"file '{png.resolve().as_posix()}'")
        lines.append(f"duration {hold:.3f}")
        t += hold
        print(" ", tag, sid, visual)
    last = slides / f"{SEGMENTS[-1][0]}.png"
    lines.append(f"file '{last.resolve().as_posix()}'")
    concat_vid = slides / "stills.concat.txt"
    concat_vid.write_text("\n".join(lines), encoding="utf-8")
    return concat_vid, cues


def hook_end(cues: list[Cue]) -> float:
    end = 0.0
    for c in cues:
        end = c.end
        if end >= HOOK_MIN:
            break
    return min(end, HOOK_CAP)


def cut_hook(src: Path, cues: list[Cue], dest: Path) -> float:
    end = hook_end(cues)
    ffmpeg_ok(
        [FFMPEG, "-y", "-i", str(src), "-t", f"{end:.3f}",
         "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", str(dest)]
    )
    return end


def make_covers() -> None:
    src_l = SLIDES / "01.png"
    src_p = SLIDES_P / "01.png"
    if src_l.exists():
        shutil.copyfile(src_l, COVER_L)
    if src_p.exists():
        shutil.copyfile(src_p, COVER_P)
        im = PILImage.open(src_p).convert("RGB")
        w, h = im.size
        target_h = int(w * 4 / 3)
        top = max(0, min(h - target_h, (h - target_h) // 5))
        im.crop((0, top, w, top + target_h)).resize((1080, 1440), PILImage.Resampling.LANCZOS).save(COVER_34)


def stamp_ttl() -> None:
    subprocess.run(
        [sys.executable, str(REPO / "cron" / "janitor.py"), "--touch"],
        check=True,
    )


def write_upload(total: float, hook: float | None) -> None:
    lines = [
        "Slash Loop · Wächter, nicht Hörbuch",
        "German +38% · dual DE/EN · PlantUML",
        f"master {total/60:.1f} min",
        f"16:9  {OUT.name}",
        f"9:16  {OUT_P.name}",
        f"hook  {OUT_HOOK.name}" + (f"  {hook:.1f}s" if hook else ""),
        "covers  cover.16x9.png  cover.9x16.png  cover.3x4.png",
        "forms   PUBLISH.md   chapters.txt",
        "Cleanup only after upload confirm.",
    ]
    (WORK / "upload.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def cleanup(*, also_mp4: bool) -> None:
    for d in (AUDIO, SLIDES, SLIDES_P, PUML_PNG):
        if d.exists():
            shutil.rmtree(d)
            print("removed", d)
    for p in WORK.glob("*._silent.mp4"):
        p.unlink(missing_ok=True)
    (WORK / "_silent.mp4").unlink(missing_ok=True)
    if also_mp4:
        for p in (OUT, OUT_P, OUT_HOOK):
            if p.exists():
                p.unlink()
                print("removed", p)
    print("cleanup done · kept skills/loop-slash kit. Masters were in tmp/loop-slash/")


async def render(*, force: bool, aspect: str) -> None:
    WORK.mkdir(parents=True, exist_ok=True)
    AUDIO.mkdir(parents=True, exist_ok=True)
    print("PlantUML via Kroki…")
    for puml in sorted(DIAG.glob("*.puml")):
        dest = PUML_PNG / f"{puml.stem}.png"
        if force or not dest.exists() or dest.stat().st_mtime < puml.stat().st_mtime:
            render_puml(puml, dest)
            print(" ", dest.name)

    silence = AUDIO / "_pause.mp3"
    if force or not silence.exists():
        make_silence(silence, PAUSE)

    print("TTS German @", RATE)
    audio_parts: list[Path] = []
    durs: list[float] = []
    for i, (sid, section, visual, de, en) in enumerate(SEGMENTS):
        mp3 = AUDIO / f"{sid}.mp3"
        if force and mp3.exists():
            mp3.unlink()
        if not mp3.exists():
            await tts_save(de, mp3)
        dur = audio_duration(mp3)
        durs.append(dur)
        audio_parts.append(mp3)
        if i < len(SEGMENTS) - 1:
            audio_parts.append(silence)
        print(f"  {sid} {dur:.1f}s")

    full_audio = AUDIO / "full.mp3"
    if force or not full_audio.exists():
        if full_audio.exists():
            full_audio.unlink()
        ffmpeg_concat(audio_parts, full_audio)

    def cues_from_durs() -> list[Cue]:
        out: list[Cue] = []
        t = 0.0
        for i, ((sid, section, _visual, de, en), dur) in enumerate(zip(SEGMENTS, durs)):
            out.append(Cue(sid, section, de, en, t, t + dur))
            t += dur + (PAUSE if i < len(SEGMENTS) - 1 else 0.0)
        return out

    puml_newer = any(
        OUT.exists() and p.stat().st_mtime > OUT.stat().st_mtime for p in DIAG.glob("*.puml")
    )
    do_16 = aspect in ("both", "16x9") and (force or not OUT.exists() or puml_newer)
    do_9 = aspect in ("both", "9x16")
    cues: list[Cue] = []
    hook_s: float | None = None

    if do_16:
        concat_16, cues = build_slides(durs, tall=False)
        print("Encode 16:9…")
        encode_video(concat_16, full_audio, OUT)
        print(" ", OUT)

    if do_9:
        concat_9, cues_p = build_slides(durs, tall=True)
        cues = cues_p
        print("Encode 9:16…")
        encode_video(concat_9, full_audio, OUT_P)
        print(" ", OUT_P)
        print("Encode hook…")
        hook_s = cut_hook(OUT_P, cues_p, OUT_HOOK)
        print(f"  {OUT_HOOK}  {hook_s:.1f}s")

    if not cues:
        cues = cues_from_durs()
    write_subs(cues)
    write_chapters(cues)
    make_covers()
    total = audio_duration(full_audio)
    write_upload(total, hook_s)
    stamp_ttl()
    print(f"DONE  {total/60:.1f} min  ·  see PUBLISH.md  ·  {WORK}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--aspect", choices=("both", "16x9", "9x16"), default="both")
    ap.add_argument("--cleanup", action="store_true")
    ap.add_argument("--confirmed-uploaded", action="store_true")
    ap.add_argument("--also-mp4", action="store_true")
    args = ap.parse_args()
    if args.cleanup:
        if not args.confirmed_uploaded:
            raise SystemExit("Refusing cleanup. Pass --confirmed-uploaded after the user says the upload is satisfied.")
        cleanup(also_mp4=args.also_mp4)
        return
    asyncio.run(render(force=args.force, aspect=args.aspect))


if __name__ == "__main__":
    main()
