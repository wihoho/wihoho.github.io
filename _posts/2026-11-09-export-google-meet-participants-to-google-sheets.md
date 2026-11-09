---
layout: post
title: "Export Google Meet Participants to Google Sheets"
description: "Get a Google Meet participant list with join times, leave times and minutes in the call into Google Sheets or Excel, with no retyping."
image: https://wihoho.github.io/privacy/extensions/img/rollcall/screenshot-1.jpg
date: 2026-11-09 00:15:00 +0000
author: wihoho
---

You can move a Google Meet participant list into Google Sheets without retyping names. [RollCall](https://wihoho.github.io/privacy/extensions/rollcall/) reads Meet's People list while you are in the call. It records who joined, when each person arrived, when they left and how many minutes they stayed. You can then paste the table into a sheet or download a CSV.

You do not need a paid Google Workspace plan. RollCall works with any Meet call you join in Chrome, including free accounts and school accounts. It is free, with no account and no ads.

## Set it up once

1. Install [RollCall](https://wihoho.github.io/privacy/extensions/rollcall/) in Chrome. It also works on Chromebooks.
2. If you want to check names against a class or team, paste your roster in. You only do this once.
3. Set your rules. You can choose "late after N minutes" and a minimum time before someone counts as present. Pick numbers that match how you already report attendance, so the sheet needs no fixing later.

## Record the call

1. Join your call on meet.google.com. RollCall starts recording on its own. There is no button to press.
2. Open Meet's People panel once during the call. Meet only shows some people as video tiles. With the People panel open, RollCall sees every name, not just the faces on screen. It reminds you if the panel is closed.
3. Run the call as usual. If someone drops out and comes back, RollCall records the rejoin along with the join and leave times.
4. Open RollCall's side panel at any point to see the list. If you pasted a roster, it shows who is present, late or absent. Guests who are not on the list show up too.

## Get it into Google Sheets

There are three ways to get the data out.

1. **Copy the table.** It pastes straight into Google Sheets. For one class or one meeting, this is the quickest way.
2. **Download a CSV.** It opens in Google Sheets or Excel. This is the better choice if you keep files for records.
3. **Get a CSV automatically when the call ends.** You don't have to remember to export.

My advice is to keep one spreadsheet per class or group and add each session as a new tab. Then you can see a whole term in one file.

## Where the names are kept

Names and attendance stay in Chrome on your computer. They are never uploaded. RollCall only sends anonymous counts of successful exports and errors, with no names or meeting details. It runs only on meet.google.com.

## When it is the wrong tool

RollCall is a Chrome extension, and it only works on meet.google.com. It cannot record calls you join outside Chrome, so it misses a session you take from another device's app. The records also stay in Chrome on the computer that took them. If you teach from more than one machine, export after every call, or the history ends up split across devices.

It also depends on the People panel. If you never open it during a call, RollCall may only see the people who appeared as video tiles. That list will not match the real one.

[Add RollCall to Chrome](https://chromewebstore.google.com/detail/nfehfmpigmccopnpdfjoafdkbfaljejj?utm_source=wihoho.github.io&utm_medium=website&utm_campaign=rollcall&utm_content=post)
