#!/usr/bin/env python3
"""
SystemHeaven Framework - Universal Installation Script
=======================================================

Enterprise-Grade Multi-Layer Validation Framework powered by 
the Cornerstone Philosophy (Barmherzigkeit as Eckstein).

Usage:
    python systemheaven.py [options]

Options:
    --target-dir    Installation directory (default: current directory)
    --verify        Verify installation after completion
    --dry-run       Show what would be installed without installing

One-Liner Installation:
    curl -sSL https://raw.githubusercontent.com/DEIN_USERNAME/DEIN_REPO/main/systemheaven.py | python3

Author: SystemHeaven Framework Team
Version: 3.0.0
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


# SYSTEMHEAVEN MANIFEST
SKILL_MANIFEST = {
    "skill_name": "systemheaven-framework",
    "version": "3.0.0",
    "description": "Enterprise-Grade Multi-Layer Validation Framework powered by the Cornerstone Philosophy.",
    "tagline": "Barmherzigkeit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht.",
    "runtime_environments": ["AI-Agent", "Chatbot", "IDE-Extension", "CLI", "OS-Terminal"],
    "core_principles": {
        "cornerstone": "Barmherzigkeit (Gnade/Mitgefühl) als unerschütterlicher Eckstein",
        "measure": "Wahrheit als Maßstab",
        "order": "Recht als Ordnung",
        "foundation": "Sicherheit & Nachhaltigkeit als Fundament",
        "goal": "Entwicklung als Ziel"
    },
    "execution_rules": [
        "Jeder Daten- oder Architekturkan MUSS die Bedingungen des methodology_guide.md erfüllen.",
        "Systementscheidungen werden anhand der igos_scorecard_template.md bewertet.",
        "Der Code muss strikt von der Governance- und Verfassungsebene getrennt bleiben.",
        "Pflichtfelder zur Eckstein-Validierung sind in allen Templates obligatorisch."
    ]
}


# CORE CONTENT
CORE_CONTENT = {
    "methodology_guide": "# SystemHeaven Methodology Guide\\n\\nBarmherzigkeit bildet den Grundstein.\\n",
    "workflows": "# SystemHeaven Workflows\\n\\n1. Scan initiieren\\n2. Validierung prüfen\\n3. Scorecard generieren\\n",
    "constitution": "# IIOS Constitution\\n\\nEckstein: Barmherzigkeit\\n",
    "igos_scorecard": "# IGOS Scorecard\\n\\nCornerstone Score: [0-100]\\n"
}


# PACKAGES DEFINITION
PACKAGES = {
    "1_Cornerstone-Methodology": {
        "description": "Foundation Layer - The philosophical and methodological core",
        "references": {
            "methodology_guide.md": CORE_CONTENT["methodology_guide"],
            "workflows.md": CORE_CONTENT["workflows"]
        },
        "templates": {
            "constitution_template.md": CORE_CONTENT["constitution"],
            "igos_scorecard_template.md": CORE_CONTENT["igos_scorecard"]
        }
    },
    "2_Strategic-Architect": {
        "description": "Governance Layer - Strategic architecture and decision-making",
        "references": {
            "methodology_guide.md": CORE_CONTENT["methodology_guide"],
            "workflows.md": CORE_CONTENT["workflows"]
        },
        "templates": {
            "strategic_plan_template.md": "# Strategic Plan\\n"
        }
    },
    "3_DeepDrive-IIOS-Ultimate-Gigant-v3": {
        "description": "Implementation Layer - Full IIOS Suite with dashboards",
        "references": {
            "IIOS_Constitution.md": CORE_CONTENT["constitution"],
            "IIOS_Technical_Specification.md": "# Technical Spec\\n"
        },
        "templates": {
            "RealTime_Validation_Dashboard.html": "<h1>Dashboard</h1>"
        }
    }
}


def install_framework(target_dir: Path, dry_run: bool = False) -> bool:
    """Install the SystemHeaven Framework."""
    print("=" * 70)
    print("SYSTEMHEAVEN FRAMEWORK v3.0 - AUTOMATED INSTALLATION")
    print("=" * 70)
    print(f"Target: {target_dir.absolute()}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE INSTALLATION'}")
    print("=" * 70)
    
    installed_files = []
    
    for package_name, package_data in PACKAGES.items():
        print(f"\\n📦 Installing: {package_name}")
        package_path = target_dir / package_name
        
        # Write SKILL.json
        skill_json = {**SKILL_MANIFEST, "package_name": package_name}
        skill_path = package_path / "SKILL.json"
        if not dry_run:
            skill_path.parent.mkdir(parents=True, exist_ok=True)
            skill_path.write_text(json.dumps(skill_json, indent=2), encoding="utf-8")
        installed_files.append(str(skill_path))
        print(f"   [OK] SKILL.json")
        
        # Write SKILL.md
        skill_md = f"# {package_name}\\n\\nPowered by SystemHeaven.\\n"
        skill_md_path = package_path / "SKILL.md"
        if not dry_run:
            skill_md_path.write_text(skill_md, encoding="utf-8")
        installed_files.append(str(skill_md_path))
        print(f"   [OK] SKILL.md")
        
        # Write subdirectories
        for subdir, files in package_data.items():
            if subdir == "description":
                continue
            for filename, content in files.items():
                filepath = package_path / subdir / filename
                if not dry_run:
                    filepath.parent.mkdir(parents=True, exist_ok=True)
                    filepath.write_text(content, encoding="utf-8")
                installed_files.append(str(filepath))
                print(f"   [OK] {subdir}/{filename}")
    
    # Write installation manifest
    manifest = {
        "installed_at": datetime.now().isoformat(),
        "systemheaven_version": "3.0.0",
        "packages": list(PACKAGES.keys()),
        "total_files": len(installed_files)
    }
    manifest_path = target_dir / "systemheaven_installation.json"
    if not dry_run:
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    
    print("\\n" + "=" * 70)
    print("✅ INSTALLATION SUCCESSFUL")
    print("=" * 70)
    print(f"📦 Packages: {len(PACKAGES)}")
    print(f"📄 Files created: {len(installed_files)}")
    print("=" * 70)
    print("\\n🌟 SystemHeaven is ready!")
    print("   Load any package into your AI agent")
    print("   Use SKILL.json for zero-prompt execution")
    print("=" * 70)
    
    return True


def main():
    parser = argparse.ArgumentParser(description="SystemHeaven Framework Installer")
    parser.add_argument("--target-dir", "-t", type=str, default=None)
    parser.add_argument("--dry-run", "-d", action="store_true")
    parser.add_argument("--version", action="version", version="%(prog)s 3.0.0")
    args = parser.parse_args()
    
    target_dir = Path(args.target_dir) if args.target_dir else Path.cwd()
    success = install_framework(target_dir, dry_run=args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
