---
layout: app
title: "PlainTally: Barcode to CSV"
permalink: /apps/plaintally/
app_id: plaintally
description: "Scan barcodes and QR codes into a list on Android and save CSV or XLSX. PlainTally has no account and works offline."
image: https://play-lh.googleusercontent.com/7kFLht1sxNd1jd9i4R7BJr_k_xl6izxNc_pECVVr64lU41Lkj01Ox9cGn4iVbwdBU3SgxolByLki5YhDJy2u9g4
---

PlainTally turns a pile of barcodes into a spreadsheet. Make a list, point the camera at the labels, and each code becomes a row with its time. Save CSV or XLSX on the phone, or share it to email, chat, or a drive. There is no account, no cloud to link, and no scan limit.

The guide is [how to scan barcodes into a CSV or Excel file](/2026/11/08/scan-barcodes-into-a-spreadsheet.html). It fits stock counts, deliveries and receiving, asset tags, library books, event and class check-ins, and sample tracking.

## Scanning

- Continuous scanning: hold the phone over one label after another.
- QR codes and the common barcodes: EAN-13, EAN-8, UPC-A, UPC-E, Code 128, Code 39, Code 93, ITF, Codabar, Data Matrix, PDF417, and Aztec.
- Beep and vibration, a torch, pinch or slider zoom, and tap to focus.
- Holding the camera on the same label does not add it twice.
- Scan from a photo already on the phone.
- Type a code by hand, or use a Bluetooth or USB barcode scanner, which types straight into the list.
- Undo the last scan with one tap.

## Lists

Three built-in jobs, plus your own rule:

- Inventory count: scanning an item again adds 1 to its quantity.
- Attendance: one check-in per ID, with the time. A repeat is refused and plays a warning tone.
- Simple list: every scan is its own row.
- Your own repeat rule: add again, add and warn, ignore, or count.

You can add columns (location, price, condition, and anything else you name), and rename, reorder, or hide columns. A lookup file is a CSV of codes with names or prices; scans fill those columns in. Rows can be edited, swiped away, and searched. Lists can be renamed or duplicated.

## The file

XLSX keeps codes as text so leading zeros survive, stores quantities as numbers, and stores times as real dates. CSV can be comma, semicolon, or tab separated, in UTF-8. Either opens in the spreadsheet app you already use. You can preview the table before saving, and back up or restore every list with one file.

PlainTally has no internet permission, so a list leaves the phone only when you save or share it. The barcode reader is built into the app and works in airplane mode, in a basement stockroom, or in a warehouse with no signal. There is no account, no tracking, and no ads. The only permission is the camera.

{% include play-cta.html id="plaintally" content="app" %}
