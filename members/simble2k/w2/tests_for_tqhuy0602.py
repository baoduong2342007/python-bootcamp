"""Cross-tests for Huy's (tqhuy0602) Week 1 solutions."""

import pytest

from members.tqhuy0602.w1.grades import summary
from members.tqhuy0602.w1.rules import missing
from members.tqhuy0602.w1.text_tools import top_k
from members.tqhuy0602.w1.timetable import by_day
from members.tqhuy0602.w1.translate import insertion_sort


def test_summary_even_elements():
    """W2-4 case 1: summary on even-length score list, checking mean and median."""
    scores = [4.0, 8.0, 6.0, 2.0]
    res = summary(scores)
    assert res["min"] == 2.0
    assert res["max"] == 8.0
    assert res["mean"] == 5.0
    assert res["median"] == 5.0

    scores2 = [10.0, 1.0, 3.0, 6.0]
    res2 = summary(scores2)
    assert res2["min"] == 1.0
    assert res2["max"] == 10.0
    assert res2["mean"] == 5.0
    assert res2["median"] == 4.5


def test_top_k_zero_and_negative():
    """W2-4 case 2: top_k with k=0 or negative k must return an empty list."""
    text = "alpha beta alpha gamma beta alpha"
    assert top_k(text, 0) == []
    assert top_k(text, -1) == []
    assert top_k(text, -10) == []


def test_missing_single_shortage():
    """W2-4 case 3: missing requirement when only GPA is low or only credits are low."""
    # Only credits low (115 < 120, GPA 3.0 >= 2.0)
    assert missing(115, 3.0) == ["need 5 more credits"]
    # Only GPA low (120 >= 120, GPA 1.8 < 2.0)
    assert missing(120, 1.8) == ["need GPA at least 2.0"]


def test_by_day_preserves_duplicates():
    """W2-4 case 4: by_day preserves duplicate entries in the same weekday."""
    entries = [("CS50", "Mon"), ("MATH", "Mon"), ("CS50", "Mon"), ("ENG", "Tue")]
    res = by_day(entries)
    assert res["Mon"] == ["CS50", "CS50", "MATH"]
    assert res["Tue"] == ["ENG"]


def test_insertion_sort_in_place_and_duplicates():
    """W2-4 case 5: insertion_sort mutates in place, handles duplicates and reverse order."""
    data = [5, 2, 8, 2, 5, 1]
    res = insertion_sort(data)
    assert res is data
    assert res == [1, 2, 2, 5, 5, 8]

    # Already sorted list
    sorted_data = [1, 2, 3, 4]
    assert insertion_sort(sorted_data) is sorted_data
    assert sorted_data == [1, 2, 3, 4]

    # Reverse sorted with negative numbers
    reverse_data = [9, 5, 0, -3]
    assert insertion_sort(reverse_data) is reverse_data
    assert reverse_data == [-3, 0, 5, 9]


if __name__ == "__main__":
    pytest.main([__file__])
