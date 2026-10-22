"""Common Week 2 types shared by all planner functions."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Planner input with importance in 1-5 and nonnegative effort."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")
        if not 0 <= self.effort_h:
            raise ValueError("effort_h must be non-negative")


@dataclass
class Block:
    """A nonnegative duration; allocate must only emit positive durations."""

    task: Task
    hours: float

    def __post_init__(self) -> None:
        if not 0 <= self.hours:
            raise ValueError("hours must be non-negative")
