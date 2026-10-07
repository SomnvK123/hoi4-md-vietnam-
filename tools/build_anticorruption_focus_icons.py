"""Script to build Focus Icons for Vietnam Party Rectification & Anti-Corruption Campaign
(Cụm 2: Chỉnh đốn Đảng & Chiến dịch "Đốt lò" Phòng chống Tham nhũng - 11 focuses)
in Millennium Dawn with authentic 3D Painterly / Heraldic Relief style.

11 Focuses:
1.  party_members_private_business: Đảng viên làm Kinh tế Tư nhân (Hammer & sickle fused with business tower & gold coin, laurel)
2.  anti_corruption_steering: Ban Chỉ đạo Phòng chống Tham nhũng (Blazing furnace oven "Đốt lò", justice sword, shield, laurel)
3.  asset_declaration: Quan chức kê khai tài sản (Asset declaration ledger parchment, golden magnifying glass, transparency scale)
4.  tw4_party_building: Nghị quyết Trung ương 4 khóa XI (Party building codex, ideological purity shield, torch of rectitude)
5.  party_inspection: Ủy ban Kiểm tra Trung ương (Central Inspection Commission: crossed golden justice sword & steel shield)
6.  party_discipline: Chiến dịch Đốt lò không vùng cấm (Iron discipline hammer shattering corruption handcuffs, blazing furnace)
7.  cadre_accountability: Trách nhiệm giải trình của cán bộ (Hand oath on Constitution, office dragon seal handover, national flag)
8.  asset_recovery: Thu hồi tài sản bị chiếm đoạt (Confiscated treasure coffer with red star wax seal, money flow to treasury)
9.  clean_cadres: Đội ngũ cán bộ trong sạch (Pure white-gold lotus blooming inside golden aegis shield of integrity)
10. peoples_oversight: Nhân dân giám sát cán bộ (People's oversight beacon eye, Fatherland Front lotus crest, crowd with flags)
11. digital_anticorruption: Chống tham nhũng bằng dữ liệu (Big Data server grid scanning asset money flow, digital magnifying glass)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
- Brain showcase: anticorruption_icons_showcase.png
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
    "party_members_private_business",
    "anti_corruption_steering",
    "asset_declaration",
    "tw4_party_building",
    "party_inspection",
    "party_discipline",
    "cadre_accountability",
    "asset_recovery",
    "clean_cadres",
    "peoples_oversight",
    "digital_anticorruption",
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
# 11 BUILDER FUNCTIONS (CỤM 2: CHỈNH ĐỐN ĐẢNG & CHIẾN DỊCH "ĐỐT LÒ")
# =========================================================================

# 1. VIE_party_members_private_business: Đảng viên làm Kinh tế Tư nhân
def build_party_members_private_business() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Modern Commercial High-Rise Building & Economic Growth
    base_p = MD_GOALS / "00_economy" / "economic_civil_industry.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((80, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Communist Party badge + Golden Enterprise Coin emblem in center
    badge = Image.new("RGBA", (48, 36), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(badge)
    # Red enamel shield
    bdraw.rounded_rectangle([0, 0, 47, 35], radius=6, fill=(185, 25, 25, 255), outline=(235, 195, 45, 255), width=2)
    # Hammer and Sickle on left side
    hs = draw_hammer_and_sickle(20)
    badge.paste(hs, (4, 8), hs)
    # Golden dollar / coin cog on right side
    bdraw.ellipse([25, 7, 43, 25], fill=(245, 205, 45, 255), outline=(130, 95, 20, 255), width=1)
    bdraw.ellipse([28, 10, 40, 22], outline=(255, 235, 120, 255), width=1)
    # Small star in coin
    s_coin = create_gold_star(8)
    badge.paste(s_coin, (30, 12), s_coin)

    canvas.paste(badge, ((TARGET_SIZE[0] - badge.width) // 2, 36), badge)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "party_members_private_business")
    return canvas


# 2. VIE_anti_corruption_steering: Ban Chỉ đạo Phòng chống Tham nhũng ("Đốt lò")
def build_anti_corruption_steering() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Anti-Corruption Law / Scale / Shield
    base_p = MD_GOALS / "00_security" / "blr_anti_corruption_law.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 72), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Blazing Furnace Oven ("Lò đã nóng lên thì củi tươi cũng phải cháy")
    furnace = Image.new("RGBA", (50, 40), (0, 0, 0, 0))
    fdraw = ImageDraw.Draw(furnace)
    # Bronze iron furnace cauldron
    fdraw.polygon([(8, 18), (42, 18), (38, 38), (12, 38)], fill=(55, 45, 40, 255), outline=(225, 175, 45, 255), width=2)
    # Cauldron rim
    fdraw.rounded_rectangle([6, 14, 44, 20], radius=3, fill=(180, 130, 30, 255), outline=(245, 215, 60, 255))
    # Glowing fiery coals inside
    fdraw.ellipse([14, 22, 36, 34], fill=(255, 80, 20, 240))
    # Raging fire flames leaping out
    flames = [
        [(16, 16), (22, 2), (28, 14)],
        [(24, 14), (28, 0), (32, 12)],
        [(28, 14), (36, 4), (38, 16)],
    ]
    for fl in flames:
        fdraw.polygon(fl, fill=(255, 200, 30, 255), outline=(255, 90, 10, 255))
    # Core yellow fire
    fdraw.polygon([(22, 14), (26, 4), (30, 14)], fill=(255, 255, 140, 255))
    # Star emblem on furnace front
    s_f = create_gold_star(10)
    furnace.paste(s_f, (20, 24), s_f)

    canvas.paste(furnace, ((TARGET_SIZE[0] - furnace.width) // 2, 32), furnace)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "anti_corruption_steering")
    return canvas


# 3. VIE_asset_declaration: Quan chức kê khai tài sản
def build_asset_declaration() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Investigation / Auditor lens
    base_p = MD_GOALS / "00_security" / "investigation.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((80, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Detailed Asset Ledger Document with gold sealing stamp & checkmarks
    ledger = Image.new("RGBA", (44, 30), (0, 0, 0, 0))
    ldraw = ImageDraw.Draw(ledger)
    # White parchment paper
    ldraw.rounded_rectangle([0, 0, 42, 28], radius=3, fill=(245, 245, 240, 255), outline=(180, 140, 40, 255), width=2)
    # Header bar
    ldraw.rectangle([2, 2, 40, 7], fill=(185, 25, 25, 255))
    # Text lines & checkboxes
    for y in [11, 16, 21]:
        ldraw.line([(6, y), (28, y)], fill=(80, 90, 105, 255), width=1)
        # Green checkmark
        ldraw.polygon([(32, y), (34, y + 2), (38, y - 2)], fill=(30, 160, 40, 255))
    # Red official wax seal in bottom-right corner
    ldraw.ellipse([26, 16, 38, 26], fill=(190, 20, 20, 255), outline=(235, 195, 45, 255))
    s_seal = create_gold_star(7)
    ledger.paste(s_seal, (29, 18), s_seal)

    canvas.paste(ledger, ((TARGET_SIZE[0] - ledger.width) // 2, 46), ledger)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "asset_declaration")
    return canvas


# 4. VIE_tw4_party_building: Nghị quyết Trung ương 4 khóa XI (Xây dựng, chỉnh đốn Đảng)
def build_tw4_party_building() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Communist Party flag / banner
    base_p = MD_GOALS / "china" / "communist_party_of_china.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((78, 68), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Central Codex of Central Resolution 4 (NQ Trung ương 4) & Golden Torch
    res_badge = Image.new("RGBA", (56, 34), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(res_badge)
    # Red book with gold embossing
    rdraw.rounded_rectangle([0, 0, 54, 32], radius=5, fill=(180, 20, 20, 255), outline=(235, 195, 45, 255), width=2)
    # Book spine line
    rdraw.line([(27, 2), (27, 30)], fill=(235, 195, 45, 255), width=2)
    # Text "NQ-TW 4" in gold
    try:
        font_nq = ImageFont.truetype("C:/Windows/Fonts/georgiab.ttf", 11)
    except Exception:
        font_nq = ImageFont.load_default()
    rdraw.text((4, 4), "NQ", fill=(255, 235, 120, 255), font=font_nq)
    rdraw.text((4, 16), "TW4", fill=(255, 235, 120, 255), font=font_nq)

    # Golden torch of rectitude on right page
    rdraw.polygon([(40, 14), (43, 26), (38, 26)], fill=(225, 185, 45, 255), outline=(130, 90, 15, 255))
    # Torch flame
    rdraw.polygon([(36, 14), (40, 4), (44, 14)], fill=(255, 180, 20, 255), outline=(255, 70, 10, 255))
    rdraw.polygon([(38, 13), (40, 7), (42, 13)], fill=(255, 255, 150, 255))

    canvas.paste(res_badge, ((TARGET_SIZE[0] - res_badge.width) // 2, 38), res_badge)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "tw4_party_building")
    return canvas


# 5. VIE_party_inspection: Ủy ban Kiểm tra Trung ương
def build_party_inspection() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Heraldic Shield of Central Inspection Commission (UBKTTW)
    shield = Image.new("RGBA", (76, 72), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(shield)
    # Outer bronze-gold rim
    pts = [(38, 4), (68, 14), (64, 46), (38, 68), (12, 46), (8, 14)]
    sdraw.polygon(pts, fill=(30, 40, 55, 255), outline=(235, 195, 45, 255), width=2)
    # Inner crimson crest
    pts_in = [(38, 9), (62, 18), (59, 44), (38, 62), (17, 44), (14, 18)]
    sdraw.polygon(pts_in, fill=(175, 20, 20, 245), outline=(130, 15, 15, 255), width=1)

    # Crossed Golden Sword of Justice & Inspection Scalpel
    # Diagonal sword 1
    sdraw.line([(18, 18), (58, 54)], fill=(245, 215, 75, 255), width=2)
    sdraw.line([(14, 22), (22, 14)], fill=(245, 215, 75, 255), width=3)
    # Diagonal sword 2
    sdraw.line([(58, 18), (18, 54)], fill=(245, 215, 75, 255), width=2)
    sdraw.line([(54, 14), (62, 22)], fill=(245, 215, 75, 255), width=3)

    # Central Hammer & Sickle insignia on shield
    hs = draw_hammer_and_sickle(22)
    shield.paste(hs, ((shield.width - hs.width) // 2, 26), hs)
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
    save_game_ready_icon(canvas, "party_inspection")
    return canvas


# 6. VIE_party_discipline: Chiến dịch Đốt lò không vùng cấm
def build_party_discipline() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Anti-Corruption Crackdown (Handcuffs & Red Legal Stamp)
    base_p = MD_GOALS / "00_security" / "focus_ARG_crackdown_on_corruption.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 72), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Massive Golden War Hammer of Discipline striking down
    hammer = Image.new("RGBA", (50, 44), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(hammer)
    # Steel & gold handcuffs shattered at bottom
    hdraw.ellipse([8, 24, 22, 38], outline=(200, 215, 230, 255), width=2)
    hdraw.ellipse([28, 24, 42, 38], outline=(200, 215, 230, 255), width=2)
    # Broken chain links
    hdraw.line([(22, 31), (28, 31)], fill=(255, 215, 60, 255), width=2)
    # Heavy hammer head
    hdraw.polygon([(16, 6), (36, 6), (38, 18), (14, 18)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    # Hammer shaft
    hdraw.line([(26, 18), (26, 36)], fill=(160, 110, 20, 255), width=3)
    # Striking sparks
    for sp in [(10, 12), (40, 12), (12, 4), (38, 4)]:
        hdraw.line([(26, 12), sp], fill=(255, 240, 120, 255), width=1)
    canvas.paste(hammer, ((TARGET_SIZE[0] - hammer.width) // 2, 26), hammer)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "party_discipline")
    return canvas


# 7. VIE_cadre_accountability: Trách nhiệm giải trình của cán bộ
def build_cadre_accountability() -> Image.Image:
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

    # Red Office Seal handover & Oath badge
    oath = Image.new("RGBA", (46, 32), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(oath)
    # Pedestal
    odraw.rounded_rectangle([4, 18, 42, 28], radius=3, fill=(160, 20, 20, 255), outline=(225, 185, 45, 255), width=1)
    # Gold official dragon seal on top
    odraw.rectangle([14, 8, 32, 18], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    odraw.ellipse([18, 2, 28, 10], fill=(245, 215, 65, 255), outline=(140, 95, 20, 255), width=1)
    # Gilded star on seal
    s_seal = create_gold_star(8)
    oath.paste(s_seal, (19, 9), s_seal)
    canvas.paste(oath, ((TARGET_SIZE[0] - oath.width) // 2, 44), oath)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "cadre_accountability")
    return canvas


# 8. VIE_asset_recovery: Thu hồi tài sản bị chiếm đoạt
def build_asset_recovery() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Treasure Coffer / Money / Gold
    base_p = MD_GOALS / "00_economy" / "money.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.25)
    base = ImageEnhance.Contrast(base).enhance(1.18)
    base = base.resize((80, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Confiscation Order & National Recovery Seal
    seal_box = Image.new("RGBA", (44, 28), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(seal_box)
    # Red & gold state asset recovery vault chest
    sdraw.rounded_rectangle([2, 6, 42, 26], radius=4, fill=(160, 20, 20, 255), outline=(235, 195, 45, 255), width=2)
    sdraw.line([(22, 6), (22, 26)], fill=(235, 195, 45, 255), width=2)
    # Gold lock keyhole
    sdraw.ellipse([18, 12, 26, 20], fill=(245, 215, 60, 255), outline=(130, 90, 15, 255))
    sdraw.polygon([(21, 16), (23, 16), (22, 20)], fill=(0, 0, 0, 255))
    canvas.paste(seal_box, ((TARGET_SIZE[0] - seal_box.width) // 2, 50), seal_box)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "asset_recovery")
    return canvas


# 9. VIE_clean_cadres: Đội ngũ cán bộ trong sạch
def build_clean_cadres() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Pure Sunburst / Liberty Council
    base_p = MD_GOALS / "00_economy" / "economic_prosperity2.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Luminous Golden Lotus of Integrity & Pure Aegis
    lotus = Image.new("RGBA", (50, 42), (0, 0, 0, 0))
    ldraw = ImageDraw.Draw(lotus)
    # Shield backdrop in pure azure/gold
    ldraw.polygon([(25, 4), (45, 12), (40, 36), (25, 42), (10, 36), (5, 12)], fill=(25, 50, 85, 230), outline=(245, 205, 55, 255), width=2)
    # Blooming pure white-gold lotus petals
    # Central petal
    ldraw.polygon([(25, 8), (30, 20), (25, 34), (20, 20)], fill=(255, 250, 210, 255), outline=(225, 185, 45, 255))
    # Left petals
    ldraw.polygon([(25, 20), (14, 16), (16, 28), (25, 34)], fill=(255, 235, 140, 255), outline=(215, 175, 40, 255))
    ldraw.polygon([(25, 24), (8, 24), (12, 34), (25, 36)], fill=(245, 215, 100, 255), outline=(200, 160, 35, 255))
    # Right petals
    ldraw.polygon([(25, 20), (36, 16), (34, 28), (25, 34)], fill=(255, 235, 140, 255), outline=(215, 175, 40, 255))
    ldraw.polygon([(25, 24), (42, 24), (38, 34), (25, 36)], fill=(245, 215, 100, 255), outline=(200, 160, 35, 255))
    # Star inside lotus
    s_l = create_gold_star(9)
    lotus.paste(s_l, (21, 18), s_l)
    canvas.paste(lotus, ((TARGET_SIZE[0] - lotus.width) // 2, 28), lotus)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "clean_cadres")
    return canvas


# 10. VIE_peoples_oversight: Nhân dân giám sát cán bộ
def build_peoples_oversight() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Popular Assembly & Democracy
    base_p = MD_GOALS / "00_politics" / "democracy_genericus.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((82, 70), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # People's Vigilant Eye & Fatherland Front Lotus Crest
    beacon = Image.new("RGBA", (50, 36), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(beacon)
    # Eye contour in gold
    bdraw.ellipse([4, 6, 46, 30], outline=(245, 215, 60, 255), width=2)
    # Inner crimson iris
    bdraw.ellipse([14, 8, 36, 28], fill=(185, 20, 20, 255), outline=(245, 215, 60, 255), width=1)
    # Central golden pupil star
    s_eye = create_gold_star(14)
    beacon.paste(s_eye, (18, 11), s_eye)
    # Rays of light emanating outward
    for ang in [-35, -20, 0, 20, 35]:
        rad = math.radians(ang)
        bdraw.line([(25 + 20 * math.cos(rad), 18 + 10 * math.sin(rad)), (25 + 25 * math.cos(rad), 18 + 14 * math.sin(rad))], fill=(255, 240, 130, 255), width=2)
    canvas.paste(beacon, ((TARGET_SIZE[0] - beacon.width) // 2, 34), beacon)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "peoples_oversight")
    return canvas


# 11. VIE_digital_anticorruption: Chống tham nhũng bằng dữ liệu
def build_digital_anticorruption() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base Cyber Intelligence / Big Data Grid
    grid = Image.new("RGBA", (76, 76), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(grid)
    for r in range(12, 36, 6):
        gdraw.ellipse([38 - r, 38 - r, 38 + r, 38 + r], outline=(30, 160, 240, 180), width=1)
    for ang_deg in range(0, 360, 45):
        rad = math.radians(ang_deg)
        gdraw.line([(38, 38), (38 + 35 * math.cos(rad), 38 + 35 * math.sin(rad))], fill=(20, 200, 220, 140), width=1)
    canvas.paste(grid, ((TARGET_SIZE[0] - grid.width) // 2, 10), grid)

    # Base Anti-Corruption Shield
    base_p = MD_GOALS / "00_security" / "BLR_Anti_Corruption.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = base.resize((76, 66), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 12), base)

    # Golden laurels
    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Digital Magnifying Scanner overlay with binary & red badge
    scanner = Image.new("RGBA", (44, 30), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scanner)
    # Glass magnifying lens rim
    sdraw.ellipse([4, 2, 26, 24], outline=(245, 215, 60, 255), width=2)
    sdraw.ellipse([7, 5, 23, 21], fill=(20, 160, 220, 140))
    # Lens handle
    sdraw.line([(24, 22), (36, 28)], fill=(225, 185, 45, 255), width=3)
    # Digital binary code dots in lens
    sdraw.point([(12, 10), (18, 10), (15, 15), (12, 18), (18, 18)], fill=(255, 255, 255, 255))
    # Small cockade star on right
    s_sc = create_gold_star(10)
    scanner.paste(s_sc, (28, 6), s_sc)
    canvas.paste(scanner, ((TARGET_SIZE[0] - scanner.width) // 2, 44), scanner)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom cockade
    cockade = create_vpa_cockade(18)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 69), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "digital_anticorruption")
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
        "VIE_party_members_private_business": "GFX_focus_VIE_party_members_private_business",
        "VIE_anti_corruption_steering": "GFX_focus_VIE_anti_corruption_steering",
        "VIE_asset_declaration": "GFX_focus_VIE_asset_declaration",
        "VIE_tw4_party_building": "GFX_focus_VIE_tw4_party_building",
        "VIE_party_inspection": "GFX_focus_VIE_party_inspection",
        "VIE_party_discipline": "GFX_focus_VIE_party_discipline",
        "VIE_cadre_accountability": "GFX_focus_VIE_cadre_accountability",
        "VIE_asset_recovery": "GFX_focus_VIE_asset_recovery",
        "VIE_clean_cadres": "GFX_focus_VIE_clean_cadres",
        "VIE_peoples_oversight": "GFX_focus_VIE_peoples_oversight",
        "VIE_digital_anticorruption": "GFX_focus_VIE_digital_anticorruption",
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
    """Create a contact sheet showcase image of all 11 Anti-Corruption & Party Building focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "anticorruption_icons_showcase.png"

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

    draw.text((pad_x, 20), "BỘ ICON GFX: CHỈNH ĐỐN ĐẢNG & CHIẾN DỊCH 'ĐỐT LÒ' (CỤM 2)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "11 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "party_members_private_business": "Đảng viên làm KT Tư nhân",
        "anti_corruption_steering": "Ban Chỉ đạo PCTN (Đốt lò)",
        "asset_declaration": "Kê khai tài sản cán bộ",
        "tw4_party_building": "Nghị quyết Trung ương 4",
        "party_inspection": "Ủy ban Kiểm tra TW",
        "party_discipline": "Đốt lò không vùng cấm",
        "cadre_accountability": "Trách nhiệm giải trình",
        "asset_recovery": "Thu hồi tài sản tham nhũng",
        "clean_cadres": "Cán bộ trong sạch liêm chính",
        "peoples_oversight": "Nhân dân giám sát cán bộ",
        "digital_anticorruption": "Chống tham nhũng bằng dữ liệu",
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
    print("BUILDING 11 PARTY RECTIFICATION & ANTI-CORRUPTION FOCUS ICONS")
    print("=" * 65)

    built_icons = {}
    built_icons["party_members_private_business"] = build_party_members_private_business()
    built_icons["anti_corruption_steering"] = build_anti_corruption_steering()
    built_icons["asset_declaration"] = build_asset_declaration()
    built_icons["tw4_party_building"] = build_tw4_party_building()
    built_icons["party_inspection"] = build_party_inspection()
    built_icons["party_discipline"] = build_party_discipline()
    built_icons["cadre_accountability"] = build_cadre_accountability()
    built_icons["asset_recovery"] = build_asset_recovery()
    built_icons["clean_cadres"] = build_clean_cadres()
    built_icons["peoples_oversight"] = build_peoples_oversight()
    built_icons["digital_anticorruption"] = build_digital_anticorruption()

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
