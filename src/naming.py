# ABOUTME: Generates creative names and taglines for designs.
# ABOUTME: Uses Claude API when available, falls back to rule-based generation.

import json
import os
import random

from rich.console import Console

console = Console()

# Rule-based name components for fallback
PREFIXES = {
    "trustworthy": ["Solid", "Iron", "Steady", "True", "Core"],
    "playful": ["Bubble", "Bounce", "Fizz", "Pop", "Zigzag"],
    "serious": ["Apex", "Vertex", "Stratum", "Prime", "Axiom"],
    "luxurious": ["Noir", "Velvet", "Opulent", "Regal", "Lux"],
    "friendly": ["Sunny", "Meadow", "Hearth", "Warm", "Breeze"],
    "edgy": ["Razor", "Glitch", "Void", "Neon", "Clash"],
    "calm": ["Misty", "Willow", "Drift", "Serene", "Haze"],
    "energetic": ["Bolt", "Surge", "Ignite", "Flash", "Spark"],
    "mysterious": ["Shadow", "Enigma", "Mystic", "Obsidian", "Phantom"],
    "nostalgic": ["Retro", "Vintage", "Classic", "Heritage", "Timeless"],
}

SUFFIXES = {
    "cool": ["Frost", "Ice", "Arctic", "Blue", "Glacier"],
    "warm": ["Ember", "Sunset", "Amber", "Flame", "Coral"],
    "neutral": ["Stone", "Slate", "Ash", "Carbon", "Steel"],
    "mixed": ["Prism", "Spectrum", "Blend", "Fusion", "Duo"],
}

TAGLINE_TEMPLATES = [
    "{era} design with {mood} {temp} tones",
    "A {paradigm} approach meets {culture} sensibility",
    "{mood} vibes for {industry} with {era} influence",
    "Where {paradigm} meets {culture} minimalism",
    "{era}-inspired {paradigm} for {audience}",
]


def generate_name_fallback(dimensions: dict[str, str]) -> tuple[str, str]:
    """Generate a name and tagline using rule-based logic."""
    tone = dimensions.get("emotional_tone", "friendly")
    temp = dimensions.get("color_temperature", "neutral")

    prefix = random.choice(PREFIXES.get(tone, ["Design"]))
    suffix = random.choice(SUFFIXES.get(temp, ["System"]))
    name = f"{prefix}{suffix}"

    era = dimensions.get("design_era", "modern").replace("_", " ")
    paradigm = dimensions.get("ui_paradigm", "flat").replace("_", " ")
    culture = dimensions.get("cultural_influence", "international").replace("_", " ")
    industry = dimensions.get("industry", "tech").replace("_", " ")
    audience = dimensions.get("target_audience", "users").replace("_", " ")
    mood = dimensions.get("color_palette_mood", "natural").replace("_", " ")

    template = random.choice(TAGLINE_TEMPLATES)
    tagline = template.format(
        era=era.title(),
        paradigm=paradigm,
        culture=culture.title(),
        industry=industry,
        audience=audience,
        mood=mood,
        temp=temp,
    )

    return name, tagline.capitalize()


def generate_names_with_claude(designs: list[dict[str, str]]) -> list[tuple[str, str]]:
    """Generate names using Claude API."""
    try:
        import anthropic
    except ImportError:
        console.print("[yellow]anthropic package not installed, using fallback names[/yellow]")
        return [generate_name_fallback(d) for d in designs]

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[yellow]ANTHROPIC_API_KEY not set, using fallback names[/yellow]")
        return [generate_name_fallback(d) for d in designs]

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Generate creative names and taglines for {len(designs)} design systems.

For each design, I'll give you the key dimensions. Generate:
1. A memorable 1-2 word name (like "Nordic Frost", "Midnight Protocol", "Coral Reef")
2. A one-sentence tagline describing the aesthetic

Respond with a JSON array of objects with "name" and "tagline" fields.

Designs:
"""
    for i, dims in enumerate(designs, 1):
        key_dims = {
            "ui_paradigm": dims.get("ui_paradigm"),
            "design_era": dims.get("design_era"),
            "emotional_tone": dims.get("emotional_tone"),
            "color_temperature": dims.get("color_temperature"),
            "color_palette_mood": dims.get("color_palette_mood"),
            "cultural_influence": dims.get("cultural_influence"),
            "industry": dims.get("industry"),
        }
        prompt += f"\n{i}. {json.dumps(key_dims)}"

    prompt += "\n\nRespond with ONLY a valid JSON array, no other text."

    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )

        response_text = response.content[0].text.strip()
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
            response_text = response_text.strip()

        names_data = json.loads(response_text)
        return [(item["name"], item["tagline"]) for item in names_data]

    except Exception as e:
        console.print(f"[yellow]Claude API error: {e}[/yellow]")
        console.print("[yellow]Falling back to rule-based names[/yellow]")
        return [generate_name_fallback(d) for d in designs]


def generate_names_batch(
    designs: list[dict[str, str]],
    batch_size: int = 20,
) -> list[tuple[str, str]]:
    """Generate names for designs, batching API calls."""
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        console.print("[yellow]No API key found, using rule-based names[/yellow]")
        return [generate_name_fallback(d) for d in designs]

    results: list[tuple[str, str]] = []

    for i in range(0, len(designs), batch_size):
        batch = designs[i : i + batch_size]
        console.print(f"  Generating names {i + 1}-{i + len(batch)}...")
        batch_results = generate_names_with_claude(batch)
        results.extend(batch_results)

    return results
