"""Script to build Focus Icons for Vietnam Aerospace, Make in Vietnam & Research Foundation
(Cụm 3: Hàng không Vũ trụ, Make in Vietnam & Nền tảng Nghiên cứu - 9 focuses)
in Millennium Dawn with authentic 3D Painterly / Digital Oil Painting style.

9 Focuses:
1.  viettel_global: Viettel vươn ra toàn cầu (Global Earth with international telecom transmission beams & golden laurels)
2.  make_in_vietnam: Make in Vietnam (High-tech industrial manufacturing plant, steel beams, crimson-gold shield, laurels)
3.  digital_tech_industry_law: Luật Công nghiệp Công nghệ số (Legal codex treaty parchment & pen on azure shield, bronze laurels)
4.  nafosted: Quỹ Khoa học và Công nghệ NAFOSTED (Scientific partnership handshake over research beaker, golden laurels)
5.  research_universities: Đại học nghiên cứu (Academic graduation mortarboard cap & diploma scroll in golden laurels)
6.  vinasat: Các vệ tinh VINASAT (Geostationary telecommunications satellite with wide solar arrays in deep space, laurels)
7.  earth_observation: Vệ tinh quan sát Trái đất (Remote sensing satellite with optical aperture scanning Earth, laurels)
8.  nuclear_research: Nghiên cứu hạt nhân (Glowing Rutherford atomic orbitals with fiery nuclear core, gear & laurels)
9.  science_breakthrough: Đột phá khoa học và công nghệ (Illuminated atomic science beaker in laurels, 3 gold stars capstone)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
- Brain showcase: research_space_icons_showcase.png
"""

import math
import struct
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
GFX_FILE = ROOT / "interface" / "VIE_md_focus_icons.gfx"
FOCUS_FILE = ROOT / "common" / "national_focus" / "VIE_md_focus.txt"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")

TARGET_SIZE = (93, 91)

# =========================================================================
# UTILITIES: DDS & PNG SAVER, SHADOWS, HERALDRY
# =========================================================================

def save_game_ready_icon(canvas: Image.Image, stem: str):
    """Save canvas as transparent PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    # Enforce pure alpha=0 at 1-pixel border to guarantee clean cutouts in Clausewitz engine
    w, h = TARGET_SIZE
    pixels = canvas.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    # Save PNG
    png_path = PNG_DIR / f"{stem}.png"
    canvas.save(png_path)

    # Write uncompressed 32-bit BGRA DDS
    r, g, b, a = canvas.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I",
        124, 0x100F, TARGET_SIZE[1], TARGET_SIZE[0], TARGET_SIZE[0] * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
    )
    assert len(header) == 128
    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(header + data)
    assert len(dds_path.read_bytes()) == 33980
    print(f"  [SAVED] {stem} -> PNG & DDS (33,980 bytes)")


def create_gold_star(size: int) -> Image.Image:
    """Generate a sharp 5-pointed gold star with faceted 3D shading."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1
    r_inner = r_outer * 0.382

    pts = []
    for i in range(10):
        ang = i * math.pi / 5 - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))

    draw.polygon(pts, fill=(255, 222, 35, 255), outline=(160, 120, 10, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 248, 125, 170))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(185, 135, 10, 180))
    return im


def create_gold_star_with_glow(size: int, shadow_blur: float = 1.3) -> Image.Image:
    """Generate faceted gold star with high-depth drop shadow."""
    star = create_gold_star(size)
    pad = 4
    canvas = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow.paste(star, (pad, pad + 1), star)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(shadow_blur))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(star, (pad, pad), star)
    return canvas


