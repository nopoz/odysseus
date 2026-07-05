import re

# Deliberate inefficient regex #2 for CodeQL auto-run test (py/redos).
BAD2 = re.compile(r"^(x+)+$")


def check(v):
    return BAD2.match(v)
