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

There are **158 functional directions** organized into categories. Each one specifies required UI elements. Here are the categories and examples:

| Category | Examples |
|----------|----------|
| **Standard Web** | dashboard, admin_panel, landing_page, documentation, e_commerce, blog, wiki, pricing_page |
| **Education** | online_course, quiz_interface, flashcard_app, language_learning, lms_dashboard, grade_book, exam_interface |
| **Productivity** | project_management, kanban_board, note_taking, spreadsheet, time_tracker, invoice, crm, file_manager |
| **Communication** | messaging_app, email_client, video_call, team_chat, comment_section, live_chat_widget |
| **Media** | music_player, video_player, podcast_player, photo_gallery, streaming_service, movie_database, comic_reader |
| **Finance** | banking_dashboard, investment_portfolio, expense_tracker, crypto_tracker, pos_terminal, budget_planner |
| **Health** | fitness_tracker, meditation_app, habit_tracker, sleep_tracker, nutrition_counter, appointment_booking |
| **Travel** | flight_booking, hotel_search, trip_planner, maps_interface, transit_app, ride_sharing |
| **Social** | dating_profile, user_profile, review_site, event_discovery, community_directory |
| **Creative Tools** | code_editor, design_tool, color_picker, font_browser, component_library, markdown_editor |
| **Food & Dining** | restaurant_menu, recipe_card, food_delivery, meal_planner, wine_list |
| **Sports & Gaming** | sports_scores, tournament_bracket, game_leaderboard, character_sheet, game_inventory |
| **Events** | event_poster, ticket_booking, conference_schedule, wedding_invitation, countdown_page |
| **Utility** | calculator, survey_form, password_generator, qr_generator, unit_converter |
| **Retro & Novelty** | terminal_ui, retro_game_hud, sci_fi_console, windows_95, vaporwave, cyberpunk, 90s_website, myspace_profile |
| **Professional** | government_form, legal_document, scientific_paper, medical_chart, shipping_tracker, security_dashboard |
| **Personal** | resume_cv, personal_homepage, linktree_clone, 404_page, login_page, coming_soon |
| **Data & Analytics** | infographic, report_builder, data_table, chart_dashboard, analytics_overview |

**Each functional_direction has specific required components in `src/dimensions.py`.** Your design MUST include those elements.

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

### CRITICAL: Do NOT Include

**NO NAVIGATION SCRIPTS** - The viewer handles navigation between designs. Do NOT add:
- Keyboard event listeners for ArrowLeft/ArrowRight
- Previous/Next buttons that navigate between designs
- Any `window.location.href` redirects to other design files

**CSS COMMENTS ONLY** - Inside `<style>` blocks, use CSS comments `/* */`, never HTML comments `<!-- -->`.

```css
/* CORRECT - CSS comments inside style blocks */
:root {
    /* Color palette */
    --color-primary: #6366f1;
}

/* WRONG - HTML comments break CSS parsing */
:root {
    <!-- Color palette -->
    --color-primary: #6366f1;
}
```

---

## Documentation Block (Required)

Start your HTML with a substantial comment block (30+ lines) containing:

```html
<!--
DESIGN: [Name] - [Tagline]
ABOUTME: This design system implements [functional_direction] with [ui_paradigm] aesthetics.
ABOUTME: Key characteristics: [2-3 defining visual traits]

QUICK START - Copy these variables to apply this design:
--color-primary: #xxx;
--color-background: #xxx;
--color-surface: #xxx;
--color-text: #xxx;
--font-heading: 'Font Name', fallback;
--font-body: 'Font Name', fallback;
--radius-default: Xpx;
--space-unit: Xpx;

AESTHETIC PRINCIPLES:
1. [First principle - e.g., "High contrast borders define all interactive elements"]
2. [Second principle - e.g., "Typography scale creates dramatic hierarchy"]
3. [Third principle - e.g., "Generous whitespace emphasizes content blocks"]

BEST FOR:
- [Use case 1]
- [Use case 2]

AVOID IF:
- [Anti-pattern 1]
- [Anti-pattern 2]

FUNCTIONAL DIRECTION: [functional_direction]
This design must clearly function as a [functional_direction]. Required elements:
- [Element 1 from dimensions.py]
- [Element 2]
- [Element 3]
-->
```

This documentation helps AI agents understand and apply the design to other projects.

---

## Output

Write to: `outputs/{batch}/.staging/design-{id}.html`

**Make something distinctive.** If someone browsed through 20 designs, yours should be memorable. Go bold with your interpretation of the dimensions.

---

## Quality Expectations

- **File size**: 25-50KB is typical for a complete design. Under 15KB suggests missing components.
- **Component variety**: Include multiple states (hover, focus, active, disabled) for interactive elements.
- **Real content**: Use realistic placeholder text, not just "Lorem ipsum" everywhere.

---

## Validation Checklist

Your design will be validated for:
- [ ] File size > 10KB (aim for 25KB+)
- [ ] Contains `<!DOCTYPE html>`
- [ ] Contains `<style>` block
- [ ] Clearly reflects the assigned functional_direction
