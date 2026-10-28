"""Exceptions and plan feasibility verification."""

from collections.abc import Sequence

from .models import Task


class InfeasiblePlan(Exception):
    """Raised when available hours cannot cover total needed effort."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        """Initialize with needed effort and available hours budget."""
        self.needed_h = float(needed_h)
        self.available_h = float(available_h)
        super().__init__(
            f"Plan is infeasible: needed {self.needed_h:g} hours, "
            f"but only {self.available_h:g} hours available."
        )


def check_feasible(tasks: Sequence[Task], available_h: float) -> None:
    """Check if task effort fits within available budget. Raise InfeasiblePlan if not."""
    needed = float(sum(t.effort_h for t in tasks))
    if needed > available_h:
        raise InfeasiblePlan(needed_h=needed, available_h=available_h)
