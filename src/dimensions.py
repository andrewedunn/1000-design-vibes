# ABOUTME: Defines all design dimensions and their possible values.
# ABOUTME: These dimensions combine to create unique design system specifications.

from dataclasses import dataclass


@dataclass
class Dimension:
    """A design dimension with its possible values and descriptions."""
    name: str
    description: str
    values: dict[str, str]  # value -> description


# Tier 1: Core Visual Style

UI_PARADIGM = Dimension(
    name="ui_paradigm",
    description="The foundational visual treatment approach",
    values={
        "skeuomorphic": "Mimics real-world materials and textures",
        "flat": "Two-dimensional, no shadows or gradients",
        "material": "Google's layered paper metaphor with shadows",
        "neumorphic": "Soft, extruded elements with subtle shadows",
        "glassmorphic": "Frosted glass with blur and transparency",
        "brutalist": "Raw, stark, intentionally unpolished",
        "claymorphic": "3D, inflated, toy-like appearance",
        "organic": "Flowing, natural shapes, blob-like",
        "editorial": "Magazine-inspired, typography-focused",
    },
)

DESIGN_ERA = Dimension(
    name="design_era",
    description="Historical design movement influence",
    values={
        "arts_and_crafts": "1880s-1920s handcrafted, ornate",
        "art_nouveau": "1890-1910 flowing, organic, decorative",
        "art_deco": "1920s-1930s geometric, glamorous, symmetrical",
        "bauhaus": "1919-1933 functional, geometric, primary colors",
        "mid_century_modern": "1940s-1960s clean lines, organic curves",
        "swiss_international": "1950s-1960s grid, helvetica, objective",
        "pop_art": "1950s-1960s bold, colorful, comic-like",
        "psychedelic": "1960s-1970s swirling, vibrant, trippy",
        "punk": "1970s-1980s DIY, collage, ransom-note",
        "memphis": "1980s geometric, colorful, playful",
        "grunge": "1990s distressed, textured, dark",
        "y2k": "1998-2004 glossy, tech-optimist, chrome",
        "web2_glossy": "2004-2010 gradients, reflections, badges",
        "flat_2010s": "2010-2015 minimal, colorful, no shadows",
        "neo_brutalist": "2020s bold borders, raw, high contrast",
        "scandinavian_modern": "Minimal, functional, light, natural",
    },
)

DENSITY = Dimension(
    name="density",
    description="Information and element density",
    values={
        "ultra_airy": "Maximum whitespace, very few elements",
        "airy": "Generous spacing, breathing room",
        "balanced": "Standard comfortable spacing",
        "compact": "Tighter spacing, more content visible",
        "dense": "Minimal spacing, data-heavy",
        "ultra_dense": "Dashboard/terminal density",
    },
)

# Tier 2: Color System

COLOR_THEORY = Dimension(
    name="color_theory",
    description="Color relationship approach",
    values={
        "monochromatic": "Single hue, varying lightness/saturation",
        "analogous": "Adjacent colors on wheel",
        "complementary": "Opposite colors on wheel",
        "split_complementary": "Base + two adjacent to complement",
        "triadic": "Three evenly spaced colors",
        "tetradic": "Four colors, two complementary pairs",
        "neutral_with_accent": "Grays/neutrals with one pop color",
    },
)

COLOR_TEMPERATURE = Dimension(
    name="color_temperature",
    description="Overall warmth/coolness",
    values={
        "cool": "Blues, greens, purples dominate",
        "warm": "Reds, oranges, yellows dominate",
        "neutral": "Grays, tans, balanced",
        "mixed": "Intentional warm/cool contrast",
    },
)

COLOR_SATURATION = Dimension(
    name="color_saturation",
    description="Intensity of colors",
    values={
        "desaturated": "Muted, grayish tones",
        "muted": "Slightly reduced saturation",
        "balanced": "Natural saturation",
        "vivid": "High saturation, punchy",
        "hyper_saturated": "Neon, electric intensity",
    },
)

COLOR_CONTRAST = Dimension(
    name="color_contrast",
    description="Value range between lightest and darkest",
    values={
        "low": "Subtle, soft transitions",
        "medium": "Standard readable contrast",
        "high": "Strong black/white presence",
        "extreme": "Maximum contrast, stark",
    },
)

