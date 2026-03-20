import yaml
import os

def load_domain(path):
    domain_file = os.path.join(path, "domain.yaml")

    if not os.path.exists(domain_file):
        raise FileNotFoundError("domain.yaml not found")

    with open(domain_file, "r") as f:
        data = yaml.safe_load(f)

    return data
