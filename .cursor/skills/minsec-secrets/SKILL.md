---
name: minsec-secrets
description: >-
  Routes mindcraft secrets off plaintext .env so AI IDEs cannot index them.
  Wraps local jobs with minsec run (in-memory env inject). Use when the human
  names MinSec, .env, API Key, secrets, E2EE vault, Cloudflare D1 credentials,
  or asks to keep keys off disk for Cursor / Copilot / Claude Code.
---

# MinSec secrets

Third-party CLI: [MinSec](https://github.com/cgx9/minsec) (`npm i -g minsec`). Vendor claims E2EE + in-memory inject via `minsec run -- <cmd>`. That slogan is **ClientHeldSecret**, not **ZeroKnowledgeProof**. Deploy path: **Wrangler** / Workers / D1. Graph: `pedagogy/universe.graph.md`. Workspace should keep a shareable `.minsec` linkage, **not** production values.

Do **not** paste secrets, `.private/*.env`, or MinSec API tokens into chat. Do not invent that keys were already migrated. Do not run `minsec list` in an agent TTY if values would print.

## Layer 1 — keep plaintext off the agent index

`.gitignore` already drops `.env` / `.private/`. Cursor still reads gitignored files unless they are in [`.cursorignore`](../../../.cursorignore). Secret-shaped paths stay there. Do not weaken that file to “debug the password”.

## Layer 2 — MinSec (optional vault)

Human installs and inits. Agent does not run `npm i -g` or `minsec deploy` unless asked.

```bash
npm i -g minsec
minsec server
minsec init
minsec run -- python .cursor/skills/imap-mail-triage/scripts/triage.py --apply --backlog --limit 400
```

After IMAP (or other) secrets live in MinSec, **delete** `.private/imap-triage.env` from disk. A vault plus a leftover `.env` still feeds the indexer.

Template: [minsec.example.json](minsec.example.json). Real linkage is `.minsec` (gitignored). Commands and license caveats: [reference.md](reference.md).

## Hard

- Treat vendor “zero-knowledge / kernel inject” as **claims**. Package is new (npm 1.0.x). Do not put production keys in until the human accepts that.
- License is **non-commercial** OSS; commercial company use needs the author’s license. Do not tell a client to deploy it as if it were MIT.
- Root key loss is unrecoverable. Backup is the human’s job; never copy `~/.minsec/server.key` or `MINSEC_ROOT_KEY` into the repo.
- Fallback until MinSec is armed: existing `.private/*.env` files, still cursorignored, never pasted.
