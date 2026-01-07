# Batch Execution Guide

How to execute large batches across multiple sessions.

---

## Overview

Large batches (500-760 designs) are generated from a single manifest over multiple sessions. Each session picks up where the last left off by checking which designs already exist.

---

## Starting a New Large Batch

### 1. Generate the Manifest

```bash
python design_vibes.py manifest --count 760 --name "the-thousand"
```

This creates:
```
outputs/2026-XX-XX-the-thousand/
  manifest.json      # 760 design specs
  .staging/          # Empty, for in-progress designs
  designs/           # Empty, for validated designs
```

### 2. First Session

Tell Claude:

```
Generate designs for outputs/2026-XX-XX-the-thousand

Start with designs 1-100. Use Sonnet model.
Check the manifest at outputs/2026-XX-XX-the-thousand/manifest.json
Write to .staging/, validate, move to designs/
```

### 3. End of Session

Before ending, run:
```bash
python design_vibes.py status outputs/2026-XX-XX-the-thousand
```

This shows:
- How many designs complete
- Which IDs are missing
- Suggested next batch range

---

## Resuming a Batch (Future Sessions)

### Check Progress First

```bash
python design_vibes.py status outputs/2026-XX-XX-the-thousand
```

Example output:
```
Batch: the-thousand
Total in manifest: 760
Completed: 200 (26%)
Missing: 560
Next suggested batch: 201-300

Missing IDs: 201, 202, 203, ... 760
```

### Resume Prompt for Claude

Copy this prompt, filling in the batch folder and range:

```
Resume generating designs for 1000 Design Vibes.

BATCH: outputs/2026-XX-XX-the-thousand
RANGE: designs 201-300 (or whatever status command suggests)
MODEL: Sonnet

Instructions:
1. Read DESIGN_GUIDE_LOOSE.md
2. Read manifest.json for the batch
3. For each design ID in range:
   - Skip if design-{id}.html already exists in designs/ or .staging/
   - Generate the design per the manifest spec
   - Write to .staging/design-{id}.html
4. After all agents complete, validate and move to designs/
5. Run: python design_vibes.py build-indexes
6. Run: python design_vibes.py status outputs/2026-XX-XX-the-thousand
```

---

## Session Checklist

### Starting a Session
- [ ] Check Anthropic usage limits are visible and have capacity
- [ ] Run `status` command to see progress
- [ ] Decide batch size (50-100 designs typical)

### During Generation
- [ ] Spawn agents in parallel (10-20 at a time)
- [ ] Monitor .staging/ folder for progress
- [ ] Watch for any agent failures

### Ending a Session
- [ ] Validate all designs in .staging/
- [ ] Move validated designs to designs/
- [ ] Run `build-indexes`
- [ ] Run `status` to confirm progress
- [ ] Commit and push to GitHub
- [ ] Update main index.html if needed (design count, batch description)

---

## Gallery Updates for In-Progress Batches

The main `index.html` should show progress:

```html
<span class="run-desc">760 designs in progress (200 complete)</span>
```

Update this after each session.

---

## Troubleshooting

### Agent failed to generate a design
Check the agent output, re-run just that design ID:
```
Generate design #247 from outputs/2026-XX-XX-the-thousand/manifest.json
```

### Design failed validation
Check the validation error, manually fix or regenerate.

### Lost track of progress
The `status` command always works - it just checks what files exist.

---

## Example Timeline

| Date | Session | Designs | Total |
|------|---------|---------|-------|
| Week 1 | Session 1 | 1-100 | 100 |
| Week 1 | Session 2 | 101-200 | 200 |
| Week 2 | Session 3 | 201-350 | 350 |
| Week 3 | Session 4 | 351-500 | 500 |
| Week 4 | Session 5 | 501-650 | 650 |
| Week 5 | Session 6 | 651-760 | 760 |

At ~100-150 designs per session, 760 designs takes 5-6 sessions over a few weeks.
