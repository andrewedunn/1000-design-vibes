# Agent Architecture Design

## Overview

Generate 1000 unique design system showcases using Claude Code subagents instead of API calls. Each design agent runs with fresh context, producing higher quality output than prompt-based API generation.

## Architecture

### Components

**1. DESIGN_GUIDE.md**
- Static instruction file at project root
- Contains all HTML structure, component specs, CSS conventions
- Read fresh by each design agent
- Single source of truth for design requirements

**2. Orchestrator (Claude Code skill)**
- Invoked via `/generate-designs` or similar
- Reads manifest to find pending designs
- Spawns 3-5 design agents in parallel via Task tool
- Monitors completion, retries failures (max 3 attempts)
- Moves successful designs from staging to final folder
- Rebuilds index after each batch
- Logs failures to `failures.json`

**3. Design Agent (Task subagent)**
- Stateless, receives single design spec
- Reads DESIGN_GUIDE.md for instructions
- Writes HTML to `.staging/design-{n}.html`
- Returns success/failure status

### File Structure

```
1000-design-vibes/
├── design_vibes.py          # CLI: manifest, status commands
├── DESIGN_GUIDE.md          # Agent instructions
├── src/
│   ├── dimensions.py        # Dimension definitions
│   ├── manifest.py          # Manifest generation
│   ├── naming.py            # Rule-based naming only
│   ├── index.py             # Gallery builder
│   └── status.py            # Status reporting
├── outputs/
│   └── {date}-{name}/
│       ├── manifest.json
│       ├── index.html
│       ├── failures.json    # Failed designs log
│       ├── .staging/        # In-progress designs
│       └── designs/         # Completed designs
└── .claude/
    └── skills/
        └── generate-designs.md  # Orchestrator skill
```

## Workflow

1. **Create manifest**: `python design_vibes.py manifest --count 1000 --name batch1 --no-api`
2. **Generate designs**: Run `/generate-designs outputs/2026-01-06-batch1`
3. **Monitor progress**: `python design_vibes.py status --path outputs/2026-01-06-batch1`
4. **Review failures**: Check `failures.json`, manually retry or fix

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Parallelism | 3-5 agents | Balance speed/stability, can ramp up |
| Instructions | File-based | Single source of truth, smaller prompts |
| Output | Staging folder | Quality checkpoint before acceptance |
| Failures | Auto-retry 3x | Most failures transient, log persistent ones |

## Removed Components

- `src/generator.py` - API-based generation (replaced by agents)
- `templates/design_prompt.md` - API prompt template
- API code in `naming.py` - Keep only rule-based fallback

## CLI Commands

```bash
# Create a manifest with unique design specs
python design_vibes.py manifest --count 1000 --name mybatch --no-api

# Check generation progress
python design_vibes.py status --path outputs/2026-01-06-mybatch
```

## Success Criteria

- [ ] Can generate 10 designs via agents without errors
- [ ] Staging → final move works correctly
- [ ] Index rebuilds after each batch
- [ ] Failures logged and retriable
- [ ] Quality matches or exceeds manual Claude Code generation