COLOR_PALETTE_MOOD = Dimension(
    name="color_palette_mood",
    description="Emotional/thematic color family",
    values={
        "earth": "Browns, tans, forest greens, terracotta",
        "pastel": "Soft, light, Easter-egg colors",
        "jewel": "Rich sapphire, emerald, ruby, amethyst",
        "metallic": "Gold, silver, bronze, copper",
        "primary": "Pure red, blue, yellow",
        "monochrome": "Black, white, grays only",
        "neon": "Electric, glowing colors",
        "cyber": "Magenta, cyan, purple, tech colors",
        "natural": "Greens, blues, sky, water, earth",
        "candy": "Bright pinks, aquas, playful",
    },
)

COLOR_MODE = Dimension(
    name="color_mode",
    description="Light/dark mode support",
    values={
        "light_only": "Light background only",
        "dark_only": "Dark background only",
        "both": "Includes theme toggle",
    },
)

# Tier 3: Typography

TYPE_HEADING_CLASS = Dimension(
    name="type_heading_class",
    description="Font classification for headings",
    values={
        "geometric_sans": "Constructed, circular (Futura, Poppins, Montserrat)",
        "humanist_sans": "Calligraphic influence (Open Sans, Lato, Source Sans)",
        "neo_grotesque": "Neutral, uniform (Helvetica, Inter, Roboto)",
        "modern_serif": "High contrast, vertical (Didot, Bodoni, Playfair)",
        "transitional_serif": "Medium contrast (Times, Georgia, Libre Baskerville)",
        "old_style_serif": "Low contrast, angled (Garamond, Palatino, EB Garamond)",
        "slab_serif": "Heavy, block serifs (Rockwell, Roboto Slab, Zilla Slab)",
        "monospace": "Fixed-width (JetBrains Mono, Fira Code, IBM Plex Mono)",
        "display": "Decorative, headline-only",
        "handwritten": "Script, casual (Caveat, Patrick Hand)",
    },
)

TYPE_BODY_CLASS = Dimension(
    name="type_body_class",
    description="Font classification for body text",
    values={
        "geometric_sans": "Constructed, circular (Futura, Poppins, Montserrat)",
        "humanist_sans": "Calligraphic influence (Open Sans, Lato, Source Sans)",
        "neo_grotesque": "Neutral, uniform (Helvetica, Inter, Roboto)",
        "modern_serif": "High contrast, vertical (Didot, Bodoni, Playfair)",
        "transitional_serif": "Medium contrast (Times, Georgia, Libre Baskerville)",
        "old_style_serif": "Low contrast, angled (Garamond, Palatino, EB Garamond)",
        "slab_serif": "Heavy, block serifs (Rockwell, Roboto Slab, Zilla Slab)",
        "monospace": "Fixed-width (JetBrains Mono, Fira Code, IBM Plex Mono)",
        "display": "Decorative, headline-only",
        "handwritten": "Script, casual (Caveat, Patrick Hand)",
    },
)

TYPE_SCALE_RATIO = Dimension(
    name="type_scale_ratio",
    description="Mathematical relationship between type sizes",
    values={
        "minor_second": "1.067 - Very tight, subtle",
        "major_second": "1.125 - Tight, compact",
        "minor_third": "1.200 - Standard, comfortable",
        "major_third": "1.250 - Generous",
        "perfect_fourth": "1.333 - Pronounced hierarchy",
        "golden_ratio": "1.618 - Dramatic, classical",
    },
)

TYPE_CASE_TREATMENT = Dimension(
    name="type_case_treatment",
    description="Text transformation approach",
    values={
        "normal": "Standard mixed case",
        "uppercase_headings": "ALL CAPS for headings",
        "small_caps": "Small capitals for emphasis",
        "lowercase_only": "No capitals anywhere",
    },
)

TYPE_LETTER_SPACING = Dimension(
    name="type_letter_spacing",
    description="Tracking adjustment",
    values={
        "tight": "-2% to -1%",
        "normal": "0%",
        "loose": "+2% to +5%",
        "very_loose": "+8% to +12%",
    },
)

