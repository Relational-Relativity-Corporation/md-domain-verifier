# md-domain-verifier

> Smallest possible domain verification tool demonstrating the ABRCE operator-A admissibility check applied to code.
> **Metatron Dynamics, 2026**

---

## What this does

A running system can produce locally valid outputs while operating outside its declared domain.
This tool catches that structural failure at the source by comparing a declarative domain.yaml
against the symbols extracted from the implementation — before the system runs.

This is a direct implementation of the operator-A admissibility condition from the
[ABRCE invariant relational kernel](https://github.com/Relational-Relativity-Corporation/Invariant_Relational_Kernel_ABRCE):
declare the domain first. No processing outside the declared domain is valid.

---

## How it works

1. domain.yaml declares the domain: inputs, relations, outputs, constraints
2. scanner.py extracts symbols from the implementation (.py, .cpp, .h)
3. checks.py compares declared symbols against extracted symbols
4. eport.py prints the verification report

Errors are raised for:
- Relations present in the implementation but not declared in domain.yaml
- Relations declared in domain.yaml but absent from the implementation

Info messages are raised for:
- Declared inputs not found in the implementation
- Declared outputs not found in the implementation

---

## Structure

```
md-domain-verifier/
├── domain_verifier/
│   ├── __init__.py
│   ├── parser.py
│   ├── scanner.py
│   ├── checks.py
│   └── report.py
├── examples/
│   └── thermal_solver/
│       ├── domain.yaml
│       └── thermal_equilibrium_solver.cpp
├── md_verify.py
├── requirements.txt
└── README.md
```

---

## Setup

```
pip install pyyaml
```

---

## Example

Run:

```
python md_verify.py examples/thermal_solver
```

Output:

```
--- Domain Verification Report ---

Domain: thermal_equilibrium

[ERROR] Relation outside declared domain: convection
[ERROR] Declared relation not present in implementation: diffusion
[INFO] Declared input not used: boundary_conditions
[INFO] Declared output not produced: equilibrium_temperature

---------------------------------
```

The convection term appears in the implementation but was never declared in domain.yaml.
The diffusion relation was declared but is absent from the implementation.
Both are operator-A violations: processing is occurring outside the declared domain.

---

## ABRCE layer

This tool operates entirely at operator A — domain declaration and admissibility.
It does not execute the system. It verifies that the declared domain matches the
implemented domain before any execution occurs.

The admissibility gap this catches: a system can pass every runtime check while
operating on undeclared relations. By the time conventional monitoring detects the
anomaly, the structural violation has already propagated.

---

## Framework

Framework: [ABRCE Invariant Relational Kernel](https://relationalrelativity.dev)
Org: [Relational-Relativity-Corporation](https://github.com/Relational-Relativity-Corporation)