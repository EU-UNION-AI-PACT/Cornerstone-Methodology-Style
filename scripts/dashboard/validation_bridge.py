#!/usr/bin/env python3
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
    print("\nDemo Results:")
    print(bridge.export_for_dashboard(results))
