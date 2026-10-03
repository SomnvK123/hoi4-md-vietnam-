"""Script to build Batch 3 Focus Icons for Vietnam Army (Lục quân) in Millennium Dawn.
Batch 3 focuses (8 combat arms focuses):
1. lf_arm_infantry_org: Bộ binh: tổ chức, cơ giới hóa (Modern BTR/APC carrier, mechanized arrow, VPA cockade)
2. lf_arm_infantry_train: Bộ binh: đào tạo sĩ quan & binh sĩ (Modern rifle equipment, golden training laurel, crossed cartridges)
3. lf_arm_armor_org: Tăng thiết giáp: tổ chức (T-90 Main Battle Tank, ERA armor, tactical armor chevron shield)
4. lf_arm_armor_train: Tăng thiết giáp: đào tạo kíp xe (Tank gun optics reticle, thermal sight, 125mm APFSDS rounds)
5. lf_arm_arty_org: Pháo binh: tổ chức, hỏa lực (152mm heavy howitzer firing, crossed cannons, VPA artillery shield)
6. lf_arm_arty_train: Pháo binh: đào tạo pháo thủ (Ballistic targeting grid, laser rangefinder, artillery shell, golden laurels)
7. lf_arm_engineers: Công binh: đào tạo & chiến đấu (Combat engineer gear, pontoon bridge, crossed sapper shovels & cogwheel)
8. lf_combined_arms: Hiệp đồng binh chủng (Tri-vector combined arms assault arrows, VPA star shield, armored fist)

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
        draw.polygon([center, tip, valley_left], fill=(255, 235, 100, 120))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(200, 150, 10, 140))
    return im


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


def create_vpa_tactical_shield(w: int = 34, h: int = 40) -> Image.Image:
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


def create_artillery_shell(w: int = 14, h: int = 38) -> Image.Image:
    """Generate a sharp 152mm high-explosive artillery projectile."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx = w / 2

    # Ogive tip
    pts_tip = [(cx - 2, 2), (cx + 2, 2), (cx + 5, 12), (cx - 5, 12)]
    draw.polygon(pts_tip, fill=(220, 180, 70, 255), outline=(140, 100, 20, 255))
    draw.ellipse((cx - 2, 1, cx + 2, 3), fill=(240, 210, 100, 255))

    # Main shell body (olive & brass driving band)
    draw.rectangle((cx - 5.5, 12, cx + 5.5, 34), fill=(60, 75, 55, 255), outline=(30, 42, 28, 255))
    # Driving band (copper)
    draw.rectangle((cx - 5.5, 27, cx + 5.5, 30), fill=(210, 120, 70, 255), outline=(140, 70, 30, 255))
    # Base
    draw.rectangle((cx - 5, 34, cx + 5, 36), fill=(45, 55, 40, 255))
    return im


# ==========================================
# 1. VIE_lf_arm_infantry_org (Cơ giới hóa bộ binh)
# ==========================================
def build_arm_infantry_org():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: APC armored personnel carrier
    p_apc = MD_SAMPLES / "apc.png"
    if p_apc.exists():
        apc = Image.open(p_apc).convert("RGBA")
        apc = apc.resize((82, 66), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(apc.convert("RGB")).enhance(1.20)
        enh = ImageEnhance.Color(enh).enhance(1.15)
        apc = Image.merge("RGBA", (*enh.split(), apc.split()[-1]))
        canvas.paste(apc, (6, 16), apc)

    # Tactical mechanized advance chevron (Red with gold border)
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(46, 6), (72, 22), (64, 22), (46, 12), (28, 22), (20, 22)], fill=(212, 175, 55, 255), outline=(130, 95, 20, 255))
    draw.polygon([(46, 9), (68, 22), (62, 22), (46, 14), (30, 22), (24, 22)], fill=(185, 25, 25, 255))

    # Small VPA star cockade at bottom right
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (62, 60), badge)

    save_game_ready_icon(canvas, "lf_arm_infantry_org")


