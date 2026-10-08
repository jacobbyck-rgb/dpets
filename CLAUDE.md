# Diamond Pet Foods playbook

Live page: https://claude.ai/artifact/YRsSGGsJxgZNavYAWCbgQn (shared db: `orders`, `warehouses`, `rhythm`).

## When Jacob sends an update (email, Slack, screenshot, PDF)

Update the live board right away, without being asked, using ArtifactData on the URL above:

- Read the order first (`get orders/WN-#####`) and pin writes with `if_version`.
- Change every field the update touches: `stage` (+ `stageSince` = today when the stage moves),
  `masterPo` (on every order it covers), `group`, `apptDate`/`apptTime`/`conf`, `pallets`/`skus`/`qty`,
  `wh`, `payer`, quote counts (`qHandled`, `qReworked`, `qDisposed`), `closeout` ticks, `nextNote`.
- Append what happened, dated, to `notes`. Don't drop earlier notes.
- New WN# → create `orders/WN-#####` with the same fields the page uses (`wn`, `po`, depot fields from the PO, `wh`, `stage`, `stageSince`, `closeout: {}`, `created`).
- Then tell Jacob what changed per WN# and what's next, and draft any reply/email he needs to send.

## After changing the page itself

`python3 tools/build.py <Diamond xlsx>` → test → commit/push → refresh `snapshot/` (ArtifactData list, out_dir) →
publish `diamond-playbook.html` to the URL above → send the download and include the live link.

Quotes, the warehouse and the customer live in the WarehouseNow web app (Quotes tab); the board mirrors them.
Carrier pays → the Load # in the app must be changed to the carrier. Track `payer` and `payerOk` on the board.

New emails in Front (ADW ticket etc.): Compose new, tag with the WN#, add to the Diamond Pet mailbox (diamondpet@warehousenow.com).

Keep Diamond paperwork (PDFs, BOLs, stickers, photos) out of git.

## Order Study Board (non-Diamond orders)

Jacob's learning dashboard: https://claude.ai/artifact/5ztuUc4ZjBSe7T3NyATScu (shared db: `orders`, `processes`,
`rules`, `warehouses`, `terms`, `questions`). Older doc version: https://claude.ai/code/artifact/9a623705-28c1-4927-bd83-60d160f585ba
When he says "study WN-#####", read its Slack channel (`#<WN#>-city-st-service-customer-region`) start to finish, then with ArtifactData:
- `orders/<wn>`: wn, customer, customerType, service, temp, city, region, pallets, warehouse, cost, billed, cycle,
  outcome (clean|rough|failed|open), date, slack, summary, timeline [{when,text}], wentRight [], improve [].
- New rules → `rules/rNN` {text, why, wn, topic, date}; warehouses → `warehouses/<slug>` {name, location, region, temp,
  contact, rates, hours, rating (go-to|ok|watch|no cap|avoid), notes, orders []}; terms → `terms/<slug>` {term, meaning,
  group}; questions → `questions/qNN` {text, from, done:false, answer:"", date}.
- New service type → `processes/<slug>` {name, summary, steps [{title,text}], differs, learnedFrom []}; else add the WN# to learnedFrom.
- Photos ("Read the Load" tab): pull load photos from the order's Slack channel (slack_read_file), downscale to <=1400px,
  upload with Artifact `asset: true`, then `photos/pNN` {asset (id), wn, order, title, stage, verdict (bad|good|fixed|doc),
  defects [defect ids], spots [{x%, y%, label}] placed on what to notice, lesson, quiz {question, options[], answer (index), why}}.
  Defect field guide lives in `defects/<id>` (id = drawing: good, lean, collapsed, wrapshort, sideways, overhang, crushed,
  broken, gaps, wet, seal); add the WN# to `seenOn` when an order shows it. Photos are Diamond-free customer data: never commit them.
