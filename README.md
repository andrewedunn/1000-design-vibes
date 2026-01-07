# 1000 Design Vibes

Generate unique, self-contained design system showcases. Each design is a single HTML file that's both a visual demo and a complete style guide.

## What is this?

This tool creates design systems from scratch by combining 30+ visual dimensions:
- UI paradigm (flat, material, glassmorphic, brutalist...)
- Design era (art deco, bauhaus, y2k, neo-brutalist...)
- Color theory (monochromatic, complementary, triadic...)
- Typography, spacing, shadows, and more

Each combination produces a unique design with its own personality, name, and complete component library.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/yourusername/1000-design-vibes
cd 1000-design-vibes
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Add your API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# Generate 20 unique design seeds
python design_vibes.py manifest --count 20 --name "my-first-batch"

# Create the HTML showcases (first 10)
python design_vibes.py generate \
  --manifest outputs/2025-01-06-my-first-batch/manifest.json \
  --start 1 --end 10

# Open the gallery
open outputs/2025-01-06-my-first-batch/index.html
```

## Commands

### `manifest` - Create design seeds

```bash
python design_vibes.py manifest --count 20 --name "test"
```

Creates a `manifest.json` with unique dimension combinations and creative names.

Options:
- `--count` - Number of designs to generate (default: 20)
- `--name` - Optional suffix for the output folder

### `generate` - Build HTML showcases

```bash
python design_vibes.py generate \
  --manifest outputs/2025-01-06-test/manifest.json \
  --start 1 --end 10
```

Creates `design-1.html` through `design-10.html` plus an `index.html` gallery.

Options:
- `--manifest` - Path to manifest.json
- `--start` - First design ID to generate
- `--end` - Last design ID to generate
- `--model` - LLM model to use (default: claude-sonnet-4-20250514)
- `--force` - Regenerate even if files exist

### `validate` - Check your output

```bash
python design_vibes.py validate --path outputs/2025-01-06-test/
```

Checks for missing files, invalid HTML, and other issues.

## Output Structure

```
outputs/
  2025-01-06-my-first-batch/
    manifest.json           # The design seeds
    index.html              # Gallery homepage
    designs/
      design-1.html         # Individual showcases
      design-2.html
      ...
```

Each HTML file is completely self-contained (except for Google Fonts) and includes:
- Full component library (buttons, forms, cards, etc.)
- CSS custom properties for all design tokens
- LLM-readable documentation for recreating the style
- Keyboard/touch navigation to browse designs

## Requirements

- Python 3.8+
- Anthropic API key (for Claude)

## License

MIT
