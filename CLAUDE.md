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

## Slack (connector)

New Diamond orders get a Slack channel from Capri (e.g. `#13135-monrovia-md-rework-diamond-pet-foods-northeast`;
some start under the carrier's name, e.g. `...-pace-logistics-...`, and get renamed). They land in Jacob's
"Diamond Pet" sidebar section. Track only NEW orders as they come in (plus the orders already on the board);
don't backfill the old channels. When Jacob says "update WN-#####", read that channel yourself and update the board.
Otherwise don't read the Slack channels by default; work from what Jacob sends. Don't draft Slack asks to the warehouse/relo team: Jacob asks in the thread himself (10/08).

## After changing the page itself

`python3 tools/build.py <Diamond xlsx>` → test → commit/push → refresh `snapshot/` (ArtifactData list, out_dir) →
publish `diamond-playbook.html` to the URL above → send the download and include the live link.

Quotes, the warehouse and the customer live in the WarehouseNow web app (Quotes tab); the board mirrors them.
Payer defaults to Diamond direct; only change it if Thomas says the carrier pays. Carrier pays → the Load # in the app must be changed to the carrier.
App Load # = the Costco PO from the email subject (asked Genderson whether it should be the master PO instead). Track `payer` and `payerOk` on the board.

New emails in Front (ADW ticket etc.): Compose new, tag with the WN#, add to the Diamond Pet mailbox (diamondpet@warehousenow.com).

Keep Diamond paperwork (PDFs, BOLs, stickers, photos) out of git.

People: Genderson = Grant = "G" (Genderson Tarazona, "Grant Tar", grant@warehousenow.com) — one person. He requests Costco portal appointments; Jacob has his own portal login as of 10/06 (G reset the password).
ADW contact by depot: Krista Davidson = NE (NJ 175 Monroe Twp, MD 1052 Frederick); Chanh Rodriguez = West (960 Mira Loma; ADW ticket emails To Crodriguez@adww.com + CShults@adww.com (Chanh also replies from crodriguez@adwsales.com), Cc diamondosd@diamondpet.com + diamondpet@warehousenow.com, from requests@); Stacy = Sumner (171) + Grey Secord (Gsecord@acosta.com) helps with Sumner PO refreshes - keep Grey on Sumner emails; Sumner + SLC depots: +/-2 day grace from the PO requested delivery date (since 7/20/26); Mark Taylor + Lida Mcghee-Rowell = Morris IL (267).
Invoice format (Mariah 10/07): customer Diamond invoice lines = $25/pallet HANDLED as ONE line (not split $12.50 in + $12.50 out), $65/pallet reworked, $400 delivery; weekends/redelivery added manually per case. App customer quotes still show $12.50/$12.50 (G) - Mariah merges them. Mariah sends invoices once an order is Complete and needs the POD; she posts vendor invoices + PODs in the WN Slack channel.
Billing rule (G, 10/06): anything the WH push & wraps counts as a full rework on our (customer) side. E.g. 5 reworked + 4 push & wrapped = bill 9 reworked pallets.
Customer bill = in/outs (unload + reload) on EVERY pallet offloaded at the WH (confirm the count with the WH; FTL 37 on the BOL = 37 in/outs) + rework pallets + delivery.
Runners Inc charges a $125 rework minimum on small loads (12598, 12840) — quote 1–2 pallet Runners jobs at the minimum.
Runners Inc emails (Shoja): always To snabavi@runnersinc.com, ops@runnersinc.com AND freddock@runnersinc.com (Frederick dock; Jacob 10/06).
Single damaged bag returned at the Costco receiver (carrier emails "DISPOSITION REQUIRED", e.g. AMX on PO 001740921500, 10/06): Anna replies with the SOP template. It never gets a WN# or Slack channel and doesn't go on the board. Optional: send ADW a ticket for it.
Every email draft for Jacob starts with To:, Cc: and Subject: lines, then the body. End with "Thank you," only - NO name (Front adds his signature; Jacob 10/07).
When telling ADW (Krista etc.) a Costco appt was requested/approved, attach the portal screenshot.
Carrier asks WarehouseNow for extra stop / out-of-route miles / detention to drop a refused pallet at our WH: that is between the carrier and Diamond, not us (Hanson 10/06). Point them to Diamond; note how fast we gave the address.
Detention / layover rule (G 10/06): WarehouseNow pays ONLY when (1) we take more than 2 hours from the OS&D report to give the WH address AND get the driver offloaded, or (2) we fail to provide a WH in a timely manner. Otherwise no.
Account strategy (G 10/06, Hanson aware): Diamond is thin-margin on purpose. $400 deliveries are hard to hit (fuel); we comp the gap from the rework spread, and on 1-pallet jobs we usually eat it. We keep it for name/reputation and visibility to Costco, Sam's and Chewy contacts. So capitalize on every new logo/contact (carriers, brokers, DC/receiving people): intro call, try to get them to send us reworks. When a new company/contact shows up on an order, flag it to Jacob as a lead.
Chewy scheduling portal: NEVER submit a new/modify request to update a pending one. Every submission restarts Chewy's 48-hour response clock (Thomas 10/06, 13088). Wait for the answer on the original ref; add carrier info only by replying to Chewy's response, or ask Thomas to push.
Chewy AVP1 (Wilkes-Barre PA) redeliveries: offer them to CoreX Gress first (Glenn Gress Jr. ggress@corexgress.com 570-914-9276, Al Mackarey amackarey@corexgress.com; SCAC CQBY, DOT 3476018; did 13088 for $500). Glenn 10/07: they run drivers to/from a nearby customer often and want every future load into that Chewy.
Chewy FC codes are easy to mix up (AVF1 vs AVP1): double-check the FC code against the PO/BOL ship-to before submitting. 13088's 10/2 request went to AVF1 by mistake and never got an answer.
MD depot (1052 Frederick) weekly cycle (G/Hanson 10/06, Diamond's Jan Tappel + Krista agreed): Each week Krista emails Jacob to confirm POs + quantities for the master; Diamond OS&D (Jan Tappel, jtappel@diamondpet.com) is cc'd. Keep Jan on those replies. ADW issues ONE master consolidated PO every WEDNESDAY. Whatever arrived before goes on it; anything arriving Wed/Thu/Fri/weekend goes on the NEXT Wednesday's master. FTL refusals still redeliver on their original PO. One truck = charge the customer delivery once. Runners: 1 week free storage; rework minimum was $185, G got it to $135 (~mid Sept); Hanson may call Shoja to try for no minimum. Margin plan (G): find local carriers that can hit ~$400 so deliveries break even or better.
G 10/06: ideally run the same weekly Wednesday master-PO cycle for NJ (175, Krista) and CA (960 Mira Loma, Chanh) too, to keep it organized (Diamond already does weekly for LA). Propose it to ADW for those depots.
Weekly Wednesday master PO for NJ (175) / Mira Loma (960): ON HOLD - do NOT add the proposal line to ADW drafts until Jacob says to (Jacob 10/07, WN-13343).
Costco portal: "No appointment found" on a PO search can mean the appointment is already COMPLETED (delivered), not missing. Check the Supplier Portal History (PPD) or ask the WH for the POD before re-requesting (10520921303 was delivered 10/2, 10/07 lesson).
Before saying something was NOT done (no POD, no appt, not delivered), check first: Front (search the PO / master PO / WN tag / sender), the WN and #diamond-deliveries Slack channels, and the board notes. Say "I can't find it" rather than "it wasn't done" (Jacob 10/07).
Chewy refusals (e.g. 13088, 13315): NO ADW ticket (ADW = Costco depots only). Diamond (Thomas) approves the rework; WarehouseNow books the redelivery truck and requests the appt in the Chewy scheduling portal (carrier name + SCAC required, submit once).
Carriers/brokers/customers send driver info, ETAs and docs to US (requests@ / the thread), never straight to the warehouse. We are the warehouse broker: Jacob passes it on to the WH. Never give a carrier the WH emails in a draft (Jacob 10/08). Check WH hours on the dashboard before quoting them (Runners 0800-1700 M-F).
Mira Loma (960) CAN issue a master PO too: Chanh gave master PO 9601008164 for WN-13343 (10/07) instead of rebooking the original PO. Use whatever PO Chanh says; relabel pallets with the new PO.
