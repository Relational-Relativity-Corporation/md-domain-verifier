def print_report(domain, results):
    print("\n--- Domain Verification Report ---\n")
    print(f"Domain: {domain.get('domain', 'unknown')}\n")

    for e in results["errors"]:
        print(f"[ERROR] {e}")

    for w in results["warnings"]:
        print(f"[WARNING] {w}")

    for i in results["info"]:
        print(f"[INFO] {i}")

    print("\n---------------------------------\n")
