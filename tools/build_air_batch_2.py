"""Script to build Batch 2 Focus Icons for Vietnam Air Force & Air Defense (PK-KQ) in Millennium Dawn.
Batch 2 focuses (Trục 3 Khởi đầu Quân chủng, Tiêm kích & Tên lửa Phòng không Nòng cốt - 5 focuses):
1. airf_training_standardization: Chuẩn hóa Đào tạo Phi công & Kỹ thuật viên
2. airf_fighter_force: Phát triển Lực lượng Tiêm kích
3. airf_sam_force: Phát triển Lực lượng Tên lửa SAM & Radar
4. airf_command_reform_1: Cải cách Chỉ huy PK-KQ I
5. airf_first_force: Cơ cấu Lực lượng Ban đầu

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
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals\00_airforce")

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
# 1. VIE_airf_training_standardization
# =========================================================================
def build_airf_training_standardization() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Generic_Pilots.dds (jet pilot in helmet, HUD visor, laurel wreath)
    base_path = MD_GOALS / "Generic_Pilots.dds"
    base = Image.open(base_path).convert("RGBA")

    # Scale to fit nicely with breathing room
    base_resized = base.resize((84, 69), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Subtle cyan HUD glow and crosshairs behind visor
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((46 - 9, 28 - 7, 46 + 9, 28 + 7), fill=(40, 180, 240, 60))
    draw.line((46 - 7, 28, 46 + 7, 28), fill=(80, 220, 255, 120), width=1)
    draw.line((46, 28 - 5, 46, 28 + 5), fill=(80, 220, 255, 120), width=1)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_training_standardization")
    return canvas


# =========================================================================
# 2. VIE_airf_fighter_force
# =========================================================================
def build_airf_fighter_force() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: modern_fighter.dds (Su-27/Su-30 Flanker soaring over sea/sky with golden laurel wreath)
    base_path = MD_GOALS / "modern_fighter.dds"
    base = Image.open(base_path).convert("RGBA")

    # Slight color/contrast enhancement for vibrant aviation atmosphere
    base = ImageEnhance.Color(base).enhance(1.15)
    base = ImageEnhance.Contrast(base).enhance(1.08)

    # Resize to fit frame
    base_resized = base.resize((86, 73), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_fighter_force")
    return canvas


# =========================================================================
# 3. VIE_airf_sam_force
# =========================================================================
def build_airf_sam_force() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: guided_missile.dds (supersonic SAM launch over TEL exhaust plume in wreath)
    base_path = MD_GOALS / "guided_missile.dds"
    base = Image.open(base_path).convert("RGBA")

    # Inpaint the Russian tricolor stripe (around x=48..54, y=50..58) to sleek missile off-white / haze gray
    base_clean = base.copy()
    draw_base = ImageDraw.Draw(base_clean)
    # Paint over stripe with missile body off-white
    draw_base.polygon([(46, 50), (55, 48), (55, 59), (46, 61)], fill=(228, 230, 235, 255))
    # Add thin tactical red ring for VPA PK-KQ missile marking
    draw_base.line([(48, 54), (54, 52)], fill=(200, 25, 25, 255), width=2)

    # Resize to fit target frame
    base_resized = base_clean.resize((85, 85), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_sam_force")
    return canvas


# =========================================================================
# 4. VIE_airf_command_reform_1
# =========================================================================
def build_airf_command_reform_1() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: air_doctrine.dds (winged chess king flanked by winged knights)
    base_path = MD_GOALS / "air_doctrine.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 70), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-2)

    # Add VPA cockade roundel to the central king piece
    cockade = create_vpa_cockade(19)
    paste_centered(canvas, cockade, offset_x=0, offset_y=-2)

    # Faceted gold star at apex above king crown
    star = create_gold_star_with_glow(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Golden Air Force wings at bottom
    wings = create_airforce_wings(38, 14)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_command_reform_1")
    return canvas


# =========================================================================
# 5. VIE_airf_first_force
# =========================================================================
def build_airf_first_force() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: airforce_base_1.dds (3 supersonic fighters in formation over satellite globe)
    base_path = MD_GOALS / "airforce_base_1.dds"
    base = Image.open(base_path).convert("RGBA")

    # Resize to fit frame
    base_resized = base.resize((86, 71), Image.Resampling.LANCZOS)
    paste_centered(canvas, base_resized, offset_x=0, offset_y=-3)

    # Cover the lower center plane silhouette with a small VPA roundel
    cockade = create_vpa_cockade(14)
    paste_centered(canvas, cockade, offset_x=0, offset_y=26)

    # Faceted gold star at apex with drop shadow
    star = create_gold_star_with_glow(20)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Layer golden air force wings at bottom ribbon
    wings = create_airforce_wings(42, 15)
    paste_centered(canvas, wings, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "airf_first_force")
    return canvas


def create_showcase(icons, labels):
    """Generate a high-res showcase banner for Batch 2."""
    card_w, card_h = 170, 210
    pad = 20
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

    draw.text((pad, 15), "VIETNAM AIR FORCE & AIR DEFENSE (PK-KQ) - BATCH 2 GFX SHOWCASE", fill=(255, 215, 0, 255), font=font_title)
    draw.text((pad, 42), "Trục 3: Khởi đầu Quân chủng, Tiêm kích & Tên lửa Phòng không Nòng cốt (5 Focuses)", fill=(160, 190, 220, 255), font=font_sub)

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

    out_showcase = BRAIN_DIR / "air_batch_2_showcase.png"
    im.save(out_showcase)
    print(f"Saved Showcase: {out_showcase}")


def create_tree_simulation():
    """Generate in-game focus tree simulation for Batch 2 in relation to Batch 1 and Root."""
    im = Image.new("RGBA", (850, 460), (14, 18, 26, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_header = ImageFont.truetype("arialbd.ttf", 16)
        font_foc = ImageFont.truetype("arial.ttf", 10)
    except Exception:
        font_header = font_foc = ImageFont.load_default()

    draw.text((20, 15), "IN-GAME FOCUS TREE SIMULATION - AIR FORCE TRỤC 3 (BATCH 2)", fill=(255, 215, 0, 255), font=font_header)

    # Connections
    c_gold = (212, 175, 55, 200)

    # Root -> airf_training_standardization
    draw.line((425, 45 + 35, 425, 100), fill=c_gold, width=2)

    # airf_training_standardization -> fighter_force & sam_force
    draw.line((425, 100 + 70, 425, 185), fill=c_gold, width=2)
    draw.line((240 + 46, 185, 610 + 46, 185), fill=c_gold, width=2)
    draw.line((240 + 46, 185, 240 + 46, 195), fill=c_gold, width=2)
    draw.line((610 + 46, 185, 610 + 46, 195), fill=c_gold, width=2)

    # fighter_force & sam_force -> command_reform_1
    draw.line((240 + 46, 195 + 70, 240 + 46, 280), fill=c_gold, width=2)
    draw.line((610 + 46, 195 + 70, 610 + 46, 280), fill=c_gold, width=2)
    draw.line((240 + 46, 280, 610 + 46, 280), fill=c_gold, width=2)
    draw.line((425, 280, 425, 290), fill=c_gold, width=2)

    # command_reform_1 -> first_force
    draw.line((425, 290 + 70, 425, 375), fill=c_gold, width=2)

    nodes = [
        ("airf_training_standardization", "Chuẩn hóa Đào tạo Phi công", 425 - 46, 100),
        ("airf_fighter_force", "Lực lượng Tiêm kích", 240, 195),
        ("airf_sam_force", "Lực lượng Tên lửa SAM", 610, 195),
        ("airf_command_reform_1", "Cải cách Chỉ huy PK-KQ I", 425 - 46, 290),
        ("airf_first_force", "Cơ cấu Lực lượng Ban đầu", 425 - 46, 375),
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

        tb_w = 150
        tb_x = nx + 46 - tb_w // 2
        tb_y = ny + 76
        draw.rounded_rectangle((tb_x, tb_y, tb_x + tb_w, tb_y + 16), radius=3, fill=(15, 20, 28, 240), outline=outline_c, width=1)
        draw.text((tb_x + 6, tb_y + 2), title, fill=(255, 235, 140, 255), font=font_foc)

    out_sim = BRAIN_DIR / "air_batch_2_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def main():
    print("Building Air Force Batch 2 focus icons (PK-KQ Trục 3)...")
    ic1 = build_airf_training_standardization()
    ic2 = build_airf_fighter_force()
    ic3 = build_airf_sam_force()
    ic4 = build_airf_command_reform_1()
    ic5 = build_airf_first_force()
    print("Completed all 5 icons for Air Force Batch 2!")

    icons = [ic1, ic2, ic3, ic4, ic5]
    labels = [
        "Chuẩn hóa\nĐào tạo Phi công",
        "Phát triển\nLực lượng Tiêm kích",
        "Lực lượng\nTên lửa SAM & Radar",
        "Cải cách Chỉ huy\nPK-KQ I",
        "Cơ cấu Lực lượng\nBan đầu"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    print("Batch 2 build, showcase & simulation finished successfully!")


if __name__ == "__main__":
    main()
