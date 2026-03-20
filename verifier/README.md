# md-domain-verifier

A CLI tool that verifies whether code operates within explicitly defined domain boundaries.

## Overview

This tool compares:

- **Declared system** ? domain.yaml
- **Implemented system** ? source code

It detects mismatches between the two, including:

- Relations used but not declared
- Declared relations not implemented
- Inputs defined but not used
- Outputs expected but not produced

## Example

Run:

python md_verify.py examples/thermal_solver

Example output:

--- Domain Verification Report ---

Domain: thermal_equilibrium

[ERROR] Relation outside declared domain: convection
[ERROR] Declared relation not present in implementation: diffusion
[INFO] Declared input not used: boundary_conditions
[INFO] Declared output not produced: equilibrium_temperature

---------------------------------

## What This Means

- The system is performing a transformation (convection) not defined in the domain
- A declared transformation (diffusion) is not present in the implementation
- Inputs and outputs do not align with system behavior

This reveals when a system operates outside its declared assumptions.

## Why It Matters

Most systems fail not because of syntax errors, but because they operate outside the conditions under which they are valid.

This tool makes those mismatches visible.

## Structure

md-domain-verifier/
¦
+-- md_verify.py
+-- verifier/
¦   +-- parser.py
¦   +-- scanner.py
¦   +-- checks.py
¦   +-- report.py
¦
+-- examples/
¦   +-- thermal_solver/
¦       +-- domain.yaml
¦       +-- thermal_equilibrium_solver.cpp

## Status

Early reference implementation.

## License

MIT (or specify)
