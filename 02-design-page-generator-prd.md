# Design Page Generator PRD

## Overview

This document defines how an LLM should generate self-contained HTML design showcase pages from manifest entries. Each generated page serves dual purposes:

1. **Visual showcase**: A browsable demonstration of the design system
2. **LLM instruction set**: Embedded documentation that allows any coding LLM to replicate the style

---

## Core Principles

### 1. Self-contained
Every HTML file must work with zero external dependencies (except Google Fonts CDN). No build step, no npm, no framework.

### 2. LLM-readable
The embedded documentation should be optimized for LLM consumption, not just human reading. Include structured data, clear rules, and concrete examples.

### 3. Production-ready
Components should be accessible, responsive, and use modern CSS. Not just "pretty demos" but actually usable patterns.

### 4. Transferable
The design should be extractable to any framework (React, Vue, Svelte, vanilla) by an LLM reading the file.

---

## File Structure

Each design file follows this exact structure:

```html
<!--
================================================================================
DESIGN SYSTEM: [Name]
================================================================================

ABOUTME: [One line description]
ABOUTME: [Second line with key characteristics]

================================================================================
FOR AI ASSISTANTS
================================================================================

This design system document is optimized for LLM consumption. When a user asks
you to "make my app look like this," follow the rules below precisely.

## QUICK START

Apply these CSS variables to your root element:
[CSS variable block]

## AESTHETIC PRINCIPLES

- [Principle 1]
- [Principle 2]
- [Principle 3]
- [Principle 4]

## COLOR SYSTEM

| Token | Value | Usage |
|-------|-------|-------|
| --color-primary | #XXXXXX | [When to use] |
| --color-secondary | #XXXXXX | [When to use] |
| [etc.]

## TYPOGRAPHY

Font Stack: [Exact font stack]
Headings: [Font, weights, sizes]
Body: [Font, weights, sizes]
Scale Ratio: [Ratio used]

| Element | Font | Size | Weight | Line Height |
|---------|------|------|--------|-------------|
| h1 | [font] | [size] | [weight] | [lh] |
| [etc.]

## SPACING SYSTEM

Base Unit: [Xpx]
Scale: [multipliers used]

| Token | Value | Usage |
|-------|-------|-------|
| --space-xs | [value] | [usage] |
| [etc.]

## COMPONENT PATTERNS

### Buttons

Primary: [full CSS description]
Secondary: [full CSS description]
States: hover, active, disabled, focus

### Cards

[Full pattern description]

### Form Inputs

[Full pattern description]

### [Other components...]

## SHADOWS

| Token | Value | Usage |
|-------|-------|-------|
| --shadow-sm | [value] | [usage] |
| [etc.]

## BORDERS & RADII

Border Default: [value]
Radius Scale:
| Token | Value | Usage |
|-------|-------|-------|
| --radius-sm | [value] | [usage] |
| [etc.]

## DO's ✓

1. [Specific do]
2. [Specific do]
3. [Specific do]
4. [Specific do]
5. [Specific do]

## DON'Ts ✗

1. [Specific don't]
2. [Specific don't]
3. [Specific don't]
4. [Specific don't]
5. [Specific don't]

## ACCESSIBILITY

- Contrast ratios: [specifics]
- Focus indicators: [how they work]
- Touch targets: [minimum sizes]
- Motion: [reduced motion handling]

## EXTENDING THIS DESIGN

When adding new components:
1. [Guidance 1]
2. [Guidance 2]
3. [Guidance 3]

Example - adding a new alert component:
[Code example]

================================================================================
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Name] - Design System</title>
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=[fonts]&display=swap" rel="stylesheet">
    
    <!-- Design System Data (machine-readable) -->
    <script type="application/json" id="design-system-data">
    {
        "name": "[Name]",
        "version": "1.0.0",
        "description": "[Description]",
        "dimensions": { /* from manifest */ },
        "tokens": {
            "colors": { },
            "typography": { },
            "spacing": { },
            "shadows": { },
            "radii": { }
        },
        "bestFor": ["use case 1", "use case 2"],
        "avoid": ["anti-pattern 1", "anti-pattern 2"]
    }
    </script>
    
    <style>
        /* CSS Variables (Design Tokens) */
        :root {
            /* Colors */
            --color-primary: ;
            --color-primary-hover: ;
            --color-secondary: ;
            /* ... */
            
            /* Typography */
            --font-heading: ;
            --font-body: ;
            /* ... */
            
            /* Spacing */
            --space-unit: ;
            --space-xs: ;
            --space-sm: ;
            /* ... */
            
            /* Shadows */
            --shadow-sm: ;
            --shadow-md: ;
            /* ... */
            
            /* Radii */
            --radius-sm: ;
            --radius-md: ;
            /* ... */
        }
        
        /* Base Styles */
        
        /* Component Styles */
        
        /* Utility Classes */
        
        /* Responsive Styles */
        
        /* Reduced Motion */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                transition-duration: 0.01ms !important;
            }
        }
    </style>
</head>
<body>
    <!-- Design showcase content -->
    
    <!-- Navigation script -->
    <script>
        // Keyboard and touch navigation
    </script>
</body>
</html>
```

