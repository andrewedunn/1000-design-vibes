# Design Guide (Loose) - 1000 Design Vibes

Generate a self-contained HTML file showcasing a unique design system. **Be creative with layout and structure.**

---

## Core Requirements

1. **Self-contained** - Only external dependency allowed: Google Fonts
2. **Complete design system** - Colors, typography, spacing, components
3. **LLM-readable** - Include documentation in HTML comments
4. **Accessible** - WCAG AA contrast, visible focus states, 44px touch targets

---

## Creative Freedom

You have full creative control over:

- **Page structure** - Not required to follow any template
- **Section types** - Invent sections that fit the design's personality
- **Layout approach** - Grid, freeform, asymmetric, scrolling, cards, whatever fits
- **Component selection** - Show what best demonstrates this design system
- **Visual storytelling** - Let the design speak for itself

**The only constraint:** The page should effectively showcase a usable design system that another developer could understand and apply.

---

## Dimension Interpretation

Use these as creative inspiration, not rigid rules:

### UI Paradigm
| Value | Essence |
|-------|---------|
| `flat` | Clean, no shadows, solid colors |
| `material` | Layered surfaces, elevation |
| `neumorphic` | Soft extruded forms, monochromatic |
| `glassmorphic` | Blur, transparency, light |
| `brutalist` | Raw, stark, honest structure |
| `claymorphic` | Soft, puffy, playful depth |
| `skeuomorphic` | Real-world textures and materials |
| `organic` | Flowing, blob-like, natural curves |
| `editorial` | Typography-driven, magazine-like |

### Design Era
| Value | Spirit |
|-------|--------|
| `bauhaus` | Functional geometry, primary colors |
| `art_deco` | Glamour, symmetry, gold accents |
| `mid_century_modern` | Organic curves, optimism |
| `swiss_international` | Grid precision, objectivity |
| `memphis` | Playful geometry, bold patterns |
| `y2k` | Tech optimism, chrome, gradients |
| `neo_brutalist` | Raw HTML aesthetic, bold borders |
| `scandinavian_modern` | Light, minimal, natural |
| `punk` | DIY, chaotic, anti-establishment |
| `grunge` | Textured, worn, authentic |
| `art_nouveau` | Organic lines, nature-inspired ornament |
| `pop_art` | Bold, graphic, commercial irony |

### Color
- **Theory**: monochromatic | complementary | analogous | triadic | split_complementary | tetradic | neutral_with_accent
- **Temperature**: cool | warm | neutral | mixed
- **Saturation**: desaturated | muted | balanced | vivid | hyper_saturated
- **Mood**: earth | pastel | jewel | neon | monochrome | candy | metallic | natural | cyber | primary

### Typography
- **Heading fonts**: geometric_sans, humanist_sans, neo_grotesque, modern_serif, slab_serif, display, old_style_serif, transitional_serif, monospace, handwritten
- **Body fonts**: geometric_sans, humanist_sans, neo_grotesque, transitional_serif, slab_serif, monospace, modern_serif, old_style_serif, display
- **Scale ratios**: minor_second (1.067) → golden_ratio (1.618)

### Spatial & Surface
- **Density**: ultra_dense → ultra_airy
- **Corners**: sharp | subtle | rounded | very_rounded | pill | organic
- **Shadows**: none | subtle | medium | hard | dramatic | colored | layered | inset
- **Borders**: none | hairline | thin | medium | thick | double | dashed
- **Textures**: none | noise | paper | fabric | geometric_pattern | organic_pattern | gradient_mesh

### Functional Direction
| Value | Focus |
|-------|-------|
| `dashboard` | Analytics, metrics, data-heavy panels |
| `admin_panel` | Backend management, CRUD interfaces |
| `mobile_app` | Mobile-first, touch-optimized |
| `landing_page` | Marketing, conversion-focused |
| `documentation` | Docs sites, technical content |
| `e_commerce` | Product catalog, checkout flows |
| `portfolio` | Personal/agency showcase |
| `blog` | Content-focused, reading experience |
| `data_visualization` | Charts, graphs, data storytelling |
| `social_platform` | Feeds, profiles, interactions |

---

## Technical Requirements

### CSS Variables (must define)
```css
:root {
    /* Colors */
    --color-primary: ;
    --color-background: ;
    --color-surface: ;
    --color-text: ;
    --color-text-muted: ;

    /* Typography */
    --font-heading: ;
    --font-body: ;

    /* Spacing */
    --space-unit: ; /* base unit */

    /* Shapes */
    --radius-default: ;
    --shadow-default: ;
}
```

### Accessibility
- Text contrast: 4.5:1 minimum
- Focus indicators on all interactive elements
- Include `@media (prefers-reduced-motion: reduce)` block

### Navigation Script (Required)
Include this exact script at the end of your `<body>`, updating CURRENT_DESIGN to match the design ID:

```javascript
<script>
(function() {
    const TOTAL = 10;
    const CURRENT = 1; // UPDATE THIS to match design ID

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') window.location.href = `design-${CURRENT === TOTAL ? 1 : CURRENT + 1}.html`;
        if (e.key === 'ArrowLeft') window.location.href = `design-${CURRENT === 1 ? TOTAL : CURRENT - 1}.html`;
    });

    let startX;
    document.addEventListener('touchstart', e => startX = e.touches[0].clientX);
    document.addEventListener('touchend', e => {
        const diff = startX - e.changedTouches[0].clientX;
        if (Math.abs(diff) > 50) {
            window.location.href = diff > 0
                ? `design-${CURRENT === TOTAL ? 1 : CURRENT + 1}.html`
                : `design-${CURRENT === 1 ? TOTAL : CURRENT - 1}.html`;
        }
    });
})();
</script>
```

---

## Documentation Block

Start with an HTML comment containing:
- Design name and ABOUTME lines
- Quick-start CSS variables
- Aesthetic principles (what makes this design unique)
- Key token values

---

## Output

Write to: `outputs/{batch}/.staging/design-{id}.html`

**Make something distinctive.** If someone browsed through 20 designs, yours should be memorable.

---

## Validation Checklist

Your design will be validated for:
- [ ] File size > 10KB
- [ ] Contains `<!DOCTYPE html>`
- [ ] Contains `<style>` block
- [ ] Contains `ArrowRight` and `ArrowLeft` navigation handlers
- [ ] Navigation actually works (functions are defined, not just listeners)
