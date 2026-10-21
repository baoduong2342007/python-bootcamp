"""Unit tests for allocate function in T-W2 study planner."""

from datetime import date

import pytest

from shared.allocate import allocate
from shared.contract import Task


@pytest.fixture
def sample_tasks() -> list[Task]:
    return [
        Task(title="Assignment", importance=4, effort_h=1.5, deadline=date(2026, 10, 27)),
        Task(title="DS exam", importance=5, effort_h=6.0, deadline=date(2026, 10, 30)),
        Task(title="Quick review", importance=3, effort_h=0.0, deadline=date(2026, 11, 1)),
        Task(title="Final essay", importance=2, effort_h=2.0, deadline=date(2026, 11, 5)),
    ]


def test_allocate_empty_tasks():
    assert allocate([], 5.0) == []


def test_allocate_non_positive_budget(sample_tasks):
    assert allocate(sample_tasks, 0.0) == []
    assert allocate(sample_tasks, -1.5) == []


def test_allocate_example_from_spec(sample_tasks):
    """Spec example: Assignment (1.5h), DS exam (6.0h) with 2.0h budget.

    Assignment receives 1.5h, DS exam receives 0.5h.
    """
    blocks = allocate(sample_tasks[:2], 2.0)
    assert len(blocks) == 2
    assert blocks[0].task.title == "Assignment"
    assert blocks[0].hours == 1.5
    assert blocks[1].task.title == "DS exam"
    assert blocks[1].hours == 0.5
    assert sum(b.hours for b in blocks) == 2.0


def test_allocate_exact_and_surplus(sample_tasks):
    # Exact sum of first two tasks: 1.5 + 6.0 = 7.5
    blocks_exact = allocate(sample_tasks[:2], 7.5)
    assert len(blocks_exact) == 2
    assert blocks_exact[0].hours == 1.5
    assert blocks_exact[1].hours == 6.0

    # Surplus budget: 10.0h available for 7.5h tasks
    blocks_surplus = allocate(sample_tasks[:2], 10.0)
    assert len(blocks_surplus) == 2
    assert blocks_surplus[0].hours == 1.5
    assert blocks_surplus[1].hours == 6.0
    assert sum(b.hours for b in blocks_surplus) == 7.5


def test_allocate_skips_zero_effort_tasks(sample_tasks):
    # sample_tasks has "Quick review" with effort_h=0.0
    blocks = allocate(sample_tasks, 10.0)
    titles = [b.task.title for b in blocks]
    assert "Quick review" not in titles
    assert all(b.hours > 0 for b in blocks)


def test_allocate_immutability(sample_tasks):
    tasks_copy = [Task(t.title, t.importance, t.effort_h, t.deadline) for t in sample_tasks]
    allocate(sample_tasks, 4.0)
    assert sample_tasks == tasks_copy


def test_allocate_preserves_task_identities(sample_tasks):
    blocks = allocate(sample_tasks[:2], 2.0)
    assert blocks[0].task is sample_tasks[0]
    assert blocks[1].task is sample_tasks[1]
