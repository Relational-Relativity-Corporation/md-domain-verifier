def run_checks(domain, symbols):
    results = {
        "errors": [],
        "warnings": [],
        "info": []
    }

    inputs = set(domain.get("inputs", []))
    relations = set(domain.get("relations", []))
    outputs = set(domain.get("outputs", []))

    declared = inputs | relations | outputs

    # 🔴 Check for relations used but not declared
    for s in symbols:
        if s not in declared:
            if s not in inputs and s not in outputs:
                results["errors"].append(f"Relation outside declared domain: {s}")

    # 🔴 Check declared relations not used
    for r in relations:
        if r not in symbols:
            results["errors"].append(f"Declared relation not present in implementation: {r}")

    # 🔵 Info for unused inputs/outputs
    for i in inputs:
        if i not in symbols:
            results["info"].append(f"Declared input not used: {i}")

    for o in outputs:
        if o not in symbols:
            results["info"].append(f"Declared output not produced: {o}")

    return results