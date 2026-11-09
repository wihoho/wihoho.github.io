---
layout: post
title: "Take attendance by scanning QR codes on Android"
description: "Check people in to a class or event by scanning their QR codes or ID cards. Each person counts once and gets a timestamp. Save the list as CSV or XLSX."
image: https://play-lh.googleusercontent.com/7kFLht1sxNd1jd9i4R7BJr_k_xl6izxNc_pECVVr64lU41Lkj01Ox9cGn4iVbwdBU3SgxolByLki5YhDJy2u9g4
date: 2026-11-09 00:12:00 +0000
author: wihoho
---

You can run a check-in desk for a class, a club meeting or a workshop with one phone. [PlainTally](/apps/plaintally/) has an attendance list that records each ID once, with the time. If someone scans a second time, the scan is refused and a warning tone plays. At the end you save a CSV or XLSX file that opens in the spreadsheet app you already use.

There is no account, no cloud to link and no scan limit. The only permission is the camera.

## Set up the list

1. Install [PlainTally](/apps/plaintally/) and make a new list. Choose the Attendance job.
2. If you want names next to the codes, prepare a lookup file. This is a CSV of codes with names. When a code is scanned, the name fills in.
3. Add any columns you need, such as room or session. You can also rename, reorder or hide columns.
4. If the same group meets every week, duplicate the list and rename the copy for each session.

Each person needs a code. It can be a QR code or a common barcode on a student or staff card. PlainTally reads QR codes, EAN-13, EAN-8, UPC-A, UPC-E, Code 128, Code 39, Code 93, ITF, Codabar, Data Matrix, PDF417 and Aztec.

## Check people in

1. Open the list and point the camera at the first code. Scanning is continuous, so the next person can step up right away.
2. Wait for the beep or the vibration. Each check-in becomes a row with its time.
3. If someone tries to check in again, the scan is refused and you hear the warning tone. Holding the camera on the same label does not add it twice either.
4. In a dim hall, turn on the torch. For small codes, use pinch or slider zoom, or tap to focus.
5. If someone sends their code as an image, save it and scan it from the photo on the phone.
6. If someone forgot their card, type the ID by hand.
7. If you scanned the wrong thing, undo the last scan with one tap. You can also edit a row, swipe it away, or search the list for a name.

A Bluetooth or USB barcode scanner also works. It types straight into the list, which helps when the queue is long.

## No signal needed

The barcode reader is built into the app. It works in airplane mode, in a basement room or in a hall with no reception. Many venues have poor signal at the door, so it matters here.

## Save the register

When the session ends, save the list.

- XLSX keeps codes as text, so IDs with leading zeros stay intact. Times are stored as real dates, so you can sort and filter them.
- CSV can be comma, semicolon or tab separated, in UTF-8.
- Preview the table before you save.
- Save the file on the phone, or share it to email, chat or a drive.

You can back up every list in one file and restore it later. That is a sensible step before you switch phones.

## When it is the wrong tool

PlainTally has no internet permission. A list stays on the phone that scanned it until you save or share it. If you run two entrances and need both phones to see one live list, this app will not do that. A guest refused at one door would not be flagged at the other. Each phone would keep its own list, and you would have to merge the files in a spreadsheet afterwards. For one desk or one teacher, that limit does not come up.

There is no tracking and there are no ads. The names and times stay on your phone unless you share them.

{% include play-cta.html id="plaintally" content="guide2" %}
