"""Build the air-branch focus icons (Truc 2 VIE_apm_*, Truc 3 VIE_airf_*) from the Commons photographs already downloaded for the air event pictures.

No new downloads: each focus reuses assets/event_pictures/raw/<event>.jpg and copies that picture's licence, author and page into
assets/focus_icons/CREDITS.json (CC BY / CC BY-SA need attribution). Output follows build_vie_focus_icons.py: 93x91 uncompressed
32-bit DDS in gfx/interface/goals/, PNG preview in assets/focus_icons/png/, sprites GFX_focus_VIE_<stem> in their own file
interface/VIE_md_air_focus_icons.gfx (build_vie_focus_icons.py rewrites VIE_md_focus_icons.gfx, so the two never share a file).
After the sprites exist the focus `icon = GFX_focus_generic_*` lines of the same focuses are switched to the new sprite names.

    python tools/build_vie_air_focus_icons.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_vie_focus_icons import ASSETS, CREDITS as ICON_CREDITS, DDS, PNG, crop_icon, write_dds  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "assets" / "event_pictures" / "raw"
EVENT_CREDITS = ROOT / "assets" / "event_pictures" / "CREDITS.json"
GFX = ROOT / "interface" / "VIE_md_air_focus_icons.gfx"
FOCUS_FILE = ROOT / "common" / "national_focus" / "VIE_md_focus.txt"

# focus id -> (event picture used, optional crop fractions [x0, y0, x1, y1])
ICONS = {
    # Truc 2
    "VIE_apm_law": ("vie_air_proc.1", None),
    "VIE_apm_a32": ("vie_air_ind.11", None),
    "VIE_apm_a31": ("vie_air_ind.21", None),
    "VIE_apm_radar": ("vie_air_ind.31", None),
    "VIE_apm_integration": ("vie_air_ind.41", None),
    "VIE_apm_uav": ("vie_air_ind.51", None),
    "VIE_apm_mature": ("vie_air_ind.32", None),
    # Truc 3 - chain
    "VIE_airf_training_standardization": ("vie_air_proc.15", None),
    "VIE_airf_fighter_force": ("vie_air_proc.3", None),
    "VIE_airf_sam_force": ("vie_air_proc.2", None),
    "VIE_airf_command_reform_1": ("vie_air_ind.33", None),
    "VIE_airf_first_force": ("vie_air_proc.5", None),
    "VIE_airf_command_reform_2": ("vie_air_ind.22", None),
    "VIE_airf_medium_force": ("vie_air_proc.9", None),
    "VIE_airf_operating_range": ("vie_air_proc.6", None),
    # Truc 3 - branch A
    "VIE_airf_iads": ("vie_air_proc.7", None),
    "VIE_airf_layered_defence": ("vie_air_proc.10", None),
    "VIE_airf_ew_antistealth": ("vie_air_ind.42", None),
    "VIE_airf_iads_command": ("vie_air_ind.23", None),
    # Truc 3 - branch B
    "VIE_airf_multirole": ("vie_air_proc.13", None),
    "VIE_airf_multirole_fleet": ("vie_air_ind.13", None),
    "VIE_airf_sustainment": ("vie_air_ind.12", None),
    "VIE_airf_airlift_tanker": ("vie_air_proc.8", None),
    "VIE_airf_multirole_wing": ("vie_air_proc.14", None),
    # Truc 3 - branch C
    "VIE_airf_unmanned": ("vie_air_ind.53", None),
    "VIE_airf_isr_uav": ("vie_air_ind.52", None),
    "VIE_airf_datalink": ("vie_air_proc.11", None),
    "VIE_airf_strike_uav": ("vie_air_ind.51", [0.0, 0.0, 0.6, 1.0]),
    "VIE_airf_teaming": ("vie_air_ind.52", [0.4, 0.0, 1.0, 1.0]),
}


def stem_of(focus_id: str) -> str:
    return focus_id.replace("VIE_", "", 1)       # apm_law, airf_iads ...


def main() -> None:
    PNG.mkdir(parents=True, exist_ok=True)
    DDS.mkdir(parents=True, exist_ok=True)
    event_credits = json.loads(EVENT_CREDITS.read_text(encoding="utf-8"))
    credits = json.loads(ICON_CREDITS.read_text(encoding="utf-8")) if ICON_CREDITS.exists() else {}
    for focus_id, (event_id, crop) in ICONS.items():
        stem = stem_of(focus_id)
        raw = RAW / (event_id.replace(".", "_") + ".jpg")
        info = event_credits[event_id]
        img = crop_icon(Image.open(raw), crop)
        img.save(PNG / f"{stem}.png")
        write_dds(DDS / f"{stem}.dds", img)
        credits[stem] = {"focus": focus_id, "title": info["title"], "author": info["author"], "license": info["license"], "url": info["page"]}
        print(f"built {stem} <- {info['title']}")
    ICON_CREDITS.write_text(json.dumps(credits, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    lines = ["spriteTypes = {"]
    for focus_id in ICONS:
        stem = stem_of(focus_id)
        lines += ["\tspriteType = {", f'\t\tname = "GFX_focus_VIE_{stem}"', f'\t\ttexturefile = "gfx/interface/goals/{stem}.dds"', "\t}"]
    lines.append("}")
    GFX.write_text("\n".join(lines) + "\n", encoding="utf-8")

    text = FOCUS_FILE.read_bytes().decode("utf-8")
    for focus_id in ICONS:
        pattern = re.compile(r"(\tfocus = \{\r?\n\t\tid = %s\r?\n\t\ticon = )GFX_focus_generic_\w+" % re.escape(focus_id))
        text, n = pattern.subn(r"\1GFX_focus_VIE_" + stem_of(focus_id), text)
        if n == 0 and f"icon = GFX_focus_VIE_{stem_of(focus_id)}" not in text:
            raise SystemExit(f"icon line not found for {focus_id}")
    FOCUS_FILE.write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
