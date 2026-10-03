"""Script to build Batch 5 Focus Icons for Vietnam Army (Lục quân) in Millennium Dawn.
Batch 5 focuses (10 High-Tech, Cyber & Capstone focuses):
1. lf_command_reform_2: Cải cách bộ chỉ huy II (Operations center radar screen, satellite link, command stylus, VPA shield)
2. lf_cap_border_urban: Tác chiến biên giới và đô thị (Border stone pillar with national emblem, urban bunker, STV rifle)
3. lf_cap_area_control: Khống chế địa bàn (Special forces commandos, crossed tactical daggers, night infrared grid)
4. lf_cap_army_ad: Phòng không lục quân (Mobile SAM anti-air missile launcher, low-altitude tracking radar, VPA badge)
5. lf_cap_ad_coord: Hiệp đồng PK với PK-KQ (Long-range phased-array radar dome, soaring SAM missile, golden laurels)
6. lf_cap_cyber_ew: Tác chiến mạng và điện tử (Electronic jamming antenna, pulsing cyan electromagnetic waves, cyber shield)
7. lf_cap_info_ops: Tác chiến thông tin hiệp đồng (Military C4ISR satellite in orbit, tactical downlink beam, digital network)
8. lf_selective_modernization: Hiện đại hóa chọn lọc (NVG night vision goggles on ballistic helmet, green phosphor glow, optical sight)
9. lf_command_reform_3: Cải cách bộ chỉ huy III (3D holographic joint command war-table, strategic AI arrows, golden general laurels)
10. lf_force_complete: Hoàn thiện lực lượng vũ trang (Grand VPA emblem, radiant sunburst, golden rice wreath, victory banner)

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
# 1. VIE_lf_command_reform_2 (Cải cách bộ chỉ huy II)
# ==========================================
def build_command_reform_2():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Radar screen & operations command
    p_cmd = MD_SAMPLES / "Generic_Command_Power.png"
    if p_cmd.exists():
        cmd = Image.open(p_cmd).convert("RGBA")
        cmd = cmd.resize((82, 74), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(cmd.convert("RGB")).enhance(1.20)
        cmd = Image.merge("RGBA", (*enh.split(), cmd.split()[-1]))
        canvas.paste(cmd, (5, 10), cmd)

    # Tactical satellite uplink grid (cyan lines)
    draw = ImageDraw.Draw(canvas)
    draw.arc((14, 18, 80, 84), start=200, end=340, fill=(0, 220, 240, 220), width=2)
    draw.arc((22, 26, 72, 76), start=200, end=340, fill=(0, 220, 240, 180), width=1)
    # Tactical blips
    draw.ellipse((28, 28, 34, 34), fill=(255, 215, 0, 255))
    draw.ellipse((62, 32, 68, 38), fill=(220, 30, 30, 255))

    # Center VPA Shield
    shield = create_vpa_tactical_shield(34, 40)
    canvas.paste(shield, (30, 24), shield)

    save_game_ready_icon(canvas, "lf_command_reform_2")


# ==========================================
# 2. VIE_lf_cap_border_urban (Tác chiến biên giới và đô thị)
# ==========================================
def build_cap_border_urban():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Border bunker & fortification
    p_bunker = MD_SAMPLES / "border_conflict_bunker.png"
    if p_bunker.exists():
        bunker = Image.open(p_bunker).convert("RGBA")
        bunker = bunker.resize((80, 68), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(bunker.convert("RGB")).enhance(1.20)
        bunker = Image.merge("RGBA", (*enh.split(), bunker.split()[-1]))
        canvas.paste(bunker, (6, 14), bunker)

    # Vietnam Granite Border Pillar (Cột mốc biên cương)
    draw = ImageDraw.Draw(canvas)
    # Pillar body (granite gray)
    draw.polygon([(64, 14), (74, 8), (84, 14), (84, 62), (64, 62)], fill=(190, 195, 200, 255), outline=(100, 105, 110, 255))
    # Red national emblem plaque on pillar
    draw.rectangle((68, 22, 80, 34), fill=(190, 25, 25, 255), outline=(120, 15, 15, 255))
    draw.polygon([(74, 24), (76, 28), (79, 28), (76.5, 30), (77.5, 33), (74, 31), (70.5, 33), (71.5, 30), (69, 28), (72, 28)], fill=(255, 215, 0, 255))

    # Top VPA roundel
    cockade = create_vpa_cockade(size=26)
    canvas.paste(cockade, (6, 6), cockade)

    save_game_ready_icon(canvas, "lf_cap_border_urban")


# ==========================================
# 3. VIE_lf_cap_area_control (Khống chế địa bàn)
# ==========================================
def build_cap_area_control():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Special forces commando motif
    p_sf = MD_SAMPLES / "special_forces.png"
    if p_sf.exists():
        sf = Image.open(p_sf).convert("RGBA")
        sf = sf.resize((82, 68), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(sf.convert("RGB")).enhance(1.25)
        sf = Image.merge("RGBA", (*enh.split(), sf.split()[-1]))
        canvas.paste(sf, (6, 12), sf)

    # Infrared night targeting grid (Night optics green/cyan)
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 44
    draw.ellipse((cx - 30, cy - 30, cx + 30, cy + 30), outline=(50, 230, 120, 160), width=1)
    draw.line([(cx - 34, cy), (cx - 10, cy)], fill=(50, 230, 120, 200), width=1)
    draw.line([(cx + 10, cy), (cx + 34, cy)], fill=(50, 230, 120, 200), width=1)
    draw.line([(cx, cy - 34), (cx, cy - 10)], fill=(50, 230, 120, 200), width=1)
    draw.line([(cx, cy + 10), (cx, cy + 34)], fill=(50, 230, 120, 200), width=1)

    # Top VPA cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (34, 2), badge)

    save_game_ready_icon(canvas, "lf_cap_area_control")


# ==========================================
# 4. VIE_lf_cap_army_ad (Phòng không lục quân)
# ==========================================
def build_cap_army_ad():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Mobile SAM anti-air launcher
    p_sam = MD_SAMPLES / "SAM.png"
    if p_sam.exists():
        sam = Image.open(p_sam).convert("RGBA")
        sam = sam.resize((80, 68), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(sam.convert("RGB")).enhance(1.25)
        enh = ImageEnhance.Color(enh).enhance(1.15)
        sam = Image.merge("RGBA", (*enh.split(), sam.split()[-1]))
        canvas.paste(sam, (6, 14), sam)

    # Anti-air tracking radar sweep (cyan arc)
    draw = ImageDraw.Draw(canvas)
    draw.arc((12, 6, 82, 76), start=210, end=330, fill=(0, 220, 240, 220), width=2)
    # Launch vector arrow
    draw.line([(66, 32), (80, 14)], fill=(255, 215, 0, 255), width=2)
    draw.polygon([(82, 12), (76, 16), (79, 19)], fill=(255, 215, 0, 255))

    # Top VPA shield
    shield = create_vpa_tactical_shield(30, 36)
    canvas.paste(shield, (8, 6), shield)

    save_game_ready_icon(canvas, "lf_cap_army_ad")


# ==========================================
# 5. VIE_lf_cap_ad_coord (Hiệp đồng PK với PK-KQ)
# ==========================================
def build_cap_ad_coord():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Long-range phased-array radar
    p_radar = MD_SAMPLES / "army_radar.png"
    if p_radar.exists():
        radar = Image.open(p_radar).convert("RGBA")
        radar = radar.resize((82, 70), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(radar.convert("RGB")).enhance(1.20)
        radar = Image.merge("RGBA", (*enh.split(), radar.split()[-1]))
        canvas.paste(radar, (6, 12), radar)

    # Interceptor SAM missile soaring up
    draw = ImageDraw.Draw(canvas)
    # Missile contrail (white/cyan)
    draw.line([(24, 76), (68, 20)], fill=(200, 240, 255, 180), width=3)
    draw.line([(24, 76), (68, 20)], fill=(0, 210, 240, 255), width=1)
    # Missile body
    draw.polygon([(72, 16), (65, 22), (68, 26)], fill=(240, 240, 240, 255), outline=(180, 30, 30, 255))

    # Top VPA cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (8, 4), badge)

    save_game_ready_icon(canvas, "lf_cap_ad_coord")


# ==========================================
# 6. VIE_lf_cap_cyber_ew (Tác chiến mạng và điện tử)
# ==========================================
def build_cap_cyber_ew():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Cyberwarfare motif
    p_cyber = MD_SAMPLES / "army_cyberwar.png"
    if p_cyber.exists():
        cyber = Image.open(p_cyber).convert("RGBA")
        cyber = cyber.resize((82, 72), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(cyber.convert("RGB")).enhance(1.25)
        cyber = Image.merge("RGBA", (*enh.split(), cyber.split()[-1]))
        canvas.paste(cyber, (6, 10), cyber)

    # Electromagnetic pulse waves (cyan neon concentric arcs)
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 44
    draw.arc((cx - 36, cy - 36, cx + 36, cy + 36), start=30, end=150, fill=(0, 240, 255, 220), width=2)
    draw.arc((cx - 26, cy - 26, cx + 26, cy + 26), start=30, end=150, fill=(0, 240, 255, 180), width=1)
    draw.arc((cx - 36, cy - 36, cx + 36, cy + 36), start=210, end=330, fill=(0, 240, 255, 220), width=2)
    draw.arc((cx - 26, cy - 26, cx + 26, cy + 26), start=210, end=330, fill=(0, 240, 255, 180), width=1)

    # Central VPA star shield
    shield = create_vpa_tactical_shield(32, 38)
    canvas.paste(shield, (31, 24), shield)

    save_game_ready_icon(canvas, "lf_cap_cyber_ew")


# ==========================================
# 7. VIE_lf_cap_info_ops (Tác chiến thông tin hiệp đồng)
# ==========================================
def build_cap_info_ops():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Military C4ISR satellite in orbit
    p_sat = MD_SAMPLES / "weaponized_satellites.png"
    if p_sat.exists():
        sat = Image.open(p_sat).convert("RGBA")
        sat = sat.resize((84, 70), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(sat.convert("RGB")).enhance(1.20)
        sat = Image.merge("RGBA", (*enh.split(), sat.split()[-1]))
        canvas.paste(sat, (5, 10), sat)

    # Downlink encrypted tactical data beam (Gold & Cyan lines)
    draw = ImageDraw.Draw(canvas)
    draw.line([(47, 40), (24, 82)], fill=(255, 215, 0, 180), width=2)
    draw.line([(47, 40), (47, 84)], fill=(0, 220, 240, 200), width=2)
    draw.line([(47, 40), (70, 82)], fill=(255, 215, 0, 180), width=2)

    # Ground tactical node blips
    draw.ellipse((21, 80, 27, 86), fill=(0, 220, 240, 255))
    draw.ellipse((44, 82, 50, 88), fill=(255, 215, 0, 255))
    draw.ellipse((67, 80, 73, 86), fill=(0, 220, 240, 255))

    # Top VPA cockade
    badge = create_vpa_cockade(size=26)
    canvas.paste(badge, (34, 2), badge)

    save_game_ready_icon(canvas, "lf_cap_info_ops")


# ==========================================
# 8. VIE_lf_selective_modernization (Hiện đại hóa chọn lọc)
# ==========================================
def build_selective_modernization():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: NVG Night Vision goggles on tactical helmet
    p_nvg = MD_SAMPLES / "army_nightvision.png"
    if p_nvg.exists():
        nvg = Image.open(p_nvg).convert("RGBA")
        nvg = nvg.resize((82, 70), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(nvg.convert("RGB")).enhance(1.25)
        nvg = Image.merge("RGBA", (*enh.split(), nvg.split()[-1]))
        canvas.paste(nvg, (6, 12), nvg)

    # Phosphor green night vision glow circles
    draw = ImageDraw.Draw(canvas)
    draw.ellipse((32, 38, 44, 50), outline=(50, 255, 120, 240), width=2)
    draw.ellipse((50, 38, 62, 50), outline=(50, 255, 120, 240), width=2)

    # Top VPA tactical shield
    shield = create_vpa_tactical_shield(32, 38)
    canvas.paste(shield, (31, 2), shield)

    save_game_ready_icon(canvas, "lf_selective_modernization")


# ==========================================
# 9. VIE_lf_command_reform_3 (Cải cách bộ chỉ huy III)
# ==========================================
def build_command_reform_3():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Command power with 3D holographic war table
    p_cmd = MD_SAMPLES / "Generic_Command_Power.png"
    if p_cmd.exists():
        cmd = Image.open(p_cmd).convert("RGBA")
        cmd = cmd.resize((84, 76), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(cmd.convert("RGB")).enhance(1.25)
        cmd = Image.merge("RGBA", (*enh.split(), cmd.split()[-1]))
        canvas.paste(cmd, (5, 8), cmd)

    # Golden laurels of Supreme Command embracing bottom
    draw = ImageDraw.Draw(canvas)
    draw.arc((12, 20, 82, 84), start=20, end=160, fill=(212, 175, 55, 255), width=3)

    # Strategic AI Tri-Arrows at top
    draw.polygon([(47, 4), (54, 16), (40, 16)], fill=(255, 215, 0, 255), outline=(160, 120, 10, 255))
    draw.polygon([(26, 12), (36, 20), (28, 24)], fill=(0, 220, 240, 255))
    draw.polygon([(68, 12), (58, 20), (66, 24)], fill=(220, 30, 30, 255))

    # Center Grand VPA Shield
    shield = create_vpa_tactical_shield(36, 42)
    canvas.paste(shield, (29, 22), shield)

    save_game_ready_icon(canvas, "lf_command_reform_3")


# ==========================================
# 10. VIE_lf_force_complete (Hoàn thiện lực lượng vũ trang)
# ==========================================
def build_force_complete():
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: Sunburst rays of Victory
    draw = ImageDraw.Draw(canvas)
    cx, cy = 47, 44
    for i in range(16):
        ang = i * math.pi / 8
        x1 = cx + 22 * math.cos(ang)
        y1 = cy + 22 * math.sin(ang)
        x2 = cx + 42 * math.cos(ang)
        y2 = cy + 42 * math.sin(ang)
        draw.line([(x1, y1), (x2, y2)], fill=(255, 215, 0, 140), width=2)

    # Grand golden rice wreath & cogwheel
    draw.ellipse((cx - 36, cy - 36, cx + 36, cy + 36), outline=(212, 175, 55, 240), width=3)
    # Industrial cog teeth at bottom
    for i in range(8):
        ang = math.pi / 4 + i * math.pi / 14
        tx = cx + 37 * math.cos(ang)
        ty = cy + 37 * math.sin(ang)
        draw.rectangle((tx - 2, ty - 2, tx + 2, ty + 2), fill=(212, 175, 55, 255))

    # Large VPA Cockade Medal in center
    cockade = create_vpa_cockade(size=44)
    canvas.paste(cockade, (int(cx - cockade.width / 2), int(cy - cockade.height / 2) - 4), cockade)

    # Crimson Victory Ribbon across bottom
    draw.polygon([(14, 72), (80, 72), (74, 86), (47, 82), (20, 86)], fill=(205, 25, 25, 255), outline=(130, 15, 15, 255))
    draw.line([(18, 75), (76, 75)], fill=(255, 215, 0, 255), width=1)
    draw.line([(22, 82), (72, 82)], fill=(255, 215, 0, 255), width=1)

    save_game_ready_icon(canvas, "lf_force_complete")


if __name__ == "__main__":
    print("Building Batch 5 (10 High-Tech, Cyber & Capstone icons)...")
    build_command_reform_2()
    build_cap_border_urban()
    build_cap_area_control()
    build_cap_army_ad()
    build_cap_ad_coord()
    build_cap_cyber_ew()
    build_cap_info_ops()
    build_selective_modernization()
    build_command_reform_3()
    build_force_complete()
    print("Batch 5 icons built successfully!")