---

## Required Components

Every design showcase must include working examples of these components:

### Tier 1: Essential (must have)

| Component | Variants | States |
|-----------|----------|--------|
| **Buttons** | Primary, Secondary, Outline, Ghost, Destructive | Default, Hover, Active, Disabled, Focus, Loading |
| **Text inputs** | Default, With label, With error, With helper text, Disabled | Focus, Error, Success |
| **Cards** | Basic, With image, With actions, Clickable | Hover, Selected |
| **Typography** | h1-h6, body, small, caption, link | — |
| **Navigation** | Header nav, Mobile menu | Active state, Hover |

### Tier 2: Important (should have)

| Component | Variants |
|-----------|----------|
| **Select/Dropdown** | Default, Multi-select |
| **Checkbox** | Default, Indeterminate |
| **Radio** | Default, Radio group |
| **Toggle/Switch** | Default, With label |
| **Badge/Tag** | Various colors, Dismissible |
| **Avatar** | Image, Initials, Sizes |
| **Alert/Toast** | Info, Success, Warning, Error |
| **Modal/Dialog** | Basic, With form |
| **Tabs** | Horizontal, Vertical |
| **Table** | Basic, Sortable, With actions |

### Tier 3: Mobile/App (must have some)

Each design must include at least 3 of these:

| Component | Description |
|-----------|-------------|
| **Bottom nav** | Mobile app-style bottom navigation |
| **FAB** | Floating action button |
| **Bottom sheet** | Slide-up panel |
| **Card list** | Scrollable card feed |
| **Pull-to-refresh** | Loading indicator |
| **Skeleton loader** | Content placeholder |
| **Swipe actions** | Swipe-to-reveal actions |
| **Segmented control** | iOS-style toggle |
| **Touch-optimized list** | Large touch targets |

---

## Showcase Page Sections

Each design file should include these sections in order:

### 1. Hero/Header
- Design name prominently displayed
- One-sentence description
- Visual representation of the aesthetic

### 2. Color Palette
- All colors displayed as swatches
- Hex values visible
- Usage labels (Primary, Secondary, Background, etc.)
- Contrast ratios shown for text colors

### 3. Typography Specimen
- All heading levels (h1-h6)
- Body text at different sizes
- Font weights available
- Line height demonstrations
- Letter spacing if notable

### 4. Spacing & Layout
- Visual spacing scale
- Grid demonstration
- Container widths

### 5. Component Gallery
- All Tier 1 components
- All Tier 2 components (or most)
- At least 3 Tier 3 mobile components
- Each with all variants and states

### 6. Example Layouts
- One "hero section" example
- One "feature grid" example
- One "form" example
- One "dashboard card" example
- One "mobile screen" example

### 7. Design Tokens Reference
- Visual table of all CSS variables
- Copy-able values

### 8. Best For / Avoid
- Use case recommendations
- Anti-patterns to avoid

---

## Accessibility Requirements

