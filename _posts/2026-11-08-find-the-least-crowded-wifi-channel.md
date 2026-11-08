---
layout: post
title: "How to find the least crowded Wi-Fi channel"
description: "Use an Android phone to see which Wi-Fi channel your router shares with the neighbours, then pick a quieter one. PlainWiFi recommends a channel. It does not boost the signal."
image: https://play-lh.googleusercontent.com/jbNoEZaiK4AqnTSs8_UeTfA-CRt4fozw1O0Legia_iD2cEeBnrdTfA4qGH7efNMT8Fzw-OJ9KEDhx6FYK3Ci
date: 2026-11-08 00:07:00 +0000
author: wihoho
---

If video calls fall apart in one room and the router is sitting on channel 6 with half the street, the fix is usually the channel, not a "booster" app. [PlainWiFi](/apps/plainwifi/) reads what Android already knows about nearby networks and tells you whether changing channel is worth it.

The steps match the Play listing as of November 2026.

## Scan the networks you can actually see

1. Install [PlainWiFi](/apps/plainwifi/). It opens on your networks. There is no account.
2. When you tap Allow and scan, Android asks for location. It does that for every app that wants Wi-Fi scan results, because a scan could be used to guess where a phone is. PlainWiFi asks only then, and it does not read or store your position. The live signal meter works without that permission.
3. Read the recommendation. The listing's example is the shape of the sentence you get: "Your network is on channel 6, shared with 3 others. Try channel 11."
4. Open the channel graph. It covers 2.4 GHz, 5 GHz, and 6 GHz, and it draws 40, 80, and 160 MHz networks at their real width. Two networks can sit on different channel numbers and still overlap. The picture is how you see that.
5. Note the flags. DFS channels are marked, and so are open or WEP networks.

The list shows signal strength, channel, band, channel width, security, and Wi-Fi generation (Wi-Fi 4, 5, 6, 6E, and 7). The last scan stays on screen. If Android refuses another scan for a while, PlainWiFi shows how old the results are instead of an empty list.

## Change the router, not the phone

PlainWiFi does not log into your router, does not show saved Wi-Fi passwords, does not boost the signal, and does not run a speed test. Write down the channel it suggests, open the router's admin page, and set the channel there. Then scan again from the same spot and see whether your network is still sharing a channel.

## Find the dead room

Walk the house with the room walk. Measure a room, name it, and repeat. The free version measures 3 rooms and ranks them weakest first. That is enough to compare the sofa, the kitchen, and the room where calls fail.

An optional one-time purchase, with no subscription, adds unlimited rooms, saved walks (so you can compare before and after you move the router), and CSV export. The listing does not show a price, so I am not going to invent one. Everything described above the purchase is free.

The app has no internet permission. A scan leaves the phone only if you export it. There are no ads, no analytics, no tracking, and no account.

If you are also sketching where the router and the desk should go, the room names line up with a drawing in [PlainPlan](/apps/plainplan/).

{% include play-cta.html id="plainwifi" content="guide" %}
