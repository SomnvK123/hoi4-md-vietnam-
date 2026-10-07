"""Script to build Focus Icons for Vietnam Diplomacy & Foreign Affairs (Cluster 2: 9 Focuses)
Cluster 2: Trục ASEAN, Đa phương & Biểu tượng Cây tre
13. asean_integration: Đường lối Đối ngoại (Root focus)
14. asean_chair: Năm Chủ tịch ASEAN và thúc đẩy COC
15. code_of_conduct: Bộ Quy tắc Ứng xử ở Biển Đông (COC)
16. un_security_council: Ủy viên không thường trực Hội đồng Bảo an LHQ
17. multilateral_champion: Quốc gia đa phương uy tín
18. apec_host: Đăng cai APEC
19. mekong_commission: Ủy hội sông Mê Kông
20. mekong_dams_response: Đáp lại các đập thượng nguồn
21. bamboo_diplomacy: Bản lĩnh ngoại giao cây tre Việt Nam (Capstone)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, strictly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
"""

import math
import struct
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"

TARGET_SIZE = (93, 91)

# =========================================================================
# COMMON UTILITIES: DDS SAVER, STARS, LAURELS, SHADOWS
# =========================================================================

def save_game_ready_icon(canvas: Image.Image, stem: str):
    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    assert canvas.size == TARGET_SIZE
    assert canvas.mode == "RGBA"

    w, h = TARGET_SIZE
    pixels = canvas.load()
    for x in range(w):
        pixels[x, 0] = (pixels[x, 0][0], pixels[x, 0][1], pixels[x, 0][2], 0)
        pixels[x, h - 1] = (pixels[x, h - 1][0], pixels[x, h - 1][1], pixels[x, h - 1][2], 0)
    for y in range(h):
        pixels[0, y] = (pixels[0, y][0], pixels[0, y][1], pixels[0, y][2], 0)
        pixels[w - 1, y] = (pixels[w - 1, y][0], pixels[w - 1, y][1], pixels[w - 1, y][2], 0)

    png_path = PNG_DIR / f"{stem}.png"
    canvas.save(png_path)

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


def create_golden_laurel_wreath(width: int = 86, height: int = 74) -> Image.Image:
    im = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    cx, cy = width / 2, height / 2 + 6
    rx, ry = width * 0.43, height * 0.45

    c_leaf = (235, 190, 40, 255)
    c_leaf_hl = (255, 235, 115, 255)
    c_shadow = (140, 95, 15, 255)

    num_leaves = 13
    for side in (-1, 1):
        for i in range(num_leaves):
            t = i / (num_leaves - 1)
            ang = math.pi * 0.55 + t * math.pi * 0.85
            if side == 1:
                ang = math.pi * 0.45 - t * math.pi * 0.85

            px = cx + rx * math.cos(ang)
            py = cy + ry * math.sin(ang)

            tang_x = -rx * math.sin(ang)
            tang_y = ry * math.cos(ang)
            tang_len = math.hypot(tang_x, tang_y) + 1e-5
            tang_x /= tang_len
            tang_y /= tang_len

            leaf_ang = math.atan2(tang_y, tang_x) + (0.45 if side == -1 else -0.45)
            leaf_len = 8.5
            leaf_w = 4.2

            tip_x = px + leaf_len * math.cos(leaf_ang)
            tip_y = py + leaf_len * math.sin(leaf_ang)
            norm_x = -math.sin(leaf_ang) * (leaf_w * 0.5)
            norm_y = math.cos(leaf_ang) * (leaf_w * 0.5)

            pts = [
                (px, py),
                (px + leaf_len * 0.5 * math.cos(leaf_ang) + norm_x, py + leaf_len * 0.5 * math.sin(leaf_ang) + norm_y),
                (tip_x, tip_y),
                (px + leaf_len * 0.5 * math.cos(leaf_ang) - norm_x, py + leaf_len * 0.5 * math.sin(leaf_ang) - norm_y),
            ]
            draw.polygon(pts, fill=c_leaf, outline=c_shadow)
            draw.line([(px, py), (tip_x, tip_y)], fill=c_leaf_hl, width=1)

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


def load_md_goal(rel_path: str, target_box: tuple = (76, 68), enhance_color: float = 1.25) -> Image.Image:
    p = MD_GOALS / rel_path
    if not p.exists():
        return Image.new("RGBA", target_box, (0, 0, 0, 0))
    im = Image.open(p).convert("RGBA")
    if enhance_color != 1.0:
        im = ImageEnhance.Color(im).enhance(enhance_color)
    im = ImageEnhance.Contrast(im).enhance(1.15)
    im.thumbnail(target_box, Image.Resampling.LANCZOS)
    return im


# =========================================================================
# 9 CLUSTER 2 ICON BUILDERS
# =========================================================================

