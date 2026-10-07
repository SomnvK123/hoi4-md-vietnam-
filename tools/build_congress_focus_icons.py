"""Script to build Focus Icons for Vietnam Party Congress & Era of Rising Spine
(Cụm 1: Đại hội Đảng & Trục Kỷ nguyên mới - 11 focuses)
in Millennium Dawn with authentic 3D Painterly / Heraldic Relief style.

11 Focuses:
1.  prepare_congress_9: Chuẩn bị Đại hội IX (Party Congress banner, red leather documents portfolio, golden quill & laurel)
2.  resolution_congress_9: Nghị quyết Đại hội IX - 2001 (Roman 'IX' in minted gold medallion, industrial factory & gear, laurel)
3.  resolution_congress_10: Nghị quyết Đại hội X - 2006 (Roman 'X' in minted gold medallion, global WTO globe, laurel)
4.  resolution_congress_11: Nghị quyết Đại hội XI - 2011 (Roman 'XI' in minted gold medallion, Platform 2011 codex & torch, laurel)
5.  resolution_congress_12: Nghị quyết Đại hội XII - 2016 (Roman 'XII' in minted gold medallion, iron discipline sword & shield, laurel)
6.  resolution_congress_13: Nghị quyết Đại hội XIII - 2021 (Roman 'XIII' in minted gold medallion, high-tech digital circuits & data, laurel)
7.  resolution_congress_14: Nghị quyết Đại hội XIV - 2026 (Roman 'XIV' in minted gold medallion, triumphal portal to new era sunrise, star)
8.  concentration_of_power: Lãnh đạo hạt nhân: tập trung quyền lực (Imperial golden dragon seal on crimson pedestal, sword)
9.  institutional_opening: Mở rộng giám sát thể chế (Golden scale of justice, golden master key, National Assembly dome)
10. era_of_rising: Kỷ nguyên vươn mình của dân tộc (Golden Lac bird ascending over bronze drum sunrise, 3 gold stars)
11. party_centennial_2030: Một trăm năm thành lập Đảng - 1930-2030 (Centennial gold medallion '100', hammer & sickle, ribbon '1930-2030')

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
- Brain showcase: congress_spine_icons_showcase.png
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
    "prepare_congress_9",
    "resolution_congress_9",
    "resolution_congress_10",
    "resolution_congress_11",
    "resolution_congress_12",
    "resolution_congress_13",
    "resolution_congress_14",
    "concentration_of_power",
    "institutional_opening",
    "era_of_rising",
    "party_centennial_2030",
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


def draw_hammer_and_sickle(size: int = 24) -> Image.Image:
    """Generate official Communist gold Hammer and Sickle emblem."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2

    # Hammer handle (diagonal shaft)
    draw.line([(cx - 6, cy + 8), (cx + 6, cy - 4)], fill=(245, 195, 35, 255), width=2)
    # Hammer head
    draw.polygon([(cx + 3, cy - 7), (cx + 8, cy - 2), (cx + 6, cy), (cx + 1, cy - 5)], fill=(255, 225, 80, 255), outline=(130, 90, 10, 255))
    # Sickle curved blade
    draw.arc([cx - 9, cy - 9, cx + 5, cy + 5], start=110, end=320, fill=(255, 225, 80, 255), width=2)
    # Sickle handle
    draw.line([(cx - 7, cy + 3), (cx - 8, cy + 8)], fill=(180, 120, 20, 255), width=2)

    return im


