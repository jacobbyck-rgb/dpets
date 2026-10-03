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
Carrier pays → the Load # in the app must be changed to the carrier. Track `payer`, `payerOk`, `loadNo` on the board.

Keep Diamond paperwork (PDFs, BOLs, stickers, photos) out of git.
