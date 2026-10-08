# Diplomacy focus artwork

`asean_integration.png` and `border_settlement.png` are the original transparent
PNG artworks generated with OpenAI image generation and selected by the user.
Their designs follow `.claude/docs/art-style-guide/`, especially volumes 3 and 5.

The complete badge already includes its diplomatic wreath frame. Preserve it;
do not apply the additional frame in `tools/process_focus_batch.py`.

The game uses `gfx/interface/goals/<stem>.dds` through the existing
`GFX_focus_VIE_<stem>` sprite definitions. The matching PNG exports are in
`assets/focus_icons/png/`.

To reproduce the two exports from the repository root:

```python
from pathlib import Path
import sys
from PIL import Image, ImageOps

sys.path.insert(0, "tools")
from build_vie_focus_icons import write_dds

for stem in ("asean_integration", "border_settlement"):
    with Image.open(Path("assets/focus_icons/raw") / f"{stem}.png") as source:
        art = ImageOps.contain(
            source.convert("RGBA"), (91, 89), Image.Resampling.LANCZOS
        )
    icon = Image.new("RGBA", (93, 91), (0, 0, 0, 0))
    icon.paste(art, ((93 - art.width) // 2, (91 - art.height) // 2))
    icon.save(Path("assets/focus_icons/png") / f"{stem}.png")
    write_dds(Path("gfx/interface/goals") / f"{stem}.dds", icon)
```

Exports are 93x91 pixels, uncompressed 32-bit BGRA DDS with no mipmaps
(33,980 bytes), with a fully transparent one-pixel outer border.
The legacy diplomacy icon builders generate different artwork and will replace
these exports if run for the same stems.
