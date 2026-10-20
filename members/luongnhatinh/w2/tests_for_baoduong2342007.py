import pytest

from members.baoduong2342007.w1.grades import summary
from members.baoduong2342007.w1.rules import missing
from members.baoduong2342007.w1.text_tools import top_k
from members.baoduong2342007.w1.timetable import by_day
from members.baoduong2342007.w1.translate import binary_search


def test_summary_even_number_of_elements():
    """W2-4 case 1: summary on even-length score list, testing mean and median."""
    scores = [2.0, 4.0, 6.0, 8.0]
    res = summary(scores)
    assert res["min"] == 2.0
    assert res["max"] == 8.0
    assert res["mean"] == 5.0
    assert res["median"] == 5.0

    scores_unsorted = [10.0, 2.0, 4.0, 8.0]
    res_unsorted = summary(scores_unsorted)
    assert res_unsorted["min"] == 2.0
    assert res_unsorted["max"] == 10.0
    assert res_unsorted["mean"] == 6.0
    assert res_unsorted["median"] == 6.0


def test_top_k_zero_and_negative():
    """W2-4 case 2: top_k with k=0 or negative number must return an empty list."""
    text = "apple banana apple cherry banana apple"
    assert top_k(text, 0) == []
    assert top_k(text, -1) == []
    assert top_k(text, -5) == []


def test_missing_single_shortage():
    """W2-4 case 3: missing requirement when only GPA is low or only credits are missing."""
    # Only GPA is low (credits = 120 >= 120, GPA = 1.8 < 2.0)
    gpa_shortage = missing(120, 1.8)
    assert gpa_shortage == ["need GPA at least 2.0"]

    # Only credits are low (credits = 119 < 120, GPA = 3.5 >= 2.0)
    credit_shortage = missing(119, 3.5)
    assert credit_shortage == ["need 1 more credits"]


def test_by_day_duplicate_courses():
    """W2-4 case 4: by_day preserves duplicate course entries on the same weekday."""
    entries = [
        ("MATH101", "Mon"),
        ("CS101", "Mon"),
        ("MATH101", "Mon"),
        ("PHY101", "Tue"),
    ]
    timetable = by_day(entries)
    assert timetable["Mon"] == ["CS101", "MATH101", "MATH101"]
    assert timetable["Tue"] == ["PHY101"]


def test_binary_search_single_element():
    """W2-4 case 5: TV1 binary_search on a single-element list (found vs not found)."""
    single = [42]
    # Found target
    assert binary_search(single, 42) == 0

    # Target smaller than element -> not found
    assert binary_search(single, 10) == -1

    # Target larger than element -> not found
    assert binary_search(single, 99) == -1


if __name__ == "__main__":
    pytest.main([__file__])
