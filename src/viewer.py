# ABOUTME: Generates unified design viewer for browsing all designs.
# ABOUTME: Creates all-designs.json and viewer.html for iframe-based slideshow.

import json
from pathlib import Path
from datetime import datetime

from rich.console import Console

console = Console()


def collect_all_designs(outputs_path: Path) -> list[dict]:
    """Collect all designs from all batches into a single list."""
    all_designs = []

    for run_dir in sorted(outputs_path.iterdir()):
        if not run_dir.is_dir():
            continue

        manifest_path = run_dir / "manifest.json"
        designs_dir = run_dir / "designs"

        if not manifest_path.exists() or not designs_dir.exists():
            continue

        manifest = json.loads(manifest_path.read_text())
        batch_name = run_dir.name

        for design in manifest.get("designs", []):
            design_file = designs_dir / f"design-{design['id']}.html"
            if design_file.exists():
                all_designs.append({
                    "batch": batch_name,
                    "id": design["id"],
                    "name": design["name"],
                    "tagline": design["tagline"],
                    "path": f"outputs/{batch_name}/designs/design-{design['id']}.html",
                    "dimensions": design.get("dimensions", {})
                })

    return all_designs


def generate_viewer_html(designs: list[dict]) -> str:
    """Generate the viewer HTML page."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>1000 Design Vibes</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        :root {{
            --bg: #0a0a0a;
            --surface: #141414;
            --border: #2a2a2a;
            --text: #e5e5e5;
            --text-muted: #888;
            --accent: #6366f1;
        }}

        body {{
            font-family: 'Space Grotesk', -apple-system, sans-serif;
            background: var(--bg);
            color: var(--text);
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 1.5rem;
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            flex-shrink: 0;
        }}

        .header-left {{
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }}

        .logo {{
            font-weight: 600;
            font-size: 1rem;
            color: var(--text);
            text-decoration: none;
        }}

        .about-link {{
            font-size: 0.875rem;
            color: var(--text-muted);
            text-decoration: none;
            transition: color 0.15s;
        }}

        .about-link:hover {{
            color: var(--accent);
        }}

        .nav-controls {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .nav-btn {{
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            padding: 0.5rem 1rem;
            border-radius: 6px;
            cursor: pointer;
            font-family: inherit;
            font-size: 0.875rem;
            transition: border-color 0.15s, background 0.15s;
        }}

        .nav-btn:hover {{
            border-color: var(--accent);
            background: var(--surface);
        }}

        .nav-btn:disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}

        .counter {{
            font-size: 0.875rem;
            color: var(--text-muted);
            min-width: 100px;
            text-align: center;
        }}

        .design-info {{
            text-align: right;
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .design-text {{
            text-align: right;
        }}

        .design-name {{
            font-weight: 500;
            font-size: 0.9rem;
        }}

        .design-meta {{
            font-size: 0.75rem;
            color: var(--text-muted);
        }}

        .prompt-toggle {{
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 0.4rem 0.75rem;
            border-radius: 6px;
            cursor: pointer;
            font-family: inherit;
            font-size: 0.8rem;
            transition: all 0.15s;
            white-space: nowrap;
        }}

        .prompt-toggle:hover {{
            border-color: var(--accent);
            color: var(--text);
        }}

        .prompt-toggle.active {{
            background: var(--accent);
            border-color: var(--accent);
            color: white;
        }}

        .prompt-panel {{
            background: var(--surface);
            border-bottom: 1px solid var(--border);
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease-out;
        }}

        .prompt-panel.open {{
            max-height: 400px;
            overflow-y: auto;
        }}

        .prompt-content {{
            padding: 1rem 1.5rem;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 1rem;
        }}

        .dim-group {{
            background: var(--bg);
            border-radius: 6px;
            padding: 0.75rem;
        }}

        .dim-label {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 0.25rem;
        }}

        .dim-value {{
            font-size: 0.875rem;
            color: var(--text);
        }}

        .viewer-container {{
            flex: 1;
            position: relative;
            overflow: hidden;
        }}

        iframe {{
            width: 100%;
            height: 100%;
            border: none;
            background: white;
        }}

        .loading {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: var(--text-muted);
        }}

        .keyboard-hint {{
            position: fixed;
            bottom: 1rem;
            left: 50%;
            transform: translateX(-50%);
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-size: 0.8rem;
            color: var(--text-muted);
            opacity: 0;
            transition: opacity 0.3s;
            pointer-events: none;
            z-index: 100;
        }}

        .keyboard-hint.visible {{
            opacity: 1;
        }}

        @media (max-width: 768px) {{
            header {{
                flex-direction: column;
                gap: 0.75rem;
                padding: 0.75rem 1rem;
            }}

            .header-left {{
                width: 100%;
                justify-content: space-between;
            }}

            .design-info {{
                text-align: left;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="header-left">
            <span class="logo">1000 Design Vibes</span>
            <a href="about.html" class="about-link">What the heck is this?</a>
            <div class="nav-controls">
                <button class="nav-btn" id="prevBtn" title="Previous (←)">← Prev</button>
                <span class="counter" id="counter">1 / {len(designs)}</span>
                <button class="nav-btn" id="nextBtn" title="Next (→)">Next →</button>
            </div>
        </div>
        <div class="design-info">
            <div class="design-text">
                <div class="design-name" id="designName">Loading...</div>
                <div class="design-meta" id="designMeta"></div>
            </div>
            <button class="prompt-toggle" id="promptToggle">Show Prompt</button>
        </div>
    </header>

    <div class="prompt-panel" id="promptPanel">
        <div class="prompt-content" id="promptContent"></div>
    </div>

    <div class="viewer-container">
        <div class="loading" id="loading">Loading design...</div>
        <iframe id="viewer" title="Design preview"></iframe>
    </div>

    <div class="keyboard-hint" id="hint">
        ← → Arrow keys to navigate
    </div>

    <script>
        const designs = {json.dumps(designs, indent=2)};

        let currentIndex = 0;
        const viewer = document.getElementById('viewer');
        const counter = document.getElementById('counter');
        const designName = document.getElementById('designName');
        const designMeta = document.getElementById('designMeta');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const loading = document.getElementById('loading');
        const promptToggle = document.getElementById('promptToggle');
        const promptPanel = document.getElementById('promptPanel');
        const promptContent = document.getElementById('promptContent');

        function renderDimensions(dims) {{
            if (!dims || Object.keys(dims).length === 0) {{
                return '<div class="dim-group"><div class="dim-value" style="color: var(--text-muted)">No dimension data available</div></div>';
            }}
            return Object.entries(dims)
                .map(([key, value]) => `
                    <div class="dim-group">
                        <div class="dim-label">${{key.replace(/_/g, ' ')}}</div>
                        <div class="dim-value">${{value}}</div>
                    </div>
                `).join('');
        }}

        function loadDesign(index) {{
            if (index < 0 || index >= designs.length) return;

            currentIndex = index;
            const design = designs[index];

            loading.style.display = 'block';
            viewer.style.opacity = '0';

            viewer.onload = () => {{
                loading.style.display = 'none';
                viewer.style.opacity = '1';
            }};

            viewer.src = design.path;
            counter.textContent = `${{index + 1}} / ${{designs.length}}`;
            designName.textContent = design.name;
            designMeta.textContent = `${{design.batch}} · #${{design.id}}`;

            prevBtn.disabled = index === 0;
            nextBtn.disabled = index === designs.length - 1;

            // Update prompt panel content
            promptContent.innerHTML = renderDimensions(design.dimensions);

            // Update URL hash for bookmarking
            history.replaceState(null, '', `#${{design.batch}}/${{design.id}}`);
        }}

        // Prompt toggle
        promptToggle.addEventListener('click', () => {{
            promptPanel.classList.toggle('open');
            promptToggle.classList.toggle('active');
            promptToggle.textContent = promptPanel.classList.contains('open') ? 'Hide Prompt' : 'Show Prompt';
        }});

        function next() {{
            if (currentIndex < designs.length - 1) {{
                loadDesign(currentIndex + 1);
            }}
        }}

        function prev() {{
            if (currentIndex > 0) {{
                loadDesign(currentIndex - 1);
            }}
        }}

        // Button handlers
        prevBtn.addEventListener('click', prev);
        nextBtn.addEventListener('click', next);

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowRight') {{
                e.preventDefault();
                next();
            }} else if (e.key === 'ArrowLeft') {{
                e.preventDefault();
                prev();
            }}
        }});

        // Parse hash on load
        function parseHash() {{
            const hash = window.location.hash.slice(1);
            if (hash) {{
                const [batch, id] = hash.split('/');
                const index = designs.findIndex(d => d.batch === batch && d.id === parseInt(id));
                if (index !== -1) {{
                    return index;
                }}
            }}
            return 0;
        }}

        // Initialize
        loadDesign(parseHash());

        // Show hint briefly
        if (!localStorage.getItem('viewer-hint-shown')) {{
            const hint = document.getElementById('hint');
            setTimeout(() => hint.classList.add('visible'), 1000);
            setTimeout(() => {{
                hint.classList.remove('visible');
                localStorage.setItem('viewer-hint-shown', '1');
            }}, 4000);
        }}
    </script>
</body>
</html>
'''


def build_viewer(outputs_path: Path) -> None:
    """Build the unified design viewer."""
    console.print("[blue]Collecting designs from all batches...[/blue]")

    designs = collect_all_designs(outputs_path)

    if not designs:
        console.print("[red]No designs found![/red]")
        return

    console.print(f"[green]Found {len(designs)} designs across {len(set(d['batch'] for d in designs))} batches[/green]")

    # Write JSON
    json_path = outputs_path.parent / "all-designs.json"
    json_path.write_text(json.dumps(designs, indent=2))
    console.print(f"[green]Wrote {json_path}[/green]")

    # Write index HTML (the viewer is now the main page)
    viewer_html = generate_viewer_html(designs)
    index_path = outputs_path.parent / "index.html"
    index_path.write_text(viewer_html)
    console.print(f"[green]Wrote {index_path}[/green]")

    console.print(f"\n[bold]Open index.html to browse all {len(designs)} designs![/bold]")
