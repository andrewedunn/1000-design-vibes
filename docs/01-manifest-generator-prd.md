# Design Manifest Generator PRD

## Overview

The manifest generator creates a JSON file containing unique "design seeds" — structured specifications that define every visual aspect of a design. Each seed is a unique combination of dimensions that an LLM will use to generate a self-contained HTML design showcase.

## Goals

1. **Uniqueness**: Every manifest entry must be mathematically unique across all dimensions
2. **Diversity**: Ensure broad coverage across all dimension values (no clustering)
3. **Reproducibility**: Same seed → same manifest entry (deterministic)
4. **Extensibility**: Easy to add new dimensions or values
5. **Batch-friendly**: Support generating subsets (designs 1-20, 21-40, etc.)

---

## Manifest Structure

### Top-level schema

```json
{
  "version": "1.0.0",
  "generated_at": "2025-01-06T12:00:00Z",
  "total_designs": 1000,
  "dimensions_version": "1.0.0",
  "designs": [
    { /* Design entry */ }
  ]
}
```

### Individual design entry schema

```json
{
  "id": 1,
  "seed": "a1b2c3d4e5f6",
  "name": "Nordic Frost",
  "tagline": "Clean Scandinavian minimalism with icy blue accents",
  
  "dimensions": {
    "ui_paradigm": "flat",
    "design_era": "scandinavian_modern",
    "density": "airy",
    
    "color_theory": "analogous",
    "color_temperature": "cool",
    "color_saturation": "muted",
    "color_contrast": "medium",
    "color_palette_mood": "natural",
    "color_mode": "light_only",
    
    "type_heading_class": "geometric_sans",
    "type_body_class": "humanist_sans",
    "type_scale_ratio": "perfect_fourth",
    "type_case_treatment": "normal",
    "type_letter_spacing": "normal",
    "type_line_height": "normal",
    
    "corner_radius": "subtle",
    "spacing_base": "8px",
    "border_style": "hairline",
    "shadow_style": "subtle",
    "container_style": "outlined",
    
    "grid_system": "12_column",
    "alignment": "left",
    "hierarchy_approach": "whitespace",
    
    "surface_texture": "none",
    "gradient_usage": "none",
    "icon_style": "outlined",
    
    "industry": "saas",
    "target_audience": "enterprise",
    "emotional_tone": "trustworthy",
    "cultural_influence": "scandinavian"
  },
  
  "generated_name_hints": {
    "brand_style": "two_word_compound",
    "examples": ["Clearpath", "Northbeam", "Frostline"]
  },
  
  "meta": {
    "dimension_hash": "sha256:abc123...",
    "uniqueness_verified": true
  }
}
```

---

## Dimension Definitions

### Tier 1: Core Visual Style

#### `ui_paradigm`
The foundational visual treatment approach.

| Value | Description |
|-------|-------------|
| `skeuomorphic` | Mimics real-world materials and textures |
| `flat` | Two-dimensional, no shadows or gradients |
| `material` | Google's layered paper metaphor with shadows |
| `neumorphic` | Soft, extruded elements with subtle shadows |
| `glassmorphic` | Frosted glass with blur and transparency |
| `brutalist` | Raw, stark, intentionally unpolished |
| `claymorphic` | 3D, inflated, toy-like appearance |
| `organic` | Flowing, natural shapes, blob-like |
| `editorial` | Magazine-inspired, typography-focused |

#### `design_era`
Historical design movement influence.

| Value | Description |
|-------|-------------|
| `arts_and_crafts` | 1880s-1920s handcrafted, ornate |
| `art_nouveau` | 1890-1910 flowing, organic, decorative |
| `art_deco` | 1920s-1930s geometric, glamorous, symmetrical |
| `bauhaus` | 1919-1933 functional, geometric, primary colors |
| `mid_century_modern` | 1940s-1960s clean lines, organic curves |
| `swiss_international` | 1950s-1960s grid, helvetica, objective |
| `pop_art` | 1950s-1960s bold, colorful, comic-like |
| `psychedelic` | 1960s-1970s swirling, vibrant, trippy |
| `punk` | 1970s-1980s DIY, collage, ransom-note |
| `memphis` | 1980s geometric, colorful, playful |
| `grunge` | 1990s distressed, textured, dark |
| `y2k` | 1998-2004 glossy, tech-optimist, chrome |
| `web2_glossy` | 2004-2010 gradients, reflections, badges |
| `flat_2010s` | 2010-2015 minimal, colorful, no shadows |
| `neo_brutalist` | 2020s bold borders, raw, high contrast |
| `scandinavian_modern` | Minimal, functional, light, natural |

