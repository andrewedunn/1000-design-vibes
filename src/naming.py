# ABOUTME: Generates creative names and taglines for designs.
# ABOUTME: Uses rule-based generation from dimension vocabularies.

import random

# Rule-based name components - rich vocabulary for varied names
TONE_WORDS = {
    "trustworthy": ["Solid", "Iron", "Steady", "True", "Core", "Anchor", "Foundation", "Bastion", "Pillar", "Fortress"],
    "playful": ["Bubble", "Bounce", "Fizz", "Pop", "Zigzag", "Confetti", "Spritz", "Whimsy", "Quirk", "Twist"],
    "serious": ["Apex", "Vertex", "Stratum", "Prime", "Axiom", "Helix", "Matrix", "Protocol", "Canon", "Thesis"],
    "luxurious": ["Noir", "Velvet", "Opulent", "Regal", "Lux", "Satin", "Gilded", "Imperial", "Majestic", "Royal"],
    "friendly": ["Sunny", "Meadow", "Hearth", "Warm", "Breeze", "Harbor", "Haven", "Oasis", "Bloom", "Garden"],
    "edgy": ["Razor", "Glitch", "Void", "Neon", "Clash", "Fracture", "Static", "Pulse", "Riot", "Surge"],
    "calm": ["Misty", "Willow", "Drift", "Serene", "Haze", "Zen", "Tranquil", "Still", "Whisper", "Echo"],
    "energetic": ["Bolt", "Surge", "Ignite", "Flash", "Spark", "Blaze", "Thunder", "Volt", "Kinetic", "Turbo"],
    "mysterious": ["Shadow", "Enigma", "Mystic", "Obsidian", "Phantom", "Cipher", "Shroud", "Veil", "Dusk", "Twilight"],
    "nostalgic": ["Retro", "Vintage", "Classic", "Heritage", "Timeless", "Antique", "Revival", "Epoch", "Era", "Legacy"],
}

TEMP_WORDS = {
    "cool": ["Frost", "Ice", "Arctic", "Blue", "Glacier", "Winter", "Crystal", "Nordic", "Tundra", "Polar"],
    "warm": ["Ember", "Sunset", "Amber", "Flame", "Coral", "Terra", "Copper", "Sienna", "Blush", "Rose"],
    "neutral": ["Stone", "Slate", "Ash", "Carbon", "Steel", "Graphite", "Pewter", "Chalk", "Marble", "Quartz"],
    "mixed": ["Prism", "Spectrum", "Blend", "Fusion", "Duo", "Mosaic", "Palette", "Gradient", "Shift", "Flow"],
}

CULTURE_WORDS = {
    "japanese": ["Zen", "Sakura", "Kaze", "Mizu", "Sora", "Ori", "Kyo", "Tori"],
    "scandinavian": ["Nordic", "Fjord", "Birch", "Hygge", "Frost", "Lund", "Saga", "Tide"],
    "mediterranean": ["Azure", "Olive", "Terra", "Cove", "Coast", "Sol", "Porto", "Mare"],
    "african": ["Savanna", "Baobab", "Safari", "Kente", "Sahel", "Zulu", "Serengeti", "Nubia"],
    "latin_american": ["Sol", "Luna", "Fiesta", "Alma", "Vida", "Fuego", "Cielo", "Tropic"],
    "middle_eastern": ["Oasis", "Dune", "Minaret", "Bazaar", "Saffron", "Jasmine", "Kasbah", "Silk"],
    "south_asian": ["Lotus", "Mandala", "Sari", "Indigo", "Jasmine", "Chai", "Monsoon", "Spice"],
    "eastern_european": ["Slavic", "Amber", "Birch", "Steppe", "Winter", "Taiga", "Aurora", "Frost"],
    "international": ["Global", "Metro", "Urban", "Cosmo", "Prime", "Core", "Nexus", "Hub"],
    "indigenous": ["Terra", "Root", "Spirit", "Sky", "Earth", "River", "Stone", "Ancient"],
}

