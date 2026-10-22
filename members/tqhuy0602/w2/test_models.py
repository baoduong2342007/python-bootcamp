"""Additional W2-1 boundary coverage beyond the instructor's smoke test."""

from dataclasses import is_dataclass
from datetime import date

import pytest

from .models import Task


@pytest.mark.parametrize("importance", [1, 5])
def test_importance_boundaries(importance):
    task = Task("exam", importance, 1.5, date(2026, 10, 30))
    assert is_dataclass(task)
    assert task.importance == importance


@pytest.mark.parametrize("importance", [0, 6])
def test_importance_out_of_range(importance):
    with pytest.raises(ValueError, match="importance"):
        Task("exam", importance, 1.5, date(2026, 10, 30))


@pytest.mark.parametrize(
    ("today", "expected"),
    [(date(2026, 10, 26), 4), (date(2026, 10, 30), 0), (date(2026, 11, 2), 0)],
)
def test_days_left_clamps_at_zero(today, expected):
    assert Task("exam", 3, 1, date(2026, 10, 30)).days_left(today) == expected