def create_vpa_cockade(size: int = 20) -> Image.Image:
    """Generate official Vietnam gold & red cockade roundel."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(215, 175, 45, 255), outline=(125, 90, 15, 255))
    r_inner = r_outer - 2.0
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))

    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def apply_ambient_drop_shadow(canvas: Image.Image, radius: float = 1.8) -> Image.Image:
    """Generate soft ambient occlusion drop shadow behind entire composite icon."""
    out = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    shadow.paste(canvas, (0, 1), canvas)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(radius))
    shadow_a = shadow.split()[-1].point(lambda p: int(p * 0.8))
    shadow = Image.merge("RGBA", (black, black, black, shadow_a))
    out.paste(shadow, (0, 0), shadow)
    out.paste(canvas, (0, 0), canvas)
    return out


# =========================================================================
# 9 BUILDER FUNCTIONS (CỤM 3: HÀNG KHÔNG VŨ TRỤ, MAKE IN VIETNAM & NGHIÊN CỨU)
# =========================================================================

# 1. VIE_viettel_global: Viettel vươn ra toàn cầu
def build_viettel_global() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_regions" / "global_community.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom Military/National cockade on pedestal
    cockade = create_vpa_cockade(17)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "viettel_global")
    return canvas


# 2. VIE_make_in_vietnam: Make in Vietnam
def build_make_in_vietnam() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_economy" / "industry_civilian.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Central crimson heart shield with golden star
    draw = ImageDraw.Draw(canvas)
    cx = TARGET_SIZE[0] // 2
    pts_shield = [(cx - 10, 32), (cx + 10, 32), (cx + 10, 46), (cx, 54), (cx - 10, 46)]
    draw.polygon(pts_shield, fill=(195, 25, 25, 255), outline=(245, 205, 45, 255), width=1)
    mini_star = create_gold_star(12)
    canvas.paste(mini_star, (cx - mini_star.width // 2, 35), mini_star)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade on pedestal
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "make_in_vietnam")
    return canvas


# 3. VIE_digital_tech_industry_law: Luật Công nghiệp Công nghệ số
def build_digital_tech_industry_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_diplomacy" / "treaty.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "digital_tech_industry_law")
    return canvas


# 4. VIE_nafosted: Quỹ Khoa học và Công nghệ NAFOSTED
def build_nafosted() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_science" / "scientific_exchange.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "nafosted")
    return canvas


# 5. VIE_research_universities: Đại học nghiên cứu
def build_research_universities() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_science" / "university.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "research_universities")
    return canvas


# 6. VIE_vinasat: Các vệ tinh VINASAT
def build_vinasat() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_science" / "weaponized_satellites.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "vinasat")
    return canvas


# 7. VIE_earth_observation: Vệ tinh quan sát Trái đất (VNREDSat-1)
def build_earth_observation() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "taiwan" / "tai_nspo.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade on pedestal
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "earth_observation")
    return canvas


# 8. VIE_nuclear_research: Nghiên cứu hạt nhân (Lò Đà Lạt)
def build_nuclear_research() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_science" / "circular_electron_positron_collider.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(16)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "nuclear_research")
    return canvas


# 9. VIE_science_breakthrough: Đột phá khoa học và công nghệ (Capstone)
def build_science_breakthrough() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_science" / "research4.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # 3 Faceted 3D Gold Stars across apex (Science Breakthrough Capstone)
    s_center = create_gold_star_with_glow(20)
    s_side = create_gold_star_with_glow(15)
    cx = TARGET_SIZE[0] // 2
    canvas.paste(s_center, (cx - s_center.width // 2, -1), s_center)
    canvas.paste(s_side, (cx - 24 - s_side.width // 2, 4), s_side)
    canvas.paste(s_side, (cx + 24 - s_side.width // 2, 4), s_side)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "science_breakthrough")
    return canvas


# =========================================================================
# REGISTRATION & SHOWCASE
# =========================================================================

STEMS = [
    "viettel_global", "make_in_vietnam", "digital_tech_industry_law",
    "nafosted", "research_universities", "vinasat",
    "earth_observation", "nuclear_research", "science_breakthrough"
]


def register_sprites():
    """Register all spriteTypes in VIE_md_focus_icons.gfx if missing."""
    text = GFX_FILE.read_text(encoding="utf-8")
    added = 0
    new_entries = []

    for stem in STEMS:
        sprite_name = f"GFX_focus_VIE_{stem}"
        if sprite_name not in text:
            entry = f"""\tspriteType = {{
\t\tname = "{sprite_name}"
\t\ttexturefile = "gfx/interface/goals/{stem}.dds"
\t}}"""
            new_entries.append(entry)
            added += 1

    if new_entries:
        idx = text.rfind("}")
        if idx != -1:
            updated = text[:idx] + "\n".join(new_entries) + "\n" + text[idx:]
            GFX_FILE.write_text(updated, encoding="utf-8")
            print(f"Registered {added} new spriteTypes in {GFX_FILE}")
    else:
        print("All spriteTypes already registered.")


def update_focus_tree_icons():
    """Update common/national_focus/VIE_md_focus.txt with the new GFX_focus_VIE_ icons."""
    text = FOCUS_FILE.read_text(encoding="utf-8")
    updated = text

    focus_mapping = {
        "VIE_viettel_global": "GFX_focus_VIE_viettel_global",
        "VIE_make_in_vietnam": "GFX_focus_VIE_make_in_vietnam",
        "VIE_digital_tech_industry_law": "GFX_focus_VIE_digital_tech_industry_law",
        "VIE_nafosted": "GFX_focus_VIE_nafosted",
        "VIE_research_universities": "GFX_focus_VIE_research_universities",
        "VIE_vinasat": "GFX_focus_VIE_vinasat",
        "VIE_earth_observation": "GFX_focus_VIE_earth_observation",
        "VIE_nuclear_research": "GFX_focus_VIE_nuclear_research",
        "VIE_science_breakthrough": "GFX_focus_VIE_science_breakthrough",
    }

    import re
    replaced_count = 0
    for fid, new_gfx in focus_mapping.items():
        pattern = rf"(id\s*=\s*{fid}\s*\n\s*icon\s*=\s*)(\w+)"
        if re.search(pattern, updated):
            updated, n = re.subn(pattern, rf"\g<1>{new_gfx}", updated)
            if n > 0:
                replaced_count += n
                print(f"  [FOCUS TREE] {fid} -> icon = {new_gfx}")

    if replaced_count > 0:
        FOCUS_FILE.write_text(updated, encoding="utf-8")
        print(f"Updated {replaced_count} focuses in {FOCUS_FILE}")
    else:
        print("Focus tree icons already up to date.")


def create_showcase_artifact(icons: dict[str, Image.Image]):
    """Create a contact sheet showcase image of all 9 Research & Space focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "research_space_icons_showcase.png"

    cols = 5
    rows = (len(icons) + cols - 1) // cols
    card_w, card_h = 185, 145
    pad_x, pad_y = 20, 20
    header_h = 90

    total_w = pad_x * 2 + cols * card_w + (cols - 1) * 15
    total_h = header_h + rows * card_h + (rows - 1) * 15 + pad_y

    canvas = Image.new("RGBA", (total_w, total_h), (14, 18, 24, 255))
    draw = ImageDraw.Draw(canvas)

    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 13)
        font_id = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_name = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except Exception:
        font_title = font_sub = font_id = font_name = None

    draw.text((pad_x, 20), "BỘ ICON GFX: HÀNG KHÔNG VŨ TRỤ & NỀN TẢNG NGHIÊN CỨU", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "9 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "viettel_global": "Viettel vươn ra toàn cầu",
        "make_in_vietnam": "Make in Vietnam",
        "digital_tech_industry_law": "Luật CN Công nghệ số",
        "nafosted": "Quỹ KH-CN NAFOSTED",
        "research_universities": "Đại học nghiên cứu",
        "vinasat": "Các vệ tinh VINASAT",
        "earth_observation": "Vệ tinh quan sát Trái đất",
        "nuclear_research": "Nghiên cứu hạt nhân",
        "science_breakthrough": "Đột phá KH-CN (Capstone)",
    }

    for idx, (stem, img) in enumerate(icons.items()):
        c = idx % cols
        r = idx // cols
        x = pad_x + c * (card_w + 15)
        y = header_h + r * (card_h + 15)

        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=8, fill=(22, 28, 38, 255), outline=(45, 60, 80, 255))

        icon_x = x + (card_w - img.width) // 2
        icon_y = y + 10
        canvas.paste(img, (icon_x, icon_y), img)

        t_title = focus_titles.get(stem, stem)
        draw.text((x + 8, y + card_h - 36), stem, fill=(240, 200, 80, 255), font=font_id)
        draw.text((x + 8, y + card_h - 20), t_title, fill=(200, 215, 230, 255), font=font_name)

    canvas.save(out_path)
    print(f"Showcase image saved: {out_path}")


def main():
    print("=" * 65)
    print("BUILDING 9 RESEARCH, AEROSPACE & MAKE IN VIETNAM FOCUS ICONS")
    print("=" * 65)

    built_icons = {}
    built_icons["viettel_global"] = build_viettel_global()
    built_icons["make_in_vietnam"] = build_make_in_vietnam()
    built_icons["digital_tech_industry_law"] = build_digital_tech_industry_law()
    built_icons["nafosted"] = build_nafosted()
    built_icons["research_universities"] = build_research_universities()
    built_icons["vinasat"] = build_vinasat()
    built_icons["earth_observation"] = build_earth_observation()
    built_icons["nuclear_research"] = build_nuclear_research()
    built_icons["science_breakthrough"] = build_science_breakthrough()

    print("\nRegistering GFX sprites...")
    register_sprites()

    print("\nUpdating focus tree...")
    update_focus_tree_icons()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 9 ICONS GENERATED & REGISTERED")
    print("=" * 65)


if __name__ == "__main__":
    main()