Read before writing and pin with `if_version`; never drop existing rows (questions hold Jacob's answers).
Team flow: load board/Front → QB (channel + fast reply) → Coverage (warehouse bids, cx quote) → account owner (approval, app) → Ops (warehouse, driver, pics, cx updates) → Accounting (final costs, invoice).

## Escalate to Danielle (Jacob's boss) — flag it every time
When any update shows one of these, start the reply with "⚠️ Loop in Danielle" plus a 2-line Slack draft to her:
scope change (more pallets/hours/new service) · vendor price change after approval or margin near $0/negative ·
customer complaint, time/billing dispute or discount ask · service failure (crew short/no-show, driver left, not finished, rejected) ·
damage, disposal, temp loss or possible claim · safety (customer driver doing labor, PPE, injury) · timeline we told the customer slips ·
payment risk (paying vendor off-quote, unpaid new customer). · anything Jacob hasn't handled before.
Damage: get the warehouse's disposal rate right away. If an hour passes with no answer, reach Danielle. Never tell the customer we'll dispose; report the damage and ask how they want it handled (dispose, back on the truck, salvage).

## Account Expansion Map (repeat non-Diamond accounts)
https://claude.ai/artifact/XtMP875zicgpcVqSjMsvW3 (shared db: `companies/<key>` with locations[] + contacts[] (ids like `cre-l03`, `cre-c02`),
`track/<rowId>` {status, notes, at} written by the page). Accounts: cre, mvt, bison, transloop, arrive, artur, pace, giltner, backhaul.
New contact/location from an order → read the company doc, append with the next id, write with `if_version`. Never overwrite `track`.

## Drafting Slack posts
Tag @ops-west / @coverage only when they must act; never "for vis" on finished actions (each tag adds an Ops task).
Warehouse cost changes → tag Sebastian (Coverage). Sign a COD before sending it.
Driver paid the warehouse directly → don't bill the customer on top (it exposes margin); hand to Danielle.

## Load Situations Playbook (lessons from 81 non-Diamond orders)
https://claude.ai/artifact/FDpopwcSroSLFid1S6xbA8 — cases by stage, Jacob's "don't repeat" list, checklists, quiz.
When drafting or advising, watch for these repeats and call them out:
- Intake: confirm truck location; read BOL temp (app often says dry); who pays → change customer in app; ask load/PO # early.
- Quote: per pallet with est. count (no unknown-count all-in); $350 min for 1–3 pallets; OT/weekend fee; never warehouse rates in cx quote; don't cut Coverage's price; name city/warehouse/work day/pickup day.
- Approval: written yes → post "approved" in channel + move to Approved in app. Driver is not the customer.
- Before arrival: driver name/phone/ETA to whs, whs confirms back, send SOP (no driver payment, wrap to pallet, 2 load bars, seal, photos), written pallet cap.
- Close: seal photo before driver leaves; vendor invoice in writing vs quote (tag Coverage); final = units×rate; COD signed and sent before complete; green complete before invoice; check invoice total + bill-to.
- New customer: collect payment before release. Reply to cx emails within 10 min. G only for escalations; after 4 PM CT tag night ops.
Reminders tab (same artifact, db `reminders/<trigger id>` {title, wn, detail, when ISO, recurring, status open|done|cancelled, source claude|jacob}):
every time a reminder is created (send_later/create_trigger) add its row; when cancelled set status "cancelled"; when one fires and is handled set "done".
Morning lesson routine: trig_01JpB5CJAfniuX37rMs6nCHf (weekdays 6:53 CT), progress in study board `meta/lessons`.
Coaching ("How they want it done", same artifact, db `coaching/<id>` {who, date, wn, quote, rule, topic}): any correction or "moving forward"
from Genderson/Danielle/Sam/team → add a row right away and follow it in every draft. G (10/7): tag only when they must act; no tags after
an email/action is done. G (10/6): don't tag him on things already learned (master POs) — only new parts.
Top coaching to apply in drafts: ask G in the order channel not DM; G only for escalations/new stuff (whs questions → Ops/coverer);
tag one person; never paste whs messages/PDFs to cx or Diamond (filter; POD/sticker only); answer the email even after a text
("per our conversation"); real dates not "this day"; vendor bill over quote → Johan before paying, invoice in writing; check every invoice yourself.
MAIN HUB = Load Situations Playbook (Jacob prefers it over the study board). `orders/<wn>` there {wn, customer, city, state, service, region,
slack (channel name), slackUrl (https://warehousenowhq.slack.com/archives/<channel id>), status active|closed, diamond, cases, summary, updated}:
add each new order channel; set status closed when the channel is archived; bump `cases` when a case is added. Studied orders still go to the study board too.
Freight Floor Basics (https://claude.ai/artifact/SU5ah9fxgfLPGqAHGMoVVJ, scratchpad freight-101.html, static): keep updating — new term,
load type or situation from an order → add it there and republish.