### Color contrast
- Normal text: minimum 4.5:1 against background
- Large text (18px+): minimum 3:1
- UI components: minimum 3:1
- Include actual ratio values in documentation

### Focus indicators
- Visible focus ring on all interactive elements
- Focus ring must have 3:1 contrast against adjacent colors
- Never use `outline: none` without replacement

### Touch targets
- Minimum 44x44px for all interactive elements
- 48x48px preferred for primary actions
- Adequate spacing between targets

### Reduced motion
- Include `prefers-reduced-motion` media query
- Disable or reduce animations for users who prefer it

### Semantic HTML
- Use appropriate heading hierarchy
- Use `<button>` for buttons, not divs
- Use `<a>` for links
- Include proper ARIA labels where needed

### Screen reader considerations
- Decorative images have empty alt or aria-hidden
- Form inputs have associated labels
- Error messages are announced

---

## Responsive Requirements

### Breakpoints
All designs must be responsive with these breakpoints:

```css
/* Mobile first */
/* Base: 0-639px (mobile) */

@media (min-width: 640px) { /* sm: tablet */ }
@media (min-width: 768px) { /* md: tablet landscape */ }
@media (min-width: 1024px) { /* lg: desktop */ }
@media (min-width: 1280px) { /* xl: large desktop */ }
```

### Mobile requirements
- Hamburger/mobile menu for navigation
- Touch-friendly button sizes
- Readable text without zooming (16px minimum)
- No horizontal scroll
- Thumb-zone considerations

### Viewport testing
Designs should be tested/viewable at:
- 375px (iPhone SE)
- 390px (iPhone 14)
- 768px (iPad)
- 1024px (iPad landscape / small laptop)
- 1440px (desktop)

---

## CSS Architecture

### Variables first
All design decisions should be CSS variables:

```css
:root {
    /* Don't do this */
    /* color: #3b82f6; */
    
    /* Do this */
    --color-primary: #3b82f6;
}

.button {
    background: var(--color-primary);
}
```

### Naming convention
Use consistent naming:

```css
/* Colors */
--color-{name}: ;
--color-{name}-hover: ;
--color-{name}-active: ;

/* Typography */
--font-{family-purpose}: ;
--text-{size-name}: ;
--font-weight-{name}: ;
--line-height-{name}: ;
--letter-spacing-{name}: ;

/* Spacing */
--space-{size}: ;

/* Shadows */
--shadow-{size}: ;

/* Radii */
--radius-{size}: ;

/* Transitions */
--transition-{property}: ;
```

### Component classes
Use BEM-like naming:

```css
.card { }
.card--featured { }
.card__header { }
.card__body { }
.card__footer { }

.btn { }
.btn--primary { }
.btn--secondary { }
.btn--sm { }
.btn--lg { }
.btn:disabled { }
```

---

## Navigation System

Each design file includes JavaScript for navigation:

### Keyboard navigation
- `ArrowLeft` / `ArrowRight`: Previous/next design
- `Escape`: Return to gallery index
- `?` or `h`: Show help (optional)

### Touch navigation
- Swipe left/right on mobile
- Edge swipe detection

### Prefetching
- `<link rel="prefetch">` for adjacent pages
- Improves navigation speed

### Wrap-around
- Design N → Design 1 when navigating forward from last
- Design 1 → Design N when navigating backward from first

### Visual hint
- One-time toast/tooltip explaining navigation
- Use `localStorage` to show only once
- Style matches the design aesthetic

### Implementation

