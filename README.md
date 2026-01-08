# 1000 Design Vibes

Generate unique, self-contained design system showcases using Claude Code subagents. Each design is a single HTML file that's both a visual demo and a complete style guide.

**Live Gallery:** [andrewedunn.github.io/1000-design-vibes](https://andrewedunn.github.io/1000-design-vibes)

**Current Status:** 370 designs generated. 630 to go.

## What is this?

I was working on a project and hated the design because I'm a terrible designer. I asked Claude to generate a few options. That worked well enough that I wondered: what if I described a design using a bunch of different dimensions and let Claude go nuts?

Turns out you can. And once you have a few options why not make a thousand?

## The Plot Twist

I started with 35 dimensions—color theory, typography, visual density, cultural influence, you name it. Figured more control meant better results. I was wrong.

Randomly combining 35 dimensions produces chaos. "Brutalist + playful + corporate + neon + Japanese minimalist" is not a coherent design brief.

**The insight:** Less is more. Give the LLM 5 core constraints and let it be the expert designer.

| Approach | Result |
|----------|--------|
| 35 random dimensions | Wacky, conflicting designs |
| 5 core dimensions | Coherent, polished designs |

The 5 dimensions that matter:
- **functional_direction** - What the page IS (dashboard, blog, quiz app, Windows 95 throwback)
- **design_era** - Aesthetic period (swiss international, art deco, y2k, neo-brutalist)
- **emotional_tone** - How it should feel (calm, energetic, mysterious, playful)
- **industry** - Business context (tech, healthcare, entertainment, finance)
- **color_mode** - Light, dark, or both

Everything else—typography, spacing, colors, shapes—the agent picks to support these five.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/andrewedunn/1000-design-vibes
cd 1000-design-vibes
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Generate 20 designs with 5 core dimensions (recommended)
python design_vibes.py manifest --count 20 --name "my-batch" --core-only

# Or go nuts with all 35 dimensions
python design_vibes.py manifest --count 20 --name "my-batch"

# Generate designs using Claude Code
# Open in Claude Code and say: "Generate designs for outputs/2026-01-07-my-batch"
```

## Commands

### `manifest` - Create design seeds

```bash
# Recommended: 5 core dimensions, agent picks the rest
python design_vibes.py manifest --count 100 --name "batch1" --core-only

# All 35 dimensions (for experimentation)
python design_vibes.py manifest --count 100 --name "batch1"
```

Options:
- `--count` - Number of designs to generate (default: 20)
- `--name` - Suffix for the output folder
- `--core-only` - Only specify 5 core dimensions, let agent choose the rest

### `status` - Check progress

```bash
python design_vibes.py status --path outputs/2026-01-07-my-batch
```

Shows completed, in-progress, and pending designs. Also provides a resume prompt for Claude.

### `build-indexes` - Rebuild batch galleries

```bash
python design_vibes.py build-indexes
```

Regenerates the index.html for each batch with updated stats and design cards.

### `build-viewer` - Rebuild main gallery

```bash
python design_vibes.py build-viewer
```

Regenerates the main index.html with all designs from all batches.

### `validate` - Check for issues

```bash
# Check for CSS comment issues and other problems
python design_vibes.py validate --path outputs/2026-01-07-my-batch

# Auto-fix fixable issues
python design_vibes.py validate --path outputs/2026-01-07-my-batch --fix
```

## Generating Designs with Claude Code

1. Create a manifest:
   ```bash
   python design_vibes.py manifest --count 100 --name "my-batch" --core-only
   ```

2. Open the project in Claude Code and run:
   ```
   Generate designs for outputs/2026-01-07-my-batch
   ```

3. Claude Code reads the manifest and spawns Sonnet subagents in parallel to generate each design. Designs are validated and moved from `.staging/` to `designs/`.

4. Check progress:
   ```bash
   python design_vibes.py status --path outputs/2026-01-07-my-batch
   ```

5. Rebuild the galleries:
   ```bash
   python design_vibes.py build-indexes
   python design_vibes.py build-viewer
   ```

For large batches (500+) executed over multiple sessions, see [docs/BATCH_EXECUTION.md](docs/BATCH_EXECUTION.md).

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

## Project Structure

```
├── design_vibes.py              # CLI entry point
├── DESIGN_GUIDE_MINIMAL.md      # Agent instructions (5 core dimensions)
├── DESIGN_GUIDE_LOOSE.md        # Agent instructions (all dimensions)
├── index.html                   # Main gallery (generated)
├── about.html                   # Project info and run list
├── all-designs.json             # All designs metadata (generated)
├── src/
│   ├── dimensions.py            # 35 dimension definitions (412 values)
│   ├── manifest.py              # Manifest generation
│   ├── naming.py                # Creative name generation
│   ├── index.py                 # Batch gallery builder
│   ├── viewer.py                # Main gallery builder
│   ├── validate.py              # Design validation
│   └── status.py                # Progress reporting
├── docs/
│   ├── ROADMAP.md               # Project roadmap and experiments log
│   └── BATCH_EXECUTION.md       # Multi-session batch guide
└── outputs/                     # Generated designs
```

## The 35 Dimensions (if you want to go nuts)

You can still use all 35 dimensions if you want to experiment:

- **Visual Style**: UI Paradigm, Design Era, Density
- **Color System**: Color Theory, Temperature, Saturation, Contrast, Palette Mood, Light/Dark Mode
- **Typography**: Heading Font Class, Body Font Class, Scale Ratio, Case Treatment, Letter Spacing, Line Height
- **Shape & Space**: Corner Radius, Spacing Base, Border Style, Shadow Style, Container Style
- **Layout**: Grid System, Alignment, Hierarchy Approach, Page Structure, Navigation Pattern
- **Texture & Detail**: Surface Texture, Gradient Usage, Icon Style
- **Context**: Industry, Target Audience, Emotional Tone, Cultural Influence, Functional Direction (158 options!)

412 possible values total. More combinations than I'll ever generate.

## Requirements

- Python 3.10+
- Claude Code (Claude Max subscription recommended for parallel agents)

## License

MIT
