# Generate Designs Skill

Generate design system HTML files using parallel Sonnet subagents.

## Usage

```
Generate designs for outputs/2026-01-07-batch
```

Or to resume a partial batch:
```
Resume generating designs for outputs/2026-01-07-batch, designs 51-100
```

## Workflow

1. **Load manifest**: Read `{path}/manifest.json`
2. **Check progress**: Skip designs already in `designs/` or `.staging/`
3. **Ensure staging exists**: Create `{path}/.staging/` if needed
4. **Spawn Sonnet agents**: Launch 10-20 design agents in parallel via Task tool
5. **Monitor completion**: Wait for agents to finish
6. **Validate outputs**: Check each `.staging/design-{n}.html` is valid
7. **Move to final**: Move valid designs from `.staging/` to `designs/`
8. **Log failures**: Write failures to `failures.json`
9. **Rebuild index**: Run `python design_vibes.py build-indexes`
10. **Report status**: Run `python design_vibes.py status --path {path}`
11. **Repeat**: Continue with next batch until all done

## Spawning Design Agents

For each pending design, spawn a Task with `subagent_type="general-purpose"` and `model="sonnet"`:

```
prompt: |
  Generate design #{id} for 1000 Design Vibes.

  Read the design guide at DESIGN_GUIDE_LOOSE.md and the manifest at {path}/manifest.json.

  The functional_direction "{functional_direction}" is PRIMARY - this MUST look like a {functional_direction}.

  Design: {name}
  Tagline: {tagline}

  Dimensions:
  {dimensions as YAML}

  Write to: {path}/.staging/design-{id}.html
  Navigation script: TOTAL={total}, CURRENT={id}
```

## Parallel Execution

- Spawn 10-20 agents at once using multiple Task tool calls in a single message
- Use `run_in_background: true` for async execution
- Wait for all to complete before spawning next batch
- Track which agents succeed/fail

## Validation

Before moving from staging to final, check:
- File size > 10KB (aim for 25KB+)
- Contains `<!DOCTYPE html>`
- Contains `<style>` and `</style>` tags
- Contains `ArrowRight` and `ArrowLeft` navigation handlers
- Navigation script has correct TOTAL and CURRENT values

## Handling Failures

If an agent fails:
1. Log the error to `failures.json`:
   ```json
   {"id": 7, "error": "Agent timed out", "attempts": 1, "timestamp": "..."}
   ```
2. Retry up to 2 times
3. After failures, skip and continue

## Status Reporting

After each batch, run the status command:
```bash
python design_vibes.py status --path {path}
```

This shows progress and suggests the next batch range with a resume prompt.

## Multi-Session Batches

For large batches across multiple sessions, see `docs/BATCH_EXECUTION.md`.

The key workflow:
1. Generate manifest once with full count (e.g., 760)
2. Each session, run `status` to see what's pending
3. Use the suggested resume prompt to continue
4. Repeat until complete
