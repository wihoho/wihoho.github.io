---
layout: post
title: "How to turn a WhatsApp chat or SMS backup into a PDF"
description: "Export a WhatsApp chat or an SMS backup XML file and lay it out as a dated PDF with page numbers. PlainThread only reads the file you give it."
image: https://play-lh.googleusercontent.com/TYImtxYOYOfqd1RBtime6lNX3Q4x5PxwJxooH8W3Wv9TLd4AYfa1b6u0PjQbMjxp9lQeC-ejj4wh5RWyDil5BA
date: 2026-11-08 00:08:00 +0000
author: wihoho
---

A landlord, an HR person, or a small-claims form often wants the conversation on paper, with dates, not a scroll of screenshots. [PlainThread](/apps/plainthread/) turns a chat export or an SMS backup into that PDF. It does not read your messages on its own. You give it a file.

The steps below match the Play listing as of November 2026. PlainThread is a formatting tool, not legal advice. Keep the original messages. Whether a printout is accepted is up to the court or agency.

## From a WhatsApp chat

1. Open the chat in WhatsApp.
2. Tap ⋮ › More › Export chat.
3. Share the file to PlainThread, or save it and open the `.txt` or `.zip` from inside the app.
4. Read the summary of what was found. Check the participants, the message counts, and the first and last dates.
5. If a date could be day/month or month/day, confirm which one. Do this before you print.
6. Pick the whole chat or a date range. On the listing, "All" means all.
7. Tap Create PDF.

The PDF puts the sender, date, and time on every message, adds day headings, and numbers the pages ("Page 3 of 12"). Paper size is A4 or Letter. Attachments are listed by file name at the time they were sent. Right-to-left scripts, accents, and emoji are kept.

## From text messages

PlainThread does not ask for permission to read SMS. Back up with an app that writes an `.xml` file. The listing uses SMS Backup & Restore as the example. Open that `.xml` in PlainThread, or share it across, pick the conversation, and create the PDF. You get both sides, with times, and photos listed where they were sent.

Two things the preview will tell you, which are easy to miss: unsent drafts are counted, and RCS (chat-feature) messages are often absent from an SMS backup. PlainThread cannot put back a message that was never in the file.

## Read the completeness check

Before you send the PDF to anyone, read the check. It says, in plain language, when:

- only one person's messages were found
- an attachment is named but was not included
- media or deleted messages were left out of the export
- there is a long gap, or the export may have hit a size limit
- a line is not part of a message

Nothing in that last case is dropped quietly. If the check complains, go back to the original app and export again rather than pretending the gap is not there.

## The record page

There is no message cap and no watermark. You can put an exhibit or case label on every page. An export-record page lists the source file names, SHA-256 fingerprints, counts, date settings, time zone, and the app version. That is the page I would keep with the original `.txt` or `.xml`.

PlainThread cannot prove the file was never edited, and it is not affiliated with WhatsApp, Meta, or any backup app. Use it for conversations you are part of. The app has no internet permission, and working copies are deleted when you close the chat.

There are no ads, no analytics, no account, no subscription, and no in-app purchases.

{% include play-cta.html id="plainthread" content="guide" %}