def create_congress_medallion(roman_text: str, font_size: int = 26, w: int = 58, h: int = 34) -> Image.Image:
    """Create a minted heraldic state medallion badge with embossed gold rim and 3D Roman text."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    # Outer beveled gold rim
    draw.rounded_rectangle([0, 0, w - 1, h - 1], radius=7, fill=(225, 185, 45, 255), outline=(130, 90, 15, 255), width=1)
    draw.rounded_rectangle([2, 2, w - 3, h - 3], radius=5, fill=(255, 235, 120, 255))

    # Inner rich crimson enamel field
    draw.rounded_rectangle([3, 3, w - 4, h - 4], radius=4, fill=(185, 20, 20, 255), outline=(140, 15, 15, 255), width=1)

    # Filigree inner border
    draw.rounded_rectangle([5, 5, w - 6, h - 6], radius=3, outline=(245, 205, 55, 180), width=1)

    # 3D Roman Numeral text
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), roman_text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (w - tw) // 2 - bbox[0]
    ty = (h - th) // 2 - bbox[1]

    # Text shadow
    draw.text((tx + 1, ty + 2), roman_text, font=font, fill=(45, 5, 5, 230))
    # Text dark bronze outline
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx or dy:
                draw.text((tx + dx, ty + dy), roman_text, font=font, fill=(110, 75, 10, 255))
    # Text gold body
    draw.text((tx, ty), roman_text, font=font, fill=(255, 220, 45, 255))
    # Specular highlight
    draw.text((tx, ty - 1), roman_text, font=font, fill=(255, 250, 175, 210))

    # Drop shadow for entire medallion
    pad = 4
    canvas = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    shadow.paste(im, (pad, pad + 2), im)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(1.8))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(im, (pad, pad), im)
    return canvas


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

    # 12 leaf pairs along elliptical arc
    for i in range(12):
        frac = i / 11.0
        ang_left = math.pi * 0.55 + frac * math.pi * 0.95
        ang_right = math.pi * 0.45 - frac * math.pi * 0.95

        # Left branch
        lx = cx + rx * math.cos(ang_left)
        ly = cy + ry * math.sin(ang_left)
        l_leaf_ang = ang_left - 0.4

        # Right branch
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
# 11 BUILDER FUNCTIONS (CỤM 1: ĐẠI HỘI ĐẢNG & KỶ NGUYÊN MỚI)
# =========================================================================

# 1. VIE_prepare_congress_9: Chuẩn bị Đại hội IX
def build_prepare_congress_9() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Party Communist banner & emblem
    base_p = MD_GOALS / "china" / "communist_party_of_china.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((78, 68), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    # Golden laurels embracing the congress banner
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Leather document portfolio & golden quill
    doc = Image.new("RGBA", (44, 28), (0, 0, 0, 0))
    ddraw = ImageDraw.Draw(doc)
    # Red leather portfolio with gold corner trim
    ddraw.rounded_rectangle([0, 0, 42, 26], radius=4, fill=(175, 20, 20, 255), outline=(225, 185, 45, 255), width=2)
    ddraw.line([(21, 0), (21, 26)], fill=(225, 185, 45, 255), width=2)
    # Gold star on cover
    gstar = create_gold_star(12)
    doc.paste(gstar, (5, 7), gstar)
    # Gold quill pen slanted
    ddraw.line([(26, 22), (38, 4)], fill=(245, 215, 75, 255), width=2)
    ddraw.polygon([(38, 4), (41, 1), (40, 7)], fill=(255, 245, 140, 255))
    canvas.paste(doc, ((TARGET_SIZE[0] - doc.width) // 2, 52), doc)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "prepare_congress_9")
    return canvas


# 2. VIE_resolution_congress_9: Nghị quyết Đại hội IX (2001 - Công nghiệp hoá)
def build_resolution_congress_9() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Industrial Factory & Gear
    base_p = MD_GOALS / "00_economy" / "focus_generic_communist_industry.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.18)
    base = base.resize((82, 72), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Minted Heraldic Medallion "IX"
    medallion = create_congress_medallion("IX", font_size=25, w=54, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 28), medallion)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_congress_9")
    return canvas


# 3. VIE_resolution_congress_10: Nghị quyết Đại hội X (2006 - Đổi mới & Hội nhập WTO)
def build_resolution_congress_10() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Global Trade & WTO
    base_p = MD_GOALS / "00_organizations" / "wto.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Minted Heraldic Medallion "X"
    medallion = create_congress_medallion("X", font_size=26, w=50, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 28), medallion)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_congress_10")
    return canvas


# 4. VIE_resolution_congress_11: Nghị quyết Đại hội XI (2011 - Cương lĩnh 2011)
def build_resolution_congress_11() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Constitution / Parliament Codex
    base_p = MD_GOALS / "00_politics" / "Focus_Parliament_Constitution.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Minted Heraldic Medallion "XI"
    medallion = create_congress_medallion("XI", font_size=25, w=54, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 28), medallion)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_congress_11")
    return canvas


# 5. VIE_resolution_congress_12: Nghị quyết Đại hội XII (2016 - Chỉnh đốn Đảng & Kỷ luật thép)
def build_resolution_congress_12() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Heraldic Steel Shield & Sword of Discipline
    shield = Image.new("RGBA", (76, 72), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shield)
    # Shield shape
    pts = [(38, 4), (68, 14), (64, 46), (38, 68), (12, 46), (8, 14)]
    sdraw.polygon(pts, fill=(35, 45, 60, 255), outline=(225, 185, 45, 255), width=2)
    # Inner crimson crest
    pts_in = [(38, 9), (62, 18), (59, 44), (38, 62), (17, 44), (14, 18)]
    sdraw.polygon(pts_in, fill=(155, 20, 20, 240), outline=(120, 15, 15, 255), width=1)

    # Vertical golden sword of discipline through center
    sdraw.line([(38, 2), (38, 66)], fill=(245, 215, 75, 255), width=2)
    # Sword crossguard
    sdraw.line([(28, 16), (48, 16)], fill=(245, 215, 75, 255), width=3)
    # Pommel
    sdraw.ellipse([35, 0, 41, 6], fill=(255, 235, 120, 255))
    canvas.paste(shield, ((TARGET_SIZE[0] - shield.width) // 2, 8), shield)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Minted Heraldic Medallion "XII"
    medallion = create_congress_medallion("XII", font_size=24, w=58, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 28), medallion)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_congress_12")
    return canvas


# 6. VIE_resolution_congress_13: Nghị quyết Đại hội XIII (2021 - Tinh gọn & Chuyển đổi số)
def build_resolution_congress_13() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # High-tech glowing digital circular grid
    grid = Image.new("RGBA", (76, 76), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grid)
    for r in range(12, 36, 6):
        gdraw.ellipse([38 - r, 38 - r, 38 + r, 38 + r], outline=(30, 160, 240, 180), width=1)
    for ang_deg in range(0, 360, 30):
        rad = math.radians(ang_deg)
        gdraw.line([(38, 38), (38 + 35 * math.cos(rad), 38 + 35 * math.sin(rad))], fill=(20, 200, 220, 120), width=1)
    canvas.paste(grid, ((TARGET_SIZE[0] - grid.width) // 2, 10), grid)

    # Base Communist Flag
    base_p = MD_GOALS / "china" / "communist_party_of_china.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = base.resize((74, 64), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 12), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Minted Heraldic Medallion "XIII"
    medallion = create_congress_medallion("XIII", font_size=23, w=62, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 28), medallion)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_congress_13")
    return canvas


# 7. VIE_resolution_congress_14: Nghị quyết Đại hội XIV (2026 - Kỷ nguyên mới)
def build_resolution_congress_14() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base National Unity Sunburst / Dawn
    base_p = MD_GOALS / "00_politics" / "national_unity_red.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 72), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Minted Heraldic Medallion "XIV"
    medallion = create_congress_medallion("XIV", font_size=24, w=60, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 28), medallion)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "resolution_congress_14")
    return canvas


# 8. VIE_concentration_of_power: Lãnh đạo hạt nhân: tập trung quyền lực
def build_concentration_of_power() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Supreme Leadership / Presidential Republic
    base_p = MD_GOALS / "00_politics" / "SOV_presidential_republic.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Imperial Gold Dragon Seal / Authority Emblem in center
    seal = Image.new("RGBA", (36, 32), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(seal)
    # Red pedestal
    sdraw.rectangle([6, 20, 30, 28], fill=(160, 20, 20, 255), outline=(225, 185, 35, 255), width=1)
    # Gold imperial dragon seal block
    sdraw.rectangle([8, 10, 28, 20], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    sdraw.ellipse([11, 2, 25, 12], fill=(245, 210, 65, 255), outline=(140, 95, 20, 255), width=1)
    # Central star on seal
    star_s = create_gold_star(10)
    seal.paste(star_s, (13, 11), star_s)
    canvas.paste(seal, ((TARGET_SIZE[0] - seal.width) // 2, 36), seal)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "concentration_of_power")
    return canvas


# 9. VIE_institutional_opening: Mở rộng giám sát thể chế
def build_institutional_opening() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Court / Scale of Justice
    base_p = MD_GOALS / "00_politics" / "focus_generic_court.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Golden Master Key of Institutional Reform
    key = Image.new("RGBA", (34, 18), (0, 0, 0, 0))
    kdraw = ImageDraw.Draw(key)
    # Key ring
    kdraw.ellipse([1, 4, 11, 14], outline=(245, 205, 45, 255), width=2)
    kdraw.ellipse([4, 7, 8, 11], fill=(0, 0, 0, 0))
    # Key shaft
    kdraw.rectangle([10, 8, 30, 10], fill=(245, 205, 45, 255), outline=(130, 95, 20, 255))
    # Key wards
    kdraw.rectangle([24, 10, 26, 15], fill=(245, 205, 45, 255))
    kdraw.rectangle([28, 10, 30, 14], fill=(245, 205, 45, 255))
    canvas.paste(key, ((TARGET_SIZE[0] - key.width) // 2, 48), key)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "institutional_opening")
    return canvas


# 10. VIE_era_of_rising: Kỷ nguyên vươn mình của dân tộc
def build_era_of_rising() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Economic Prosperity & Sunburst
    base_p = MD_GOALS / "00_economy" / "economic_prosperity2.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.28)
    base = ImageEnhance.Contrast(base).enhance(1.18)
    base = base.resize((84, 72), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Ascending Golden Lac Bird (Chim Lạc) silhouette in high relief
    bird = Image.new("RGBA", (50, 42), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bird)
    # Sweeping wings of Lac bird
    pts_wing_left = [(25, 24), (8, 6), (18, 16), (2, 12), (16, 22)]
    pts_wing_right = [(25, 24), (42, 6), (32, 16), (48, 12), (34, 22)]
    bdraw.polygon(pts_wing_left, fill=(255, 235, 120, 255), outline=(160, 115, 15, 255))
    bdraw.polygon(pts_wing_right, fill=(240, 200, 50, 255), outline=(150, 105, 15, 255))
    # Bird head & beak soaring upward
    bdraw.polygon([(24, 28), (26, 28), (25, 8), (23, 2), (22, 6)], fill=(255, 245, 150, 255), outline=(170, 125, 20, 255))
    # Tail feathers
    bdraw.polygon([(23, 28), (27, 28), (29, 38), (25, 34), (21, 38)], fill=(225, 185, 35, 255), outline=(140, 95, 15, 255))
    canvas.paste(bird, ((TARGET_SIZE[0] - bird.width) // 2, 28), bird)

    # 3 Gold Stars Capstone on top (Triple Star Crest)
    s_mid = create_gold_star_with_glow(16)
    s_left = create_gold_star(12)
    s_right = create_gold_star(12)

    canvas.paste(s_mid, ((TARGET_SIZE[0] - s_mid.width) // 2, -1), s_mid)
    canvas.paste(s_left, ((TARGET_SIZE[0] - s_mid.width) // 2 - 14, 3), s_left)
    canvas.paste(s_right, ((TARGET_SIZE[0] - s_mid.width) // 2 + 18, 3), s_right)

    # Bottom National cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "era_of_rising")
    return canvas


# 11. VIE_party_centennial_2030: Một trăm năm thành lập Đảng (1930 - 2030)
def build_party_centennial_2030() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Grand Red Sunburst & Communist Flag backdrop
    base_p = MD_GOALS / "china" / "communist_party_of_china.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Double Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Central Monumental "100" Medallion with Hammer & Sickle
    medallion = create_congress_medallion("100", font_size=24, w=58, h=33)
    canvas.paste(medallion, ((TARGET_SIZE[0] - medallion.width) // 2, 27), medallion)

    # Golden Hammer & Sickle above the medallion
    hs = draw_hammer_and_sickle(20)
    canvas.paste(hs, ((TARGET_SIZE[0] - hs.width) // 2, 14), hs)

    # Centennial Ribbon "1930 - 2030"
    ribbon = Image.new("RGBA", (66, 16), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(ribbon)
    rdraw.rounded_rectangle([0, 0, 65, 15], radius=3, fill=(170, 15, 15, 255), outline=(235, 195, 45, 255), width=1)
    try:
        rfont = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 9)
    except Exception:
        rfont = ImageFont.load_default()
    rdraw.text((6, 2), "1930 - 2030", fill=(255, 235, 120, 255), font=rfont)
    canvas.paste(ribbon, ((TARGET_SIZE[0] - ribbon.width) // 2, 54), ribbon)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom National cockade
    cockade = create_vpa_cockade(17)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "party_centennial_2030")
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
        "VIE_prepare_congress_9": "GFX_focus_VIE_prepare_congress_9",
        "VIE_resolution_congress_9": "GFX_focus_VIE_resolution_congress_9",
        "VIE_resolution_congress_10": "GFX_focus_VIE_resolution_congress_10",
        "VIE_resolution_congress_11": "GFX_focus_VIE_resolution_congress_11",
        "VIE_resolution_congress_12": "GFX_focus_VIE_resolution_congress_12",
        "VIE_resolution_congress_13": "GFX_focus_VIE_resolution_congress_13",
        "VIE_resolution_congress_14": "GFX_focus_VIE_resolution_congress_14",
        "VIE_concentration_of_power": "GFX_focus_VIE_concentration_of_power",
        "VIE_institutional_opening": "GFX_focus_VIE_institutional_opening",
        "VIE_era_of_rising": "GFX_focus_VIE_era_of_rising",
        "VIE_party_centennial_2030": "GFX_focus_VIE_party_centennial_2030",
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
    """Create a contact sheet showcase image of all 11 Congress & Era of Rising focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "congress_spine_icons_showcase.png"

    cols = 6
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

    draw.text((pad_x, 20), "BỘ ICON GFX: ĐẠI HỘI ĐẢNG & TRỤC KỶ NGUYÊN MỚI (CỤM 1)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "11 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "prepare_congress_9": "Chuẩn bị Đại hội IX",
        "resolution_congress_9": "Nghị quyết Đại hội IX",
        "resolution_congress_10": "Nghị quyết Đại hội X",
        "resolution_congress_11": "Nghị quyết Đại hội XI",
        "resolution_congress_12": "Nghị quyết Đại hội XII",
        "resolution_congress_13": "Nghị quyết Đại hội XIII",
        "resolution_congress_14": "Nghị quyết Đại hội XIV",
        "concentration_of_power": "Tập trung quyền lực",
        "institutional_opening": "Mở rộng giám sát thể chế",
        "era_of_rising": "Kỷ nguyên vươn mình",
        "party_centennial_2030": "100 năm thành lập Đảng",
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
    print("BUILDING 11 PARTY CONGRESS & ERA OF RISING FOCUS ICONS")
    print("=" * 65)

    built_icons = {}
    built_icons["prepare_congress_9"] = build_prepare_congress_9()
    built_icons["resolution_congress_9"] = build_resolution_congress_9()
    built_icons["resolution_congress_10"] = build_resolution_congress_10()
    built_icons["resolution_congress_11"] = build_resolution_congress_11()
    built_icons["resolution_congress_12"] = build_resolution_congress_12()
    built_icons["resolution_congress_13"] = build_resolution_congress_13()
    built_icons["resolution_congress_14"] = build_resolution_congress_14()
    built_icons["concentration_of_power"] = build_concentration_of_power()
    built_icons["institutional_opening"] = build_institutional_opening()
    built_icons["era_of_rising"] = build_era_of_rising()
    built_icons["party_centennial_2030"] = build_party_centennial_2030()

    print("\nRegistering GFX sprites...")
    register_sprites()

    print("\nUpdating focus tree...")
    update_focus_tree_icons()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 11 ICONS GENERATED & REGISTERED")
    print("=" * 65)


if __name__ == "__main__":
    main()
