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
def manifest(count: int, name: str | None):
    """Create a manifest with unique design seeds."""
    from src.manifest import generate_manifest
    generate_manifest(count=count, name=name)


@cli.command()
@click.option("--path", required=True, help="Path to output folder")
def status(path: str):
    """Show generation progress for a batch."""
    from src.status import show_status
    show_status(path=path)


@cli.command()
def build_indexes():
    """Build or rebuild index pages for all runs."""
    from pathlib import Path
    from src.index import build_all_indexes

    outputs_path = Path("outputs")
    if not outputs_path.exists():
        click.echo("No outputs directory found")
        return

    build_all_indexes(outputs_path)
    click.echo("Done!")


if __name__ == "__main__":
    cli()
