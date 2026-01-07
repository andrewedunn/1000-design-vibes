# Design Guide for 1000 Design Vibes

This document provides complete instructions for generating a self-contained HTML design showcase. Read this fully before generating any design.

---

## Your Task

Generate a complete, self-contained HTML file that:
1. Showcases a unique design system based on the provided dimensions
2. Contains embedded LLM-readable documentation
3. Works with zero external dependencies (except Google Fonts)
4. Is immediately usable in a browser

---

## File Structure

Every design file follows this exact structure:

```html
<!--
================================================================================
DESIGN SYSTEM: [Name]
================================================================================

ABOUTME: [One-line description]
ABOUTME: [Key characteristics]

================================================================================
FOR AI ASSISTANTS
================================================================================

This design system is optimized for LLM consumption. Follow these rules precisely.

## QUICK START
[CSS variable block to copy]

## AESTHETIC PRINCIPLES
- [4-5 principles specific to this design]

## COLOR SYSTEM
| Token | Value | Usage |
|-------|-------|-------|
| --color-primary | #XXXXXX | [usage] |
[etc.]

## TYPOGRAPHY
Font Stack: [exact fonts]
[Typography table]

## SPACING SYSTEM
Base Unit: [Xpx]
[Spacing table]

## COMPONENT PATTERNS
[Detailed patterns for buttons, cards, inputs, etc.]

## SHADOWS / BORDERS / RADII
[Tables with values]

## DO's and DON'Ts
[5 specific do's and 5 don'ts for this design]

## ACCESSIBILITY
[Contrast ratios, focus indicators, touch targets]

================================================================================
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Name] - Design System</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=[fonts]&display=swap" rel="stylesheet">

    <!-- Design System Data -->
    <script type="application/json" id="design-system-data">
    {
        "name": "[Name]",
        "version": "1.0.0",
        "dimensions": { /* from manifest */ },
        "tokens": { /* all design tokens */ }
    }
    </script>

    <style>
        :root {
            /* All CSS variables */
        }

        /* Base styles */
        /* Component styles */
        /* Responsive styles */

        @media (prefers-reduced-motion: reduce) {
            * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
        }
    </style>
</head>
<body>
    <!-- Showcase sections -->

    <script>
        // Navigation JavaScript
    </script>
</body>
</html>
```

---

## Required Components

### Tier 1: Essential (must have all)

| Component | Variants | States |
|-----------|----------|--------|
| **Buttons** | Primary, Secondary, Outline, Ghost, Destructive | Hover, Active, Disabled, Focus |
| **Text inputs** | Default, With label, With error, Disabled | Focus, Error, Success |
| **Cards** | Basic, With image, Clickable | Hover, Selected |
| **Typography** | h1-h6, body, small, caption, link | — |

### Tier 2: Important (should have most)

| Component | Variants |
|-----------|----------|
| **Select/Dropdown** | Default |
| **Checkbox** | Default, Checked |
| **Radio** | Default, Radio group |
| **Toggle/Switch** | On, Off |
| **Badge/Tag** | Various colors |
| **Avatar** | Image, Initials |
| **Alert** | Info, Success, Warning, Error |
| **Tabs** | Horizontal |

### Tier 3: Mobile (must have at least 3)

| Component | Description |
|-----------|-------------|
| **Bottom nav** | Mobile app navigation |
| **FAB** | Floating action button |
| **Skeleton loader** | Content placeholder |
| **Card list** | Scrollable feed |
| **Segmented control** | iOS-style toggle |

---

## Showcase Page Sections

Include these sections in order:

1. **Hero** - Design name, one-sentence description
2. **Color Palette** - All colors as swatches with hex values
3. **Typography Specimen** - All heading levels, body text, weights
4. **Component Gallery** - All components with variants and states
5. **Example Layouts** - Hero section, form, dashboard card, mobile screen
6. **Design Tokens Reference** - Table of all CSS variables

---

## Dimension Interpretation

### UI Paradigm

