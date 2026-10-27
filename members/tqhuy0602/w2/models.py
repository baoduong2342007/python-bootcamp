"""W2-1: task data and deadline arithmetic."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """Personal CSV task; shared planner conversion happens at the W3 boundary."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be between 1 and 5")

    def days_left(self, today: date) -> int:
        """Return remaining calendar days, clamping overdue tasks to zero."""
        return max(0, (self.deadline - today).days)
