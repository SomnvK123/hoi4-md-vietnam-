"""Convert AI generated high-resolution focus icons to game-ready 93x91 transparent PNG and DDS files.

Algorithm:
1. Corner flood-fill on near-white background to extract clean alpha mask.
2. Smooth alpha edges and de-fringe to remove white halo.
3. Center-fit onto transparent (93, 91) canvas with padding.
4. Export game-ready DDS (32-bit BGRA uncompressed) and preview PNG.
"""

import os
import struct
import sys
from collections import deque
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
PNG_DIR = ROOT / "assets" / "focus_icons" / "png"
DDS_DIR = ROOT / "gfx" / "interface" / "goals"
TARGET_SIZE = (93, 91)
ICON_MAX_SIZE = (86, 84)  # Leave padding around the badge


def extract_cutout(img: Image.Image, bg_tolerance: int = 25) -> Image.Image:
    img = img.convert("RGBA")
    w, h = img.size
    pixels = img.load()

    # Flood-fill background from the 4 corners
    corners = [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1)]
    visited = set(corners)
    queue = deque(corners)
    bg_mask = set()

    # Determine background color from corners
    avg_r = sum(pixels[x, y][0] for x, y in corners) // 4
    avg_g = sum(pixels[x, y][1] for x, y in corners) // 4
    avg_b = sum(pixels[x, y][2] for x, y in corners) // 4

    while queue:
        x, y = queue.popleft()
        r, g, b, _ = pixels[x, y]
        # Check distance to background color or near-white threshold
        dist = ((r - avg_r) ** 2 + (g - avg_g) ** 2 + (b - avg_b) ** 2) ** 0.5
        is_bg = dist < bg_tolerance or (r > 230 and g > 230 and b > 230)
        if is_bg:
            bg_mask.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    # Create alpha channel
    alpha_img = Image.new("L", (w, h), 255)
    alpha_pixels = alpha_img.load()
    for x, y in bg_mask:
        alpha_pixels[x, y] = 0

    # Smooth the alpha mask slightly for clean anti-aliasing
    alpha_smooth = alpha_img.filter(ImageFilter.GaussianBlur(radius=0.7))

    r, g, b, _ = img.split()
    cutout = Image.merge("RGBA", (r, g, b, alpha_smooth))

    # Crop to non-empty bounding box
    bbox = alpha_smooth.getbbox()
    if bbox:
        cutout = cutout.crop(bbox)

    return cutout


def process_icon(src_path: Path, stem: str):
    if not src_path.exists():
        print(f"Error: Source image not found: {src_path}")
        sys.exit(1)

    PNG_DIR.mkdir(parents=True, exist_ok=True)
    DDS_DIR.mkdir(parents=True, exist_ok=True)

    raw_img = Image.open(src_path)

    # 1. Extract cutout with transparent background
    cutout = extract_cutout(raw_img)

    # 2. Fit into max icon bounds while maintaining aspect ratio
    cutout.thumbnail(ICON_MAX_SIZE, Image.Resampling.LANCZOS)

    # 3. Punch up contrast and colors slightly for small-scale readability
    cutout_rgb = ImageEnhance.Contrast(cutout.convert("RGB")).enhance(1.15)
    cutout_rgb = ImageEnhance.Color(cutout_rgb).enhance(1.10)
    r, g, b = cutout_rgb.split()
    cutout = Image.merge("RGBA", (r, g, b, cutout.split()[-1]))

    # 4. Center on completely transparent 93x91 canvas
    canvas = Image.new("RGBA", TARGET_SIZE, (0, 0, 0, 0))
    offset_x = (TARGET_SIZE[0] - cutout.width) // 2
    offset_y = (TARGET_SIZE[1] - cutout.height) // 2
    canvas.paste(cutout, (offset_x, offset_y), cutout)

    # Save PNG
    png_path = PNG_DIR / f"{stem}.png"
    canvas.save(png_path)
    print(f"Saved transparent PNG: {png_path}")

    # Write uncompressed 32-bit BGRA DDS
    r, g, b, a = canvas.split()
    data = Image.merge("RGBA", (b, g, r, a)).tobytes()
    header = b"DDS " + struct.pack(
        "<7I11I8I5I", 124, 0x100F, TARGET_SIZE[1], TARGET_SIZE[0], TARGET_SIZE[0] * 4, 0, 0, *([0] * 11),
        32, 0x41, 0, 32, 0x00FF0000, 0x0000FF00, 0x000000FF, 0xFF000000, 0x1000, 0, 0, 0, 0
    )
    assert len(header) == 128
    dds_path = DDS_DIR / f"{stem}.dds"
    dds_path.write_bytes(header + data)
    print(f"Saved transparent DDS: {dds_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools/build_ai_focus_icons.py <input_image_path> <stem>")
        sys.exit(1)

    src = Path(sys.argv[1])
    stem = sys.argv[2]
    process_icon(src, stem)
