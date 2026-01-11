from __future__ import annotations
from typing import Iterable


def count_changes(numbers: Iterable[int]) -> int:
    """
    Count how many times the current integer differs from the previous integer.

    Rules:
    - Ignore non-integer values.
    - The first valid integer establishes `previous` and is not compared.
    - If current == previous, it does not count as a change.

    Time: O(n)
    Space: O(1)
    """
    count = 0
    previous: int | None = None

    for current in numbers:
        # Ignore non-integer values.
        if not isinstance(current, int):
            continue

        if previous is not None and current != previous:
            count += 1

        previous = current

    return count