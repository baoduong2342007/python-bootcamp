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


@pytest.mark.parametrize("importance", [0, 6])
def test_invalid_importance(importance):
    with pytest.raises(ValueError):
        Task("a", importance, 1, date(2026, 10, 30))


def test_negative_effort():
    with pytest.raises(ValueError):
        Task("a", 1, -1, date(2026, 10, 30))


def test_negative_block_hours():
    with pytest.raises(ValueError):
        Block(Task("a", 1, 1, date(2026, 10, 30)), -0.5)
