#!/usr/bin/env python3
# ABOUTME: CLI entry point for 1000 Design Vibes.
# ABOUTME: Provides manifest, generate, and validate commands.

import click
from dotenv import load_dotenv

load_dotenv()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """1000 Design Vibes - Generate unique design system showcases."""
    pass


@cli.command()
@click.option("--count", default=20, help="Number of designs to generate")
@click.option("--name", default=None, help="Optional name suffix for output folder")
@click.option("--no-api", is_flag=True, help="Use rule-based names instead of Claude API")
def manifest(count: int, name: str | None, no_api: bool):
    """Create a manifest with unique design seeds."""
    from src.manifest import generate_manifest
    generate_manifest(count=count, name=name, use_api=not no_api)


@cli.command()
@click.option("--manifest", "manifest_path", required=True, help="Path to manifest.json")
@click.option("--start", default=1, help="First design ID to generate")
@click.option("--end", default=None, type=int, help="Last design ID to generate")
@click.option("--model", default="claude-sonnet-4-20250514", help="Model to use for generation")
@click.option("--force", is_flag=True, help="Regenerate even if files exist")
def generate(manifest_path: str, start: int, end: int | None, model: str, force: bool):
    """Generate HTML showcase pages from a manifest."""
    from src.generator import generate_designs
    generate_designs(
        manifest_path=manifest_path,
        start=start,
        end=end,
        model=model,
        force=force,
    )


@cli.command()
@click.option("--path", required=True, help="Path to output folder to validate")
def validate(path: str):
    """Validate a generated design library."""
    from src.validator import validate_output
    validate_output(path=path)


if __name__ == "__main__":
    cli()
