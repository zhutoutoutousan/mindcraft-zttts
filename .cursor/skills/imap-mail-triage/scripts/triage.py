#!/usr/bin/env python3
"""IMAP header triage. Rules first, optional LLM leftover. Never SMTP.

    python .cursor/skills/imap-mail-triage/scripts/triage.py --list-folders
    python .cursor/skills/imap-mail-triage/scripts/triage.py --dry-run --limit 50
    python .cursor/skills/imap-mail-triage/scripts/triage.py --apply --unseen
"""
from __future__ import annotations

import argparse
import imaplib
import json
import os
import re
import ssl
import sys
from datetime import date
from email.header import decode_header, make_header
from email.message import Message
from email.parser import BytesParser
from email.policy import default as email_policy
from pathlib import Path
from urllib import error, request

ROOT = Path(__file__).resolve().parents[4]
SKILL = Path(__file__).resolve().parent.parent
PRIVATE_ENV = ROOT / ".private" / "imap-triage.env"
PRIVATE_RULES = ROOT / ".private" / "imap-triage.rules.json"
EXAMPLE_RULES = Path(__file__).resolve().parent / "rules.example.json"
DIGEST_DIR = ROOT / "tmp" / "imap-triage"


def load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def hdr(msg: Message, name: str) -> str:
    raw = msg.get(name, "") or ""
    try:
        return str(make_header(decode_header(raw))).replace("\n", " ").strip()
    except Exception:
        return raw.replace("\n", " ").strip()


def domain_of(from_hdr: str) -> str:
    m = re.search(r"@([A-Za-z0-9.-]+)", from_hdr)
    return (m.group(1) if m else "").lower().rstrip(".")


def load_rules(path: Path | None) -> dict:
    src = path or (PRIVATE_RULES if PRIVATE_RULES.is_file() else EXAMPLE_RULES)
    data = json.loads(src.read_text(encoding="utf-8"))
    data["_src"] = str(src)
    return data


AUTOMATED = (
    "noreply",
    "no-reply",
    "no_reply",
    "donotreply",
    "do-not-reply",
    "newsletter",
    "notifications@",
    "mailer-daemon",
    "jobs-noreply",
    "invitations@",
    "messages-",
    "em.linkedin",
    "e.linkedin",
    "inmail",
)


def looks_like_person(from_hdr: str) -> bool:
    low = from_hdr.lower()
    if any(tok in low for tok in AUTOMATED):
        return False
    head = from_hdr.split("<", 1)[0].strip().strip('"')
    parts = [p for p in re.split(r"[\s,]+", head) if p and p.lower() not in {"me", "via"}]
    words = [p for p in parts if re.match(r"^[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ'.-]+$", p)]
    if len(words) < 2:
        return False
    if words[-1].lower() in {
        "tutorials",
        "team",
        "official",
        "news",
        "newsletter",
        "support",
        "info",
        "mail",
        "gmbh",
        "ltd",
        "inc",
        "ag",
        "kg",
    }:
        return False
    m = re.search(r"<([^@>]+)@", from_hdr)
    local = (m.group(1) if m else "").lower()
    if local in {
        "info",
        "hello",
        "news",
        "newsletter",
        "support",
        "team",
        "mail",
        "service",
        "marketing",
        "noreply",
        "no-reply",
        "contact",
        "cs",
    }:
        return False
    return True


def needle_in(hay: str, needle: str) -> bool:
    """Substring match; short alnum tokens use word edges so PIN ≠ opinion."""
    n = needle.lower()
    if len(n) <= 4 and n.isalnum():
        return bool(re.search(rf"(?<![a-z0-9äöüß]){re.escape(n)}(?![a-z0-9äöüß])", hay))
    return n in hay


def match_rule(from_hdr: str, subject: str, rules: list[dict]) -> dict | None:
    from_l = from_hdr.lower()
    sub_l = subject.lower()
    dom = domain_of(from_hdr)
    for rule in rules:
        domains = [d.lower().lstrip("@") for d in rule.get("from_domain") or []]
        if domains and not any(dom == d or dom.endswith("." + d) for d in domains):
            continue
        contains = [c.lower() for c in rule.get("from_contains") or []]
        if contains and not any(c in from_l for c in contains):
            continue
        blocked = [c.lower() for c in rule.get("from_not_contains") or []]
        if blocked and any(c in from_l for c in blocked):
            continue
        subjects = [s.lower() for s in rule.get("subject_contains") or []]
        if subjects and not any(needle_in(sub_l, s) for s in subjects):
            continue
        if rule.get("person_from") and not looks_like_person(from_hdr):
            continue
        folder = (rule.get("folder") or "").strip()
        if not folder:
            continue
        if domains or contains or subjects or rule.get("person_from"):
            return rule
    return None


