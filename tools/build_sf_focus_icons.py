"""Script to build Focus Icons for Vietnam Special Forces (Trục 4 Lực lượng Đặc biệt - 11 focuses)
in Millennium Dawn with authentic 3D Painterly / Digital Oil Painting style.

11 Focuses:
1.  sf_command: Bộ Tư lệnh Lực lượng Đặc biệt (Joint Special Operations Command - Winged combat dagger, 3D gold star, VPA roundel)
2.  sf_sapper: Phát triển Binh chủng Đặc công (Jungle Ghost camouflaged commando in ghillie hood, antique bronze laurel wreath, gold star)
3.  sf_sapper_training: Huấn luyện Đặc công (Modern tactical operator with quad-tube NVG night vision goggles breaking from gold laurel medallion)
4.  sf_sapper_equipment: Trang bị Đột kích Đặc công (Tactical suppressed carbine with optical scope on combat camo gear wheel)
5.  sf_sapper_command: Chiến thuật và Chỉ huy Đặc công (Nocturnal sniper aiming into the night, golden crescent moon, bronze heraldic shield)
6.  sf_sapper_elite: Lữ đoàn Đặc công Tinh nhuệ (Masked commando in winged golden heraldic shield, crimson backdrop, 3 faceted gold stars)
7.  sf_marine: Phát triển Hải quân đánh bộ (Sculpted iron anchor, crossed naval rifles, nautical rope, ocean blue medallion, Vietnam Naval roundel)
8.  sf_marine_training: Huấn luyện Đổ bộ (Amphibious landing assault craft charging beachhead surf, foaming waves, naval helm & laurels)
9.  sf_marine_equipment: Trang bị Đổ bộ (Armored littoral combat assault craft with twin cannons, naval anchor pedestal, gold star)
10. sf_marine_command: Tác chiến Biển và Chỉ huy (Naval chess king & bishop pieces representing operational doctrine, azure diamond shield & laurels)
11. sf_marine_elite: Lữ đoàn Hải quân đánh bộ Tinh nhuệ (Tactical marine combat operator in digital camo & plate carrier, 3 faceted gold stars)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- c:/Users/doans/.gemini/antigravity-ide/brain/add5d4ba-18d3-49e5-8343-5c2c59714d4f/special_forces_icons_showcase.png
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


def create_vpa_cockade(size: int = 20, naval: bool = False) -> Image.Image:
    """Generate official Vietnam People's Army or Naval roundel cockade."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    # Outer brass / gold rim
    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(215, 175, 45, 255), outline=(125, 90, 15, 255))
    if naval:
        r_mid = r_outer - 1.5
        draw.ellipse((cx - r_mid, cy - r_mid, cx + r_mid, cy + r_mid), fill=(18, 48, 110, 255), outline=(10, 25, 60, 255))
        r_inner = r_mid - 2.5
        draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(195, 25, 25, 255), outline=(120, 15, 15, 255))
    else:
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
# 11 BUILDER FUNCTIONS FOR SPECIAL FORCES (TRỤC 4)
# =========================================================================

# 1. VIE_sf_command: Bộ Tư lệnh Lực lượng Đặc biệt
def build_sf_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "united_kingdom" / "special_air_service.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # VPA Cockade on hilt/crossguard
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 42), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_command")
    return canvas


# 2. VIE_sf_sapper: Phát triển Binh chủng Đặc công
def build_sf_sapper() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "soldiers" / "Generic_Jungle_Ghost.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom VPA cockade in wreath ribbon
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_sapper")
    return canvas


