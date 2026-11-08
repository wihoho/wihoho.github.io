#!/usr/bin/env python3
"""Submit the page URLs from this site's sitemap index to IndexNow.

The key is read from the INDEXNOW_KEY environment variable. A real key is
never committed. IndexNow checks that https://wihoho.github.io/indexnow-key.txt
contains that same key. GitHub Pages publishes the file that is in git, so
replace the placeholder in indexnow-key.txt with the secret's value (one
line, no quotes) before this script can succeed.

Usage:
  INDEXNOW_KEY=... python3 script/indexnow.py
  INDEXNOW_KEY=... python3 script/indexnow.py --wait 180
  python3 script/indexnow.py --dry-run --sitemap-file /tmp/jekyll-site/sitemap.xml
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

HOST = "wihoho.github.io"
KEY_URL = f"https://{HOST}/indexnow-key.txt"
SITEMAP_INDEX = f"https://{HOST}/sitemap_index.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
USER_AGENT = "wihoho-indexnow/1.0"


def fetch(url: str, timeout: int = 30) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def locs(xml_bytes: bytes) -> list[str]:
    root = ET.fromstring(xml_bytes)
    found = []
    for element in root.findall(".//sm:loc", NS):
        if element.text:
            found.append(element.text.strip())
    if not found:
        for element in root.iter():
            if element.tag.endswith("loc") and element.text:
                found.append(element.text.strip())
    return found


def is_sitemap(url: str) -> bool:
    path = url.split("?", 1)[0].lower()
    return path.endswith(".xml")


def page_urls_from(url: str, seen: set[str] | None = None) -> list[str]:
    seen = seen if seen is not None else set()
    if url in seen:
        return []
    seen.add(url)
    body = fetch(url)
    pages: list[str] = []
    for loc in locs(body):
        if not loc.startswith(f"https://{HOST}/") and loc.rstrip("/") != f"https://{HOST}":
            continue
        if is_sitemap(loc):
            pages.extend(page_urls_from(loc, seen))
        elif not loc.endswith(KEY_URL.rsplit("/", 1)[-1]):
            pages.append(loc.split("#", 1)[0])
    return pages


def key_matches(key: str) -> bool:
    try:
        live = fetch(KEY_URL).decode("utf-8", "replace").strip()
    except urllib.error.URLError as error:
        print(f"Could not read {KEY_URL}: {error}")
        return False
    return live == key


def wait_for_marker(marker: str, seconds: int) -> bool:
    deadline = time.time() + seconds
    while True:
        try:
            body = fetch(f"https://{HOST}/sitemap.xml").decode("utf-8", "replace")
            if marker in body:
                return True
        except urllib.error.URLError as error:
            print(f"Sitemap not ready yet: {error}")
        if time.time() >= deadline:
            return False
        time.sleep(15)


def submit(key: str, urls: list[str]) -> int:
    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": KEY_URL,
        "urlList": urls[:10000],
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": USER_AGENT},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            status = response.status
            body = response.read().decode("utf-8", "replace")[:500]
    except urllib.error.HTTPError as error:
        status = error.code
        body = error.read().decode("utf-8", "replace")[:500]
    print(f"IndexNow responded {status} for {len(payload['urlList'])} URLs.")
    if body.strip():
        print(body.strip())
    return status


def valid_key(key: str) -> bool:
    if not 8 <= len(key) <= 128:
        return False
    return all(character.isalnum() or character == "-" for character in key)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wait", type=int, default=0, help="Seconds to wait until sitemap.xml contains /apps/")
    parser.add_argument("--dry-run", action="store_true", help="Print URL counts and do not POST")
    parser.add_argument("--sitemap-file", help="Read a local urlset or sitemap index instead of the live site")
    args = parser.parse_args()

    key = os.environ.get("INDEXNOW_KEY", "").strip()
    if args.dry_run and args.sitemap_file and not key:
        key = "dry-run-only"
    if not key:
        print("INDEXNOW_KEY is not set. Add it as a repository secret. Not submitting.")
        return 0
    if key != "dry-run-only" and not valid_key(key):
        print("INDEXNOW_KEY must be 8-128 characters: letters, digits, and dashes only.")
        return 1

    if args.sitemap_file:
        urls = []
        seen: set[str] = set()
        for loc in locs(open(args.sitemap_file, "rb").read()):
            if is_sitemap(loc) and loc.startswith("http"):
                urls.extend(page_urls_from(loc, seen))
            else:
                urls.append(loc)
    else:
        if not args.dry_run and not key_matches(key):
            print(f"{KEY_URL} does not contain INDEXNOW_KEY yet.")
            print("Replace the single line in indexnow-key.txt with that key and wait for GitHub Pages to publish it.")
            print("Not submitting.")
            return 0
        if args.wait:
            print(f"Waiting up to {args.wait}s for /apps/ to appear in the live sitemap.")
            if not wait_for_marker("/apps/", args.wait):
                print("Timed out waiting for the new sitemap. Not submitting.")
                return 1
        try:
            urls = page_urls_from(SITEMAP_INDEX)
        except urllib.error.URLError as error:
            print(f"Could not read {SITEMAP_INDEX}: {error}")
            return 1

    # Preserve order, drop duplicates.
    unique = list(dict.fromkeys(urls))
    print(f"Collected {len(unique)} page URLs.")
    if args.dry_run or key == "dry-run-only":
        for url in unique:
            print(url)
        return 0
    status = submit(key, unique)
    if status in (200, 202):
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
