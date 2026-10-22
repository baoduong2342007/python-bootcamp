"""Tests for the common planner types."""

from datetime import date

import pytest

from shared.contract import Block, Task


@pytest.mark.parametrize("importance", [1, 5])
def test_valid_task_and_block(importance):
    task = Task("a", importance, 0, date(2026, 10, 30))
    assert task.effort_h == 0
    block = Block(task, 0)
    assert block.task is task and block.hours == 0


def test_positive_fractional_effort_and_hours():
    task = Task("a", 3, 1.5, date(2026, 10, 30))
    block = Block(task, 0.75)
    assert task.effort_h == 1.5
    assert block.task is task and block.hours == 0.75


@pytest.mark.parametrize("importance", [0, 6])
def test_invalid_importance(importance):
    with pytest.raises(ValueError, match="^importance must be between 1 and 5$"):
        Task("a", importance, 1, date(2026, 10, 30))


@pytest.mark.parametrize("effort", [-1, float("nan")], ids=["negative", "nan"])
def test_invalid_effort(effort):
    with pytest.raises(ValueError, match="^effort_h must be non-negative$"):
        Task("a", 1, effort, date(2026, 10, 30))


@pytest.mark.parametrize("hours", [-0.5, float("nan")], ids=["negative", "nan"])
def test_invalid_block_hours(hours):
    with pytest.raises(ValueError, match="^hours must be non-negative$"):
        Block(Task("a", 1, 1, date(2026, 10, 30)), hours)
