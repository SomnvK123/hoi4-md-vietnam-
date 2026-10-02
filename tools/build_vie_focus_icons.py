"""Find, review and build Vietnam army-branch focus icons from Wikimedia Commons photographs.

Two steps, because a photo has to be looked at before it is used as a 93x91 icon:

  python tools/build_vie_focus_icons.py search [stem ...]
      For each focus (or the named stems) search Commons, keep only freely licensed images, download
      small candidates to assets/focus_icons/candidates/<stem>_<n>.jpg plus a contact sheet
      <stem>_sheet.png and candidates/meta.json (title, author, licence, url).

  python tools/build_vie_focus_icons.py build [stem ...]
      Read assets/focus_icons/selection.json  {stem: {"pick": n, "crop": [x0, y0, x1, y1]}}  (crop is
      optional, fractions of the candidate image), crop to the icon size, write
      assets/focus_icons/png/<stem>.png, gfx/interface/goals/<stem>.dds, interface/VIE_md_focus_icons.gfx
      and assets/focus_icons/CREDITS.json.

Downloads use curl (urllib is blocked by the proxy on this machine). Output DDS is uncompressed 32-bit
BGRA without mipmaps, 93x91, like Millennium Dawn's own focus icons (gfx/interface/goals/00_army/*.dds).
Run from anywhere. Pillow is required.
"""
from __future__ import annotations

import json
import re
import struct
import subprocess
import sys
import urllib.parse
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "focus_icons"
CAND = ASSETS / "candidates"
PNG = ASSETS / "png"
DDS = ROOT / "gfx" / "interface" / "goals"
GFX = ROOT / "interface" / "VIE_md_focus_icons.gfx"
SELECTION = ASSETS / "selection.json"
CREDITS = ASSETS / "CREDITS.json"
SIZE = (93, 91)
MAX_CAND = 3  # keep the review set small
UA = "hoi4-md-vietnam-focus-icons/1.0 (https://github.com/SomnvK123/hoi4-md-vietnam-)"

