# ABOUTME: Script to remove arrow key navigation from design files
# ABOUTME: This allows the viewer's navigation to work without conflicts

import re
from pathlib import Path

def strip_arrow_navigation(html: str) -> str:
    """Remove ArrowLeft/ArrowRight key handlers from HTML."""

    # Pattern 1: Lines with ArrowLeft or ArrowRight in if statements
    # Handles: if (e.key === 'ArrowRight') { ... }
    # Handles: if (e.key === 'ArrowLeft') navigatePrevious();
    patterns = [
        # Multi-line if blocks with ArrowRight/ArrowLeft
        r"\s*if\s*\(\s*e\.key\s*===?\s*['\"]Arrow(?:Right|Left)['\"]\s*\)\s*\{[^}]*\}\s*\n?",
        # Single-line if statements
        r"\s*if\s*\(\s*e\.key\s*===?\s*['\"]Arrow(?:Right|Left)['\"]\s*\)[^;]*;\s*\n?",
        # Case statements in switch blocks
        r"\s*case\s*['\"]Arrow(?:Right|Left)['\"]:[^:]*?(?=case|default|break|\})",
    ]

    result = html
    for pattern in patterns:
        result = re.sub(pattern, '\n', result, flags=re.MULTILINE | re.DOTALL)

    return result


def process_file(filepath: Path) -> bool:
    """Process a single file. Returns True if modified."""
    content = filepath.read_text()

    if 'ArrowRight' not in content and 'ArrowLeft' not in content:
        return False

    new_content = strip_arrow_navigation(content)

    if new_content != content:
        filepath.write_text(new_content)
        return True

    return False


def main():
    outputs_path = Path("outputs")
    modified = 0
    total = 0

    for batch_dir in sorted(outputs_path.iterdir()):
        designs_dir = batch_dir / "designs"
        if not designs_dir.exists():
            continue

        for design_file in sorted(designs_dir.glob("design-*.html")):
            total += 1
            if process_file(design_file):
                modified += 1
                print(f"  Modified: {design_file.relative_to(outputs_path)}")

    print(f"\nProcessed {total} files, modified {modified}")


if __name__ == "__main__":
    main()
