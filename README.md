# 1000 Design Vibes

Generate unique, self-contained design system showcases using Claude Code subagents. Each design is a single HTML file that's both a visual demo and a complete style guide.

**Current Status:** 140 designs generated across 5 test runs.

## What is this?

This project generates design systems by combining 30+ visual dimensions:
- **UI paradigm**: flat, material, glassmorphic, brutalist, organic...
- **Design era**: art deco, bauhaus, y2k, neo-brutalist, punk...
- **Color theory**: monochromatic, complementary, triadic...
- **Typography, spacing, shadows, and 25+ more dimensions**

Each combination produces a unique design with its own personality, creative name, and complete component library. All designs are self-contained HTML files that work offline.

## Browse the Gallery

Open `outputs/index.html` in your browser to see all generated designs. Each design page includes:
- Full component library (buttons, forms, cards, navigation)
- Complete CSS custom properties for all design tokens
- Keyboard navigation (← →) to browse designs
- Mobile touch/swipe support

## Quick Start

```bash
# Clone and setup
git clone https://github.com/yourusername/1000-design-vibes
cd 1000-design-vibes
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Generate 20 unique design seeds
python design_vibes.py manifest --count 20 --name "my-batch"

# Generate designs using Claude Code (see below)
```

## Workflow

### 1. Create a manifest

```bash
python design_vibes.py manifest --count 100 --name "batch1"
```

Creates a `manifest.json` with unique dimension combinations and creative names.

### 2. Generate designs with Claude Code

Open the project in Claude Code and run:

```
Generate designs for outputs/2026-01-06-batch1
```

Claude Code reads the manifest and spawns subagents to generate each design. Designs are written to `.staging/` first, then moved to `designs/` after validation.

### 3. Check progress

```bash
python design_vibes.py status --path outputs/2026-01-06-batch1
```

Shows completed, in-progress, and failed designs.

### 4. Browse your designs

```bash
open outputs/2026-01-06-batch1/index.html
```

## Commands

### `manifest` - Create design seeds

```bash
python design_vibes.py manifest --count 20 --name "test"
```

Options:
- `--count` - Number of designs to generate (default: 20)
- `--name` - Optional suffix for the output folder

### `status` - Check progress

```bash
python design_vibes.py status --path outputs/2026-01-06-test
```

Shows:
- Completed designs (in `designs/`)
- Staging designs (in `.staging/`)
- Failed designs (in `failures.json`)
- Pending designs (not yet started)

### `build-indexes` - Rebuild gallery pages

```bash
python design_vibes.py build-indexes
```

Regenerates the index.html for each run with updated stats and design cards.

## Output Structure

```
outputs/
  2026-01-06-batch1/
    manifest.json           # The design seeds
    index.html              # Gallery homepage
    failures.json           # Failed design attempts
    .staging/               # Designs in progress
    designs/
      design-1.html         # Completed showcases
      design-2.html
      ...
```

Each HTML file is completely self-contained (except for Google Fonts) and includes:
- Full component library (buttons, forms, cards, etc.)
- CSS custom properties for all design tokens
- LLM-readable documentation for recreating the style
- Keyboard/touch navigation to browse designs

## How It Works

1. **Manifest generation** (Python) - Creates unique combinations of 30+ dimensions
2. **Design generation** (Claude Code) - Spawns parallel subagents to generate HTML
3. **Validation** - Checks designs before moving to final folder
4. **Index building** - Creates gallery with all designs

## Files

- `DESIGN_GUIDE.md` - Instructions for design agents
- `src/dimensions.py` - All 30+ dimension definitions
- `src/manifest.py` - Manifest generation logic
- `src/naming.py` - Creative name generation
- `src/index.py` - Gallery builder
- `src/status.py` - Progress reporting

## Requirements

- Python 3.10+
- Claude Code (Claude Max plan recommended)

## License

MIT
