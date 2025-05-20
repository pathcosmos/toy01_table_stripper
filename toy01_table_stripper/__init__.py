"""toy01_table_stripper package."""

__all__ = ["strip_table"]


def strip_table(data: str) -> str:
    """Return the input string without any HTML <table> tags."""
    result_lines = []
    in_table = False
    for line in data.splitlines():
        if "<table" in line:
            in_table = True
            continue
        if "</table>" in line:
            in_table = False
            continue
        if not in_table:
            result_lines.append(line)
    return "\n".join(result_lines)

