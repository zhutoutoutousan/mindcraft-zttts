#!/usr/bin/env python3
"""Inventory CLI for .private/inventory.toon.md.

  status [--days N]            zones, items, expired / expiring / missing-MHD counts
  homework                     open Hausaufgaben, overdue flagged
  done --id <id>               close a Hausaufgabe
  set --id <item> [fields]     update an item (bb, label, opened, certainty, qty, note)
  add --zone <id> --label TXT  append a new item to a zone

Store is found by walking up from this script until .private/inventory.toon.md exists.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date, timedelta
from pathlib import Path

import yaml

TODAY = date.today()


def store_path() -> Path:
    for parent in Path(__file__).resolve().parents:
        candidate = parent / ".private" / "inventory.toon.md"
        if candidate.exists():
            return candidate
    sys.exit("store not found: .private/inventory.toon.md")


def load() -> dict:
    with store_path().open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def save(data: dict) -> None:
    data["updated"] = TODAY.isoformat()
    with store_path().open("w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False, width=120)


def find_item(data: dict, item_id: str):
    for zone in data.get("zones", []):
        for item in zone.get("items", []):
            if item.get("id") == item_id:
                return zone, item
    sys.exit(f"item not found: {item_id}")


def find_hw(data: dict, hw_id: str):
    for hw in data.get("homework", []):
        if hw.get("id") == hw_id:
            return hw
    sys.exit(f"homework not found: {hw_id}")


def bb_flag(item: dict, days: int):
    bb = item.get("bestBefore")
    if not bb:
        return "no-mhd"
    bb_date = date.fromisoformat(str(bb))
    if bb_date < TODAY:
        return "EXPIRED"
    if bb_date <= TODAY + timedelta(days=days):
        return "expiring"
    return "ok"


def cmd_status(args) -> None:
    data = load()
    days = args.days
    totals = {"EXPIRED": 0, "expiring": 0, "no-mhd": 0, "guess": 0}
    for zone in data.get("zones", []):
        print(f"[{zone.get('label', zone.get('id'))}]")
        for item in zone.get("items", []):
            flag = bb_flag(item, days)
            totals[flag] = totals.get(flag, 0) + 1
            if item.get("certainty") == "guess":
                totals["guess"] = totals.get("guess", 0) + 1
            parts = [f"  {item.get('id')}", f"{item.get('qty')}x {item.get('unit', '?')}",
                     item.get("label", "?")]
            if item.get("bestBefore"):
                parts.append(f"MHD {item['bestBefore']}")
            parts.append(flag)
            if item.get("certainty") == "guess":
                parts.append("(guess)")
            print("  ".join(parts))
    print(f"-- expired {totals['EXPIRED']} | expiring<={days}d {totals['expiring']} "
          f"| no-MHD {totals['no-mhd']} | guess {totals['guess']}")


def cmd_homework(args) -> None:
    data = load()
    for hw in data.get("homework", []):
        if hw.get("status") != "open":
            continue
        due = str(hw.get("due", ""))
        overdue = due not in ("recurring", "") and date.fromisoformat(due) < TODAY
        mark = "OVERDUE" if overdue else due
        print(f"{hw.get('id')}  due={mark}  {hw.get('text')}")


def cmd_done(args) -> None:
    data = load()
    hw = find_hw(data, args.id)
    hw["status"] = "done"
    hw["doneDate"] = TODAY.isoformat()
    save(data)
    print(f"done: {args.id}")


def cmd_set(args) -> None:
    data = load()
    _, item = find_item(data, args.id)
    for key, value in (("label", args.label), ("bestBefore", args.bb),
                       ("opened", args.opened), ("certainty", args.certainty),
                       ("qty", args.qty), ("note", args.note)):
        if value is not None:
            item[key] = value
    save(data)
    print(f"updated: {args.id}")


def cmd_add(args) -> None:
    data = load()
    for zone in data.get("zones", []):
        if zone.get("id") == args.zone:
            zone.setdefault("items", []).append({
                "id": args.item_id,
                "label": args.label,
                "qty": args.qty,
                "unit": args.unit,
                "opened": args.opened,
                "bestBefore": args.bb,
                "certainty": args.certainty,
                "note": args.note,
            })
            save(data)
            print(f"added: {args.item_id} -> {args.zone}")
            return
    known = ", ".join(z.get("id", "?") for z in data.get("zones", []))
    sys.exit(f"zone not found: {args.zone} (known: {known})")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_status = sub.add_parser("status")
    p_status.add_argument("--days", type=int, default=3)
    p_status.set_defaults(func=cmd_status)

    p_hw = sub.add_parser("homework")
    p_hw.set_defaults(func=cmd_homework)

    p_done = sub.add_parser("done")
    p_done.add_argument("--id", required=True)
    p_done.set_defaults(func=cmd_done)

    p_set = sub.add_parser("set")
    p_set.add_argument("--id", required=True)
    p_set.add_argument("--bb")
    p_set.add_argument("--label")
    p_set.add_argument("--opened", choices=["true", "false", "unknown"])
    p_set.add_argument("--certainty", choices=["read", "guess"])
    p_set.add_argument("--qty", type=int)
    p_set.add_argument("--note")
    p_set.set_defaults(func=cmd_set)

    p_add = sub.add_parser("add")
    p_add.add_argument("--zone", required=True)
    p_add.add_argument("--item-id", required=True)
    p_add.add_argument("--label", required=True)
    p_add.add_argument("--qty", type=float, default=1)
    p_add.add_argument("--unit", default="Stück")
    p_add.add_argument("--bb")
    p_add.add_argument("--opened", default="false",
                       choices=["true", "false", "unknown"])
    p_add.add_argument("--certainty", default="guess", choices=["read", "guess"])
    p_add.add_argument("--note")
    p_add.set_defaults(func=cmd_add)

    args = parser.parse_args()
    if hasattr(args, "opened") and args.opened in ("true", "false"):
        args.opened = args.opened == "true"
    args.func(args)


if __name__ == "__main__":
    main()
