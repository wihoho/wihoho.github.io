---
layout: post
title: "Extract pages from a PDF in Chrome without uploading it"
description: "Pull out only the pages you need from a PDF in Chrome. Type a range like 1-3, 5, 8- and get a new file. Nothing is uploaded and no account is needed."
image: https://wihoho.github.io/privacy/extensions/img/convertlocal/screenshot-1.jpg
date: 2026-11-09 00:01:00 +0000
author: wihoho
---

Sometimes you only need part of a PDF. Maybe it's the signed page of a contract, two pages of a bank statement, or one chapter of a long report. You can pull those pages into a new file in Chrome with [ConvertLocal](https://wihoho.github.io/privacy/extensions/convertlocal/), and the file stays on your computer the whole time. It converts inside Chrome, so nothing goes to a server. There is no email step and no account.

That matters most for documents you would not post publicly, like statements, IDs, medical letters or anything with an account number on it.

ConvertLocal is free, has no ads, and works in Chrome and on Chromebooks.

## Pick the pages you want

1. Add [ConvertLocal](https://wihoho.github.io/privacy/extensions/convertlocal/) to Chrome.
2. Open it and go to merge and split.
3. Add the PDF you want to cut down.
4. Type the pages to extract. A range like `1-3, 5, 8-` takes pages 1 to 3, page 5, and page 8 to the end.
5. Save the new PDF.

The range format is worth learning. You can give it single pages, runs of pages, and an open end, all in one line. You don't have to click through thumbnails one page at a time.

## Split one PDF into several files

If you need more than one piece, extract one range, save it, then come back for the next. For example:

1. Extract `1-4` for the cover letter.
2. Extract `5-12` for the main document.
3. Extract `13-` for the appendix.

You end up with three smaller files from the same original.

## Put pages back together

Splitting often comes before merging. Say you need page 2 from one PDF and pages 6 to 9 from another, sent as a single file. Extract each part first, then use merge to join them. You can put the files in any order before you save.

## Make the result small enough to send

Scanned documents get heavy fast. If the pages you pulled out come from a scan and the file is still too big for an email attachment, ConvertLocal can shrink scanned PDFs. I would do that last, once you have exactly the pages you want, so you are not shrinking pages you are going to throw away.

## When you need images instead of a PDF

If someone wants a picture of a page rather than a PDF, ConvertLocal can also turn every page, or just the pages you choose, into PNG or JPG. Pick 72, 150 or 300 dpi, and download them all in one ZIP. Use 300 dpi if the page has small print someone needs to read.

## Where it falls short

If the PDF is a scan and you were hoping to pull those pages into Word to edit the text, ConvertLocal can't do that yet. PDF to Word needs selectable text, and scanned PDFs need OCR, which isn't included. For a scan, splitting and shrinking work fine. Editing the words does not.

## Quick access

You can also right-click an image on a page to turn it into a PDF, or right-click a PDF link to convert it to Word. For splitting, open the extension and use merge and split.

[Add ConvertLocal to Chrome](https://chromewebstore.google.com/detail/occdpjilcfllpjoglccegekkoeknjcan?utm_source=wihoho.github.io&utm_medium=website&utm_campaign=convertlocal&utm_content=post)
