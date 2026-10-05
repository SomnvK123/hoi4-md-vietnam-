"""Script to build Focus Icons for Vietnam Internal Security (Nhánh An ninh Nội địa - 5 focuses) in Millennium Dawn.

5 Focuses:
1. sec_public_order: Trật tự Công cộng (Police shield, VPA star, crossed tactical batons, red/blue flashing beacon, urban grid)
2. sec_border_control: Siết Biên giới & Kiểm soát Di chuyển (Vietnam Border Milestone with national crest, striped barrier gate, watchtower searchlight)
3. sec_surveillance_network: Mạng lưới Giám sát Đại chúng (AI CCTV dome camera, biometric facial recognition brackets, mesh network nodes)
4. sec_cyber_sovereignty: Chủ quyền Mạng (Glowing cyber shield with VPA star, digital firewall, circuit traces, national cryptographic lock)
5. sec_state_data_center: Trung tâm Dữ liệu Quốc gia (Mainframe server racks, national smart chip card CCCD, central AI processor, database cylinders)

Outputs:
- gfx/interface/goals/<stem>.dds (32-bit BGRA uncompressed DDS, 93x91, exactly 33,980 bytes)
- assets/focus_icons/png/<stem>.png (32-bit RGBA PNG, 93x91)
- Registers spriteTypes in interface/VIE_md_focus_icons.gfx
- Updates common/national_focus/VIE_md_focus.txt
"""

import os
import re
import sys
import math
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps

if sys.stdout:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
GFX_FILE = ROOT / "interface" / "VIE_md_focus_icons.gfx"
FOCUS_FILE = ROOT / "common" / "national_focus" / "VIE_md_focus.txt"

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
    print(f"Saved: {stem} -> PNG & DDS (33,980 bytes)")


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

    draw.polygon(pts, fill=(255, 218, 20, 255), outline=(160, 120, 15, 255))
    for i in range(5):
        tip = pts[i * 2]
        center = (cx, cy)
        valley_left = pts[(i * 2 - 1) % 10]
        draw.polygon([center, tip, valley_left], fill=(255, 245, 120, 140))
        valley_right = pts[(i * 2 + 1) % 10]
        draw.polygon([center, tip, valley_right], fill=(190, 135, 10, 150))
    return im


