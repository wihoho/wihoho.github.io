---
layout: post
title: "How to put the date, time, and GPS location on photos"
description: "Stamp the date, time, and GPS fix onto Android photos and video while you shoot, and keep a log with a fingerprint of each file."
image: https://play-lh.googleusercontent.com/avH9yMnedHFKXI8_urAUCmrSKsB_o6cwWY9JvMI8YxzjS7Q-hExb00GhH3DqhZ-uByPkzZv6MwXQvrC0Z2MROA
date: 2026-11-08 00:04:00 +0000
author: wihoho
---

For a delivery, a site visit, or a cracked tile you want dated, the useful photo is the one that shows when and where it was taken. [PlainStamp](/apps/plainstamp/) writes that onto the picture as you shoot, instead of trusting a filename later.

The steps match the Play listing as of November 2026.

## Set the stamp once

1. Install [PlainStamp](/apps/plainstamp/). The only permission it requires at the start is the camera. There is no account.
2. Pick a date and time format. There are 9. Add the UTC offset and the time-zone name if the photo will be read in another zone.
3. Turn on location if you want coordinates. The listing says GPS works offline, as decimal degrees or as degrees, minutes, and seconds, with accuracy, altitude, and speed. Location is asked for only when you enable it, and it is not used in the background.
4. Add a title or project name, a note of up to three lines, and a sequence number if you are shooting a set. A logo or signature is optional.
5. Place the text. You get six positions, four sizes, seven colours, four fonts, and a shadow, outline, or box so the text survives a bright wall. The preview is the file that will be saved.

Check the phone's clock and, if you are indoors, the GPS accuracy before you shoot a set you care about. The stamp records what the phone reports. A wrong clock or a poor fix is a wrong stamp.

Street address is a separate, optional line. The app has no internet permission. The [privacy policy](https://wihoho.github.io/privacy/plainstamp/) says the address comes from the phone's built-in geocoder, which on most phones may use the network. Coordinates themselves do not need that lookup. If you are offline and need a place, leave the street line off and keep the GPS numbers.

## Shoot

The camera is the phone's own, with flash, a timer, a grid, and pinch zoom. Switch lenses, including ultra-wide when the phone has it. The volume keys are a shutter. Saving runs in the background, so you can take the next photo without waiting.

For video, the time ticks in every frame. Sound is optional. A long recording is split into parts of 10, 30, or 60 minutes so one failure does not take the whole take with it. The microphone is requested only if you record video with sound.

## Stamp a photo you already took, and keep a log

Pick gallery photos and stamp them with their own date and place, or with the current time. Pick a video and burn in a clock that runs with the video. The originals are not changed. You can also keep the untouched original next to each stamped photo.

Each item in the capture log stores the device time, time zone, GPS fix and its accuracy, how the GPS clock compared with the phone clock, and a SHA-256 fingerprint of the file. Later, check a file against that fingerprint. Export the log as a PDF report or a CSV.

There are no ads, no analytics, no tracking, and no account. If the photo also needs a company name tiled across it, watermark the exported picture in [PlainMark](/apps/plainmark/).

{% include play-cta.html id="plainstamp" content="guide" %}
