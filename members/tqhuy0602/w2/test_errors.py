"""Feasibility at insufficient, exact, surplus and empty budgets."""

from datetime import date

import pytest

from .errors import InfeasiblePlan, check_feasible
from .models import Task


def tasks_needing_ten_hours():
    return [Task("a", 3, 6, date(2026, 10, 30)), Task("b", 3, 4, date(2026, 10, 30))]


def test_insufficient_budget_preserves_details():
    with pytest.raises(InfeasiblePlan) as exc:
        check_feasible(tasks_needing_ten_hours(), 2)
    assert exc.value.needed_h == 10
    assert exc.value.available_h == 2
    assert "10" in str(exc.value) and "2" in str(exc.value)


@pytest.mark.parametrize("available_h", [10, 12])
def test_exact_or_larger_budget_is_feasible(available_h):
    assert check_feasible(tasks_needing_ten_hours(), available_h) is None


def test_empty_plan_with_zero_budget():
    assert check_feasible([], 0) is None