# ==========================================
# 2. VIE_lf_arm_infantry_train (Đào tạo bộ binh)
# ==========================================
def build_arm_infantry_train():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Infantry equipment & rifle
    p_eq = MD_SAMPLES / "Focus_Infantry_Equipment.png"
    if p_eq.exists():
        eq = Image.open(p_eq).convert("RGBA")
        eq = eq.resize((82, 64), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(eq.convert("RGB")).enhance(1.25)
        eq = Image.merge("RGBA", (*enh.split(), eq.split()[-1]))
        canvas.paste(eq, (6, 14), eq)

    # Top VPA tactical shield
    shield = create_vpa_tactical_shield(32, 38)
    canvas.paste(shield, (31, 4), shield)

    # Golden laurels embracing bottom
    draw = ImageDraw.Draw(canvas)
    # Target reticle lines
    draw.ellipse((22, 24, 72, 74), outline=(212, 175, 55, 140), width=1)
    draw.line([(47, 20), (47, 78)], fill=(212, 175, 55, 160), width=1)
    draw.line([(18, 49), (76, 49)], fill=(212, 175, 55, 160), width=1)

    save_game_ready_icon(canvas, "lf_arm_infantry_train")


# ==========================================
# 3. VIE_lf_arm_armor_org (Tăng thiết giáp: tổ chức)
# ==========================================
def build_arm_armor_org():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Modern Main Battle Tank T-90
    p_tank = MD_SAMPLES / "md_t90.png"
    if p_tank.exists():
        tank = Image.open(p_tank).convert("RGBA")
        tank = tank.resize((84, 68), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(tank.convert("RGB")).enhance(1.25)
        enh = ImageEnhance.Color(enh).enhance(1.20)
        tank = Image.merge("RGBA", (*enh.split(), tank.split()[-1]))
        canvas.paste(tank, (5, 14), tank)

    # Heavy armor shield on top-left
    badge = create_vpa_cockade(size=30)
    canvas.paste(badge, (6, 6), badge)

    # Tactical armor spearhead arrow at top-right
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(78, 8), (88, 22), (80, 22), (80, 36), (76, 36), (76, 22), (68, 22)], fill=(212, 175, 55, 255), outline=(130, 95, 20, 255))
    draw.polygon([(78, 11), (85, 21), (79, 21), (79, 34), (77, 34), (77, 21), (71, 21)], fill=(185, 25, 25, 255))

    save_game_ready_icon(canvas, "lf_arm_armor_org")


# ==========================================
# 4. VIE_lf_arm_armor_train (Đào tạo kíp xe tăng)
# ==========================================
def build_arm_armor_train():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Armored assault motif
    p_assault = MD_SAMPLES / "Armored_Troops.png"
    if p_assault.exists():
        assault = Image.open(p_assault).convert("RGBA")
        assault = assault.resize((82, 66), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(assault.convert("RGB")).enhance(1.20)
        assault = Image.merge("RGBA", (*enh.split(), assault.split()[-1]))
        canvas.paste(assault, (6, 12), assault)

    # Tank optical reticle overlay (Thermal / laser sight)
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 44
    draw.ellipse((cx - 32, cy - 32, cx + 32, cy + 32), outline=(0, 220, 240, 180), width=1)
    draw.ellipse((cx - 18, cy - 18, cx + 18, cy + 18), outline=(0, 220, 240, 220), width=1)
    draw.line([(cx - 36, cy), (cx - 10, cy)], fill=(0, 220, 240, 220), width=1)
    draw.line([(cx + 10, cy), (cx + 36, cy)], fill=(0, 220, 240, 220), width=1)
    draw.line([(cx, cy - 36), (cx, cy - 10)], fill=(0, 220, 240, 220), width=1)
    draw.line([(cx, cy + 10), (cx, cy + 36)], fill=(0, 220, 240, 220), width=1)

    # Top VPA gold star badge
    star_badge = create_vpa_cockade(size=24)
    canvas.paste(star_badge, (35, 2), star_badge)

    save_game_ready_icon(canvas, "lf_arm_armor_train")


# ==========================================
# 5. VIE_lf_arm_arty_org (Pháo binh: tổ chức, hỏa lực)
# ==========================================
def build_arm_arty_org():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: 152mm howitzer firing
    p_arty = MD_SAMPLES / "artillery2.png"
    if p_arty.exists():
        arty = Image.open(p_arty).convert("RGBA")
        arty = arty.resize((86, 72), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(arty.convert("RGB")).enhance(1.25)
        enh = ImageEnhance.Color(enh).enhance(1.15)
        arty = Image.merge("RGBA", (*enh.split(), arty.split()[-1]))
        canvas.paste(arty, (4, 10), arty)

    # Top VPA artillery shield
    shield = create_vpa_tactical_shield(32, 38)
    canvas.paste(shield, (8, 6), shield)

    # Muzzle flash enhancement (bright yellow-orange starburst)
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((68, 16, 86, 34), fill=(255, 200, 50, 180), outline=(255, 120, 20, 220))
    draw.ellipse((72, 20, 82, 30), fill=(255, 255, 200, 240))

    save_game_ready_icon(canvas, "lf_arm_arty_org")


# ==========================================
# 6. VIE_lf_arm_arty_train (Pháo binh: đào tạo pháo thủ)
# ==========================================
def build_arm_arty_train():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Background ballistic mil-grid
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 44
    draw.ellipse((cx - 34, cy - 34, cx + 34, cy + 34), outline=(212, 175, 55, 150), width=1)
    draw.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), outline=(212, 175, 55, 180), width=1)
    draw.line([(cx - 38, cy), (cx + 38, cy)], fill=(212, 175, 55, 200), width=1)
    draw.line([(cx, cy - 38), (cx, cy + 38)], fill=(212, 175, 55, 200), width=1)

    # Artillery shell in foreground center
    shell = create_artillery_shell(16, 44)
    canvas.paste(shell, (39, 22), shell)

    # Crossed cannons or laurels flanking
    draw.line([(24, 72), (40, 56)], fill=(212, 175, 55, 255), width=2)
    draw.line([(70, 72), (54, 56)], fill=(212, 175, 55, 255), width=2)

    # Top VPA cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (34, 4), badge)

    save_game_ready_icon(canvas, "lf_arm_arty_train")


