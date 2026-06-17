#!/usr/bin/env python3
"""
IIOS Framework Build & Synchronization Script
==============================================

This script centralizes template management across all three .skill packages:
- cornerstone-methodology(6)
- strategic-architect-methodology(1)
- deepdrive-iios-ultimate-gigant-v3(2)

It eliminates code redundancy by synchronizing master templates from the
Cornerstone package to dependent packages automatically.

Usage:
    python build_framework.py [command] [options]

Commands:
    sync        Synchronize templates from master to dependent packages
    validate    Validate all templates against schema requirements
    build       Full build process (sync + validate + generate docs)
    dashboard   Generate HTML dashboard integration files

Author: IIOS Framework Team
Version: 1.0.0
"""

import os
import sys
import shutil
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class IIOSFrameworkBuilder:
    """Centralized build and synchronization manager for IIOS Framework packages."""

    # Package configuration
    MASTER_PACKAGE = "cornerstone-methodology(6)"
    DEPENDENT_PACKAGES = [
        "strategic-architect-methodology(1)",
        "deepdrive-iios-ultimate-gigant-v3(2)"
    ]

    # Core templates to synchronize
    CORE_TEMPLATES = [
        "constitution_template.md",
        "technical_specification_template.md",
        "visual_design_standard_template.md",
        "governance_standard_template.md",
        "certification_framework_template.md",
        "igos_scorecard_template.md"
    ]

    # Core references to synchronize
    CORE_REFERENCES = [
        "methodology_guide.md",
        "workflows.md",
        "case_study.md",
        "iios_constitution.md",
        "glossary.md",
        "role_model.md",
        "certification_levels.md",
        "reference_architecture.md",
        "workflows_enhanced.md",
        "llm_instruction_guide.md",
        "10_reference_cases.md"
    ]

    def __init__(self, base_path: Optional[str] = None):
        """Initialize the builder with base path."""
        self.base_path = Path(base_path) if base_path else Path(__file__).parent.parent
        self.sync_log: List[Dict] = []
        self.validation_results: List[Dict] = []

    def _get_package_path(self, package_name: str) -> Path:
        """Get the full path to a package directory."""
        return self.base_path / package_name

    def _get_template_path(self, package_name: str, template_name: str) -> Path:
        """Get the full path to a template file."""
        return self._get_package_path(package_name) / "templates" / template_name

    def _get_reference_path(self, package_name: str, reference_name: str) -> Path:
        """Get the full path to a reference file."""
        return self._get_package_path(package_name) / "references" / reference_name

    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of a file for comparison."""
        if not file_path.exists():
            return ""
        with open(file_path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()

    def sync_templates(self, dry_run: bool = False) -> Dict:
        """
        Synchronize templates from master package to all dependent packages.

        Args:
            dry_run: If True, only report what would be changed without making changes

        Returns:
            Dictionary with synchronization statistics
        """
        stats = {
            "templates_synced": 0,
            "templates_unchanged": 0,
            "templates_created": 0,
            "errors": []
        }

        print(f"{'[DRY RUN] ' if dry_run else ''}Synchronizing templates...")
        print(f"Master: {self.MASTER_PACKAGE}")
        print(f"Targets: {', '.join(self.DEPENDENT_PACKAGES)}")
        print("-" * 60)

        for template in self.CORE_TEMPLATES:
            master_path = self._get_template_path(self.MASTER_PACKAGE, template)

            if not master_path.exists():
                stats["errors"].append(f"Master template not found: {template}")
                continue

            master_hash = self._calculate_file_hash(master_path)

            for package in self.DEPENDENT_PACKAGES:
                target_path = self._get_template_path(package, template)
                target_hash = self._calculate_file_hash(target_path)

                if target_hash == master_hash:
                    stats["templates_unchanged"] += 1
                    print(f"  ✓ {template} → {package} (unchanged)")
                else:
                    if target_path.exists():
                        stats["templates_synced"] += 1
                        action = "updated"
                    else:
                        stats["templates_created"] += 1
                        action = "created"

                    print(f"  → {template} → {package} ({action})")

                    if not dry_run:
                        try:
                            shutil.copy2(master_path, target_path)
                            self.sync_log.append({
                                "timestamp": datetime.now().isoformat(),
                                "template": template,
                                "target": package,
                                "action": action,
                                "master_hash": master_hash
                            })
                        except Exception as e:
                            stats["errors"].append(f"Failed to copy {template} to {package}: {str(e)}")

        return stats

    def sync_references(self, dry_run: bool = False) -> Dict:
        """
        Synchronize reference documents from master to dependent packages.

        Args:
            dry_run: If True, only report what would be changed

        Returns:
            Dictionary with synchronization statistics
        """
        stats = {
            "references_synced": 0,
            "references_unchanged": 0,
            "references_created": 0,
            "errors": []
        }

        print(f"\n{'[DRY RUN] ' if dry_run else ''}Synchronizing references...")
        print("-" * 60)

        for reference in self.CORE_REFERENCES:
            master_path = self._get_reference_path(self.MASTER_PACKAGE, reference)

            if not master_path.exists():
                stats["errors"].append(f"Master reference not found: {reference}")
                continue

            master_hash = self._calculate_file_hash(master_path)

            for package in self.DEPENDENT_PACKAGES:
                target_path = self._get_reference_path(package, reference)
                target_hash = self._calculate_file_hash(target_path)

                if target_hash == master_hash:
                    stats["references_unchanged"] += 1
                    print(f"  ✓ {reference} → {package} (unchanged)")
                else:
                    if target_path.exists():
                        stats["references_synced"] += 1
                        action = "updated"
                    else:
                        stats["references_created"] += 1
                        action = "created"

                    print(f"  → {reference} → {package} ({action})")

                    if not dry_run:
                        try:
                            # Ensure references directory exists
                            target_path.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(master_path, target_path)
                        except Exception as e:
                            stats["errors"].append(f"Failed to copy {reference} to {package}: {str(e)}")

        return stats

    def validate_templates(self) -> Dict:
        """
        Validate all templates for required sections and structure.

        Returns:
            Dictionary with validation results
        """
        results = {
            "valid": 0,
            "invalid": 0,
            "errors": []
        }

        print("\nValidating templates...")
        print("-" * 60)

        required_sections = {
            "constitution_template.md": ["Präambel", "Artikel I", "Pflichtfeld"],
            "technical_specification_template.md": ["Architecture", "Score", "Pflichtfeld"],
            "governance_standard_template.md": ["Governance", "Rollen", "Pflichtfeld"],
            "certification_framework_template.md": ["Zertifizierungsprinzipien", "IGOS", "Pflichtfeld"],
            "igos_scorecard_template.md": ["Cornerstone Score", "Integrity Score", "Gesamtscore"],
            "visual_design_standard_template.md": ["Design", "Visual", "Score"]
        }

        for template in self.CORE_TEMPLATES:
            master_path = self._get_template_path(self.MASTER_PACKAGE, template)

            if not master_path.exists():
                results["errors"].append(f"Template not found: {template}")
                results["invalid"] += 1
                continue

            content = master_path.read_text(encoding="utf-8")
            required = required_sections.get(template, [])

            missing = [section for section in required if section not in content]

            if missing:
                results["invalid"] += 1
                results["errors"].append(f"{template}: Missing sections {missing}")
                print(f"  ✗ {template} (missing: {', '.join(missing)})")
            else:
                results["valid"] += 1
                print(f"  ✓ {template}")

        return results

    def generate_dashboard_files(self, output_dir: Optional[str] = None) -> Dict:
        """
        Generate HTML dashboard integration files for IGOS Scorecard visualization.

        Args:
            output_dir: Directory to output dashboard files (default: scripts/dashboard/)

        Returns:
            Dictionary with generation statistics
        """
        if output_dir is None:
            output_dir = self.base_path / "scripts" / "dashboard"
        else:
            output_dir = Path(output_dir)

        output_dir.mkdir(parents=True, exist_ok=True)

        stats = {"files_created": 0, "errors": []}

        print("\nGenerating dashboard files...")
        print("-" * 60)

        # Generate IGOS Scorecard Dashboard HTML
        dashboard_html = self._generate_igos_dashboard_html()
        dashboard_path = output_dir / "igos_scorecard_dashboard.html"

        try:
            dashboard_path.write_text(dashboard_html, encoding="utf-8")
            stats["files_created"] += 1
            print(f"  ✓ Created: {dashboard_path.name}")
        except Exception as e:
            stats["errors"].append(f"Failed to create dashboard: {str(e)}")

        # Generate radar chart component
        radar_js = self._generate_radar_chart_js()
        radar_path = output_dir / "radar_chart.js"

        try:
            radar_path.write_text(radar_js, encoding="utf-8")
            stats["files_created"] += 1
            print(f"  ✓ Created: {radar_path.name}")
        except Exception as e:
            stats["errors"].append(f"Failed to create radar chart: {str(e)}")

        # Generate validation bridge module
        bridge_py = self._generate_validation_bridge()
        bridge_path = output_dir / "validation_bridge.py"

        try:
            bridge_path.write_text(bridge_py, encoding="utf-8")
            stats["files_created"] += 1
            print(f"  ✓ Created: {bridge_path.name}")
        except Exception as e:
            stats["errors"].append(f"Failed to create validation bridge: {str(e)}")

        return stats

    def _generate_igos_dashboard_html(self) -> str:
        """Generate the main IGOS Scorecard Dashboard HTML."""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IIOS IGOS Scorecard Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e94560;
            min-height: 100vh;
            padding: 2rem;
        }
        .container { max-width: 1400px; margin: 0 auto; }
        header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: rgba(233, 69, 96, 0.1);
            border-radius: 16px;
            border: 1px solid rgba(233, 69, 96, 0.3);
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(135deg, #e94560 0%, #ff6b6b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .motto {
            font-style: italic;
            color: #a0a0a0;
            font-size: 1.1rem;
        }
        .scores-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin-bottom: 3rem;
        }
        .score-card {
            background: rgba(255,255,255,0.05);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid rgba(233, 69, 96, 0.2);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .score-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(233, 69, 96, 0.3);
        }
        .score-card.critical { border-color: #e94560; }
        .score-card.warning { border-color: #ffd93d; }
        .score-card.good { border-color: #6bcb77; }
        .score-label {
            font-size: 0.9rem;
            color: #a0a0a0;
            margin-bottom: 0.5rem;
        }
        .score-value {
            font-size: 3rem;
            font-weight: bold;
            color: #fff;
        }
        .chart-container {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(233, 69, 96, 0.2);
        }
        .section-title {
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            color: #e94560;
        }
        #radarChart { max-height: 400px; }
        .status-indicator {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .status-pass { background: #6bcb77; }
        .status-fail { background: #e94560; }
        .status-warn { background: #ffd93d; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>IIOS IGOS Scorecard Dashboard</h1>
            <p class="motto">"Barmherzigkeit ist der Eckstein; Wahrheit ihr Maßstab, Recht ihre Ordnung und Entwicklung ihre Frucht."</p>
        </header>

        <div class="scores-grid">
            <div class="score-card" id="cornerstone-card">
                <div class="score-label">Cornerstone Score</div>
                <div class="score-value" id="cornerstone-score">--</div>
            </div>
            <div class="score-card" id="integrity-card">
                <div class="score-label">Integrity Score</div>
                <div class="score-value" id="integrity-score">--</div>
            </div>
            <div class="score-card" id="compliance-card">
                <div class="score-label">Compliance Score</div>
                <div class="score-value" id="compliance-score">--</div>
            </div>
            <div class="score-card" id="risk-card">
                <div class="score-label">Risk Score</div>
                <div class="score-value" id="risk-score">--</div>
            </div>
            <div class="score-card" id="governance-card">
                <div class="score-label">Governance Score</div>
                <div class="score-value" id="governance-score">--</div>
            </div>
            <div class="score-card" id="development-card">
                <div class="score-label">Development Score</div>
                <div class="score-value" id="development-score">--</div>
            </div>
        </div>

        <div class="chart-container">
            <h2 class="section-title">Score Radar Analysis</h2>
            <canvas id="radarChart"></canvas>
        </div>

        <div class="chart-container">
            <h2 class="section-title">Certification Status</h2>
            <div id="certification-status">
                <p><span class="status-indicator status-warn"></span>Pending Assessment</p>
            </div>
        </div>
    </div>

    <script src="radar_chart.js"></script>
    <script>
        // Demo data - in production, this would be loaded from the IIOS framework
        const igosData = {
            cornerstone: 85,
            integrity: 92,
            compliance: 78,
            risk: 88,
            governance: 81,
            development: 75
        };

        // Update score displays
        function updateScores(data) {
            document.getElementById('cornerstone-score').textContent = data.cornerstone + '%';
            document.getElementById('integrity-score').textContent = data.integrity + '%';
            document.getElementById('compliance-score').textContent = data.compliance + '%';
            document.getElementById('risk-score').textContent = data.risk + '%';
            document.getElementById('governance-score').textContent = data.governance + '%';
            document.getElementById('development-score').textContent = data.development + '%';

            // Color coding
            Object.keys(data).forEach(key => {
                const card = document.getElementById(key + '-card');
                const score = data[key];
                card.classList.remove('critical', 'warning', 'good');
                if (score < 70) card.classList.add('critical');
                else if (score < 85) card.classList.add('warning');
                else card.classList.add('good');
            });
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            updateScores(igosData);
            initRadarChart(igosData);
        });
    </script>
</body>
</html>'''

    def _generate_radar_chart_js(self) -> str:
        """Generate the radar chart JavaScript component."""
        return '''/**
 * IIOS IGOS Scorecard Radar Chart Component
 * 
 * Visualizes the six core IIOS scores in an interactive radar chart.
 * Integrates with the IGOS Scorecard Template for real-time visualization.
 */

function initRadarChart(data) {
    const ctx = document.getElementById('radarChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: [
                'Cornerstone\\n(20%)',
                'Integrity\\n(20%)',
                'Compliance\\n(20%)',
                'Risk\\n(15%)',
                'Governance\\n(15%)',
                'Development\\n(10%)'
            ],
            datasets: [{
                label: 'Current Scores',
                data: [
                    data.cornerstone,
                    data.integrity,
                    data.compliance,
                    data.risk,
                    data.governance,
                    data.development
                ],
                backgroundColor: 'rgba(233, 69, 96, 0.2)',
                borderColor: '#e94560',
                borderWidth: 2,
                pointBackgroundColor: '#e94560',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: '#e94560'
            }, {
                label: 'Target (Platinum)',
                data: [95, 95, 95, 95, 95, 95],
                backgroundColor: 'rgba(107, 203, 119, 0.1)',
                borderColor: '#6bcb77',
                borderWidth: 2,
                borderDash: [5, 5],
                pointBackgroundColor: '#6bcb77',
                pointBorderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    min: 0,
                    ticks: {
                        stepSize: 20,
                        color: '#a0a0a0'
                    },
                    grid: {
                        color: 'rgba(233, 69, 96, 0.1)'
                    },
                    angleLines: {
                        color: 'rgba(233, 69, 96, 0.1)'
                    },
                    pointLabels: {
                        color: '#e94560',
                        font: {
                            size: 12,
                            weight: 'bold'
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#a0a0a0'
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(26, 26, 46, 0.9)',
                    titleColor: '#e94560',
                    bodyColor: '#fff',
                    borderColor: '#e94560',
                    borderWidth: 1
                }
            }
        }
    });
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { initRadarChart };
}'''

    def _generate_validation_bridge(self) -> str:
        """Generate the Python validation bridge for markdown-driven validation."""
        return '''#!/usr/bin/env python3
"""
IIOS Validation Bridge
=======================

