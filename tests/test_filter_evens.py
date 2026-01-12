from problems.filtering.filter_evens import filter_evens


def test_empty():
    assert filter_evens([]) == []


def test_filters_evens():
    assert filter_evens([1, 2, 3, 4, 6]) == [2, 4, 6]


def test_all_odds():
    assert filter_evens([1, 3, 5]) == []