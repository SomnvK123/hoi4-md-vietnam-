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

## Diplomacy batch 01, revision 2 (2026-10-08)

Four new masters: `asean_chair`, `un_security_council`,
`special_relations_laos`, and `bamboo_diplomacy`. Revision 1's shiny brass
badges were rejected for looking cartoonish.

Revision 2 uses matte editorial painting, realistic proportions and actions
informed by Vietnamese poster collections and diplomacy press coverage:

- ASEAN: a hand raising the chairmanship gavel conveys taking responsibility,
  supported by Vietnam's flag and a conference table.
- Security Council: a horseshoe council table and Vietnam's delegate station
  convey a seat and voice in an international institution.
- Vietnam-Laos: a handshake under both flags conveys mutual support;
  a bridge alone could be mistaken for an infrastructure focus.
- Bamboo: rooted earth, strong culms and wind-bent shoots convey independent
  principles and flexibility. Natural bamboo replaces a decorative jade bundle.

The museum and press references, generation prompts and original output paths
are recorded in `diplomacy_batch_01_prompts.json`. References were studied,
not copied into game textures. Institutional motifs are illustrative, not
certified reproductions of official emblems. All masters were generated with
the built-in OpenAI image tool, with actual alpha.

Rebuild only these four exports from the repository root:

```powershell
python assets/focus_icons/raw/export_diplomacy_batch_01.py
```

If the Windows `python` alias is unavailable, use an installed Python with
Pillow (the bundled Codex Python was used for this run). The recipe imports
only `write_dds`, keeps both earlier ASEAN/border assets intact, verifies
pixel round-trips and mappings, and creates dark/light previews. Technical
records are in `diplomacy_batch_01_record.json`. Previews and the DDS/GFX audit
log are in `../previews/diplomacy_batch_01/`.

Visual review: all four viewed at native 93x91 on dark and light backgrounds.
Primary gestures and silhouettes remain distinct; fine furniture, root and
leaf details are secondary at this scale. In-game display and hover are unrun.
