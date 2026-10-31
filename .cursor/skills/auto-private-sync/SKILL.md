---
name: auto-private-sync
description: >-
  Automatically downloads .private/ files from R2 storage when they are missing
  in the workspace. Triggered when user asks to process emails, check life-queue,
  or access any .private data. Use when the agent detects .private/ does not exist
  or is empty, and R2 credentials (STORAGE_*) are available.
---

# Auto .private/ Sync from R2

**Trigger**: When `.private/` directory is missing or empty in workspace, and user requests:
- E-Mail-Triage / IMAP processing / "处理邮件" / "整理邮件"
- Life queue / Ausländerbehörde / Ausreise / China travel
- Any private data access (CPU.md, life-queue.fu.md, nutrition.toon.md, etc.)

## Auto-sync workflow

1. **Check**: Does `/workspace/.private/` exist and contain files?
   ```bash
   [ -d /workspace/.private ] && [ "$(ls -A /workspace/.private 2>/dev/null)" ]
   ```

2. **If missing or empty**: Download from R2 automatically
   ```bash
   python3 /workspace/.cursor/skills/auto-private-sync/sync_from_r2.py
   ```

3. **Continue**: Proceed with the original user request

## Never

- Ask user permission to download (just do it when R2 creds exist)
- Download if `.private/` already has files (check first)
- Fail silently; report download errors clearly

## Files downloaded

Priority files for common tasks:
- `imap-triage.env` + `imap-triage.rules.json` (E-Mail)
- `life-queue.fu.md` (Ausländerbehörde, Ausreise)
- `CPU.md` (private CPU queue)
- `imap-gmail.env` (Gmail access)
- Travel files: `reisen/*.txt`, `reisen/*.eml`

Full sync downloads entire `dot-private/mindcraft-zttts/` prefix from R2.

## Dependencies

- R2 credentials: `STORAGE_ENDPOINT`, `STORAGE_ACCESS_KEY`, `STORAGE_SECRET_KEY`, `STORAGE_BUCKET_PRIVATE`
- boto3 (install if missing: `pip3 install boto3`)
- Script: `.cursor/skills/auto-private-sync/sync_from_r2.py`

## After sync

- Run the user's original request (e.g., IMAP triage, life-queue check)
- Do NOT narrate "I downloaded files" unless download failed
- Just proceed as if `.private/` was always there
