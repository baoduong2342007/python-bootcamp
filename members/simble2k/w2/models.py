"""Task model for personal Week 2 exercises."""

import math
from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not (1 <= self.importance <= 5):
            raise ValueError("importance must be between 1 and 5")
        if math.isnan(self.effort_h) or not (self.effort_h >= 0):
            raise ValueError("effort_h must be non-negative")
        self.effort_h = float(self.effort_h)

    def days_left(self, today: date) -> int:
        """Return days until deadline, minimum 0. Today or past due returns 0."""
        return max(0, (self.deadline - today).days)
