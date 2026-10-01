"""Download, crop, and encode Vietnam event pictures for HOI4.

Sources are searched on Wikimedia Commons. Output DDS files use BC1/DXT1,
matching the existing HOI4 leader assets in this repository.
"""
from __future__ import annotations

import io
import json
import struct
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "assets" / "event_pictures" / "raw"
PNG = ROOT / "assets" / "event_pictures" / "png"
DDS = ROOT / "gfx" / "event_pictures"
GFX = ROOT / "interface" / "VIE_md_event_pictures.gfx"
CREDITS = ROOT / "assets" / "event_pictures" / "CREDITS.json"
TARGET = (210, 176)

EVENTS = {
    "vie_proc_army.1": ("vie_proc_army_1", "T-54 T-55 tank Finland Vietnam"),
    "vie_proc_army.2": ("vie_proc_army_2", "Polish T-72 tank"),
    "vie_proc_army.5": ("vie_proc_army_5", "T-54 tank upgrade Vietnam"),
    "vie_proc_army.8": ("vie_proc_army_8", "Igla missile soldier"),
    "vie_proc_army.11": ("vie_proc_army_11", "Vietnamese assault rifle soldier"),
    "vie_proc_army.14": ("vie_proc_army_14", "Vietnam Russia military meeting"),
    "vie_proc_army.15": ("vie_proc_army_15", "Vietnam T-90 tank"),
    "vie_proc_army.16": ("vie_proc_army_16", "Vietnam T-90S tank"),
    "vie_proc_army.18": ("vie_proc_army_18", "K9 Thunder howitzer"),
    "vie_proc_army.19": ("vie_proc_army_19", "K9 Thunder howitzer"),
    "vie_proc_army.20": ("vie_proc_army_20", "K9 Thunder delivery"),
    "vie_proc_army.21": ("vie_proc_army_21", "K9 Thunder artillery crew"),
    "vie_proc_army.30": ("vie_proc_army_30", "BMP-3 infantry fighting vehicle"),
    "vie_proc_army.31": ("vie_proc_army_31", "BMP-3 interior crew"),
    "vie_proc_army.32": ("vie_proc_army_32", "BMP-3 amphibious exercise"),
    "vie_proc_army.35": ("vie_proc_army_35", "TOS-1A launcher"),
    "vie_proc_army.38": ("vie_proc_army_38", "CAESAR self propelled howitzer"),
    "vie_proc_army.39": ("vie_proc_army_39", "CAESAR howitzer"),
    "vie_proc_army.40": ("vie_proc_army_40", "CAESAR howitzer firing"),
    "vie_def_ind.1": ("vie_def_ind_1", "Vietnam defence exhibition"),
    "vie_def_ind.2": ("vie_def_ind_2", "T-90 tank maintenance"),
    "vie_def_ind.3": ("vie_def_ind_3", "defence industry factory"),
    "vie_def_ind.4": ("vie_def_ind_4", "National Assembly Building Hanoi Vietnam"),
}