# 13. VIE_asean_integration: Đường lối Đối ngoại (Root)
def build_asean_integration() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base ASEAN mutual trade / world globe
    base = load_md_goal("00_organizations/asean_mutual_trade.dds", target_box=(84, 70), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # 4-Direction Diplomatic Golden Compass with Vietnam Crest Core
    compass = Image.new("RGBA", (44, 44), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(compass)
    # Outer gold compass ring
    cdraw.ellipse([2, 2, 41, 41], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    cdraw.ellipse([5, 5, 38, 38], fill=(20, 45, 100, 255), outline=(255, 225, 75, 255), width=1)

    # 4-point star compass rose
    cx, cy = 22, 22
    for tip_x, tip_y in [(cx, 4), (cx, 40), (4, cy), (40, cy)]:
        cdraw.polygon([(cx, cy), (tip_x, tip_y), (cx + (tip_y - cy) * 0.35, cy + (tip_x - cx) * 0.35)], fill=(255, 235, 100, 255))
        cdraw.polygon([(cx, cy), (tip_x, tip_y), (cx - (tip_y - cy) * 0.35, cy - (tip_x - cx) * 0.35)], fill=(185, 135, 15, 255))

    # Central crimson seal of Vietnam
    cdraw.ellipse([14, 14, 30, 30], fill=(215, 25, 25, 255), outline=(255, 230, 75, 255), width=1)
    s_core = create_gold_star(9)
    compass.paste(s_core, (18, 17), s_core)

    canvas.paste(compass, ((TARGET_SIZE[0] - compass.width) // 2, 28), compass)

    # Top gold star
    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "asean_integration")
    return canvas


# 14. VIE_asean_chair: Năm Chủ tịch ASEAN và thúc đẩy COC
def build_asean_chair() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_organizations/asean_mutual_trade.dds", target_box=(82, 68), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # ASEAN Chairman Gavel & Crest
    chair = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chair)
    # ASEAN emblem disk (red circle, yellow padi stalks, blue border)
    cdraw.ellipse([4, 2, 39, 37], fill=(210, 25, 25, 255), outline=(25, 60, 145, 255), width=3)
    # Golden sheaf of 10 padi stalks
    for i in range(-4, 5):
        cdraw.line([(22 + i * 2, 12), (22 + i * 1.5, 30)], fill=(255, 225, 65, 255), width=2)
    # Gavel of chairmanship diagonally resting across
    cdraw.polygon([(6, 12), (18, 6), (22, 14), (10, 20)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    cdraw.line([(14, 13), (38, 35)], fill=(150, 95, 25, 255), width=4)
    cdraw.line([(14, 13), (38, 35)], fill=(245, 215, 75, 255), width=2)

    canvas.paste(chair, ((TARGET_SIZE[0] - chair.width) // 2, 32), chair)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "asean_chair")
    return canvas


# 15. VIE_code_of_conduct: Bộ Quy tắc Ứng xử ở Biển Đông (COC)
def build_code_of_conduct() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_diplomacy/diplomatic_treaty.dds", target_box=(82, 68), enhance_color=1.2)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # DOC/COC Legal Treaty Scroll with Maritime Waves & Peace Dove
    coc = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(coc)
    # Scroll paper
    cdraw.rounded_rectangle([4, 6, 40, 36], radius=3, fill=(245, 240, 220, 255), outline=(190, 145, 30, 255), width=2)
    # Maritime waves across scroll bottom
    cdraw.chord([6, 22, 38, 36], 0, 180, fill=(25, 95, 175, 255))
    # Code of conduct lines
    for y in [10, 14, 18]:
        cdraw.line([(8, y), (36, y)], fill=(40, 45, 55, 255), width=2)
    # White Peace Dove silhouette over waves
    cdraw.polygon([(16, 22), (22, 16), (28, 20), (25, 25), (19, 26)], fill=(255, 255, 255, 255), outline=(215, 175, 45, 255))
    # Olive branch
    cdraw.line([(24, 19), (29, 17)], fill=(60, 160, 60, 255), width=1)

    canvas.paste(coc, ((TARGET_SIZE[0] - coc.width) // 2, 32), coc)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "code_of_conduct")
    return canvas


# 16. VIE_un_security_council: Ủy viên không thường trực Hội đồng Bảo an LHQ
def build_un_security_council() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_organizations/united_nations.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # UN Security Council Horseshoe Table & "VIET NAM" Plate
    un_box = Image.new("RGBA", (46, 38), (0, 0, 0, 0))
    udraw = ImageDraw.Draw(un_box)
    # UN sky blue medallion
    udraw.ellipse([6, 2, 40, 36], fill=(70, 150, 230, 255), outline=(235, 195, 45, 255), width=2)
    # Horseshoe assembly table in navy
    udraw.arc([10, 8, 36, 34], 0, 180, fill=(255, 255, 255, 255), width=4)
    # Vietnam Nameplate at center
    udraw.rounded_rectangle([13, 24, 33, 34], radius=2, fill=(215, 25, 25, 255), outline=(255, 225, 75, 255), width=1)
    s_un = create_gold_star(6)
    un_box.paste(s_un, (20, 26), s_un)

    canvas.paste(un_box, ((TARGET_SIZE[0] - un_box.width) // 2, 34), un_box)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "un_security_council")
    return canvas


# 17. VIE_multilateral_champion: Quốc gia đa phương uy tín
def build_multilateral_champion() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_diplomacy/focus_generic_approach_the_west.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Multilateral Globe with Rostrum and Golden Quill
    multi = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(multi)
    # Globe in deep azure with golden lat/long lines
    mdraw.ellipse([4, 2, 39, 37], fill=(30, 85, 160, 255), outline=(235, 195, 45, 255), width=2)
    for rad in [14, 24, 34]:
        mdraw.ellipse([21 - rad // 2, 19 - rad // 2, 21 + rad // 2, 19 + rad // 2], outline=(255, 235, 95, 160))
    # Multilateral rostrum podium at front
    mdraw.polygon([(14, 20), (28, 20), (26, 36), (16, 36)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    mdraw.rectangle([17, 24, 25, 30], fill=(210, 25, 25, 255))
    s_pod = create_gold_star(5)
    multi.paste(s_pod, (18, 25), s_pod)

    canvas.paste(multi, ((TARGET_SIZE[0] - multi.width) // 2, 32), multi)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "multilateral_champion")
    return canvas


# 18. VIE_apec_host: Đăng cai APEC
def build_apec_host() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/ExpandTrade.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # APEC Pacific Rim Summit Emblem (Stylized Sails & Globe)
    apec = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(apec)
    # Pacific Ocean disk in aquamarine
    adraw.ellipse([4, 4, 39, 39], fill=(20, 110, 160, 255), outline=(235, 195, 45, 255), width=2)
    # Stylized multi-colored APEC sails: Green, Blue, Red
    adraw.polygon([(10, 32), (18, 12), (22, 32)], fill=(35, 160, 65, 255), outline=(255, 255, 255, 200))
    adraw.polygon([(18, 32), (24, 8), (28, 32)], fill=(30, 95, 195, 255), outline=(255, 255, 255, 200))
    adraw.polygon([(24, 32), (32, 14), (34, 32)], fill=(215, 35, 35, 255), outline=(255, 255, 255, 200))
    # Sunbeam over Pacific
    adraw.arc([6, 6, 38, 38], 200, 340, fill=(255, 230, 75, 255), width=2)

    canvas.paste(apec, ((TARGET_SIZE[0] - apec.width) // 2, 32), apec)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "apec_host")
    return canvas


# 19. VIE_mekong_commission: Ủy hội sông Mê Kông (MRC)
def build_mekong_commission() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_economy/economic_water_supply.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Mekong River Commission (MRC) Hydrological Emblem
    mrc = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mrc)
    # Emerald river basin disk
    mdraw.ellipse([4, 2, 39, 37], fill=(25, 130, 115, 255), outline=(235, 195, 45, 255), width=2)
    # Meandering Mekong river wave in bright aqua
    pts_river = [(10, 34), (16, 26), (24, 28), (28, 16), (26, 6), (30, 6), (32, 18), (28, 32), (18, 32), (12, 36)]
    mdraw.polygon(pts_river, fill=(80, 220, 240, 255), outline=(255, 255, 255, 220))
    # Golden water droplet
    mdraw.ellipse([18, 14, 26, 24], fill=(255, 230, 75, 255), outline=(140, 95, 15, 255))

    canvas.paste(mrc, ((TARGET_SIZE[0] - mrc.width) // 2, 32), mrc)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "mekong_commission")
    return canvas


# 20. VIE_mekong_dams_response: Đáp lại các đập thượng nguồn
def build_mekong_dams_response() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_energy_resources/water_dam.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Mega-dam barrier & telemetry monitoring radar gauge
    dam = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    ddraw = ImageDraw.Draw(dam)
    # Dam concrete spillway in industrial steel-gray
    ddraw.polygon([(4, 12), (39, 12), (35, 36), (8, 36)], fill=(150, 155, 165, 255), outline=(70, 75, 80, 255), width=2)
    # Dam floodgate slots
    for x in [12, 20, 28]:
        ddraw.rectangle([x, 14, x + 4, 30], fill=(25, 85, 150, 255))
        # Gushing water spray
        ddraw.line([(x + 2, 30), (x + 2, 36)], fill=(120, 210, 255, 255), width=2)
    # Sensor telemetry tower on dam crown
    ddraw.polygon([(20, 4), (24, 4), (23, 12), (21, 12)], fill=(235, 195, 45, 255))
    ddraw.arc([16, 0, 28, 8], 180, 360, fill=(255, 230, 80, 255), width=2)

    canvas.paste(dam, ((TARGET_SIZE[0] - dam.width) // 2, 32), dam)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "mekong_dams_response")
    return canvas


# 21. VIE_bamboo_diplomacy: Bản lĩnh ngoại giao cây tre Việt Nam (Capstone)
def build_bamboo_diplomacy() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base grand financial agreement / diplomatic halo
    base = load_md_goal("00_diplomacy/focus_generic_financial_agreement.dds", target_box=(86, 72), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 8), base)

    # Triumphant full golden laurel wreath
    laurel = create_golden_laurel_wreath(90, 78)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 8), laurel)

    # Magnificent 3D Golden Bamboo Grove (Lũy Tre Việt Nam)
    # Concept: "Gốc vững, thân chắc, cành uyển chuyển"
    bamboo = Image.new("RGBA", (50, 46), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bamboo)

    # Earth mound with deep roots (Gốc vững)
    bdraw.ellipse([4, 34, 45, 45], fill=(120, 80, 25, 255), outline=(215, 175, 45, 255), width=1)
    # Deep golden root lines
    for rx in [12, 18, 25, 32, 38]:
        bdraw.line([(rx, 38), (rx + (rx - 25) * 0.4, 44)], fill=(235, 195, 45, 255), width=2)

    # 3 Sturdy Bamboo Culms (Thân chắc) in golden-emerald bamboo shades
    # Center culm
    cx = 25
    for seg_y in [30, 22, 14, 6]:
        bdraw.rounded_rectangle([cx - 4, seg_y, cx + 4, seg_y + 7], radius=2, fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
        bdraw.line([(cx - 5, seg_y + 7), (cx + 5, seg_y + 7)], fill=(255, 235, 95, 255), width=2)

    # Left bending culm
    for i, seg_y in enumerate([32, 24, 17, 10]):
        ox = -8 - i * 1.5
        bdraw.rounded_rectangle([cx + ox - 3, seg_y, cx + ox + 3, seg_y + 6], radius=2, fill=(180, 195, 45, 255), outline=(100, 110, 15, 255), width=1)

    # Right bending culm
    for i, seg_y in enumerate([32, 24, 17, 10]):
        ox = 8 + i * 1.5
        bdraw.rounded_rectangle([cx + ox - 3, seg_y, cx + ox + 3, seg_y + 6], radius=2, fill=(180, 195, 45, 255), outline=(100, 110, 15, 255), width=1)

    # Graceful bamboo leaves swaying in wind (Cành uyển chuyển)
    leaf_pts = [
        # Left cluster
        [(15, 10), (6, 5), (10, 12)],
        [(14, 16), (4, 15), (11, 20)],
        # Right cluster
        [(35, 10), (44, 5), (40, 12)],
        [(36, 16), (46, 15), (39, 20)],
        # Top cluster
        [(25, 6), (19, 0), (22, 8)],
        [(25, 6), (31, 0), (28, 8)],
    ]
    for pts in leaf_pts:
        bdraw.polygon(pts, fill=(255, 235, 95, 255), outline=(140, 120, 20, 255))

    # Center golden seal of Vietnam on culm base
    bdraw.ellipse([18, 22, 32, 36], fill=(215, 25, 25, 255), outline=(255, 230, 75, 255), width=1)
    s_bam = create_gold_star(8)
    bamboo.paste(s_bam, (21, 25), s_bam)

    canvas.paste(bamboo, ((TARGET_SIZE[0] - bamboo.width) // 2, 26), bamboo)

    # Radiant summit 3D Gold Star
    star = create_gold_star_with_glow(24)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "bamboo_diplomacy")
    return canvas


def main():
    print("=" * 60)
    print("BUILDING CLUSTER 2: 9 DIPLOMACY FOCUS ICONS")
    print("=" * 60)

    builders = [
        ("asean_integration", build_asean_integration),
        ("asean_chair", build_asean_chair),
        ("code_of_conduct", build_code_of_conduct),
        ("un_security_council", build_un_security_council),
        ("multilateral_champion", build_multilateral_champion),
        ("apec_host", build_apec_host),
        ("mekong_commission", build_mekong_commission),
        ("mekong_dams_response", build_mekong_dams_response),
        ("bamboo_diplomacy", build_bamboo_diplomacy),
    ]

    for stem, fn in builders:
        fn()

    print("\nCluster 2 complete! 9 icons rendered & saved.")


if __name__ == "__main__":
    main()
