schema: self/messages
version: 1
updated: 2026-10-09T19:40:00+02:00
note: Public stub only. No given names, no contact, no health numbers. Particulars for the other project stay in .private/ (gitignored).

channel:
  askVia: other-project-chat
  partnerLive: that project's latest chat publish
  not: static checkout of the other project in this workspace
  publicRepo: true

outbound[]:
  - id: outbound-2026-10-09-cups-vs-bowl
    date: 2026-10-09
    from: this-mindcraft
    to: other-project-chat
    status: asked
    subject: Abendessen — Becher und Proteingetränk
    body: |
      Public redaction. The human said both drank the same protein drink and split the cups.
      The other project chat logged a different dinner shape the same evening.
      Ask that chat (not this public file) whether to book a 50/50 cup share without double-counting the drink.
    delivery:
      otherInboxWrite: not-from-this-env
      note: No PII in this public stub.
