# Design System Page Generator

You are generating design #{id} from a design library.

## Design Specification

**Name:** {name}
**Tagline:** {tagline}

### Dimensions

{dimensions_formatted}

## Requirements

Generate a complete, self-contained HTML file that serves as both:
1. A visual showcase of this design system
2. LLM-readable documentation so another AI can replicate this style

### File Structure

The HTML file must follow this exact structure:

```html
<!--
================================================================================
DESIGN SYSTEM: {name}
================================================================================

ABOUTME: [One line describing what this design IS]
ABOUTME: [Key visual characteristics - 3-4 traits]

================================================================================
FOR AI ASSISTANTS - HOW TO USE THIS DESIGN SYSTEM
================================================================================

[Comprehensive documentation including:]
- Quick Start CSS variables block
- Aesthetic philosophy (4 core principles)
- Color system table with hex, usage, contrast ratios
- Typography table with all sizes/weights
- Spacing system
- Component recipes (buttons, cards, inputs with full CSS)
- DO's and DON'Ts specific to THIS design
- Accessibility notes
- Best for / Avoid using for

================================================================================
-->
<!DOCTYPE html>
...rest of file
```

### Required Components

**Tier 1 (Must Have):**
- Buttons: Primary, Secondary, Outline, Ghost, Destructive (all states)
- Text inputs: Default, With label, With error, Disabled
- Cards: Basic, With image, Clickable
- Typography: h1-h6, body, small, caption, link
- Navigation: Header nav with mobile menu

**Tier 2 (Should Have):**
- Select/Dropdown
- Checkbox and Radio
- Toggle/Switch
- Badge/Tag
- Avatar
- Alert/Toast (Info, Success, Warning, Error)
- Modal/Dialog
- Tabs
- Table

**Tier 3 (Pick 3+ Mobile Components):**
- Bottom navigation
- Floating action button (FAB)
- Bottom sheet
- Skeleton loader
- Segmented control
- Touch-optimized list

### Showcase Sections

Include these sections in order:
1. Hero with design name and visual representation
2. Color palette with swatches and hex values
3. Typography specimen (all heading levels, body text)
4. Spacing scale visualization
5. Component gallery with all variants and states
6. Example layouts (hero section, feature grid, form, dashboard card, mobile screen)
7. Design tokens reference table

### Technical Requirements

1. **Self-contained**: Only external dependency is Google Fonts CDN
2. **CSS Variables**: All design decisions as custom properties in :root
3. **Accessible**: WCAG AA contrast, visible focus indicators, 44px touch targets
4. **Responsive**: Mobile-first, works from 375px to 1440px+
5. **Reduced motion**: Include prefers-reduced-motion media query

### CSS Architecture

Use this naming convention:
```css
:root {{
  /* Colors */
  --color-primary: ;
  --color-primary-hover: ;
  --color-secondary: ;
  --color-background: ;
  --color-surface: ;
  --color-text: ;
  --color-text-muted: ;
  --color-border: ;
  --color-error: ;
  --color-success: ;
  --color-warning: ;

  /* Typography */
  --font-heading: ;
  --font-body: ;
  --text-xs: ;
  --text-sm: ;
  --text-base: ;
  --text-lg: ;
  --text-xl: ;
  --text-2xl: ;
  --text-3xl: ;
  --text-4xl: ;

  /* Spacing */
  --space-xs: ;
  --space-sm: ;
  --space-md: ;
  --space-lg: ;
  --space-xl: ;
  --space-2xl: ;

  /* Shadows, Radii, Borders, Transitions */
}}
```

### Navigation Script

Include this at the end of the body:
```javascript
(function() {{
  const TOTAL = {total_designs};
  const CURRENT = {id};

  document.addEventListener('keydown', (e) => {{
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowRight') window.location.href = `design-${{CURRENT === TOTAL ? 1 : CURRENT + 1}}.html`;
    if (e.key === 'ArrowLeft') window.location.href = `design-${{CURRENT === 1 ? TOTAL : CURRENT - 1}}.html`;
    if (e.key === 'Escape') window.location.href = 'index.html';
  }});

  let startX = 0;
  document.addEventListener('touchstart', e => startX = e.touches[0].clientX, {{passive: true}});
  document.addEventListener('touchend', e => {{
    const diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) {{
      window.location.href = diff > 0
        ? `design-${{CURRENT === TOTAL ? 1 : CURRENT + 1}}.html`
        : `design-${{CURRENT === 1 ? TOTAL : CURRENT - 1}}.html`;
    }}
  }}, {{passive: true}});
}})();
```

### Machine-Readable Data

Include this in the <head>:
```html
<script type="application/json" id="design-system-data">
{{
  "id": {id},
  "name": "{name}",
  "version": "1.0.0",
  "dimensions": {dimensions_json},
  "tokens": {{ /* extracted from CSS */ }}
}}
</script>
```

## Dimension Interpretation Guide

Based on the dimensions, implement:

- **ui_paradigm**: The core visual treatment (flat=no shadows, material=layered shadows, glassmorphic=blur+transparency, brutalist=raw borders, etc.)
- **design_era**: Historical influence on patterns and motifs
- **color_theory + color_temperature + color_saturation**: Determines the palette
- **type_heading_class + type_body_class**: Pick appropriate Google Fonts
- **type_scale_ratio**: Mathematical sizing relationship
- **corner_radius**: Border radius philosophy throughout
- **shadow_style**: How shadows are applied (or not)
- **industry + target_audience + emotional_tone**: Contextual appropriateness

## Output

Generate the complete HTML file. Do not truncate. Include:
- Full HTML comment documentation block (this is critical for LLM consumption)
- Complete CSS with all variables and component styles
- All showcase sections with working component examples
- Navigation JavaScript
- Structured JSON data block

The file should be immediately usable - opening it in a browser shows a complete design system showcase.
