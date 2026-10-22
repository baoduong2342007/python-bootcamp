"""Total effort calculation for study planner."""

from collections.abc import Sequence

from shared.contract import Task


def total_effort(tasks: Sequence[Task]) -> float:
    """Calculate the total effort hours for given tasks.

    Returns 0.0 if tasks sequence is empty.
    Does not mutate input tasks sequence or task objects.
    """
    if not tasks:
        return 0.0
    return float(sum(t.effort_h for t in tasks))
