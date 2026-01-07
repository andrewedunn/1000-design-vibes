# CLAUDE.md

Instructions for AI assistants working on this project.

## Project Overview

1000 Design Vibes is a CLI tool that generates unique, self-contained design system showcases. Each design is an HTML file that works as both a visual demo and LLM-readable documentation.

## Quick Start

```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your ANTHROPIC_API_KEY

# Generate a manifest with 20 designs
python design_vibes.py manifest --count 20 --name "test"

# Generate HTML files for designs 1-10
python design_vibes.py generate --manifest outputs/YYYY-MM-DD-test/manifest.json --start 1 --end 10

# Validate the output
python design_vibes.py validate --path outputs/YYYY-MM-DD-test/
```

## Architecture

See [docs/plans/2025-01-06-architecture-design.md](docs/plans/2025-01-06-architecture-design.md) for the full design document.

### Key Files

| File | Purpose |
|------|---------|
| `design_vibes.py` | CLI entry point |
| `src/dimensions.py` | All 30+ dimension definitions |
| `src/manifest.py` | Manifest generation logic |
| `src/generator.py` | HTML page generation |
| `src/naming.py` | Name generation (Claude + fallback) |
| `src/index.py` | Gallery index builder |
| `src/validator.py` | Validation checks |
| `templates/design_prompt.md` | Prompt template for HTML generation |

### Commands

- **manifest**: Creates design seeds (dimension combos + names)
- **generate**: Creates HTML pages from seeds, auto-rebuilds index
- **validate**: Checks output for completeness and validity

## Development Guidelines

### Code Style

- All files start with 2-line `// ABOUTME:` comment (or `# ABOUTME:` for Python)
- Match existing patterns in the codebase
- Keep dependencies minimal

### Testing

```bash
# Run tests (when we have them)
pytest

# Quick manual test
python design_vibes.py manifest --count 5 --name "dev-test"
```

### Key Design Decisions

1. **Self-contained HTML** - No build step, only Google Fonts as external dep
2. **Date-stamped outputs** - Each run is isolated in its own folder
3. **Resume-friendly** - generate skips existing files unless --force
4. **Claude for names** - Falls back to rule-based if no API key

## Key Docs

- [Architecture Design](docs/plans/2025-01-06-architecture-design.md)
- [Roadmap](docs/ROADMAP.md)
- [Dimension Reference](docs/DIMENSIONS.md) (auto-generated)

## PRD Reference

The original requirements are in three files:
- `01-manifest-generator-prd.md` - Manifest structure and generation
- `02-design-page-generator-prd.md` - HTML page requirements
- `03-prompt-templates.md` - Prompts for LLM generation
