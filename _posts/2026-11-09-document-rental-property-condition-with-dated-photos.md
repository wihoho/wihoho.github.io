---
layout: post
title: "Document a Rental's Condition with Dated, Located Photos"
description: "Record a rental's condition at move-in or move-out. Take photos stamped with date, time and GPS, then export a log as a PDF or CSV."
image: https://play-lh.googleusercontent.com/avH9yMnedHFKXI8_urAUCmrSKsB_o6cwWY9JvMI8YxzjS7Q-hExb00GhH3DqhZ-uByPkzZv6MwXQvrC0Z2MROA
date: 2026-11-09 00:11:00 +0000
author: wihoho
---

When you move into a rental, or move out, your photos of each room are your record of how the place looked. A date and a place on each photo make that record clearer. [PlainStamp](/apps/plainstamp/) adds the date, time and GPS position to each photo as you take it. It also keeps a log that you can export as a PDF report or a CSV spreadsheet. I would still treat a stamp as a record of what the phone reported, and not as proof by itself. If the phone's clock or location is wrong, the stamp is wrong too.

You don't need an account, and no ad plays before the shutter. The only permission the app needs is the camera.

## Before you walk in

1. In system settings, check the phone's date, time and time zone. The app stamps whatever the phone tells it.
2. Install [PlainStamp](/apps/plainstamp/) and turn on location. The app asks for location only when you turn that feature on, and it never uses location in the background.
3. Choose one of the 9 date formats. If your landlord lives in another region, add the UTC offset and the time-zone name.
4. Show the GPS position in decimal or in degrees, minutes and seconds, and include the accuracy. Coordinates don't need a network lookup.
5. Add a street address only if you want one. The phone's built-in geocoder writes the address, and on most phones that lookup may use the network.
6. For the title, type the address and "move-in". Use the note, up to 3 lines, for the unit number or the names of people who were there. Keep the sequence number on so the photos stay in order.
7. Turn on the option to keep the untouched original next to each stamped photo.

Put a box or an outline behind the text so it stays readable on white walls and on dark floors. The preview looks the same as the saved file.

## Go room by room

1. Start at the front door and go around each room in the same direction. If your phone has an ultra-wide lens, switch to it to fit a whole room in one shot.
2. Get close to any damage, like marks on walls, chipped counters or stained carpet. Use the flash in dark cupboards and pinch to zoom on small details.
3. You can use a volume key as the shutter. Photos save in the background, so you can keep shooting.
4. For a walk-through, record a video. The stamp's clock ticks in every frame, and you can record with or without sound. Long recordings are saved in parts of 10, 30 or 60 minutes, so one problem doesn't cost you the whole video.

## Add photos you already took

If you took some shots with the normal camera, pick them from the gallery. You can stamp them with their own date and place, or with the current time. Use their own date when that is what really happened. Your original files stay unchanged.

## Export the log

The log lists every photo and video with:

- the device time and time zone
- the GPS fix and its accuracy
- a comparison of the GPS clock and the phone clock
- a SHA-256 fingerprint of the file

The clock comparison is a quick way to spot a phone clock that has drifted.

1. Export the log as a PDF report and send it with the photos.
2. Or export a CSV file if you track the tenancy in a spreadsheet.
3. At move-out, check whether each file still matches its fingerprint in the log.

## When it is the wrong tool

PlainStamp has no internet permission. It won't upload your photos or share an album with your landlord. You send the files yourself. If you and your landlord need to fill in a shared report online together, you will need another way to do that. PlainStamp can still give you the dated photos to attach.

{% include play-cta.html id="plainstamp" content="guide2" %}
