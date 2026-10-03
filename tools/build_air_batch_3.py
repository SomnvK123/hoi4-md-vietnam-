"""Script to build Batch 3 Focus Icons for Vietnam Air Force & Air Defense (PK-KQ) in Millennium Dawn.
Batch 3 focuses (Nâng cấp Bán kính Tác chiến & Mạng Phòng không Tích hợp IADS - 6 focuses):
1. airf_command_reform_2: Cải cách Chỉ huy Phòng không - Không quân II (Biên đội tiêm kích vút bay qua khiên kim cương, quân hiệu PK-KQ, cánh bay vàng, sao vàng)
2. airf_medium_force: Lực lượng Không quân Trung bình (Đội hình tiêm kích đa nhiệm trên khiên vàng nguyệt quế, cánh bay PK-KQ, sao vàng)
3. airf_operating_range: Mở rộng Bán kính Tác chiến & Căn cứ Tiền phương (Tiêm kích tuần tra biển Đông với các vòng cung bán kính tác chiến, cánh bay vàng, sao vàng)
4. airf_iads: Phòng không Tích hợp IADS (Tổ hợp tên lửa SAM trên khiên đỏ, mái vòm ô dù bảo vệ bầu trời Tổ quốc, cánh bay vàng, sao vàng)
5. airf_layered_defence: Mạng Tên lửa Nhiều tầng (Tổ hợp bệ phóng tự hành TEL 8x8 cơ động đa tầng trong vành nguyệt quế, cánh bay PK-KQ, sao vàng)
6. airf_ew_antistealth: Tác chiến Điện tử & Chống tàng hình (Đài radar băng sóng mét nhìn vòng phát luồng xung điện từ chống tàng hình, cánh bay vàng, sao vàng)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Artifact showcase & tree simulation images
"""

import os
import sys
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")

TARGET_SIZE = (93, 91)


