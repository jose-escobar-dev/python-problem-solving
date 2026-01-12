from problems.control_flow.count_changes import count_changes


def test_empty_iterable():
    assert count_changes([]) == 0


def test_ignores_non_int():
    assert count_changes([1, "x", 1, 2]) == 1


def test_counts_changes():
    assert count_changes([3, 3, 5, 5, 2, 2, 6]) == 3  # 3->5, 5->2, 2->6