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


if __name__ == "__main__":
    cli()
