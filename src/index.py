# ABOUTME: Builds the gallery index.html page.
# ABOUTME: Creates a browsable grid of all designs with previews and navigation.

import json
import os
from datetime import datetime
from pathlib import Path

from rich.console import Console

console = Console()


def format_size(size_bytes: int) -> str:
    """Format bytes as human-readable size."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def get_run_stats(output_path: Path) -> dict:
    """Get stats about the run (file sizes, count, etc.)."""
    designs_dir = output_path / "designs"
    total_size = 0
    file_count = 0

    if designs_dir.exists():
        for f in designs_dir.glob("design-*.html"):
            total_size += f.stat().st_size
            file_count += 1

    return {
        "file_count": file_count,
        "total_size": total_size,
        "total_size_formatted": format_size(total_size),
        "avg_size": total_size // file_count if file_count > 0 else 0,
        "avg_size_formatted": format_size(total_size // file_count) if file_count > 0 else "0 B",
    }


def get_color_preview_style(dimensions: dict[str, str]) -> str:
    """Generate a CSS gradient preview based on color dimensions."""
    mood = dimensions.get("color_palette_mood", "natural")
    temp = dimensions.get("color_temperature", "neutral")
    mode = dimensions.get("color_mode", "light_only")

    # Base colors by mood
    mood_colors = {
        "earth": ["#8B4513", "#D2691E", "#228B22"],
        "pastel": ["#FFB6C1", "#E6E6FA", "#98FB98"],
        "jewel": ["#50C878", "#E0115F", "#0F52BA"],
        "metallic": ["#FFD700", "#C0C0C0", "#CD7F32"],
        "primary": ["#FF0000", "#0000FF", "#FFFF00"],
        "monochrome": ["#2D2D2D", "#6B6B6B", "#A9A9A9"],
        "neon": ["#FF00FF", "#00FFFF", "#39FF14"],
        "cyber": ["#FF00FF", "#00BFFF", "#8A2BE2"],
        "natural": ["#228B22", "#87CEEB", "#DEB887"],
        "candy": ["#FF69B4", "#00CED1", "#FFD700"],
    }

    colors = mood_colors.get(mood, ["#6366f1", "#8b5cf6", "#a855f7"])

    if mode == "dark_only":
        return f"background: linear-gradient(135deg, #1a1a2e 0%, {colors[0]}44 50%, {colors[1]}44 100%);"
    else:
        return f"background: linear-gradient(135deg, {colors[0]} 0%, {colors[1]} 50%, {colors[2]} 100%);"


def build_index(output_path: Path, manifest: dict, run_name: str = None, model: str = "unknown") -> None:
    """Build the index.html gallery page with stats and collapsible sections."""
    designs = manifest["designs"]
    total = manifest["total_designs"]
    generated_at = manifest.get("generated_at", "Unknown")

    # Parse timestamp for display
    try:
        dt = datetime.fromisoformat(generated_at)
        formatted_date = dt.strftime("%B %d, %Y at %I:%M %p")
    except Exception:
        formatted_date = generated_at

    # Get run stats
    stats = get_run_stats(output_path)

    # Check which designs exist
    designs_dir = output_path / "designs"
    existing_ids = set()
    if designs_dir.exists():
        for f in designs_dir.glob("design-*.html"):
            try:
                design_id = int(f.stem.replace("design-", ""))
                existing_ids.add(design_id)
            except ValueError:
                pass

    # Try to load the design guide prompt
    project_root = output_path.parent.parent
    prompt_content = ""
    for guide_name in ["DESIGN_GUIDE_LOOSE.md", "DESIGN_GUIDE.md"]:
        guide_path = project_root / guide_name
        if guide_path.exists():
            prompt_content = guide_path.read_text()
            break

    # Escape HTML in prompt
    import html
    prompt_escaped = html.escape(prompt_content) if prompt_content else "Prompt not available"

    # Build design cards HTML
    cards_html = []
    for design in designs:
        exists = design["id"] in existing_ids
        color_style = get_color_preview_style(design["dimensions"])

        paradigm = design["dimensions"].get("ui_paradigm", "").replace("_", " ")
        era = design["dimensions"].get("design_era", "").replace("_", " ")
        tone = design["dimensions"].get("emotional_tone", "").replace("_", " ")

        card = f"""
        <a href="{'design-' + str(design['id']) + '.html' if exists else '#'}"
           class="card {'disabled' if not exists else ''}"
           {'aria-disabled="true"' if not exists else ''}>
            <div class="card-preview" style="{color_style}">
                <span class="card-number">#{design['id']}</span>
            </div>
            <div class="card-content">
                <h3 class="card-title">{design['name']}</h3>
                <p class="card-tagline">{design['tagline']}</p>
                <div class="card-tags">
                    <span class="tag">{paradigm}</span>
                    <span class="tag">{era}</span>
                    <span class="tag">{tone}</span>
                </div>
            </div>
        </a>
        """
        cards_html.append(card)

    # Get run name from path if not provided
    if not run_name:
        run_name = output_path.name

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{run_name} - 1000 Design Vibes</title>
    <style>
        :root {{
            --color-bg: #0a0a0a;
            --color-surface: #141414;
            --color-border: #2a2a2a;
            --color-text: #e5e5e5;
            --color-text-muted: #888;
            --color-accent: #6366f1;
            --radius: 12px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--color-bg);
            color: var(--color-text);
            line-height: 1.6;
            min-height: 100vh;
        }}

        header {{
            padding: 2rem;
            border-bottom: 1px solid var(--color-border);
            max-width: 1600px;
            margin: 0 auto;
        }}

        .breadcrumb {{
            font-size: 0.875rem;
            color: var(--color-text-muted);
            margin-bottom: 1rem;
        }}

        .breadcrumb a {{
            color: var(--color-accent);
            text-decoration: none;
        }}

        .breadcrumb a:hover {{
            text-decoration: underline;
        }}

        h1 {{
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .subtitle {{
            color: var(--color-text-muted);
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }}

        .stats-grid {{
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            margin-bottom: 1.5rem;
        }}

        .stat {{
            text-align: left;
        }}

        .stat-value {{
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--color-accent);
        }}

        .stat-label {{
            font-size: 0.75rem;
            color: var(--color-text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        details {{
            margin-top: 1rem;
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius);
            overflow: hidden;
        }}

        summary {{
            padding: 1rem 1.25rem;
            cursor: pointer;
            font-weight: 500;
            user-select: none;
        }}

        summary:hover {{
            background: rgba(255,255,255,0.02);
        }}

        .details-content {{
            padding: 1rem 1.25rem;
            border-top: 1px solid var(--color-border);
            max-height: 400px;
            overflow-y: auto;
        }}

        .details-content pre {{
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            font-size: 0.8rem;
            line-height: 1.5;
            color: var(--color-text-muted);
        }}

        .gallery {{
            display: grid;
            grid-template-columns: repeat(1, 1fr);
            gap: 1.5rem;
            padding: 2rem;
            max-width: 1600px;
            margin: 0 auto;
        }}

        @media (min-width: 640px) {{
            .gallery {{ grid-template-columns: repeat(2, 1fr); }}
        }}

        @media (min-width: 1024px) {{
            .gallery {{ grid-template-columns: repeat(3, 1fr); }}
        }}

        @media (min-width: 1280px) {{
            .gallery {{ grid-template-columns: repeat(4, 1fr); }}
        }}

        .card {{
            display: block;
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            border-radius: var(--radius);
            overflow: hidden;
            text-decoration: none;
            color: inherit;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .card:hover:not(.disabled) {{
            transform: translateY(-4px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
        }}

        .card:focus {{
            outline: 2px solid var(--color-accent);
            outline-offset: 2px;
        }}

        .card.disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}

        .card-preview {{
            height: 120px;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .card-number {{
            position: absolute;
            top: 0.75rem;
            left: 0.75rem;
            background: rgba(0, 0, 0, 0.5);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 600;
        }}

        .card-content {{
            padding: 1rem;
        }}

        .card-title {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }}

        .card-tagline {{
            font-size: 0.85rem;
            color: var(--color-text-muted);
            margin-bottom: 0.75rem;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .card-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .tag {{
            font-size: 0.7rem;
            padding: 0.2rem 0.5rem;
            background: var(--color-border);
            border-radius: 4px;
            text-transform: capitalize;
        }}

        footer {{
            text-align: center;
            padding: 2rem;
            color: var(--color-text-muted);
            font-size: 0.9rem;
            border-top: 1px solid var(--color-border);
        }}

        footer a {{
            color: var(--color-accent);
        }}

        .keyboard-hint {{
            position: fixed;
            bottom: 1rem;
            left: 50%;
            transform: translateX(-50%);
            background: var(--color-surface);
            border: 1px solid var(--color-border);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-size: 0.8rem;
            color: var(--color-text-muted);
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
        }}

        .keyboard-hint.visible {{
            opacity: 1;
        }}
    </style>
</head>
<body>
    <header>
        <nav class="breadcrumb">
            <a href="../../../index.html">All Runs</a> / {run_name}
        </nav>
        <h1>{run_name}</h1>
        <p class="subtitle">Generated {formatted_date}</p>

        <div class="stats-grid">
            <div class="stat">
                <div class="stat-value">{len(existing_ids)}</div>
                <div class="stat-label">Designs</div>
            </div>
            <div class="stat">
                <div class="stat-value">{stats['total_size_formatted']}</div>
                <div class="stat-label">Total Size</div>
            </div>
            <div class="stat">
                <div class="stat-value">{stats['avg_size_formatted']}</div>
                <div class="stat-label">Avg Size</div>
            </div>
            <div class="stat">
                <div class="stat-value" style="text-transform: capitalize;">{model}</div>
                <div class="stat-label">Model</div>
            </div>
        </div>

        <details>
            <summary>View Prompt Used</summary>
            <div class="details-content">
                <pre>{prompt_escaped}</pre>
            </div>
        </details>
    </header>

    <main class="gallery">
        {''.join(cards_html)}
    </main>

    <footer>
        <p>Use arrow keys to navigate, Enter to open</p>
        <p>Generated with <a href="https://github.com/anthropics/claude-code">Claude Code</a></p>
    </footer>

    <div class="keyboard-hint" id="hint">
        Use arrow keys to navigate • Enter to open
    </div>

    <script>
        // Keyboard navigation
        const cards = Array.from(document.querySelectorAll('.card:not(.disabled)'));
        let currentIndex = -1;

        function focusCard(index) {{
            if (index >= 0 && index < cards.length) {{
                currentIndex = index;
                cards[index].focus();
            }}
        }}

        document.addEventListener('keydown', (e) => {{
            const cols = window.innerWidth >= 1280 ? 4 : window.innerWidth >= 1024 ? 3 : window.innerWidth >= 640 ? 2 : 1;

            if (e.key === 'ArrowRight') {{
                e.preventDefault();
                focusCard(currentIndex + 1);
            }} else if (e.key === 'ArrowLeft') {{
                e.preventDefault();
                focusCard(currentIndex - 1);
            }} else if (e.key === 'ArrowDown') {{
                e.preventDefault();
                focusCard(currentIndex + cols);
            }} else if (e.key === 'ArrowUp') {{
                e.preventDefault();
                focusCard(currentIndex - cols);
            }} else if (e.key === 'Enter' && currentIndex >= 0) {{
                cards[currentIndex].click();
            }}
        }});

        cards.forEach((card, i) => {{
            card.addEventListener('focus', () => currentIndex = i);
        }});

        // Show hint briefly
        if (!localStorage.getItem('gallery-hint-shown')) {{
            const hint = document.getElementById('hint');
            setTimeout(() => hint.classList.add('visible'), 1000);
            setTimeout(() => {{
                hint.classList.remove('visible');
                localStorage.setItem('gallery-hint-shown', '1');
            }}, 5000);
        }}
    </script>
</body>
</html>
"""

    # Write to designs folder so relative links work
    designs_dir = output_path / "designs"
    designs_dir.mkdir(exist_ok=True)
    index_path = designs_dir / "index.html"
    index_path.write_text(html)
    console.print(f"[green]Built index at {index_path}[/green]")


def build_all_indexes(outputs_path: Path) -> None:
    """Build index pages for all runs in outputs directory."""
    # Known model info (could be stored in manifest later)
    run_models = {
        "2026-01-07-batch-100": "haiku",
        "2026-01-07-nav-test": "haiku",
        "2026-01-06-ab-test-loose": "haiku + sonnet",
        "2026-01-06-full-test": "sonnet",
        "2026-01-06-test-batch": "sonnet",
    }

    for run_dir in sorted(outputs_path.iterdir(), reverse=True):
        if not run_dir.is_dir():
            continue
        manifest_path = run_dir / "manifest.json"
        if not manifest_path.exists():
            continue

        console.print(f"[blue]Building index for {run_dir.name}...[/blue]")
        manifest = json.loads(manifest_path.read_text())
        model = run_models.get(run_dir.name, "unknown")
        build_index(run_dir, manifest, run_name=run_dir.name, model=model)
