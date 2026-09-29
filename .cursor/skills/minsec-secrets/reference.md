# MinSec — vendor map

Upstream, not audited here.

| | |
| --- | --- |
| GitHub | https://github.com/cgx9/minsec |
| npm | https://www.npmjs.com/package/minsec (`minsec`, 1.0.x) |
| Install | `npm i -g minsec` |
| Local server | `minsec server` → dashboard `http://localhost:9876/` |
| Edge | `minsec deploy cloudflare` (Workers + D1). Needs `npx wrangler login` |
| Run | `minsec run -- <command>` injects into the child process env |
| Linkage | `.minsec` in the project root (empty `endpoint`/`apiKey` inherit `~/.minsec/`) |

## What stays in mindcraft

| Kind | Path |
| --- | --- |
| Example linkage (no tokens) | `.cursor/skills/minsec-secrets/minsec.example.json` |
| IMAP template (empty password) | `.cursor/skills/imap-mail-triage/env.example` |
| Live IMAP until migrated | `.private/imap-triage.env` (gitignored + cursorignored) |
| Agent index denylist | `.cursorignore` |

`triage.py` already skips dotenv keys that are already in `os.environ`, so `minsec run -- python …/triage.py` works. Zero-disk only after the `.env` file is gone.

## Caveats

- **Root key**: `~/.minsec/server.key` or Cloudflare `MINSEC_ROOT_KEY`. Lose it → ciphertext is gone.
- **License**: Non-Commercial Open Source (MinSec 1.0). Personal / study / non-profit free; commercial use needs author authorization.
- **Threat model**: stops workspace scanners from reading a plaintext `.env`. It does not stop a process dump, a malicious skill, pasting a secret into chat, or **AgentTty** (`minsec list` / env dumps in the agent terminal). Java apps must use `System.getenv`, not `System.getProperty` (**JavaProcessEnv**).
