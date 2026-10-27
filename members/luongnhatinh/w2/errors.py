from collections.abc import Sequence

from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float, message: str = "") -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        if not message:
            message = (
                f"Infeasible plan: needed {needed_h}h exceeds available {available_h}h"
            )
        super().__init__(message)


def check_feasible(tasks: Sequence[Task], available_h: float) -> None:
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h=needed_h, available_h=available_h)
