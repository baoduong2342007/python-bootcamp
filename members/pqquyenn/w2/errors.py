"""Custom exceptions and feasibility checking for study planning."""

from collections.abc import Sequence

from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when required study effort exceeds available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = float(needed_h)
        self.available_h = float(available_h)
        super().__init__(
            f"Infeasible plan: needed {self.needed_h:g} hours, but only {self.available_h:g} hours available"
        )


def check_feasible(tasks: Sequence[Task], available_h: float) -> None:
    """Verify that the total effort required does not exceed available hours.

    Raises InfeasiblePlan if needed_h > available_h.
    """
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