| Value | Implementation |
|-------|----------------|
| `flat` | No shadows, no gradients, solid colors, clean edges |
| `material` | Layered surfaces, subtle shadows, elevation system |
| `neumorphic` | Soft shadows both directions, monochromatic, extruded look |
| `glassmorphic` | `backdrop-filter: blur()`, transparency, border glow |
| `brutalist` | Raw borders, stark contrast, visible structure |
| `claymorphic` | Soft, inflated, puffy elements with colored shadows |
| `skeuomorphic` | Textures, gradients, real-world material mimicry |
| `organic` | Flowing blob shapes, irregular curves |
| `editorial` | Strong typography hierarchy, magazine-like layout |

### Design Era

| Value | Implementation |
|-------|----------------|
| `bauhaus` | Primary colors, geometric shapes, functional |
| `art_deco` | Gold accents, symmetry, chevrons, glamour |
| `mid_century_modern` | Organic curves, wood tones, atomic age |
| `swiss_international` | Grid-based, Helvetica-like fonts, objective |
| `memphis` | Colorful, geometric patterns, playful |
| `y2k` | Chrome, gradients, tech-optimism |
| `neo_brutalist` | Bold borders, raw HTML aesthetic |
| `scandinavian_modern` | Minimal, light, natural materials |

### Color Theory

| Value | Implementation |
|-------|----------------|
| `monochromatic` | One hue, vary lightness (e.g., `hsl(220, 60%, 20-80%)`) |
| `complementary` | Two hues 180° apart (e.g., blue + orange) |
| `analogous` | Three adjacent hues (e.g., blue + teal + green) |
| `triadic` | Three hues 120° apart (e.g., red + yellow + blue) |
| `neutral_with_accent` | Grays with one pop of color |

### Color Temperature

| Value | Colors |
|-------|--------|
| `cool` | Blues, teals, purples, mint |
| `warm` | Reds, oranges, yellows, coral |
| `neutral` | Grays, tans, off-whites |
| `mixed` | Intentional warm/cool contrast |

### Color Palette Mood

| Value | Characteristics |
|-------|-----------------|
| `earth` | Browns, greens, terracotta |
| `pastel` | Soft, desaturated, gentle |
| `jewel` | Rich, deep, saturated |
| `neon` | Bright, electric, vibrant |
| `monochrome` | Black, white, grays |
| `candy` | Bright pinks, blues, playful |
| `metallic` | Golds, silvers, chrome |

### Typography Classes

| Heading Class | Font Suggestions |
|---------------|------------------|
| `geometric_sans` | Poppins, Montserrat, Futura, Quicksand |
| `humanist_sans` | Open Sans, Lato, Source Sans Pro, Nunito |
| `neo_grotesque` | Inter, Roboto, Helvetica Neue |
| `modern_serif` | Playfair Display, Bodoni Moda |
| `slab_serif` | Roboto Slab, Zilla Slab |
| `display` | Oswald, Bebas Neue, Anton |
| `transitional_serif` | Georgia, Times New Roman, Merriweather |
| `monospace` | Fira Code, JetBrains Mono, IBM Plex Mono |

| Body Class | Font Suggestions |
|------------|------------------|
| `geometric_sans` | Poppins, Nunito |
| `humanist_sans` | Open Sans, Lato, Source Sans |
| `neo_grotesque` | Inter, Roboto, Work Sans |
| `humanist_serif` | Georgia, Charter, Merriweather |
| `monospace` | Fira Code, JetBrains Mono |

### Type Scale Ratios

| Value | Ratio | Example (16px base) |
|-------|-------|---------------------|
| `minor_second` | 1.067 | h1: 21px |
| `major_second` | 1.125 | h1: 28px |
| `minor_third` | 1.2 | h1: 33px |
| `major_third` | 1.25 | h1: 39px |
| `perfect_fourth` | 1.333 | h1: 50px |
| `augmented_fourth` | 1.414 | h1: 57px |
| `perfect_fifth` | 1.5 | h1: 76px |
| `golden_ratio` | 1.618 | h1: 108px |

---

## Accessibility Requirements

### Color Contrast
- Normal text: 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- UI components: 3:1 minimum

### Focus Indicators
- Visible focus ring on ALL interactive elements
- 3:1 contrast against adjacent colors
- Never `outline: none` without replacement

### Touch Targets
- Minimum 44x44px for all interactive elements
- 48x48px preferred for primary actions

