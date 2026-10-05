import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
import math
import struct

ROOT = Path(__file__).resolve().parents[2]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")
TARGET_SIZE = (93, 91)

def create_gold_star(size: int) -> Image.Image:
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
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    # Outer brass rim
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

def enforce_border(canvas: Image.Image) -> Image.Image:
    pixels = canvas.load()
    w, h = TARGET_SIZE
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)
    return canvas

# --- BUILDERS ---

def build_sf_command() -> Image.Image:
    # Joint SF Command: Sculpted Golden Wings, Commando Dagger, VPA Roundel, Top 3D Star
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "united_kingdom" / "special_air_service.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # VPA Cockade on hilt/banner
    cockade = create_vpa_cockade(18, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 42), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_sf_sapper() -> Image.Image:
    # Dac Cong Branch: Jungle Ghost Camouflaged Commando in Antique Bronze Laurel Wreath
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "soldiers" / "Generic_Jungle_Ghost.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.14)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    # Bottom VPA cockade in wreath ribbon
    cockade = create_vpa_cockade(17, naval=False)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 67), cockade)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_sf_sapper_training() -> Image.Image:
    # Commando Training: Modern Quad-NVG Operator Breaking from Gold Laurel Medallion
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
    return enforce_border(canvas)

def build_sf_sapper_equipment() -> Image.Image:
    # Commando Equipment: Suppressed Carbine, Optics, Camo Gear Wheel
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
    return enforce_border(canvas)

def build_sf_sapper_command() -> Image.Image:
    # Night Recon & Infiltration: Sniper with Suppressed Rifle, Golden Crescent Moon & Bronze Shield
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
    return enforce_border(canvas)

def build_sf_sapper_elite() -> Image.Image:
    # Elite Commando Brigade Capstone: Masked Commando in Winged Golden Shield, 3 Gold Stars
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "hong_kong" / "HK_elite_team.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.15)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # 3 Faceted 3D Gold Stars across apex
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
    return enforce_border(canvas)

def build_sf_marine() -> Image.Image:
    # Naval Infantry: Sculpted Anchor, Crossed Rifles, Nautical Rope, Blue Medallion
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_navy" / "amphibious_assault.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.20)
    base = ImageEnhance.Contrast(base).enhance(1.12)
    base = base.resize((82, 75), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 7), base)

    # Naval cockade at the anchor ring
    cockade = create_vpa_cockade(18, naval=True)
    canvas.paste(cockade, ((TARGET_SIZE[0] - cockade.width) // 2, 57), cockade)

    # Top faceted 3D Gold Star
    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    return enforce_border(canvas)

def build_sf_marine_training() -> Image.Image:
    # Amphibious Assault Training: Landing Craft Charging Surf, Helm & Laurel Wreath
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
    return enforce_border(canvas)

def build_sf_marine_equipment() -> Image.Image:
    # Marine Equipment & Amphibious Combat Craft: Fast Attack Riverine/Littoral Craft
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
    return enforce_border(canvas)

def build_sf_marine_command() -> Image.Image:
    # Marine Command & Maritime Doctrine: Chess Pieces on Azure Shield & Laurels
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
    return enforce_border(canvas)

def build_sf_marine_elite() -> Image.Image:
    # Elite Marine Brigade Capstone: Combat Marine with Tactical Armor & 3 Gold Stars
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    base_p = MD_GOALS / "00_army" / "soldiers" / "legacy_of_marines.dds"
    base = Image.open(base_p).convert("RGBA")
    base = ImageEnhance.Color(base).enhance(1.22)
    base = ImageEnhance.Contrast(base).enhance(1.14)
    base = base.resize((84, 76), Image.Resampling.LANCZOS)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # 3 Faceted 3D Gold Stars across apex
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
    return enforce_border(canvas)

def main():
    icons = {
        "sf_command": build_sf_command(),
        "sf_sapper": build_sf_sapper(),
        "sf_sapper_training": build_sf_sapper_training(),
        "sf_sapper_equipment": build_sf_sapper_equipment(),
        "sf_sapper_command": build_sf_sapper_command(),
        "sf_sapper_elite": build_sf_sapper_elite(),
        "sf_marine": build_sf_marine(),
        "sf_marine_training": build_sf_marine_training(),
        "sf_marine_equipment": build_sf_marine_equipment(),
        "sf_marine_command": build_sf_marine_command(),
        "sf_marine_elite": build_sf_marine_elite(),
    }

    # Render test showcase
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

    out = BRAIN_DIR / "sf_v2_showcase.png"
    canvas.save(out)
    print("Saved v2 showcase to", out)

if __name__ == "__main__":
    main()
