from __future__ import annotations

import re


def clean_value(value: str):

    # remove inline comments (#, !, and parentheses)
    value = re.split(r"[#!(]", value, maxsplit=1)[0].strip()

    # booleans
    if value.upper() in {".TRUE.", "TRUE", "T"}:
        return True
    if value.upper() in {".FALSE.", "FALSE", "F"}:
        return False

    # Numeric with optional trailing units
    match = re.fullmatch(
        r"([+-]?(\d+(\.\d*)?|\.\d+)([Ee][+-]?\d+)?)(?:\s*[a-zA-Z]+)?",
        value,
        re.IGNORECASE,
    )
    if match:
        return float(match.group(1))

    list_of_values = []
    # expand multiplier syntax (e.g. 6*0)
    for part in value.split():
        if "*" in part:
            try:
                n, v = part.split("*", 1)
                list_of_values.extend([float(v)] * int(n))
            except ValueError:
                list_of_values.append(part)
        else:
            list_of_values.append(part)

    # list of numbers
    if len(list_of_values) > 1:
        try:
            return [float(t) for t in list_of_values]
        except ValueError:
            return value

    token = list_of_values[0]

    # int
    if re.fullmatch(r"[+-]?\d+", token):
        return int(token)
    return value


def format_value(value) -> str:

    if isinstance(value, bool):
        return ".TRUE." if value else ".FALSE."

    if isinstance(value, (list, tuple)):
        return " ".join(format_value(v) for v in value)

    return str(value)
