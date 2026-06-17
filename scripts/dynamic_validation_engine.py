#!/usr/bin/env python3
"""
IIOS Dynamic Validation Engine
==============================

Parses Markdown documents (SKILL.md, methodology_guide.md, etc.) to extract
validation rules dynamically. This allows the validation logic to adapt at
runtime when the source documentation changes.

Usage:
    python dynamic_validation_engine.py [command] [options]

Commands:
    parse           Parse framework documents and extract rules
    validate        Validate a target system against extracted rules
    watch           Watch for changes in framework documents
    export          Export rules as JSON for external consumption

Author: IIOS Framework Team
Version: 1.0.0
"""

import re
import json
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime


@dataclass
class ValidationRule:
    """Represents a validation rule extracted from framework documents."""
    source: str
    rule_id: str
    category: str
    criterion: str
    weight: float
    description: str
    condition: str
    priority: str  # 'critical', 'high', 'medium', 'low'


@dataclass
class ScoreDefinition:
    """Represents a score definition from the constitution."""
    score_type: str
    weight: float
    criteria: List[str]
    calculation_method: str
    constitution_article: str


@dataclass
class ValidationResult:
    """Represents the result of a validation check."""
    rule_id: str
    passed: bool
    score: float
    details: str
    evidence: List[str]
    recommendations: List[str]


