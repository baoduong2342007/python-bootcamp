"""W2-4: requirement-based edge checks for Minh's Week 1 functions.

Run explicitly: python -m pytest -q members/tqhuy0602/w2/tests_for_luongnhatinh.py
"""

import pytest

from members.luongnhatinh.w1.grades import summary
from members.luongnhatinh.w1.rules import missing
from members.luongnhatinh.w1.text_tools import top_k
from members.luongnhatinh.w1.timetable import by_day
from members.luongnhatinh.w1.translate import primes_up_to


def test_summary_even_unsorted_scores():
    scores = [10.0, 2.0, 4.0, 8.0]
    assert summary(scores) == {"min": 2.0, "max": 10.0, "mean": 6.0, "median": 6.0}
    assert scores == [10.0, 2.0, 4.0, 8.0]


@pytest.mark.parametrize("k", [0, -1])
def test_top_k_nonpositive(k):
    assert top_k("apple banana apple", k) == []


def test_missing_only_gpa():
    assert missing(120, 1.99) == ["need GPA at least 2.0"]


def test_missing_only_one_credit():
    assert missing(119, 2.0) == ["need 1 more credits"]


def test_by_day_keeps_duplicate_courses():
    entries = [("MATH", "Mon"), ("CS", "Mon"), ("MATH", "Mon"), ("PHY", "Tue")]
    assert by_day(entries) == {"Mon": ["CS", "MATH", "MATH"], "Tue": ["PHY"]}


def test_primes_at_smallest_prime():
    assert primes_up_to(2) == [2]
