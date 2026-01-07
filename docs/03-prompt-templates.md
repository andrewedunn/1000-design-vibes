# Design Library Prompt Templates

This document contains the actual prompts to use at each stage of design library generation.

---

## Prompt 1: Generate the Manifest

Use this prompt with any capable LLM or as part of a Python script.

```
# Design Library Manifest Generator

Generate a JSON manifest for {N} unique design system specifications.

## Output Format

```json
{
  "version": "1.0.0",
  "generated_at": "{ISO timestamp}",
  "total_designs": {N},
  "designs": [
    {
      "id": 1,
      "name": "{Creative name}",
      "tagline": "{One sentence description}",
      "dimensions": {
        "ui_paradigm": "{value}",
        "design_era": "{value}",
        "density": "{value}",
        "color_theory": "{value}",
        "color_temperature": "{value}",
        "color_saturation": "{value}",
        "color_contrast": "{value}",
        "color_palette_mood": "{value}",
        "color_mode": "{value}",
        "type_heading_class": "{value}",
        "type_body_class": "{value}",
        "type_scale_ratio": "{value}",
        "type_case_treatment": "{value}",
        "type_letter_spacing": "{value}",
        "type_line_height": "{value}",
        "corner_radius": "{value}",
        "spacing_base": "{value}",
        "border_style": "{value}",
        "shadow_style": "{value}",
        "container_style": "{value}",
        "grid_system": "{value}",
        "alignment": "{value}",
        "hierarchy_approach": "{value}",
        "surface_texture": "{value}",
        "gradient_usage": "{value}",
        "icon_style": "{value}",
        "industry": "{value}",
        "target_audience": "{value}",
        "emotional_tone": "{value}",
        "cultural_influence": "{value}"
      }
    }
  ]
}
```

## Dimension Values

### ui_paradigm
skeuomorphic | flat | material | neumorphic | glassmorphic | brutalist | claymorphic | organic | editorial

### design_era
arts_and_crafts | art_nouveau | art_deco | bauhaus | mid_century_modern | swiss_international | pop_art | psychedelic | punk | memphis | grunge | y2k | web2_glossy | flat_2010s | neo_brutalist | scandinavian_modern

### density
ultra_airy | airy | balanced | compact | dense | ultra_dense

### color_theory
monochromatic | analogous | complementary | split_complementary | triadic | tetradic | neutral_with_accent

### color_temperature
cool | warm | neutral | mixed

### color_saturation
desaturated | muted | balanced | vivid | hyper_saturated

### color_contrast
low | medium | high | extreme

### color_palette_mood
earth | pastel | jewel | metallic | primary | monochrome | neon | cyber | natural | candy

### color_mode
light_only | dark_only | both

### type_heading_class
geometric_sans | humanist_sans | neo_grotesque | modern_serif | transitional_serif | old_style_serif | slab_serif | monospace | display | handwritten

### type_body_class
(same as type_heading_class)

### type_scale_ratio
minor_second | major_second | minor_third | major_third | perfect_fourth | golden_ratio

### type_case_treatment
normal | uppercase_headings | small_caps | lowercase_only

### type_letter_spacing
tight | normal | loose | very_loose

### type_line_height
tight | normal | loose | very_loose

### corner_radius
sharp | subtle | rounded | very_rounded | pill | organic

### spacing_base
4px | 8px | 10px | 12px

### border_style
none | hairline | thin | medium | thick | double | dashed

### shadow_style
none | subtle | medium | hard | dramatic | colored | layered | inset

### container_style
open | outlined | filled | floating | inset

### grid_system
single_column | two_column | three_column | four_column | twelve_column | asymmetric | modular | broken | freeform

### alignment
left | center | right | justified | mixed

### hierarchy_approach
size | color | position | weight | whitespace

### surface_texture
none | noise | paper | fabric | gradient_mesh | geometric_pattern | organic_pattern

### gradient_usage
none | subtle_background | accent | duotone | mesh | glassmorphic

### icon_style
outlined | filled | duotone | hand_drawn | isometric | emoji

### industry
finance | healthcare | education | ecommerce | saas | gaming | media | food | travel | real_estate | fashion | fitness | nonprofit | government | creative | developer

### target_audience
enterprise | smb | consumer_mass | consumer_premium | developer | children | seniors | gen_z

### emotional_tone
trustworthy | playful | serious | luxurious | friendly | edgy | calm | energetic | mysterious | nostalgic

### cultural_influence
scandinavian | japanese | mediterranean | american_corporate | british_traditional | german_industrial | french_elegant | latin_vibrant | african_bold | middle_eastern

## Requirements

1. **Uniqueness**: Every design must have a unique combination of dimensions. No two designs should have identical dimension sets.

2. **Diversity**: Distribute values across all dimensions. Don't cluster around certain combinations. Each dimension value should appear roughly equally across all designs.

3. **Creative names**: Generate evocative names that hint at the design's character. Examples:
   - "Midnight Protocol" (dark, tech, serious)
   - "Coral Reef" (warm, organic, playful)
   - "Swiss Precision" (minimal, grid, corporate)
   - "Memphis Mayhem" (colorful, playful, 80s)

4. **Coherent taglines**: The tagline should capture the essence of the dimension combination in plain language.

5. **Allow unexpected combinations**: Don't filter out "weird" combinations. Brutalist + pastel is valid. Glassmorphic + grunge is valid. Let creative tension exist.

## Generate designs {START} through {END}

Output only the JSON array of design entries for this range. Ensure no duplicates with any previously generated designs.
```

