"""Download, crop and encode the air event pictures (Truc 1 vie_air_proc.*, Truc 2 vie_air_ind.*, Truc 3 vie_air_force.*) from Wikimedia Commons.

Unlike build_vie_event_pictures.py (first search hit), every picture here is a hand-picked Commons FILE, and its
license, author and page are written to assets/event_pictures/CREDITS.json (CC BY / CC BY-SA need attribution).
Existing sprites in interface/VIE_md_event_pictures.gfx are kept; the vie_air_proc ones are appended or replaced.

    python tools/build_vie_air_event_pictures.py
"""
from __future__ import annotations

import html
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_vie_event_pictures import CREDITS, DDS, GFX, PNG, RAW, crop_image, encode_bc1  # noqa: E402

UA = {"User-Agent": "hoi4-md-vietnam-event-pictures/1.0 (event art for a fan mod)"}

# event id -> Commons file title (checked 2026-10-02: licenses are free; attribution kept in CREDITS.json)
PICTURES = {
    "vie_air_proc.1": "File:MIG 21 VIETNAMESE AIR FORCE AT THE B52 VICTORY CENTRE HUU TIEP LAKE HA NOI VIETNAM FEB 2012 (6832950578).jpg",
    "vie_air_proc.2": "File:UA anti-air training 2021 S-300 (1).jpg",
    "vie_air_proc.3": "File:VPAF Su-30MK2.jpg",
    "vie_air_proc.5": "File:VPAF Su-30MK2 flares.jpg",
    "vie_air_proc.6": "File:Vietnam Air Force Sukhoi Su-30MK2 - VDE2024.jpg",
    "vie_air_proc.7": "File:S-125 Pechora-2M VEN.jpg",
    "vie_air_proc.8": "File:Airbus C295 EC-001 ILA-2022.jpg",
    "vie_air_proc.9": "File:Su-30MK2 number 8533 Jan-2017.jpg",
    "vie_air_proc.10": "File:SPYDER.jpg",
    "vie_air_proc.11": "File:ERA Vera NG at ILA-2024.jpg",
    "vie_air_proc.13": "File:Vietnamese Su-30MK2.jpg",
    "vie_air_proc.14": "File:Yakovlev Yak-130 134 White PAS 2013 01.jpg",
    "vie_air_proc.15": "File:Five T-6C Texan II (601-605) for Vietnam People's Air Force.jpg",
    # Truc 2 (CNQP hang khong - phong khong): 15 event chon
    "vie_air_ind.11": "File:Sukhoi Su-27 Flanker (14260536207).jpg",
    "vie_air_ind.12": "File:Vietnamese Su-22M4 with Kh-25s.jpg",
    "vie_air_ind.13": "File:Su-30MK2 and Kh-25.jpg",
    "vie_air_ind.21": "File:SAM S-75 Dvina. ЗРК С-75 \"Двина\" (7322067464).jpg",
    "vie_air_ind.22": "File:Mordenized SNR-125 radar by Viettel.jpg",
    "vie_air_ind.23": "File:S-300 launcher, 2009.jpg",
    "vie_air_ind.31": "File:P18M surveilance radar of Viettel.jpg",
    "vie_air_ind.32": "File:Viettel High Tech VRS-MRS 3D air-surveillance radar.png",
    "vie_air_ind.33": "File:VRS-S54S A80.jpg",
    "vie_air_ind.41": "File:Python-5-missile-0006.jpg",
    "vie_air_ind.42": "File:VRS-Viettel.jpg",
    "vie_air_ind.43": "File:Beechcraft T-6C Texan II, ILA 2024, Schoenefeld (ILA43887).jpg",
    "vie_air_ind.51": "File:BTS-99 loitering munition of Z199 Factory.jpg",
    "vie_air_ind.52": "File:Pacific Friendship 2026- US, Vietnamese partners train with drones, support water rescue operations in Vietnam (9788238).jpg",
    "vie_air_ind.53": "File:BXL-01 loitering munition of Z131 Factory.jpg",
    # Truc 3 (xay dung luc luong): 5 event chon
    "vie_air_force.1": "File:VPAF Su-30MK2.jpg",
    "vie_air_force.2": "File:Vietnam Air Force Sukhoi Su-30MK2 - VDE2024.jpg",
    "vie_air_force.10": "File:UA anti-air training 2021 S-300 (1).jpg",
    "vie_air_force.11": "File:P18M surveilance radar of Viettel.jpg",
    "vie_air_force.30": "File:Su-30MK2 number 8533 Jan-2017.jpg",
}


def fetch(url: str) -> bytes:
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as response:
                return response.read()
        except urllib.error.HTTPError as err:
            if err.code != 429:
                raise
            time.sleep(10 * (attempt + 1))
    raise RuntimeError("rate limited: " + url)


def file_info(title: str) -> dict:
    params = {"action": "query", "titles": title, "prop": "imageinfo", "iiprop": "url|mime|size|extmetadata",
              "iiurlwidth": 1000, "format": "json"}
    payload = json.loads(fetch("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)))
    page = next(iter(payload["query"]["pages"].values()))
    info = page["imageinfo"][0]
    meta = info.get("extmetadata", {})
    clean = lambda key: html.unescape(re.sub(r"<[^>]+>", "", meta.get(key, {}).get("value", ""))).strip()
    return {
        "title": page["title"], "page": info["descriptionurl"], "image_url": info.get("thumburl") or info["url"],
        "license": clean("LicenseShortName"), "license_url": clean("LicenseUrl"), "author": clean("Artist"),
    }


def main() -> None:
    for directory in (RAW, PNG, DDS):
        directory.mkdir(parents=True, exist_ok=True)
    credits = json.loads(CREDITS.read_text(encoding="utf-8")) if CREDITS.exists() else {}
    for event_id, title in PICTURES.items():
        stem = event_id.replace(".", "_")
        raw_path = RAW / f"{stem}.jpg"
        if raw_path.exists() and event_id in credits and credits[event_id].get("license"):
            data = raw_path.read_bytes()  # already downloaded: keep the credit, rebuild the sprite
            print(f"{event_id}: reuse {credits[event_id]['title']}")
            info = credits[event_id]
        else:
            info = file_info(title)
            print(f"{event_id}: {info['title']} [{info['license']}] by {info['author'][:50]}")
            data = fetch(info["image_url"])
            raw_path.write_bytes(data)
            time.sleep(3)
        image = crop_image(data)
        image.save(PNG / f"{stem}.png", optimize=True)
        (DDS / f"{stem}.dds").write_bytes(encode_bc1(image))
        credits[event_id] = info
    CREDITS.write_text(json.dumps(credits, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    text = GFX.read_text(encoding="utf-8")
    for event_id in PICTURES:
        stem = event_id.replace(".", "_")
        entry = f'\tspriteType = {{\n\t\tname = "GFX_VIE_report_event_{stem}"\n\t\ttexturefile = "gfx/event_pictures/{stem}.dds"\n\t}}\n'
        if f'GFX_VIE_report_event_{stem}"' not in text:
            text = text.rstrip().rstrip("}").rstrip() + "\n" + entry + "}\n"
    GFX.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