#### `density`
Information and element density.

| Value | Description |
|-------|-------------|
| `ultra_airy` | Maximum whitespace, very few elements |
| `airy` | Generous spacing, breathing room |
| `balanced` | Standard comfortable spacing |
| `compact` | Tighter spacing, more content visible |
| `dense` | Minimal spacing, data-heavy |
| `ultra_dense` | Dashboard/terminal density |

---

### Tier 2: Color System

#### `color_theory`
Color relationship approach.

| Value | Description |
|-------|-------------|
| `monochromatic` | Single hue, varying lightness/saturation |
| `analogous` | Adjacent colors on wheel |
| `complementary` | Opposite colors on wheel |
| `split_complementary` | Base + two adjacent to complement |
| `triadic` | Three evenly spaced colors |
| `tetradic` | Four colors, two complementary pairs |
| `neutral_with_accent` | Grays/neutrals with one pop color |

#### `color_temperature`
Overall warmth/coolness.

| Value | Description |
|-------|-------------|
| `cool` | Blues, greens, purples dominate |
| `warm` | Reds, oranges, yellows dominate |
| `neutral` | Grays, tans, balanced |
| `mixed` | Intentional warm/cool contrast |

#### `color_saturation`
Intensity of colors.

| Value | Description |
|-------|-------------|
| `desaturated` | Muted, grayish tones |
| `muted` | Slightly reduced saturation |
| `balanced` | Natural saturation |
| `vivid` | High saturation, punchy |
| `hyper_saturated` | Neon, electric intensity |

#### `color_contrast`
Value range between lightest and darkest.

| Value | Description |
|-------|-------------|
| `low` | Subtle, soft transitions |
| `medium` | Standard readable contrast |
| `high` | Strong black/white presence |
| `extreme` | Maximum contrast, stark |

#### `color_palette_mood`
Emotional/thematic color family.

| Value | Description |
|-------|-------------|
| `earth` | Browns, tans, forest greens, terracotta |
| `pastel` | Soft, light, Easter-egg colors |
| `jewel` | Rich sapphire, emerald, ruby, amethyst |
| `metallic` | Gold, silver, bronze, copper |
| `primary` | Pure red, blue, yellow |
| `monochrome` | Black, white, grays only |
| `neon` | Electric, glowing colors |
| `cyber` | Magenta, cyan, purple, tech colors |
| `natural` | Greens, blues, sky, water, earth |
| `candy` | Bright pinks, aquas, playful |

#### `color_mode`
Light/dark mode support.

| Value | Description |
|-------|-------------|
| `light_only` | Light background only |
| `dark_only` | Dark background only |
| `both` | Includes theme toggle |

---

### Tier 3: Typography

#### `type_heading_class`
Font classification for headings.

| Value | Description | Example families |
|-------|-------------|------------------|
| `geometric_sans` | Constructed, circular | Futura, Poppins, Montserrat |
| `humanist_sans` | Calligraphic influence | Open Sans, Lato, Source Sans |
| `neo_grotesque` | Neutral, uniform | Helvetica, Inter, Roboto |
| `modern_serif` | High contrast, vertical | Didot, Bodoni, Playfair |
| `transitional_serif` | Medium contrast | Times, Georgia, Libre Baskerville |
| `old_style_serif` | Low contrast, angled | Garamond, Palatino, EB Garamond |
| `slab_serif` | Heavy, block serifs | Rockwell, Roboto Slab, Zilla Slab |
| `monospace` | Fixed-width | JetBrains Mono, Fira Code, IBM Plex Mono |
| `display` | Decorative, headline-only | Various display faces |
| `handwritten` | Script, casual | Caveat, Patrick Hand |

#### `type_body_class`
Font classification for body text. Same values as heading.

#### `type_scale_ratio`
Mathematical relationship between type sizes.

