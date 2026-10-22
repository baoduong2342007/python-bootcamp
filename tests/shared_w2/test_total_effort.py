"""Unit tests for shared total_effort function."""

from datetime import date

import pytest

from shared.contract import Task
from shared.study_planner import total_effort as total_effort_pkg
from shared.total_effort import total_effort


def test_total_effort_empty() -> None:
    """Empty task sequence returns 0.0 as a float."""
    assert total_effort([]) == 0.0
    assert isinstance(total_effort([]), float)
    assert total_effort(()) == 0.0


def test_total_effort_single() -> None:
    """Single task returns its exact effort_h."""
    t = Task("Single task", 3, 4.5, date(2026, 11, 1))
    assert total_effort([t]) == 4.5


def test_total_effort_multiple() -> None:
    """Multiple tasks return the sum of their effort hours."""
    tasks = [
        Task("DS exam", 5, 6.0, date(2026, 10, 30)),
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
    ]
    assert total_effort(tasks) == 7.5


def test_total_effort_zero_effort() -> None:
    """Tasks with zero effort are counted correctly."""
    tasks = [
        Task("Zero effort 1", 2, 0.0, date(2026, 10, 30)),
        Task("Normal effort", 4, 3.2, date(2026, 10, 31)),
        Task("Zero effort 2", 1, 0.0, date(2026, 11, 1)),
    ]
    assert total_effort(tasks) == 3.2


def test_total_effort_immutability() -> None:
    """Input list and Task attributes remain unmodified."""
    t1 = Task("Task A", 3, 2.5, date(2026, 11, 1))
    t2 = Task("Task B", 4, 3.5, date(2026, 11, 2))
    original_list = [t1, t2]
    list_copy = list(original_list)

    result = total_effort(original_list)

    assert result == 6.0
    assert original_list == list_copy
    assert t1.effort_h == 2.5
    assert t2.effort_h == 3.5


def test_total_effort_pkg_export() -> None:
    """Verify package import total_effort behaves identically."""
    tasks = [Task("Task A", 3, 2.5, date(2026, 11, 1))]
    assert total_effort_pkg(tasks) == 2.5


if __name__ == "__main__":
    pytest.main([__file__])