def create_gold_laurel_wreath(w: int, h: int) -> Image.Image:
    """Generate golden laurel branches curving upwards."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    cx = w / 2

    leaf_count = 9
    for side in (-1, 1):
        for i in range(leaf_count):
            t = (i + 1) / (leaf_count + 1)
            ang = math.pi / 2 + side * (t * 0.95 * math.pi / 2 + 0.1)
            rx = (w / 2 - 8)
            ry = (h / 2 - 6)
            lx = cx + rx * math.cos(ang)
            ly = h - 10 - ry * math.sin(ang)

            leaf_len = 8 - t * 2.5
            leaf_ang = ang + side * 0.4
            p1 = (lx, ly)
            p2 = (lx + leaf_len * math.cos(leaf_ang), ly - leaf_len * math.sin(leaf_ang))
            p3 = (lx + leaf_len * 0.6 * math.cos(leaf_ang + 0.3), ly - leaf_len * 0.6 * math.sin(leaf_ang + 0.3))
            p4 = (lx + leaf_len * 0.6 * math.cos(leaf_ang - 0.3), ly - leaf_len * 0.6 * math.sin(leaf_ang - 0.3))
            draw.polygon([p1, p3, p2, p4], fill=(245, 205, 45, 240), outline=(160, 120, 15, 255))

    draw.ellipse((cx - 5, h - 14, cx + 5, h - 6), fill=(215, 175, 40, 255), outline=(140, 100, 15, 255))
    return im


# ==========================================
# 5 INTERNAL SECURITY ICON BUILDERS
# ==========================================

def build_sec_public_order() -> Image.Image:
    """1. sec_public_order: Trật tự Công cộng"""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44

    # Tactical Shield (Deep Red & Police Dark Navy with Gold Rim)
    w_s, h_s = 68, 76
    pts = [
        (cx - w_s/2, cy - h_s/2 + 4),
        (cx + w_s/2, cy - h_s/2 + 4),
        (cx + w_s/2, cy + 6),
        (cx, cy + h_s/2 - 2),
        (cx - w_s/2, cy + 6)
    ]
    draw.polygon(pts, fill=(18, 28, 48, 250), outline=(225, 185, 45, 255), width=3)
    
    # Inner red police emblem shield
    pts_in = [
        (cx - w_s/2 + 5, cy - h_s/2 + 9),
        (cx + w_s/2 - 5, cy - h_s/2 + 9),
        (cx + w_s/2 - 5, cy + 5),
        (cx, cy + h_s/2 - 7),
        (cx - w_s/2 + 5, cy + 5)
    ]
    draw.polygon(pts_in, fill=(180, 25, 30, 240), outline=(245, 215, 60, 160), width=1)

    # Crossed Police Tactical Batons behind cockade
    for angle in (-35, 35):
        rad = math.radians(angle)
        dx, dy = 28 * math.sin(rad), 28 * math.cos(rad)
        draw.line([(cx - dx, cy + dy - 2), (cx + dx, cy - dy - 2)], fill=(40, 45, 52, 255), width=4)
        draw.line([(cx - dx, cy + dy - 2), (cx + dx, cy - dy - 2)], fill=(90, 100, 115, 255), width=2)
        # Baton handle grip
        hx, hy = cx - dx * 0.75, cy + dy * 0.75 - 2
        draw.circle((hx, hy), 3, fill=(215, 180, 50, 255))

    # Flashing Emergency Beacon at top (Red left, Blue right)
    beacon_y = cy - 24
    draw.rounded_rectangle([cx - 16, beacon_y, cx - 2, beacon_y + 10], radius=3, fill=(240, 35, 35, 255), outline=(150, 20, 20, 255))
    draw.rounded_rectangle([cx + 2, beacon_y, cx + 16, beacon_y + 10], radius=3, fill=(30, 120, 245, 255), outline=(15, 60, 160, 255))
    draw.rectangle([cx - 18, beacon_y + 9, cx + 18, beacon_y + 13], fill=(70, 75, 85, 255))

    # Central Police Gold Star Cockade
    star = create_gold_star(26)
    canvas.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2 + 2)), star)

    # Golden Laurel Wreath at bottom
    laurel = create_gold_laurel_wreath(74, 46)
    canvas.paste(laurel, (int(cx - laurel.width / 2), 44), laurel)

    return canvas


def build_sec_border_control() -> Image.Image:
    """2. sec_border_control: Siết Biên giới & Kiểm soát Di chuyển"""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44

    # Dark mountain frontier background circle
    draw.ellipse([cx - 36, cy - 36, cx + 36, cy + 36], fill=(22, 34, 30, 250), outline=(215, 175, 45, 255), width=2)

    # Mountain silhouette in background
    draw.polygon([(cx - 34, cy + 10), (cx - 16, cy - 14), (cx + 6, cy + 4), (cx + 26, cy - 18), (cx + 34, cy + 10)], fill=(38, 55, 48, 255))

    # Searchlight beam sweeping across from top right
    beam_pts = [(cx + 28, cy - 24), (cx - 32, cy + 18), (cx - 12, cy + 28)]
    draw.polygon(beam_pts, fill=(255, 255, 210, 50))

    # Vietnam National Border Milestone (Cột mốc biên giới quốc gia)
    # Granite pillar body (trapezoidal tapered stone)
    pole_w_top = 18
    pole_w_bot = 24
    pole_top_y = cy - 14
    pole_bot_y = cy + 28
    
    # 3D Granite Bevel: Left side light, Right side shadow
    pts_left = [
        (cx, pole_top_y - 6), # Pyramid tip
        (cx - pole_w_top / 2, pole_top_y),
        (cx - pole_w_bot / 2, pole_bot_y),
        (cx, pole_bot_y)
    ]
    draw.polygon(pts_left, fill=(225, 230, 235, 255), outline=(130, 140, 150, 255))
    
    pts_right = [
        (cx, pole_top_y - 6),
        (cx + pole_w_top / 2, pole_top_y),
        (cx + pole_w_bot / 2, pole_bot_y),
        (cx, pole_bot_y)
    ]
    draw.polygon(pts_right, fill=(180, 190, 200, 255), outline=(110, 120, 130, 255))

    # Red National Emblem plate on milestone
    draw.rounded_rectangle([cx - 6, pole_top_y + 4, cx + 6, pole_top_y + 16], radius=2, fill=(205, 25, 30, 255), outline=(235, 190, 50, 255))
    star_mini = create_gold_star(10)
    canvas.paste(star_mini, (int(cx - star_mini.width / 2), int(pole_top_y + 5)), star_mini)

    # Crossed Checkpoint Barrier Gates (Red & White Striped Barie)
    bar_y = cy + 14
    draw.line([(cx - 32, bar_y - 8), (cx + 32, bar_y + 4)], fill=(240, 240, 240, 255), width=4)
    # Red stripes along barrier
    for st in range(-28, 28, 12):
        draw.line([(cx + st, bar_y - 8 + (st + 28) * 12 // 56), (cx + st + 6, bar_y - 8 + (st + 34) * 12 // 56)], fill=(225, 30, 30, 255), width=4)

    # Barbed wire at base
    draw.line([(cx - 32, cy + 30), (cx + 32, cy + 30)], fill=(90, 100, 110, 255), width=2)
    for bx in range(int(cx - 26), int(cx + 28), 10):
        draw.line([(bx - 3, cy + 27), (bx + 3, cy + 33)], fill=(180, 190, 200, 255), width=2)
        draw.line([(bx + 3, cy + 27), (bx - 3, cy + 33)], fill=(180, 190, 200, 255), width=2)

    return canvas


def build_sec_surveillance_network() -> Image.Image:
    """3. sec_surveillance_network: Mạng lưới Giám sát Đại chúng"""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44

    # High-tech dark circle
    draw.ellipse([cx - 36, cy - 36, cx + 36, cy + 36], fill=(16, 22, 32, 250), outline=(40, 190, 140, 220), width=2)

    # Digital Mesh Network Nodes in background
    nodes = [
        (cx - 24, cy - 16), (cx - 10, cy - 26), (cx + 18, cy - 20),
        (cx - 20, cy + 16), (cx + 22, cy + 14), (cx + 10, cy + 24)
    ]
    for p1 in nodes:
        for p2 in nodes:
            if p1 != p2:
                draw.line([p1, p2], fill=(30, 120, 180, 60), width=1)
    for nx, ny in nodes:
        draw.ellipse([nx - 2, ny - 2, nx + 2, ny + 2], fill=(40, 220, 160, 200))

    # CCTV Surveillance Camera (Wall/Pole mounted dome/bullet camera)
    # Mount bracket
    draw.polygon([(cx - 30, cy - 18), (cx - 16, cy - 12), (cx - 16, cy - 6), (cx - 30, cy - 12)], fill=(80, 90, 100, 255))
    # Camera body (angled downward)
    cam_body = [
        (cx - 16, cy - 16), (cx + 10, cy - 6), (cx + 8, cy + 6), (cx - 16, cy - 4)
    ]
    draw.polygon(cam_body, fill=(210, 220, 230, 255), outline=(70, 80, 95, 255))
    # Dark lens cylinder
    draw.polygon([(cx + 10, cy - 6), (cx + 18, cy - 3), (cx + 16, cy + 9), (cx + 8, cy + 6)], fill=(30, 35, 45, 255), outline=(100, 110, 125, 255))
    # Cyan optical glass lens glint
    draw.ellipse([cx + 11, cy - 1, cx + 17, cy + 7], fill=(40, 200, 240, 255))
    # Red recording LED light
    draw.circle((cx - 8, cy - 12), 2, fill=(240, 30, 30, 255))

    # Biometric Facial Recognition Target Brackets (Green HUD)
    t_cx, t_cy = cx + 8, cy + 16
    t_sz = 14
    # 4 corner brackets
    draw.line([(t_cx - t_sz, t_cy - t_sz), (t_cx - t_sz + 6, t_cy - t_sz)], fill=(50, 240, 120, 255), width=2)
    draw.line([(t_cx - t_sz, t_cy - t_sz), (t_cx - t_sz, t_cy - t_sz + 6)], fill=(50, 240, 120, 255), width=2)

    draw.line([(t_cx + t_sz, t_cy - t_sz), (t_cx + t_sz - 6, t_cy - t_sz)], fill=(50, 240, 120, 255), width=2)
    draw.line([(t_cx + t_sz, t_cy - t_sz), (t_cx + t_sz, t_cy - t_sz + 6)], fill=(50, 240, 120, 255), width=2)

    draw.line([(t_cx - t_sz, t_cy + t_sz), (t_cx - t_sz + 6, t_cy + t_sz)], fill=(50, 240, 120, 255), width=2)
    draw.line([(t_cx - t_sz, t_cy + t_sz), (t_cx - t_sz, t_cy + t_sz - 6)], fill=(50, 240, 120, 255), width=2)

    draw.line([(t_cx + t_sz, t_cy + t_sz), (t_cx + t_sz - 6, t_cy + t_sz)], fill=(50, 240, 120, 255), width=2)
    draw.line([(t_cx + t_sz, t_cy + t_sz), (t_cx + t_sz, t_cy + t_sz - 6)], fill=(50, 240, 120, 255), width=2)

    # Face silhouette inside brackets
    draw.ellipse([t_cx - 4, t_cy - 7, t_cx + 4, t_cy + 1], fill=(40, 220, 140, 140))
    draw.polygon([(t_cx - 7, t_cy + 10), (t_cx - 4, t_cy + 2), (t_cx + 4, t_cy + 2), (t_cx + 7, t_cy + 10)], fill=(40, 220, 140, 140))

    return canvas


def build_sec_cyber_sovereignty() -> Image.Image:
    """4. sec_cyber_sovereignty: Chủ quyền Mạng"""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44

    # Grand Cybernetic Shield (Layered dark blue with bright cyan cyber borders)
    w_s, h_s = 68, 76
    pts = [
        (cx - w_s/2, cy - h_s/2 + 4),
        (cx + w_s/2, cy - h_s/2 + 4),
        (cx + w_s/2, cy + 6),
        (cx, cy + h_s/2 - 2),
        (cx - w_s/2, cy + 6)
    ]
    draw.polygon(pts, fill=(12, 22, 38, 250), outline=(30, 210, 245, 255), width=3)

    # Circuit Board Traces radiating within shield
    traces = [
        [(cx - 24, cy - 24), (cx - 16, cy - 16), (cx - 16, cy - 4)],
        [(cx + 24, cy - 24), (cx + 16, cy - 16), (cx + 16, cy - 4)],
        [(cx - 26, cy + 6), (cx - 14, cy + 18), (cx, cy + 24)],
        [(cx + 26, cy + 6), (cx + 14, cy + 18), (cx, cy + 24)],
        [(cx - 28, cy - 8), (cx - 20, cy - 8), (cx - 14, cy)],
        [(cx + 28, cy - 8), (cx + 20, cy - 8), (cx + 14, cy)],
    ]
    for tr in traces:
        draw.line(tr, fill=(40, 180, 220, 180), width=2)
        draw.circle(tr[0], 2, fill=(245, 215, 60, 255))

    # Brick Firewall Pattern in center backdrop
    for fy in range(int(cy - 12), int(cy + 14), 6):
        draw.line([(cx - 18, fy), (cx + 18, fy)], fill=(220, 60, 40, 120), width=1)
        shift = 4 if (fy // 6) % 2 == 0 else 0
        for fx in range(int(cx - 18) + shift, int(cx + 18), 8):
            draw.line([(fx, fy), (fx, fy + 5)], fill=(220, 60, 40, 120), width=1)

    # Central National Cyber Roundel with VPA Star
    r_core = 16
    draw.ellipse([cx - r_core, cy - r_core - 2, cx + r_core, cy + r_core - 2], fill=(195, 25, 30, 255), outline=(235, 195, 45, 255), width=2)
    star = create_gold_star(18)
    canvas.paste(star, (int(cx - star.width / 2), int(cy - star.height / 2 - 2)), star)

    # Robust Gold Padlock at base of core
    pad_y = cy + 14
    # Shackle
    draw.arc([cx - 7, pad_y - 8, cx + 7, pad_y + 4], start=180, end=360, fill=(230, 240, 250, 255), width=2)
    # Body
    draw.rounded_rectangle([cx - 9, pad_y - 2, cx + 9, pad_y + 12], radius=2, fill=(235, 195, 45, 255), outline=(140, 100, 15, 255))
    # Keyhole
    draw.circle((cx, pad_y + 3), 2, fill=(40, 30, 10, 255))
    draw.line([(cx, pad_y + 4), (cx, pad_y + 8)], fill=(40, 30, 10, 255), width=1)

    return canvas


def build_sec_state_data_center() -> Image.Image:
    """5. sec_state_data_center: Trung tâm Dữ liệu Quốc gia"""
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    cx, cy = 46, 44

    # Hexagonal server facility housing
    hex_pts = [
        (cx - 36, cy - 20), (cx, cy - 38), (cx + 36, cy - 20),
        (cx + 36, cy + 20), (cx, cy + 38), (cx - 36, cy + 20)
    ]
    draw.polygon(hex_pts, fill=(18, 24, 36, 250), outline=(215, 175, 45, 255), width=2)

    # Server Racks on Left & Right
    # Left Server Tower
    draw.rounded_rectangle([cx - 30, cy - 22, cx - 12, cy + 22], radius=2, fill=(28, 34, 46, 255), outline=(70, 85, 105, 255))
    for sy in range(int(cy - 18), int(cy + 20), 6):
        draw.line([(cx - 28, sy), (cx - 14, sy)], fill=(45, 55, 70, 255), width=2)
        # LED indicators (green, blue, amber)
        draw.circle((cx - 26, sy), 1, fill=(40, 220, 120, 255))
        draw.circle((cx - 22, sy), 1, fill=(40, 180, 240, 255))

    # Right Server Tower
    draw.rounded_rectangle([cx + 12, cy - 22, cx + 30, cy + 22], radius=2, fill=(28, 34, 46, 255), outline=(70, 85, 105, 255))
    for sy in range(int(cy - 18), int(cy + 20), 6):
        draw.line([(cx + 14, sy), (cx + 28, sy)], fill=(45, 55, 70, 255), width=2)
        draw.circle((cx + 16, sy), 1, fill=(40, 220, 120, 255))
        draw.circle((cx + 20, sy), 1, fill=(40, 180, 240, 255))

    # Center: National Citizen Smart ID Card (CCCD gắn chip)
    card_w, card_h = 32, 22
    card_x, card_y = cx - card_w/2, cy - card_h/2 - 2
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=3, fill=(235, 245, 252, 255), outline=(160, 185, 210, 255))
    # Red banner header on card
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + 5], radius=2, fill=(195, 30, 35, 255))
    # Miniature VPA Star on card header
    star_tiny = create_gold_star(6)
    canvas.paste(star_tiny, (int(card_x + 3), int(card_y)), star_tiny)

    # Golden Smart Microchip on card
    chip_x, chip_y = card_x + 4, card_y + 8
    draw.rounded_rectangle([chip_x, chip_y, chip_x + 9, chip_y + 8], radius=1, fill=(245, 215, 60, 255), outline=(160, 120, 20, 255))
    draw.line([(chip_x + 3, chip_y), (chip_x + 3, chip_y + 8)], fill=(180, 130, 20, 255))
    draw.line([(chip_x + 6, chip_y), (chip_x + 6, chip_y + 8)], fill=(180, 130, 20, 255))
    draw.line([(chip_x, chip_y + 4), (chip_x + 9, chip_y + 4)], fill=(180, 130, 20, 255))

    # Barcode / photo placeholder on card
    draw.rectangle([card_x + 16, card_y + 8, card_x + 28, card_y + 10], fill=(80, 120, 160, 255))
    draw.rectangle([card_x + 16, card_y + 12, card_x + 25, card_y + 14], fill=(120, 150, 180, 255))

    # Database Cylinders Stack at bottom
    db_y = cy + 18
    for d_offset in (0, 5):
        draw.ellipse([cx - 16, db_y + d_offset, cx + 16, db_y + d_offset + 8], fill=(30, 140, 220, 240), outline=(215, 175, 45, 255))
        draw.rectangle([cx - 16, db_y + d_offset + 4, cx + 16, db_y + d_offset + 8], fill=(20, 100, 170, 240))
        draw.ellipse([cx - 16, db_y + d_offset + 4, cx + 16, db_y + d_offset + 12], fill=(25, 120, 195, 240), outline=(215, 175, 45, 255))

    return canvas


# ==========================================
# MAIN EXECUTION, GFX & FOCUS UPDATES
# ==========================================

FOCUS_MAP = {
    "VIE_sec_public_order": ("sec_public_order", build_sec_public_order),
    "VIE_sec_border_control": ("sec_border_control", build_sec_border_control),
    "VIE_sec_surveillance_network": ("sec_surveillance_network", build_sec_surveillance_network),
    "VIE_sec_cyber_sovereignty": ("sec_cyber_sovereignty", build_sec_cyber_sovereignty),
    "VIE_sec_state_data_center": ("sec_state_data_center", build_sec_state_data_center),
}


def register_gfx():
    """Register spriteTypes in interface/VIE_md_focus_icons.gfx."""
    txt = GFX_FILE.read_text(encoding="utf-8")
    added = 0
    for fid, (stem, _) in FOCUS_MAP.items():
        sprite_name = f"GFX_focus_VIE_{stem}"
        if sprite_name not in txt:
            entry = f"""\tspriteType = {{
\t\tname = "{sprite_name}"
\t\ttexturefile = "gfx/interface/goals/{stem}.dds"
\t}}
"""
            last_brace = txt.rfind("}")
            txt = txt[:last_brace] + entry + txt[last_brace:]
            added += 1
            print(f"Registered sprite: {sprite_name}")

    if added > 0:
        GFX_FILE.write_text(txt, encoding="utf-8")
        print(f"Added {added} spriteType entries to {GFX_FILE.name}")
    else:
        print("All sprites already registered in GFX file.")


def update_focus_tree():
    """Update icon = in common/national_focus/VIE_md_focus.txt to use the new custom sprites."""
    txt = FOCUS_FILE.read_text(encoding="utf-8")
    updated = 0
    for fid, (stem, _) in FOCUS_MAP.items():
        sprite_name = f"GFX_focus_VIE_{stem}"
        # Match the focus block for fid and replace icon = ...
        pattern = re.compile(rf"(id\s*=\s*{fid}\b.*?)(\bicon\s*=\s*\S+)", re.DOTALL)
        m = pattern.search(txt)
        if m:
            old_icon_line = m.group(2)
            new_icon_line = f"icon = {sprite_name}"
            # Replace only this occurrence
            start, end = m.span(2)
            txt = txt[:start] + new_icon_line + txt[end:]
            updated += 1
            print(f"Updated focus {fid}: {old_icon_line} -> {new_icon_line}")

    FOCUS_FILE.write_text(txt, encoding="utf-8")
    print(f"Successfully updated {updated} focus icon references in {FOCUS_FILE.name}")


def main():
    print("==============================================")
    print("Building 5 Focus Icons for Internal Security (Nhánh An ninh Nội địa)")
    print("==============================================")

    for fid, (stem, builder) in FOCUS_MAP.items():
        img = builder()
        save_game_ready_icon(img, stem)

    print("\nRegistering GFX definitions...")
    register_gfx()

    print("\nUpdating focus tree icon references...")
    update_focus_tree()

    print("\n[SUCCESS] Completed all Internal Security focus icons!")


if __name__ == "__main__":
    main()
