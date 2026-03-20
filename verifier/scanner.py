import os
import re

STOPWORDS = {
    "int", "double", "float", "return", "main", "using",
    "namespace", "std", "include", "cout", "endl",
    "void", "char", "long", "short", "bool", "if", "else",
    "for", "while", "switch", "case", "break", "continue",
    "iostream", "true", "false", "null", "none", "self",
    "print", "import", "from", "class", "def", "pass"
}

# Suffixes that indicate a local computational variable, not a relation
LOCAL_SUFFIXES = ("_temp", "_val", "_buf", "_tmp", "_result", "_out", "_in")

def strip_comments(content):
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'#.*', '', content)
    return content

def is_local_variable(token):
    """
    Returns True if the token looks like a computational intermediate
    rather than a named domain relation.
    Filters common local variable naming patterns.
    """
    t = token.lower()
    if any(t.endswith(s) for s in LOCAL_SUFFIXES):
        return True
    # bare 'temp' or 'new_*' style intermediates
    if t == "temp" or t.startswith("new_"):
        return True
    return False

def scan_codebase(path):
    symbols = set()

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith((".py", ".cpp", ".h")):
                with open(os.path.join(root, file), "r", errors="ignore") as f:
                    content = strip_comments(f.read())
                    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', content)

                    for t in tokens:
                        t_lower = t.lower()
                        if t_lower in STOPWORDS:
                            continue
                        if is_local_variable(t_lower):
                            continue
                        if len(t_lower) < 5:
                            continue
                        symbols.add(t_lower)

    return symbols