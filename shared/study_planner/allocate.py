"""Greedy study time allocation module for T-W2 study planner."""

from collections.abc import Sequence

from shared.contract import Block, Task


def allocate(tasks: Sequence[Task], hours: float) -> list[Block]:
    """Greedily allocate available study hours to tasks in the received order.

    Rules:
    - If budget hours <= 0, returns an empty list.
    - Allocates up to task.effort_h for each task in received order.
    - Allows partial allocation for the last task if remaining budget is less than effort_h.
    - Tasks with effort_h <= 0 do not produce a block.
    - Never produces blocks with 0 or negative hours.
    - Total allocated hours never exceeds available hours budget.
    - Does not mutate input tasks sequence or task objects.
    """
    if hours <= 0:
        return []

    blocks: list[Block] = []
    remaining_hours = float(hours)

    for task in tasks:
        if remaining_hours <= 0:
            break
        if task.effort_h <= 0:
            continue

        assigned = min(task.effort_h, remaining_hours)
        if assigned > 0:
            blocks.append(Block(task=task, hours=assigned))
            remaining_hours -= assigned

    return blocks
