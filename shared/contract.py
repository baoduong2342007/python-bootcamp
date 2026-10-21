"""Common Week 2 types shared by all planner functions."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")
        if self.effort_h < 0:
            raise ValueError("effort_h must be non-negative")


@dataclass
class Block:
    task: Task
    hours: float

    def __post_init__(self) -> None:
        if self.hours < 0:
            raise ValueError("hours must be non-negative")
