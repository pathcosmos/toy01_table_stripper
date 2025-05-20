from __future__ import annotations

import sys
from toy01_table_stripper import strip_table


def main() -> int:
    data = sys.stdin.read()
    print(strip_table(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