### Reduced Motion
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

---

## Responsive Breakpoints

```css
/* Mobile first - base is 0-639px */
@media (min-width: 640px) { /* sm: tablet */ }
@media (min-width: 768px) { /* md: tablet landscape */ }
@media (min-width: 1024px) { /* lg: desktop */ }
@media (min-width: 1280px) { /* xl: large desktop */ }
```

Test at: 375px, 768px, 1024px, 1440px

---

## CSS Variable Naming

```css
:root {
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

    /* Shadows */
    --shadow-sm: ;
    --shadow-md: ;
    --shadow-lg: ;

    /* Radii */
    --radius-sm: ;
    --radius-md: ;
    --radius-lg: ;
    --radius-full: 9999px;

    /* Transitions */
    --transition-fast: 150ms ease;
    --transition-base: 200ms ease;
    --transition-slow: 300ms ease;
}
```

---

## Navigation JavaScript

Include this in every design file (update TOTAL_DESIGNS and CURRENT_DESIGN):

```javascript
(function() {
    const TOTAL_DESIGNS = 20;  // Update from manifest
    const CURRENT_DESIGN = 1;   // Update for each file

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            const next = CURRENT_DESIGN === TOTAL_DESIGNS ? 1 : CURRENT_DESIGN + 1;
            window.location.href = `design-${next}.html`;
        }
        if (e.key === 'ArrowLeft') {
            const prev = CURRENT_DESIGN === 1 ? TOTAL_DESIGNS : CURRENT_DESIGN - 1;
            window.location.href = `design-${prev}.html`;
        }
        if (e.key === 'Escape') {
            window.location.href = '../index.html';
        }
    });

    // Touch navigation
    let touchStartX = 0;
    document.addEventListener('touchstart', (e) => {
        touchStartX = e.touches[0].clientX;
    });
    document.addEventListener('touchend', (e) => {
        const diff = touchStartX - e.changedTouches[0].clientX;
        if (Math.abs(diff) > 50) {
            if (diff > 0) {
                const next = CURRENT_DESIGN === TOTAL_DESIGNS ? 1 : CURRENT_DESIGN + 1;
                window.location.href = `design-${next}.html`;
            } else {
                const prev = CURRENT_DESIGN === 1 ? TOTAL_DESIGNS : CURRENT_DESIGN - 1;
                window.location.href = `design-${prev}.html`;
            }
        }
    });

    // Prefetch adjacent pages
    ['prefetch'].forEach(rel => {
        const next = document.createElement('link');
        next.rel = rel;
        next.href = `design-${CURRENT_DESIGN === TOTAL_DESIGNS ? 1 : CURRENT_DESIGN + 1}.html`;
        document.head.appendChild(next);
    });

    // One-time navigation hint
    if (!localStorage.getItem('design-nav-hint-shown')) {
        const hint = document.createElement('div');
        hint.innerHTML = '← → to navigate • Esc for gallery';
        hint.style.cssText = `
            position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);
            padding: 12px 24px; background: var(--color-surface, #333);
            color: var(--color-text, #fff); border-radius: var(--radius-md, 8px);
            font-size: 14px; z-index: 9999; opacity: 0; transition: opacity 0.3s;
        `;
        document.body.appendChild(hint);
        setTimeout(() => hint.style.opacity = '1', 500);
        setTimeout(() => {
            hint.style.opacity = '0';
            setTimeout(() => hint.remove(), 300);
            localStorage.setItem('design-nav-hint-shown', 'true');
        }, 4000);
    }
})();
```

---

## Output Checklist

Before considering a design complete:

- [ ] HTML comment documentation is comprehensive
- [ ] JSON data block is valid
- [ ] All CSS variables defined
- [ ] All Tier 1 components present with states
- [ ] At least 3 Tier 3 mobile components
- [ ] Color contrast passes WCAG AA
- [ ] Focus indicators visible
- [ ] Works at 375px and 1440px
- [ ] Navigation JavaScript included
- [ ] File is self-contained (only Google Fonts external)

---

## Writing to Staging

Write your output to: `outputs/{batch}/.staging/design-{id}.html`

The orchestrator will validate and move to the final `designs/` folder.
