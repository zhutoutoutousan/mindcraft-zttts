# Auto .private/ Sync from R2

Automatically downloads `.private/` files from R2 storage when they're missing in the Cloud Agent workspace.

## How it works

1. **Trigger**: When user asks for E-Mail triage, life-queue, or any private data
2. **Check**: Agent detects `.private/` is missing or empty
3. **Auto-download**: Runs `sync_from_r2.py` using R2 credentials from Cursor Cloud Secrets
4. **Continue**: Proceeds with original request

## Setup

1. **Add R2 credentials to Cursor Cloud Secrets**:
   - `STORAGE_ENDPOINT` (e.g., `https://your-account.r2.cloudflarestorage.com`)
   - `STORAGE_ACCESS_KEY`
   - `STORAGE_SECRET_KEY`
   - `STORAGE_BUCKET_PRIVATE`

2. **Upload .private/ to R2** with prefix `dot-private/mindcraft-zttts/`:
   ```bash
   # Example: Upload local .private/ to R2
   aws s3 sync D:\mindcraft-zttts\.private\ s3://your-bucket/dot-private/mindcraft-zttts/ \
     --endpoint-url https://your-account.r2.cloudflarestorage.com
   ```

3. **Use the skill**: Agent automatically syncs when needed

## Manual sync

```bash
cd /workspace
python3 .cursor/skills/auto-private-sync/sync_from_r2.py
```

## Files synced

- `imap-triage.env` - IMAP credentials for email triage
- `imap-gmail.env` - Gmail IMAP credentials
- `imap-triage.rules.json` - Email routing rules
- `life-queue.fu.md` - Private life tasks (Ausländerbehörde, etc.)
- `CPU.md` - Private CPU queue
- `reisen/` - Travel documents and confirmations
- All other files under `dot-private/mindcraft-zttts/`

## Privacy

- Files are gitignored (`.private/` in `.gitignore`)
- Credentials never appear in chat
- IMAP passwords stored in `.private/*.env` only

## Integration with other skills

- `imap-mail-triage`: Uses `.private/imap-triage.env`
- Daily brief, life queue, etc.: Use `.private/*.fu.md`