TYPE_LINE_HEIGHT = Dimension(
    name="type_line_height",
    description="Leading/line-height",
    values={
        "tight": "1.2",
        "normal": "1.5",
        "loose": "1.75",
        "very_loose": "2.0",
    },
)

# Tier 4: Shape & Space

CORNER_RADIUS = Dimension(
    name="corner_radius",
    description="Border radius philosophy",
    values={
        "sharp": "0px, no rounding",
        "subtle": "2-4px, barely visible",
        "rounded": "8-12px, clearly rounded",
        "very_rounded": "16-24px, soft",
        "pill": "50%/9999px, full round",
        "organic": "Irregular, blob-like",
    },
)

SPACING_BASE = Dimension(
    name="spacing_base",
    description="Base unit for spacing grid",
    values={
        "4px": "4px base unit",
        "8px": "8px base unit (most common)",
        "10px": "10px base unit",
        "12px": "12px base unit",
    },
)

BORDER_STYLE = Dimension(
    name="border_style",
    description="Border treatment",
    values={
        "none": "No borders",
        "hairline": "1px subtle",
        "thin": "2px visible",
        "medium": "3-4px pronounced",
        "thick": "5px+ bold",
        "double": "Double-line borders",
        "dashed": "Dashed lines",
    },
)

SHADOW_STYLE = Dimension(
    name="shadow_style",
    description="Shadow treatment",
    values={
        "none": "No shadows",
        "subtle": "Barely visible, soft",
        "medium": "Standard drop shadow",
        "hard": "Sharp, defined edge",
        "dramatic": "Long, offset shadows",
        "colored": "Tinted shadows",
        "layered": "Multiple stacked shadows",
        "inset": "Inner shadows (neumorphic)",
    },
)

CONTAINER_STYLE = Dimension(
    name="container_style",
    description="How containers/cards are defined",
    values={
        "open": "No visual boundary",
        "outlined": "Border only, transparent",
        "filled": "Solid background",
        "floating": "Shadow-defined",
        "inset": "Recessed appearance",
    },
)

# Tier 5: Layout

GRID_SYSTEM = Dimension(
    name="grid_system",
    description="Layout grid approach",
    values={
        "single_column": "One column, vertical flow",
        "two_column": "Two equal columns",
        "three_column": "Three columns",
        "four_column": "Four columns",
        "twelve_column": "12-column fluid grid",
        "asymmetric": "Intentionally unequal",
        "modular": "Module-based grid",
        "broken": "Overlapping, rule-breaking",
        "freeform": "No grid constraints",
    },
)

ALIGNMENT = Dimension(
    name="alignment",
    description="Text and element alignment",
    values={
        "left": "Left-aligned (LTR default)",
        "center": "Centered",
        "right": "Right-aligned",
        "justified": "Full justification",
        "mixed": "Intentionally varied",
    },
)

HIERARCHY_APPROACH = Dimension(
    name="hierarchy_approach",
    description="Primary method for creating visual hierarchy",
    values={
        "size": "Size differences dominate",
        "color": "Color/saturation differences",
        "position": "Placement creates hierarchy",
        "weight": "Font weight differences",
        "whitespace": "Spacing creates importance",
    },
)

# Tier 6: Texture & Detail

SURFACE_TEXTURE = Dimension(
    name="surface_texture",
    description="Background/surface treatment",
    values={
        "none": "Smooth, flat",
        "noise": "Subtle grain/noise",
        "paper": "Paper-like texture",
        "fabric": "Woven/textile feel",
        "gradient_mesh": "Complex gradient backgrounds",
        "geometric_pattern": "Repeating geometric shapes",
        "organic_pattern": "Natural, irregular patterns",
    },
)

GRADIENT_USAGE = Dimension(
    name="gradient_usage",
    description="Gradient application",
    values={
        "none": "No gradients",
        "subtle_background": "Very soft bg gradients",
        "accent": "Gradients on CTAs/accents",
        "duotone": "Two-color image treatment",
        "mesh": "Complex multi-stop gradients",
        "glassmorphic": "Blur + transparency",
    },
)

ICON_STYLE = Dimension(
    name="icon_style",
    description="Icon treatment",
    values={
        "outlined": "Stroke-only icons",
        "filled": "Solid filled icons",
        "duotone": "Two-tone icons",
        "hand_drawn": "Sketchy, imperfect",
        "isometric": "3D isometric",
        "emoji": "Emoji as icons",
    },
)

