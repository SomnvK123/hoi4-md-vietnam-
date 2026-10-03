"""Script to build Batch 2 Focus Icons for Vietnam Army (Lục quân) in Millennium Dawn.
Batch 2 focuses:
1. lf_army_reform: Cải cách quân đội, tinh gọn biên chế (VPA command shield, tactical arrows, streamlined org nodes)
2. lf_logistics_merge: Hợp nhất Hậu cần – Kỹ thuật (Kamaz military 6x6 truck, crossed technical wrenches, VPA cockade)
3. lf_basic_training: Đào tạo lục quân cơ bản (Bia bắn số 4 quân sự, modern soldier aiming STV rifle, 7.62mm cartridges, golden laurels)

Generates 93x91 transparent PNG and uncompressed 32-bit BGRA DDS files.
"""

import os
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
MD_SAMPLES = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f\md_samples")

TARGET_SIZE = (93, 91)


def save_game_ready_icon(canvas: Image.Image, stem: str):
    """Save canvas as transparent PNG and 32-bit BGRA uncompressed DDS."""
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

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
    print(f"Saved DDS: {dds_path}")


def create_gold_star(size: int) -> Image.Image:
    """Generate a sharp 5-pointed gold star with faceted shading."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1
    r_inner = r_outer * 0.382

    # Draw individual faceted triangles for 3D metallic feel
    pts = []
    for i in range(10):
        ang = i * math.pi / 5 - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))

    # Main gold body
    draw.polygon(pts, fill=(255, 215, 0, 255), outline=(170, 130, 20, 255))

    # Facet shading on left side of each ray
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 235, 100, 120))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(200, 150, 10, 140))

    return im


def create_vpa_cockade(size: int = 34) -> Image.Image:
    """Generate an official VPA roundel cockade."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2
    r_outer = size / 2 - 1

    # Outer gold rim
    draw.ellipse((cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer), fill=(212, 175, 55, 255), outline=(130, 95, 20, 255), width=1)
    
    # Inner dark red circle
    r_inner = r_outer - 2.5
    draw.ellipse((cx - r_inner, cy - r_inner, cx + r_inner, cy + r_inner), fill=(185, 25, 25, 255), outline=(120, 15, 15, 255), width=1)

    # Gold star
    star_sz = int(r_inner * 1.5)
    star = create_gold_star(star_sz)
    im.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2)), star)
    return im


def create_vpa_tactical_shield(w: int = 36, h: int = 42) -> Image.Image:
    """Generate a sleek angular VPA tactical shield."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    pts = [(2, 2), (w - 3, 2), (w - 3, int(h * 0.62)), (int(w / 2), h - 2), (2, int(h * 0.62))]
    draw.polygon(pts, fill=(212, 175, 55, 255), outline=(120, 85, 15, 255))

    pts_in = [(4, 4), (w - 5, 4), (w - 5, int(h * 0.60)), (int(w / 2), h - 5), (4, int(h * 0.60))]
    draw.polygon(pts_in, fill=(180, 25, 25, 255), outline=(110, 15, 15, 255))

    star = create_gold_star(int(w * 0.58))
    im.paste(star, (int((w - star.width) / 2), int(h * 0.16)), star)
    return im


def create_rifle_cartridge(w: int = 12, h: int = 34) -> Image.Image:
    """Generate a sharp 7.62x39mm brass/copper cartridge."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx = w / 2

    # Copper bullet tip
    tip_pts = [(cx - 2.5, 11), (cx, 1), (cx + 2.5, 11)]
    draw.polygon(tip_pts, fill=(210, 115, 70, 255), outline=(120, 60, 30, 255))

    # Brass neck & shoulder
    draw.polygon([(cx - 3, 11), (cx + 3, 11), (cx + 4.5, 15), (cx - 4.5, 15)], fill=(212, 175, 55, 255), outline=(130, 100, 25, 255))

    # Brass case body
    draw.rectangle((cx - 4.5, 15, cx + 4.5, 29), fill=(212, 175, 55, 255), outline=(130, 100, 25, 255))

    # Extractor groove
    draw.rectangle((cx - 4, 29, cx + 4, 31), fill=(140, 110, 25, 255))

    # Rim
    draw.rectangle((cx - 5, 31, cx + 5, 33), fill=(212, 175, 55, 255), outline=(130, 100, 25, 255))

    return im


