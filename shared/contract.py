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
            raise ValueError(f"Importance must be in range 1-5, got {self.importance}")
        if self.effort_h < 0:
            raise ValueError(f"Effort must be non-negative, got {self.effort_h}")


@dataclass
class Block:
    task: Task
    hours: float

    def __post_init__(self) -> None:
        if self.hours < 0:
            raise ValueError(f"Hours must be non-negative, got {self.hours}")
