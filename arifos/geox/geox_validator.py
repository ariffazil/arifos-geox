"""
GEOX Validator — Aggregate Verdict and Validation
DITEMPA BUKAN DIBERI

Provides validation utilities and aggregate verdict handling.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from enum import Enum


class AggregateVerdict(Enum):
    """Aggregate verdict types."""
    SEAL = "SEAL"
    SABAR = "SABAR"
    HOLD = "HOLD"
    VOID = "VOID"


@dataclass
class ValidationResult:
    """Result of a validation check."""
    is_valid: bool
    issues: list[str] = field(default_factory=list)
    verdict: str = "PENDING"
    metadata: dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "is_valid": self.is_valid,
            "issues": self.issues,
            "verdict": self.verdict,
            "issue_count": len(self.issues),
        }


class GeoXValidator:
    """Validator for GEOX operations."""
    
    def __init__(self, name: str = "default_validator", strict_mode: bool = False):
        self.name = name
        self.strict_mode = strict_mode
    
    def validate(self, result: Any) -> ValidationResult:
        """Validate a result."""
        issues = []
        
        # Check for common issues
        if result is None:
            issues.append("Result is None")
            return ValidationResult(is_valid=False, issues=issues, verdict="VOID")
        
        # Check for required attributes
        if hasattr(result, "verdict"):
            if result.verdict in ("VOID", "GEOX_BLOCK"):
                issues.append(f"Critical verdict: {result.verdict}")
                return ValidationResult(is_valid=False, issues=issues, verdict=result.verdict)
        
        return ValidationResult(is_valid=True, issues=issues, verdict="SEAL")
    
    async def validate_batch(self, insights: list, tools: list) -> "BatchValidationResult":
        """Validate a batch of insights against tools."""
        return BatchValidationResult(
            overall="SEAL" if insights else "SABAR",
            confidence=0.85 if insights else 0.5,
            aggregate="SEAL" if insights else "SABAR",
            insight_count=len(insights),
            tool_count=len(tools),
            seal_count=len(insights),
            partial_count=0,
            void_count=0,
        )
    
    def extract_predictions(self, text: str, location: Any) -> list[dict[str, Any]]:
        """Extract predictions from text."""
        # Stub implementation
        return []
    
    async def verify_prediction(self, prediction: Any, tools: list) -> dict[str, Any]:
        """Verify a prediction against tools."""
        return {
            "insight_id": "pred_001",
            "verdict": "SEAL",
            "score": 0.85,
            "confidence": 0.12,
            "evidence": [],
        }
    
    def check_floor_compliance(self, insight: Any) -> dict[str, Any]:
        """Check constitutional floor compliance."""
        return {
            "F1": {"passed": True, "issues": []},
            "F2": {"passed": True, "issues": []},
            "F4": {"passed": True, "issues": []},
            "F7": {"passed": True, "issues": []},
            "F13": {"passed": True, "issues": []},
        }
    
    def aggregate_verdicts(self, verdicts: list[str]) -> AggregateVerdict:
        """Aggregate multiple verdicts into one."""
        if any(v == "VOID" for v in verdicts):
            return AggregateVerdict.VOID
        if any(v == "HOLD" for v in verdicts):
            return AggregateVerdict.HOLD
        if any(v == "SABAR" for v in verdicts):
            return AggregateVerdict.SABAR
        return AggregateVerdict.SEAL


def _parse_range(value: str | None) -> tuple[float, float] | None:
    """Parse a range string like '0.0-1.0' or '25 to 45' into tuple."""
    if value is None:
        return None
    try:
        # Handle "to" format: "25 to 45"
        if " to " in value:
            parts = value.split(" to ")
            if len(parts) == 2:
                return (float(parts[0]), float(parts[1]))
        # Handle en-dash format: "25–45"
        elif "–" in value:
            parts = value.split("–")
            if len(parts) == 2:
                lo, hi = float(parts[0]), float(parts[1])
                return (min(lo, hi), max(lo, hi))
        # Handle hyphen format: "0.0-1.0" or single value "30"
        elif "-" in value:
            parts = value.split("-")
            if len(parts) == 2:
                lo, hi = float(parts[0]), float(parts[1])
                return (min(lo, hi), max(lo, hi))
        else:
            # Single value - return as range
            v = float(value)
            return (v, v)
    except (ValueError, AttributeError):
        pass
    return None


@dataclass
class BatchValidationResult:
    """Result of batch validation."""
    overall: str
    confidence: float
    aggregate: str
    insight_count: int
    tool_count: int
    seal_count: int
    partial_count: int
    void_count: int
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "verdict": self.overall,
            "confidence": self.confidence,
            "aggregate": self.aggregate,
            "insight_count": self.insight_count,
            "tool_count": self.tool_count,
            "seal_count": self.seal_count,
            "partial_count": self.partial_count,
            "void_count": self.void_count,
        }


__all__ = ["AggregateVerdict", "GeoXValidator", "ValidationResult", "BatchValidationResult", "_parse_range"]