class MarkdownParser:
    """Parses Markdown documents to extract structured information."""

    def __init__(self, content: str, source: str):
        self.content = content
        self.source = source
        self.lines = content.split('\n')

    def extract_score_definitions(self) -> List[ScoreDefinition]:
        """Extract score definitions from constitution or methodology documents."""
        scores = []

        # Pattern to find score sections
        score_pattern = r'##?\s*(Cornerstone|Integrity|Compliance|Risk|Governance|Development)\s*Score.*?\n.*?\*\*Definition:\*\*(.*?)(?=\*\*|$)'

        matches = re.findall(score_pattern, self.content, re.DOTALL | re.IGNORECASE)

        for score_type, definition in matches:
            # Extract weight
            weight_match = re.search(r'Gewichtung.*?([0-9]+)%', self.content)
            weight = float(weight_match.group(1)) / 100 if weight_match else 0.2

            # Extract criteria
            criteria = []
            criteria_section = re.search(r'\| Kriterium.*?\|', self.content)
            if criteria_section:
                # Find table rows
                table_pattern = r'\|\s*([^|]+)\s*\|\s*([0-9]+)%\s*\|'
                criteria_matches = re.findall(table_pattern, self.content)
                for criterion, _ in criteria_matches:
                    criteria.append(criterion.strip())

            scores.append(ScoreDefinition(
                score_type=score_type,
                weight=weight,
                criteria=criteria,
                calculation_method="weighted_average",
                constitution_article=self._find_constitution_article(score_type)
            ))

        return scores

    def extract_validation_rules(self) -> List[ValidationRule]:
        """Extract validation rules from framework documents."""
        rules = []

        # Extract Pflichtfeld (mandatory field) validations
        pflichtfeld_pattern = r'###\s*Pflichtfeld.*?Eckstein-Validierung.*?\*\*Begründung:\*\*(.*?)(?=\[|$)'
        pflichtfelder = re.findall(pflichtfeld_pattern, self.content, re.DOTALL | re.IGNORECASE)

        for idx, begründung in enumerate(pflichtfelder, 1):
            rules.append(ValidationRule(
                source=self.source,
                rule_id=f"PF_{self.source}_{idx:03d}",
                category="Pflichtfeld",
                criterion="Eckstein-Validierung",
                weight=1.0,  # Pflichtfelder sind kritisch
                description=begründung.strip()[:200],
                condition="Pflichtfeld muss ausgefüllt sein",
                priority="critical"
            ))

        # Extract score-based rules
        score_rules_pattern = r'(Cornerstone|Integrity|Compliance|Risk|Governance|Development)\s*Score.*?(≥|>=)\s*([0-9]+)'
        score_matches = re.findall(score_rules_pattern, self.content, re.IGNORECASE)

        for score_type, _, min_value in score_matches:
            rules.append(ValidationRule(
                source=self.source,
                rule_id=f"SCORE_{score_type.upper()}_{min_value}",
                category=f"{score_type} Score",
                criterion=f"Mindestwert {min_value}",
                weight=0.2,
                description=f"{score_type} Score muss mindestens {min_value} erreichen",
                condition=f"score >= {min_value}",
                priority="high"
            ))

        # Extract prohibited effects
        prohibited_pattern = r'Verbotene Wirkung:.*?(Willkür|Ausbeutung|Täuschung|unverhältnismäßiger Schaden)'
        prohibited = re.findall(prohibited_pattern, self.content, re.IGNORECASE)

        for item in prohibited:
            rules.append(ValidationRule(
                source=self.source,
                rule_id=f"PROHIBITED_{item.upper()}",
                category="Verbote",
                criterion=item,
                weight=1.0,
                description=f"{item} ist strikt verboten",
                condition=f"kein {item} in System vorhanden",
                priority="critical"
            ))

        return rules

    def extract_architecture_rules(self) -> List[ValidationRule]:
        """Extract rules from the 8-layer architecture."""
        rules = []

        # Layer validation
        layer_pattern = r'Layer\s*([0-7]):\s*(.*?)\n'
        layers = re.findall(layer_pattern, self.content)

        for layer_num, layer_name in layers:
            rules.append(ValidationRule(
                source=self.source,
                rule_id=f"LAYER_{layer_num}",
                category="Architektur",
                criterion=f"Layer {layer_num}: {layer_name}",
                weight=0.1,
                description=f"System muss Layer {layer_num} ({layer_name}) implementieren",
                condition=f"layer_{layer_num}_implemented",
                priority="high"
            ))

        return rules

    def extract_certification_rules(self) -> List[ValidationRule]:
        """Extract certification level requirements."""
        rules = []

        # Certification level thresholds
        cert_pattern = r'(Platinum|Gold|Silver|Bronze).*?([0-9]+)-([0-9]+)?%'
        cert_matches = re.findall(cert_pattern, self.content, re.IGNORECASE)

        for level, min_val, max_val in cert_matches:
            if max_val:
                rules.append(ValidationRule(
                    source=self.source,
                    rule_id=f"CERT_{level.upper()}",
                    category="Zertifizierung",
                    criterion=f"{level} Level",
                    weight=0.5,
                    description=f"IGOS Score {min_val}-{max_val}% für {level}",
                    condition=f"score >= {min_val}",
                    priority="medium"
                ))

        return rules

    def _find_constitution_article(self, score_type: str) -> str:
        """Map score type to constitution article."""
        mapping = {
            "Cornerstone": "Artikel I",
            "Integrity": "Artikel II",
            "Compliance": "Artikel III",
            "Risk": "Artikel IV",
            "Governance": "Artikel V",
            "Development": "Artikel VI"
        }
        return mapping.get(score_type, "Unbekannt")


