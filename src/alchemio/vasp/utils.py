from __future__ import annotations

import re


def parse_number(s):
    """Parse a string into int, float, or (float, unit) tuple."""
    if isinstance(s, (int, float)):
        return s
    # INTEGERS (+/- INT)
    if re.fullmatch(r"[+-]?\d+", s):
        return int(s)
    #INT or FLOAT with Units
    match = re.fullmatch(
        r"([+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?)\s*([a-zA-Z°µΩ%/]+(?:\s*[a-zA-Z°µΩ%/]+)*)",
        s,
    )
    if match:
        return (float(match.group(1)), match.group(2))
    return float(s)

def clean_value(value: str):
    """Clean and parse a raw config string value."""
    # remove inline comments (#, !, and parentheses)
    value = re.split(r"[#!(]", value, maxsplit=1)[0].strip()
    # booleans
    if value.upper() in {".TRUE.", "TRUE", "T"}:
        return True
    if value.upper() in {".FALSE.", "FALSE", "F"}:
        return False
    # try direct numeric parse (int, float, or float+unit)
    try:
        return parse_number(value)
    except ValueError:
        pass
    # expand multiplier syntax (e.g. 6*0)
    list_of_values = []
    for part in value.split():
        if "*" in part:
            try:
                n, v = part.split("*", 1)
                list_of_values.extend([parse_number(v)] * int(n))
            except ValueError:
                list_of_values.append(part)
        else:
            list_of_values.append(part)
    # list of numbers
    if len(list_of_values) > 1:
        try:
            return [parse_number(t) for t in list_of_values]
        except ValueError:
            return value
    # unparseable — return as-is
    return value


def format_value(value) -> str:

    if isinstance(value, bool):
        return ".TRUE." if value else ".FALSE."

    if isinstance(value, (list, tuple)):
        return " ".join(format_value(v) for v in value)

    return str(value)