ABOUT_ME = re.compile(
    r"bewerbung|your application|job application|interview|kennenlern|"
    r"vorstellungsgespr|freelance projekt|endkunden|"
    r"面试|投递|应徵|应聘|简历|录用|笔试|面试邀请|对您很感兴趣|"
    r"thank you for applying|we received your application|"
    r"candidate profile|applicant privacy|headhunt|"
    r"job offer|employment contract|coding challenge|"
    r"recruiter|talent acquisition",
    re.I,
)

RECRUITER_LOCAL = (
    "recruiter@",
    "careers@",
    "talent@",
    "hiring@",
    "jobs@",
    "people@",
    "humanresources",
    "hr@",
)


def about_human(from_hdr: str, subject: str) -> bool:
    """Likely needs Todo: 1:1, application, interview. Not newsletters."""
    low_from = from_hdr.lower()
    if any(
        tok in low_from
        for tok in ("newsletter", "maz-online", "indeed.com", "kleinanzeigen", "substack.com")
    ):
        return False
    if looks_like_person(from_hdr):
        return True
    if ABOUT_ME.search(subject or ""):
        return True
    if any(tok in low_from for tok in RECRUITER_LOCAL):
        return True
    return False


def llm_folder(from_hdr: str, subject: str, folders: list[str]) -> str | None:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        return None
    base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
    allowed = [f for f in folders if f.upper() not in {"INBOX", "SENT", "TRASH", "DRAFTS", "SPAM"}]
    payload = {
        "model": model,
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Pick exactly one mailbox folder for this email. "
                    "Reply with JSON {\"folder\":\"...\"} only. "
                    "If unsure use INBOX. Never invent a folder name."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(
                    {"from": from_hdr, "subject": subject, "folders": allowed},
                    ensure_ascii=False,
                ),
            },
        ],
    }
    req = request.Request(
        f"{base}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except error.URLError:
        return None
    text = (((body.get("choices") or [{}])[0].get("message") or {}).get("content") or "").strip()
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        folder = str(json.loads(m.group(0)).get("folder") or "").strip()
    except json.JSONDecodeError:
        return None
    if folder in allowed or folder == "INBOX":
        return folder
    return None


def connect() -> imaplib.IMAP4_SSL:
    host = os.environ.get("IMAP_HOST", "imap.secureserver.net")
    port = int(os.environ.get("IMAP_PORT", "993"))
    user = os.environ.get("IMAP_USER", "").strip()
    password = os.environ.get("IMAP_PASSWORD", "")
    if not user or not password:
        raise SystemExit(
            "Missing IMAP_USER / IMAP_PASSWORD. Copy .private/imap-triage.env from the skill."
        )
    if "legal@" in user.lower():
        raise SystemExit("Refuse: legal mailbox is human-only.")
    ctx = ssl.create_default_context()
    client = imaplib.IMAP4_SSL(host, port, ssl_context=ctx)
    try:
        client.login(user, password)
    except imaplib.IMAP4.error as exc:
        raise SystemExit(
            f"IMAP login failed on {host}: {exc}. "
            "GoDaddy Titan uses imap.secureserver.net; native Titan uses imap.titan.email."
        ) from exc
    return client


def list_folders(client: imaplib.IMAP4_SSL) -> list[str]:
    typ, rows = client.list()
    if typ != "OK" or not rows:
        return []
    names: list[str] = []
    for raw in rows:
        if not raw:
            continue
        line = raw.decode("utf-8", "replace") if isinstance(raw, (bytes, bytearray)) else str(raw)
        m = re.search(r'"([^"]*)"\s*$', line) or re.search(r"\s(\S+)$", line)
        if m:
            names.append(m.group(1))
    return names


def quote_mbox(name: str) -> str:
    return '"' + name.replace("\\", "\\\\").replace('"', '\\"') + '"'


def ensure_folder(client: imaplib.IMAP4_SSL, name: str, existing: set[str]) -> None:
    if name in existing or not name or name.upper() == "INBOX":
        return
    typ, _ = client.create(quote_mbox(name))
    if typ == "OK":
        existing.add(name)
        return
    # Already exists under another encoding.
    existing.add(name)


def uid_headers(client: imaplib.IMAP4_SSL, uid: bytes) -> Message:
    typ, data = client.uid(
        "FETCH",
        uid,
        "(BODY.PEEK[HEADER.FIELDS (FROM TO SUBJECT DATE)])",
    )
    if typ != "OK" or not data:
        raise RuntimeError(f"FETCH failed for uid {uid!r}")
    blob = b""
    for part in data:
        if isinstance(part, tuple) and len(part) >= 2 and isinstance(part[1], (bytes, bytearray)):
            blob = part[1]
            break
    return BytesParser(policy=email_policy).parsebytes(blob)


def move_uid(client: imaplib.IMAP4_SSL, uid: bytes, folder: str) -> None:
    dest = quote_mbox(folder)
    typ, _ = client.uid("MOVE", uid, dest)
    if typ == "OK":
        return
    typ, _ = client.uid("COPY", uid, dest)
    if typ != "OK":
        raise RuntimeError(f"COPY to {folder} failed")
    client.uid("STORE", uid, "+FLAGS", r"(\Deleted)")


def xfer_all(client: imaplib.IMAP4_SSL, src: str, dst: str, limit: int) -> int:
    typ, _ = client.select(quote_mbox(src))
    if typ != "OK":
        raise SystemExit(f"Cannot select {src}")
    typ, data = client.uid("SEARCH", None, "ALL")
    if typ != "OK":
        raise SystemExit("SEARCH failed")
    uids = [u for u in (data[0] or b"").split() if u][:limit]
    moved = 0
    for uid in uids:
        move_uid(client, uid, dst)
        moved += 1
    try:
        client.expunge()
    except imaplib.IMAP4.error:
        pass
    return moved


def write_digest(rows: list[dict]) -> Path:
    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    path = DIGEST_DIR / f"digest-{date.today().isoformat()}.json"
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def main() -> int:
    p = argparse.ArgumentParser(description="IMAP header triage. Never sends.")
    p.add_argument(
        "--env",
        type=Path,
        default=PRIVATE_ENV,
        help="Dotenv path. Titan stays .private/imap-triage.env; Gmail uses a second file.",
    )
    p.add_argument("--list-folders", action="store_true")
    p.add_argument("--dry-run", action="store_true", default=False)
    p.add_argument("--apply", action="store_true")
    p.add_argument("--unseen", action="store_true")
    p.add_argument("--backlog", action="store_true")
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--offset", type=int, default=0)
    p.add_argument("--llm", action="store_true")
    p.add_argument("--stats", action="store_true", help="Print From-domain counts; no MOVE")
    p.add_argument(
        "--ensure-folders",
        action="store_true",
        help="CREATE any folder named in the rules file",
    )
    p.add_argument("--mailbox", default=None, help="Override IMAP mailbox (default INBOX)")
    p.add_argument(
        "--only-folder",
        default=None,
        help="Only MOVE when the destination equals this folder (rescue Todo from Archive)",
    )
    p.add_argument(
        "--fn-scan",
        action="store_true",
        help="Scan for about-the-human false negatives and send them to Todo",
    )
    p.add_argument("--xfer", default=None, help="Move ALL messages from this folder")
    p.add_argument("--xfer-to", default=None, help="Destination for --xfer (Trash = recoverable delete)")
    p.add_argument("--default-folder", default=None, help="Override rules default_folder")
    p.add_argument("--rules", type=Path, default=None)
    args = p.parse_args()
    load_dotenv(args.env)
    if not args.list_folders and not args.apply:
        args.dry_run = True
    if args.apply:
        args.dry_run = False

    rules_doc = load_rules(args.rules)
    if args.default_folder:
        rules_doc["default_folder"] = args.default_folder
    client = connect()
    try:
        folders = list_folders(client)
        if args.list_folders:
            print("\n".join(folders) or "(no folders)")
            return 0

        if args.xfer:
            if not args.xfer_to:
                raise SystemExit("--xfer-to required")
            if not args.apply:
                raise SystemExit("--xfer needs --apply")
            existing_now = set(folders)
            ensure_folder(client, args.xfer_to, existing_now)
            n = xfer_all(client, args.xfer, args.xfer_to, args.limit)
            print(json.dumps({"ok": True, "xfer": args.xfer, "to": args.xfer_to, "moved": n}))
            return 0

        mailbox = (
            args.mailbox
            or os.environ.get("IMAP_MAILBOX")
            or rules_doc.get("mailbox")
            or "INBOX"
        )
        wanted = []
        for rule in rules_doc.get("rules") or []:
            f = (rule.get("folder") or "").strip()
            if f and f not in wanted:
                wanted.append(f)
        for extra in rules_doc.get("ensure_folders") or []:
            e = str(extra).strip()
            if e and e not in wanted:
                wanted.append(e)
        if args.ensure_folders or (args.apply and wanted):
            existing_now = set(folders)
            for name in wanted:
                ensure_folder(client, name, existing_now)
            folders = list_folders(client)

        typ, _ = client.select(quote_mbox(mailbox), readonly=args.dry_run and not args.ensure_folders)
        if typ != "OK":
            raise SystemExit(f"Cannot select {mailbox}")

        criterion = "UNSEEN" if args.unseen or not args.backlog else "ALL"
        typ, data = client.uid("SEARCH", None, criterion)
        if typ != "OK":
            raise SystemExit("SEARCH failed")
        all_uids = [u for u in (data[0] or b"").split() if u]
        newest = list(reversed(all_uids))
        uids = newest[args.offset : args.offset + args.limit]

        if args.stats:
            from collections import Counter

            counts: Counter[str] = Counter()
            samples: list[dict] = []
            for uid in uids:
                msg = uid_headers(client, uid)
                from_hdr = hdr(msg, "From")
                subject = hdr(msg, "Subject")
                dom = domain_of(from_hdr) or "(none)"
                counts[dom] += 1
                if len(samples) < 40:
                    samples.append({"from": from_hdr, "subject": subject, "domain": dom})
            DIGEST_DIR.mkdir(parents=True, exist_ok=True)
            path = DIGEST_DIR / "stats.json"
            path.write_text(
                json.dumps(
                    {
                        "ok": True,
                        "count": len(uids),
                        "domains": counts.most_common(80),
                        "sample": samples,
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            print(f"ok count={len(uids)} stats={path}")
            for dom, n in counts.most_common(40):
                print(f"{n:4d}  {dom.encode('ascii', 'replace').decode()}")
            return 0

        existing = set(folders)
        out: list[dict] = []
        for uid in uids:
            msg = uid_headers(client, uid)
            from_hdr = hdr(msg, "From")
            subject = hdr(msg, "Subject")
            if args.fn_scan:
                if about_human(from_hdr, subject):
                    folder = "Todo"
                    via = "fn-scan"
                else:
                    out.append(
                        {
                            "uid": uid.decode(),
                            "from": from_hdr,
                            "subject": subject,
                            "folder": None,
                            "via": "fn-ok",
                            "moved": False,
                        }
                    )
                    continue
            else:
                rule = match_rule(from_hdr, subject, rules_doc.get("rules") or [])
                folder = rule["folder"] if rule else None
                via = "rule" if rule else None
                if not folder and args.llm:
                    folder = llm_folder(from_hdr, subject, folders)
                    via = "llm" if folder else None
                if not folder and not args.only_folder:
                    default = (rules_doc.get("default_folder") or "").strip()
                    if default and default.upper() != mailbox.upper():
                        folder = default
                        via = "zero-inbox"
            if args.only_folder and (not folder or folder != args.only_folder):
                out.append(
                    {
                        "uid": uid.decode(),
                        "from": from_hdr,
                        "subject": subject,
                        "folder": None,
                        "via": "skip",
                        "moved": False,
                    }
                )
                continue
            if not folder or folder == mailbox:
                out.append(
                    {
                        "uid": uid.decode(),
                        "from": from_hdr,
                        "subject": subject,
                        "folder": None,
                        "via": via or "leave",
                        "moved": False,
                    }
                )
                continue
            if folder not in existing:
                out.append(
                    {
                        "uid": uid.decode(),
                        "from": from_hdr,
                        "subject": subject,
                        "folder": folder,
                        "via": via,
                        "moved": False,
                        "error": "folder missing on server",
                    }
                )
                continue
            moved = False
            if args.apply:
                move_uid(client, uid, folder)
                moved = True
            out.append(
                {
                    "uid": uid.decode(),
                    "from": from_hdr,
                    "subject": subject,
                    "folder": folder,
                    "via": via,
                    "moved": moved,
                }
            )
        if args.apply:
            try:
                client.expunge()
            except imaplib.IMAP4.error:
                pass
        digest = write_digest(out)
        moved_n = sum(1 for r in out if r.get("moved"))
        planned = sum(1 for r in out if r.get("folder") and not r.get("error"))
        inbox_n = None
        try:
            typ, data = client.status(quote_mbox(mailbox), "(MESSAGES)")
            if typ == "OK" and data:
                raw = data[0].decode() if isinstance(data[0], (bytes, bytearray)) else str(data[0])
                m = re.search(r"MESSAGES\s+(\d+)", raw)
                if m:
                    inbox_n = int(m.group(1))
        except Exception:
            inbox_n = None
        print(
            json.dumps(
                {
                    "ok": True,
                    "dry_run": args.dry_run,
                    "rules": rules_doc.get("_src"),
                    "count": len(out),
                    "planned": planned,
                    "moved": moved_n,
                    "digest": str(digest),
                    "inbox": inbox_n,
                },
                ensure_ascii=False,
            )
        )
        return 0
    finally:
        try:
            client.logout()
        except Exception:
            pass


if __name__ == "__main__":
    sys.exit(main())
