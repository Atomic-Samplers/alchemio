from __future__ import annotations

import re
from pathlib import Path

from VaspIncar import VaspIncar


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


def read_incar(file_path: str) -> VaspIncar:
    data = {}
    current_key = None
    multiline_buffer = []
    continuation_key = None
    continuation_buffer = []
    block_key = None  # <-- new
    block_buffer = {}  # <-- new

    path = Path(file_path)
    with path.open() as f:
        for line in f:
            line_strip = line.rstrip("\n")

            if line_strip.startswith(("#", "!")):
                continue

            # ── Multiline string mode ────────────────────────────────────────
            if current_key is not None:
                if '"' in line_strip:
                    multiline_buffer.append(line_strip)
                    data[current_key] = "\n".join(multiline_buffer)
                    current_key = None
                    multiline_buffer = []
                else:
                    multiline_buffer.append(line_strip)
                continue

            # ── Line-continuation mode ───────────────────────────────────────
            if continuation_key is not None:
                line_content = line_strip.rstrip("\\")
                continuation_buffer.append(line_content)
                if not line_strip.endswith("\\"):
                    data[continuation_key] = clean_value(" ".join(continuation_buffer))
                    continuation_key = None
                    continuation_buffer = []
                continue

            # ── Block mode (e.g. KERNEL_TRUNCATION { ... }) ──────────────────
            if block_key is not None:
                if line_strip.strip() == "}":
                    data[block_key] = block_buffer
                    block_key = None
                    block_buffer = {}
                elif "=" in line_strip:
                    sub_key, sub_val = line_strip.split("=", 1)
                    block_buffer[sub_key.strip()] = clean_value(sub_val.strip())
                continue

            # ── Detect block opening: "KEY {" ────────────────────────────────
            block_match = re.match(r"^(\w+)\s*\{", line_strip)
            if block_match:
                block_key = block_match.group(1)
                block_buffer = {}
                continue

            # Skip lines without '='
            if "=" not in line_strip:
                continue

            # ── Multiple assignments on one line ─────────────────────────────
            if ";" in line_strip:
                for sub_line in line_strip.split(";"):
                    if "=" in sub_line:
                        key, value = sub_line.split("=", 1)
                        data[key.strip()] = clean_value(value)
                continue

            # ── Normal single assignment ─────────────────────────────────────
            key, value = line_strip.split("=", 1)
            key = key.strip()
            value = value.strip()

            # Multiline string start
            if value.startswith('"'):
                if value.endswith('"') and len(value) > 1:
                    data[key] = clean_value(value)
                    continue
                current_key = key
                multiline_buffer = [value]
                continue

            # Line continuation start
            if value.endswith("\\"):
                continuation_key = key
                continuation_buffer = [value.rstrip("\\")]
                continue

            data[key] = clean_value(value)

    return VaspIncar(**data)


def format_value(value) -> str:

    if isinstance(value, bool):
        return ".TRUE." if value else ".FALSE."

    if isinstance(value, (list, tuple)):
        return " ".join(format_value(v) for v in value)

    return str(value)


def write_incar(incar: VaspIncar, filename: str):
    path = Path(filename)
    with path.open("w") as f:
        for key, value in incar.items():
            # Nested dict block (e.g. KERNEL_TRUNCATION_FACTOR)
            if isinstance(value, dict):
                f.write(f"{key} {{\n")
                for sub_key, sub_val in value.items():
                    f.write(f"  {sub_key} = {format_value(sub_val)}\n")
                f.write("}\n")
                continue

            # Multiline strings → wrap in double quotes
            if isinstance(value, str) and "\n" in value:
                f.write(f'{key} = "{value}"\n')
                continue

            f.write(f"{key} = {format_value(value)}\n")
