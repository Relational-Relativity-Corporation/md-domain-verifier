import os
import re

STOPWORDS = {
    "int", "double", "float", "return", "main", "using",
    "namespace", "std", "include", "cout", "endl",
    "void", "char", "long", "short", "bool", "if", "else",
    "for", "while", "switch", "case", "break", "continue",
    "iostream"
}

def strip_comments(content):
    # remove C/C++ single-line comments
    content = re.sub(r'//.*', '', content)
    # remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    return content

def is_local_variable(token):
    return token.endswith("temp")

def scan_codebase(path):
    symbols = set()

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith((".py", ".cpp", ".h")):
                with open(os.path.join(root, file), "r", errors="ignore") as f:
                    content = f.read()

                    content = strip_comments(content)

                    tokens = re.findall(r'\b[a-zA-Z_]+\b', content)

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