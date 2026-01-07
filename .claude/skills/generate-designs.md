# Generate Designs Skill

Generate design system HTML files using parallel subagents.

## Usage

```
/generate-designs outputs/2026-01-06-batch
```

## Workflow

1. **Load manifest**: Read `{path}/manifest.json`
2. **Check progress**: Identify which designs are pending (not in `designs/` or `.staging/`)
3. **Ensure staging exists**: Create `{path}/.staging/` if needed
4. **Spawn agents**: Launch 3-5 design agents in parallel via Task tool
5. **Monitor completion**: Wait for agents to finish
6. **Validate outputs**: Check each `.staging/design-{n}.html` is valid
7. **Move to final**: Move valid designs from `.staging/` to `designs/`
8. **Log failures**: Write failures to `failures.json`
9. **Rebuild index**: Call the index builder
10. **Report status**: Show completion summary
11. **Repeat**: Continue with next batch until all done

## Spawning Design Agents

For each pending design, spawn a Task with `subagent_type="general-purpose"`:

```
prompt: |
  You are generating design #{id} for the 1000 Design Vibes project.

  First, read the DESIGN_GUIDE.md file at the project root for complete instructions.

  Then generate a complete HTML file for this design:

  Name: {name}
  Tagline: {tagline}

  Dimensions:
  {dimensions as YAML}

  Write the output to: {path}/.staging/design-{id}.html

  The file must be complete and self-contained. Follow DESIGN_GUIDE.md exactly.
```

## Parallel Execution

- Spawn 3-5 agents at once using multiple Task tool calls in a single message
- Wait for all to complete before spawning next batch
- Track which agents succeed/fail

## Handling Failures

If an agent fails:
1. Log the error to `failures.json`:
   ```json
   {"id": 7, "error": "Agent timed out", "attempts": 1, "timestamp": "..."}
   ```
2. Retry up to 3 times
3. After 3 failures, skip and continue

## Validation

Before moving from staging to final:
- File exists and is not empty
- Contains `<!DOCTYPE html>`
- Contains the design name
- Contains `<style>` and `</style>` tags

## Index Rebuild

After each batch:
```python
from src.index import build_index
build_index(output_path, manifest)
```

## Status Reporting

After completion:
```
Batch: 2026-01-06-mybatch
Completed: 47/100
Failed: 3
Remaining: 50

Failed designs: #12, #34, #67
```