# focus id -> (stem, [search queries]). Stem is the file name; sprite name is GFX_focus_VIE_<stem>.
FOCI = {
    "VIE_lf_army_reform": ("lf_army_reform", ['deepcategory:"Military parades in Vietnam" parade', 'deepcategory:"Vietnam People\'s Army" parade', 'deepcategory:"Vietnam People\'s Army" soldiers marching']),
    "VIE_lf_logistics_merge": ("lf_logistics_merge", ['deepcategory:"Military vehicles of Vietnam" truck', 'deepcategory:"Military equipment of the Vietnam People\'s Army" truck', 'deepcategory:"Military vehicles of Vietnam"', 'EMB:Vietnamese People\'s Army Transport Vector']),
    "VIE_lf_basic_training": ("lf_basic_training", ['deepcategory:"Vietnam People\'s Army" training', 'deepcategory:"Military education in Vietnam"', 'deepcategory:"Vietnam People\'s Army" recruits', 'EMB:Vietnamese People\'s Army Barracks Vector']),
    "VIE_lf_arm_infantry_org": ("lf_arm_infantry_org", ['deepcategory:"Military equipment of the Vietnam People\'s Army" infantry', 'deepcategory:"Military equipment of the Vietnam People\'s Army" BTR', 'deepcategory:"Vietnam People\'s Army" infantry', 'EMB:Vietnam People\'s Army Motorized Infantry Vector']),
    "VIE_lf_arm_infantry_train": ("lf_arm_infantry_train", ['deepcategory:"Weapons of the Vietnam People\'s Army" soldier', 'deepcategory:"Vietnam People\'s Army" rifle', 'deepcategory:"Firearms of Vietnam"', 'EMB:Vietnamese People\'s Army Ammunition Vector']),
    "VIE_lf_arm_armor_org": ("lf_arm_armor_org", ['deepcategory:"Armour of Vietnam" T-54', 'deepcategory:"Armour of Vietnam" tank column', 'Vietnam T-54 tank']),
    "VIE_lf_arm_armor_train": ("lf_arm_armor_train", ['deepcategory:"Armour of Vietnam" T-90', 'deepcategory:"Armour of Vietnam" tank crew', 'deepcategory:"Military equipment of the Vietnam People\'s Army" tank', 'EMB:Vietnamese People\'s Army Tank Vector']),
    "VIE_lf_arm_arty_org": ("lf_arm_arty_org", ['deepcategory:"Military equipment of the Vietnam People\'s Army" howitzer', 'deepcategory:"Military equipment of the Vietnam People\'s Army" artillery', 'D-30 howitzer Vietnam', 'Type 59 field gun Vietnam', 'EMB:Vietnamese People\'s Army Artillery Vector']),
    "VIE_lf_arm_arty_train": ("lf_arm_arty_train", ['deepcategory:"Military equipment of the Vietnam People\'s Army" artillery crew', 'deepcategory:"Vietnam People\'s Army" artillery', 'Vietnam artillery gun crew', 'EMB:Vietnamese People\'s Army Ordnance Vector']),
    "VIE_lf_arm_engineers": ("lf_arm_engineers", ['deepcategory:"Military equipment of the Vietnam People\'s Army" engineer', 'deepcategory:"Vietnam People\'s Army" engineers', 'Vietnam pontoon bridge', 'EMB:Vietnamese People\'s Army Engineer Vector']),
    "VIE_lf_combined_arms": ("lf_combined_arms", ['deepcategory:"Vietnam People\'s Army" exercise', 'deepcategory:"Military equipment of the Vietnam People\'s Army" tank infantry', 'Vietnam military exercise', 'EMB:Vietnam People\'s Army Vector']),
    "VIE_lf_command_reform_1": ("lf_command_reform_1", ['deepcategory:"Vietnam People\'s Army" officers', 'deepcategory:"Ministry of Defence (Vietnam)"', 'Vietnam general staff', 'EMB:Vietnam People\'s Army General Staff Vector']),
    "VIE_lf_fs_mobile_force": ("lf_fs_mobile_force", ['deepcategory:"Military equipment of the Vietnam People\'s Army" BTR-60', 'deepcategory:"Armour of Vietnam" armored vehicle', 'deepcategory:"Military vehicles of Vietnam" armored', 'EMB:Vietnamese People\'s Army Motorcycle Vector']),
    "VIE_lf_fs_mobile_corps": ("lf_fs_mobile_corps", ['deepcategory:"Military equipment of the Vietnam People\'s Army" BMP', 'deepcategory:"Armour of Vietnam" BMP', 'deepcategory:"Military vehicles of Vietnam" convoy', 'EMB:Vietnam People\'s Army Motorized Infantry Vector']),
    "VIE_lf_fs_main_corps": ("lf_fs_main_corps", ['Quân đoàn 12', 'Quân đoàn 34', 'deepcategory:"Vietnam People\'s Army" corps', 'EMB:Vietnam People\'s Army Vector']),
    "VIE_lf_fs_lean_corps": ("lf_fs_lean_corps", ['Quân đoàn 34', 'deepcategory:"Flags of Vietnam People\'s Army"', 'deepcategory:"Vietnam People\'s Army" flag', 'EMB:Vietnam People\'s Army Vector']),
    "VIE_lf_fs_depth_defence": ("lf_fs_depth_defence", ['deepcategory:"Vietnam People\'s Army" bunker', 'Vietnam bunker', 'deepcategory:"Military facilities of Vietnam"', 'EMB:Vietnamese People\'s Army Engineering Arm Vector']),
    "VIE_lf_fs_militia_units": ("lf_fs_militia_units", ['deepcategory:"Vietnam Militia and Self-Defence Force"', 'dân quân tự vệ', 'EMB:Vietnam Militia Self-Defence emblem']),
    "VIE_lf_dev_strategic": ("lf_dev_strategic", ['deepcategory:"Military equipment of the Vietnam People\'s Army" helicopter', 'deepcategory:"Vietnam People\'s Air Force" helicopter', 'Vietnam Mi-8 helicopter', 'EMB:Vietnamese People\'s Army Transport Vector']),
    "VIE_lf_dev_territorial": ("lf_dev_territorial", ['deepcategory:"Vietnam People\'s Army" reserve', 'deepcategory:"Vietnam People\'s Army" soldiers', 'deepcategory:"Vietnam People\'s Ground Forces"', 'EMB:Vietnam People\'s Army Politics Vector']),
    "VIE_lf_command_reform_2": ("lf_command_reform_2", ['deepcategory:"Ministry of Defence (Vietnam)"', 'deepcategory:"Military buildings in Vietnam"', 'Vietnam military headquarters', 'EMB:Vietnam People\'s Army General Staff Vector']),
    "VIE_lf_cap_border_urban": ("lf_cap_border_urban", ['deepcategory:"Vietnam Border Defence Force"', 'Bộ đội biên phòng', 'Vietnam border guard', 'EMB:Vietnam Border Defense Force Vector']),
    "VIE_lf_cap_area_control": ("lf_cap_area_control", ['deepcategory:"Vietnam People\'s Army" street', 'deepcategory:"Military parades in Vietnam"', 'Vietnam soldiers city', 'EMB:Vietnamese People\'s Army Commando Vector']),
    "VIE_lf_cap_army_ad": ("lf_cap_army_ad", ['deepcategory:"Military equipment of the Vietnam People\'s Army" anti-aircraft', 'deepcategory:"Military equipment of the Vietnam People\'s Army" missile', 'Vietnam air defence gun', 'EMB:Insignia of the Vietnam People\'s Army Air Defence - Air Force']),
    "VIE_lf_cap_ad_coord": ("lf_cap_ad_coord", ['deepcategory:"Military of Vietnam" radar Viettel', 'Vietnamese radar station', 'Vietnam air defence radar', 'EMB:Vietnam People\'s Air Force Vector']),
    "VIE_lf_cap_cyber_ew": ("lf_cap_cyber_ew", ['deepcategory:"Military communications equipment of Vietnam"', 'deepcategory:"Military communications in Vietnam"', 'Vietnam military signal vehicle', 'EMB:Vietnam Electronic Warfare Vector']),
    "VIE_lf_cap_info_ops": ("lf_cap_info_ops", ['Viettel military', 'deepcategory:"Military communications equipment of Vietnam" radio', 'Viettel communications', 'EMB:Vietnam Cyberspace Operation Vector']),
    "VIE_lf_selective_modernization": ("lf_selective_modernization", ['K9 Thunder Vietnam', 'XCB-01', 'deepcategory:"Military equipment of the Vietnam People\'s Army" modern', 'Vietnam military expo vehicle', 'EMB:Vietnamese People\'s Army Defense Industry']),
    "VIE_lf_command_reform_3": ("lf_command_reform_3", ['Viettel', 'deepcategory:"Military communications equipment of Vietnam" command', 'Vietnam military command vehicle', 'EMB:Vietnamese People\'s Army Communications']),
    "VIE_lf_force_complete": ("lf_force_complete", ['deepcategory:"Military parades in Vietnam"', 'Duyệt binh', 'deepcategory:"Vietnam People\'s Ground Forces" parade', 'EMB:Vietnam People\'s Army Vector']),
    "VIE_modernize_vpa": ("modernize_vpa", ['deepcategory:"Vietnam People\'s Army" soldiers', 'deepcategory:"Military equipment of the Vietnam People\'s Army" soldiers', "Vietnam People's Army soldier modern", 'EMB:Vietnam People\'s Army Vector']),
    "VIE_def_industry_law": ("def_industry_law", ['Vietnam defence industry', 'deepcategory:"Military facilities of Vietnam" factory', 'Viettel factory', 'EMB:Vietnamese People\'s Army Defense Industry']),
    "VIE_military_enterprises_core": ("military_enterprises_core", ['Viettel', 'Viettel factory', 'Viettel High Tech', 'EMB:Vietnamese People\'s Army Ordnance Vector']),
    "VIE_military_enterprises_divest": ("military_enterprises_divest", ['Vietnam factory production line', 'Vietnam industrial plant', 'Vietnam factory workers', 'EMB:Vietnamese People\'s Army Petroleum Vector']),
    "VIE_path_self_reliant_deterrence": ("path_self_reliant_deterrence", ['deepcategory:"Military equipment of the Vietnam People\'s Army" self-propelled', 'PTH-152', 'XCB-01', 'EMB:Vietnam People\'s Army Rocket Vector']),
    # Naval industry axis (Truc 2 hai quan). Registry only: run `search` then review before switching the focuses
    # from their generic icons to GFX_focus_VIE_<stem>.
    "VIE_naval_defence_law": ("naval_defence_law", ['deepcategory:"Vietnam People\'s Navy"', 'Vietnam People\'s Navy ship', 'deepcategory:"Ships of the Vietnam People\'s Navy"']),
    "VIE_ba_son_shipyards": ("ba_son_shipyards", ['Ba Son Shipyard', 'Ba Son shipyard Ho Chi Minh City', 'deepcategory:"Shipyards of Vietnam"']),
    "VIE_naval_mro": ("naval_mro", ['Cam Ranh Bay naval base', 'Cam Ranh International Port', 'deepcategory:"Cam Ranh Bay"']),
    "VIE_small_combatant_construction": ("small_combatant_construction", ['Molniya class Vietnam', 'Project 1241.8 Vietnam', 'deepcategory:"Tarantul-class corvettes" Vietnam']),
    "VIE_naval_systems_integration": ("naval_systems_integration", ['Gepard-class frigate Vietnam', 'Vietnamese frigate Dinh Tien Hoang', 'deepcategory:"Gepard-class frigates"']),
    "VIE_naval_defence_2030": ("naval_defence_2030", ['Kilo-class submarine Vietnam', 'Vietnamese submarine Hanoi', 'deepcategory:"Kilo-class submarines of the Vietnam People\'s Navy"']),
    "VIE_nf_training_standardization": ("nf_training_standardization", ['Vietnam People\'s Navy Academy', 'Naval Academy Nha Trang']),
    "VIE_nf_surface_force": ("nf_surface_force", ['Gepard-class frigate Vietnam', 'Vietnam People\'s Navy frigate']),
    "VIE_nf_submarine_force": ("nf_submarine_force", ['Kilo-class submarine Vietnam', 'Vietnamese submarine Hanoi']),
    "VIE_nf_command_reform_1": ("nf_command_reform_1", ['Vietnam People\'s Navy headquarters', 'Vietnam People\'s Navy flag']),
    "VIE_nf_first_force": ("nf_first_force", ['Molniya class Vietnam', 'Vietnam People\'s Navy fleet']),
    "VIE_nf_command_reform_2": ("nf_command_reform_2", ['Vietnam People\'s Navy brigade', 'Vietnam People\'s Navy ship formation']),
    "VIE_nf_medium_force": ("nf_medium_force", ['Vietnamese frigate Dinh Tien Hoang', 'Gepard 3.9 Vietnam']),
    "VIE_nf_operating_range": ("nf_operating_range", ['Vietnam People\'s Navy ship at sea', 'Cam Ranh Bay naval base']),
    "VIE_nf_denial": ("nf_denial", ['Bastion-P Vietnam', 'K-300P Bastion-P coastal defence']),
    "VIE_nf_denial_defence": ("nf_denial_defence", ['Coastal defence missile Vietnam', 'Bastion-P launcher']),
    "VIE_nf_denial_subs": ("nf_denial_subs", ['Kilo-class submarine Vietnam', 'Project 636 Hanoi']),
    "VIE_nf_denial_command": ("nf_denial_command", ['Vietnam People\'s Navy command', 'Vietnam naval region']),
    "VIE_nf_greenwater": ("nf_greenwater", ['Vietnamese frigate Gepard', 'Vietnam People\'s Navy escort']),
    "VIE_nf_regional_frigates": ("nf_regional_frigates", ['Gepard-class frigate Vietnam', 'Sigma 9814']),
    "VIE_nf_amphibious_fleet": ("nf_amphibious_fleet", ['Vietnam amphibious ship', 'Landing ship Vietnam People\'s Navy']),
    "VIE_nf_lhd_program": ("nf_lhd_program", ['Juan Carlos I amphibious assault ship', 'Landing helicopter dock']),
    "VIE_nf_regional_command": ("nf_regional_command", ['Vietnam People\'s Navy fleet command', 'Vietnam naval flag']),
    "VIE_nf_bluewater": ("nf_bluewater", ['Vietnam People\'s Navy ship at sea', 'Vietnamese destroyer']),
    "VIE_nf_ocean_escort": ("nf_ocean_escort", ['Kolkata-class destroyer', 'Type 052D destroyer']),
    "VIE_nf_replenishment": ("nf_replenishment", ['Replenishment oiler underway', 'Fleet replenishment ship']),
    "VIE_nf_naval_aviation": ("nf_naval_aviation", ['Ka-28 helicopter Vietnam', 'Naval aviation helicopter deck']),
    "VIE_nf_carrier_group": ("nf_carrier_group", ['INS Vikrant aircraft carrier', 'Light aircraft carrier']),
}
FREE = re.compile(r"^(CC[ -]BY|CC0|Public domain|PD|Attribution|GFDL)", re.I)


