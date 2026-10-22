"""W2-4: Cross-tests for Member 5 - Bao (simble2k) Week 1 modules."""

import pytest

from members.simble2k.w1.grades import summary
from members.simble2k.w1.rules import missing
from members.simble2k.w1.text_tools import top_k
from members.simble2k.w1.timetable import by_day
from members.simble2k.w1.translate import unique_preserve_order


def test_summary_even_length():
    """Case 1: summary on even-length score list, verifying min, max, mean, and median."""
    scores = [2.0, 4.0, 6.0, 8.0]
    result = summary(scores)
    assert result["min"] == 2.0
    assert result["max"] == 8.0
    assert result["mean"] == 5.0
    assert result["median"] == 5.0

    scores_unsorted = [7.5, 3.0, 9.5, 4.0]
    result2 = summary(scores_unsorted)
    assert result2["min"] == 3.0
    assert result2["max"] == 9.5
    assert result2["mean"] == 6.0
    assert result2["median"] == 5.75


def test_top_k_non_positive_k():
    """Case 2: top_k with k=0 or negative k must return an empty list."""
    text = "hello world hello python world hello"
    assert top_k(text, 0) == []
    assert top_k(text, -1) == []
    assert top_k(text, -10) == []
    assert top_k("", 0) == []
    assert top_k("", -2) == []


def test_missing_single_shortage():
    """Case 3: missing when only GPA is low or only credits are low."""
    # Only credits low (110 < 120, GPA 3.5 >= 2.0)
    assert missing(110, 3.5) == ["need 10 more credits"]
    # Only GPA low (120 >= 120, GPA 1.75 < 2.0)
    assert missing(120, 1.75) == ["need GPA at least 2.0"]
    # Both low
    both = missing(100, 1.5)
    assert "need 20 more credits" in both
    assert "need GPA at least 2.0" in both
    # Both met
    assert missing(120, 2.0) == []
    assert missing(140, 3.8) == []


def test_by_day_preserves_duplicate_courses():
    """Case 4: by_day keeps duplicate courses on the same day in sorted order."""
    entries = [
        ("Discrete Math", "Mon"),
        ("Calculus", "Mon"),
        ("Discrete Math", "Mon"),
        ("Physics", "Tue"),
    ]
    result = by_day(entries)
    assert result["Mon"] == ["Calculus", "Discrete Math", "Discrete Math"]
    assert result["Tue"] == ["Physics"]


def test_unique_preserve_order_contract():
    """Case 5: unique_preserve_order retains first occurrences and does not mutate input."""
    original = [4, 2, 7, 2, 4, 9, 1, 7]
    input_copy = list(original)
    result = unique_preserve_order(original)

    # Must preserve first occurrence order without duplicates
    assert result == [4, 2, 7, 9, 1]

    # Input list must not be modified
    assert original == input_copy

    # Edge cases
    assert unique_preserve_order([]) == []
    assert unique_preserve_order([5, 5, 5, 5]) == [5]
    assert unique_preserve_order([1, 2, 3]) == [1, 2, 3]
    assert unique_preserve_order([-2, -5, -2, 0, -5]) == [-2, -5, 0]


if __name__ == "__main__":
    pytest.main([__file__])