# ==========================================
# 7. VIE_lf_arm_engineers (Công binh: đào tạo & chiến đấu)
# ==========================================
def build_arm_engineers():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Engineer troops motif
    p_eng = MD_SAMPLES / "ARM_ssr_engineer_troops.png"
    if p_eng.exists():
        eng = Image.open(p_eng).convert("RGBA")
        eng = eng.resize((78, 74), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(eng.convert("RGB")).enhance(1.20)
        eng = Image.merge("RGBA", (*enh.split(), eng.split()[-1]))
        canvas.paste(eng, (8, 10), eng)

    # Top VPA shield
    shield = create_vpa_tactical_shield(32, 38)
    canvas.paste(shield, (31, 4), shield)

    # Crossed technical engineer shovels / bridge lightning bolt
    draw = ImageDraw.Draw(canvas)
    draw.line([(18, 78), (76, 78)], fill=(212, 175, 55, 240), width=3)
    draw.line([(24, 74), (70, 74)], fill=(120, 140, 160, 220), width=2)

    save_game_ready_icon(canvas, "lf_arm_engineers")


# ==========================================
# 8. VIE_lf_combined_arms (Hiệp đồng binh chủng)
# ==========================================
def build_combined_arms():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: MD combined arms asset
    p_comb = MD_SAMPLES / "combined_arms.png"
    if p_comb.exists():
        comb = Image.open(p_comb).convert("RGBA")
        comb = comb.resize((84, 72), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(comb.convert("RGB")).enhance(1.25)
        enh = ImageEnhance.Color(enh).enhance(1.20)
        comb = Image.merge("RGBA", (*enh.split(), comb.split()[-1]))
        canvas.paste(comb, (5, 10), comb)

    # Center: VPA Gold Star Shield
    shield = create_vpa_tactical_shield(36, 42)
    canvas.paste(shield, (29, 22), shield)

    # Three convergence assault arrows (Red, Gold, Cyan)
    draw = ImageDraw.Draw(canvas)
    # Left flank (Armor - Gold)
    draw.polygon([(14, 52), (26, 42), (24, 54)], fill=(255, 215, 0, 255), outline=(160, 120, 10, 255))
    # Right flank (Mechanized Infantry - Cyan)
    draw.polygon([(80, 52), (68, 42), (70, 54)], fill=(0, 220, 240, 255), outline=(0, 130, 150, 255))
    # Top strike (Artillery - Crimson)
    draw.polygon([(47, 4), (41, 16), (53, 16)], fill=(220, 30, 30, 255), outline=(130, 15, 15, 255))

    save_game_ready_icon(canvas, "lf_combined_arms")


if __name__ == "__main__":
    print("Building Batch 3 (8 Combat Arms icons)...")
    build_arm_infantry_org()
    build_arm_infantry_train()
    build_arm_armor_org()
    build_arm_armor_train()
    build_arm_arty_org()
    build_arm_arty_train()
    build_arm_engineers()
    build_combined_arms()
    print("Batch 3 icons built successfully!")