def save_game_ready_icon(canvas: Image.Image, stem: str):
    """Save canvas as transparent PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    # Enforce pure alpha=0 at 1-pixel border to guarantee clean cutouts
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
    print(f"Saved PNG: {png_path}")

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
    print(f"Saved DDS: {dds_path} (33,980 bytes)")


def create_gold_star(size: int) -> Image.Image:
    """Generate a sharp 5-pointed gold star with faceted shading."""
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

    draw.polygon(pts, fill=(255, 215, 0, 255), outline=(170, 130, 20, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 235, 100, 140))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(190, 140, 10, 160))
    return im


def create_gold_star_with_glow(size: int) -> Image.Image:
    """Generate faceted gold star with high-depth drop shadow."""
    star = create_gold_star(size)
    pad = 4
    canvas = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (size + pad * 2, size + pad * 2), (0, 0, 0, 0))
    shadow.paste(star, (pad, pad + 1), star)
    r, g, b, a = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a)).filter(ImageFilter.GaussianBlur(1.2))
    canvas.paste(shadow, (0, 0), shadow)
    canvas.paste(star, (pad, pad), star)
    return canvas


def create_vpa_cockade(size: int = 30) -> Image.Image:
    """Generate an official VPA roundel cockade."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(212, 175, 55, 255), outline=(130, 95, 20, 255), width=1)
    r_inner = r_outer - 2.5
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(185, 25, 25, 255), outline=(120, 15, 15, 255), width=1)
    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_airforce_wings(w: int = 36, h: int = 14) -> Image.Image:
    """Generate sleek golden air force pilot wings with central star and drop shadow."""
    pad = 3
    full_w = w + pad * 2
    full_h = h + pad * 2
    wings_raw = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(wings_raw)
    cy = h / 2
    cx = w / 2

    # Left wing feathers
    for i in range(3):
        y_off = (i - 1) * 2.5
        pts_left = [
            (cx - 3, cy + y_off),
            (cx - w // 2, cy - 2 + y_off * 1.3),
            (cx - w // 2 + 4, cy + 2 + y_off),
            (cx - 3, cy + 3 + y_off)
        ]
        draw.polygon(pts_left, fill=(240, 200, 55, 255), outline=(150, 110, 20, 255))
        draw.line((cx - 3, cy + y_off, cx - w // 2, cy - 2 + y_off * 1.3), fill=(255, 245, 130, 255), width=1)

    # Right wing feathers
    for i in range(3):
        y_off = (i - 1) * 2.5
        pts_right = [
            (cx + 3, cy + y_off),
            (cx + w // 2, cy - 2 + y_off * 1.3),
            (cx + w // 2 - 4, cy + 2 + y_off),
            (cx + 3, cy + 3 + y_off)
        ]
        draw.polygon(pts_right, fill=(240, 200, 55, 255), outline=(150, 110, 20, 255))
        draw.line((cx + 3, cy + y_off, cx + w // 2, cy - 2 + y_off * 1.3), fill=(255, 245, 130, 255), width=1)

    # Central red roundel with gold star
    r = 5
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(205, 25, 25, 255), outline=(140, 100, 15, 255), width=1)
    star = create_gold_star(8)
    wings_raw.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)

    # Composite with drop shadow
    im = Image.new("RGBA", (full_w, full_h), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (full_w, full_h), (0, 0, 0, 0))
    shadow.paste(wings_raw, (pad, pad + 1), wings_raw)
    r_ch, g_ch, b_ch, a_ch = shadow.split()
    black = Image.new("L", shadow.size, 0)
    shadow = Image.merge("RGBA", (black, black, black, a_ch)).filter(ImageFilter.GaussianBlur(1.0))
    im.paste(shadow, (0, 0), shadow)
    im.paste(wings_raw, (pad, pad), wings_raw)
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 1. VIE_airf_command_reform_2 (Cải cách Chỉ huy PK-KQ II)
# =========================================================================
def build_airf_command_reform_2() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/Jet_Fighters.dds (Two climbing fighters in midnight blue diamond frame with laurel wreath)
    base_path = MD_GOALS / "00_airforce" / "Jet_Fighters.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Add central VPA cockade roundel between the climbing jets and diamond center
    cockade = create_vpa_cockade(17)
    paste_centered(canvas, cockade, offset_x=0, offset_y=4)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_command_reform_2")
    return canvas


# =========================================================================
# 2. VIE_airf_medium_force (Lực lượng Không quân Trung bình)
# =========================================================================
def build_airf_medium_force() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/fighters.dds (Two Flanker fighters in formation over golden bronze shield with wreath)
    base_path = MD_GOALS / "00_airforce" / "fighters.dds"
    base = Image.open(base_path).convert("RGBA")

    # Enhance contrast and saturation
    base = ImageEnhance.Color(base).enhance(1.15)
    base = ImageEnhance.Contrast(base).enhance(1.10)

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_medium_force")
    return canvas


# =========================================================================
# 3. VIE_airf_operating_range (Mở rộng Bán kính Tác chiến)
# =========================================================================
def build_airf_operating_range() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/advan_fighters.dds (Fighter banking across circular nautical/sky blue ring with wreath)
    base_path = MD_GOALS / "00_airforce" / "advan_fighters.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Overlay expanding tactical combat range rings (concentric cyan/gold navigation range arcs)
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44
    # Range ring 1 (inner)
    draw.arc((cx - 18, cy - 18, cx + 18, cy + 18), start=180, end=360, fill=(70, 200, 240, 160), width=1)
    # Range ring 2 (middle)
    draw.arc((cx - 27, cy - 27, cx + 27, cy + 27), start=170, end=350, fill=(240, 210, 80, 180), width=1)
    # Range ring 3 (outer)
    draw.arc((cx - 35, cy - 35, cx + 35, cy + 35), start=190, end=330, fill=(70, 220, 255, 140), width=1)
    # Range tick marks
    draw.line((cx - 27, cy, cx - 23, cy), fill=(240, 210, 80, 200), width=1)
    draw.line((cx + 23, cy, cx + 27, cy), fill=(240, 210, 80, 200), width=1)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_operating_range")
    return canvas


# =========================================================================
# 4. VIE_airf_iads (Phòng không Tích hợp IADS)
# =========================================================================
def build_airf_iads() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: israel_palestine/iron_dome.dds (Multi-tube canister SAM launcher on red shield with wreath)
    base_path = MD_GOALS / "israel_palestine" / "iron_dome.dds"
    base = Image.open(base_path).convert("RGBA")

    # Inpaint any unwanted base ribbon elements by cropping cleanly or fitting
    base_resized = base.resize((85, 80), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Overlay IADS protective air umbrella dome (concentric translucent cyan and gold shield arcs)
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44
    # Protective dome glow
    draw.arc((cx - 36, cy - 36, cx + 36, cy + 36), start=195, end=345, fill=(60, 210, 255, 180), width=2)
    draw.arc((cx - 33, cy - 33, cx + 33, cy + 33), start=200, end=340, fill=(255, 230, 100, 150), width=1)
    draw.arc((cx - 28, cy - 28, cx + 28, cy + 28), start=205, end=335, fill=(60, 210, 255, 120), width=1)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom (covers generic ribbon cleanly)
    wings = create_airforce_wings(42, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_iads")
    return canvas


# =========================================================================
# 5. VIE_airf_layered_defence (Mạng Tên lửa Nhiều tầng)
# =========================================================================
def build_airf_layered_defence() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_airforce/patriot.dds (Modern heavy 8x8 wheeled mobile SAM TEL truck in firing position with wreath)
    base_path = MD_GOALS / "00_airforce" / "patriot.dds"
    base = Image.open(base_path).convert("RGBA")

    # Slight contrast boost
    base = ImageEnhance.Contrast(base).enhance(1.10)

    # Resize to fit frame
    base_resized = base.resize((86, 75), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Upgrade the bottom ribbon with official VPA Air Force wings
    wings = create_airforce_wings(42, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_layered_defence")
    return canvas


# =========================================================================
# 6. VIE_airf_ew_antistealth (Tác chiến Điện tử & Chống tàng hình)
# =========================================================================
def build_airf_ew_antistealth() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 00_army/army_radar.dds (Heavy rotating radar dish cabin with antenna in laurel wreath)
    base_path = MD_GOALS / "00_army" / "army_radar.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((85, 74), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Draw radiating electromagnetic pulse / anti-stealth radar emission waves from dish
    draw = ImageDraw.Draw(canvas)
    dish_x, dish_y = 50, 32
    # Radio pulses radiating top-right
    draw.arc((dish_x - 12, dish_y - 12, dish_x + 12, dish_y + 12), start=280, end=380, fill=(70, 210, 255, 180), width=1)
    draw.arc((dish_x - 20, dish_y - 20, dish_x + 20, dish_y + 20), start=285, end=375, fill=(255, 230, 80, 160), width=1)
    draw.arc((dish_x - 28, dish_y - 28, dish_x + 28, dish_y + 28), start=290, end=370, fill=(70, 220, 255, 140), width=1)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_ew_antistealth")
    return canvas


def create_showcase(icons, labels):
    """Generate a high-res showcase banner for Batch 3."""
    card_w, card_h = 165, 210
    pad = 18
    n = len(icons)
    total_w = pad + n * (card_w + pad)
    total_h = card_h + pad * 2 + 50

    im = Image.new("RGBA", (total_w, total_h), (16, 22, 32, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 20)
        font_sub = ImageFont.truetype("arial.ttf", 12)
        font_card = ImageFont.truetype("arialbd.ttf", 12)
    except Exception:
        font_title = font_sub = font_card = ImageFont.load_default()

    draw.text((pad, 15), "VIETNAM AIR FORCE & AIR DEFENSE (PK-KQ) - BATCH 3 GFX SHOWCASE", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad, 42), "Nâng cấp Bán kính Tác chiến & Mạng Phòng không Tích hợp IADS (6 Focuses)", fill=(160, 190, 220, 255), font=font_sub)

    for i, (ic, lbl) in enumerate(zip(icons, labels)):
        cx = pad + i * (card_w + pad)
        cy = pad + 50

        draw.rounded_rectangle((cx, cy, cx + card_w, cy + card_h), radius=8, fill=(24, 32, 46, 255), outline=(50, 70, 100, 255), width=2)
        draw.ellipse((cx + card_w // 2 - 45, cy + 20, cx + card_w // 2 + 45, cy + 110), fill=(10, 40, 75, 120))

        # Paste preview icon
        preview_sz = (93, 91)
        im.paste(ic, (cx + (card_w - preview_sz[0]) // 2, cy + 20), ic)

        # Label text box
        lines = lbl.split("\n")
        ty = cy + 125
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font_card)
            tw = bbox[2] - bbox[0]
            draw.text((cx + (card_w - tw) // 2, ty), line, fill=(230, 240, 255, 255), font=font_card)
            ty += 16

        draw.text((cx + card_w // 2 - 32, cy + card_h - 22), "33,980 B (DDS)", fill=(130, 170, 200, 255), font=font_sub)

    out_showcase = BRAIN_DIR / "air_batch_3_showcase.png"
    im.save(out_showcase)
    print(f"Saved Showcase: {out_showcase}")


def create_tree_simulation():
    """Generate in-game focus tree simulation for Batch 3."""
    im = Image.new("RGBA", (880, 520), (14, 18, 26, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_foc = ImageFont.truetype("arial.ttf", 10)
    except Exception:
        font_header = font_foc = ImageFont.load_default()

    draw.text((20, 15), "IN-GAME FOCUS TREE SIMULATION - BATCH 3 (PK-KQ & IADS)", fill=(255, 215, 0, 255), font=font_header)

    c_gold = (212, 175, 55, 200)

    # Spine: first_force (from Batch 2) -> command_reform_2 -> medium_force -> operating_range
    draw.line((440, 40, 440, 75), fill=c_gold, width=2)
    draw.line((440, 75 + 70, 440, 160), fill=c_gold, width=2)
    draw.line((440, 160 + 70, 440, 245), fill=c_gold, width=2)

    # operating_range -> Branch A: IADS
    draw.line((440, 245 + 70, 440, 325), fill=c_gold, width=2)
    draw.line((440, 325, 240 + 46, 325), fill=c_gold, width=2)
    draw.line((240 + 46, 325, 240 + 46, 335), fill=c_gold, width=2)

    # iads -> layered_defence
    draw.line((240 + 46, 335 + 70, 240 + 46, 420), fill=c_gold, width=2)

    # layered_defence -> ew_antistealth
    draw.line((240 + 46, 420 + 35, 550 + 46, 420 + 35), fill=c_gold, width=2)

    nodes = [
        ("airf_command_reform_2", "Cải cách Chỉ huy PK-KQ II", 440 - 46, 75),
        ("airf_medium_force", "Không quân Tầm trung", 440 - 46, 160),
        ("airf_operating_range", "Mở rộng Bán kính Tác chiến", 440 - 46, 245),
        ("airf_iads", "Phòng không Tích hợp (IADS)", 240, 335),
        ("airf_layered_defence", "Mạng Tên lửa Nhiều tầng", 240, 420),
        ("airf_ew_antistealth", "Tác chiến ĐT & Chống tàng hình", 550, 420),
    ]

    for stem, title, nx, ny in nodes:
        png_p = PNG_DIR / f"{stem}.png"
        if png_p.exists():
            ic = Image.open(png_p).convert("RGBA").resize((70, 68), Image.Resampling.LANCZOS)
        else:
            ic = Image.new("RGBA", (70, 68), (40, 50, 60, 255))

        outline_c = (235, 195, 60, 255)
        fill_c = (26, 36, 50, 255)
        draw.rounded_rectangle((nx, ny, nx + 92, ny + 74), radius=4, fill=fill_c, outline=outline_c, width=2)
        im.paste(ic, (nx + 11, ny + 3), ic)

        tb_w = 160
        tb_x = nx + 46 - tb_w // 2
        tb_y = ny + 76
        draw.rounded_rectangle((tb_x, tb_y, tb_x + tb_w, tb_y + 16), radius=3, fill=(15, 20, 28, 240), outline=outline_c, width=1)
        draw.text((tb_x + 6, tb_y + 2), title, fill=(255, 235, 140, 255), font=font_foc)

    out_sim = BRAIN_DIR / "air_batch_3_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def main():
    print("Building Air Force Batch 3 focus icons (PK-KQ & IADS)...")
    ic1 = build_airf_command_reform_2()
    ic2 = build_airf_medium_force()
    ic3 = build_airf_operating_range()
    ic4 = build_airf_iads()
    ic5 = build_airf_layered_defence()
    ic6 = build_airf_ew_antistealth()
    print("Completed all 6 icons for Air Force Batch 3!")

    icons = [ic1, ic2, ic3, ic4, ic5, ic6]
    labels = [
        "Cải cách Chỉ huy\nPK-KQ II",
        "Không quân\nTầm trung",
        "Mở rộng Bán kính\nTác chiến",
        "Phòng không\nTích hợp (IADS)",
        "Mạng Tên lửa\nNhiều tầng",
        "Tác chiến ĐT &\nChống tàng hình"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    print("Batch 3 build, showcase & simulation finished successfully!")


if __name__ == "__main__":
    main()
