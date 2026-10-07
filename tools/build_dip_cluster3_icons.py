"""Redesigned Focus Icons for Vietnam Diplomacy (Cluster 3: 13 Focuses)
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
MD_FLAGS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\flags")
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"

TARGET_SIZE = (93, 91)

# =========================================================================
# COMMON UTILITIES & AUTHENTIC FLAGS
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
        v_left = pts[(i * 2 - 1) % 10]
        v_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, v_left], fill=(255, 248, 125, 170))
        draw.polygon([center, tip, v_right], fill=(185, 135, 10, 180))
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


def render_vietnam_flag(size: tuple = (34, 23), waving: bool = True) -> Image.Image:
    """Render 100% authentic Cờ đỏ sao vàng (Red flag, 5-pointed gold star in center)."""
    w, h = size
    im = Image.new("RGBA", size, (218, 37, 29, 255))
    draw = ImageDraw.Draw(im)
    cx, cy = w / 2, h / 2
    r_outer = h * 0.38
    r_inner = r_outer * 0.382
    pts = []
    for i in range(10):
        ang = i * math.pi / 5 - math.pi / 2
        r = r_outer if i % 2 == 0 else r_inner
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    draw.polygon(pts, fill=(255, 222, 35, 255), outline=(180, 130, 10, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        v_left = pts[(i * 2 - 1) % 10]
        v_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, v_left], fill=(255, 248, 120, 220))
        draw.polygon([center, tip, v_right], fill=(200, 145, 15, 220))

    if waving:
        wave = Image.new("RGBA", size, (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wave)
        for x in range(w):
            val = int(28 * math.sin(x / w * math.pi * 2.8))
            if val > 0:
                wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
            else:
                wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
        im = Image.alpha_composite(im, wave)

    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, w - 1, h - 1], outline=(235, 195, 45, 240), width=1)
    return im


def load_partner_flag(filename: str, size: tuple = (34, 23), waving: bool = True) -> Image.Image:
    p = MD_FLAGS / filename
    if not p.exists():
        im = Image.new("RGBA", size, (180, 180, 180, 255))
    else:
        im = Image.open(p).convert("RGBA").resize(size, Image.Resampling.LANCZOS)

    if waving:
        w, h = size
        wave = Image.new("RGBA", size, (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wave)
        for x in range(w):
            val = int(28 * math.sin(x / w * math.pi * 2.8))
            if val > 0:
                wdraw.line([(x, 0), (x, h)], fill=(255, 255, 255, val))
            else:
                wdraw.line([(x, 0), (x, h)], fill=(0, 0, 0, -val))
        im = Image.alpha_composite(im, wave)

    draw = ImageDraw.Draw(im)
    draw.rectangle([0, 0, size[0] - 1, size[1] - 1], outline=(235, 195, 45, 240), width=1)
    return im


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
            ang = math.pi * 0.55 + t * math.pi * 0.85 if side == -1 else math.pi * 0.45 - t * math.pi * 0.85
            px = cx + rx * math.cos(ang)
            py = cy + ry * math.sin(ang)
            tang_x = -rx * math.sin(ang)
            tang_y = ry * math.cos(ang)
            tang_len = math.hypot(tang_x, tang_y) + 1e-5
            tang_x /= tang_len
            tang_y /= tang_len

            leaf_ang = math.atan2(tang_y, tang_x) + (0.45 if side == -1 else -0.45)
            leaf_len = 8.5
            tip_x = px + leaf_len * math.cos(leaf_ang)
            tip_y = py + leaf_len * math.sin(leaf_ang)
            norm_x = -math.sin(leaf_ang) * 2.1
            norm_y = math.cos(leaf_ang) * 2.1

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


# =========================================================================
# 13 CLUSTER 3 BUILDERS - 100% ACCURATE VIETNAM FLAGS & UNIQUE CENTERPIECES
# =========================================================================

# 22. VIE_us_engagement: Cái bắt tay lịch sử 1995, Cờ đỏ sao vàng & Cờ Mỹ trên cán cờ mạ vàng
def build_us_engagement() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Diplomatic Handshake & Pacific Bridge Monument
    med = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)

    # Blue Pacific Ocean medallion
    mdraw.ellipse([4, 2, 45, 43], fill=(20, 50, 115, 255), outline=(235, 195, 45, 255), width=2)

    # Pacific Reconciliation Bridge Arch in gold
    mdraw.arc([8, 14, 41, 40], 180, 360, fill=(255, 225, 75, 255), width=3)

    # Historic 1995 Handshake Glyph in central medallion
    mdraw.ellipse([12, 14, 37, 39], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=1)
    mdraw.polygon([(18, 26), (23, 21), (27, 25), (32, 22), (30, 29), (24, 31), (19, 28)], fill=(255, 230, 80, 255))

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 26), med)

    # Two Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_usa = load_partner_flag("USA_democratic.tga", size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_usa, (TARGET_SIZE[0] - 6 - f_usa.width, 36), f_usa)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_engagement")
    return canvas


# 23. VIE_us_comprehensive_partnership: Nhà Trắng & Phủ Chủ tịch Hà Nội kết nối dải lụa vàng
def build_us_comprehensive_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(90, 78)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 8), laurel)

    # Bilateral Presidential Partnership Seal
    seal = Image.new("RGBA", (52, 48), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(seal)

    # Outer gold seal disc
    sdraw.ellipse([4, 2, 47, 45], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    sdraw.ellipse([7, 5, 44, 42], fill=(160, 25, 25, 255), outline=(255, 235, 95, 255), width=1)

    # Intertwined Golden Silk Ribbon sash tying Washington & Hanoi
    sdraw.polygon([(12, 16), (26, 22), (12, 28)], fill=(255, 235, 95, 255))
    sdraw.polygon([(40, 16), (26, 22), (40, 28)], fill=(255, 235, 95, 255))
    sdraw.ellipse([20, 16, 32, 28], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255))

    s_star = create_gold_star(9)
    seal.paste(s_star, (21, 18), s_star)

    # Comprehensive partnership laurel wreath within seal
    sdraw.arc([10, 8, 41, 39], 40, 140, fill=(255, 225, 75, 255), width=2)

    canvas.paste(seal, ((TARGET_SIZE[0] - seal.width) // 2, 26), seal)

    star = create_gold_star_with_glow(24)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_comprehensive_partnership")
    return canvas


# 24. VIE_us_embargo_lifted: Ổ khóa cấm vận thép bị xích bẻ gãy tung tóe, tiêm kích siêu âm vút bay
def build_us_embargo_lifted() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Shattered Embargo Padlock & Supersonic Fighter Jet in Golden Relief
    lock_ui = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    ldraw = ImageDraw.Draw(lock_ui)

    # Heavy steel padlock body in gray steel
    ldraw.rounded_rectangle([12, 18, 38, 42], radius=4, fill=(160, 165, 175, 255), outline=(60, 65, 75, 255), width=2)
    # Broken open shackle swinging apart with sparks
    ldraw.arc([16, 2, 34, 22], 180, 360, fill=(235, 195, 45, 255), width=3)
    ldraw.line([(16, 12), (16, 18)], fill=(235, 195, 45, 255), width=3)
    # Sparks breaking out
    ldraw.line([(32, 8), (40, 2)], fill=(255, 225, 60, 255), width=2)
    ldraw.line([(34, 14), (44, 12)], fill=(255, 225, 60, 255), width=2)

    # Modern Supersonic Jet Fighter silhouette breaking free in gold
    ldraw.polygon([(25, 18), (38, 30), (25, 26), (12, 30)], fill=(255, 230, 75, 255), outline=(140, 95, 15, 255))
    s_lock = create_gold_star(7)
    lock_ui.paste(s_lock, (21, 31), s_lock)

    canvas.paste(lock_ui, ((TARGET_SIZE[0] - lock_ui.width) // 2, 26), lock_ui)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_embargo_lifted")
    return canvas


# 25. VIE_us_carrier_visit: Siêu tàu sân bay Nimitz lướt sóng uy nghi giữa Vịnh Đà Nẵng
def build_us_carrier_visit() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # US Supercarrier at Da Nang Harbor & Son Tra Peninsula
    carrier = Image.new("RGBA", (52, 48), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(carrier)

    # Deep blue Da Nang Bay sea oval
    cdraw.ellipse([4, 8, 47, 44], fill=(20, 65, 130, 255), outline=(235, 195, 45, 255), width=2)

    # Son Tra green mountain silhouette in background
    cdraw.polygon([(6, 26), (18, 14), (32, 22), (46, 18), (46, 26)], fill=(35, 95, 70, 220))

    # Supercarrier angled flight deck in naval slate-gray
    cdraw.polygon([(8, 30), (44, 24), (46, 32), (10, 38)], fill=(125, 130, 140, 255), outline=(50, 55, 60, 255), width=2)
    # Island superstructure tower
    cdraw.rectangle([(34, 18), (40, 24)], fill=(170, 175, 185, 255), outline=(50, 55, 60, 255))
    # Runway landing stripe in pure white
    cdraw.line([(10, 33), (44, 27)], fill=(255, 255, 255, 255), width=1)

    # Friendship anchor & golden star crest
    s_car = create_gold_star(8)
    carrier.paste(s_car, (14, 16), s_car)

    canvas.paste(carrier, ((TARGET_SIZE[0] - carrier.width) // 2, 26), carrier)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_carrier_visit")
    return canvas


# 26. VIE_us_tariff_deal: Cán cân thương mại container & Con dấu biểu thuế ưu đãi mạ vàng
def build_us_tariff_deal() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Balance Scale of Trade & Customs Exemption Seal
    tariff = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(tariff)

    # Brass Balance Scale
    tdraw.line([(25, 6), (25, 42)], fill=(235, 195, 45, 255), width=3)
    tdraw.line([(8, 14), (42, 14)], fill=(235, 195, 45, 255), width=2)
    # Scale pans
    tdraw.chord([4, 22, 16, 32], 0, 180, fill=(255, 225, 75, 255), outline=(130, 90, 15, 255))
    tdraw.chord([34, 22, 46, 32], 0, 180, fill=(255, 225, 75, 255), outline=(130, 90, 15, 255))
    # Suspension lines
    tdraw.line([(10, 14), (5, 23)], fill=(185, 135, 15, 255))
    tdraw.line([(10, 14), (15, 23)], fill=(185, 135, 15, 255))
    tdraw.line([(40, 14), (35, 23)], fill=(185, 135, 15, 255))
    tdraw.line([(40, 14), (45, 23)], fill=(185, 135, 15, 255))

    # Customs Wax Seal in red & gold on ledger base
    tdraw.ellipse([19, 28, 31, 40], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=1)
    s_tar = create_gold_star(6)
    tariff.paste(s_tar, (22, 31), s_tar)

    canvas.paste(tariff, ((TARGET_SIZE[0] - tariff.width) // 2, 26), tariff)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "us_tariff_deal")
    return canvas


# 27. VIE_csp_network: Chòm sao 8 Đối tác Chiến lược Toàn diện xoay quanh Ngôi sao Việt Nam
def build_csp_network() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(90, 78)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 8), laurel)

    # Constellation Network of 8 Comprehensive Strategic Partners
    csp = Image.new("RGBA", (52, 50), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(csp)

    cx, cy = 26, 24
    r_orbit = 20

    # Constellation connection filaments in glowing gold
    for i in range(8):
        ang = i * math.pi / 4
        px = cx + r_orbit * math.cos(ang)
        py = cy + r_orbit * math.sin(ang)
        cdraw.line([(cx, cy), (px, py)], fill=(255, 230, 85, 200), width=1)
        cdraw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 245, 140, 255), outline=(180, 130, 10, 255))

    # Center Radiant Vietnam Core Crest
    cdraw.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=2)
    s_csp = create_gold_star(11)
    csp.paste(s_csp, (cx - 5, cy - 5), s_csp)

    canvas.paste(csp, ((TARGET_SIZE[0] - csp.width) // 2, 24), csp)

    star = create_gold_star_with_glow(24)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "csp_network")
    return canvas


# 28. VIE_japan_partnership: Núi Phú Sĩ, Hoa anh đào & Hoa sen, Cầu Nhật Tân, Cờ VN & Cờ Nhật
def build_japan_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Mount Fuji & Sakura Blossom Medallion
    med = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)

    # Medallion base in soft rose-cream
    mdraw.ellipse([4, 2, 45, 43], fill=(255, 245, 248, 255), outline=(235, 195, 45, 255), width=2)

    # Mount Fuji silhouette with snow cap
    mdraw.polygon([(10, 36), (25, 14), (40, 36)], fill=(35, 60, 120, 255))
    mdraw.polygon([(21, 20), (25, 14), (29, 20), (27, 22), (25, 20), (23, 22)], fill=(255, 255, 255, 255))

    # Red Sun disc rising behind Fuji
    mdraw.ellipse([18, 6, 32, 20], fill=(188, 0, 45, 255))

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 26), med)

    # Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_jap = load_partner_flag("JAP.tga", size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_jap, (TARGET_SIZE[0] - 6 - f_jap.width, 36), f_jap)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "japan_partnership")
    return canvas


# 29. VIE_korea_partnership: Tấm wafer vi mạch silicon tinh xảo ánh vàng, Cờ VN & Cờ Hàn Quốc
def build_korea_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # High-Tech Silicon Wafer Semiconductor & Circuitry
    chip = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chip)

    # Silicon wafer circular disc in high-tech midnight indigo
    cdraw.ellipse([4, 2, 45, 43], fill=(15, 30, 55, 255), outline=(235, 195, 45, 255), width=2)

    # Semiconductor circuit traces grid in glowing neon gold
    for y in [12, 18, 24, 30]:
        cdraw.line([(10, y), (39, y)], fill=(255, 230, 80, 200), width=1)
    for x in [15, 21, 28, 34]:
        cdraw.line([(x, 8), (x, 37)], fill=(255, 230, 80, 200), width=1)

    # Central Core Microchip processor
    cdraw.rounded_rectangle([18, 16, 31, 29], radius=2, fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=1)
    s_kr = create_gold_star(7)
    chip.paste(s_kr, (21, 19), s_kr)

    canvas.paste(chip, ((TARGET_SIZE[0] - chip.width) // 2, 26), chip)

    # Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_kor = load_partner_flag("KOR_democratic.tga", size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_kor, (TARGET_SIZE[0] - 6 - f_kor.width, 36), f_kor)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "korea_partnership")
    return canvas


# 30. VIE_india_partnership: Tên lửa BrahMos vươn nòng dũng mãnh, Bánh xe Ashoka, Cờ VN & Cờ Ấn Độ
def build_india_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Ashoka Chakra & BrahMos Defense Missile Launching
    med = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)

    # Indian Tricolor Medallion Disc
    mdraw.ellipse([4, 2, 45, 43], fill=(255, 255, 255, 255), outline=(235, 195, 45, 255), width=2)
    mdraw.chord([4, 2, 45, 43], 180, 360, fill=(255, 140, 40, 255))
    mdraw.chord([4, 2, 45, 43], 0, 180, fill=(35, 140, 45, 255))
    mdraw.rectangle([6, 17, 43, 28], fill=(255, 255, 255, 255))

    # Navy Ashoka Chakra Wheel (24 spokes) in center
    mdraw.ellipse([18, 16, 31, 29], outline=(0, 0, 136, 255), width=1)
    s_in = create_gold_star(6)
    med.paste(s_in, (21, 19), s_in)

    # BrahMos Supersonic Anti-Ship Missile launching diagonally in gold
    mdraw.polygon([(28, 6), (33, 11), (20, 24), (15, 19)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    # Rocket exhaust flame
    mdraw.polygon([(15, 19), (20, 24), (12, 32)], fill=(255, 110, 20, 255))

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 26), med)

    # Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_ind = load_partner_flag("IND_democratic.tga", size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_ind, (TARGET_SIZE[0] - 6 - f_ind.width, 36), f_ind)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "india_partnership")
    return canvas


# 31. VIE_australia_partnership: Máy bay tuần thám biển P-8A, Chòm sao Nam Thập Tự, Cờ VN & Cờ Úc
def build_australia_partnership() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Southern Cross Constellation & P-8A Maritime Patrol Aircraft
    med = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)

    # Deep Navy Blue Ocean & Night Sky Disc
    mdraw.ellipse([4, 2, 45, 43], fill=(10, 35, 90, 255), outline=(235, 195, 45, 255), width=2)

    # Southern Cross 5 Stars
    stars_pos = [(25, 9), (25, 28), (17, 18), (32, 17), (29, 23)]
    for sx, sy in stars_pos:
        mdraw.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 255, 255, 255))

    # P-8A Poseidon Maritime Patrol Plane in flight in gold relief
    mdraw.polygon([(14, 26), (36, 18), (34, 24), (16, 32)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    mdraw.line([(22, 16), (28, 34)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 26), med)

    # Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_ast = load_partner_flag("AST_democratic.tga", size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_ast, (TARGET_SIZE[0] - 6 - f_ast.width, 36), f_ast)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "australia_partnership")
    return canvas


# 32. VIE_france_eu: Khải Hoàn Môn, Vòng 12 sao vàng EU, Hiệp ước EVFTA, Cờ VN & Cờ Pháp
def build_france_eu() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Arc de Triomphe & EU 12-Star Ring Medallion
    med = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(med)

    # EU Navy Azure Disc
    mdraw.ellipse([4, 2, 45, 43], fill=(10, 45, 125, 255), outline=(235, 195, 45, 255), width=2)

    # Circle of 12 Golden EU Stars
    for i in range(12):
        ang = i * math.pi / 6
        sx = 24.5 + 15 * math.cos(ang)
        sy = 22.5 + 15 * math.sin(ang)
        mdraw.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(255, 225, 65, 255))

    # Arc de Triomphe Monument in central gold relief
    mdraw.polygon([(16, 32), (16, 14), (33, 14), (33, 32), (28, 32), (28, 22), (21, 22), (21, 32)],
                  fill=(245, 220, 85, 255), outline=(140, 95, 15, 255), width=1)

    canvas.paste(med, ((TARGET_SIZE[0] - med.width) // 2, 26), med)

    # Authentic Flags
    f_vie = render_vietnam_flag(size=(32, 21), waving=True)
    f_fra = load_partner_flag("FRA_democratic.tga", size=(32, 21), waving=True)

    draw = ImageDraw.Draw(canvas)
    draw.line([(8, 68), (28, 32)], fill=(235, 195, 45, 255), width=2)
    draw.line([(TARGET_SIZE[0] - 8, 68), (TARGET_SIZE[0] - 28, 32)], fill=(235, 195, 45, 255), width=2)

    canvas.paste(f_vie, (6, 36), f_vie)
    canvas.paste(f_fra, (TARGET_SIZE[0] - 6 - f_fra.width, 36), f_fra)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "france_eu")
    return canvas


# 33. VIE_gulf_investment: Tòa tháp tài chính tương lai vùng Vịnh, giàn khoan & dòng vốn petrodollar
def build_gulf_investment() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Gulf Sovereign Wealth Fund & Futuristic Skyline Towers
    gulf = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gulf)

    # Desert sunset golden amber disc
    gdraw.ellipse([4, 2, 45, 43], fill=(130, 80, 20, 255), outline=(235, 195, 45, 255), width=2)

    # Futuristic Burj / Dubai Spire Skyscrapers in gold & glass
    gdraw.polygon([(22, 6), (27, 6), (28, 38), (21, 38)], fill=(255, 240, 140, 255), outline=(150, 105, 20, 255))
    gdraw.polygon([(14, 16), (19, 16), (20, 38), (13, 38)], fill=(235, 200, 75, 255), outline=(140, 95, 15, 255))
    gdraw.polygon([(30, 20), (35, 20), (36, 38), (29, 38)], fill=(235, 200, 75, 255), outline=(140, 95, 15, 255))

    # Offshore Petrochemical Oil Derrick to the right
    gdraw.polygon([(36, 18), (42, 18), (44, 38), (34, 38)], fill=(180, 140, 40, 255))

    # Golden Dinar / Petrodollar Investment Streams flowing to Vietnam
    gdraw.ellipse([18, 30, 32, 44], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=2)
    s_gf = create_gold_star(7)
    gulf.paste(s_gf, (21, 33), s_gf)

    canvas.paste(gulf, ((TARGET_SIZE[0] - gulf.width) // 2, 26), gulf)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "gulf_investment")
    return canvas


# 34. VIE_global_south_ties: Địa cầu Nam Bán Cầu, Tháp viễn thông Viettel 5G phát sóng châu Phi
def build_global_south_ties() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Global South Globe & Viettel Telecom Antenna Tower
    south = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(south)

    # Emerald Earth Globe Medallion
    sdraw.ellipse([4, 2, 45, 43], fill=(25, 115, 75, 255), outline=(235, 195, 45, 255), width=2)

    # African continent golden silhouette relief
    pts_africa = [(16, 12), (32, 14), (34, 22), (28, 34), (22, 38), (18, 26)]
    sdraw.polygon(pts_africa, fill=(60, 150, 95, 255), outline=(255, 230, 80, 200))

    # Viettel Telecom 5G Transmission Lattice Tower in gleaming gold
    sdraw.polygon([(23, 6), (27, 6), (29, 38), (21, 38)], fill=(245, 215, 65, 255), outline=(140, 95, 15, 255))
    for ty in [14, 20, 26, 32]:
        sdraw.line([(22, ty), (28, ty)], fill=(255, 240, 120, 255), width=1)

    # Radiating golden broadcast waves across continents
    sdraw.arc([16, 0, 34, 14], 200, 340, fill=(255, 230, 80, 255), width=2)
    sdraw.arc([12, -4, 38, 18], 200, 340, fill=(255, 230, 80, 200), width=1)

    # Golden Star of Vietnam at base
    sdraw.ellipse([19, 28, 31, 40], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=1)
    s_gs = create_gold_star(6)
    south.paste(s_gs, (22, 31), s_gs)

    canvas.paste(south, ((TARGET_SIZE[0] - south.width) // 2, 26), south)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "global_south_ties")
    return canvas


def main():
    print("=" * 60)
    print("REBUILDING CLUSTER 3: 13 REDESIGNED DIPLOMACY FOCUS ICONS")
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

    print("\nCluster 3 Redesign complete! 13 icons rendered & saved.")


if __name__ == "__main__":
    main()
