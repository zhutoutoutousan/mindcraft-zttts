---
name: local-tasks
description: >-
  Bidirectional task queue system between Cloud Agent and local Cursor instance.
  Cloud Agent creates tasks that require local execution (e.g., sending emails via
  local Outlook, accessing local files), stores them with full context in .private/
  and R2. Local Cursor instance pulls tasks, executes them, and syncs results back.
  Use when Cloud Agent cannot perform an action due to network/environment restrictions.
---

# Local Tasks - Cloud ↔ Local Task Queue

**Purpose**: Bridge Cloud Agent limitations (SMTP blocked, no GUI) with local machine capabilities (email clients, file access, browsers).

## Workflow

### 1. **Cloud Agent** creates local task:
```bash
python3 .cursor/skills/local-tasks/create_task.py \
  --id "send-superfit-emails" \
  --type "email_send" \
  --priority "high" \
  --context "SuperFit außerordentliche Kündigung für beide Personen"
```

Task is saved to:
- `.private/local-tasks/queue/<task-id>.json` (local)
- `dot-private/mindcraft-zttts/local-tasks/queue/<task-id>.json` (R2)

### 2. **Local Cursor** pulls and executes:
```bash
# On local machine (Windows/macOS)
python .cursor/skills/local-tasks/pull_and_execute.py
```

Pulls tasks from R2, executes locally, marks complete.

### 3. **Sync results** back to Cloud:
Results uploaded to R2, Cloud Agent can check status.

## Task Structure

```json
{
  "id": "send-superfit-emails-20261101",
  "type": "email_send",
  "status": "pending",
  "priority": "high",
  "created_at": "2026-11-01T01:30:00+03:00",
  "created_by": "cloud-agent",
  "context": {
    "description": "Send SuperFit cancellation emails with PDF attachments",
    "details": "Both Tian Shao and Yushu Qin need to submit PDF documents...",
    "background": "SuperFit requires PDF format, previous text submissions rejected"
  },
  "payload": {
    "emails": [
      {
        "from": "tian.shao@namelos.xyz",
        "to": ["member@superfit.club"],
        "cc": ["175112137@qq.com"],
        "subject": "Nachreichung Unterlagen im PDF-Format – Mitglied 7-7057051",
        "body": "...",
        "attachments": [
          {
            "name": "Abmeldebestatigung-Yushu-Qin.pdf",
            "r2_path": "dot-private/mindcraft-zttts/melde/...",
            "local_fallback": "D:/downloads/..."
          }
        ]
      }
    ],
    "smtp_config": {
      "method": "webmail_or_outlook",
      "host": "smtp.secureserver.net",
      "port": 587
    }
  },
  "execution": {
    "executed_at": null,
    "executed_by": null,
    "result": null,
    "logs": []
  }
}
```

## Task Types

- `email_send`: Send email via local client
- `file_access`: Access local files not on R2
- `browser_action`: Perform browser-based action (form submission, etc.)
- `gui_action`: Interact with GUI applications
- `manual_review`: Human review required with context

## Scripts

### Cloud Agent:
- `create_task.py` - Create new local task
- `check_status.py` - Check task execution status
- `sync_from_r2.py` - Pull completed tasks

### Local Cursor:
- `pull_and_execute.py` - Main executor
- `sync_to_r2.py` - Upload results
- `task_handlers/` - Specific handlers per task type

## Storage

### Local (.private/local-tasks/):
```
.private/local-tasks/
├── queue/           # Pending tasks
├── in-progress/     # Currently executing
├── completed/       # Done tasks
└── failed/          # Failed tasks with logs
```

### R2 (dot-private/mindcraft-zttts/local-tasks/):
Mirror of local structure, synced bidirectionally.

## Security

- SMTP credentials stay in `.private/` (never in task JSON)
- Local Cursor reads credentials from local `.private/imap-triage.env`
- Sensitive data in `context.private_notes` (not synced to public workspace)

## Never

- Execute tasks without user review (unless auto-approved task type)
- Send emails without confirming attachments are attached
- Sync `.private/` credentials to R2 (only task metadata)