def commons_image(query: str) -> tuple[bytes, dict]:
    params = {
        "action": "query", "generator": "search", "gsrsearch": query,
        "gsrnamespace": 6, "gsrlimit": 10, "prop": "imageinfo",
        "iiprop": "url|mime|extmetadata", "iiurlwidth": 1000, "format": "json",
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"User-Agent": "hoi4-md-vietnam-event-pictures/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    pages = payload.get("query", {}).get("pages", {})
    for page in pages.values():
        info = page.get("imageinfo", [{}])[0]
        if not info.get("mime", "").startswith("image/"):
            continue
        image_url = info.get("thumburl") or info.get("url")
        if not image_url:
            continue
        try:
            request = urllib.request.Request(image_url, headers={"User-Agent": "hoi4-md-vietnam-event-pictures/1.0"})
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read()
            image = Image.open(io.BytesIO(data))
            if image.width >= 400 and image.height >= 300:
                return data, {"title": page.get("title", ""), "url": image_url}
        except Exception:
            continue
    raise RuntimeError(f"No suitable Wikimedia Commons image found for: {query}")


def crop_image(data: bytes) -> Image.Image:
    image = Image.open(io.BytesIO(data)).convert("RGB")
    target_ratio = TARGET[0] / TARGET[1]
    ratio = image.width / image.height
    if ratio > target_ratio:
        width = round(image.height * target_ratio)
        left = (image.width - width) // 2
        image = image.crop((left, 0, left + width, image.height))
    else:
        height = round(image.width / target_ratio)
        top = (image.height - height) // 2
        image = image.crop((0, top, image.width, top + height))
    return image.resize(TARGET, Image.Resampling.LANCZOS)


def rgb565(red: int, green: int, blue: int) -> int:
    return ((red >> 3) << 11) | ((green >> 2) << 5) | (blue >> 3)


def unpack565(value: int) -> tuple[int, int, int]:
    return ((value >> 11 & 31) * 255 // 31, (value >> 5 & 63) * 255 // 63, (value & 31) * 255 // 31)


def encode_block(pixels: list[tuple[int, int, int]]) -> bytes:
    average = tuple(sum(pixel[i] for pixel in pixels) // len(pixels) for i in range(3))
    brightest = max(pixels, key=lambda pixel: sum(pixel))
    darkest = min(pixels, key=lambda pixel: sum(pixel))
    color_a = rgb565(*brightest)
    color_b = rgb565(*darkest)
    if color_a < color_b:
        color_a, color_b = color_b, color_a
    first = unpack565(color_a)
    second = unpack565(color_b)
    palette = [first, second]
    palette.extend(tuple((2 * first[i] + second[i]) // 3 for i in range(3)) for _ in [0])
    palette.append(tuple((first[i] + 2 * second[i]) // 3 for i in range(3)))
    indices = 0
    for index, pixel in enumerate(pixels):
        nearest = min(range(4), key=lambda palette_index: sum((pixel[i] - palette[palette_index][i]) ** 2 for i in range(3)))
        indices |= nearest << (2 * index)
    return struct.pack("<HHI", color_a, color_b, indices)


def encode_bc1(image: Image.Image) -> bytes:
    image = image.convert("RGB")
    blocks = bytearray()
    for top in range(0, image.height, 4):
        for left in range(0, image.width, 4):
            pixels = [image.getpixel((min(left + x, image.width - 1), min(top + y, image.height - 1))) for y in range(4) for x in range(4)]
            blocks.extend(encode_block(pixels))
    header = struct.pack(
        "<4s7I11I8I5I",
        b"DDS ", 124, 0x00081007, image.height, image.width, len(blocks), 0, 0,
        *([0] * 11), 32, 0x4, 0x31545844, 24, 0, 0, 0, 0, 0x1000, 0, 0, 0, 0,
    )
    return header + blocks


def main() -> None:
    for directory in (RAW, PNG, DDS):
        directory.mkdir(parents=True, exist_ok=True)
    credits = {}
    for event_id, (stem, query) in EVENTS.items():
        raw_path = RAW / f"{stem}.jpg"
        png_path = PNG / f"{stem}.png"
        dds_path = DDS / f"{stem}.dds"
        if not raw_path.exists():
            data, source = commons_image(query)
            raw_path.write_bytes(data)
            credits[event_id] = {"query": query, **source}
        else:
            credits[event_id] = {"query": query, "title": "existing local source"}
        image = crop_image(raw_path.read_bytes())
        image.save(png_path, optimize=True)
        dds_path.write_bytes(encode_bc1(image))
        print(f"built {event_id} -> {dds_path.name}")
    CREDITS.write_text(json.dumps(credits, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["spriteTypes = {"]
    for event_id, (stem, _) in EVENTS.items():
        lines.extend(["\tspriteType = {", f'\t\tname = "GFX_VIE_report_event_{stem}"', f'\t\ttexturefile = "gfx/event_pictures/{stem}.dds"', "\t}"])
    lines.append("}")
    GFX.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
