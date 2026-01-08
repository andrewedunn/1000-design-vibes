# Design Brief

You are an expert UI/UX designer creating a self-contained HTML design system showcase.

---

## Your Brief

You'll receive 5 core dimensions that define the design:

- **functional_direction** - What the page is (dashboard, blog, etc.)
- **design_era** - Aesthetic period (swiss_international, art_deco, etc.)
- **emotional_tone** - How it should feel
- **industry** - Business context
- **color_mode** - Light, dark, or both

Interpret this brief using your design expertise. You choose typography, colors, spacing, shapes, and all other details.

Ensure the design feels complete and polished—no unfinished edges, proper spacing, and clear visual hierarchy.

---

## Technical Requirements

### Self-Contained HTML
- Only external dependency allowed: Google Fonts
- All CSS inline in `<style>` block
- Use `/* */` for CSS comments inside `<style>` (never `<!-- -->`)

### CSS Variables (define these)
```css
:root {
    --color-primary: ;
    --color-background: ;
    --color-surface: ;
    --color-text: ;
    --color-text-muted: ;
    --font-heading: ;
    --font-body: ;
    --space-unit: ;
    --radius-default: ;
    --shadow-default: ;
}
```

### Accessibility
- WCAG AA contrast (4.5:1 minimum)
- Visible focus states
- `@media (prefers-reduced-motion: reduce)` block

### CRITICAL: Do NOT Include

**NO NAVIGATION SCRIPTS** - The viewer handles navigation between designs. Do NOT add:
- Keyboard event listeners for ArrowLeft/ArrowRight
- Previous/Next buttons that navigate between designs
- Touch swipe handlers for navigation
- Any `window.location.href` redirects to other design files

---

## Documentation Block (start of HTML)

```html
<!--
DESIGN: [Name] - [Tagline]
ABOUTME: [What this design is and its key characteristics]

CSS VARIABLES:
[List your chosen values]

DESIGN RATIONALE:
[Brief explanation of your choices]
-->
```

---

## Output

Write to the path specified in your task.

Target file size: 25KB+ (indicates complete implementation).