def create_bullseye_target(size: int = 62) -> Image.Image:
    """Generate military shooting target (Bia bắn số 4 quân sự)."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx, cy = size / 2, size / 2

    # Ring 4: Tactical olive
    r4 = size / 2 - 2
    draw.ellipse((cx - r4, cy - r4, cx + r4, cy + r4), fill=(40, 58, 36, 255), outline=(18, 28, 18, 255), width=2)

    # Ring 3: Olive tone
    r3 = r4 * 0.74
    draw.ellipse((cx - r3, cy - r3, cx + r3, cy + r3), fill=(52, 74, 48, 255), outline=(25, 38, 24, 255), width=1)

    # Ring 2: Parchment off-white
    r2 = r4 * 0.50
    draw.ellipse((cx - r2, cy - r2, cx + r2, cy + r2), fill=(232, 228, 214, 255), outline=(25, 38, 24, 255), width=1)

    # Ring 1: Dark bullseye center
    r1 = r4 * 0.26
    draw.ellipse((cx - r1, cy - r1, cx + r1, cy + r1), fill=(28, 28, 28, 255), outline=(170, 35, 35, 255), width=1)

    # Center red pip
    r0 = r4 * 0.08
    draw.ellipse((cx - r0, cy - r0, cx + r0, cy + r0), fill=(215, 30, 30, 255))

    # Crosshairs
    draw.line((cx - r4, cy, cx - r1 * 0.7, cy), fill=(255, 255, 255, 190), width=1)
    draw.line((cx + r1 * 0.7, cy, cx + r4, cy), fill=(255, 255, 255, 190), width=1)
    draw.line((cx, cy - r4, cx, cy - r1 * 0.7), fill=(255, 255, 255, 190), width=1)
    draw.line((cx, cy + r1 * 0.7, cx, cy + r4), fill=(255, 255, 255, 190), width=1)

    return im


def build_army_reform():
    """Build VIE_lf_army_reform (Cải cách quân đội, tinh gọn biên chế)."""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # 1. Base framework from MD army_reform
    p_base = MD_SAMPLES / "sample_army_reform.png"
    if p_base.exists():
        base = Image.open(p_base).convert("RGBA")
        base = base.resize((82, 74), Image.Resampling.LANCZOS)
        # Enhance contrast
        enh = ImageEnhance.Contrast(base.convert("RGB")).enhance(1.15)
        base = Image.merge("RGBA", (*enh.split(), base.split()[-1]))
        canvas.paste(base, (6, 8), base)

    # 2. Add central VPA tactical shield
    shield = create_vpa_tactical_shield(34, 40)
    canvas.paste(shield, (30, 18), shield)

    # 3. Add strategic reform arrows (red & cyan) indicating streamlined command
    draw = ImageDraw.Draw(canvas)
    # Right flank arrow (Cyan C4I)
    draw.polygon([(70, 38), (82, 38), (76, 30)], fill=(0, 210, 240, 220), outline=(0, 130, 160, 255))
    # Left flank arrow (Crimson VPA)
    draw.polygon([(22, 38), (10, 38), (16, 30)], fill=(220, 40, 40, 220), outline=(140, 20, 20, 255))

    # 4. Streamlined 3-node hierarchy at the bottom
    # Center node
    draw.rectangle((41, 68, 51, 74), fill=(212, 175, 55, 255), outline=(130, 95, 20, 255))
    # Left node
    draw.rectangle((21, 75, 31, 81), fill=(180, 30, 30, 255), outline=(100, 15, 15, 255))
    # Right node
    draw.rectangle((61, 75, 71, 81), fill=(0, 180, 220, 255), outline=(0, 100, 130, 255))
    # Connecting lines
    draw.line([(46, 74), (46, 78), (26, 78), (26, 75)], fill=(212, 175, 55, 220), width=1)
    draw.line([(46, 78), (66, 78), (66, 75)], fill=(212, 175, 55, 220), width=1)

    save_game_ready_icon(canvas, "lf_army_reform")


def build_logistics_merge():
    """Build VIE_lf_logistics_merge (Hợp nhất Hậu cần – Kỹ thuật)."""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # 1. Background: Technical gear wheel
    p_supply = MD_SAMPLES / "sample_focus_generic_supply_line.png"
    if p_supply.exists():
        supply_bg = Image.open(p_supply).convert("RGBA")
        supply_bg = supply_bg.resize((84, 76), Image.Resampling.LANCZOS)
        # Tone down to subtle dark titanium background
        supply_alpha = supply_bg.split()[-1].point(lambda p: int(p * 0.45))
        supply_bg.putalpha(supply_alpha)
        canvas.paste(supply_bg, (5, 6), supply_bg)

    # 2. Hero: KamAZ 6x6 Military Transport Truck (Hậu cần)
    p_kamaz = MD_SAMPLES / "sample_kamaz.png"
    if p_kamaz.exists():
        truck = Image.open(p_kamaz).convert("RGBA")
        truck = truck.resize((78, 68), Image.Resampling.LANCZOS)
        # Enhance military contrast and olive saturation
        enh = ImageEnhance.Contrast(truck.convert("RGB")).enhance(1.25)
        enh = ImageEnhance.Color(enh).enhance(1.20)
        truck = Image.merge("RGBA", (*enh.split(), truck.split()[-1]))
        canvas.paste(truck, (8, 12), truck)

    # 3. Foreground: Crossed Technical Wrenches (Kỹ thuật)
    p_wrenches = MD_SAMPLES / "continuous_repairments.png"
    if p_wrenches.exists():
        wrenches = Image.open(p_wrenches).convert("RGBA")
        wrenches = wrenches.resize((48, 48), Image.Resampling.LANCZOS)
        # Add drop shadow
        shadow = wrenches.split()[-1].filter(ImageFilter.GaussianBlur(1.2))
        shadow_im = Image.new("RGBA", wrenches.size, (0, 0, 0, 180))
        shadow_im.putalpha(shadow)
        canvas.paste(shadow_im, (44, 40), shadow_im)
        canvas.paste(wrenches, (43, 39), wrenches)

    # 4. VPA Star Cockade (top-left)
    cockade = create_vpa_cockade(size=28)
    # subtle shadow
    c_shadow = cockade.split()[-1].filter(ImageFilter.GaussianBlur(1.0))
    c_shadow_im = Image.new("RGBA", cockade.size, (0, 0, 0, 160))
    c_shadow_im.putalpha(c_shadow)
    canvas.paste(c_shadow_im, (7, 6), c_shadow_im)
    canvas.paste(cockade, (6, 5), cockade)

    save_game_ready_icon(canvas, "lf_logistics_merge")


def build_basic_training():
    """Build VIE_lf_basic_training (Đào tạo lục quân cơ bản)."""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # 1. Background: Military target (Bia bắn số 4)
    target = create_bullseye_target(size=60)
    canvas.paste(target, (16, 8), target)

    # 2. Hero: Modern infantry soldier aiming rifle
    p_soldier = MD_SAMPLES / "Generic_Soldier_Aiming.png"
    if p_soldier.exists():
        soldier = Image.open(p_soldier).convert("RGBA")
        soldier = soldier.resize((72, 64), Image.Resampling.LANCZOS)
        # Adjust tone to Vietnamese army olive/camo
        enh = ImageEnhance.Contrast(soldier.convert("RGB")).enhance(1.20)
        enh = ImageEnhance.Color(enh).enhance(1.10)
        soldier = Image.merge("RGBA", (*enh.split(), soldier.split()[-1]))

        # Shadow behind soldier
        s_shadow = soldier.split()[-1].filter(ImageFilter.GaussianBlur(1.2))
        s_shadow_im = Image.new("RGBA", soldier.size, (0, 0, 0, 160))
        s_shadow_im.putalpha(s_shadow)
        canvas.paste(s_shadow_im, (18, 16), s_shadow_im)
        canvas.paste(soldier, (17, 15), soldier)

    # 3. Two crossed 7.62x39mm rifle cartridges at bottom
    cart1 = create_rifle_cartridge(w=10, h=30).rotate(25, expand=True, resample=Image.Resampling.BICUBIC)
    cart2 = create_rifle_cartridge(w=10, h=30).rotate(-25, expand=True, resample=Image.Resampling.BICUBIC)

    canvas.paste(cart1, (26, 52), cart1)
    canvas.paste(cart2, (46, 52), cart2)

    # 4. VPA red-and-gold star cockade at the top
    top_badge = create_vpa_cockade(size=24)
    canvas.paste(top_badge, (34, 1), top_badge)

    save_game_ready_icon(canvas, "lf_basic_training")


if __name__ == "__main__":
    print("Building Batch 2 icons...")
    build_army_reform()
    build_logistics_merge()
    build_basic_training()
    print("Batch 2 icons built successfully!")
