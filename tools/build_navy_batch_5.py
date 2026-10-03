"""Script to build Batch 5 Focus Icons for Vietnam Navy (Hải quân) in Millennium Dawn.
Batch 5 focuses (Trục 3 Viễn dương Bluewater, Hậu cần & Cụm Tàu sân bay - 6 focuses):
23. nf_regional_command: Bộ chỉ huy Hạm đội Khu vực (Bánh lái hoa tiêu, khiên hải quân mạ vàng, nòng pháo hạm, quân hiệu VPA, mỏ neo)
24. nf_bluewater: Hải quân Viễn dương / Bluewater Fleet (Biên đội 3 chiến hạm rẽ sóng đại dương, máy bay tuần thám, vòng nguyệt quế vàng, sao vàng)
25. nf_ocean_escort: Hộ tống Viễn dương / Khu trục hạm (Khu trục hạm tên lửa dẫn đường phóng tên lửa đối không, tiêm kích hạm, mỏ neo vàng)
26. nf_replenishment: Bảo đảm Hậu cần Hạm đội (Tàu tiếp tế hậu cần trên biển UNREP, cần cẩu hàng hóa, đĩa tròn xanh biển, mỏ neo vàng)
27. nf_naval_aviation: Không quân Hải quân (Tiêm kích hạm Su-30MK2 rẽ mây trên bầu trời biển cả, vòng nguyệt quế vàng, sao vàng 3D)
28. nf_carrier_group: Nhóm Tác chiến Tàu sân bay (Kỳ hạm tàu sân bay boong chéo phóng tiêm kích hạm, vòng nguyệt quế bạc-vàng danh dự, sao vàng)

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
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
BRAIN_DIR = Path(r"C:\Users\doans\.gemini\antigravity-ide\brain\add5d4ba-18d3-49e5-8343-5c2c59714d4f")
MD_GOALS = Path(r"D:\SteamLibrary\steamapps\workshop\content\394360\2777392649\gfx\interface\goals")

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


def create_naval_anchor(w: int, h: int, color_type: str = "gold") -> Image.Image:
    """Generate a crisp metallic naval anchor."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)
    
    if color_type == "gold":
        c_fill = (220, 180, 50, 255)
        c_light = (255, 230, 110, 255)
        c_dark = (140, 100, 15, 255)
    else:
        c_fill = (180, 195, 205, 255)
        c_light = (225, 235, 245, 255)
        c_dark = (90, 105, 115, 255)

    cx = w / 2
    ring_r = int(w * 0.16)
    ring_cy = ring_r + 2
    draw.ellipse((cx - ring_r, ring_cy - ring_r, cx + ring_r, ring_cy + ring_r), fill=c_fill, outline=c_dark, width=2)
    inner_r = int(ring_r * 0.45)
    draw.ellipse((cx - inner_r, ring_cy - inner_r, cx + inner_r, ring_cy + inner_r), fill=(0, 0, 0, 0), outline=c_dark, width=1)

    bar_y = int(h * 0.26)
    bar_w = int(w * 0.65)
    bar_h = int(h * 0.09)
    draw.rounded_rectangle((cx - bar_w / 2, bar_y, cx + bar_w / 2, bar_y + bar_h), radius=2, fill=c_fill, outline=c_dark)
    draw.ellipse((cx - bar_w / 2 - 2, bar_y - 1, cx - bar_w / 2 + bar_h + 1, bar_y + bar_h + 1), fill=c_light, outline=c_dark)
    draw.ellipse((cx + bar_w / 2 - bar_h - 1, bar_y - 1, cx + bar_w / 2 + 2, bar_y + bar_h + 1), fill=c_light, outline=c_dark)

    shank_w = int(w * 0.14)
    shank_top = ring_cy + ring_r - 2
    shank_bot = int(h * 0.78)
    draw.rectangle((cx - shank_w / 2, shank_top, cx + shank_w / 2, shank_bot), fill=c_fill, outline=c_dark)
    draw.line((cx - 1, shank_top + 2, cx - 1, shank_bot - 2), fill=c_light, width=1)

    arc_box = (int(w * 0.10), int(h * 0.50), int(w * 0.90), int(h * 0.96))
    draw.arc(arc_box, start=20, end=160, fill=c_fill, width=int(w * 0.13))
    draw.arc(arc_box, start=20, end=160, fill=c_dark, width=1)

    fluke_sz = int(w * 0.20)
    lf_x = int(w * 0.16)
    lf_y = int(h * 0.65)
    draw.polygon([(lf_x, lf_y - fluke_sz), (lf_x + fluke_sz, lf_y), (lf_x - fluke_sz // 2, lf_y)], fill=c_light, outline=c_dark)
    rf_x = int(w * 0.84)
    rf_y = int(h * 0.65)
    draw.polygon([(rf_x, rf_y - fluke_sz), (rf_x - fluke_sz, rf_y), (rf_x + fluke_sz // 2, rf_y)], fill=c_light, outline=c_dark)
    draw.polygon([(cx - 4, int(h * 0.94)), (cx + 4, int(h * 0.94)), (cx, h - 2)], fill=c_fill, outline=c_dark)
    return im


def paste_centered(target: Image.Image, src: Image.Image, offset_x: int = 0, offset_y: int = 0):
    """Paste src onto target centered with offsets."""
    tx = (target.width - src.width) // 2 + offset_x
    ty = (target.height - src.height) // 2 + offset_y
    target.paste(src, (tx, ty), src)


# =========================================================================
# 23. VIE_nf_regional_command (Bộ chỉ huy Hạm đội Khu vực)
# =========================================================================
def build_nf_regional_command() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: navy2.dds (ship's wheel/helm on ornate shield with dual naval cannons)
    p_cmd = MD_GOALS / "00_navy" / "navy2.dds"
    if p_cmd.exists():
        im_cmd = Image.open(p_cmd).convert("RGBA")
        im_cmd = im_cmd.resize((86, 76), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_cmd, offset_x=0, offset_y=-2)

    # In center of ship's wheel: VPA Naval Roundel Cockade
    cockade = create_vpa_cockade(size=22)
    paste_centered(canvas, cockade, offset_x=0, offset_y=-2)

    # Top apex: 3D Faceted Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_regional_command")
    return canvas


# =========================================================================
# 24. VIE_nf_bluewater (Hải quân Viễn dương / Bluewater Fleet)
# =========================================================================
def build_nf_bluewater() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: focus_SMB_blue_water_fleet.dds (3 warships in battle formation cutting ocean waves, maritime patrol aircraft overhead, golden laurel frame)
    p_blue = MD_GOALS / "00_navy" / "focus_SMB_blue_water_fleet.dds"
    if p_blue.exists():
        im_blue = Image.open(p_blue).convert("RGBA")
        im_blue = im_blue.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_blue, offset_x=0, offset_y=-3)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_bluewater")
    return canvas


# =========================================================================
# 25. VIE_nf_ocean_escort (Hộ tống Viễn dương / Khu trục hạm)
# =========================================================================
def build_nf_ocean_escort() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: exercise_keen_sword.dds (modern guided-missile destroyer launching missile with fiery plume, fighter jet above, in golden laurel wreath)
    p_esc = MD_GOALS / "00_navy" / "exercise_keen_sword.dds"
    if p_esc.exists():
        im_esc = Image.open(p_esc).convert("RGBA")
        im_esc = im_esc.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_esc, offset_x=0, offset_y=-3)

    # Top apex: 3D Faceted Gold Star
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_ocean_escort")
    return canvas


# =========================================================================
# 26. VIE_nf_replenishment (Bảo đảm Hậu cần Hạm đội / Tiếp tế Trên biển UNREP)
# =========================================================================
def build_nf_replenishment() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: ENG_Expand_Trade_Fleet.dds (fleet replenishment vessel with crane loading supplies in deep blue medallion and golden wreath)
    p_rep = MD_GOALS / "00_navy" / "ENG_Expand_Trade_Fleet.dds"
    if p_rep.exists():
        im_rep = Image.open(p_rep).convert("RGBA")
        im_rep = im_rep.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_rep, offset_x=0, offset_y=-3)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(16)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_replenishment")
    return canvas


# =========================================================================
# 27. VIE_nf_naval_aviation (Không quân Hải quân)
# =========================================================================
def build_nf_naval_aviation() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: modern_fighter.dds (Su-30MK2 Flanker naval strike fighter in sky/sea circular frame with golden laurel wreath)
    p_air = MD_GOALS / "00_airforce" / "modern_fighter.dds"
    if p_air.exists():
        im_air = Image.open(p_air).convert("RGBA")
        im_air = im_air.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_air, offset_x=0, offset_y=-3)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_naval_aviation")
    return canvas


# =========================================================================
# 28. VIE_nf_carrier_group (Nhóm Tác chiến Tàu sân bay - Capstone)
# =========================================================================
def build_nf_carrier_group() -> Image.Image:
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))

    # Base: carriers2.dds (modern angled flight deck aircraft carrier launching catapult jet with silver/golden laurel wreath)
    p_car = MD_GOALS / "00_navy" / "carriers2.dds"
    if p_car.exists():
        im_car = Image.open(p_car).convert("RGBA")
        im_car = im_car.resize((86, 78), Image.Resampling.LANCZOS)
        paste_centered(canvas, im_car, offset_x=0, offset_y=-3)

    # Top apex: 3D Faceted Gold Star of Vietnam
    star = create_gold_star(18)
    paste_centered(canvas, star, offset_x=0, offset_y=-32)

    # Bottom: Golden naval anchor
    anchor = create_naval_anchor(w=16, h=18, color_type="gold")
    paste_centered(canvas, anchor, offset_x=0, offset_y=26)

    save_game_ready_icon(canvas, "nf_carrier_group")
    return canvas


def create_showcase(icons, labels):
    """Generate professional Batch 5 showcase artifact."""
    n = len(icons)
    card_w = 110
    total_w = n * card_w + 30
    total_h = 165

    im = Image.new("RGBA", (total_w, total_h), (16, 22, 30, 255))
    draw = ImageDraw.Draw(im)

    try:
        font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 13)
        font_label = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
    except Exception:
        font_title = ImageFont.load_default()
        font_label = ImageFont.load_default()

    draw.text((15, 12), "HẢI QUÂN NHÂN DÂN VIỆT NAM (HQNDVN) - BATCH 5: VIỄN DƯƠNG & TÀU SÂN BAY", fill=(255, 215, 0, 255), font=font_title)

    for i, (icon, label) in enumerate(zip(icons, labels)):
        cx = 15 + i * card_w + 8
        cy = 40

        # Card container
        draw.rounded_rectangle((cx - 4, cy - 4, cx + 93 + 4, cy + 91 + 4), radius=4, fill=(24, 32, 44, 255), outline=(48, 64, 84, 255), width=1)
        im.paste(icon, (cx, cy), icon)

        # Label underneath
        draw.text((cx - 2, cy + 98), label, fill=(215, 225, 235, 255), font=font_label)

    out_path = BRAIN_DIR / "navy_batch_5_showcase.png"
    im.save(out_path)
    print(f"Saved Showcase: {out_path}")