PARADIGM_WORDS = {
    "flat": ["Clean", "Pure", "Clear", "Crisp", "Stark"],
    "material": ["Layer", "Depth", "Surface", "Float", "Lift"],
    "neumorphic": ["Soft", "Sculpt", "Mold", "Shape", "Form"],
    "skeuomorphic": ["Real", "Tangible", "Touch", "Craft", "Made"],
    "brutalist": ["Raw", "Bold", "Block", "Mass", "Force"],
    "glassmorphic": ["Glass", "Blur", "Frost", "Trans", "Lucent"],
    "claymorphic": ["Clay", "Dough", "Pillow", "Plush", "Soft"],
    "web3_defi": ["Chain", "Node", "Token", "Link", "Hash"],
    "web2_glossy": ["Gloss", "Shine", "Chrome", "Mirror", "Sheen"],
    "minimalist": ["Zero", "Void", "Null", "Sparse", "Bare"],
}

ERA_WORDS = {
    "bauhaus": ["Gropius", "Weimar", "Function", "Modular", "Grid"],
    "art_deco": ["Deco", "Gatsby", "Luxe", "Gilded", "Jazz"],
    "mid_century_modern": ["Eames", "Atomic", "Starburst", "Retro", "Mid"],
    "memphis": ["Memphis", "Squiggle", "Radical", "Pop", "Wild"],
    "swiss_international": ["Helvetica", "Grid", "Order", "System", "Type"],
    "y2k": ["Cyber", "Digi", "Glitch", "Pixel", "Dot"],
    "contemporary": ["Now", "Current", "Today", "Modern", "Fresh"],
    "futurism": ["Hyper", "Ultra", "Neo", "Future", "Next"],
    "vaporwave": ["Wave", "Vapor", "Neon", "Retro", "Dream"],
    "art_nouveau": ["Nouveau", "Flora", "Vine", "Curve", "Bloom"],
}

TAGLINE_TEMPLATES = [
    "{era} design with {mood} {temp} tones",
    "A {paradigm} approach meets {culture} sensibility",
    "{mood} vibes for {industry}",
    "Where {paradigm} meets {culture} aesthetics",
    "{era}-inspired design for {audience}",
    "{culture} minimalism with {mood} undertones",
    "The {paradigm} way to {industry}",
    "{mood} meets {temp}: a {era} perspective",
    "Crafted for {audience} with {culture} roots",
    "{temp} palette, {mood} spirit",
]


def generate_name(dimensions: dict[str, str]) -> tuple[str, str]:
    """Generate a name and tagline using rule-based logic."""
    tone = dimensions.get("emotional_tone", "friendly")
    temp = dimensions.get("color_temperature", "neutral")
    culture = dimensions.get("cultural_influence", "international")
    paradigm = dimensions.get("ui_paradigm", "flat")
    era = dimensions.get("design_era", "contemporary")

    # Build name from multiple word sources for variety
    name_strategies = [
        # Tone + Temperature (e.g., "Serene Frost")
        lambda: f"{random.choice(TONE_WORDS.get(tone, ['Design']))} {random.choice(TEMP_WORDS.get(temp, ['System']))}",
        # Culture word + Temperature (e.g., "Nordic Crystal")
        lambda: f"{random.choice(CULTURE_WORDS.get(culture, ['Global']))} {random.choice(TEMP_WORDS.get(temp, ['Flow']))}",
        # Paradigm word + Culture word (e.g., "Glass Fjord")
        lambda: f"{random.choice(PARADIGM_WORDS.get(paradigm, ['Modern']))} {random.choice(CULTURE_WORDS.get(culture, ['Hub']))}",
        # Era word + Tone word (e.g., "Atomic Spark")
        lambda: f"{random.choice(ERA_WORDS.get(era, ['Modern']))} {random.choice(TONE_WORDS.get(tone, ['Core']))}",
        # Tone + Culture (e.g., "Velvet Sakura")
        lambda: f"{random.choice(TONE_WORDS.get(tone, ['Prime']))} {random.choice(CULTURE_WORDS.get(culture, ['Core']))}",
    ]

    name = random.choice(name_strategies)()

    # Build tagline
    era_str = era.replace("_", " ").title()
    paradigm_str = paradigm.replace("_", " ")
    culture_str = culture.replace("_", " ").title()
    industry = dimensions.get("industry", "tech").replace("_", " ")
    audience = dimensions.get("target_audience", "users").replace("_", " ")
    mood = dimensions.get("color_palette_mood", "natural").replace("_", " ")

    template = random.choice(TAGLINE_TEMPLATES)
    tagline = template.format(
        era=era_str,
        paradigm=paradigm_str,
        culture=culture_str,
        industry=industry,
        audience=audience,
        mood=mood,
        temp=temp,
    )

    return name, tagline.capitalize()
