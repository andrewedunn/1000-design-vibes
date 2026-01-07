# ABOUTME: Generates HTML design showcase pages from manifest entries.
# ABOUTME: Calls Claude API to create self-contained design system files.

import json
import os
from pathlib import Path

import anthropic
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from .index import build_index

console = Console()

PROMPT_TEMPLATE_PATH = Path(__file__).parent.parent / "templates" / "design_prompt.md"


def load_manifest(manifest_path: str) -> dict:
    """Load and validate a manifest file."""
    with open(manifest_path) as f:
        return json.load(f)


def format_dimensions(dimensions: dict[str, str]) -> str:
    """Format dimensions as a readable list."""
    lines = []
    for key, value in dimensions.items():
        formatted_key = key.replace("_", " ").title()
        formatted_value = value.replace("_", " ")
        lines.append(f"- **{formatted_key}**: {formatted_value}")
    return "\n".join(lines)


def build_prompt(design: dict, total_designs: int) -> str:
    """Build the generation prompt for a design."""
    template = PROMPT_TEMPLATE_PATH.read_text()

    prompt = template.format(
        id=design["id"],
        name=design["name"],
        tagline=design["tagline"],
        dimensions_formatted=format_dimensions(design["dimensions"]),
        dimensions_json=json.dumps(design["dimensions"], indent=2),
        total_designs=total_designs,
    )

    return prompt


def generate_single_design(
    design: dict,
    total_designs: int,
    output_dir: Path,
    model: str,
    client: anthropic.Anthropic,
) -> bool:
    """Generate a single design HTML file."""
    prompt = build_prompt(design, total_designs)

    try:
        response = client.messages.create(
            model=model,
            max_tokens=16000,
            messages=[{"role": "user", "content": prompt}],
        )

        html_content = response.content[0].text

        # Clean up if wrapped in code blocks
        if html_content.startswith("```html"):
            html_content = html_content[7:]
        if html_content.startswith("```"):
            html_content = html_content[3:]
        if html_content.endswith("```"):
            html_content = html_content[:-3]
        html_content = html_content.strip()

        # Save the file
        output_file = output_dir / f"design-{design['id']}.html"
        output_file.write_text(html_content)

        return True

    except Exception as e:
        console.print(f"[red]Error generating design {design['id']}: {e}[/red]")
        return False


def generate_designs(
    manifest_path: str,
    start: int,
    end: int | None,
    model: str,
    force: bool,
) -> None:
    """Generate HTML showcase pages from a manifest."""
    console.print(f"\n[bold blue]1000 Design Vibes[/bold blue] - Design Generator\n")

    # Load manifest
    manifest = load_manifest(manifest_path)
    total_designs = manifest["total_designs"]
    designs = manifest["designs"]

    # Determine range
    if end is None:
        end = total_designs
    end = min(end, total_designs)

    # Get output directory from manifest path
    output_dir = Path(manifest_path).parent / "designs"
    output_dir.mkdir(exist_ok=True)

    console.print(f"Manifest: [green]{manifest_path}[/green]")
    console.print(f"Generating designs {start}-{end} of {total_designs}")
    console.print(f"Model: [cyan]{model}[/cyan]")
    console.print(f"Output: [green]{output_dir}[/green]\n")

    # Check API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        console.print("[red]Error: ANTHROPIC_API_KEY not set[/red]")
        return

    client = anthropic.Anthropic(api_key=api_key)

    # Filter designs in range
    designs_to_generate = [d for d in designs if start <= d["id"] <= end]

    # Check for existing files
    if not force:
        skipped = []
        remaining = []
        for design in designs_to_generate:
            output_file = output_dir / f"design-{design['id']}.html"
            if output_file.exists():
                skipped.append(design["id"])
            else:
                remaining.append(design)

        if skipped:
            console.print(f"[yellow]Skipping {len(skipped)} existing designs: {skipped}[/yellow]")
            console.print("[dim]Use --force to regenerate[/dim]\n")

        designs_to_generate = remaining

    if not designs_to_generate:
        console.print("[green]All designs already generated![/green]")
        return

    # Generate designs
    success_count = 0
    fail_count = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Generating designs...", total=len(designs_to_generate))

        for design in designs_to_generate:
            progress.update(task, description=f"Design {design['id']}: {design['name']}")

            success = generate_single_design(
                design=design,
                total_designs=total_designs,
                output_dir=output_dir,
                model=model,
                client=client,
            )

            if success:
                success_count += 1
                console.print(f"  [green]✓[/green] #{design['id']}: {design['name']}")
            else:
                fail_count += 1

            progress.update(task, advance=1)

    # Summary
    console.print(f"\n[bold]Generation complete![/bold]")
    console.print(f"  [green]✓ Success: {success_count}[/green]")
    if fail_count:
        console.print(f"  [red]✗ Failed: {fail_count}[/red]")

    # Count total generated files
    generated_files = list(output_dir.glob("design-*.html"))
    console.print(f"\n  Total designs generated: {len(generated_files)}/{total_designs}")

    # Rebuild index
    console.print(f"\n[bold]Rebuilding gallery index...[/bold]")
    build_index(Path(manifest_path).parent, manifest)
    console.print(f"[green]✓[/green] Index updated")

    console.print(f"\n[dim]Open {Path(manifest_path).parent / 'index.html'} to browse designs[/dim]")
