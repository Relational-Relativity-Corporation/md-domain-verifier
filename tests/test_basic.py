import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from verifier.parser import load_domain
from verifier.scanner import scan_codebase
from verifier.checks import run_checks

EXAMPLE_PATH = os.path.join(os.path.dirname(__file__), "..", "examples", "thermal_solver")

def test_undeclared_relation_detected():
    """convection appears in the implementation but is not in domain.yaml — must be an error."""
    domain  = load_domain(EXAMPLE_PATH)
    symbols = scan_codebase(EXAMPLE_PATH)
    results = run_checks(domain, symbols)
    errors  = results["errors"]
    assert any("convection" in e for e in errors), (
        f"Expected 'convection' to be flagged as undeclared. Errors: {errors}"
    )

def test_missing_declared_relation_detected():
    """diffusion is declared in domain.yaml but absent from the implementation — must be an error."""
    domain  = load_domain(EXAMPLE_PATH)
    symbols = scan_codebase(EXAMPLE_PATH)
    results = run_checks(domain, symbols)
    errors  = results["errors"]
    assert any("diffusion" in e for e in errors), (
        f"Expected 'diffusion' to be flagged as missing. Errors: {errors}"
    )

def test_no_false_positives_on_declared_inputs():
    """
    Declared inputs that are absent from the implementation should appear
    in info — not in errors.
    """
    domain  = load_domain(EXAMPLE_PATH)
    symbols = scan_codebase(EXAMPLE_PATH)
    results = run_checks(domain, symbols)
    errors  = " ".join(results["errors"])
    assert "boundary_conditions" not in errors, (
        "boundary_conditions is a declared input — should not appear as an error."
    )

def test_error_count():
    """Thermal solver example must produce exactly 2 errors."""
    domain  = load_domain(EXAMPLE_PATH)
    symbols = scan_codebase(EXAMPLE_PATH)
    results = run_checks(domain, symbols)
    assert len(results["errors"]) == 2, (
        f"Expected exactly 2 errors, got {len(results['errors'])}: {results['errors']}"
    )