def curl(url: str, out: Path | None = None) -> bytes:
    cmd = ["curl", "-sL", "--max-time", "60", "-A", UA, url]
    if out is not None:
        cmd += ["-o", str(out)]
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode != 0:
        raise RuntimeError(f"curl failed {res.returncode}: {url}")
    return res.stdout


def strip_html(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text or "")).strip()


# The Commons categories "Military of Vietnam" etc. are full of US/ARVN/Viet Cong photos from the Vietnam War.
# Those are NOT the Vietnam People's Army of 2000-2026, so reject them by category, title, description and date.
BAD_CATS = re.compile(
    r"South Vietnam|Republic of Vietnam|Vietnam War|ARVN|Army of the Republic|Viet ?Cong|Vietcong|United States|U\.S\.|"
    r"American|Australian|Korean|Indochina War|Dien Bien Phu|Battle of|Massacre|Prisoner|1950s|1960s|1970s|"
    r"Military Assistance Command|Operation |Cold War|Vietnamization|helicopters? of the United States|NLF|Anzac",
    re.I)
BAD_TITLE = re.compile(
    r"\bUS\b|\bUSA\b|U\.S\.|\bARVN\b|Viet ?Cong|\bVC\b|Marine|Battalion|Brigade, [0-9]|Airborne|Screaming Eagle|Anzac|"
    r"\bRAR\b|Nixon|Saigon|Tan Son Nhut|Khe Sanh|Hue 1968|\b19[4-8]\d\b|Firebase|Fire Base|Camp |"
    r"Phu Lam|Long Binh|Pleiku Integrated|Cholon|Counter-battery|Huey|\bUH-1|\bM60\b|\bM79\b|\bM16\b|\bF-4\b",
    re.I)
