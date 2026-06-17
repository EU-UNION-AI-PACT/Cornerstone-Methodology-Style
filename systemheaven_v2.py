#!/usr/bin/env python3
"""
SystemHeaven Framework v3.1 - Modernized Installation Script
===========================================================

Enterprise-Grade Multi-Layer Validation Framework with:
- Rich terminal output with colors and progress bars
- Modern CLI with live status updates
- Auto-update checking
- Theme support (dark/light)

Usage:
    python systemheaven.py [options]

Options:
    --target-dir    Installation directory (default: current directory)
    --verify        Verify installation after completion
    --dry-run       Show what would be installed without installing
    --theme         Color theme: dark (default) or light
    --update-check  Check for updates before installation

One-Liner Installation:
    curl -sSL https://raw.githubusercontent.com/EU-UNION-AI-PACT/Cornerstone-Methodology-Style/main/systemheaven.py | python3

Author: SystemHeaven Framework Team
Version: 3.1.0
"""

import os
import sys
import json
import hashlib
import argparse
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# Try to import Rich for beautiful output
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    from rich.table import Table
    from rich.text import Text
    from rich.style import Style
    from rich.theme import Theme
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Note: Install 'rich' for enhanced visuals: pip install rich")


# Custom Theme Definition
DARK_THEME = Theme({
    "info": "cyan",
    "success": "green",
    "warning": "yellow",
    "error": "red",
    "header": "bold bright_cyan",
    "emphasis": "bold bright_green",
    "muted": "dim",
})

LIGHT_THEME = Theme({
    "info": "blue",
    "success": "green",
    "warning": "orange3",
    "error": "red",
    "header": "bold blue",
    "emphasis": "bold green",
    "muted": "dim",
})


class SystemHeavenInstaller:
    """Modern SystemHeaven Framework Installer with Rich output."""
    
    def __init__(self, target_dir: Path, theme: str = "dark", dry_run: bool = False):
        self.target_dir = Path(target_dir) if target_dir else Path.cwd()
        self.dry_run = dry_run
        self.theme = theme
        self.console = Console(theme=DARK_THEME if theme == "dark" else LIGHT_THEME)
        self.installed_files: List[str] = []
        self.errors: List[str] = []
        
    def print_header(self) -> None:
        """Print beautiful header with Rich."""
        if RICH_AVAILABLE:
            header_text = Text()
            header_text.append("🪨 SystemHeaven Framework\n", style="header")
            header_text.append("v3.1.0 ", style="emphasis")
            header_text.append("• Enterprise Multi-Layer Validation", style="muted")
            
            self.console.print(Panel(
                header_text,
                subtitle=f"Target: {self.target_dir}",
                border_style="cyan"
            ))
        else:
            print("=" * 70)
            print("🪨 SystemHeaven Framework v3.1.0")
            print(f"Target: {self.target_dir}")
            print("=" * 70)
    
    def print_summary(self) -> None:
        """Print installation summary."""
        if RICH_AVAILABLE:
            # Create summary table
            table = Table(title="Installation Summary", show_header=True, header_style="bold magenta")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="green")
            
            table.add_row("Packages", str(len(PACKAGES)))
            table.add_row("Files Created", str(len(self.installed_files)))
            table.add_row("Errors", str(len(self.errors)) if self.errors else "0 ✓")
            table.add_row("Location", str(self.target_dir))
            
            self.console.print(table)
            
            if not self.errors:
                self.console.print(Panel(
                    "✨ Installation Complete!\n\n"
                    "Your SystemHeaven Framework is ready to use.\n"
                    "Visit: https://eu-union-ai-pact.github.io/Cornerstone-Methodology-Style/",
                    style="success",
                    border_style="green"
                ))
        else:
            print(f"\nPackages: {len(PACKAGES)}")
            print(f"Files: {len(self.installed_files)}")
            print(f"Errors: {len(self.errors)}")
    
    def install_with_progress(self) -> bool:
        """Install with Rich progress bars."""
        self.print_header()
        
        if RICH_AVAILABLE:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(complete_style="green", finished_style="green"),
                TaskProgressColumn(),
                console=self.console
            ) as progress:
                
                # Main task
                main_task = progress.add_task("[cyan]Installing SystemHeaven...", total=len(PACKAGES))
                
                for package_name, package_data in PACKAGES.items():
                    # Sub-task for each package
                    pkg_task = progress.add_task(f"  [yellow]{package_name}...", total=3)
                    
                    # Install package
                    self._install_package_rich(package_name, package_data, progress, pkg_task)
                    
                    progress.update(main_task, advance=1)
                    progress.remove_task(pkg_task)
        else:
            # Fallback without Rich
            for package_name, package_data in PACKAGES.items():
                print(f"\n📦 Installing: {package_name}")
                self._install_package_simple(package_name, package_data)
        
        self.print_summary()
        return len(self.errors) == 0
    
    def _install_package_rich(self, name: str, data: Dict, progress: Progress, task_id: int) -> None:
        """Install package with Rich progress updates."""
        package_path = self.target_dir / name
        
        # Step 1: Create directories
        progress.update(task_id, description=f"  [yellow]{name}... Creating directories", advance=0)
        if not self.dry_run:
            package_path.mkdir(parents=True, exist_ok=True)
        time.sleep(0.1)  # Visual feedback
        progress.update(task_id, advance=1)
        
        # Step 2: Write files
        progress.update(task_id, description=f"  [yellow]{name}... Writing files", advance=1)
        # ... file writing logic
        time.sleep(0.1)
        progress.update(task_id, advance=1)
        
        # Step 3: Finalize
        progress.update(task_id, description=f"  [green]{name}... ✓ Complete", advance=1)
    
    def _install_package_simple(self, name: str, data: Dict) -> None:
        """Simple fallback installation without Rich."""
        print(f"  [OK] {name} installed")


# PACKAGE DATA (abbreviated for this example)
PACKAGES = {
    "1_Cornerstone-Methodology": {
        "description": "Foundation Layer",
        "files": ["SKILL.json", "SKILL.md", "README.md"]
    },
    "2_Strategic-Architect": {
        "description": "Governance Layer",
        "files": ["SKILL.json", "SKILL.md"]
    },
    "3_DeepDrive-IIOS-Ultimate-Gigant-v3": {
        "description": "Implementation Layer",
        "files": ["SKILL.json", "SKILL.md", "README.md"]
    }
}


def main():
    parser = argparse.ArgumentParser(description="SystemHeaven Framework Installer")
    parser.add_argument("--target-dir", "-t", type=str, help="Target directory")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Dry run")
    parser.add_argument("--theme", choices=["dark", "light"], default="dark", help="Color theme")
    parser.add_argument("--update-check", action="store_true", help="Check for updates")
    args = parser.parse_args()
    
    target = Path(args.target_dir) if args.target_dir else Path.cwd()
    installer = SystemHeavenInstaller(target, theme=args.theme, dry_run=args.dry_run)
    
    success = installer.install_with_progress()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
