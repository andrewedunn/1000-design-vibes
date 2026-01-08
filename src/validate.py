# ABOUTME: Validates design HTML files for common issues.
# ABOUTME: Checks for unclosed CSS comments, HTML comments in style blocks, and other problems.

import re
from pathlib import Path
from dataclasses import dataclass

from rich.console import Console
from rich.table import Table

console = Console()


@dataclass
class ValidationIssue:
    """Represents a validation issue found in a design file."""
    file: str
    issue_type: str
    description: str
    line: int | None = None
    fixable: bool = True


def validate_css_comments(content: str, filename: str) -> list[ValidationIssue]:
    """Check for CSS comment issues inside style blocks."""
    issues = []
    lines = content.split('\n')

    # Find the style block
    style_start = None
    style_end = None
    root_line = None

    for i, line in enumerate(lines, 1):
        if '<style>' in line or '<style ' in line:
            style_start = i
        if '</style>' in line:
            style_end = i
        if ':root' in line and '{' in line:
            root_line = i
            break

    if not style_start or not root_line:
        return issues

    # Check for HTML comments inside style block (before :root)
    style_section = '\n'.join(lines[style_start-1:root_line-1])
    if '<!--' in style_section:
        # Find the actual line number
        for i in range(style_start, root_line):
            if '<!--' in lines[i-1]:
                issues.append(ValidationIssue(
                    file=filename,
                    issue_type="html_comment_in_css",
                    description="HTML comment <!-- --> used inside <style> block (should use /* */)",
                    line=i,
                    fixable=True
                ))
                break

    # Check for unclosed CSS comments before :root
    css_comment_open = None
    css_comment_close = None

    for i in range(style_start, root_line):
        line = lines[i-1]
        if '/*' in line and css_comment_open is None:
            css_comment_open = i
        if '*/' in line:
            css_comment_close = i

    if css_comment_open and (css_comment_close is None or css_comment_close > root_line):
        issues.append(ValidationIssue(
            file=filename,
            issue_type="unclosed_css_comment",
            description="CSS comment /* not closed before :root declaration",
            line=css_comment_open,
            fixable=True
        ))

    return issues


def validate_design(file_path: Path) -> list[ValidationIssue]:
    """Validate a single design file and return any issues found."""
    issues = []
    content = file_path.read_text()
    filename = file_path.name

    # Basic structure checks
    if '<!DOCTYPE html>' not in content:
        issues.append(ValidationIssue(
            file=filename,
            issue_type="missing_doctype",
            description="Missing <!DOCTYPE html> declaration",
            fixable=False
        ))

    if '<style' not in content:
        issues.append(ValidationIssue(
            file=filename,
            issue_type="missing_style",
            description="Missing <style> block",
            fixable=False
        ))

    if 'ArrowRight' not in content or 'ArrowLeft' not in content:
        issues.append(ValidationIssue(
            file=filename,
            issue_type="missing_navigation",
            description="Missing keyboard navigation script",
            fixable=False
        ))

    # File size check
    size = file_path.stat().st_size
    if size < 10000:
        issues.append(ValidationIssue(
            file=filename,
            issue_type="too_small",
            description=f"File size {size} bytes is below 10KB minimum",
            fixable=False
        ))

    # CSS comment checks
    issues.extend(validate_css_comments(content, filename))

    return issues