# Tier 7: Context

INDUSTRY = Dimension(
    name="industry",
    description="Target industry vertical",
    values={
        "finance": "Banking, fintech, investing",
        "healthcare": "Medical, wellness, health tech",
        "education": "EdTech, learning, academic",
        "ecommerce": "Online retail, marketplaces",
        "saas": "B2B software, productivity",
        "gaming": "Games, entertainment",
        "media": "News, video, content",
        "food": "Restaurants, delivery, recipes",
        "travel": "Booking, hospitality",
        "real_estate": "Property, listings",
        "fashion": "Apparel, luxury goods",
        "fitness": "Gyms, workout apps",
        "nonprofit": "Charities, causes",
        "government": "Public sector, civic",
        "creative": "Agencies, portfolios",
        "developer": "Dev tools, APIs, docs",
    },
)

TARGET_AUDIENCE = Dimension(
    name="target_audience",
    description="Primary user demographic",
    values={
        "enterprise": "Large business users",
        "smb": "Small/medium business",
        "consumer_mass": "General public",
        "consumer_premium": "Luxury/premium consumers",
        "developer": "Technical users",
        "children": "Kids, family",
        "seniors": "Older adults",
        "gen_z": "Younger generation",
    },
)

EMOTIONAL_TONE = Dimension(
    name="emotional_tone",
    description="Intended emotional response",
    values={
        "trustworthy": "Reliable, secure",
        "playful": "Fun, lighthearted",
        "serious": "Professional, formal",
        "luxurious": "Premium, exclusive",
        "friendly": "Approachable, warm",
        "edgy": "Bold, rebellious",
        "calm": "Peaceful, serene",
        "energetic": "Dynamic, exciting",
        "mysterious": "Intriguing, dark",
        "nostalgic": "Retro, sentimental",
    },
)

CULTURAL_INFLUENCE = Dimension(
    name="cultural_influence",
    description="Geographic/cultural design tradition",
    values={
        "scandinavian": "Nordic minimal, hygge",
        "japanese": "Wabi-sabi, zen, minimal",
        "mediterranean": "Warm, terracotta, tiles",
        "american_corporate": "Professional, blue-chip",
        "british_traditional": "Heritage, refined",
        "german_industrial": "Engineered, precise",
        "french_elegant": "Chic, sophisticated",
        "latin_vibrant": "Colorful, energetic",
        "african_bold": "Geometric, earth tones",
        "middle_eastern": "Ornate, geometric patterns",
    },
)

