"""Redesigned Focus Icons for Vietnam Diplomacy (Cluster 2: 9 Focuses)
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
# COMMON UTILITIES
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
# 9 CLUSTER 2 BUILDERS
# =========================================================================

# 13. VIE_asean_integration: La bàn thiên văn ngoại giao, Quốc huy Việt Nam & Bó lúa ASEAN
def build_asean_integration() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(90, 78)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 8), laurel)

    # Celestial Diplomatic Astrolabe Compass & Vietnam National Crest
    comp = Image.new("RGBA", (52, 50), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(comp)

    # Outer Astrolabe Gold Ring with engraved cardinal markings
    cdraw.ellipse([2, 2, 49, 47], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=2)
    cdraw.ellipse([6, 6, 45, 43], fill=(15, 40, 95, 255), outline=(255, 225, 75, 255), width=1)

    # 8-Direction Star Compass Rose
    cx, cy = 25, 24
    for i in range(8):
        ang = i * math.pi / 4 - math.pi / 2
        r_tip = 19 if i % 2 == 0 else 14
        tip_x = cx + r_tip * math.cos(ang)
        tip_y = cy + r_tip * math.sin(ang)
        ang_left = ang + 0.35
        ang_right = ang - 0.35
        w_p = 5.5
        cdraw.polygon([(cx, cy), (tip_x, tip_y), (cx + w_p * math.cos(ang_left), cy + w_p * math.sin(ang_left))], fill=(255, 240, 120, 255))
        cdraw.polygon([(cx, cy), (tip_x, tip_y), (cx + w_p * math.cos(ang_right), cy + w_p * math.sin(ang_right))], fill=(185, 135, 15, 255))

    # Core National Coat of Arms Seal (Quốc huy Việt Nam)
    cdraw.ellipse([15, 14, 35, 34], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=2)
    s_core = create_gold_star(11)
    comp.paste(s_core, (19, 18), s_core)

    canvas.paste(comp, ((TARGET_SIZE[0] - comp.width) // 2, 24), comp)

    # Radiant capstone gold star
    star = create_gold_star_with_glow(24)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "asean_integration")
    return canvas


# 14. VIE_asean_chair: Đĩa gốm men lam 10 nhánh lúa vàng ASEAN & Búa chủ tịch cẩm lai nẹp vàng
def build_asean_chair() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # ASEAN Emblem Medallion on Ceramic Cobalt Disc
    chair = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(chair)

    # Cobalt blue outer rim with gold rim
    cdraw.ellipse([4, 2, 45, 43], fill=(20, 55, 135, 255), outline=(235, 195, 45, 255), width=2)
    # Bright red central circle
    cdraw.ellipse([9, 7, 40, 38], fill=(218, 37, 29, 255), outline=(255, 255, 255, 255), width=1)

    # Official Sheaf of 10 Padi Stalks in gold tied with red string
    for i in range(-4, 5):
        ox = i * 2.2
        cdraw.line([(24 + ox, 14), (24 + ox * 0.7, 34)], fill=(255, 225, 65, 255), width=2)
    # Red binding ribbon around stalks
    cdraw.rectangle([18, 22, 30, 25], fill=(200, 20, 20, 255), outline=(255, 235, 95, 255))

    # Chairman Gavel resting diagonally in 3D perspective
    cdraw.polygon([(8, 14), (20, 6), (24, 14), (12, 22)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255), width=1)
    cdraw.line([(16, 14), (42, 40)], fill=(130, 80, 20, 255), width=4)
    cdraw.line([(16, 14), (42, 40)], fill=(245, 215, 75, 255), width=2)

    canvas.paste(chair, ((TARGET_SIZE[0] - chair.width) // 2, 26), chair)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "asean_chair")
    return canvas


# 15. VIE_code_of_conduct: Tập hiệp ước pháp lý DOC/COC, bồ câu trắng & ngọn hải đăng Trường Sa
def build_code_of_conduct() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Legal Treaty Parchment Scroll & White Peace Dove over Ocean Reefs
    coc = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(coc)

    # Leather & Parchment Treaty Codex in navy and cream
    cdraw.rounded_rectangle([5, 8, 44, 42], radius=4, fill=(248, 244, 225, 255), outline=(190, 145, 30, 255), width=2)
    # Ocean waves at scroll base
    cdraw.chord([7, 26, 42, 40], 0, 180, fill=(25, 95, 175, 255))
    # Treaty clauses lines
    for y in [13, 18, 23]:
        cdraw.line([(9, y), (36, y)], fill=(45, 55, 70, 255), width=2)

    # Peace Dove with spread wings in pure white
    cdraw.polygon([(18, 26), (25, 18), (32, 22), (28, 29), (22, 30)], fill=(255, 255, 255, 255), outline=(215, 175, 45, 255))
    # Green olive branch
    cdraw.line([(28, 21), (34, 18)], fill=(45, 160, 50, 255), width=2)

    # Truong Sa Lighthouse beacon in distance
    cdraw.polygon([(36, 12), (40, 12), (39, 24), (37, 24)], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255))
    cdraw.polygon([(38, 12), (44, 8), (44, 16)], fill=(255, 245, 160, 160))

    canvas.paste(coc, ((TARGET_SIZE[0] - coc.width) // 2, 26), coc)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "code_of_conduct")
    return canvas


# 16. VIE_un_security_council: Hội trường bàn móng ngựa HĐBA LHQ & Biển tên mạ vàng "VIET NAM"
def build_un_security_council() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # UN Security Council Horseshoe Chamber Assembly
    un = Image.new("RGBA", (52, 48), (0, 0, 0, 0))
    udraw = ImageDraw.Draw(un)

    # UN Sky Blue Medallion with Olive Branches
    udraw.ellipse([6, 2, 45, 41], fill=(65, 145, 225, 255), outline=(235, 195, 45, 255), width=2)

    # Horseshoe Council Assembly Table in white leather & gold
    udraw.arc([11, 8, 40, 36], 0, 180, fill=(255, 255, 255, 255), width=5)
    udraw.arc([14, 11, 37, 33], 0, 180, fill=(235, 195, 45, 255), width=2)

    # Member microphones representation
    for ang_deg in [30, 60, 90, 120, 150]:
        ang_rad = ang_deg * math.pi / 180
        mx = 25.5 + 13 * math.cos(ang_rad)
        my = 22 + 13 * math.sin(ang_rad)
        udraw.ellipse([mx - 1, my - 1, mx + 1, my + 1], fill=(30, 30, 30, 255))

    # Prominent Gilded Vietnam Nameplate at Forefront
    udraw.rounded_rectangle([14, 28, 38, 40], radius=3, fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=1)
    s_un = create_gold_star(7)
    un.paste(s_un, (22, 30), s_un)

    canvas.paste(un, ((TARGET_SIZE[0] - un.width) // 2, 26), un)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "un_security_council")
    return canvas


# 17. VIE_multilateral_champion: Địa cầu đa phương viền kinh tuyến vàng, bục diễn đàn & bút ký vàng
def build_multilateral_champion() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(90, 78)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 8), laurel)

    # Multilateral Summit Rostrum & Crystal Azure Globe
    multi = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(multi)

    # Globe in azure blue with golden lat/long grid
    mdraw.ellipse([4, 2, 45, 43], fill=(30, 85, 160, 255), outline=(235, 195, 45, 255), width=2)
    for rad in [14, 26, 36]:
        mdraw.ellipse([25 - rad // 2, 22 - rad // 2, 25 + rad // 2, 22 + rad // 2], outline=(255, 235, 95, 160))

    # International Summit Rostrum Podium with Microphones
    mdraw.polygon([(16, 22), (34, 22), (31, 42), (19, 42)], fill=(235, 195, 45, 255), outline=(130, 90, 15, 255))
    # Red national crest banner on rostrum
    mdraw.rectangle([20, 26, 30, 34], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255))
    s_pod = create_gold_star(6)
    multi.paste(s_pod, (22, 27), s_pod)

    # Golden Fountain Pen signing treaty at right
    mdraw.polygon([(36, 12), (40, 16), (28, 28), (24, 24)], fill=(255, 235, 95, 255), outline=(160, 110, 15, 255))

    canvas.paste(multi, ((TARGET_SIZE[0] - multi.width) // 2, 26), multi)

    star = create_gold_star_with_glow(24)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -2), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "multilateral_champion")
    return canvas


# 18. VIE_apec_host: Cánh buồm APEC 3D đa sắc, Cầu Rồng Đà Nẵng & Thái Bình Dương tỏa ánh hào quang
def build_apec_host() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Dynamic APEC Sails Emblem & Pacific Rim Horizon
    apec = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(apec)

    # Pacific Ocean Disc in turquoise-cyan
    adraw.ellipse([4, 4, 45, 45], fill=(20, 110, 165, 255), outline=(235, 195, 45, 255), width=2)

    # Stylized 3D Multi-colored APEC Sails: Emerald Green, Deep Azure, Scarlet Red
    # Green sail
    adraw.polygon([(10, 36), (20, 12), (24, 36)], fill=(35, 165, 75, 255), outline=(255, 255, 255, 220))
    # Blue sail
    adraw.polygon([(20, 36), (28, 8), (32, 36)], fill=(25, 95, 205, 255), outline=(255, 255, 255, 220))
    # Red sail
    adraw.polygon([(28, 36), (38, 14), (40, 36)], fill=(218, 37, 29, 255), outline=(255, 255, 255, 220))

    # Golden Sunbeam rising over Pacific Rim
    adraw.arc([6, 6, 44, 44], 200, 340, fill=(255, 230, 75, 255), width=2)

    canvas.paste(apec, ((TARGET_SIZE[0] - apec.width) // 2, 26), apec)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "apec_host")
    return canvas


# 19. VIE_mekong_commission: Dải lụa sông Mê Kông ngọc bích, giọt nước sinh thái & vòng 6 nước ven sông
def build_mekong_commission() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # MRC Hydrological River Basin & Ecological Droplet
    mrc = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mrc)

    # Emerald River Basin Disc
    mdraw.ellipse([4, 2, 45, 43], fill=(25, 135, 120, 255), outline=(235, 195, 45, 255), width=2)

    # Meandering Mekong River ribbon flowing through the disc
    pts_river = [(10, 40), (18, 30), (28, 32), (32, 18), (28, 6), (33, 6), (37, 20), (32, 36), (20, 36), (12, 42)]
    mdraw.polygon(pts_river, fill=(80, 225, 245, 255), outline=(255, 255, 255, 240))

    # Golden Ecological Freshwater Droplet in center
    mdraw.ellipse([20, 16, 30, 28], fill=(255, 230, 75, 255), outline=(140, 95, 15, 255), width=1)
    s_drop = create_gold_star(6)
    mrc.paste(s_drop, (22, 18), s_drop)

    canvas.paste(mrc, ((TARGET_SIZE[0] - mrc.width) // 2, 26), mrc)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "mekong_commission")
    return canvas


# 20. VIE_mekong_dams_response: Thân đập thủy điện bê tông xả bọt trắng, tháp cảm biến & bông lúa miền Tây
def build_mekong_dams_response() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    laurel = create_golden_laurel_wreath(88, 76)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 9), laurel)

    # Hydroelectric Dam Spillway Wall & Telemetry Sensor Mast
    dam = Image.new("RGBA", (50, 48), (0, 0, 0, 0))
    ddraw = ImageDraw.Draw(dam)

    # Massive Concrete Dam Wall
    ddraw.polygon([(4, 14), (45, 14), (41, 42), (8, 42)], fill=(155, 160, 170, 255), outline=(70, 75, 85, 255), width=2)
    # Sluice Floodgates with gushing water spray
    for x in [13, 23, 33]:
        ddraw.rectangle([x, 16, x + 5, 34], fill=(25, 85, 150, 255))
        # White foam rushing down
        ddraw.line([(x + 2, 34), (x + 2, 42)], fill=(160, 230, 255, 255), width=2)

    # Telemetry Monitoring Mast on dam crest
    ddraw.polygon([(23, 4), (27, 4), (26, 14), (24, 14)], fill=(235, 195, 45, 255))
    ddraw.arc([18, 0, 32, 10], 180, 360, fill=(255, 230, 80, 255), width=2)

    # Golden Rice Stalk guarding against drought at bottom
    ddraw.arc([6, 36, 44, 46], 0, 180, fill=(255, 222, 35, 255), width=2)

    canvas.paste(dam, ((TARGET_SIZE[0] - dam.width) // 2, 26), dam)

    star = create_gold_star_with_glow(22)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -1), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "mekong_dams_response")
    return canvas


# 21. VIE_bamboo_diplomacy: KIỆT TÁC 3D NGOẠI GIAO CÂY TRE VIỆT NAM (CAPSTONE)
# "Gốc vững, thân chắc, cành uyển chuyển"
def build_bamboo_diplomacy() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Triumphant golden laurel wreath
    laurel = create_golden_laurel_wreath(92, 80)
    canvas.paste(laurel, ((TARGET_SIZE[0] - laurel.width) // 2, 7), laurel)

    # Majestic 3D Golden Bamboo Grove (Lũy Tre Ngà Việt Nam)
    bamboo = Image.new("RGBA", (56, 52), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(bamboo)

    # Fertile Mother Earth Mound with Deep Gilded Roots (GỐC VỮNG)
    bdraw.ellipse([4, 38, 51, 51], fill=(110, 70, 20, 255), outline=(215, 175, 45, 255), width=2)
    for rx in [12, 19, 28, 36, 44]:
        bdraw.line([(rx, 42), (rx + (rx - 28) * 0.45, 50)], fill=(235, 195, 45, 255), width=2)

    # Sturdy Segmented Golden Culms (THÂN CHẮC)
    # Center dominant culm
    cx = 28
    for seg_y in [32, 23, 14, 5]:
        bdraw.rounded_rectangle([cx - 4, seg_y, cx + 4, seg_y + 8], radius=2, fill=(245, 205, 55, 255), outline=(140, 95, 15, 255), width=1)
        # Ring joint node
        bdraw.line([(cx - 5, seg_y + 8), (cx + 5, seg_y + 8)], fill=(255, 240, 120, 255), width=2)

    # Left resilient culm bending dynamically with wind
    for i, seg_y in enumerate([34, 25, 17, 9]):
        ox = -9 - i * 1.8
        bdraw.rounded_rectangle([cx + ox - 3, seg_y, cx + ox + 3, seg_y + 7], radius=2, fill=(195, 210, 50, 255), outline=(110, 120, 15, 255), width=1)
        bdraw.line([(cx + ox - 4, seg_y + 7), (cx + ox + 4, seg_y + 7)], fill=(255, 240, 110, 255), width=2)

    # Right resilient culm
    for i, seg_y in enumerate([34, 25, 17, 9]):
        ox = 9 + i * 1.8
        bdraw.rounded_rectangle([cx + ox - 3, seg_y, cx + ox + 3, seg_y + 7], radius=2, fill=(195, 210, 50, 255), outline=(110, 120, 15, 255), width=1)
        bdraw.line([(cx + ox - 4, seg_y + 7), (cx + ox + 4, seg_y + 7)], fill=(255, 240, 110, 255), width=2)

    # Graceful Cascading Leaves swaying in breeze (CÀNH UYỂN CHUYỂN)
    leaf_polys = [
        # Left foliage
        [(16, 9), (4, 4), (9, 13)],
        [(15, 16), (2, 14), (8, 21)],
        [(12, 24), (2, 25), (8, 30)],
        # Right foliage
        [(39, 9), (51, 4), (46, 13)],
        [(40, 16), (53, 14), (47, 21)],
        [(43, 24), (53, 25), (47, 30)],
        # Top canopy foliage
        [(28, 5), (19, 0), (24, 7)],
        [(28, 5), (37, 0), (32, 7)],
    ]
    for pts in leaf_polys:
        bdraw.polygon(pts, fill=(255, 235, 95, 255), outline=(150, 130, 20, 255))

    # Core Red Emblem with Gold Star on bamboo trunk
    bdraw.ellipse([20, 23, 36, 39], fill=(218, 37, 29, 255), outline=(255, 222, 35, 255), width=2)
    s_bam = create_gold_star(9)
    bamboo.paste(s_bam, (23, 26), s_bam)

    canvas.paste(bamboo, ((TARGET_SIZE[0] - bamboo.width) // 2, 24), bamboo)

    # Radiant Summit 3D Star of Vietnam illuminating the grove
    star = create_gold_star_with_glow(26)
    canvas.paste(star, ((TARGET_SIZE[0] - star.width) // 2, -3), star)

    canvas = apply_ambient_drop_shadow(canvas)
    save_game_ready_icon(canvas, "bamboo_diplomacy")
    return canvas


def main():
    print("=" * 60)
    print("REBUILDING CLUSTER 2: 9 REDESIGNED DIPLOMACY FOCUS ICONS")
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

    print("\nCluster 2 Redesign complete! 9 icons rendered & saved.")


if __name__ == "__main__":
    main()
