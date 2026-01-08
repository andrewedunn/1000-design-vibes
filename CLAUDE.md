# CLAUDE.md

Instructions for AI assistants working on this project.

## Project Overview

1000 Design Vibes generates unique, self-contained design system showcases. Each design is an HTML file that works as both a visual demo and LLM-readable documentation.

**Current state:** 620 designs across 12 batches. Goal is 1000.

**Key insight**: Less is more. Use `--core-only` to specify just 5 dimensions and let the agent pick the rest. This produces more coherent designs than specifying all 35 dimensions randomly.

## Quick Reference

```bash
# Create a manifest with 5 core dimensions (recommended)
python design_vibes.py manifest --count 100 --name "batch1" --core-only

# Or use all 35 dimensions (for experimentation)
python design_vibes.py manifest --count 100 --name "batch1"

# Check progress (shows resume prompt for incomplete batches)
python design_vibes.py status --path outputs/2026-01-07-batch1

# Validate designs for CSS issues
python design_vibes.py validate --path outputs/2026-01-07-batch1 --fix

# Rebuild viewer after generation
python design_vibes.py build-viewer

# Browse designs
open index.html
```

## Generating Designs

When asked to generate designs:

1. **Read the manifest** to find design specs
2. **Check what exists** - skip designs already in `designs/` or `.staging/`
3. **Spawn Sonnet agents in parallel** (10-20 at a time) using Task tool
4. Each agent reads `DESIGN_GUIDE_MINIMAL.md` (for core-only) or `DESIGN_GUIDE_LOOSE.md` and writes to `.staging/`
5. **Validate outputs** using `python design_vibes.py validate --path {batch} --fix`
6. **Move valid designs** from `.staging/` to `designs/`
7. Run `build-viewer` to update the viewer
8. **Update about.html** with the new batch (see Post-Batch Checklist below)
9. Repeat until batch complete

### Spawning a Design Agent (Core-Only)

```
Task tool with subagent_type="general-purpose", model="sonnet":

Generate design #{id} for 1000 Design Vibes.

Read the design guide at DESIGN_GUIDE_MINIMAL.md and manifest for this batch.

Design: {name}
Tagline: {tagline}

Core Dimensions:
  functional_direction: {value}  <- PRIMARY: this MUST look like a {value}
  design_era: {value}
  emotional_tone: {value}
  industry: {value}
  color_mode: {value}

You choose all other design details (typography, colors, spacing, etc.) to create a coherent design.

Write to: outputs/{batch}/.staging/design-{id}.html

IMPORTANT: Do NOT add navigation scripts (ArrowLeft/ArrowRight handlers). The viewer handles navigation.
```

### Validation Checklist

Before moving from staging:
- File size > 10KB (aim for 25KB+)
- Contains `<!DOCTYPE html>`
- Contains `<style>` block with proper CSS comments (/* */, not <!-- -->)
- **NO navigation scripts** (ArrowLeft/ArrowRight handlers) - viewer handles this
- Clearly reflects the functional_direction

Run `python design_vibes.py validate --path {batch} --fix` to auto-fix CSS comment issues.

**IMPORTANT:** After moving designs from staging, always run validation AND check for navigation scripts:
```bash
python design_vibes.py validate --path {batch} --fix
# Then strip any navigation scripts (they break the viewer):
grep -l "ArrowRight" outputs/{batch}/designs/design-*.html
# If any found, remove the keydown event listeners
```

### Post-Batch Checklist

After completing a batch, update the following:

1. **about.html** - The "What the heck is this?" page
   - Update the stats row at the top (total designs, batch count, remaining)
   - Add the new batch to the "Design Runs" list (click to expand with approach info)

2. **CLAUDE.md** - This file
   - Update the "Current state" line with new totals

3. **Rebuild viewer**
   ```bash
   python design_vibes.py build-viewer
   ```

## Multi-Session Batch Execution

For large batches (500+) executed over multiple sessions, see `docs/BATCH_EXECUTION.md`.

The `status` command shows:
- Progress (completed/staging/pending)
- Suggested next batch range
- Ready-to-copy resume prompt

## Architecture

### Key Files

| File | Purpose |
|------|---------|
| `design_vibes.py` | CLI entry point |
| `DESIGN_GUIDE_MINIMAL.md` | Agent instructions for 5 core dimensions (recommended) |
| `DESIGN_GUIDE_LOOSE.md` | Agent instructions for all 35 dimensions |
| `src/dimensions.py` | 35 dimensions, 412 values, 158 functional directions |
| `src/manifest.py` | Manifest generation with --core-only support |
| `src/naming.py` | Creative name generation |
| `src/viewer.py` | Main viewer/gallery builder |
| `src/validate.py` | Design validation and CSS fix |
| `src/status.py` | Progress reporting with resume prompts |

### Output Structure

```
outputs/{date}-{name}/
  manifest.json     # Design seeds
  failures.json     # Failed attempts (if any)
  .staging/         # In-progress designs
  designs/
    design-1.html   # Completed designs
    design-2.html
    ...
```

## Key Design Decisions

1. **5 core dimensions** - `--core-only` produces best results; agent picks coherent supporting choices
2. **Claude Code Sonnet agents** - Not Haiku or API; Sonnet produces best quality
3. **Self-contained HTML** - Only Google Fonts as external dependency
4. **Date-stamped outputs** - Each run is isolated
5. **Staging folder** - Validate before accepting
6. **Parallel agents** - 10-20 at a time for speed
7. **Functional direction is PRIMARY** - The `functional_direction` dimension drives page structure and required components

## Code Style

- All Python files start with 2-line `# ABOUTME:` comment
- Match existing patterns
- Keep dependencies minimal

## Key Docs

| Doc | Purpose |
|-----|---------|
| [about.html](about.html) | Public "What is this?" page - **UPDATE AFTER EACH BATCH** |
| [README.md](README.md) | Full usage docs with the evolution story |
| [ROADMAP.md](docs/ROADMAP.md) | Version history, experiments log, future plans |
| [BATCH_EXECUTION.md](docs/BATCH_EXECUTION.md) | Multi-session batch guide with resume instructions |
| [DESIGN_GUIDE_MINIMAL.md](DESIGN_GUIDE_MINIMAL.md) | Agent instructions for core-only (recommended) |
| [DESIGN_GUIDE_LOOSE.md](DESIGN_GUIDE_LOOSE.md) | Agent instructions for all 35 dimensions |
