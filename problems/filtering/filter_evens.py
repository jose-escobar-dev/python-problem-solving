from __future__ import annotations


def filter_evens(numbers: list[int]) -> list[int]:
    """
    Return a list containing only even integers from `numbers`.

    Rules:
    - If the list is empty, return [].
    - Assumes input is list[int] (type hints); no extra validation needed.

    Time: O(n)
    Space: O(n) for output
    """
    # Check if the list is empty
    if not numbers:
        return []

    return [n for n in numbers if n % 2 == 0]