FUNCTIONAL_DIRECTION = Dimension(
    name="functional_direction",
    description="Primary functional purpose - THIS DRIVES THE PAGE STRUCTURE",
    values={
        # === STANDARD WEB TYPES ===
        "dashboard": "Analytics panels, metrics grid, sidebar nav, data cards, charts",
        "admin_panel": "Table views, CRUD forms, action buttons, breadcrumbs, filters",
        "landing_page": "Hero section, CTAs, testimonials, pricing tables, conversion focus",
        "documentation": "Sidebar TOC, code blocks, search, breadcrumbs, prev/next links",
        "e_commerce": "Product grid, filters, cart icon, product cards with prices, ratings",
        "portfolio": "Project cards, case study sections, about/contact, work samples",
        "blog": "Article layout, reading typography, author byline, related posts",
        "social_feed": "Post cards with avatar/timestamp, like/comment buttons, feed layout",
        "forum": "Thread list, post/reply structure, user badges, vote counts",
        "wiki": "Article with TOC, edit button, revision history, internal links",
        "knowledge_base": "Search-prominent, category cards, FAQ accordion, help articles",
        "pricing_page": "Tier comparison cards, feature checkmarks, CTA buttons, toggle billing",
        "changelog": "Version entries, date headers, tag badges, expandable details",
        "status_page": "Service list with indicators, uptime graphs, incident history",

        # === EDUCATION & LEARNING ===
        "online_course": "Video player area, lesson sidebar, progress bar, notes section",
        "quiz_interface": "Question card, answer options, progress indicator, timer, score",
        "flashcard_app": "Card flip interaction, deck progress, study stats, streak",
        "language_learning": "Lesson modules, XP/streak display, practice exercises, mascot",
        "lms_dashboard": "Course cards, assignment list, grades, calendar, announcements",
        "textbook_reader": "Page content, chapter nav, highlights, annotations, bookmarks",
        "tutorial_walkthrough": "Step-by-step panels, code snippets, try-it areas, checkpoints",
        "grade_book": "Student roster, assignment columns, score cells, averages, filters",
        "exam_interface": "Question navigation, answer area, flag for review, submit, timer",
        "certification_page": "Certificate display, verification code, share buttons, details",

        # === PRODUCTIVITY & WORK ===
        "project_management": "Task columns/lists, assignees, due dates, progress bars",
        "kanban_board": "Draggable columns, task cards, labels, swimlanes, WIP limits",
        "note_taking": "Editor area, notebook sidebar, tags, search, formatting toolbar",
        "spreadsheet": "Cell grid, column/row headers, formula bar, sheet tabs, toolbar",
        "time_tracker": "Timer display, task list, weekly summary, project breakdown",
        "invoice": "Company header, line items table, totals, payment terms, due date",
        "crm": "Contact list, deal pipeline, activity timeline, company cards",
        "help_desk": "Ticket list, status badges, priority tags, assignee, response area",
        "file_manager": "Folder tree, file grid/list, breadcrumbs, upload, preview pane",
        "presentation": "Slide canvas, thumbnail sidebar, presenter notes, controls",

        # === COMMUNICATION ===
        "messaging_app": "Conversation list, chat bubbles (left/right), input field, timestamps",
        "email_client": "Inbox list, preview pane, folder sidebar, compose button, search",
        "video_call": "Video grid, participant list, controls bar, chat sidebar, screen share",
        "team_chat": "Channel sidebar, message thread, reactions, mentions, file attachments",
        "comment_section": "Threaded comments, reply forms, vote buttons, user avatars",
        "live_chat_widget": "Chat bubble, message history, typing indicator, agent info",
        "announcement_board": "Post cards, pinned items, categories, timestamps, admin badges",

        # === MEDIA & ENTERTAINMENT ===
        "music_player": "Now playing with album art, progress bar, controls, playlist queue",
        "video_player": "Video area, playback controls, quality selector, captions, related",
        "podcast_player": "Episode list, player controls, show notes, subscribe button",
        "photo_gallery": "Image grid, lightbox, albums, upload, filters",
        "news_reader": "Article list, reading pane, categories, save/share, font controls",
        "streaming_service": "Content rows, thumbnails, play buttons, categories, continue watching",
        "movie_database": "Movie cards, ratings, cast list, reviews, watchlist button",
        "comic_reader": "Page view, panel zoom, chapter navigation, reading progress",
        "audio_visualizer": "Waveform/spectrum display, track info, playback, color themes",
        "live_stream": "Video player, chat sidebar, viewer count, streamer info, donations",

        # === FINANCE & BUSINESS ===
        "banking_dashboard": "Account summary, transaction list, quick actions, spending chart",
        "investment_portfolio": "Holdings table, performance chart, gain/loss, allocation pie",
        "expense_tracker": "Transaction list, category breakdown, budget progress, add expense",
        "crypto_tracker": "Coin list, price charts, portfolio value, market cap, watchlist",
        "pos_terminal": "Product grid, cart, payment buttons, receipt preview, numpad",
        "stock_ticker": "Price display, mini charts, volume, ticker tape, alerts",
        "budget_planner": "Category budgets, spending bars, remaining amounts, monthly view",
        "subscription_manager": "Service list, costs, renewal dates, total monthly, cancel",

        # === HEALTH & WELLNESS ===
        "fitness_tracker": "Progress rings, stat cards, activity feed, workout log, goals",
        "meditation_app": "Session timer, breathing guide, streak display, ambient backgrounds",
        "habit_tracker": "Habit grid, streak counts, daily checkboxes, statistics, reminders",
        "sleep_tracker": "Sleep score, duration graph, sleep stages, bedtime, trends",
        "nutrition_counter": "Food log, calorie/macro breakdown, meal sections, barcode scan",
        "appointment_booking": "Calendar picker, time slots, provider selection, confirmation",
        "symptom_checker": "Body map, symptom selection, severity scale, recommendations",
        "medical_records": "Patient info, visit history, medications, test results, documents",
        "mental_health_journal": "Daily entry, mood tracker, prompts, insights, privacy lock",

        # === TRAVEL & LOCATION ===
        "flight_booking": "Search form, flight results, filters, seat map, booking flow",
        "hotel_search": "Property cards, map view, filters, amenities, reviews, book button",
        "trip_planner": "Itinerary timeline, day cards, map, budget tracker, packing list",
        "maps_interface": "Map canvas, search bar, directions panel, layers, pins",
        "transit_app": "Route planner, departure times, line maps, service alerts, favorites",
        "restaurant_finder": "Listing cards, map, filters, cuisine types, ratings, distance",
        "ride_sharing": "Map with car locations, pickup/dropoff, fare estimate, driver info",
        "travel_guide": "Destination hero, attractions, tips, photos, local info",

        # === SOCIAL & COMMUNITY ===
        "dating_profile": "Photos carousel, bio, interests tags, match percentage, message",
        "user_profile": "Avatar, bio, stats, activity feed, followers, settings",
        "community_directory": "Member cards, search, filters, join button, activity stats",
        "review_site": "Star ratings, review cards, photos, helpful votes, owner response",
        "event_discovery": "Event cards, date filters, map, categories, RSVP, sharing",
        "group_page": "Cover photo, member list, discussion feed, events, files",

        # === CREATIVE TOOLS ===
        "code_editor": "Editor pane, file tree, tabs, terminal, syntax highlighting, minimap",
        "design_tool": "Canvas area, toolbar, layers panel, properties sidebar, zoom",
        "color_picker": "Color wheel, sliders, swatches, palette generator, export formats",
        "font_browser": "Specimen cards, preview text, filters, categories, download",
        "component_library": "Component cards, code snippets, props table, live preview",
        "icon_library": "Icon grid, search, categories, size/color options, copy code",
        "markdown_editor": "Split pane editor/preview, toolbar, file browser, export",
        "animation_timeline": "Timeline tracks, keyframes, playhead, properties, preview",

        # === REAL ESTATE ===
        "property_listing": "Photo gallery, price, details grid, map, agent contact, similar",
        "floor_plan": "Interactive plan, room labels, measurements, furniture toggle",
        "mortgage_calculator": "Input sliders, monthly payment, amortization chart, comparison",

        # === FOOD & DINING ===
        "restaurant_menu": "Categories, dish name + description + price, specials, dietary icons",
        "recipe_card": "Ingredients list, numbered steps, prep/cook time, servings, ratings",
        "food_delivery": "Restaurant list, menu, cart, checkout, order tracking, address",
        "meal_planner": "Weekly calendar, recipe cards, shopping list, nutrition totals",
        "wine_list": "Regions, varietals, tasting notes, price, pairings, sommelier picks",

        # === SPORTS & GAMING ===
        "sports_scores": "Live scores, team matchups, league standings, schedule, stats",
        "fantasy_sports": "Team roster, points, matchup, waiver wire, league standings",
        "tournament_bracket": "Bracket tree, match cards, seeds, winners path, champion",
        "game_leaderboard": "Rank list, player names, scores, trophies, filters, search",
        "character_sheet": "Stats block, inventory grid, abilities, portrait, level/XP",
        "game_inventory": "Item grid, categories, equip slots, stats comparison, sort",
        "achievement_showcase": "Badge grid, unlock progress, rarity, descriptions, dates",

        # === NEWS & PUBLISHING ===
        "newspaper": "Multi-column layout, masthead, bylines, pull quotes, sections",
        "magazine_spread": "Large imagery, editorial layout, pull quotes, captions",
        "newsletter": "Header branding, article sections, CTA buttons, footer links",
        "press_release": "Company header, headline, dateline, body text, contact info",
        "podcast_directory": "Show cards, categories, charts, episode lists, subscribe",

        # === EVENTS & BOOKING ===
        "event_poster": "Giant headline, date/time/venue, artistic layout, RSVP",
        "ticket_booking": "Event details, seat map, ticket types, quantity, checkout",
        "conference_schedule": "Day tabs, time slots, session cards, tracks, speakers",
        "wedding_invitation": "Couple names, date/venue, RSVP form, registry, story",
        "countdown_page": "Large countdown timer, event name, email signup, teaser",

        # === UTILITY PAGES ===
        "calculator": "Display, number pad, operation buttons, history, modes",
        "survey_form": "Question progression, answer types, progress bar, submit",
        "url_shortener": "Input field, shorten button, result with copy, click stats",
        "password_generator": "Output field, length slider, options checkboxes, copy button",
        "unit_converter": "Input/output fields, unit dropdowns, swap button, conversions",
        "qr_generator": "Input field, QR display, download button, customization options",

        # === RETRO & NOVELTY ===
        "terminal_ui": "Monospace everything, command prompts, green/amber on black, ASCII",
        "retro_game_hud": "Score display, health bar, lives, pixel aesthetic, power-ups",
        "sci_fi_console": "Holographic panels, tech readouts, glowing borders, hexagonal",
        "windows_95": "Title bars, start menu, desktop icons, gray beveled buttons",
        "vaporwave": "Pink/cyan gradients, grid backgrounds, glitch effects, statues",
        "cyberpunk": "Neon on dark, glitch effects, tech overlays, angular shapes",
        "pixel_art_ui": "Pixelated elements, 8-bit aesthetic, chiptune vibes, retro palette",
        "90s_website": "Under construction GIFs, hit counter, guestbook, tiled backgrounds",
        "myspace_profile": "Top 8 friends, profile song, sparkly GIFs, custom CSS chaos",
        "vintage_catalog": "Product illustrations, item numbers, prices, order form, retro",

        # === PROFESSIONAL & INDUSTRY ===
        "government_form": "Form fields, section numbers, official seals, instructions",
        "legal_document": "Numbered paragraphs, signatures, seals, formal typography",
        "scientific_paper": "Abstract, sections, citations, figures, references list",
        "medical_chart": "Patient header, vitals, notes sections, orders, signatures",
        "lab_results": "Test names, values, reference ranges, flags, interpretation",
        "shipping_tracker": "Package status, timeline, map, delivery estimate, details",
        "inventory_system": "Stock levels, SKUs, locations, reorder alerts, movements",
        "security_dashboard": "Threat alerts, logs, status indicators, maps, severity",
        "iot_dashboard": "Device cards, sensor readings, status lights, graphs, controls",

        # === PERSONAL & MISC ===
        "resume_cv": "Contact header, experience timeline, skills, education, achievements",
        "business_card": "Name, title, contact info, logo, QR code, minimal layout",
        "personal_homepage": "Hero intro, about, projects, contact, social links",
        "linktree_clone": "Profile pic, bio, stacked link buttons, social icons",
        "memorial_page": "Photo, dates, biography, guestbook, photo gallery, donations",
        "coming_soon": "Logo, launch countdown, email signup, social links, teaser",
        "404_page": "Error message, illustration, search, navigation suggestions",
        "maintenance_page": "Status message, estimated time, contact info, updates",
        "login_page": "Form fields, submit button, forgot password, social login, signup",
        "settings_panel": "Toggle groups, preference sections, save buttons, categories",
        "onboarding_flow": "Step indicator, single focus content, progress, next/back",
        "cookie_consent": "Banner, accept/reject buttons, preferences, privacy link",
        "age_verification": "Date inputs or yes/no, legal text, submit, logo",

        # === DATA & ANALYTICS ===
        "infographic": "Data visualizations, icon stats, flow diagrams, comparisons",
        "report_builder": "Chart widgets, drag-drop, filters, date range, export options",
        "data_table": "Sortable columns, pagination, filters, row selection, bulk actions",
        "chart_dashboard": "Multiple chart types, filters, date range, drill-down, export",
        "analytics_overview": "KPI cards, trend lines, comparison periods, top lists",
    },
)

