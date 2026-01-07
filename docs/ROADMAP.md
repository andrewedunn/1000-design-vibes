# 1000 Design Vibes - Roadmap

## Completed

### v0.1 - API-Based Generation
- [x] Manifest generator with 30+ design dimensions
- [x] Anthropic API-based design generation
- [x] Rule-based creative naming

### v0.2 - Claude Code Subagent Architecture (2026-01-06)
- [x] Removed API dependency entirely
- [x] DESIGN_GUIDE.md for agent instructions
- [x] Parallel subagent generation via Task tool
- [x] Staging → validation → final workflow
- [x] Gallery index generation
- [x] Status command for progress tracking
- [x] Successfully generated 20 designs in ~7 minutes

---

### v0.3 - GitHub Ready (2026-01-07)
- [x] A/B tested Haiku vs Sonnet with loose guide (10 designs)
- [x] Fixed navigation bug (exact script in guide)
- [x] Generated 100 designs with Haiku
- [x] Master gallery index at outputs/index.html
- [x] Per-run index pages with stats and collapsible prompt
- [x] CLI command: `build-indexes`

**Findings:**
- Sonnet produces noticeably better quality designs
- Navigation script must be exact (vague instructions caused 50% failure)
- Haiku produces ~19KB avg files, acceptable but less polished
- Building to 1000 designs incrementally over weeks is sustainable

---

### v0.4 - Functional Direction & Layout Dimensions (2026-01-07)
- [x] Expanded `functional_direction` from 10 to **158 options** across 18 categories
- [x] Categories include: Standard Web, Education, Productivity, Communication, Media, Finance, Health, Travel, Social, Creative Tools, Food & Dining, Sports & Gaming, Events, Utility, Retro & Novelty, Professional, Personal, Data & Analytics
- [x] Added 4 layout structure dimensions: page_structure, navigation_pattern, hero_style, content_flow
- [x] Updated DESIGN_GUIDE_LOOSE.md to make functional_direction the PRIMARY driver
- [x] Total dimensions: 31 → 35, total values: ~200 → 412
- [x] GitHub Pages deployed at andrewedunn.github.io/1000-design-vibes

**Key Change:** functional_direction now determines page structure and required components, not just styling. Each direction specifies exact UI elements that must be present. Guide explicitly states "If your design doesn't clearly look like its functional_direction, you've failed the task."

---

## Planned

### Screenshot Generation
- Auto-generate preview thumbnails for gallery
- Use Playwright for headless rendering
- Include in gallery index cards

### Multi-Model Strategy
Based on A/B test results:
- Determine which model works best for different design types
- Potentially use Haiku for simpler designs (cost savings)
- Route complex designs to Sonnet

---

## Ideas (Future)

### Quality & Validation
- Design scoring/rating system
- Automated visual diff between designs
- Component coverage validation
- Accessibility auditing (axe-core)
- Lighthouse scores

### Export Formats
- Export design tokens to Tailwind config
- Generate React/Vue component libraries
- Figma tokens export

### Web UI
- Browser-based gallery with filters
- Side-by-side comparison view
- "Remix" feature for variations

---

## Experiments Log

| Date | Experiment | Designs | Model | Avg Size | Notes |
|------|------------|---------|-------|----------|-------|
| 2026-01-06 | full-test | 20 | Sonnet | ~90KB | Uniform layouts, ~1M tokens |
| 2026-01-06 | test-batch | 7 | Sonnet | ~59KB | Initial test |
| 2026-01-06 | ab-test-loose | 10 | Mixed | ~28KB | 5 Haiku + 5 Sonnet, 50% nav failure |
| 2026-01-07 | nav-test | 3 | Haiku | ~33KB | Fixed nav script, all passed |
| 2026-01-07 | batch-100 | 100 | Haiku | ~19KB | First large batch, 2.1MB total |

**Key Learnings:**
- Loose guide produces more varied layouts but smaller files
- Navigation must be an exact script, not vague instructions
- Haiku is ~3x cheaper but Sonnet quality is noticeably better
- Target: Use Sonnet for future batches, build to 1000 incrementally

---

## Resource Notes

### Token Usage (Claude Max 20x)
- ~40K tokens per design with strict guide
- Monthly budget: ~40-50M tokens
- Current capacity: ~600-800 designs/month
- Goal: Optimize to 1000+ designs/month

### Model Selection
- **Opus**: Complex debugging, architecture decisions
- **Sonnet**: Default for design generation (quality + speed balance)
- **Haiku**: Potential for simpler designs, 3x cheaper