---

## Prompt 2: Generate Design Pages (Batch)

Use this prompt with Claude Code or a similar code-capable LLM.

```
# Design System Page Generator

Generate HTML design showcase files for the following manifest entries.

## Manifest Entries (Designs {START}-{END})

```json
{paste manifest entries here}
```

## File Requirements

For each design, create a file named `design-{id}.html` that is:

1. **Completely self-contained**: Only external dependency is Google Fonts
2. **LLM-instructable**: Another AI should be able to read the file and replicate the design in any framework
3. **Production-ready**: Accessible, responsive, uses modern CSS

## File Structure

Each file must follow this exact structure:

```html
<!--
================================================================================
DESIGN SYSTEM: {Name}
================================================================================

ABOUTME: {One line summary - what this design IS}
ABOUTME: {Second line - key visual characteristics}

================================================================================
FOR AI ASSISTANTS - HOW TO USE THIS DESIGN SYSTEM
================================================================================

When asked to "make something look like this design," follow these rules:

## QUICK START - COPY THESE VARIABLES

```css
:root {
  {All CSS custom properties}
}
```

## AESTHETIC PHILOSOPHY

This design embodies {design_era} influences with a {ui_paradigm} approach.

Core principles:
• {Principle 1 - specific to this design}
• {Principle 2 - specific to this design}
• {Principle 3 - specific to this design}
• {Principle 4 - specific to this design}

## COLOR SYSTEM

| Token | Hex | RGB | Usage |
|-------|-----|-----|-------|
| --color-primary | #XXXXXX | rgb(X,X,X) | {When to use} |
| --color-primary-hover | #XXXXXX | rgb(X,X,X) | {When to use} |
{Continue for all colors}

Contrast ratios:
- Primary on background: X.X:1 ✓
- Text on background: X.X:1 ✓
{All relevant contrast ratios}

## TYPOGRAPHY

Heading font: {Font name} ({type_heading_class})
Body font: {Font name} ({type_body_class})
Scale ratio: {ratio} ({type_scale_ratio})

| Element | Font | Size | Weight | Line Height | Letter Spacing |
|---------|------|------|--------|-------------|----------------|
| h1 | {font} | {size}rem | {weight} | {lh} | {ls} |
| h2 | {font} | {size}rem | {weight} | {lh} | {ls} |
| h3 | {font} | {size}rem | {weight} | {lh} | {ls} |
| h4 | {font} | {size}rem | {weight} | {lh} | {ls} |
| h5 | {font} | {size}rem | {weight} | {lh} | {ls} |
| h6 | {font} | {size}rem | {weight} | {lh} | {ls} |
| body | {font} | {size}rem | {weight} | {lh} | {ls} |
| small | {font} | {size}rem | {weight} | {lh} | {ls} |
| caption | {font} | {size}rem | {weight} | {lh} | {ls} |

