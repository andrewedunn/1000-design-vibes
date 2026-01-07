# ABOUTME: Shows generation progress for a design batch.
# ABOUTME: Reports completed, staging, and failed designs.

import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()


def show_status(path: str) -> None:
    """Show generation progress for a batch."""
    output_path = Path(path)

    if not output_path.exists():
        console.print(f"[red]Error:[/red] Path not found: {path}")
        return

    manifest_path = output_path / "manifest.json"
    if not manifest_path.exists():
        console.print(f"[red]Error:[/red] No manifest.json found in {path}")
        return

    manifest = json.loads(manifest_path.read_text())
    total = manifest["total_designs"]

    # Count completed designs
    designs_dir = output_path / "designs"
    completed = set()
    if designs_dir.exists():
        for f in designs_dir.glob("design-*.html"):
            try:
                design_id = int(f.stem.replace("design-", ""))
                completed.add(design_id)
            except ValueError:
                pass

    # Count staging designs
    staging_dir = output_path / ".staging"
    staging = set()
    if staging_dir.exists():
        for f in staging_dir.glob("design-*.html"):
            try:
                design_id = int(f.stem.replace("design-", ""))
                staging.add(design_id)
            except ValueError:
                pass

    # Load failures if any
    failures_path = output_path / "failures.json"
    failures = []
    if failures_path.exists():
        failures = json.loads(failures_path.read_text())

    failed_ids = {f["id"] for f in failures}
    pending = total - len(completed) - len(staging) - len(failed_ids)

    # Display summary
    console.print(f"\n[bold blue]1000 Design Vibes[/bold blue] - Status\n")
    console.print(f"Batch: [cyan]{output_path.name}[/cyan]")
    console.print()

    table = Table(show_header=False, box=None)
    table.add_column("Label", style="dim")
    table.add_column("Count", justify="right")
    table.add_column("Bar", width=30)

    def progress_bar(count: int, total: int, color: str) -> str:
        pct = count / total if total > 0 else 0
        filled = int(pct * 30)
        return f"[{color}]{'█' * filled}[/{color}]{'░' * (30 - filled)}"

    table.add_row("Completed", f"[green]{len(completed)}[/green]", progress_bar(len(completed), total, "green"))
    table.add_row("In Staging", f"[yellow]{len(staging)}[/yellow]", progress_bar(len(staging), total, "yellow"))
    table.add_row("Failed", f"[red]{len(failed_ids)}[/red]", progress_bar(len(failed_ids), total, "red"))
    table.add_row("Pending", f"[dim]{pending}[/dim]", progress_bar(pending, total, "dim"))
    table.add_row("", "", "")
    table.add_row("Total", f"[bold]{total}[/bold]", "")

    console.print(table)

    # Show next designs to generate
    if pending > 0:
        all_done = completed | staging | failed_ids
        next_ids = sorted([i for i in range(1, total + 1) if i not in all_done])[:5]
        console.print(f"\n[dim]Next to generate: {', '.join(f'#{i}' for i in next_ids)}[/dim]")

    # Show failures if any
    if failures:
        console.print(f"\n[red]Failed designs:[/red]")
        for f in failures[:5]:
            console.print(f"  #{f['id']}: {f.get('error', 'Unknown error')}")
        if len(failures) > 5:
            console.print(f"  ... and {len(failures) - 5} more")

    console.print()
