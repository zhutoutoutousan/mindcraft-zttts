# Local Tasks - Anleitung für lokale Ausführung

## Übersicht

Dieses System ermöglicht es dem Cloud Agent, Tasks zu erstellen, die nur auf Ihrer lokalen Maschine ausgeführt werden können (z.B. E-Mail-Versand via Outlook, GUI-Aktionen, lokale Dateizugriffe).

## Für Sie: Lokale Ausführung

### 1. Prerequisites (einmalig)

```bash
# Python-Abhängigkeiten installieren
pip install boto3

# R2-Credentials in .private/storage.env speichern (falls nicht vorhanden)
# Oder: Umgebungsvariablen setzen
export STORAGE_ENDPOINT=...
export STORAGE_ACCESS_KEY=...
export STORAGE_SECRET_KEY=...
export STORAGE_BUCKET_PRIVATE=...
```

### 2. Tasks abholen und ausführen

```bash
cd D:\mindcraft-zttts  # Ihr lokales Repo

# Alle pending tasks zeigen (ohne Ausführung)
python .cursor/skills/local-tasks/pull_and_execute.py --dry-run

# Tasks ausführen
python .cursor/skills/local-tasks/pull_and_execute.py
```

### 3. Was passiert

Das Script:
1. ✅ Lädt pending tasks aus R2 herunter
2. ✅ Sortiert nach Priorität (urgent → high → normal → low)
3. ✅ Führt jeden Task aus:
   - **email_send**: Öffnet `.eml` in Ihrem Standard-E-Mail-Client (Outlook/Thunderbird) mit allen Anhängen
   - **file_access**: Liest/schreibt lokale Dateien
   - **browser_action**: Öffnet URLs oder führt Browser-Aktionen aus
   - **manual_review**: Zeigt Kontext an und wartet auf Bestätigung
4. ✅ Markiert Tasks als `completed` oder `failed`
5. ✅ Synct Ergebnisse zurück zu R2

### 4. Aktueller Task: SuperFit E-Mails

**Task-ID**: `send-superfit-emails-20261101`

**Was wird gemacht**:
- 2 E-Mails an `member@superfit.club` mit CC an `175112137@qq.com`
- Anhänge:
  - Abmeldebescheinigung (Yushu Qin / Tian Shao)
  - Pegasus Flugbuchung (PC978, 27.10.2026)

**Erwarteter Ablauf**:
1. Script erstellt `.eml`-Dateien
2. Öffnet sie in Outlook/Thunderbird
3. Sie überprüfen die E-Mails (To, CC, Subject, Body, Anhänge)
4. Sie klicken auf "Senden"
5. Script markiert Task als `completed`

## Troubleshooting

### "boto3 not installed"
```bash
pip install boto3
```

### "Missing R2 credentials"
Credentials in `.private/storage.env` speichern oder als Environment-Variablen setzen.

### E-Mail öffnet nicht automatisch
`.eml`-Datei liegt in `%TEMP%` - manuell in E-Mail-Client öffnen.

### Anhänge fehlen
Script prüft zuerst `local_fallback`-Pfade, dann R2. Falls Dateien fehlen:
```bash
# R2 sync nochmal laufen lassen
python .cursor/skills/auto-private-sync/sync_from_r2.py
```

## Für Cloud Agent

### Task erstellen

```bash
python3 .cursor/skills/local-tasks/create_task.py \
  --id "unique-task-id" \
  --type "email_send" \
  --priority "high" \
  --context "Was soll gemacht werden" \
  --payload '{"key": "value"}'
```

### Zu R2 syncen

```bash
python3 .cursor/skills/local-tasks/sync_to_r2.py
```

### Task-Status prüfen

```bash
python3 .cursor/skills/local-tasks/check_status.py --id "task-id"
```

## Sicherheit

- ✅ Credentials bleiben in `.private/` (nie in Task-JSON)
- ✅ Sensible Daten in `context.private_notes` (nicht im öffentlichen Repo)
- ✅ PII-Daten niemals in Git committen
- ✅ R2-Upload nur für Task-Metadaten und benötigte Anhänge

## Workflow-Diagramm

```
Cloud Agent (blocked SMTP)
    ↓
    [create_task.py] → Task in .private/local-tasks/queue/
    ↓
    [sync_to_r2.py] → Upload zu R2
    
    ... Cloud Agent beendet ...
    
Lokale Cursor-Instanz
    ↓
    [pull_and_execute.py] → Download von R2
    ↓
    [task_handlers/email_send.py] → .eml öffnen in Outlook
    ↓
    User sendet E-Mail manuell
    ↓
    [mark_complete] → Upload zu R2 (completed/)
```
