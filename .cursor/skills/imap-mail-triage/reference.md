# IMAP mail triage — Titan + n8n

## Titan (GoDaddy)

| | |
| --- | --- |
| IMAP (GoDaddy Titan) | `imap.secureserver.net` `993` SSL |
| IMAP (native Titan) | `imap.titan.email` `993` SSL — not for GoDaddy-managed boxes |
| SMTP | do not configure in this skill |
| Auth | full mailbox address + mailbox password |

GoDaddy-skinned webmail (GoDaddy logo, left-nav Account / Security & Access) **does not show** Enable Titan on Other Apps. That control lives on native Titan Settings (gear). Missing it is expected. Security & Access is sessions only.

GoDaddy IMAP table: https://www.godaddy.com/help/use-imap-settings-to-add-my-professional-email-to-a-client-32204

Titan IMAP article tells GoDaddy users to use GoDaddy support, not `imap.titan.email`: https://support.titan.email/hc/en-us/articles/900000215446-Configure-Titan-on-other-apps-using-IMAP-POP

`--list-folders` is the smoke test. If `imap.titan.email` fails, switch host to `imap.secureserver.net`.

## Rule vs model

1. Domain / `noreply` / newsletter → `Life-Subscription` or `Junk`.
2. Avature → `Money-Job-Avature`.
3. Bewerbung / Interview in subject → `Money-Job`.
4. No match → leave in INBOX (or `--llm` if a key exists).

Do not spend tokens on LinkedIn job-alert mail.

## n8n (optional second runtime)

Same policy, different host. Only if n8n is already running.

1. Credentials: IMAP account (same host/user/app password).
2. Trigger: IMAP Email (UNSEEN) or Cron + IMAP.
3. IF / Switch on `from` domain (LinkedIn, Indeed, Salesforce) → **Move** to `Life-Subscription`.
4. Switch on subject keywords → `Money-Job`.
5. Optional OpenAI node only on the unmatched branch; parse a folder name; Move.
6. No Gmail/SMTP send node. No auto-reply.

Do not duplicate: pick **this script** or n8n, not both on the same UNSEEN stream.

## Privacy

- `.private/imap-triage.env` and `.private/imap-triage.rules.json` are gitignored via `.private/`. The `.env` is also in `.cursorignore` so the agent index does not ingest the mailbox password.
- Optional vault: `.cursor/skills/minsec-secrets`. After `minsec run` injects `IMAP_*`, delete the disk file.
- Digest in `tmp/` is headers only. No Ausweis, no mail body in pedagogy.
- Second mailbox `legal@` stays out of `IMAP_USER`.
- Gmail is a third mailbox: `.private/imap-gmail.env` + `--env`. Host `imap.gmail.com` `993`. Password is a Google App password, not the Gmail login. Do not overwrite Titan `imap-triage.env`. Template: `env.gmail.example`.
