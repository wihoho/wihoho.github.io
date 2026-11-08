---
layout: page
title: Free Android apps
permalink: /apps/
description: "Free Android apps by tedmosby: scan to PDF, chats to PDF, Wi-Fi channels, louder videos, floor plans, photo stamps, watermarks, drum pads and barcode spreadsheets."
---

These are the Android apps currently on Google Play under [tedmosby](https://play.google.com/store/apps/developer?id=tedmosby). Most of them have no account and no internet permission, so files stay on the phone until you choose to share them. Each app links to a practical guide and to its Play listing.

{% for app in site.data.apps %}
## [{{ app.short_name }}]({{ app.path }})

{{ app.short }}

[{{ app.name }}]({{ app.path }}) · [Guide]({{ app.post }}) · [Privacy policy]({{ app.privacy }})

{% include play-cta.html id=app.id content="apps-index" %}
{% endfor %}

Older projects, including the Chrome extensions, are on the [portfolio](/portfolio/).
