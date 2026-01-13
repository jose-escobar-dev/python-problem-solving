from typing import Iterable


def group_consecutive_equals(numbers: Iterable[int]) -> list[list[int]]:
    """
    Group consecutive equal integers into sublists.

    Args:
        numbers: An iterable of integers. Non-integer values are ignored.

    Returns:
        A list of lists, where each inner list contains consecutive
        equal integers from the input.

    Rules:
        - Only consecutive values are grouped.
        - Equal values separated by different numbers start a new group.
        - Non-integer values are skipped.
    """
    groups = []
    current_group = []
    previous = None  # Tracks the last valid integer processed

    for current in numbers:
        # Skip invalid input to keep the function tolerant of mixed data
        if not isinstance(current, int):
            continue

        # First valid value initializes the first group
        if previous is None:
            current_group = [current]
            previous = current
            continue

        if current == previous:
            # Same value → extend the current group
            current_group.append(current)
        else:
            # New value → close current group and start a new one
            groups.append(current_group)
            current_group = [current]

        previous = current

    # Append the last group if any values were collected
    if current_group:
        groups.append(current_group)

    return groups
