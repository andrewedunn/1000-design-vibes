#!/usr/bin/env python3
# ABOUTME: CLI entry point for 1000 Design Vibes.
# ABOUTME: Provides manifest and status commands. Design generation happens via Claude Code agents.

import click


@click.group()
@click.version_option(version="0.2.0")
def cli():
    """1000 Design Vibes - Generate unique design system showcases."""
    pass


@cli.command()
@click.option("--count", default=20, help="Number of designs to generate")
@click.option("--name", default=None, help="Optional name suffix for output folder")
@click.option("--core-only", is_flag=True, help="Only specify core dimensions, let agent choose the rest")
def manifest(count: int, name: str | None, core_only: bool):
    """Create a manifest with unique design seeds."""
    from src.manifest import generate_manifest
    generate_manifest(count=count, name=name, core_only=core_only)


@cli.command()
@click.option("--path", required=True, help="Path to output folder")
def status(path: str):
    """Show generation progress for a batch."""
    from src.status import show_status
    show_status(path=path)


@cli.command()
@click.option("--path", required=True, help="Path to output folder")
@click.option("--fix", is_flag=True, help="Attempt to fix fixable issues")
def validate(path: str, fix: bool):
    """Validate designs for CSS comment issues and other problems."""
    from pathlib import Path
    from src.validate import validate_batch, show_validation_report

    batch_path = Path(path)
    if not batch_path.exists():
        click.echo(f"Path not found: {path}")
        return

    results = validate_batch(batch_path, fix=fix)
    show_validation_report(results)


@cli.command()
def build_viewer():
    """Build unified viewer for browsing all designs."""
    from pathlib import Path
    from src.viewer import build_viewer

    outputs_path = Path("outputs")
    if not outputs_path.exists():
        click.echo("No outputs directory found")
        return

    build_viewer(outputs_path)


if __name__ == "__main__":
    cli()