def fix_css_comments(file_path: Path) -> tuple[bool, str]:
    """
    Fix CSS comment issues in a design file.
    Returns (was_fixed, description).
    """
    content = file_path.read_text()
    lines = content.split('\n')
    modified = False
    fixes = []

    # Find style block and :root
    style_start = None
    root_line = None

    for i, line in enumerate(lines):
        if '<style>' in line or '<style ' in line:
            style_start = i
        if ':root' in line and '{' in line:
            root_line = i
            break

    if not style_start or not root_line:
        return False, "Could not find style block or :root"

    # Fix HTML comments in style block
    for i in range(style_start, root_line):
        if '<!--' in lines[i]:
            lines[i] = lines[i].replace('<!--', '/*')
            modified = True
            fixes.append(f"Line {i+1}: Replaced <!-- with /*")
        if '-->' in lines[i] and '<style' not in lines[i]:
            lines[i] = lines[i].replace('-->', '*/')
            modified = True
            fixes.append(f"Line {i+1}: Replaced --> with */")

    # Check if CSS comment is unclosed before :root
    css_comment_open = None
    css_comment_closed = False

    for i in range(style_start, root_line):
        if '/*' in lines[i]:
            css_comment_open = i
        if '*/' in lines[i]:
            css_comment_closed = True

    if css_comment_open is not None and not css_comment_closed:
        # Insert */ before :root line
        lines.insert(root_line, '        */')
        modified = True
        fixes.append(f"Line {root_line+1}: Inserted */ to close CSS comment")

    if modified:
        file_path.write_text('\n'.join(lines))
        return True, '; '.join(fixes)

    return False, "No fixes needed"


def validate_batch(batch_path: Path, fix: bool = False) -> dict:
    """
    Validate all designs in a batch.
    Returns dict with results summary.
    """
    designs_dir = batch_path / "designs"
    if not designs_dir.exists():
        designs_dir = batch_path / ".staging"

    if not designs_dir.exists():
        console.print(f"[red]No designs or staging folder found in {batch_path}[/red]")
        return {"total": 0, "with_issues": 0, "issues": []}

    all_issues = []
    files_with_issues = set()
    fixed_count = 0

    design_files = sorted(designs_dir.glob("design-*.html"))

    for design_file in design_files:
        issues = validate_design(design_file)

        if issues:
            files_with_issues.add(design_file.name)

            if fix:
                # Try to fix fixable issues
                fixable = [i for i in issues if i.fixable]
                if fixable:
                    was_fixed, fix_desc = fix_css_comments(design_file)
                    if was_fixed:
                        fixed_count += 1
                        console.print(f"[green]Fixed {design_file.name}:[/green] {fix_desc}")
                        # Re-validate after fix
                        issues = validate_design(design_file)

        all_issues.extend(issues)

    return {
        "total": len(design_files),
        "with_issues": len(files_with_issues),
        "issues": all_issues,
        "fixed": fixed_count
    }


def show_validation_report(results: dict) -> None:
    """Display a formatted validation report."""
    issues = results["issues"]

    if not issues:
        console.print(f"\n[green]✓ All {results['total']} designs passed validation[/green]")
        return

    # Group by issue type
    by_type = {}
    for issue in issues:
        if issue.issue_type not in by_type:
            by_type[issue.issue_type] = []
        by_type[issue.issue_type].append(issue)

    console.print(f"\n[yellow]Found {len(issues)} issues in {results['with_issues']} files:[/yellow]\n")

    table = Table(show_header=True, header_style="bold")
    table.add_column("Issue Type", style="cyan")
    table.add_column("Count", justify="right")
    table.add_column("Fixable", justify="center")

    for issue_type, type_issues in sorted(by_type.items()):
        fixable = "✓" if type_issues[0].fixable else "✗"
        table.add_row(issue_type, str(len(type_issues)), fixable)

    console.print(table)

    if results.get("fixed", 0) > 0:
        console.print(f"\n[green]Fixed {results['fixed']} files[/green]")

    # Show first few of each type
    console.print("\n[bold]Examples:[/bold]")
    for issue_type, type_issues in sorted(by_type.items()):
        console.print(f"\n  [cyan]{issue_type}[/cyan]:")
        for issue in type_issues[:3]:
            line_info = f" (line {issue.line})" if issue.line else ""
            console.print(f"    • {issue.file}{line_info}: {issue.description}")
        if len(type_issues) > 3:
            console.print(f"    ... and {len(type_issues) - 3} more")
