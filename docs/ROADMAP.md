# Roadmap

Future enhancements and ideas for 1000 Design Vibes.

## Planned

### Multi-Provider Support
- Add `--provider` flag to support different LLM backends
- Providers to consider: OpenAI, Anthropic, Ollama (local), Together.ai
- Abstract LLM calls behind a clean interface
- Config file option so users don't need to pass flags every time

```bash
# Future syntax
python design_vibes.py generate --provider openai --model gpt-4o ...
python design_vibes.py generate --provider ollama --model llama3 ...
```

### Screenshot Generation
- Auto-generate preview screenshots for each design
- Use Playwright or similar for headless rendering
- Include thumbnails in the gallery index

## Ideas (Not Yet Planned)

### Web UI
- Browser-based interface for exploring designs
- Filter/search by dimensions
- Side-by-side comparison view

### Dimension Constraints
- Soft rules between dimensions (e.g., "glassmorphic prefers cool colors")
- Weighted sampling to favor certain aesthetic combinations
- Exclusion rules to prevent clashing combinations

### Enhanced Validation
- Accessibility auditing (axe-core integration)
- Contrast ratio checking
- Lighthouse scores

### Export Formats
- Export design tokens to various formats (Tailwind config, CSS-in-JS, Figma tokens)
- Generate React/Vue/Svelte component libraries from designs

### Community Features
- Gallery of community-generated designs
- Voting/rating system
- "Remix" feature to create variations of existing designs

## Known Limitations

- Generation is sequential (parallel would hit rate limits)
- No automated accessibility testing yet
- Index thumbnails are color swatches, not actual screenshots

## Contributing Ideas

Have an idea? Open an issue or add it here via PR!
