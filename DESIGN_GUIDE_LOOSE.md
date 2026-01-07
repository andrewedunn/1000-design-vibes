# Design Guide (Loose) - 1000 Design Vibes

Generate a self-contained HTML file showcasing a unique design system. **Be creative with layout and structure.**

---

## Core Requirements

1. **Self-contained** - Only external dependency allowed: Google Fonts
2. **Complete design system** - Colors, typography, spacing, components
3. **LLM-readable** - Include documentation in HTML comments
4. **Accessible** - WCAG AA contrast, visible focus states, 44px touch targets

---

## CRITICAL: Functional Direction Drives Everything

**The `functional_direction` dimension is the PRIMARY driver of your design.** It determines the page structure, components, and layout - not just styling.

| Value | YOU MUST INCLUDE |
|-------|------------------|
| `dashboard` | Sidebar nav, metric cards with numbers, charts/graphs, data tables, status indicators |
| `admin_panel` | Data tables, CRUD action buttons, form inputs, filters, breadcrumbs |
| `landing_page` | Hero section with CTA, feature grid, testimonial cards, pricing table |
| `documentation` | Sidebar table of contents, code blocks, search bar, prev/next navigation |
| `e_commerce` | Product cards with prices, filter sidebar, shopping cart icon, ratings |
| `portfolio` | Project cards with images, case study sections, about/contact |
| `blog` | Article with proper typography, author byline, related posts, reading time |
| `social_platform` | Post cards with avatar/name/timestamp, like/comment buttons, feed layout |
| `music_player` | Large album art, progress bar, play/pause/skip buttons, playlist |
| `messaging_app` | Conversation list sidebar, chat bubbles (left/right), message input |
| `calendar_app` | Month grid or week view, event cards, mini calendar, today button |
| `email_client` | Inbox list, email preview pane, folder sidebar, compose button |
| `weather_app` | Large current temp, weather icon, hourly row, 5-day forecast |
| `fitness_tracker` | Progress rings/circles, stat cards, activity list, goal indicators |
| `settings_panel` | Grouped toggles, dropdown selects, save button, section headers |
| `onboarding_flow` | Step indicator dots, single focused content, next/back buttons |
| `terminal_ui` | Monospace font everywhere, command prompts, dark bg with green/amber text |
| `retro_game_hud` | Score display, health/lives, pixel-style elements, game-like layout |
| `sci_fi_console` | Glowing borders, tech readouts, hexagonal or angular shapes |
| `newspaper` | Multi-column text, large masthead, bylines, pull quotes |
| `restaurant_menu` | Food categories, dish name + description + price format |
| `recipe_card` | Ingredients list, numbered steps, prep/cook time, servings |
| `event_poster` | Giant headline, date/time/venue prominently displayed |
| `magazine_spread` | Large images, pull quotes, editorial layout |
| `streaming_service` | Content rows with thumbnails, play buttons, category headers |
| `vintage_catalog` | Product grid with illustrations, item numbers, retro styling |
| `museum_exhibit` | Lots of whitespace, caption-style text, gallery cards |
| `meditation_app` | Calm colors, breathing circle placeholder, session cards |
| `government_form` | Form fields, section numbers, official/bureaucratic styling |
| `infographic` | Data viz elements, icon + stat combinations, flow diagrams |

**If your design doesn't clearly look like its functional_direction, you've failed the task.**

---

## Layout Structure Dimensions

These dimensions further control layout:

### Page Structure
| Value | Layout |
|-------|--------|
| `hero_sections` | Hero at top, then stacked sections |
| `split_screen` | Two columns throughout |
| `card_mosaic` | Bento/Pinterest mixed grid |
| `app_shell` | Fixed nav frame + scrolling content |
| `sidebar_main` | Persistent sidebar + main area |
| `fullscreen_slides` | Viewport-height sections |

### Navigation Pattern
| Value | Implementation |
|-------|----------------|
| `top_fixed` | Sticky header |
| `side_persistent` | Always-visible sidebar nav |
| `bottom_bar` | Mobile-style bottom nav |
| `floating_pill` | Floating nav button/pill |
| `tabs` | Tab-based navigation |
| `none` | No navigation |

### Hero Style
| Value | Treatment |
|-------|-----------|
| `full_viewport` | 100vh hero |
| `split_image` | Image + content side by side |
| `centered_minimal` | Just text, lots of space |
| `none` | No hero, dive into content |

### Content Flow
| Value | Organization |
|-------|--------------|
| `card_grid` | Uniform cards |
| `masonry` | Varied heights |
| `timeline` | Chronological |
| `list_detail` | List + detail panel |
| `kanban` | Column board |

---

## Visual Dimension Interpretation

Use these as creative inspiration:

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
