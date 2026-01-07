# ABOUTME: Builds the gallery index.html page.
# ABOUTME: Creates a browsable grid of all designs with previews and navigation.

from pathlib import Path

from rich.console import Console

console = Console()


def build_index(output_path: Path, manifest: dict) -> None:
    """Build the index.html gallery page."""
    console.print("[yellow]index builder not yet implemented[/yellow]")
