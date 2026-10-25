"""W2-3: report insufficient study time without swallowing the failure."""

from .models import Task


class InfeasiblePlan(Exception):
    """A plan requires more study hours than the available budget."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Plan needs {needed_h:g} h; only {available_h:g} h available.")


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan with required/available hours when the budget is short."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