# Tier 8: Layout Structure

PAGE_STRUCTURE = Dimension(
    name="page_structure",
    description="Overall page layout architecture",
    values={
        "hero_sections": "Traditional hero → stacked sections flow",
        "split_screen": "Two-column layout throughout",
        "card_mosaic": "Bento/Pinterest-style mixed grid",
        "editorial_scroll": "Magazine long-form vertical",
        "app_shell": "Fixed nav + scrolling content area",
        "sidebar_main": "Persistent sidebar with main content",
        "single_canvas": "One continuous surface, no sections",
        "modular_blocks": "Distinct stackable content blocks",
        "asymmetric_panels": "Deliberately unbalanced layout",
        "fullscreen_slides": "Viewport-height sections",
    },
)

NAVIGATION_PATTERN = Dimension(
    name="navigation_pattern",
    description="Primary navigation style",
    values={
        "top_fixed": "Standard sticky header nav",
        "top_transparent": "Transparent header over hero",
        "side_persistent": "Always-visible sidebar nav",
        "side_collapsible": "Hamburger → slide out drawer",
        "bottom_bar": "Mobile-style fixed bottom nav",
        "floating_pill": "Floating nav element (centered or corner)",
        "hidden_scroll": "Appears on scroll up, hides on scroll down",
        "tabs": "Tab-based navigation",
        "breadcrumb_only": "No main nav, just breadcrumbs",
        "none": "No navigation (single page, artistic)",
    },
)