| Value | Ratio | Description |
|-------|-------|-------------|
| `minor_second` | 1.067 | Very tight, subtle |
| `major_second` | 1.125 | Tight, compact |
| `minor_third` | 1.200 | Standard, comfortable |
| `major_third` | 1.250 | Generous |
| `perfect_fourth` | 1.333 | Pronounced hierarchy |
| `golden_ratio` | 1.618 | Dramatic, classical |

#### `type_case_treatment`
Text transformation approach.

| Value | Description |
|-------|-------------|
| `normal` | Standard mixed case |
| `uppercase_headings` | ALL CAPS for headings |
| `small_caps` | Small capitals for emphasis |
| `lowercase_only` | No capitals anywhere |

#### `type_letter_spacing`
Tracking adjustment.

| Value | Description |
|-------|-------------|
| `tight` | -2% to -1% |
| `normal` | 0% |
| `loose` | +2% to +5% |
| `very_loose` | +8% to +12% |

#### `type_line_height`
Leading/line-height.

| Value | Description |
|-------|-------------|
| `tight` | 1.2 |
| `normal` | 1.5 |
| `loose` | 1.75 |
| `very_loose` | 2.0 |

---

### Tier 4: Shape & Space

#### `corner_radius`
Border radius philosophy.

| Value | Description |
|-------|-------------|
| `sharp` | 0px, no rounding |
| `subtle` | 2-4px, barely visible |
| `rounded` | 8-12px, clearly rounded |
| `very_rounded` | 16-24px, soft |
| `pill` | 50%/9999px, full round |
| `organic` | Irregular, blob-like |

#### `spacing_base`
Base unit for spacing grid.

| Value | Description |
|-------|-------------|
| `4px` | 4px base unit |
| `8px` | 8px base unit (most common) |
| `10px` | 10px base unit |
| `12px` | 12px base unit |

#### `border_style`
Border treatment.

| Value | Description |
|-------|-------------|
| `none` | No borders |
| `hairline` | 1px subtle |
| `thin` | 2px visible |
| `medium` | 3-4px pronounced |
| `thick` | 5px+ bold |
| `double` | Double-line borders |
| `dashed` | Dashed lines |

#### `shadow_style`
Shadow treatment.

| Value | Description |
|-------|-------------|
| `none` | No shadows |
| `subtle` | Barely visible, soft |
| `medium` | Standard drop shadow |
| `hard` | Sharp, defined edge |
| `dramatic` | Long, offset shadows |
| `colored` | Tinted shadows |
| `layered` | Multiple stacked shadows |
| `inset` | Inner shadows (neumorphic) |

#### `container_style`
How containers/cards are defined.

| Value | Description |
|-------|-------------|
| `open` | No visual boundary |
| `outlined` | Border only, transparent |
| `filled` | Solid background |
| `floating` | Shadow-defined |
| `inset` | Recessed appearance |

---

### Tier 5: Layout

#### `grid_system`
Layout grid approach.

| Value | Description |
|-------|-------------|
| `single_column` | One column, vertical flow |
| `two_column` | Two equal columns |
| `three_column` | Three columns |
| `four_column` | Four columns |
| `twelve_column` | 12-column fluid grid |
| `asymmetric` | Intentionally unequal |
| `modular` | Module-based grid |
| `broken` | Overlapping, rule-breaking |
| `freeform` | No grid constraints |

#### `alignment`
Text and element alignment.

| Value | Description |
|-------|-------------|
| `left` | Left-aligned (LTR default) |
| `center` | Centered |
| `right` | Right-aligned |
| `justified` | Full justification |
| `mixed` | Intentionally varied |

#### `hierarchy_approach`
Primary method for creating visual hierarchy.

| Value | Description |
|-------|-------------|
| `size` | Size differences dominate |
| `color` | Color/saturation differences |
| `position` | Placement creates hierarchy |
| `weight` | Font weight differences |
| `whitespace` | Spacing creates importance |

---

### Tier 6: Texture & Detail

#### `surface_texture`
Background/surface treatment.

| Value | Description |
|-------|-------------|
| `none` | Smooth, flat |
| `noise` | Subtle grain/noise |
| `paper` | Paper-like texture |
| `fabric` | Woven/textile feel |
| `gradient_mesh` | Complex gradient backgrounds |
| `geometric_pattern` | Repeating geometric shapes |
| `organic_pattern` | Natural, irregular patterns |

#### `gradient_usage`
Gradient application.