def create_tree_simulation():
    """Generate in-game focus tree simulation diagram for Batch 5."""
    canvas_w = 820
    canvas_h = 440
    im = Image.new("RGBA", (canvas_w, canvas_h), (16, 20, 28, 255))
    draw = ImageDraw.Draw(im)

    # Grid lines
    for x in range(0, canvas_w, 35):
        draw.line((x, 0, x, canvas_h), fill=(25, 32, 45, 255), width=1)
    for y in range(0, canvas_h, 35):
        draw.line((0, y, canvas_w, y), fill=(25, 32, 45, 255), width=1)

    try:
        font_header = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 14)
        font_sub = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
        font_foc = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 10)
    except Exception:
        font_header = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_foc = ImageFont.load_default()

    draw.text((20, 15), "HOI4 / MILLENNIUM DAWN - CÂY TIÊU ĐIỂM HẢI QUÂN (BATCH 5: VIỄN DƯƠNG & CAPSTONE)", fill=(255, 215, 0, 255), font=font_header)
    draw.text((20, 35), "Mô phỏng hiển thị in-game: BTL Khu vực, Hạm đội Viễn dương, Khu trục hạm, Tiếp tế UNREP, KQ Hải quân & Cụm Tàu sân bay", fill=(160, 175, 195, 255), font=font_sub)

    c_gold = (190, 150, 45, 255)

    # Branch 1: LHD Program (Batch 4) -> Regional Command (x=100, y=140 -> x=100, y=250)
    draw.line((100 + 46, 140 + 70, 100 + 46, 250), fill=c_gold, width=2)

    # Branch 2: Operating Range (Batch 3) -> Bluewater (x=500, y=55 -> x=500, y=140)
    draw.line((500 + 46, 55 + 70, 500 + 46, 140), fill=c_gold, width=2)

    # Bluewater -> 3 branches: Ocean Escort (x=330, y=235), Replenishment (x=500, y=235), Naval Aviation (x=670, y=235)
    draw.line((500 + 46, 140 + 70, 500 + 46, 225), fill=c_gold, width=2)
    draw.line((330 + 46, 225, 670 + 46, 225), fill=c_gold, width=2)
    draw.line((330 + 46, 225, 330 + 46, 235), fill=c_gold, width=2)
    draw.line((500 + 46, 225, 500 + 46, 235), fill=c_gold, width=2)
    draw.line((670 + 46, 225, 670 + 46, 235), fill=c_gold, width=2)

    # 3 branches converge into Carrier Group at (x=500, y=330)
    draw.line((330 + 46, 235 + 70, 330 + 46, 320), fill=c_gold, width=2)
    draw.line((500 + 46, 235 + 70, 500 + 46, 320), fill=c_gold, width=2)
    draw.line((670 + 46, 235 + 70, 670 + 46, 320), fill=c_gold, width=2)
    draw.line((330 + 46, 320, 670 + 46, 320), fill=c_gold, width=2)
    draw.line((500 + 46, 320, 500 + 46, 330), fill=c_gold, width=2)

    nodes = [
        # Upstream anchors
        ("nf_lhd_program", "Tàu LHD Đổ bộ", 100, 100, False),
        ("nf_operating_range", "Mở rộng Phạm vi HĐ", 500, 45, False),
        # Batch 5 nodes
        ("nf_regional_command", "BTL Hạm đội Khu vực", 100, 245, True),
        ("nf_bluewater", "HQ Viễn dương (Bluewater)", 500, 135, True),
        ("nf_ocean_escort", "Khu trục hạm Hộ tống", 330, 235, True),
        ("nf_replenishment", "Tiếp tế Trên biển UNREP", 500, 235, True),
        ("nf_naval_aviation", "Không quân Hải quân", 670, 235, True),
        ("nf_carrier_group", "Cụm Tàu sân bay (CSG)", 500, 330, True),
    ]

    for stem, title, nx, ny, is_batch5 in nodes:
        png_p = PNG_DIR / f"{stem}.png"
        if png_p.exists():
            ic = Image.open(png_p).convert("RGBA").resize((70, 68), Image.Resampling.LANCZOS)
        else:
            ic = Image.new("RGBA", (70, 68), (40, 50, 60, 255))

        outline_c = (235, 195, 60, 255) if is_batch5 else (65, 85, 110, 255)
        fill_c = (26, 36, 50, 255) if is_batch5 else (20, 28, 38, 255)
        draw.rounded_rectangle((nx, ny, nx + 92, ny + 74), radius=4, fill=fill_c, outline=outline_c, width=2 if is_batch5 else 1)
        im.paste(ic, (nx + 11, ny + 3), ic)

        tb_w = 135
        tb_x = nx + 46 - tb_w // 2
        tb_y = ny + 76
        draw.rounded_rectangle((tb_x, tb_y, tb_x + tb_w, tb_y + 16), radius=3, fill=(15, 20, 28, 240), outline=outline_c, width=1)
        draw.text((tb_x + 6, tb_y + 2), title, fill=(255, 235, 140, 255) if is_batch5 else (180, 195, 210, 255), font=font_foc)

    out_sim = BRAIN_DIR / "navy_batch_5_tree_simulation.png"
    im.save(out_sim)
    print(f"Saved Simulation: {out_sim}")


def main():
    print("Building Navy Batch 5 focus icons...")
    ic1 = build_nf_regional_command()
    ic2 = build_nf_bluewater()
    ic3 = build_nf_ocean_escort()
    ic4 = build_nf_replenishment()
    ic5 = build_nf_naval_aviation()
    ic6 = build_nf_carrier_group()
    print("Completed all 6 icons for Navy Batch 5!")

    icons = [ic1, ic2, ic3, ic4, ic5, ic6]
    labels = [
        "BTL Hạm đội Khu vực",
        "HQ Viễn dương",
        "Khu trục hạm Hộ tống",
        "Tiếp tế UNREP",
        "Không quân Hải quân",
        "Cụm Tàu sân bay (CSG)"
    ]
    create_showcase(icons, labels)
    create_tree_simulation()
    print("Batch 5 build, showcase & simulation finished successfully!")


if __name__ == "__main__":
    main()