HERO_STYLE = Dimension(
    name="hero_style",
    description="Hero/header section treatment",
    values={
        "full_viewport": "Takes entire viewport height",
        "half_viewport": "50vh hero section",
        "contained": "Padded container, not edge-to-edge",
        "split_image": "Image on one side, content on other",
        "centered_minimal": "Just text, lots of breathing room",
        "video_background": "Placeholder for video bg",
        "image_background": "Full-bleed background image area",
        "gradient_background": "Bold gradient background",
        "illustrated": "Custom illustration placeholder",
        "none": "No hero, dive straight into content",
    },
)

CONTENT_FLOW = Dimension(
    name="content_flow",
    description="How content is organized and flows",
    values={
        "vertical_scroll": "Standard vertical scrolling",
        "card_grid": "Uniform card grid",
        "masonry": "Pinterest-style varied heights",
        "timeline": "Sequential/chronological flow",
        "accordion": "Expandable sections",
        "tabs_panels": "Tabbed content panels",
        "carousel": "Horizontal sliding content",
        "list_detail": "List view with detail panel",
        "kanban": "Column-based board layout",
        "tree": "Hierarchical tree structure",
    },
)


# All dimensions in order
ALL_DIMENSIONS: list[Dimension] = [
    # Tier 1: Core Visual Style
    UI_PARADIGM,
    DESIGN_ERA,
    DENSITY,
    # Tier 2: Color System
    COLOR_THEORY,
    COLOR_TEMPERATURE,
    COLOR_SATURATION,
    COLOR_CONTRAST,
    COLOR_PALETTE_MOOD,
    COLOR_MODE,
    # Tier 3: Typography
    TYPE_HEADING_CLASS,
    TYPE_BODY_CLASS,
    TYPE_SCALE_RATIO,
    TYPE_CASE_TREATMENT,
    TYPE_LETTER_SPACING,
    TYPE_LINE_HEIGHT,
    # Tier 4: Shape & Space
    CORNER_RADIUS,
    SPACING_BASE,
    BORDER_STYLE,
    SHADOW_STYLE,
    CONTAINER_STYLE,
    # Tier 5: Layout
    GRID_SYSTEM,
    ALIGNMENT,
    HIERARCHY_APPROACH,
    # Tier 6: Texture & Detail
    SURFACE_TEXTURE,
    GRADIENT_USAGE,
    ICON_STYLE,
    # Tier 7: Context
    INDUSTRY,
    TARGET_AUDIENCE,
    EMOTIONAL_TONE,
    CULTURAL_INFLUENCE,
    FUNCTIONAL_DIRECTION,
    # Tier 8: Layout Structure
    PAGE_STRUCTURE,
    NAVIGATION_PATTERN,
    HERO_STYLE,
    CONTENT_FLOW,
]


def get_dimension_names() -> list[str]:
    """Return all dimension names."""
    return [d.name for d in ALL_DIMENSIONS]


def get_dimension_values(dimension_name: str) -> list[str]:
    """Return all valid values for a dimension."""
    for d in ALL_DIMENSIONS:
        if d.name == dimension_name:
            return list(d.values.keys())
    raise ValueError(f"Unknown dimension: {dimension_name}")