Connects HTML dashboards with the IIOS Framework validation engine.
Parses Markdown documents to extract validation rules dynamically.

Usage:
    from validation_bridge import IIOSValidationBridge
    bridge = IIOSValidationBridge()
    results = bridge.validate_system("/path/to/system")
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class ValidationRule:
    """Represents a validation rule extracted from framework documents."""
    source: str
    category: str
    criterion: str
    weight: float
    description: str


@dataclass
class ScoreResult:
    """Represents a score calculation result."""
    score_type: str
    value: float
    max_value: float
    details: Dict


class IIOSValidationBridge:
    """Bridge between IIOS Framework documents and validation engine."""

    def __init__(self, framework_path: Optional[str] = None):
        """Initialize with path to IIOS framework."""
        self.framework_path = Path(framework_path) if framework_path else Path(__file__).parent.parent.parent
        self.rules: List[ValidationRule] = []
        self.scores: Dict[str, ScoreResult] = {}

    def parse_igos_scorecard_template(self) -> List[ValidationRule]:
        """Parse the IGOS Scorecard template to extract validation rules."""
        template_path = self.framework_path / "cornerstone-methodology(6)" / "templates" / "igos_scorecard_template.md"
        
        if not template_path.exists():
            raise FileNotFoundError(f"IGOS Scorecard template not found: {template_path}")

        content = template_path.read_text(encoding="utf-8")
        rules = []

        # Extract score sections with regex
        score_patterns = [
            ("Cornerstone Score", r"Cornerstone Score.*?Gewichtung:\s*(\d+)%", 0.20),
            ("Integrity Score", r"Integrity Score.*?Gewichtung:\s*(\d+)%", 0.20),
            ("Compliance Score", r"Compliance Score.*?Gewichtung:\s*(\d+)%", 0.20),
            ("Risk Score", r"Risk Score.*?Gewichtung:\s*(\d+)%", 0.15),
            ("Governance Score", r"Governance Score.*?Gewichtung:\s*(\d+)%", 0.15),
            ("Development Score", r"Development Score.*?Gewichtung:\s*(\d+)%", 0.10)
        ]

        for score_name, pattern, default_weight in score_patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            weight = float(match.group(1)) / 100 if match else default_weight
            
            rules.append(ValidationRule(
                source="igos_scorecard_template.md",
                category=score_name,
                criterion=f"{score_name} validation",
                weight=weight,
                description=f"Validates system compliance with {score_name} criteria"
            ))

        self.rules = rules
        return rules

    def calculate_igos_score(self, assessments: Dict[str, float]) -> Dict:
        """
        Calculate IGOS overall score from individual assessments.

        Args:
            assessments: Dict mapping score types to values (0-100)

        Returns:
            Dict with individual scores, overall score, and certification level
        """
        weights = {
            "cornerstone": 0.20,
            "integrity": 0.20,
            "compliance": 0.20,
            "risk": 0.15,
            "governance": 0.15,
            "development": 0.10
        }

        overall = sum(assessments.get(k, 0) * w for k, w in weights.items())

        # Determine certification level
        if overall >= 95:
            level = "Platinum"
        elif overall >= 90:
            level = "Gold"
        elif overall >= 80:
            level = "Silver"
        elif overall >= 70:
            level = "Bronze"
        else:
            level = "Not Certified"

        return {
            "individual_scores": assessments,
            "overall_score": round(overall, 2),
            "certification_level": level,
            "max_possible": 100
        }

    def export_for_dashboard(self, results: Dict) -> str:
        """Export validation results as JSON for dashboard consumption."""
        return json.dumps(results, indent=2)


