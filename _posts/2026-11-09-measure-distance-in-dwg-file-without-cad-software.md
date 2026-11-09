---
layout: post
title: "Measure a Distance in a DWG File Without CAD Software"
description: "Check a length, offset or angle in a DWG or DXF drawing right in Chrome. No CAD install, no upload, no account. Here is how."
image: https://wihoho.github.io/privacy/extensions/img/draftlens/screenshot-1.jpg
date: 2026-11-09 00:02:00 +0000
author: wihoho
---

Sometimes you only need one number from a drawing. How wide is that opening? How far is the column from the wall? You can get that number from a DWG file without installing CAD software. [DraftLens](https://wihoho.github.io/privacy/extensions/draftlens/) opens the drawing in Chrome and has a measure tool that snaps to points in the drawing.

It is a viewer only. You can measure, but you cannot add a dimension or change a line. If you need to mark up or fix the drawing, this is the wrong tool.

The file stays on your computer. DraftLens reads it inside the browser with the open-source LibreDWG library. Nothing is uploaded. There is no account and there are no ads.

## Open the drawing

1. Add [DraftLens](https://wihoho.github.io/privacy/extensions/draftlens/) to Chrome. It is free and works on Chromebooks too.
2. Click its icon to open the viewer page.
3. Drag your file onto the page, or choose it from your files. It reads .dwg files from R13 to 2018 and later, and ASCII .dxf files.
4. If the drawing is a link on a web page or in webmail, right-click the link and pick "Open drawing in DraftLens".

## Find the part you want to measure

1. Zoom and pan with a mouse, a trackpad or a pinch.
2. If you get lost, double-click or press F to fit the whole drawing back on screen.
3. Turn off layers you don't need. Hatching, furniture or text layers can sit right on top of the lines you care about. Each layer shows its color, so it is easier to tell which one is which.

Hiding clutter first makes the next part much easier. Snapping is easier when the points you want aren't buried under other lines.

## Take the measurement

1. Start the measure tool.
2. Click the first point. The tool snaps to endpoints and centers, so you can land exactly on a corner or the middle of a circle.
3. Click the second point.
4. Read the result. You get the distance, plus ΔX, ΔY and the angle.

The ΔX and ΔY values help when you need a straight horizontal or vertical offset and the two points don't line up. The angle helps you check whether a wall or a run of pipe is really square.

## Know what the units mean

DraftLens reports distances in the drawing's own units. It does not convert them. If the drawing was made in millimetres, a result of 900 means 900 mm. If it was made in inches, the same number means inches. Before you trust a number, I would measure something whose size you already know, such as a standard door, and check that the result makes sense.

## Save or share what you found

When the view shows what you measured, save it as a PNG or print it. That gives you something to attach to an email or to bring to a site visit.

## Where it falls short

Some drawings will not show everything you expect. These are not supported yet:

- Binary DXF files
- Paper-space layouts
- 3D solids
- Embedded images
- External references

If the measurement you need depends on a sheet layout, a 3D model or a linked file, DraftLens can't show it. For a quick check of a length, an offset or an angle in a 2D drawing, it saves you from installing anything. It is free and open source under GPL-3.0.

[Add DraftLens to Chrome](https://chromewebstore.google.com/detail/clpmlbkjbnljdlcgpelijicjjhnbijll?utm_source=wihoho.github.io&utm_medium=website&utm_campaign=draftlens&utm_content=post)
