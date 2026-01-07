# 1000 Design Vibes - Architecture Design

## Overview

A CLI tool to generate unique, self-contained design system showcases. Each design is an HTML file that serves as both a visual demo and LLM-readable documentation.

## Goals

1. Generate 1000 unique design specifications ("seeds") across 30+ dimensions
2. Create self-contained HTML showcases from those seeds
3. Make it easy for others to fork and generate their own design libraries
4. Publish on GitHub with GitHub Pages hosting

## Architecture

### CLI Commands

```bash
python design_vibes.py manifest --count 20 --name "test"
python design_vibes.py generate --manifest <path> --start 1 --end 10
python design_vibes.py validate --path <output-folder>
```

**manifest** - Creates design seeds with unique dimension combinations + names/taglines

**generate** - Creates HTML showcase pages from manifest entries, auto-rebuilds index

**validate** - Checks manifest integrity, file completeness, basic HTML validation

### Project Structure

```
1000-design-vibes/
├── design_vibes.py          # CLI entry point
├── src/
│   ├── __init__.py
│   ├── manifest.py          # Manifest generation logic
│   ├── generator.py         # HTML page generation
│   ├── index.py             # Gallery index builder
│   ├── validator.py         # Validation checks
│   ├── dimensions.py        # All dimension definitions
│   ├── naming.py            # Name generation (Claude + fallback)
│   └── utils.py             # Shared helpers
├── templates/
│   └── design_prompt.md     # Prompt template for design generation
├── outputs/                  # Generated runs (gitignored)
├── docs/
│   ├── plans/               # Design documents
│   ├── ROADMAP.md           # Future enhancements
│   └── DIMENSIONS.md        # Dimension reference
├── .env                      # API keys (gitignored)
├── .env.example              # Template for .env
├── .gitignore
├── requirements.txt
├── CLAUDE.md
└── README.md
```

### Output Folder Structure

Each run creates a date-stamped folder:

```
outputs/
  2025-01-06-test/
    manifest.json
    designs/
      design-1.html
      design-2.html
      ...
    index.html
```

## Key Decisions

### Language: Python

- Most accessible for contributors
- Great CLI tooling (Click, Rich)
- PRD examples already in Python

### Dependencies

```
anthropic>=0.18.0    # Claude API client
click>=8.0           # CLI framework
rich>=13.0           # Pretty terminal output
python-dotenv>=1.0   # Load .env file
```

### Model Configuration

- Default: claude-sonnet-4-20250514 (balance of quality/speed/cost)
- Configurable via `--model` flag
- Future: multi-provider support (see ROADMAP.md)

### Name Generation

1. Primary: Claude API generates creative names from dimensions
2. Fallback: Rule-based generation if no API key
3. Names generated during manifest creation (fixed identity)

### HTML Generation Flow

1. Load design entry from manifest
2. Build prompt from template + dimensions
3. Call Claude API
4. Save as design-{id}.html
5. Quick validation
6. After batch: regenerate index.html

### Resume Behavior

- `generate` skips already-existing files by default
- Use `--force` to regenerate

## Security

- `.env` contains API keys, gitignored
- `.env.example` committed as template
- `outputs/` gitignored (users generate their own)

## Data Flow

```
dimensions.py (definitions)
        │
        ▼
manifest command ──► manifest.json (seeds + names)
        │                   │
        │                   ▼
        │           generate command ──► design-{n}.html
        │                   │
        │                   ▼
        │              index.html (auto-rebuilt)
        │                   │
        ▼                   ▼
validate command ◄──────────┘
```

## Future Enhancements

See docs/ROADMAP.md for:
- Multi-provider support (OpenAI, Ollama, etc.)
- Web UI for browsing/generating
- Constraint rules between dimensions
- Accessibility auditing in validation
- Screenshot generation for index cards
