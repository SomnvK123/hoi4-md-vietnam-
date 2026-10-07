"""Script to build Focus Icons for Vietnam Rule of Law, Constitution & Social Legislation
(Cụm 4: Hiến pháp, Pháp quyền & Lập pháp Xã hội - 7 focuses)
in Millennium Dawn with authentic 3D Painterly / Heraldic Relief style.

7 Focuses:
1.  rule_of_law_state: Nhà nước pháp quyền xã hội chủ nghĩa (Marble pillar of law, golden balance scale of justice, national shield, laurel)
2.  constitution_2013: Thi hành Hiến pháp 2013 (Monumental crimson leather 2013 Constitution codex, gold coat of arms star, laurel)
3.  cybersecurity_law: Luật An ninh mạng (Digital cyber aegis shield, binary lock, cyber sword defending national sovereignty)
4.  higher_education_law: Luật Giáo dục đại học sửa đổi (University autonomous tower, academic mortarboard, diploma scroll, torch)
5.  education_law_2019: Luật Giáo dục 2019 (Open book of national education radiating dawn light, gold fountain pen, laurel)
6.  disaster_law_2013: Luật Phòng, chống thiên tai (Protective sea dike sea wall breaking storm surge waves, rescue lifebuoy, star)
7.  civil_defense_law_2023: Luật Phòng thủ dân sự (Civil defense triangle crest on steel rescue shield, emergency protection star)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
- Brain showcase: law_constitution_icons_showcase.png
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

STEMS = [
    "rule_of_law_state",
    "constitution_2013",
    "cybersecurity_law",
    "higher_education_law",
    "education_law_2019",
    "disaster_law_2013",
    "civil_defense_law_2023",
]

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


def create_golden_laurel_wreath(w: int = 86, h: int = 76, gold_hue: bool = True) -> Image.Image:
    """Render procedural 3D metallic laurel wreath with leaves and berries."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    cx = w / 2
    cy = h / 2 + 6
    rx = w / 2 - 5
    ry = h / 2 - 5

    c_leaf = (235, 190, 45, 255) if gold_hue else (210, 175, 75, 255)
    c_leaf_hl = (255, 245, 140, 220) if gold_hue else (245, 225, 150, 220)
    c_shadow = (120, 85, 15, 255)

    for i in range(12):
        frac = i / 11.0
        ang_left = math.pi * 0.55 + frac * math.pi * 0.95
        ang_right = math.pi * 0.45 - frac * math.pi * 0.95

        lx = cx + rx * math.cos(ang_left)
        ly = cy + ry * math.sin(ang_left)
        l_leaf_ang = ang_left - 0.4

        rx_pt = cx + rx * math.cos(ang_right)
        ry_pt = cy + ry * math.sin(ang_right)
        r_leaf_ang = ang_right + 0.4

        leaf_len = 8.5 - frac * 2.0
        leaf_w = 4.0

        for px, py, lang in [(lx, ly, l_leaf_ang), (rx_pt, ry_pt, r_leaf_ang)]:
            tip_x = px + leaf_len * math.cos(lang)
            tip_y = py + leaf_len * math.sin(lang)
            norm_x = -math.sin(lang) * leaf_w * 0.5
            norm_y = math.cos(lang) * leaf_w * 0.5

            pts = [(px, py), (px + leaf_len * 0.5 * math.cos(lang) + norm_x, py + leaf_len * 0.5 * math.sin(lang) + norm_y),
                   (tip_x, tip_y), (px + leaf_len * 0.5 * math.cos(lang) - norm_x, py + leaf_len * 0.5 * math.sin(lang) - norm_y)]
            draw.polygon(pts, fill=c_leaf, outline=c_shadow)
            draw.line([(px, py), (tip_x, tip_y)], fill=c_leaf_hl, width=1)

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
# 7 BUILDER FUNCTIONS (CỤM 4: HIẾN PHÁP & LẬP PHÁP XÃ HỘI)
# =========================================================================

