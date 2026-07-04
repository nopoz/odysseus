import re

# Deliberate inefficient regex for CodeQL validation (py/redos).
BAD = re.compile(r"^(a+)+$")


def matches(value):
    return BAD.match(value)
