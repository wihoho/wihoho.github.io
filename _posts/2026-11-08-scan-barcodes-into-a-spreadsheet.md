---
layout: post
title: "How to scan barcodes into a CSV or Excel file"
description: "Scan barcodes and QR codes into a list on Android and save XLSX or CSV. PlainTally works offline, with no account and no scan limit."
image: https://play-lh.googleusercontent.com/7kFLht1sxNd1jd9i4R7BJr_k_xl6izxNc_pECVVr64lU41Lkj01Ox9cGn4iVbwdBU3SgxolByLki5YhDJy2u9g4
date: 2026-11-08 00:01:00 +0000
author: wihoho
---

A stock count or a class check-in should end as a spreadsheet, not as a camera roll of barcodes. [PlainTally](/apps/plaintally/) puts each code in a row with the time, then saves CSV or XLSX on the phone. There is no account and no scan limit.

The steps match the Play listing as of November 2026. The reader is inside the app, so it works in airplane mode.

## Pick the kind of list first

The repeat behaviour is the part people get wrong, so choose it before you scan a hundred labels.

- **Inventory count.** Scanning the same item again adds 1 to its quantity. Use this for a stocktake.
- **Attendance.** One check-in per ID, with the time. A second scan is refused and plays a warning tone. Use this for a class, an event, or a site sign-in.
- **Simple list.** Every scan is its own row, even when the code repeats.
- **Your own rule.** Add again, add and warn, ignore, or count.

You can add columns such as location, price, or condition, and rename, reorder, or hide the ones you do not need. If you already have a CSV of codes with names or prices, import it as a lookup file and scans fill those columns in.

## Scan

1. Install [PlainTally](/apps/plaintally/) and make a list. The camera permission is requested the first time you tap Scan. There are no ads and no tracking.
2. Hold the phone over one label, then the next. Continuous scanning is the default. Resting on the same label does not add a second row.
3. Use the torch, pinch or the slider to zoom, and tap to focus if a small code will not read. Beep and vibration tell you a code landed.
4. Undo is one tap, for the scan you did not mean.

Codes the listing names: QR, EAN-13, EAN-8, UPC-A, UPC-E, Code 128, Code 39, Code 93, ITF, Codabar, Data Matrix, PDF417, and Aztec.

A code that is already a picture can be scanned from a photo. You can also type a code, or use a Bluetooth or USB scanner, which types straight into the list. Rows can be edited, swiped away, or found with search. Lists can be renamed or duplicated.

## Save a file the spreadsheet will not mangle

Preview the table, then save.

- **XLSX** keeps codes as text, so a leading zero stays. Quantities are numbers. Times are real dates.
- **CSV** is UTF-8, separated by commas, semicolons, or tabs, for the spreadsheet you already use.

Share the file to email, chat, or a drive when you want it off the phone. Until then it stays there: PlainTally has no internet permission. Back up every list as one file if you are about to change phones, and restore from that file later.

A paper packing list that you also want as a PDF, rather than as rows, is a scan for [PlainScan](/apps/plainscan/). PlainTally is for the codes.

{% include play-cta.html id="plaintally" content="guide" %}