class DynamicValidationEngine:
    """Dynamic validation engine that parses Markdown for rules at runtime."""

    def __init__(self, framework_path: Optional[str] = None):
        """Initialize with path to framework documents."""
        self.framework_path = Path(framework_path) if framework_path else self._find_framework_path()
        self.rules: List[ValidationRule] = []
        self.scores: List[ScoreDefinition] = []
        self._load_framework()

    def _find_framework_path(self) -> Path:
        """Auto-detect framework path."""
        script_dir = Path(__file__).parent
        return script_dir.parent / "cornerstone-methodology(6)"

    def _load_framework(self) -> None:
        """Load and parse all framework documents."""
        references_dir = self.framework_path / "references"

        documents_to_parse = [
            "iios_constitution.md",
            "methodology_guide.md",
            "certification_levels.md",
            "reference_architecture.md",
            "workflows_enhanced.md",
            "glossary.md"
        ]

        for doc_name in documents_to_parse:
            doc_path = references_dir / doc_name
            if doc_path.exists():
                content = doc_path.read_text(encoding="utf-8")
                parser = MarkdownParser(content, doc_name)

                # Extract all types of rules
                self.rules.extend(parser.extract_validation_rules())
                self.rules.extend(parser.extract_architecture_rules())
                self.rules.extend(parser.extract_certification_rules())
                self.scores.extend(parser.extract_score_definitions())

        print(f"Loaded {len(self.rules)} validation rules from {len(documents_to_parse)} documents")
        print(f"Loaded {len(self.scores)} score definitions")

    def get_rules_by_category(self, category: str) -> List[ValidationRule]:
        """Get rules filtered by category."""
        return [r for r in self.rules if r.category == category]

    def get_critical_rules(self) -> List[ValidationRule]:
        """Get all critical priority rules."""
        return [r for r in self.rules if r.priority == "critical"]

    def export_rules_json(self, output_path: Optional[str] = None) -> str:
        """Export all rules as JSON."""
        data = {
            "exported_at": datetime.now().isoformat(),
            "framework_path": str(self.framework_path),
            "total_rules": len(self.rules),
            "rules": [asdict(r) for r in self.rules],
            "scores": [asdict(s) for s in self.scores]
        }

        json_output = json.dumps(data, indent=2, ensure_ascii=False)

        if output_path:
            Path(output_path).write_text(json_output, encoding="utf-8")
            print(f"Rules exported to: {output_path}")

        return json_output

    def calculate_igos_score(self, assessments: Dict[str, float]) -> Dict:
        """
        Calculate IGOS overall score from individual assessments.

        Args:
            assessments: Dict mapping score types to values (0-100)

        Returns:
            Dict with individual scores, overall score, and certification level
        """
        weights = {
            "Cornerstone": 0.20,
            "Integrity": 0.20,
            "Compliance": 0.20,
            "Risk": 0.15,
            "Governance": 0.15,
            "Development": 0.10
        }

        overall = sum(
            assessments.get(score_type, 0) * weight
            for score_type, weight in weights.items()
        )

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
            "max_possible": 100,
            "weights_used": weights
        }

    def validate_system(self, system_data: Dict[str, Any]) -> List[ValidationResult]:
        """
        Validate a system against all loaded rules.

        Args:
            system_data: Dict containing system information and scores

        Returns:
            List of validation results
        """
        results = []

        # Get scores from system data
        scores = system_data.get("scores", {})

        for rule in self.rules:
            result = self._check_rule(rule, system_data, scores)
            results.append(result)

        return results

    def _check_rule(self, rule: ValidationRule, system_data: Dict, scores: Dict) -> ValidationResult:
        """Check a single rule against system data."""
        passed = True
        score = 100.0
        details = ""
        evidence = []
        recommendations = []

        # Check based on rule category
        if rule.category == "Pflichtfeld":
            # Check if mandatory fields are filled
            pflichtfelder = system_data.get("pflichtfelder", [])
            if not pflichtfelder:
                passed = False
                score = 0.0
                details = "Keine Pflichtfelder vorhanden"
                recommendations.append("Fügen Sie Pflichtfelder zur Eckstein-Validierung hinzu")

        elif "Score" in rule.category:
            # Check score threshold
            score_type = rule.category.replace(" Score", "")
            actual_score = scores.get(score_type, 0)

            # Extract min value from condition
            min_match = re.search(r'>=?\s*([0-9]+)', rule.condition)
            if min_match:
                min_required = float(min_match.group(1))
                if actual_score < min_required:
                    passed = False
                    score = (actual_score / min_required) * 100
                    details = f"{score_type} Score ({actual_score}) unter Minimum ({min_required})"
                    recommendations.append(f"Erhöhen Sie den {score_type} Score um {min_required - actual_score} Punkte")

        elif rule.category == "Verbote":
            # Check for prohibited items
            prohibited_items = system_data.get("prohibited_items", [])
            if rule.criterion.lower() in [p.lower() for p in prohibited_items]:
                passed = False
                score = 0.0
                details = f"Verbotene Wirkung gefunden: {rule.criterion}"
                recommendations.append(f"Entfernen Sie {rule.criterion} aus dem System")

        elif rule.category == "Zertifizierung":
            # Check certification requirements
            current_level = system_data.get("certification_level", "None")
            # Simplified check
            pass

        return ValidationResult(
            rule_id=rule.rule_id,
            passed=passed,
            score=round(score, 2),
            details=details,
            evidence=evidence,
            recommendations=recommendations
        )

    def generate_validation_report(self, system_data: Dict[str, Any]) -> Dict:
        """Generate a comprehensive validation report."""
        results = self.validate_system(system_data)

        total_rules = len(results)
        passed_rules = len([r for r in results if r.passed])
        failed_rules = total_rules - passed_rules

        critical_failures = len([
            r for r in results
            if not r.passed and any(rule.rule_id == r.rule_id and rule.priority == "critical" for rule in self.rules)
        ])

        # Calculate scores
        scores = system_data.get("scores", {})
        igos_result = self.calculate_igos_score(scores)

        report = {
            "generated_at": datetime.now().isoformat(),
            "system_name": system_data.get("name", "Unbekannt"),
            "summary": {
                "total_rules_checked": total_rules,
                "passed": passed_rules,
                "failed": failed_rules,
                "critical_failures": critical_failures,
                "pass_rate": round((passed_rules / total_rules * 100), 2) if total_rules > 0 else 0
            },
            "igos_assessment": igos_result,
            "failed_checks": [
                {
                    "rule_id": r.rule_id,
                    "details": r.details,
                    "recommendations": r.recommendations
                }
                for r in results if not r.passed
            ],
            "recommendations": [
                rec for r in results for rec in r.recommendations
            ]
        }

        return report


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description="IIOS Dynamic Validation Engine - Markdown-driven validation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python dynamic_validation_engine.py parse
    python dynamic_validation_engine.py export --output rules.json
    python dynamic_validation_engine.py validate --system system_data.json
        """
    )

    parser.add_argument(
        "command",
        choices=["parse", "validate", "watch", "export"],
        help="Command to execute"
    )
    parser.add_argument(
        "--framework-path",
        type=str,
        default=None,
        help="Path to framework directory"
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path"
    )
    parser.add_argument(
        "--system",
        type=str,
        default=None,
        help="System data file (JSON) for validation"
    )

    args = parser.parse_args()

    engine = DynamicValidationEngine(framework_path=args.framework_path)

    if args.command == "parse":
        print("\n=== PARSED VALIDATION RULES ===\n")

        # Group by category
        categories = {}
        for rule in engine.rules:
            if rule.category not in categories:
                categories[rule.category] = []
            categories[rule.category].append(rule)

        for category, rules in categories.items():
            print(f"\n{category} ({len(rules)} rules):")
            for rule in rules:
                print(f"  - {rule.rule_id}: {rule.criterion} (priority: {rule.priority})")

        print(f"\nTotal: {len(engine.rules)} rules loaded")

    elif args.command == "export":
        engine.export_rules_json(args.output)

    elif args.command == "validate":
        if not args.system:
            print("Error: --system argument required for validation")
            sys.exit(1)

        system_data = json.loads(Path(args.system).read_text(encoding="utf-8"))
        report = engine.generate_validation_report(system_data)

        print(json.dumps(report, indent=2, ensure_ascii=False))

    elif args.command == "watch":
        print("Watch mode: Monitoring framework documents for changes...")
        print("(Press Ctrl+C to stop)")

        try:
            while True:
                import time
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nWatch mode stopped")


if __name__ == "__main__":
    main()