# 3. VIE_sf_sapper_training: Huấn luyện Đặc công
def build_sf_sapper_training() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "army_nightvision.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom VPA cockade in wreath ribbon
    cockade = create_vpa_cockade(16, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_sapper_training")
    return canvas


# 4. VIE_sf_sapper_equipment: Trang bị Đột kích Đặc công
def build_sf_sapper_equipment() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "specopsweaponsrussia.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom VPA cockade
    cockade = create_vpa_cockade(16, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_sapper_equipment")
    return canvas


# 5. VIE_sf_sapper_command: Chiến thuật và Chỉ huy Đặc công
def build_sf_sapper_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "focus_SIA_night_time_training.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom VPA cockade
    cockade = create_vpa_cockade(16, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_sapper_command")
    return canvas


# 6. VIE_sf_sapper_elite: Lữ đoàn Đặc công Tinh nhuệ
def build_sf_sapper_elite() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "hong_kong" / "HK_elite_team.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # 3 Faceted 3D Gold Stars across apex (Elite Capstone)
    s_center = create_gold_star_with_glow(20)
    s_side = create_gold_star_with_glow(15)
    cx = TARGET_SIZE[0] // 2
    canvas.paste(s_center, (cx - s_center.width // 2, -1), s_center)
    canvas.paste(s_side, (cx - 24 - s_side.width // 2, 4), s_side)
    canvas.paste(s_side, (cx + 24 - s_side.width // 2, 4), s_side)

    # Bottom VPA cockade
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_sapper_elite")
    return canvas


# 7. VIE_sf_marine: Phát triển Hải quân đánh bộ
def build_sf_marine() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "amphibious_assault.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((82, 75), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Vietnam Naval cockade at the anchor ring
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 57), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_marine")
    return canvas


# 8. VIE_sf_marine_training: Huấn luyện Đổ bộ
def build_sf_marine_training() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "generic_landing_ship.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.14)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom Naval cockade
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_marine_training")
    return canvas


# 9. VIE_sf_marine_equipment: Trang bị Đổ bộ
def build_sf_marine_equipment() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "focus_SIA_river_patrols.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.14)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom Naval cockade on the anchor crest
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_marine_equipment")
    return canvas


# 10. VIE_sf_marine_command: Tác chiến Biển và Chỉ huy
def build_sf_marine_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "naval_doctrine.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom Naval cockade
    cockade = create_vpa_cockade(17, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 68), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_marine_command")
    return canvas


# 11. VIE_sf_marine_elite: Lữ đoàn Hải quân đánh bộ Tinh nhuệ
def build_sf_marine_elite() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "soldiers" / "legacy_of_marines.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.14)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # 3 Faceted 3D Gold Stars across apex (Elite Capstone)
    s_center = create_gold_star_with_glow(20)
    s_side = create_gold_star_with_glow(15)
    cx = TARGET_SIZE[0] // 2
    canvas.paste(s_center, (cx - s_center.width // 2, -1), s_center)
    canvas.paste(s_side, (cx - 24 - s_side.width // 2, 4), s_side)
    canvas.paste(s_side, (cx + 24 - s_side.width // 2, 4), s_side)

    # Bottom Naval cockade
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "sf_marine_elite")
    return canvas


# =========================================================================
# REGISTRATION & SHOWCASE
# =========================================================================

STEMS = [
    "sf_command", "sf_sapper", "sf_sapper_training", "sf_sapper_equipment",
    "sf_sapper_command", "sf_sapper_elite", "sf_marine", "sf_marine_training",
    "sf_marine_equipment", "sf_marine_command", "sf_marine_elite"
]


def create_showcase_artifact(icons: dict[str, Image.Image]):
    """Create a contact sheet showcase image of all 11 Special Forces focus icons."""
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)
    out_path = BRAIN_DIR / "special_forces_icons_showcase.png"

    cols = 4
    rows = (len(icons) + cols - 1) // cols
    card_w, card_h = 195, 145
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

    draw.text((pad_x, 20), "BỘ ICON GFX TRỤC 4: LỰC LƯỢNG ĐẶC BIỆT (SPECIAL FORCES)", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad_x, 48), "11 Focus Icons Chuẩn Sơn Dầu Tả Thực Millennium Dawn (93x91 PNG & Uncompressed 32-bit BGRA DDS)", fill=(160, 180, 200, 255), font=font_sub)

    focus_titles = {
        "sf_command": "BTL Lực lượng Đặc biệt",
        "sf_sapper": "Phát triển Binh chủng Đặc công",
        "sf_sapper_training": "Huấn luyện Đặc công",
        "sf_sapper_equipment": "Trang bị Đột kích Đặc công",
        "sf_sapper_command": "Chiến thuật & Chỉ huy ĐC",
        "sf_sapper_elite": "Lữ đoàn Đặc công Tinh nhuệ",
        "sf_marine": "Phát triển HQ Đánh bộ",
        "sf_marine_training": "Huấn luyện Đổ bộ",
        "sf_marine_equipment": "Trang bị Đổ bộ HQĐB",
        "sf_marine_command": "Tác chiến Biển & Chỉ huy",
        "sf_marine_elite": "Lữ đoàn HQĐB Tinh nhuệ",
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
        draw.text((x + 10, y + card_h - 36), stem, fill=(240, 200, 80, 255), font=font_id)
        draw.text((x + 10, y + card_h - 20), t_title, fill=(200, 215, 230, 255), font=font_name)

    canvas.save(out_path)
    print(f"Showcase image saved: {out_path}")


def main():
    print("=" * 65)
    print("REDESIGNING 11 SPECIAL FORCES FOCUS ICONS (PAINTERLY 3D MD STYLE)")
    print("=" * 65)

    built_icons = {}
    built_icons["sf_command"] = build_sf_command()
    built_icons["sf_sapper"] = build_sf_sapper()
    built_icons["sf_sapper_training"] = build_sf_sapper_training()
    built_icons["sf_sapper_equipment"] = build_sf_sapper_equipment()
    built_icons["sf_sapper_command"] = build_sf_sapper_command()
    built_icons["sf_sapper_elite"] = build_sf_sapper_elite()
    built_icons["sf_marine"] = build_sf_marine()
    built_icons["sf_marine_training"] = build_sf_marine_training()
    built_icons["sf_marine_equipment"] = build_sf_marine_equipment()
    built_icons["sf_marine_command"] = build_sf_marine_command()
    built_icons["sf_marine_elite"] = build_sf_marine_elite()

    print("\nGenerating visual showcase artifact...")
    create_showcase_artifact(built_icons)

    print("\n" + "=" * 65)
    print("BUILD COMPLETE: ALL 11 SPECIAL FORCES ICONS REDRAWN IN 3D PAINTERLY STYLE")
    print("=" * 65)


if __name__ == "__main__":
    main()