| Value | Description |
|-------|-------------|
| `none` | No gradients |
| `subtle_background` | Very soft bg gradients |
| `accent` | Gradients on CTAs/accents |
| `duotone` | Two-color image treatment |
| `mesh` | Complex multi-stop gradients |
| `glassmorphic` | Blur + transparency |

#### `icon_style`
Icon treatment.

| Value | Description |
|-------|-------------|
| `outlined` | Stroke-only icons |
| `filled` | Solid filled icons |
| `duotone` | Two-tone icons |
| `hand_drawn` | Sketchy, imperfect |
| `isometric` | 3D isometric |
| `emoji` | Emoji as icons |

---

### Tier 7: Context

#### `industry`
Target industry vertical.

| Value | Description |
|-------|-------------|
| `finance` | Banking, fintech, investing |
| `healthcare` | Medical, wellness, health tech |
| `education` | EdTech, learning, academic |
| `ecommerce` | Online retail, marketplaces |
| `saas` | B2B software, productivity |
| `gaming` | Games, entertainment |
| `media` | News, video, content |
| `food` | Restaurants, delivery, recipes |
| `travel` | Booking, hospitality |
| `real_estate` | Property, listings |
| `fashion` | Apparel, luxury goods |
| `fitness` | Gyms, workout apps |
| `nonprofit` | Charities, causes |
| `government` | Public sector, civic |
| `creative` | Agencies, portfolios |
| `developer` | Dev tools, APIs, docs |

#### `target_audience`
Primary user demographic.

| Value | Description |
|-------|-------------|
| `enterprise` | Large business users |
| `smb` | Small/medium business |
| `consumer_mass` | General public |
| `consumer_premium` | Luxury/premium consumers |
| `developer` | Technical users |
| `children` | Kids, family |
| `seniors` | Older adults |
| `gen_z` | Younger generation |

#### `emotional_tone`
Intended emotional response.

| Value | Description |
|-------|-------------|
| `trustworthy` | Reliable, secure |
| `playful` | Fun, lighthearted |
| `serious` | Professional, formal |
| `luxurious` | Premium, exclusive |
| `friendly` | Approachable, warm |
| `edgy` | Bold, rebellious |
| `calm` | Peaceful, serene |
| `energetic` | Dynamic, exciting |
| `mysterious` | Intriguing, dark |
| `nostalgic` | Retro, sentimental |

#### `cultural_influence`
Geographic/cultural design tradition.

| Value | Description |
|-------|-------------|
| `scandinavian` | Nordic minimal, hygge |
| `japanese` | Wabi-sabi, zen, minimal |
| `mediterranean` | Warm, terracotta, tiles |
| `american_corporate` | Professional, blue-chip |
| `british_traditional` | Heritage, refined |
| `german_industrial` | Engineered, precise |
| `french_elegant` | Chic, sophisticated |
| `latin_vibrant` | Colorful, energetic |
| `african_bold` | Geometric, earth tones |
| `middle_eastern` | Ornate, geometric patterns |

---

## Uniqueness Enforcement

### Hash-based deduplication

Each design's dimensions are serialized and hashed:

```python
def compute_dimension_hash(dimensions: dict) -> str:
    # Sort keys for consistent ordering
    serialized = json.dumps(dimensions, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()
```

### Uniqueness verification

Before adding a design to the manifest:

1. Compute the dimension hash
2. Check against all existing hashes in the manifest
3. Reject if duplicate found
4. Store hash in design's `meta.dimension_hash`

### Minimum distance enforcement (optional)

To prevent "near duplicates" that differ by only one dimension:

```python
def dimension_distance(d1: dict, d2: dict) -> int:
    """Count how many dimensions differ between two designs."""
    differences = 0
    for key in d1.keys():
        if d1[key] != d2[key]:
            differences += 1
    return differences

# Require at least 3 dimensions to differ
MIN_DISTANCE = 3
```

---

## Name Generation

Each design needs a memorable name. Generate based on dimensions:

### Naming strategies by emotional tone

| Tone | Pattern | Examples |
|------|---------|----------|
| `trustworthy` | Solid + noun | Ironclad, Steadfast, Bedrock |
| `playful` | Quirky compound | Bubblepop, Zigzag, Boing |
| `serious` | Latin/Greek roots | Apex, Vertex, Stratum |
| `luxurious` | French/Italian | Noir, Velvet, Opulent |
| `friendly` | Warm + familiar | Hearthstone, Sunbeam, Meadow |
| `edgy` | Sharp + tech | Razor, Glitch, Void |
| `calm` | Nature + soft | Misty, Willow, Drift |
| `energetic` | Action + power | Bolt, Surge, Ignite |

