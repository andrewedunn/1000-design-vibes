# Design Guide (Core Only) - 1000 Design Vibes

Generate a self-contained HTML file showcasing a unique design system. **You have creative freedom** - we specify only 5 core dimensions, you choose everything else to create a coherent design.

---

## The Core-Only Approach

You receive **5 core dimensions** that define the design's identity:

| Dimension | What it controls |
|-----------|------------------|
| `functional_direction` | What the page IS - drives structure and required components |
| `design_era` | Historical aesthetic period - influences overall style |
| `emotional_tone` | How it should feel - guides mood and personality |
| `industry` | Business context - affects content and expectations |
| `color_mode` | Light or dark theme |

**Everything else is YOUR choice.** Pick colors, typography, spacing, shapes, textures, and details that work together coherently with the core dimensions.

---

## Your Creative Mandate

Make choices that feel **natural and harmonious** together. Avoid jarring combinations.

**Example of coherent choices:**
- `functional_direction: banking_dashboard` + `design_era: swiss_international` + `emotional_tone: trustworthy`
- → You might choose: neo-grotesque fonts, monochromatic blues, sharp corners, medium density, subtle shadows

**Example of incoherent choices (avoid):**
- Banking dashboard with psychedelic colors, hand-drawn icons, and organic blob shapes

**Trust your design instincts.** If a choice feels wrong for the context, pick something else.

---

## Core Requirements

1. **Self-contained** - Only external dependency: Google Fonts
2. **Complete design system** - Colors, typography, spacing, components
3. **LLM-readable** - Include documentation in HTML comments
4. **Accessible** - WCAG AA contrast, visible focus states, 44px touch targets

---

## Functional Direction (CRITICAL)

The `functional_direction` is the PRIMARY driver. It determines page structure and required UI elements.

**There are 158 functional directions** organized into categories:

| Category | Examples |
|----------|----------|
| **Standard Web** | dashboard, admin_panel, landing_page, documentation, e_commerce, blog |
| **Education** | online_course, quiz_interface, flashcard_app, lms_dashboard |
| **Productivity** | kanban_board, note_taking, spreadsheet, time_tracker, crm |
| **Communication** | messaging_app, email_client, team_chat, video_call |
| **Media** | music_player, video_player, photo_gallery, streaming_service |
| **Finance** | banking_dashboard, investment_portfolio, expense_tracker |
| **Health** | fitness_tracker, meditation_app, habit_tracker, appointment_booking |
| **Travel** | flight_booking, hotel_search, maps_interface, trip_planner |
| **Social** | user_profile, review_site, event_discovery, dating_profile |
| **Creative Tools** | code_editor, design_tool, color_picker, markdown_editor |
| **Retro & Novelty** | terminal_ui, windows_95, vaporwave, cyberpunk, 90s_website |
| **Data & Analytics** | data_table, chart_dashboard, analytics_overview |

**Each functional_direction has specific required components in `src/dimensions.py`.** Your design MUST include those elements.

**If your design doesn't clearly look like its functional_direction, you've failed.**

---

## Design Era Reference

Use these as the foundation for your style choices:

| Era | Spirit | Natural pairings |
|-----|--------|------------------|
| `bauhaus` | Functional geometry, primary colors | sharp corners, geometric sans, bold contrast |
| `art_deco` | Glamour, symmetry, metallic | display fonts, gold/black, geometric patterns |
| `mid_century_modern` | Organic curves, optimism | rounded corners, warm colors, humanist sans |
| `swiss_international` | Grid precision, objectivity | neo-grotesque, monochrome, sharp, dense |
| `memphis` | Playful geometry, bold patterns | vivid colors, display fonts, pill shapes |
| `y2k` | Tech optimism, chrome | gradients, glassmorphic, cool colors |
| `neo_brutalist` | Raw, bold borders | monospace, high contrast, thick borders |
| `scandinavian_modern` | Light, minimal, natural | airy, muted colors, humanist sans |
| `punk` | DIY, chaotic | collage aesthetic, harsh, irregular |
| `grunge` | Textured, worn | noise textures, muted, organic |
| `flat_2010s` | Minimal, colorful | no shadows, bright colors, clean |
| `psychedelic` | Swirling, vibrant | organic shapes, extreme saturation |

---

## Making Coherent Choices

When deciding typography, colors, shapes, etc., ask yourself:

1. **Does this fit the era?** A `swiss_international` design shouldn't have hand-drawn fonts.
2. **Does this match the tone?** A `luxurious` tone needs refinement, not playfulness.
3. **Does this work for the industry?** A `healthcare` design needs professionalism.
4. **Do these elements work together?** Pill-shaped buttons, organic blobs, and sharp headers clash.

**Pick a direction and commit.** Consistent choices > individually "optimal" ones.

---

## Technical Requirements

### CSS Variables (must define)
```css
:root {
    /* Colors - YOU CHOOSE based on era + tone + industry */
    --color-primary: ;
    --color-background: ;
    --color-surface: ;
    --color-text: ;
    --color-text-muted: ;

    /* Typography - YOU CHOOSE based on era + tone */
    --font-heading: ;
    --font-body: ;

    /* Spacing - YOU CHOOSE based on density preference */
    --space-unit: ;

    /* Shapes - YOU CHOOSE based on era + paradigm */
    --radius-default: ;
    --shadow-default: ;
}
```

### Accessibility
- Text contrast: 4.5:1 minimum
- Focus indicators on all interactive elements
- Include `@media (prefers-reduced-motion: reduce)` block

### Navigation Script (Required)
Include this exact script at the end of your `<body>`:

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

## Documentation Block (Required)

Start your HTML with a comment block documenting your choices:

```html
<!--
DESIGN: [Name] - [Tagline]
ABOUTME: This design implements [functional_direction] in [design_era] style.
ABOUTME: Emotional tone: [emotional_tone] | Industry: [industry]

MY DESIGN CHOICES:
- UI Paradigm: [what you chose and why]
- Color approach: [what you chose and why]
- Typography: [what you chose and why]
- Shape language: [what you chose and why]
- Density: [what you chose and why]

QUICK START - Copy these variables:
--color-primary: #xxx;
--color-background: #xxx;
--color-surface: #xxx;
--color-text: #xxx;
--font-heading: 'Font', fallback;
--font-body: 'Font', fallback;
--radius-default: Xpx;
--space-unit: Xpx;

AESTHETIC PRINCIPLES:
1. [First principle]
2. [Second principle]
3. [Third principle]

FUNCTIONAL DIRECTION: [functional_direction]
Required elements I included:
- [Element 1]
- [Element 2]
- [Element 3]
-->
```

---

## Output

Write to: `outputs/{batch}/.staging/design-{id}.html`

**Make something cohesive and distinctive.** The goal is a design where all elements feel intentionally chosen to work together.

---

## Validation Checklist

- [ ] File size > 10KB (aim for 25KB+)
- [ ] Contains `<!DOCTYPE html>`
- [ ] Contains `<style>` block
- [ ] Contains navigation handlers
- [ ] Clearly reflects the functional_direction
- [ ] Design choices feel coherent with core dimensions