# 1. VIE_rule_of_law_state: Nhà nước pháp quyền xã hội chủ nghĩa
def build_rule_of_law_state() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Court / Scale of Justice
    base_p = MD_GOALS / "00_politics" / "focus_generic_court.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Marble Pillar & Golden Law Balance Scale of Socialist Rule of Law
    pillar = Image.new("RGBA", (50, 40), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(pillar)
    # Classical marble pillar column
    pdraw.rectangle([18, 12, 32, 34], fill=(235, 235, 240, 255), outline=(215, 175, 45, 255), width=2)
    # Pillar capital (top) and base
    pdraw.rectangle([14, 8, 36, 12], fill=(245, 205, 55, 255), outline=(130, 90, 15, 255))
    pdraw.rectangle([14, 34, 36, 38], fill=(245, 205, 55, 255), outline=(130, 90, 15, 255))
    # Red & gold law shield on column
    pdraw.rounded_rectangle([19, 15, 31, 31], radius=3, fill=(185, 20, 20, 255), outline=(255, 235, 120, 255))
    s_pil = create_gold_star(8)
    pillar.paste(s_pil, (21, 19), s_pil)
    canvas.paste(pillar, ((TARGET_SIZE[0] - pillar.width) // 2, 36), pillar)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "rule_of_law_state")
    return canvas


# 2. VIE_constitution_2013: Thi hành Hiến pháp 2013
def build_constitution_2013() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Constitution Codex / Parliament
    base_p = MD_GOALS / "00_politics" / "Focus_Parliament_Constitution.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Monumental 2013 Constitution Book in Red Leather & Gold Lettering
    book13 = Image.new("RGBA", (56, 36), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(book13)
    # Red leather binding
    bdraw.rounded_rectangle([2, 2, 54, 34], radius=5, fill=(185, 20, 20, 255), outline=(245, 215, 60, 255), width=2)
    # Gold spine divider
    bdraw.line([(28, 2), (28, 34)], fill=(245, 215, 60, 255), width=2)
    # Left page: Vietnamese Coat of Arms gold star inside cockade
    bdraw.ellipse([8, 8, 24, 24], fill=(205, 25, 25, 255), outline=(255, 235, 120, 255), width=1)
    s_b13 = create_gold_star(11)
    book13.paste(s_b13, (10, 10), s_b13)
    # Right page: Text "HIEN PHAP 2013" in gold
    try:
        font_hp = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 9)
    except Exception:
        font_hp = ImageFont.load_default()
    bdraw.text((31, 6), "HIEN", fill=(255, 235, 120, 255), font=font_hp)
    bdraw.text((31, 15), "PHAP", fill=(255, 235, 120, 255), font=font_hp)
    bdraw.text((31, 24), "2013", fill=(255, 235, 120, 255), font=font_hp)
    canvas.paste(book13, ((TARGET_SIZE[0] - book13.width) // 2, 38), book13)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "constitution_2013")
    return canvas


# 3. VIE_cybersecurity_law: Luật An ninh mạng (2018)
def build_cybersecurity_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Cybersecurity Aegis Shield
    shield = Image.new("RGBA", (76, 72), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shield)
    # Outer gold rim
    pts = [(38, 4), (68, 14), (64, 46), (38, 68), (12, 46), (8, 14)]
    sdraw.polygon(pts, fill=(20, 45, 75, 255), outline=(245, 215, 60, 255), width=2)
    # Inner dark cobalt blue shield
    pts_in = [(38, 9), (62, 18), (59, 44), (38, 62), (17, 44), (14, 18)]
    sdraw.polygon(pts_in, fill=(15, 30, 55, 255), outline=(30, 160, 240, 220), width=1)
    # Cybernetic binary circuit traces on shield
    sdraw.line([(38, 10), (38, 30)], fill=(40, 220, 240, 255), width=2)
    sdraw.line([(20, 24), (38, 30)], fill=(40, 220, 240, 255), width=1)
    sdraw.line([(56, 24), (38, 30)], fill=(40, 220, 240, 255), width=1)
    # Digital Security Padlock in center
    sdraw.rounded_rectangle([28, 34, 48, 48], radius=3, fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    sdraw.arc([32, 26, 44, 38], start=180, end=0, fill=(235, 195, 45, 255), width=3)
    s_lock = create_gold_star(8)
    shield.paste(s_lock, (34, 37), s_lock)
    canvas.paste(shield, ((TARGET_SIZE[0] - shield.width) // 2, 8), shield)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "cybersecurity_law")
    return canvas


# 4. VIE_higher_education_law: Luật Giáo dục đại học sửa đổi
def build_higher_education_law() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Education Reform / Academic Hall
    base_p = MD_GOALS / "00_politics" / "free_higher_education.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # University Academic Mortarboard & Autonomous Diploma Scroll
    acad = Image.new("RGBA", (48, 36), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(acad)
    # Mortarboard diamond cap
    adraw.polygon([(24, 6), (44, 14), (24, 22), (4, 14)], fill=(30, 35, 45, 255), outline=(245, 215, 60, 255), width=2)
    # Mortarboard skullcap base
    adraw.chord([12, 14, 36, 28], start=0, end=180, fill=(30, 35, 45, 255), outline=(245, 215, 60, 255), width=1)
    # Golden tassel hanging to right
    adraw.line([(24, 14), (40, 22)], fill=(255, 235, 120, 255), width=2)
    adraw.ellipse([38, 20, 42, 24], fill=(255, 235, 120, 255))
    # Diploma scroll below with red ribbon
    adraw.rounded_rectangle([8, 26, 40, 34], radius=3, fill=(245, 245, 235, 255), outline=(225, 185, 45, 255), width=1)
    adraw.rectangle([20, 26, 28, 34], fill=(200, 25, 25, 255))
    canvas.paste(acad, ((TARGET_SIZE[0] - acad.width) // 2, 42), acad)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "higher_education_law")
    return canvas


# 5. VIE_education_law_2019: Luật Giáo dục 2019
def build_education_law_2019() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Education Reform Book
    base_p = MD_GOALS / "00_politics" / "education_reform.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Open Textbook of National Education 2019 & Gilded Fountain Pen
    edubook = Image.new("RGBA", (50, 34), (0, 0, 0, 0))
    edraw = ImageDraw.Draw(edubook)
    # Open white-gold book pages
    edraw.polygon([(4, 10), (25, 6), (25, 28), (4, 32)], fill=(245, 245, 235, 255), outline=(225, 185, 45, 255), width=2)
    edraw.polygon([(25, 6), (46, 10), (46, 32), (25, 28)], fill=(245, 245, 235, 255), outline=(225, 185, 45, 255), width=2)
    # Red star on left page
    s_ed = create_gold_star(9)
    edubook.paste(s_ed, (8, 14), s_ed)
    # Lines on right page
    for y in [12, 18, 24]:
        edraw.line([(29, y), (42, y)], fill=(80, 95, 110, 255), width=1)
    # Golden quill / fountain pen writing
    edraw.line([(22, 28), (38, 4)], fill=(245, 205, 55, 255), width=3)
    edraw.polygon([(38, 4), (42, 1), (40, 7)], fill=(255, 245, 150, 255))
    canvas.paste(edubook, ((TARGET_SIZE[0] - edubook.width) // 2, 42), edubook)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "education_law_2019")
    return canvas


# 6. VIE_disaster_law_2013: Luật Phòng, chống thiên tai
def build_disaster_law_2013() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Protective Sea Dike Sea Wall breaking storm surge waves
    sea = Image.new("RGBA", (78, 68), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sea)
    # Deep stormy ocean blue background
    sdraw.rectangle([4, 10, 74, 58], fill=(20, 50, 85, 255))
    # Crashing sea storm waves
    for x in range(6, 72, 12):
        sdraw.arc([x, 26, x + 12, 42], start=180, end=0, fill=(180, 220, 245, 255), width=3)
    # Solid concrete sea dike wall in forefront
    sdraw.polygon([(4, 42), (74, 42), (70, 62), (8, 62)], fill=(120, 130, 145, 255), outline=(235, 195, 45, 255), width=2)
    # Sea wall stone blocks texture
    for sx in [20, 36, 52]:
        sdraw.line([(sx, 42), (sx, 62)], fill=(80, 90, 105, 255), width=1)
    canvas.paste(sea, ((TARGET_SIZE[0] - sea.width) // 2, 10), sea)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Red & White Rescue Lifebuoy with National Cockade Star in center
    buoy = Image.new("RGBA", (38, 38), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(buoy)
    bdraw.ellipse([2, 2, 36, 36], fill=(245, 245, 240, 255), outline=(215, 175, 45, 255), width=2)
    # Red quarters of lifebuoy
    bdraw.pieslice([2, 2, 36, 36], start=315, end=45, fill=(205, 25, 25, 255))
    bdraw.pieslice([2, 2, 36, 36], start=135, end=225, fill=(205, 25, 25, 255))
    # Inner cutout
    bdraw.ellipse([11, 11, 27, 27], fill=(20, 50, 85, 255), outline=(215, 175, 45, 255), width=1)
    # Center star
    s_buoy = create_gold_star(10)
    buoy.paste(s_buoy, (14, 14), s_buoy)
    canvas.paste(buoy, ((TARGET_SIZE[0] - buoy.width) // 2, 36), buoy)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "disaster_law_2013")
    return canvas


# 7. VIE_civil_defense_law_2023: Luật Phòng thủ dân sự
def build_civil_defense_law_2023() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Military / Defense Mission Shield
    base_p = MD_GOALS / "00_security" / "home_defense.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # International & National Civil Defense Crest (Orange circle, Blue triangle, Gold star)
    civdef = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(civdef)
    # International Civil Defense orange roundel
    cdraw.ellipse([2, 2, 42, 42], fill=(235, 120, 20, 255), outline=(245, 215, 60, 255), width=2)
    # Equilateral blue equilateral triangle
    cdraw.polygon([(22, 6), (38, 34), (6, 34)], fill=(15, 55, 130, 255), outline=(255, 235, 120, 255), width=2)
    # Central golden star of Vietnam
    s_cd = create_gold_star(12)
    civdef.paste(s_cd, (16, 17), s_cd)
    canvas.paste(civdef, ((TARGET_SIZE[0] - civdef.width) // 2, 34), civdef)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "civil_defense_law_2023")
    return canvas


# =========================================================================
# REGISTRATION & INTEGRATION
# =========================================================================

def register_sprites():
    """Register spriteTypes in interface/VIE_md_focus_icons.gfx."""
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
        "VIE_rule_of_law_state": "GFX_focus_VIE_rule_of_law_state",
        "VIE_constitution_2013": "GFX_focus_VIE_constitution_2013",
        "VIE_cybersecurity_law": "GFX_focus_VIE_cybersecurity_law",
        "VIE_higher_education_law": "GFX_focus_VIE_higher_education_law",
        "VIE_education_law_2019": "GFX_focus_VIE_education_law_2019",
        "VIE_disaster_law_2013": "GFX_focus_VIE_disaster_law_2013",
        "VIE_civil_defense_law_2023": "GFX_focus_VIE_civil_defense_law_2023",
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
    """Create a contact sheet showcase image of all 7 Rule of Law & Constitution focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "law_constitution_icons_showcase.png"

    cols = 4
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

    draw.text((pad_x, 20), "BỘ ICON GFX: HIẾN PHÁP & LẬP PHÁP XÃ HỘI (CỤM 4)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "7 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "rule_of_law_state": "Nhà nước pháp quyền XHCN",
        "constitution_2013": "Thi hành Hiến pháp 2013",
        "cybersecurity_law": "Luật An ninh mạng 2018",
        "higher_education_law": "Luật Giáo dục Đại học",
        "education_law_2019": "Luật Giáo dục năm 2019",
        "disaster_law_2013": "Luật Phòng chống thiên tai",
        "civil_defense_law_2023": "Luật Phòng thủ dân sự",
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
    print("BUILDING 7 RULE OF LAW & SOCIAL LEGISLATION FOCUS ICONS")
    print("=" * 65)

    built_icons = {}
    built_icons["rule_of_law_state"] = build_rule_of_law_state()
    built_icons["constitution_2013"] = build_constitution_2013()
    built_icons["cybersecurity_law"] = build_cybersecurity_law()
    built_icons["higher_education_law"] = build_higher_education_law()
    built_icons["education_law_2019"] = build_education_law_2019()
    built_icons["disaster_law_2013"] = build_disaster_law_2013()
    built_icons["civil_defense_law_2023"] = build_civil_defense_law_2023()

    print("\nRegistering GFX sprites...")
    register_sprites()

    print("\nUpdating focus tree...")
    update_focus_tree_icons()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 7 ICONS GENERATED & REGISTERED")
    print("=" * 65)


if __name__ == "__main__":
    main()
