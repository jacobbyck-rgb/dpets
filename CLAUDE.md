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
payment risk (paying vendor off-quote, unpaid new customer).
Damage: get the warehouse's disposal rate right away. If an hour passes with no answer, reach Danielle. Never tell the customer we'll dispose; report the damage and ask how they want it handled (dispose, back on the truck, salvage).