### Include in manifest

```json
{
  "name": "Nordic Frost",
  "tagline": "Clean Scandinavian minimalism with icy blue accents",
  "generated_name_hints": {
    "style": "nature_compound",
    "alternatives": ["Glacier", "Fjordline", "Snowcap"]
  }
}
```

---

## Generation Algorithm

### Phase 1: Dimension value distribution

Ensure each dimension value appears roughly equally:

```python
def generate_balanced_combinations(n_designs: int) -> list:
    """Generate combinations with balanced dimension coverage."""
    
    combinations = []
    dimension_counts = defaultdict(lambda: defaultdict(int))
    
    for i in range(n_designs):
        combo = {}
        for dim_name, dim_values in DIMENSIONS.items():
            # Weight toward underrepresented values
            weights = []
            for value in dim_values:
                count = dimension_counts[dim_name][value]
                # Inverse weighting: less used = higher weight
                weights.append(1.0 / (count + 1))
            
            # Normalize weights
            total = sum(weights)
            weights = [w / total for w in weights]
            
            # Sample with weights
            chosen = random.choices(dim_values, weights=weights)[0]
            combo[dim_name] = chosen
            dimension_counts[dim_name][chosen] += 1
        
        combinations.append(combo)
    
    return combinations
```

### Phase 2: Uniqueness check

```python
def ensure_uniqueness(combinations: list) -> list:
    """Remove duplicates and regenerate."""
    
    seen_hashes = set()
    unique_combos = []
    
    for combo in combinations:
        h = compute_dimension_hash(combo)
        if h not in seen_hashes:
            seen_hashes.add(h)
            unique_combos.append(combo)
        else:
            # Regenerate this slot
            new_combo = regenerate_unique(combo, seen_hashes)
            unique_combos.append(new_combo)
            seen_hashes.add(compute_dimension_hash(new_combo))
    
    return unique_combos
```

### Phase 3: Name generation

```python
def generate_name(dimensions: dict) -> dict:
    """Generate a name based on dimensions."""
    
    # Use LLM or rule-based generator
    # Return name + tagline + alternatives
    pass
```

---

## CLI Interface

```bash
# Generate full manifest
python manifest_generator.py --count 1000 --output manifest.json

# Generate specific range (for incremental generation)
python manifest_generator.py --start 501 --end 600 --output manifest_501_600.json

# Merge manifests
python manifest_generator.py merge manifest_1_500.json manifest_501_1000.json --output manifest.json

# Validate manifest (check uniqueness, completeness)
python manifest_generator.py validate manifest.json

# Export single design for testing
python manifest_generator.py export --id 42 --output design_42_spec.json

# Statistics
python manifest_generator.py stats manifest.json
# Output: dimension value distribution, uniqueness confirmation, etc.
```

---

## Output Files

### `manifest.json`
The complete manifest with all designs.

### `manifest_schema.json`
JSON Schema for validation.

### `dimensions.json`
The dimension definitions (for documentation and validation).

### `stats.json`
Generation statistics:
- Dimension value distribution
- Uniqueness metrics
- Generation timestamp
- Version info

---

## Versioning

### Manifest version
Increment when manifest structure changes.

### Dimensions version
Increment when dimensions or values change.

Both versions stored in manifest for compatibility checking.

---

## Testing

### Unit tests
- Uniqueness verification
- Dimension coverage balance
- Hash computation consistency

### Integration tests
- Full 1000-design generation
- Merge operations
- CLI interface

### Validation tests
- Schema compliance
- Required fields present
- Dimension values valid

---

## Future Enhancements

1. **Constraint rules**: Define soft constraints (e.g., "glassmorphic prefers cool colors")
2. **Weighted sampling**: Bias toward certain combinations
3. **Exclusion rules**: Prevent specific combinations
4. **LLM-assisted naming**: Use Claude for creative names
5. **Visual clustering**: Post-generation analysis of style similarity
6. **User preferences**: Allow users to influence generation (more minimalist, more colorful, etc.)