if __name__ == "__main__":
    # Example usage
    bridge = IIOSValidationBridge()
    rules = bridge.parse_igos_scorecard_template()
    print(f"Loaded {len(rules)} validation rules from IGOS Scorecard")
    
    # Demo calculation
    demo_assessments = {
        "cornerstone": 85,
        "integrity": 92,
        "compliance": 78,
        "risk": 88,
        "governance": 81,
        "development": 75
    }
    
    results = bridge.calculate_igos_score(demo_assessments)
    print("\\nDemo Results:")
    print(bridge.export_for_dashboard(results))
'''

    def save_sync_log(self) -> None:
        """Save synchronization log to file."""
        log_path = self.base_path / "scripts" / "sync_log.json"
        
        log_data = {
            "last_sync": datetime.now().isoformat(),
            "operations": self.sync_log
        }
        
        # Load existing log if present
        if log_path.exists():
            try:
                existing = json.loads(log_path.read_text(encoding="utf-8"))
                log_data["operations"] = existing.get("operations", []) + self.sync_log
            except:
                pass

        log_path.write_text(json.dumps(log_data, indent=2), encoding="utf-8")
        print(f"\nSync log saved to: {log_path}")


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="IIOS Framework Build & Synchronization Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python build_framework.py sync              # Sync templates to all packages
    python build_framework.py sync --dry-run    # Preview changes only
    python build_framework.py validate          # Validate all templates
    python build_framework.py build           # Full build process
    python build_framework.py dashboard       # Generate dashboard files
        """
    )
    
    parser.add_argument(
        "command",
        choices=["sync", "validate", "build", "dashboard"],
        help="Command to execute"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without making them (for sync command)"
    )
    parser.add_argument(
        "--base-path",
        type=str,
        default=None,
        help="Base path to framework directory (default: parent of script)"
    )

    args = parser.parse_args()

    builder = IIOSFrameworkBuilder(base_path=args.base_path)

    if args.command == "sync":
        template_stats = builder.sync_templates(dry_run=args.dry_run)
        ref_stats = builder.sync_references(dry_run=args.dry_run)
        
        print("\n" + "=" * 60)
        print("SYNCHRONIZATION SUMMARY")
        print("=" * 60)
        print(f"Templates: {template_stats['templates_synced']} synced, "
              f"{template_stats['templates_unchanged']} unchanged, "
              f"{template_stats['templates_created']} created")
        print(f"References: {ref_stats['references_synced']} synced, "
              f"{ref_stats['references_unchanged']} unchanged, "
              f"{ref_stats['references_created']} created")
        
        if template_stats["errors"] or ref_stats["errors"]:
            print("\nERRORS:")
            for error in template_stats["errors"] + ref_stats["errors"]:
                print(f"  ! {error}")
        
        if not args.dry_run:
            builder.save_sync_log()

    elif args.command == "validate":
        results = builder.validate_templates()
        
        print("\n" + "=" * 60)
        print("VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Valid: {results['valid']}")
        print(f"Invalid: {results['invalid']}")
        
        if results["errors"]:
            print("\nERRORS:")
            for error in results["errors"]:
                print(f"  ! {error}")
        
        sys.exit(0 if results["invalid"] == 0 else 1)

    elif args.command == "build":
        print("Running full build process...\n")
        
        # Sync
        template_stats = builder.sync_templates(dry_run=False)
        ref_stats = builder.sync_references(dry_run=False)
        
        # Validate
        validation_results = builder.validate_templates()
        
        # Generate dashboards
        dashboard_stats = builder.generate_dashboard_files()
        
        print("\n" + "=" * 60)
        print("BUILD SUMMARY")
        print("=" * 60)
        print(f"Templates synced: {template_stats['templates_synced']}")
        print(f"References synced: {ref_stats['references_synced']}")
        print(f"Templates validated: {validation_results['valid']}")
        print(f"Dashboard files created: {dashboard_stats['files_created']}")
        
        builder.save_sync_log()
        
        all_errors = (
            template_stats["errors"] + 
            ref_stats["errors"] + 
            validation_results["errors"] +
            dashboard_stats["errors"]
        )
        
        if all_errors:
            print(f"\nErrors encountered: {len(all_errors)}")
            sys.exit(1)
        else:
            print("\n✓ Build completed successfully!")

    elif args.command == "dashboard":
        stats = builder.generate_dashboard_files()
        
        print("\n" + "=" * 60)
        print("DASHBOARD GENERATION SUMMARY")
        print("=" * 60)
        print(f"Files created: {stats['files_created']}")
        
        if stats["errors"]:
            print("\nERRORS:")
            for error in stats["errors"]:
                print(f"  ! {error}")
            sys.exit(1)
        else:
            print("\n✓ Dashboard files generated successfully!")


if __name__ == "__main__":
    main()