```javascript
(function() {
    const TOTAL_DESIGNS = [N];
    const CURRENT_DESIGN = [current];
    
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
            window.location.href = 'index.html';
        }
    });
    
    // Touch navigation
    let touchStartX = 0;
    document.addEventListener('touchstart', (e) => {
        touchStartX = e.touches[0].clientX;
    });
    document.addEventListener('touchend', (e) => {
        const touchEndX = e.changedTouches[0].clientX;
        const diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 50) {
            if (diff > 0) {
                // Swipe left - next
                const next = CURRENT_DESIGN === TOTAL_DESIGNS ? 1 : CURRENT_DESIGN + 1;
                window.location.href = `design-${next}.html`;
            } else {
                // Swipe right - prev
                const prev = CURRENT_DESIGN === 1 ? TOTAL_DESIGNS : CURRENT_DESIGN - 1;
                window.location.href = `design-${prev}.html`;
            }
        }
    });
    
    // Prefetch adjacent pages
    const prefetchNext = document.createElement('link');
    prefetchNext.rel = 'prefetch';
    prefetchNext.href = `design-${CURRENT_DESIGN === TOTAL_DESIGNS ? 1 : CURRENT_DESIGN + 1}.html`;
    document.head.appendChild(prefetchNext);
    
    const prefetchPrev = document.createElement('link');
    prefetchPrev.rel = 'prefetch';
    prefetchPrev.href = `design-${CURRENT_DESIGN === 1 ? TOTAL_DESIGNS : CURRENT_DESIGN - 1}.html`;
    document.head.appendChild(prefetchPrev);
    
    // One-time navigation hint
    if (!localStorage.getItem('design-nav-hint-shown')) {
        const hint = document.createElement('div');
        hint.className = 'nav-hint';
        hint.innerHTML = '← → Arrow keys to navigate • Esc for gallery';
        hint.style.cssText = `
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            padding: 12px 24px;
            background: var(--color-surface, #333);
            color: var(--color-text, #fff);
            border-radius: var(--radius-md, 8px);
            font-size: 14px;
            z-index: 9999;
            opacity: 0;
            transition: opacity 0.3s;
        `;
        document.body.appendChild(hint);
        
        setTimeout(() => hint.style.opacity = '1', 500);
        setTimeout(() => {
            hint.style.opacity = '0';
            setTimeout(() => hint.remove(), 300);
        }, 4000);
        
        localStorage.setItem('design-nav-hint-shown', 'true');
    }
})();
```

---

## Gallery Index Requirements

The `index.html` file serves as the gallery:

### Layout
- Grid of design preview cards
- Responsive: 1 col mobile, 2 col tablet, 3-4 col desktop
- Each card shows:
  - Design name
  - Visual preview (screenshot or representative colors)
  - Brief description
  - Key tags (e.g., "Minimalist", "Dark Mode", "Mobile-first")

### Navigation
- Arrow keys navigate the grid
- Enter opens selected design
- Visual focus indicator
- Search/filter functionality (optional but recommended)

### Metadata display
- Design number
- Style family
- Color scheme indicator
- Industry tag

---

## LLM Generation Prompt Template

When generating designs, use this prompt structure:

```
You are generating design #{ID} from the design manifest.

## Manifest Entry

{full JSON of the design entry from manifest}

## Requirements

Generate a complete, self-contained HTML file following these specifications:

1. **File structure**: Follow the exact structure from the Design Page Generator PRD
2. **Components**: Include all Tier 1 components, most Tier 2, and at least 3 Tier 3 mobile components
3. **Documentation**: The HTML comment block must be comprehensive enough that another LLM could replicate this design in any framework
4. **Accessibility**: Meet all WCAG 2.1 AA requirements
5. **Responsiveness**: Work from 375px to 1440px+
6. **Self-contained**: Only external dependency is Google Fonts

## Dimension Interpretation

Based on the manifest dimensions, implement:

- UI Paradigm "{ui_paradigm}": [specific implementation guidance]
- Design Era "{design_era}": [specific implementation guidance]
- Color System: {color_theory} + {color_temperature} + {color_saturation}
- Typography: {type_heading_class} headings + {type_body_class} body, {type_scale_ratio} scale
- [continue for all dimensions...]

## Creative Brief

Name: {name}
Tagline: {tagline}

Create a design that feels like: [interpretation of the dimension combination]

The design should be appropriate for: {industry} targeting {target_audience}
Emotional tone: {emotional_tone}
Cultural influence: {cultural_influence}

## Output

Generate the complete HTML file. Do not truncate or abbreviate. Include:
- Full HTML comment documentation block
- Complete CSS with all variables and component styles
- All showcase sections with real component examples
- Navigation JavaScript
- Structured JSON data block

The file should be immediately usable - someone should be able to open it in a browser and see a complete design system showcase.
```

---

## Batch Generation

For generating multiple designs:

### Batch prompt structure

```
Generate designs #{START} through #{END} from the attached manifest.

For each design:
1. Read its manifest entry
2. Generate the complete HTML file
3. Save as design-{id}.html

Process each design fully before moving to the next. Do not parallelize or abbreviate.

Manifest entries for this batch:
{JSON array of manifest entries for this batch}
```

### Recommended batch sizes
- Claude Code: 10-20 designs per batch
- Manual review after each batch
- Adjust if quality degrades

### Post-batch validation
After each batch, verify:
- [ ] All files created
- [ ] Each file opens without errors
- [ ] Components render correctly
- [ ] Navigation works between designs
- [ ] Mobile responsive
- [ ] Accessibility basics (focus states, contrast)

---

## Quality Checklist

For each generated design:

### Structure
- [ ] HTML comment documentation is comprehensive
- [ ] JSON data block is valid and complete
- [ ] All CSS variables are defined
- [ ] File is self-contained (no broken dependencies)

### Visual
- [ ] Design matches the manifest dimensions
- [ ] Colors are cohesive and accessible
- [ ] Typography hierarchy is clear
- [ ] Spacing is consistent

### Components
- [ ] All Tier 1 components present
- [ ] Components have all required states
- [ ] At least 3 mobile/app components
- [ ] Components are functional (buttons look clickable, inputs look editable)

### Accessibility
- [ ] Color contrast passes WCAG AA
- [ ] Focus indicators visible
- [ ] Touch targets 44px+
- [ ] Reduced motion respected

### Responsiveness
- [ ] Works at 375px
- [ ] Works at 768px
- [ ] Works at 1440px
- [ ] No horizontal scroll at any width

### Documentation
- [ ] LLM could recreate the design from the docs alone
- [ ] All tokens are documented
- [ ] Do's and Don'ts are specific to THIS design
- [ ] Examples show actual code

### Navigation
- [ ] Keyboard nav works
- [ ] Touch nav works on mobile
- [ ] Prefetch links present
- [ ] Hint toast appears once

---

## Example: Dimension Interpretation Guide

When an LLM receives manifest dimensions, here's how to interpret them:

### UI Paradigm interpretation

| Value | Implementation |
|-------|----------------|
| `flat` | No shadows, no gradients, solid colors, clean edges |
| `material` | Layered surfaces, subtle shadows, elevation system |
| `neumorphic` | Soft shadows both directions, monochromatic, extruded look |
| `glassmorphic` | `backdrop-filter: blur()`, transparency, border glow |
| `brutalist` | Raw borders, stark contrast, system fonts OK, visible structure |

### Color theory interpretation

| Value | Implementation |
|-------|----------------|
| `monochromatic` | Pick one hue, vary lightness (e.g., `hsl(220, 60%, 20-80%)`) |
| `complementary` | Two hues 180° apart (e.g., blue + orange) |
| `analogous` | Three adjacent hues (e.g., blue + teal + green) |
| `triadic` | Three hues 120° apart (e.g., red + yellow + blue) |

### Typography class interpretation

| Value | Font suggestions |
|-------|------------------|
| `geometric_sans` | Poppins, Montserrat, Futura, Quicksand |
| `humanist_sans` | Open Sans, Lato, Source Sans Pro, Nunito |
| `neo_grotesque` | Inter, Roboto, Helvetica Neue, Arial |
| `modern_serif` | Playfair Display, Bodoni Moda, Didot |
| `slab_serif` | Roboto Slab, Zilla Slab, Rockwell |

---

## Versioning & Updates

### Design file versioning
Each file contains version in JSON block:
```json
{
    "version": "1.0.0",
    "generated": "2025-01-06",
    "manifest_version": "1.0.0"
}
```

### Regeneration
If manifest dimensions change, files can be regenerated. Version number increments.

### Backward compatibility
Navigation JavaScript should handle missing designs gracefully (skip to next available).