## SPACING SYSTEM

Base unit: {spacing_base}
Scale: xs(0.25x), sm(0.5x), md(1x), lg(1.5x), xl(2x), 2xl(3x), 3xl(4x)

| Token | Value | Common uses |
|-------|-------|-------------|
| --space-xs | {value} | {uses} |
| --space-sm | {value} | {uses} |
| --space-md | {value} | {uses} |
| --space-lg | {value} | {uses} |
| --space-xl | {value} | {uses} |
| --space-2xl | {value} | {uses} |
| --space-3xl | {value} | {uses} |

## BORDERS & RADII

Border style: {border_style}
Default border: {value}

| Token | Value | Usage |
|-------|-------|-------|
| --radius-sm | {value} | {usage} |
| --radius-md | {value} | {usage} |
| --radius-lg | {value} | {usage} |
| --radius-full | {value} | {usage} |

## SHADOWS

Shadow style: {shadow_style}

| Token | Value | Usage |
|-------|-------|-------|
| --shadow-sm | {value} | {usage} |
| --shadow-md | {value} | {usage} |
| --shadow-lg | {value} | {usage} |
| --shadow-xl | {value} | {usage} |

## COMPONENT RECIPES

### Buttons

Primary button:
```css
.btn-primary {
  {complete CSS}
}
.btn-primary:hover { {hover state} }
.btn-primary:active { {active state} }
.btn-primary:focus-visible { {focus state} }
.btn-primary:disabled { {disabled state} }
```

Secondary button:
```css
{complete CSS with all states}
```

{Continue for outline, ghost, destructive buttons}

### Cards

```css
.card {
  {complete CSS}
}
.card:hover { {if applicable} }
```

### Form Inputs

```css
.input {
  {complete CSS}
}
.input:focus { }
.input:invalid { }
.input:disabled { }
```

### {Other key components}

## DO's ✓

1. {Specific actionable do for THIS design}
2. {Specific actionable do for THIS design}
3. {Specific actionable do for THIS design}
4. {Specific actionable do for THIS design}
5. {Specific actionable do for THIS design}

## DON'Ts ✗