BAD_DESC = re.compile(r"Vietnam War|1965|1966|1967|1968|1969|1970|1971|1972|U\.S\. Army|United States Army|US Army|ARVN|Viet ?Cong", re.I)


VPA = re.compile(
    r"Vietnam People|People's Army of Vietnam|Vietnam(ese)? (People's )?(Army|Armed Forces|military)|Viettel|Quân đội nhân dân|Bộ đội|"
    r"Duyệt binh|Quân đoàn|dân quân|Border Defence Force|Militia and Self-Defence|Military equipment of the Vietnam|Armour of Vietnam",
    re.I)


def is_wrong_era(title: str, meta: dict) -> bool:
    cats = meta.get("Categories", {}).get("value", "")
    desc = strip_html(meta.get("ImageDescription", {}).get("value", ""))
    if BAD_CATS.search(cats) or BAD_TITLE.search(title) or BAD_DESC.search(desc):
        return True
    if not VPA.search(cats + " " + title + " " + desc):  # must clearly be the Vietnam People's Army / its equipment
        return True
    when = meta.get("DateTimeOriginal", {}).get("value", "") + " " + meta.get("DateTime", {}).get("value", "")
    years = [int(y) for y in re.findall(r"\b(19\d\d|20\d\d)\b", when)]
    return bool(years) and min(years) < 1995  # before 1995 = war era or earlier; modern photos only


