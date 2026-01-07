# 1000 Design Vibes

Generate unique, self-contained design system showcases using Claude Code subagents. Each design is a single HTML file that's both a visual demo and a complete style guide.

**Live Gallery:** [andrewedunn.github.io/1000-design-vibes](https://andrewedunn.github.io/1000-design-vibes)

**Current Status:** 240 designs generated across 6 batches. 760 to go.

## What is this?

This project generates design systems by combining 35 visual dimensions:
- **Functional direction**: 158 options (dashboard, admin panel, dating profile, Windows 95, vaporwave...)
- **UI paradigm**: flat, material, glassmorphic, brutalist, organic...
- **Design era**: art deco, bauhaus, y2k, neo-brutalist, punk...
- **Layout**: page structure, navigation pattern, hero style, content flow
- **Color, typography, spacing, shadows, and 25+ more dimensions**

Each combination produces a unique design with its own personality, creative name, and complete component library. All designs are self-contained HTML files that work offline.

## Browse the Gallery

Visit [the live gallery](https://andrewedunn.github.io/1000-design-vibes) or open `index.html` locally. Each design page includes:
- Full component library (buttons, forms, cards, navigation)
- Complete CSS custom properties for all design tokens
- LLM-readable documentation for applying the design to your project
- Keyboard navigation (← →) to browse designs
- Mobile touch/swipe support

## Quick Start

```bash
# Clone and setup
git clone https://github.com/andrewedunn/1000-design-vibes
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
Generate designs for outputs/2026-01-07-batch1
```

Claude Code reads the manifest and spawns Sonnet subagents to generate each design. Designs are written to `.staging/` first, then moved to `designs/` after validation.

### 3. Check progress

```bash
python design_vibes.py status --path outputs/2026-01-07-batch1
```

Shows completed, in-progress, and pending designs. Also suggests the next batch range and provides a resume prompt for Claude.

### 4. Browse your designs

```bash
python design_vibes.py build-indexes
open outputs/2026-01-07-batch1/designs/index.html
```

## Large Batch Execution

For batches of 500+ designs executed over multiple sessions, see [docs/BATCH_EXECUTION.md](docs/BATCH_EXECUTION.md). The `status` command provides resume prompts for continuing where you left off.

## Commands

### `manifest` - Create design seeds

```bash
python design_vibes.py manifest --count 100 --name "my-batch"
```

Options:
- `--count` - Number of designs to generate (default: 20)
- `--name` - Optional suffix for the output folder

### `status` - Check progress

```bash
python design_vibes.py status --path outputs/2026-01-07-my-batch
```

Shows:
- Completed designs (in `designs/`)
- Staging designs (in `.staging/`)
- Failed designs (in `failures.json`)
- Pending designs (not yet started)
- Suggested next batch range
- Resume prompt for Claude

### `build-indexes` - Rebuild gallery pages

```bash
python design_vibes.py build-indexes
```

Regenerates the index.html for each run with updated stats and design cards.

## Output Structure

```
outputs/
  2026-01-07-batch1/
    manifest.json           # The design seeds
    failures.json           # Failed design attempts (if any)
    .staging/               # Designs in progress
    designs/
      index.html            # Batch gallery
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

1. **Manifest generation** (Python) - Creates unique combinations of 35 dimensions
2. **Design generation** (Claude Code) - Spawns parallel Sonnet subagents to generate HTML
3. **Validation** - Checks designs before moving to final folder
4. **Index building** - Creates gallery with all designs

## Project Structure

```
├── design_vibes.py          # CLI entry point
├── DESIGN_GUIDE_LOOSE.md    # Instructions for design agents
├── index.html               # Main gallery
├── src/
│   ├── dimensions.py        # 35 dimension definitions (412 values)
│   ├── manifest.py          # Manifest generation
│   ├── naming.py            # Creative name generation
│   ├── index.py             # Gallery builder
│   └── status.py            # Progress reporting
├── docs/
│   ├── ROADMAP.md           # Project roadmap and experiments log
│   └── BATCH_EXECUTION.md   # Multi-session batch guide
└── outputs/                 # Generated designs
```

## Requirements

- Python 3.10+
- Claude Code (Claude Max subscription recommended for parallel agents)

## License

MIT