1. {Specific actionable don't for THIS design}
2. {Specific actionable don't for THIS design}
3. {Specific actionable don't for THIS design}
4. {Specific actionable don't for THIS design}
5. {Specific actionable don't for THIS design}

## EXTENDING THIS DESIGN

When adding new components, follow these guidelines:
1. {Specific guidance}
2. {Specific guidance}
3. {Specific guidance}

Example - creating a new badge component:
```css
.badge {
  {example implementation following this design's rules}
}
```

## ACCESSIBILITY CHECKLIST

- [x] Color contrast meets WCAG AA (4.5:1 for text)
- [x] Focus indicators visible (3:1 contrast)
- [x] Touch targets 44x44px minimum
- [x] Reduced motion respected
- [x] Semantic HTML used

Focus indicator style for this design:
```css
:focus-visible {
  {this design's focus style}
}
```

## BEST FOR

This design works well for:
• {Specific use case 1}
• {Specific use case 2}
• {Specific use case 3}

## AVOID USING FOR

This design is NOT ideal for:
• {Specific anti-use case 1}
• {Specific anti-use case 2}

================================================================================
-->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{Name} – Design System #{id}</title>
  
  <!-- Preconnect to Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family={fonts}&display=swap" rel="stylesheet">
  
  <!-- Machine-readable design data -->
  <script type="application/json" id="design-system-data">
  {
    "id": {id},
    "name": "{name}",
    "version": "1.0.0",
    "generated": "{ISO date}",
    "dimensions": {manifest dimensions object},
    "tokens": {
      "colors": {
        "primary": "{hex}",
        "primaryHover": "{hex}",
        ...
      },
      "typography": {
        "headingFont": "{font}",
        "bodyFont": "{font}",
        "scaleRatio": {ratio},
        ...
      },
      "spacing": {
        "base": "{value}",
        "xs": "{value}",
        ...
      },
      "shadows": { ... },
      "radii": { ... },
      "borders": { ... }
    },
    "bestFor": ["{use case}", ...],
    "avoid": ["{anti-pattern}", ...]
  }
  </script>
  
  <style>
    /* ===== CSS CUSTOM PROPERTIES ===== */
    :root {
      /* Colors */
      --color-primary: ;
      --color-primary-hover: ;
      --color-primary-active: ;
      --color-secondary: ;
      --color-accent: ;
      --color-background: ;
      --color-surface: ;
      --color-text: ;
      --color-text-muted: ;
      --color-border: ;
      --color-error: ;
      --color-success: ;
      --color-warning: ;
      --color-info: ;
      
      /* Typography */
      --font-heading: ;
      --font-body: ;
      --font-mono: ;
      --text-xs: ;
      --text-sm: ;
      --text-base: ;
      --text-lg: ;
      --text-xl: ;
      --text-2xl: ;
      --text-3xl: ;
      --text-4xl: ;
      --font-weight-normal: ;
      --font-weight-medium: ;
      --font-weight-semibold: ;
      --font-weight-bold: ;
      --line-height-tight: ;
      --line-height-normal: ;
      --line-height-loose: ;
      --letter-spacing-tight: ;
      --letter-spacing-normal: ;
      --letter-spacing-wide: ;
      
      /* Spacing */
      --space-xs: ;
      --space-sm: ;
      --space-md: ;
      --space-lg: ;
      --space-xl: ;
      --space-2xl: ;
      --space-3xl: ;
      
      /* Shadows */
      --shadow-sm: ;
      --shadow-md: ;
      --shadow-lg: ;
      --shadow-xl: ;
      
      /* Radii */
      --radius-sm: ;
      --radius-md: ;
      --radius-lg: ;
      --radius-full: ;
      
      /* Borders */
      --border-width: ;
      --border-color: ;
      
      /* Transitions */
      --transition-fast: ;
      --transition-normal: ;
      --transition-slow: ;
    }
    
    /* ===== RESET & BASE ===== */
    *, *::before, *::after {
      box-sizing: border-box;
    }
    
    /* ===== TYPOGRAPHY ===== */
    
    /* ===== COMPONENTS ===== */
    
    /* Buttons */
    
    /* Cards */
    
    /* Form Inputs */
    
    /* Navigation */
    
    /* Badges */
    
    /* Alerts */
    
    /* Tables */
    
    /* Modals */
    
    /* Mobile Components */
    
    /* ===== UTILITIES ===== */
    
    /* ===== RESPONSIVE ===== */
    @media (min-width: 640px) { }
    @media (min-width: 768px) { }
    @media (min-width: 1024px) { }
    @media (min-width: 1280px) { }
    
    /* ===== REDUCED MOTION ===== */
    @media (prefers-reduced-motion: reduce) {
      *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
    
    /* ===== SHOWCASE LAYOUT ===== */
  </style>
</head>
<body>
  <!-- SHOWCASE CONTENT -->
  
  <header>
    <!-- Design name, tagline, navigation -->
  </header>
  
  <main>
    <!-- Section: Color Palette -->
    
    <!-- Section: Typography -->
    
    <!-- Section: Spacing -->
    
    <!-- Section: Buttons -->
    
    <!-- Section: Form Elements -->
    
    <!-- Section: Cards -->
    
    <!-- Section: Navigation Components -->
    
    <!-- Section: Alerts & Feedback -->
    
    <!-- Section: Tables -->
    
    <!-- Section: Mobile Components -->
    
    <!-- Section: Example Layouts -->
  </main>
  
  <footer>
    <!-- Design metadata, links -->
  </footer>
  
  <!-- Navigation Script -->
  <script>
    (function() {
      const TOTAL = {total_designs};
      const CURRENT = {id};
      
      // Keyboard navigation
      document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        
        if (e.key === 'ArrowRight') {
          window.location.href = `design-${CURRENT === TOTAL ? 1 : CURRENT + 1}.html`;
        }
        if (e.key === 'ArrowLeft') {
          window.location.href = `design-${CURRENT === 1 ? TOTAL : CURRENT - 1}.html`;
        }
        if (e.key === 'Escape') {
          window.location.href = 'index.html';
        }
      });
      
      // Touch navigation
      let startX = 0;
      document.addEventListener('touchstart', e => startX = e.touches[0].clientX, {passive: true});
      document.addEventListener('touchend', e => {
        const diff = startX - e.changedTouches[0].clientX;
        if (Math.abs(diff) > 50) {
          window.location.href = diff > 0 
            ? `design-${CURRENT === TOTAL ? 1 : CURRENT + 1}.html`
            : `design-${CURRENT === 1 ? TOTAL : CURRENT - 1}.html`;
        }
      }, {passive: true});
      
      // Prefetch
      ['prev', 'next'].forEach((dir, i) => {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = `design-${dir === 'next' 
          ? (CURRENT === TOTAL ? 1 : CURRENT + 1)
          : (CURRENT === 1 ? TOTAL : CURRENT - 1)}.html`;
        document.head.appendChild(link);
      });
      
      // One-time hint
      if (!localStorage.getItem('design-library-nav-hint')) {
        const hint = document.createElement('div');
        hint.setAttribute('role', 'status');
        hint.setAttribute('aria-live', 'polite');
        hint.innerHTML = '← → Navigate designs • Esc for gallery';
        Object.assign(hint.style, {
          position: 'fixed',
          bottom: 'var(--space-lg, 24px)',
          left: '50%',
          transform: 'translateX(-50%)',
          padding: 'var(--space-sm, 12px) var(--space-lg, 24px)',
          background: 'var(--color-surface, #1a1a1a)',
          color: 'var(--color-text, #ffffff)',
          borderRadius: 'var(--radius-md, 8px)',
          fontSize: 'var(--text-sm, 14px)',
          boxShadow: 'var(--shadow-lg)',
          zIndex: '9999',
          opacity: '0',
          transition: 'opacity 0.3s'
        });
        document.body.appendChild(hint);
        requestAnimationFrame(() => hint.style.opacity = '1');
        setTimeout(() => {
          hint.style.opacity = '0';
          setTimeout(() => hint.remove(), 300);
        }, 4000);
        localStorage.setItem('design-library-nav-hint', '1');
      }
    })();
  </script>
</body>
</html>
```

## Critical Requirements

1. **No placeholders**: Generate complete, working CSS values. Don't use `{value}` in the output.

2. **Real fonts**: Choose actual Google Fonts that match the type_heading_class and type_body_class dimensions.

3. **Working components**: All buttons, inputs, cards must actually work when clicked/focused.

4. **Specific documentation**: The DO's, DON'Ts, and principles must be specific to THIS design, not generic advice.

5. **Accessible colors**: Verify contrast ratios. If the dimension combination creates poor contrast, adjust slightly while staying true to the intent.

6. **Complete showcase**: Include visual examples of every component, not just CSS definitions.

## Generate Now

Create design-{START}.html through design-{END}.html following all specifications above.
```

---

## Prompt 3: Generate Gallery Index

```
# Design Library Index Generator

Create an index.html file that serves as a gallery for {N} design showcase files.

## Requirements

1. **Grid layout**: Responsive grid showing all designs
   - 1 column on mobile (<640px)
   - 2 columns on tablet (640-1023px)
   - 3 columns on small desktop (1024-1279px)
   - 4 columns on large desktop (1280px+)

2. **Design cards**: Each card shows:
   - Design number and name
   - Visual preview (color swatches representing the palette)
   - Brief tagline
   - Key tags (style family, mood, industry)
   - Click to open design

3. **Navigation**:
   - Arrow keys navigate the grid
   - Enter opens selected design
   - Visual focus indicator
   - Current selection highlighted

4. **Search/filter** (optional but recommended):
   - Search by name
   - Filter by dimension values (ui_paradigm, emotional_tone, etc.)

5. **Metadata display**:
   - Total design count
   - Generation date

## Design data

```json
{array of all design entries with id, name, tagline, key dimensions}
```

## Style

The index page itself should be neutral and let the design previews shine:
- Clean, minimal interface
- System font stack
- Light/dark mode support via prefers-color-scheme
- Focus on scannability

Generate the complete index.html file.
```

---

## Prompt 4: Add Documentation to Existing Files

This is the improved version of your original prompt:

```
# Design System Documentation Enhancement

I have {N} design HTML files (design-1.html through design-{N}.html).

Add comprehensive LLM-readable documentation to each file.

## For Each File

### 1. Read the existing CSS and extract:
- All CSS custom properties (--color-*, --font-*, --space-*, etc.)
- Font families used
- Component class patterns
- Shadow values
- Border radius values
- The overall aesthetic approach

### 2. Add documentation header (before <!DOCTYPE html>):

```html
<!--
================================================================================
DESIGN SYSTEM: {Name extracted or inferred from file}
================================================================================

ABOUTME: {Describe what this design IS in one line}
ABOUTME: {List 3-4 key visual characteristics}

================================================================================
FOR AI ASSISTANTS
================================================================================

[Full documentation block following the template from Prompt 2]

================================================================================
-->
```

### 3. Add/update JSON data block in <head>:

```html
<script type="application/json" id="design-system-data">
{
  "id": {N},
  "name": "{name}",
  "tokens": { /* extracted from CSS */ },
  "bestFor": [/* inferred use cases */],
  "avoid": [/* inferred anti-patterns */]
}
</script>
```

### 4. Add navigation JavaScript before </body>:

The navigation script with:
- Keyboard: Arrow keys prev/next, Escape to gallery
- Touch: Swipe navigation
- Prefetch: Adjacent pages
- Hint toast: Styled to match the design's aesthetic

### 5. Style the hint toast:

The navigation hint must use the design's own CSS variables:
```javascript
Object.assign(hint.style, {
  background: 'var(--color-surface, #333)',
  color: 'var(--color-text, #fff)',
  borderRadius: 'var(--radius-md, 8px)',
  // etc.
});
```

## Critical Rules

1. **Extract real values**: Read the actual CSS, don't make up values
2. **Design-specific documentation**: The principles, do's, don'ts must reflect THIS specific design's aesthetic
3. **Preserve existing content**: Don't modify the showcase content, only add documentation
4. **Match the aesthetic**: The hint toast must look like it belongs to the design

## Process in batches

Process files in groups of 5 to maintain quality:
- Batch 1: design-1.html through design-5.html
- Batch 2: design-6.html through design-10.html
- etc.

For each file:
1. Read the complete file
2. Analyze the CSS
3. Generate appropriate documentation
4. Add navigation
5. Save the updated file

## Begin with designs {START} through {END}
```

---

## Usage Examples

### Generate a 1000-design manifest

```bash
# With Claude Code
claude "Generate a design manifest with 1000 unique entries. 
Use the manifest generator prompt. 
Save to manifest.json"

# Or with a Python script using the prompt
python generate_manifest.py --count 1000 --output manifest.json
```

### Generate designs in batches

```bash
# Batch 1: designs 1-20
claude "Using the design page generator prompt, create designs 1-20 
from manifest.json. Save each as design-{id}.html"

# Batch 2: designs 21-40  
claude "Using the design page generator prompt, create designs 21-40
from manifest.json. Save each as design-{id}.html"

# Continue...
```

### Add documentation to existing files

```bash
claude "Using the documentation enhancement prompt, add documentation
to design-1.html through design-10.html"
```

### Generate the index

```bash
claude "Using the gallery index prompt, create index.html for all 1000 designs.
Read design names and metadata from the manifest.json file."
```

---

## Tips for Best Results

1. **Don't rush batches**: Quality degrades if you push too many designs at once. 10-20 per batch is ideal.

2. **Review early outputs**: Check the first few designs carefully. If something's off, correct the prompt before generating hundreds more.

3. **Validate accessibility**: Run a spot-check with a contrast checker on early designs.

4. **Test navigation**: Verify keyboard and touch navigation works after each batch.

5. **Keep the manifest sacred**: Don't modify manifest.json after generation starts. It's your source of truth.

6. **Version control**: Commit after each batch so you can roll back if needed.
