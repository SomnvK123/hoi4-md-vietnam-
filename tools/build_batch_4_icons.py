"""Script to build Batch 4 Focus Icons for Vietnam Army (Lục quân) in Millennium Dawn.
Batch 4 focuses (9 Force Structure & Strategic Doctrine focuses):
1. lf_command_reform_1: Cải cách bộ chỉ huy I (Command power, tactical battle map arrows, VPA shield)
2. lf_fs_mobile_force: Lực lượng cơ động (High-speed wheeled armored carrier, gold tactical chevrons, speed streaks)
3. lf_fs_mobile_corps: Cụm cơ động (Mi-17 transport helicopter, air-ground mechanized coordination, VPA cockade)
4. lf_fs_main_corps: Quân đoàn chủ lực chính quy (Quyet Chien Quyet Thang VPA flag, heavy T-90 armored formation)
5. lf_fs_lean_corps: Quân đoàn tinh, gọn, mạnh (Angular titanium lean shield, faceted 3D gold star, streamlined laurels)
6. lf_fs_depth_defence: Phòng thủ chiều sâu (Concrete bunker fortification, layered defensive perimeter, gold star shield)
7. lf_fs_militia_units: Dân quân tự vệ toàn dân (Militia riflemen, red armband, golden rice sheaves, star roundel)
8. lf_dev_strategic: Cơ động chiến lược (Strategic mobility vector, national S-curve deployment arrow, transport aircraft)
9. lf_dev_territorial: Phòng thủ khu vực & dự bị (Regional defense fortress, territorial shield, golden bastions)

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


# ==========================================
# 1. VIE_lf_command_reform_1 (Cải cách bộ chỉ huy I)
# ==========================================
def build_command_reform_1():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Command Power motif
    p_cmd = MD_SAMPLES / "Generic_Command_Power.png"
    if p_cmd.exists():
        cmd = Image.open(p_cmd).convert("RGBA")
        cmd = cmd.resize((78, 72), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(cmd.convert("RGB")).enhance(1.20)
        cmd = Image.merge("RGBA", (*enh.split(), cmd.split()[-1]))
        canvas.paste(cmd, (7, 10), cmd)

    # Central VPA shield
    shield = create_vpa_tactical_shield(32, 38)
    canvas.paste(shield, (31, 20), shield)

    # Tactical battle arrows (Cyan C4I & Red VPA)
    draw = ImageDraw.Draw(canvas)
    draw.polygon([(68, 14), (82, 14), (75, 6)], fill=(0, 220, 240, 240), outline=(0, 130, 160, 255))
    draw.polygon([(25, 14), (11, 14), (18, 6)], fill=(220, 30, 30, 240), outline=(140, 20, 20, 255))

    save_game_ready_icon(canvas, "lf_command_reform_1")


# ==========================================
# 2. VIE_lf_fs_mobile_force (Lực lượng cơ động)
# ==========================================
def build_fs_mobile_force():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Wheeled APC with speed
    p_apc = MD_SAMPLES / "apc.png"
    if p_apc.exists():
        apc = Image.open(p_apc).convert("RGBA")
        apc = apc.resize((82, 66), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(apc.convert("RGB")).enhance(1.25)
        apc = Image.merge("RGBA", (*enh.split(), apc.split()[-1]))
        canvas.paste(apc, (8, 16), apc)

    # Motion speed streaks behind vehicle
    draw = ImageDraw.Draw(canvas)
    draw.line([(6, 38), (28, 38)], fill=(255, 215, 0, 180), width=2)
    draw.line([(4, 48), (22, 48)], fill=(0, 210, 240, 180), width=2)
    draw.line([(8, 58), (26, 58)], fill=(255, 215, 0, 180), width=2)

    # Double forward mobility chevron at top right
    draw.polygon([(66, 6), (82, 18), (76, 18), (66, 10), (56, 18), (50, 18)], fill=(212, 175, 55, 255), outline=(140, 105, 20, 255))
    draw.polygon([(66, 14), (82, 26), (76, 26), (66, 18), (56, 26), (50, 26)], fill=(220, 30, 30, 255), outline=(140, 20, 20, 255))

    # VPA cockade top left
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (6, 6), badge)

    save_game_ready_icon(canvas, "lf_fs_mobile_force")


# ==========================================
# 3. VIE_lf_fs_mobile_corps (Cụm cơ động)
# ==========================================
def build_fs_mobile_corps():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Transport Helicopter (Mi-17 air assault)
    p_heli = MD_SAMPLES / "Generic_Transport_Helicopter.png"
    if p_heli.exists():
        heli = Image.open(p_heli).convert("RGBA")
        heli = heli.resize((82, 60), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(heli.convert("RGB")).enhance(1.25)
        heli = Image.merge("RGBA", (*enh.split(), heli.split()[-1]))
        canvas.paste(heli, (6, 6), heli)

    # Ground armor silhouette at bottom
    p_tank = MD_SAMPLES / "Armored_Troops.png"
    if p_tank.exists():
        tank = Image.open(p_tank).convert("RGBA")
        tank = tank.resize((66, 50), Image.Resampling.LANCZOS)
        canvas.paste(tank, (20, 38), tank)

    # Top VPA cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (34, 2), badge)

    save_game_ready_icon(canvas, "lf_fs_mobile_corps")


# ==========================================
# 4. VIE_lf_fs_main_corps (Quân đoàn chủ lực chính quy)
# ==========================================
def build_fs_main_corps():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: T-90 Main Battle Tank formation
    p_tank = MD_SAMPLES / "md_t90.png"
    if p_tank.exists():
        tank = Image.open(p_tank).convert("RGBA")
        tank = tank.resize((84, 68), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(tank.convert("RGB")).enhance(1.20)
        tank = Image.merge("RGBA", (*enh.split(), tank.split()[-1]))
        canvas.paste(tank, (6, 18), tank)

    # Large VPA Victory Flag waving at top (Cờ Quyết chiến Quyết thắng)
    draw = ImageDraw.Draw(canvas)
    # Flagpole
    draw.line([(12, 4), (12, 54)], fill=(212, 175, 55, 255), width=2)
    # Red flag fabric
    flag_pts = [(13, 6), (56, 6), (52, 28), (13, 26)]
    draw.polygon(flag_pts, fill=(215, 25, 25, 255), outline=(130, 15, 15, 255))
    # Gold star in flag
    star = create_gold_star(16)
    canvas.paste(star, (22, 9), star)

    save_game_ready_icon(canvas, "lf_fs_main_corps")


# ==========================================
# 5. VIE_lf_fs_lean_corps (Quân đoàn tinh, gọn, mạnh)
# ==========================================
def build_fs_lean_corps():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Sharp angular titanium lean shield
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 44
    # Outer cut-corner polygon
    pts_outer = [
        (47, 4), (82, 22), (76, 66), (47, 86), (18, 66), (12, 22)
    ]
    draw.polygon(pts_outer, fill=(45, 55, 68, 255), outline=(212, 175, 55, 255), width=2)

    # Inner crimson facet
    pts_inner = [
        (47, 10), (76, 25), (71, 62), (47, 80), (23, 62), (18, 25)
    ]
    draw.polygon(pts_inner, fill=(185, 25, 25, 255), outline=(120, 15, 15, 255))

    # 3 Converging tactical reform chevrons
    draw.polygon([(47, 16), (54, 28), (47, 25), (40, 28)], fill=(255, 215, 0, 255))
    draw.polygon([(26, 42), (38, 42), (35, 48), (24, 46)], fill=(0, 220, 240, 255))
    draw.polygon([(68, 42), (56, 42), (59, 48), (70, 46)], fill=(0, 220, 240, 255))

    # Large central faceted gold star
    star = create_gold_star(34)
    canvas.paste(star, (int(cx - star.width / 2), 34), star)

    save_game_ready_icon(canvas, "lf_fs_lean_corps")


# ==========================================
# 6. VIE_lf_fs_depth_defence (Phòng thủ chiều sâu)
# ==========================================
def build_fs_depth_defence():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Reinforced military fortification / bunker
    p_fort = MD_SAMPLES / "military_fort.png"
    if p_fort.exists():
        fort = Image.open(p_fort).convert("RGBA")
        fort = fort.resize((82, 70), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(fort.convert("RGB")).enhance(1.20)
        fort = Image.merge("RGBA", (*enh.split(), fort.split()[-1]))
        canvas.paste(fort, (6, 12), fort)

    # Layered defense perimeter rings
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 46
    draw.arc((cx - 38, cy - 38, cx + 38, cy + 38), start=180, end=360, fill=(212, 175, 55, 200), width=2)
    draw.arc((cx - 28, cy - 28, cx + 28, cy + 28), start=180, end=360, fill=(0, 220, 240, 220), width=2)

    # Top VPA defense cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (34, 2), badge)

    save_game_ready_icon(canvas, "lf_fs_depth_defence")


# ==========================================
# 7. VIE_lf_fs_militia_units (Dân quân tự vệ toàn dân)
# ==========================================
def build_fs_militia_units():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Militia soldiers
    p_militia = MD_SAMPLES / "Communal_Militias.png"
    if p_militia.exists():
        militia = Image.open(p_militia).convert("RGBA")
        militia = militia.resize((84, 68), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(militia.convert("RGB")).enhance(1.25)
        enh = ImageEnhance.Color(enh).enhance(1.15)
        militia = Image.merge("RGBA", (*enh.split(), militia.split()[-1]))
        canvas.paste(militia, (5, 14), militia)

    # Top VPA roundel cockade (Pith helmet star roundel)
    cockade = create_vpa_cockade(size=30)
    canvas.paste(cockade, (32, 2), cockade)

    # Red armband banner across bottom
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((18, 74, 76, 84), fill=(200, 25, 25, 255), outline=(130, 15, 15, 255))
    draw.line([(20, 76), (74, 76)], fill=(255, 215, 0, 255), width=1)
    draw.line([(20, 82), (74, 82)], fill=(255, 215, 0, 255), width=1)

    save_game_ready_icon(canvas, "lf_fs_militia_units")


# ==========================================
# 8. VIE_lf_dev_strategic (Cơ động chiến lược)
# ==========================================
def build_dev_strategic():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # S-Curve Strategic Highway Vector (North-South mobility)
    draw = ImageDraw.Draw(canvas)
    # Sweeping gold strategic mobility arrow
    curve_pts = [
        (38, 8), (44, 18), (56, 32), (48, 52), (38, 68), (50, 82)
    ]
    for i in range(len(curve_pts) - 1):
        draw.line([curve_pts[i], curve_pts[i+1]], fill=(212, 175, 55, 240), width=4)
    # Arrowhead at south
    draw.polygon([(44, 76), (56, 86), (58, 74)], fill=(255, 215, 0, 255), outline=(160, 120, 10, 255))

    # Helicopter / tactical transport on vector
    p_heli = MD_SAMPLES / "Generic_Transport_Helicopter.png"
    if p_heli.exists():
        heli = Image.open(p_heli).convert("RGBA")
        heli = heli.resize((68, 50), Image.Resampling.LANCZOS)
        canvas.paste(heli, (18, 16), heli)

    # Top VPA cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (8, 6), badge)

    save_game_ready_icon(canvas, "lf_dev_strategic")


# ==========================================
# 9. VIE_lf_dev_territorial (Phòng thủ khu vực & dự bị)
# ==========================================
def build_dev_territorial():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Defense shield & strategy
    p_def = MD_SAMPLES / "army_defence1.png"
    if p_def.exists():
        def_im = Image.open(p_def).convert("RGBA")
        def_im = def_im.resize((82, 72), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(def_im.convert("RGB")).enhance(1.20)
        def_im = Image.merge("RGBA", (*enh.split(), def_im.split()[-1]))
        canvas.paste(def_im, (6, 10), def_im)

    # Territorial defense shield in center
    shield = create_vpa_tactical_shield(36, 42)
    canvas.paste(shield, (29, 20), shield)

    # Bastion fortifications flanking
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((10, 56, 22, 72), fill=(60, 72, 85, 255), outline=(212, 175, 55, 255))
    draw.rectangle((72, 56, 84, 72), fill=(60, 72, 85, 255), outline=(212, 175, 55, 255))

    save_game_ready_icon(canvas, "lf_dev_territorial")


if __name__ == "__main__":
    print("Building Batch 4 (9 Force Structure & Strategic Doctrine icons)...")
    build_command_reform_1()
    build_fs_mobile_force()
    build_fs_mobile_corps()
    build_fs_main_corps()
    build_fs_lean_corps()
    build_fs_depth_defence()
    build_fs_militia_units()
    build_dev_strategic()
    build_dev_territorial()
    print("Batch 4 icons built successfully!")
