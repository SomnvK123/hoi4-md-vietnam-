"""Script to build Focus Icons for Vietnam Diplomacy & Foreign Affairs (Cluster 3: 13 Focuses)
Cluster 3: Đối tác Chiến lược Lớn & Toàn cầu
22. us_engagement: Bình thường hóa quan hệ với Hoa Kỳ
23. us_comprehensive_partnership: Đối tác toàn diện với Hoa Kỳ
24. us_embargo_lifted: Dỡ bỏ cấm vận vũ khí của Mỹ
25. us_carrier_visit: Tàu sân bay Mỹ ở Đà Nẵng
26. us_tariff_deal: Khung thuế quan với Mỹ
27. csp_network: Các đối tác chiến lược toàn diện
28. japan_partnership: Quan hệ đối tác với Nhật Bản
29. korea_partnership: Quan hệ đối tác với Hàn Quốc
30. india_partnership: Quan hệ đối tác với Ấn Độ
31. australia_partnership: Quan hệ đối tác với Úc
32. france_eu: Pháp và Liên minh châu Âu
33. gulf_investment: Vốn từ vùng Vịnh
34. global_south_ties: Châu Phi và châu Mỹ Latinh

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
MD_FLAGS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\flags")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"

TARGET_SIZE = (93, 91)

# =========================================================================
# COMMON UTILITIES: DDS SAVER, STARS, LAURELS, FLAGS, SHADOWS
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


def create_waving_flag(flag_name: str, size: tuple = (34, 22), border_gold: bool = True) -> Image.Image:
    flag_path = MD_FLAGS / flag_name
    if not flag_path.exists():
        im = Image.new("RGBA", size, (210, 25, 25, 255))
    else:
        im = Image.open(flag_path).convert("RGBA")
        im = im.resize(size, Image.Resampling.LANCZOS)

    w, h = size
    wave = Image.new("RGBA", size, (0, 0, 0, 0))
    wdraw = ImageDraw.Draw(wave)
    for x in range(w):
        val = int(35 * math.sin(x / w * math.pi * 2.8))
        if val > 0:
            wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
        else:
            wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
    im = Image.alpha_composite(im, wave)

    if border_gold:
        bdraw = ImageDraw.Draw(im)
        bdraw.rectangle([0, 0, w - 1, h - 1], outline=(220, 180, 45, 240), width=1)

    return im


# =========================================================================
# 13 CLUSTER 3 ICON BUILDERS
# =========================================================================

# 22. VIE_us_engagement: Bình thường hóa quan hệ với Hoa Kỳ
def build_us_engagement() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_america.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and USA
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_usa = create_waving_flag("USA_democratic.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_usa_rot = f_usa.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_usa_rot, (TARGET_SIZE[0] - 11 - f_usa_rot.width, 26), f_usa_rot)

    # 1995 Normalization Golden Handshake Medallion
    med = Image.new("RGBA", (36, 30), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 33, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([5, 4, 30, 26], fill=(20, 45, 110, 255), outline=(255, 235, 95, 255), width=1)
    mdraw.polygon([(11, 15), (16, 11), (20, 15), (25, 12), (23, 19), (17, 21), (12, 18)], fill=(255, 230, 80, 255))
    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 46), med)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_engagement")
    return canvas


# 23. VIE_us_comprehensive_partnership: Đối tác toàn diện với Hoa Kỳ
def build_us_comprehensive_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_america.dds", target_box=(82, 68), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Bilateral diplomatic seal with White House & Presidential Palace golden ribbon
    seal = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(seal)
    sdraw.ellipse([3, 2, 40, 38], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    sdraw.ellipse([6, 5, 37, 35], fill=(185, 25, 25, 255), outline=(255, 235, 95, 255), width=1)
    # Diplomatic ribbon bow tying the two nations
    sdraw.polygon([(12, 15), (22, 20), (12, 25)], fill=(255, 235, 95, 255))
    sdraw.polygon([(32, 15), (22, 20), (32, 25)], fill=(255, 235, 95, 255))
    s_core = create_gold_star(10)
    seal.paste(s_core, (17, 15), s_core)

    canvas.paste(seal, ((TARGET_SIZE[0] - seal.width) // 2, 32), seal)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_comprehensive_partnership")
    return canvas


# 24. VIE_us_embargo_lifted: Dỡ bỏ cấm vận vũ khí của Mỹ
def build_us_embargo_lifted() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/embargo.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Broken Padlock & Modern Defense Jet silhouette emerging
    lock_ui = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    ldraw = ImageDraw.Draw(lock_ui)
    # Broken steel padlock body
    ldraw.rounded_rectangle([10, 16, 34, 38], radius=3, fill=(180, 185, 195, 255), outline=(70, 75, 85, 255), width=2)
    # Unlocked open shackle swinging open
    ldraw.arc([14, 2, 30, 20], 180, 360, fill=(235, 195, 45, 255), width=3)
    ldraw.line([(14, 11), (14, 16)], fill=(235, 195, 45, 255), width=3)
    # Jet fighter silhouette breaking free in gold
    ldraw.polygon([(22, 18), (32, 28), (22, 25), (12, 28)], fill=(255, 230, 75, 255), outline=(130, 90, 15, 255))
    s_lock = create_gold_star(6)
    lock_ui.paste(s_lock, (19, 29), s_lock)

    canvas.paste(lock_ui, ((TARGET_SIZE[0] - lock_ui.width) // 2, 32), lock_ui)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_embargo_lifted")
    return canvas


# 25. VIE_us_carrier_visit: Tàu sân bay Mỹ ở Đà Nẵng
def build_us_carrier_visit() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("united_states/350_ship_navy.dds", target_box=(82, 68), enhance_color=1.3)
    if base.size == (0, 0) or base.width == 0:
        base = load_md_goal("00_trade/trade_with_america.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # US Supercarrier at Da Nang Bay with Son Tra mountain backdrop
    carrier = Image.new("RGBA", (46, 38), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(carrier)
    # Sea bay oval
    cdraw.ellipse([2, 10, 43, 36], fill=(25, 75, 140, 255), outline=(215, 175, 45, 255), width=1)
    # Supercarrier angled flight deck
    cdraw.polygon([(6, 26), (38, 22), (42, 28), (10, 32)], fill=(120, 125, 135, 255), outline=(60, 65, 70, 255), width=2)
    # Island superstructure tower
    cdraw.rectangle([30, 18, 36, 23], fill=(160, 165, 175, 255), outline=(60, 65, 70, 255))
    # Runway landing stripe in white
    cdraw.line([(8, 28), (38, 24)], fill=(255, 255, 255, 255), width=1)
    # Red star friendship anchor symbol
    s_car = create_gold_star(6)
    carrier.paste(s_car, (12, 16), s_car)

    canvas.paste(carrier, ((TARGET_SIZE[0] - carrier.width) // 2, 34), carrier)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_carrier_visit")
    return canvas


# 26. VIE_us_tariff_deal: Khung thuế quan với Mỹ
def build_us_tariff_deal() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_america.dds", target_box=(82, 68), enhance_color=1.25)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Trade Scale Balancing Cargo & Tariff Exemption Ledger
    tariff = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(tariff)
    # Balance scale in brass gold
    tdraw.line([(22, 6), (22, 34)], fill=(235, 195, 45, 255), width=3)
    tdraw.line([(8, 12), (36, 12)], fill=(235, 195, 45, 255), width=2)
    # Scale pans
    tdraw.chord([4, 18, 14, 26], 0, 180, fill=(255, 225, 75, 255), outline=(130, 90, 15, 255))
    tdraw.chord([30, 18, 40, 26], 0, 180, fill=(255, 225, 75, 255), outline=(130, 90, 15, 255))
    # Suspension strings
    tdraw.line([(9, 12), (5, 19)], fill=(185, 135, 15, 255))
    tdraw.line([(9, 12), (13, 19)], fill=(185, 135, 15, 255))
    tdraw.line([(35, 12), (31, 19)], fill=(185, 135, 15, 255))
    tdraw.line([(35, 12), (39, 19)], fill=(185, 135, 15, 255))
    # Red wax customs clearance seal
    tdraw.ellipse([17, 24, 27, 34], fill=(215, 25, 25, 255), outline=(255, 225, 75, 255), width=1)
    s_tar = create_gold_star(5)
    tariff.paste(s_tar, (19, 26), s_tar)

    canvas.paste(tariff, ((TARGET_SIZE[0] - tariff.width) // 2, 32), tariff)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_tariff_deal")
    return canvas


# 27. VIE_csp_network: Các đối tác chiến lược toàn diện
def build_csp_network() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_diplomacy/focus_generic_approach_the_west.dds", target_box=(84, 70), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 9), base)

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Constellation Network of 8 Comprehensive Strategic Partners around Vietnam Core
    csp = Image.new("RGBA", (48, 44), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(csp)

    cx, cy = 24, 22
    r_orbit = 18
    # Connecting constellation lines
    for i in range(8):
        ang = i * math.pi / 4
        px = cx + r_orbit * math.cos(ang)
        py = cy + r_orbit * math.sin(ang)
        cdraw.line([(cx, cy), (px, py)], fill=(255, 230, 85, 180), width=1)
        cdraw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(255, 245, 135, 255), outline=(180, 130, 10, 255))

    # Center Vietnam Core Seal
    cdraw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(215, 25, 25, 255), outline=(255, 225, 75, 255), width=2)
    s_csp = create_gold_star(10)
    csp.paste(s_csp, (cx - 5, cy - 5), s_csp)

    canvas.paste(csp, ((TARGET_SIZE[0] - csp.width) // 2, 28), csp)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "csp_network")
    return canvas


# 28. VIE_japan_partnership: Quan hệ đối tác với Nhật Bản
def build_japan_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_japan.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and Japan
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_jap = create_waving_flag("JAP.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_jap_rot = f_jap.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_jap_rot, (TARGET_SIZE[0] - 11 - f_jap_rot.width, 26), f_jap_rot)

    # Sakura & Lotus friendship crest
    crest = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(crest)
    cdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    cdraw.ellipse([5, 4, 28, 26], fill=(255, 240, 245, 255), outline=(215, 60, 90, 255), width=1)
    # Cherry blossom petal motif in rose-gold
    cdraw.ellipse([11, 8, 22, 19], fill=(215, 25, 25, 255))
    s_jp = create_gold_star(7)
    crest.paste(s_jp, (14, 11), s_jp)

    canvas.paste(crest, ((TARGET_SIZE[0] - crest.width) // 2, 46), crest)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "japan_partnership")
    return canvas


# 29. VIE_korea_partnership: Quan hệ đối tác với Hàn Quốc
def build_korea_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/ExpandTrade.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and South Korea
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_kor = create_waving_flag("KOR_democratic.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_kor_rot = f_kor.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_kor_rot, (TARGET_SIZE[0] - 11 - f_kor_rot.width, 26), f_kor_rot)

    # High-Tech Microchip & Taegeuk Medallion
    chip = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chip)
    cdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    cdraw.ellipse([5, 4, 28, 26], fill=(20, 35, 60, 255), outline=(255, 235, 95, 255), width=1)
    # Golden semiconductor grid
    cdraw.rectangle([10, 9, 23, 21], fill=(215, 175, 45, 255), outline=(255, 235, 95, 255))
    s_kr = create_gold_star(6)
    chip.paste(s_kr, (14, 12), s_kr)

    canvas.paste(chip, ((TARGET_SIZE[0] - chip.width) // 2, 46), chip)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "korea_partnership")
    return canvas


# 30. VIE_india_partnership: Quan hệ đối tác với Ấn Độ
def build_india_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_india.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and India
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_ind = create_waving_flag("IND_democratic.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_ind_rot = f_ind.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_ind_rot, (TARGET_SIZE[0] - 11 - f_ind_rot.width, 26), f_ind_rot)

    # Ashoka Chakra & BrahMos Defense Medallion
    med = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([5, 4, 28, 26], fill=(255, 130, 30, 255), outline=(255, 235, 95, 255), width=1)
    # Ashoka Chakra 8-spoke wheel in navy
    mdraw.ellipse([11, 9, 22, 20], fill=(255, 255, 255, 255), outline=(20, 45, 120, 255), width=1)
    s_in = create_gold_star(6)
    med.paste(s_in, (14, 12), s_in)

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 46), med)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "india_partnership")
    return canvas


# 31. VIE_australia_partnership: Quan hệ đối tác với Úc
def build_australia_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_australia.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and Australia
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_ast = create_waving_flag("AST_democratic.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_ast_rot = f_ast.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_ast_rot, (TARGET_SIZE[0] - 11 - f_ast_rot.width, 26), f_ast_rot)

    # Southern Cross & Maritime Security Medallion
    med = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([5, 4, 28, 26], fill=(15, 40, 95, 255), outline=(255, 235, 95, 255), width=1)
    s_au = create_gold_star(7)
    med.paste(s_au, (14, 11), s_au)

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 46), med)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "australia_partnership")
    return canvas


# 32. VIE_france_eu: Pháp và Liên minh châu Âu
def build_france_eu() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_trade/trade_with_europe.dds", target_box=(82, 68), enhance_color=1.3)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Crossed flags: Vietnam and France
    f_vie = create_waving_flag("VIE_communism.tga", size=(34, 23))
    f_fra = create_waving_flag("FRA_democratic.tga", size=(34, 23))

    f_vie_rot = f_vie.rotate(14, resample=Image.Resampling.BICUBIC, expand=True)
    f_fra_rot = f_fra.rotate(-14, resample=Image.Resampling.BICUBIC, expand=True)

    canvas.paste(f_vie_rot, (11, 26), f_vie_rot)
    canvas.paste(f_fra_rot, (TARGET_SIZE[0] - 11 - f_fra_rot.width, 26), f_fra_rot)

    # EU 12-Star Ring Medallion & EVFTA Scroll
    med = Image.new("RGBA", (34, 30), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)
    mdraw.ellipse([2, 1, 31, 29], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    mdraw.ellipse([5, 4, 28, 26], fill=(10, 45, 125, 255), outline=(255, 235, 95, 255), width=1)
    # Circle of golden EU stars
    for i in range(8):
        ang = i * math.pi / 4
        sx = 16 + 7 * math.cos(ang)
        sy = 15 + 7 * math.sin(ang)
        mdraw.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 230, 75, 255))
    s_eu = create_gold_star(6)
    med.paste(s_eu, (14, 12), s_eu)

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 46), med)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "france_eu")
    return canvas


# 33. VIE_gulf_investment: Vốn từ vùng Vịnh
def build_gulf_investment() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_organizations/gcc.dds", target_box=(82, 68), enhance_color=1.35)
    if base.size == (0, 0) or base.width == 0:
        base = load_md_goal("00_economy/focus_generic_financial_agreement.dds", target_box=(82, 68), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Sovereign Wealth Fund Vault Chest & Petrochemical Capital Streams
    gulf = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gulf)
    # Gold treasure vault chest
    gdraw.rounded_rectangle([6, 12, 38, 36], radius=4, fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    # Chest arched lid
    gdraw.polygon([(4, 16), (22, 6), (40, 16)], fill=(255, 225, 75, 255), outline=(130, 90, 15, 255), width=2)
    # Keyhole escutcheon
    gdraw.ellipse([19, 20, 25, 26], fill=(40, 25, 10, 255))
    gdraw.polygon([(20, 24), (24, 24), (23, 29), (21, 29)], fill=(40, 25, 10, 255))
    # Red star of Vietnam investment seal
    gdraw.ellipse([17, 10, 27, 20], fill=(215, 25, 25, 255), outline=(255, 225, 75, 255), width=1)
    s_gf = create_gold_star(6)
    gulf.paste(s_gf, (19, 12), s_gf)

    canvas.paste(gulf, ((TARGET_SIZE[0] - gulf.width) // 2, 32), gulf)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "gulf_investment")
    return canvas


# 34. VIE_global_south_ties: Châu Phi và châu Mỹ Latinh
def build_global_south_ties() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    base = load_md_goal("00_organizations/nam.dds", target_box=(82, 68), enhance_color=1.35)
    if base.size == (0, 0) or base.width == 0:
        base = load_md_goal("00_organizations/african_investment.dds", target_box=(82, 68), enhance_color=1.35)
    canvas.paste(base, ((TARGET_SIZE[0] - base.width) // 2, 10), base)

    laurel = create_golden_laurel_wreath(86, 74)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 10), laurel)

    # Global South Solidarity Map & Viettel Telecom Antenna Tower
    south = Image.new("RGBA", (44, 40), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(south)
    # Globe medallion in earth-emerald
    sdraw.ellipse([4, 2, 39, 37], fill=(30, 115, 75, 255), outline=(235, 195, 45, 255), width=2)
    # Telecom antenna lattice tower in gold
    sdraw.polygon([(20, 6), (24, 6), (26, 34), (18, 34)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    for ty in [12, 18, 24, 30]:
        sdraw.line([(19, ty), (25, ty)], fill=(255, 235, 95, 255), width=1)
    # Radiating broadcast signal arcs
    sdraw.arc([14, 0, 30, 12], 200, 340, fill=(255, 230, 80, 255), width=2)
    sdraw.arc([10, -4, 34, 16], 200, 340, fill=(255, 230, 80, 200), width=1)
    # Core star of Vietnam
    sdraw.ellipse([17, 24, 27, 34], fill=(215, 25, 25, 255), outline=(255, 225, 75, 255), width=1)
    s_gs = create_gold_star(6)
    south.paste(s_gs, (19, 26), s_gs)

    canvas.paste(south, ((TARGET_SIZE[0] - south.width) // 2, 32), south)

    star = create_gold_star_with_glow(20)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, 0), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "global_south_ties")
    return canvas


def main():
    print("=" * 60)
    print("BUILDING CLUSTER 3: 13 DIPLOMACY FOCUS ICONS")
    print("=" * 60)

    builders = [
        ("us_engagement", build_us_engagement),
        ("us_comprehensive_partnership", build_us_comprehensive_partnership),
        ("us_embargo_lifted", build_us_embargo_lifted),
        ("us_carrier_visit", build_us_carrier_visit),
        ("us_tariff_deal", build_us_tariff_deal),
        ("csp_network", build_csp_network),
        ("japan_partnership", build_japan_partnership),
        ("korea_partnership", build_korea_partnership),
        ("india_partnership", build_india_partnership),
        ("australia_partnership", build_australia_partnership),
        ("france_eu", build_france_eu),
        ("gulf_investment", build_gulf_investment),
        ("global_south_ties", build_global_south_ties),
    ]

    for stem, fn in builders:
        fn()

    print("\nCluster 3 complete! 13 icons rendered & saved.")


if __name__ == "__main__":
    main()
