# ABOUTME: Generates HTML design showcase pages from manifest entries.
# ABOUTME: Calls Claude API to create self-contained design system files.

from rich.console import Console

console = Console()


def generate_designs(
    manifest_path: str,
    start: int,
    end: int | None,
    model: str,
    force: bool,
) -> None:
    """Generate HTML showcase pages from a manifest."""
    console.print("[yellow]generate command not yet implemented[/yellow]")
    console.print(f"Would generate designs {start}-{end} from {manifest_path}")
    console.print(f"Using model: {model}, force={force}")
