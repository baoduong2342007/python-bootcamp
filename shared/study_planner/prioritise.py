"""Stable priority ordering for the Week 2 shared planner."""

from collections.abc import Sequence
from datetime import date

from shared.contract import Task


def prioritise(tasks: Sequence[Task], today: date) -> list[Task]:
    """Return a new list ordered by importance / max(1, remaining days).

    Due and overdue tasks use a one-day denominator. Equal scores keep their
    input order; neither the input sequence nor its Task objects are changed.
    """
    return sorted(
        tasks,
        key=lambda task: task.importance / max(1, (task.deadline - today).days),
        reverse=True,
    )
