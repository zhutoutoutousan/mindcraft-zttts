---
name: jd-market
description: >-
  Collects job descriptions from LinkedIn Easy Apply and BOSS直聘 (including
  zhipin.com/overseas 驻外), then writes where each industry is moving and where
  it intersects this person's real stack. Use when the human names JD, 职位描述,
  行业, 市场动向, 交集, 驻外, overseas, or when a card is read or an application
  is sent. File every card. Do not invent a market.
---

# JD market

Read a card, file it, then keep going with the application or the diligence. A market note is a separate product. It is written when the human asks for 行业 or 市场动向, or when [corpus.md](corpus.md) has grown by 10 rows since the last note.

Send rules stay in [boss-zhipin-diligence](../boss-zhipin-diligence/SKILL.md). Answer floors and the intersection axes are in [reference.md](reference.md). Sent or not-sent stays in `.private/job-bewerbungen.fu.md`. No phone, WeChat id, mailbox password, or IBAN in any of these files.

## File a card

Append one row to [corpus.md](corpus.md) the same day the card is read. Skip a duplicate job id. A recruiter repost of the same body is still a new id; mark it `mill` if the body is the Hire Feed / Quik Hire / Hired template.

```
### YYYY-MM-DD · channel · job id · sent|skipped|read
- company:
- role:
- where: remote or 驻外, city, language the card names
- asked: skills and years the card requires
- intersection: only axes from reference.md that the card actually uses
- gap: requirements that are outside those axes
- signal: one sentence on what this card says about the lane
```

Quote the card. Do not upgrade a "plus" into a requirement, and do not turn a skipped card into a trend.

## Market note

Write `notes/YYYY-MM-DD.md` from corpus rows only. Group by lane, not by company. Each lane gets three lines: what the cards are asking, where that touches the axes, what was refused and why. If a lane has one card, say one card. Do not borrow salaries, headcount, or "the market is" from outside the corpus.

Lanes to keep separate:

- China remote software
- Europe remote software
- Europe remote that asks for Mandarin or Chinese
- BOSS 驻外 (on-site abroad, not remote)
- Recruiter mills

## While applying

On a LinkedIn or BOSS pass, file the card before the next search. LinkedIn passes use AI job search. China remote uses the Chinese resume. Europe remote uses the German resume. 驻外 is not a remote application. Login walls get a corpus row `read` with `signal: list hidden until login`, not a guessed job list.