def search(query: str, limit: int = 12) -> list[dict]:
    params = {
        "action": "query", "generator": "search", "gsrsearch": query, "gsrnamespace": 6, "gsrlimit": limit,
        "prop": "imageinfo", "iiprop": "url|mime|size|extmetadata", "iiurlwidth": 700, "format": "json",
    }
    payload = json.loads(curl("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)))
    out = []
    for page in sorted(payload.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0)):
        info = (page.get("imageinfo") or [{}])[0]
        if info.get("mime") not in ("image/jpeg", "image/png"):
            continue
        meta = info.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        if not FREE.match(lic):
            continue
        if info.get("width", 0) < 500 or info.get("height", 0) < 350:
            continue
        if is_wrong_era(page.get("title", ""), meta):
            continue
        out.append({
            "title": page.get("title", ""), "thumb": info.get("thumburl") or info.get("url"),
            "page": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(page.get("title", "").replace(" ", "_")),
            "license": lic, "author": strip_html(meta.get("Artist", {}).get("value", ""))[:120],
        })
    return out


def do_search(stems: list[str]) -> None:
    CAND.mkdir(parents=True, exist_ok=True)
    metap = CAND / "meta.json"
    meta = json.loads(metap.read_text(encoding="utf-8")) if metap.exists() else {}
    for fid, (stem, queries) in FOCI.items():
        if stems and stem not in stems:
            continue
        seen, found = set(), []
        photos, emblems = [], []
        for q in queries:
            try:
                emb = q.startswith("EMB:")
                for c in search(q[4:] if emb else q):
                    if c["title"] not in seen:
                        seen.add(c["title"])
                        (emblems if emb else photos).append(c)
            except Exception as exc:  # network hiccup on one query must not stop the rest
                print(f"  {stem}: query '{q}' failed: {exc}")
        # up to 2 photographs and up to 2 branch emblems (public-domain vectors) per focus
        found = photos[:2] + emblems[:2]
        thumbs = []
        for i, c in enumerate(found, 1):
            path = CAND / f"{stem}_{i}.jpg"
            try:
                curl(c["thumb"], path)
                Image.open(path).verify()
                thumbs.append((i, path))
                c["file"] = path.name
            except Exception:
                path.unlink(missing_ok=True)
        meta[stem] = [c for c in found if "file" in c]
        make_sheet(stem, thumbs)
        print(f"{stem}: {len(thumbs)} candidates")
    metap.write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def make_sheet(stem: str, thumbs: list[tuple[int, Path]]) -> None:
    if not thumbs:
        return
    tw, th, cols = 300, 220, 4
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), (30, 30, 30))
    for k, (i, path) in enumerate(thumbs):
        img = Image.open(path).convert("RGB")
        img.thumbnail((tw - 6, th - 6))
        x, y = (k % cols) * tw + 3, (k // cols) * th + 3
        sheet.paste(img, (x, y))
        ImageDraw.Draw(sheet).rectangle((x, y, x + 24, y + 18), fill=(0, 0, 0))
        ImageDraw.Draw(sheet).text((x + 4, y + 3), str(i), fill=(255, 255, 0))
    sheet.save(CAND / f"{stem}_sheet.png")


def crop_icon(img: Image.Image, crop: list[float] | None) -> Image.Image:
    img = img.convert("RGB")
    ratio = SIZE[0] / SIZE[1]
    if crop:
        x0, y0, x1, y1 = (crop[0] * img.width, crop[1] * img.height, crop[2] * img.width, crop[3] * img.height)
    else:
        x0, y0, x1, y1 = 0, 0, img.width, img.height
    w, h = x1 - x0, y1 - y0
    if w / h > ratio:  # too wide: trim sides around the centre
        nw = h * ratio
        x0, x1 = x0 + (w - nw) / 2, x0 + (w + nw) / 2
    else:
        nh = w / ratio
        y0, y1 = y0 + (h - nh) / 2, y0 + (h + nh) / 2
    out = img.crop((round(x0), round(y0), round(x1), round(y1))).resize(SIZE, Image.Resampling.LANCZOS)
    # small icons need punch: mild contrast, colour and sharpening, then a dark inner edge
    out = ImageEnhance.Contrast(out).enhance(1.15)
    out = ImageEnhance.Color(out).enhance(1.05)
    out = out.filter(ImageFilter.UnsharpMask(radius=1.0, percent=70, threshold=2))
    ImageDraw.Draw(out).rectangle((0, 0, SIZE[0] - 1, SIZE[1] - 1), outline=(20, 20, 20))
    return out


def write_dds(path: Path, img: Image.Image) -> None:
    w, h = img.size
    r, g, b, a = img.convert("RGBA").split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I", 124, 0x100F, h, w, w * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0)
    assert len(header) == 128
    path.write_bytes(header + data)


def do_build(stems: list[str]) -> None:
    sel = json.loads(SELECTION.read_text(encoding="utf-8"))
    meta = json.loads((CAND / "meta.json").read_text(encoding="utf-8"))
    PNG.mkdir(parents=True, exist_ok=True)
    DDS.mkdir(parents=True, exist_ok=True)
    credits = json.loads(CREDITS.read_text(encoding="utf-8")) if CREDITS.exists() else {}
    for fid, (stem, _) in FOCI.items():
        if stem not in sel or (stems and stem not in stems):
            continue
        s = sel[stem]
        src = s.get("from", stem)  # a pick may come from another focus's candidate list
        cand = next(c for c in meta[src] if c["file"] == f"{src}_{s['pick']}.jpg")
        img = crop_icon(Image.open(CAND / cand["file"]), s.get("crop"))
        img.save(PNG / f"{stem}.png")
        write_dds(DDS / f"{stem}.dds", img)
        credits[stem] = {"focus": fid, "title": cand["title"], "author": cand["author"], "license": cand["license"], "url": cand["page"]}
        print(f"built {stem} <- {cand['title']}")
    CREDITS.write_text(json.dumps(credits, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    lines = ["spriteTypes = {"]
    for fid, (stem, _) in FOCI.items():
        if (DDS / f"{stem}.dds").exists():
            lines += ["\tspriteType = {", f'\t\tname = "GFX_focus_VIE_{stem}"', f'\t\ttexturefile = "gfx/interface/goals/{stem}.dds"', "\t}"]
    lines.append("}")
    GFX.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    mode, rest = (sys.argv[1] if len(sys.argv) > 1 else ""), sys.argv[2:]
    if mode == "search":
        do_search(rest)
    elif mode == "build":
        do_build(rest)
    else:
        print(__doc__)
