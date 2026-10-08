# MD Vietnam repository guidance

This is a Vietnam submod for Millennium Dawn, targeting HOI4 1.19.*.
Read [.claude/CLAUDE.md](.claude/CLAUDE.md) for repository conventions and the
documentation relevant to the requested change. Preserve existing user changes.

## Artwork tasks

For generating, editing, reviewing, exporting or integrating artwork, read
[md-art](.claude/skills/md-art/SKILL.md), then the asset-specific skill it selects.
These are repository instructions; their presence does not imply an image tool
or a game installation is available.

Use the actual consumer, sprite and texture to establish dimensions, alpha,
format and any frame/state requirements. The current defaults and evidence are
in the [art guide](.claude/docs/art-style-guide/README.md).
Do not treat either “all modern icons are vector HUD neon” or “all artwork must
be a detailed gold-framed oil painting” as a verified Millennium Dawn rule.

Keep the two selected diplomacy masters and their exports intact unless the
requested artwork change includes them. Check images at their native display
size. Report file validation, integration and in-game validation separately.

## Validation

Use the relevant commands in [.claude/docs/validation.md](.claude/docs/validation.md).
Inspect diagnostic output even when the command returns zero. Base-game/MD
sprites may be external to this submod checkout. Do not invent missing IDs or
change gameplay for an artwork-only request.
