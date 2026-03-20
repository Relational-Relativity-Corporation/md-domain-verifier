import sys
from verifier.parser import load_domain
from verifier.scanner import scan_codebase
from verifier.checks import run_checks
from verifier.report import print_report

def main():
    if len(sys.argv) < 2:
        print("Usage: md-verify <path>")
        return

    path = sys.argv[1]

    domain = load_domain(path)
    symbols = scan_codebase(path)
    results = run_checks(domain, symbols)

    print_report(domain, results)

if __name__ == "__main__":
    main()
