# ABOUTME: Generates design manifests with unique dimension combinations.
# ABOUTME: Handles weighted sampling, deduplication, and name generation via Claude.

import hashlib
import json
import os
import random
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from .dimensions import ALL_DIMENSIONS, get_dimension_names
from .naming import generate_name

console = Console()


def compute_dimension_hash(dimensions: dict[str, str]) -> str:
    """Compute a unique hash for a dimension combination."""
    serialized = json.dumps(dimensions, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()


def dimension_distance(d1: dict[str, str], d2: dict[str, str]) -> int:
    """Count how many dimensions differ between two designs."""
    differences = 0
    for key in d1.keys():
        if d1.get(key) != d2.get(key):
            differences += 1
    return differences


def generate_balanced_combinations(
    n_designs: int,
    min_distance: int = 3,
    max_attempts: int = 1000,
) -> list[dict[str, str]]:
    """Generate unique dimension combinations with balanced coverage."""
    combinations: list[dict[str, str]] = []
    seen_hashes: set[str] = set()
    dimension_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Generating {n_designs} unique combinations...", total=n_designs)

        while len(combinations) < n_designs:
            attempts = 0
            while attempts < max_attempts:
                combo = {}
                for dim in ALL_DIMENSIONS:
                    values = list(dim.values.keys())
                    weights = []
                    for value in values:
                        count = dimension_counts[dim.name][value]
                        weights.append(1.0 / (count + 1))

                    total = sum(weights)
                    weights = [w / total for w in weights]

                    chosen = random.choices(values, weights=weights)[0]
                    combo[dim.name] = chosen

                combo_hash = compute_dimension_hash(combo)
                if combo_hash in seen_hashes:
                    attempts += 1
                    continue

                if min_distance > 0 and combinations:
                    too_close = False
                    for existing in combinations[-50:]:
                        if dimension_distance(combo, existing) < min_distance:
                            too_close = True
                            break
                    if too_close:
                        attempts += 1
                        continue

                seen_hashes.add(combo_hash)
                for dim_name, value in combo.items():
                    dimension_counts[dim_name][value] += 1
                combinations.append(combo)
                progress.update(task, advance=1)
                break
            else:
                console.print(f"[yellow]Warning: Relaxing constraints after {max_attempts} attempts[/yellow]")
                combo = {}
                for dim in ALL_DIMENSIONS:
                    values = list(dim.values.keys())
                    combo[dim.name] = random.choice(values)
                combo_hash = compute_dimension_hash(combo)
                if combo_hash not in seen_hashes:
                    seen_hashes.add(combo_hash)
                    combinations.append(combo)
                    progress.update(task, advance=1)

    return combinations


def create_output_folder(name: str | None) -> Path:
    """Create a date-stamped output folder."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    folder_name = f"{date_str}-{name}" if name else date_str

    base_path = Path("outputs")
    base_path.mkdir(exist_ok=True)

    output_path = base_path / folder_name
    counter = 1
    original_path = output_path
    while output_path.exists():
        output_path = Path(f"{original_path}-{counter}")
        counter += 1

    output_path.mkdir(parents=True)
    (output_path / "designs").mkdir()

    return output_path


def generate_manifest(count: int, name: str | None) -> None:
    """Generate a complete manifest with unique designs."""
    console.print(f"\n[bold blue]1000 Design Vibes[/bold blue] - Manifest Generator\n")

    output_path = create_output_folder(name)
    console.print(f"Output folder: [green]{output_path}[/green]\n")

    combinations = generate_balanced_combinations(count)

    console.print(f"\n[bold]Generating names for {count} designs...[/bold]")
    names_and_taglines = [generate_name(combo) for combo in combinations]

    designs = []
    for i, (combo, (design_name, tagline)) in enumerate(zip(combinations, names_and_taglines), start=1):
        design = {
            "id": i,
            "seed": hashlib.md5(json.dumps(combo, sort_keys=True).encode()).hexdigest()[:12],
            "name": design_name,
            "tagline": tagline,
            "dimensions": combo,
            "meta": {
                "dimension_hash": compute_dimension_hash(combo),
                "uniqueness_verified": True,
            },
        }
        designs.append(design)

    manifest = {
        "version": "1.0.0",
        "generated_at": datetime.now().isoformat(),
        "total_designs": count,
        "dimensions_version": "1.0.0",
        "designs": designs,
    }

    manifest_path = output_path / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    console.print(f"\n[green]✓[/green] Manifest saved to: [bold]{manifest_path}[/bold]")
    console.print(f"[green]✓[/green] Generated {count} unique designs")

    console.print("\n[bold]Sample designs:[/bold]")
    for design in designs[:3]:
        console.print(f"  #{design['id']}: [cyan]{design['name']}[/cyan] - {design['tagline']}")

    console.print(f"\n[dim]Next step: python design_vibes.py generate --manifest {manifest_path} --start 1 --end 10[/dim]")
