"""Report a plan that exceeds the available study time."""

from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        """Record the required and available hours."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Plan needs {needed_h:g} h; only {available_h:g} h available")


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise InfeasiblePlan when total effort exceeds the budget."""
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
