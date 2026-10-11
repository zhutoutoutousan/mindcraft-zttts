---
name: inventory-mgmt
description: Manages the private household inventory (fridge, pantry, drinks) in .private/inventory.toon.md. Use when the human photographs fridge/pantry contents, asks what is in the Kühlschrank, tracks MHD/expiry, consume-first order, restock lists, or opens/closes inventory Hausaufgaben.
---

# Household inventory

Reads and writes `.private/inventory.toon.md`. That store is the single source of truth for food and household stock. The skill and this file stay generic: no brands, items, places, or particulars baked in here.

## Store contract

- `zones[]` → `items[]` with `id`, `label`, `qty`, `unit`, `opened` (true|false|unknown), `bestBefore` (ISO date or null), `certainty` (read|guess), `note`.
- `homework[]` with `id`, `text`, `due` (ISO date or `recurring`), `status` (open|done).
- Unknown facts stay null plus a Hausaufgabe to verify them. Never invent MHD, brands, or contents from a blurry photo — `certainty: guess` + `note` what to check.

## Workflow

1. Human sends photos → append one item per visible product, grouped by zone (compartment, door shelf, freezer…). Mark everything unreadable as guess.
2. Write Hausaufgaben for every open fact: read the MHD, identify unclear packages, photograph the remaining shelves, apply consume-first.
3. Status on ask: expired, expiring within N days (`--days`, default 3), items without MHD, open homework.
4. When the human reports consumption or reads a date, update the store (`set`, `done`). Consume-first = ascending MHD, oldest first.
5. Restock list = items at qty 0 or expired; offer it before the next shopping trip.

## Commands

Run from repo root.

```
python .cursor/skills/inventory-mgmt/scripts/inventory.py status [--days N]
python .cursor/skills/inventory-mgmt/scripts/inventory.py homework
python .cursor/skills/inventory-mgmt/scripts/inventory.py done --id <homework-id>
python .cursor/skills/inventory-mgmt/scripts/inventory.py set --id <item-id> [--bb YYYY-MM-DD] [--label TEXT] [--opened true|false|unknown] [--certainty read|guess] [--qty N] [--note TEXT]
python .cursor/skills/inventory-mgmt/scripts/inventory.py add --zone <zone-id> --label TEXT [--qty 1] [--unit TEXT] [--bb DATE]
```

Needs PyYAML. Dates ISO `YYYY-MM-DD`. `hw` prefix is convention, not enforced.

## Privacy

- Inventory particulars never leave `.private/` (gitignored). Do not copy item lists into `CPU.md`, `inflow/`, `schedule/`, or `pedagogy/`.
- Never write brands, quantities, or household facts into this skill, its script, or any tmp deliverable template.
- Food photos are the human's own; describe them into the store only. No third parties, no delivery addresses in notes.
