---
name: imap-mail-triage
description: >-
  Zero-inbox IMAP triage for GoDaddy/Titan: Todo for mail about the human
  (applications, interviews, 1:1), other mail into mindcraft folders, leftover
  to Archive. Never sends. Use when the human names 处理邮件, 整理邮件, zero
  inbox, Todo, daily mail, IMAP, Titan, or GoDaddy inbox.
---

# IMAP mail triage

Daily: **zero inbox**. About-the-human → `Todo`. Known senders → organ folders. Else `Archive`. Never leave INBOX.

```
python .cursor/skills/imap-mail-triage/scripts/triage.py --apply --backlog --limit 400
```

Repeat until `inbox` is 0. Newest first. Digest `tmp/imap-triage/digest-YYYY-MM-DD.json` (headers only). Then `python cron/janitor.py --touch`.

Do not paste `.private/imap-triage.env` into chat. Do not invent STUDY ANSWER from mail bodies.

If MinSec is armed (`.cursor/skills/minsec-secrets`): wrap the same command with `minsec run -- …` and delete the leftover `.env` so the indexer has nothing to read. Until then, keep the private env file; it is gitignored and cursorignored.

## Folders (mindcraft)

| Folder | Keep |
| --- | --- |
| Todo | Interview, Kennenlernen, 1:1, or a human-named follow-up (bank/Amt). Absage → Trash. ATS-Eingang → Archive |
| Billing | Current invoices only. Login-alert, survey, add-funds, older than 1 year, confirm-email, Aktion → Trash |
| Legal | Amt / Vertrag |
| Life | calendar, tooling, Study. LinkedIn invitations / Job Alerts, DHL tracking, Instagram → Trash |
| Inflow / Namelos | harvest / product |
| Archive | leftover, old ATS, broker mail |
| Trash | ads, Payback Einkauf, newsletters |

Empty leftover `Life-*` / `DE` / `Money-*` / `Study-*` folders are deleted on the server.

GoDaddy IMAP host: `imap.secureserver.net` `993`. Gmail is a **second** env file, not `IMAP_USER` on Titan: `.private/imap-gmail.env`, host `imap.gmail.com` `993`, Google **App-Passwort**. Smoke: `python .cursor/skills/imap-mail-triage/scripts/triage.py --env .private/imap-gmail.env --list-folders`. [reference.md](reference.md).

## Hard

- Never send. Recruiter drafts stay human.
- Headers only. No body in pedagogy.
- OWA Playwright is a different mailbox.
