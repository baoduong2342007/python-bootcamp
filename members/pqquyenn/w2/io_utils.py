"""Read CSV tasks and save tasks to JSON."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

REQUIRED_FIELDS = {"title", "importance", "effort_h", "deadline"}


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file.

    Preserves order of tasks. Raises ValueError with line number on errors.
    Header is line 1. Missing required headers raise ValueError with 'line 1'.
    Empty files or header-only files return an empty list.
    """
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return []

        # Check required fields
        if not REQUIRED_FIELDS.issubset(set(reader.fieldnames)):
            raise ValueError("line 1: missing required CSV columns")

        for row in reader:
            line_no = reader.line_num
            # Check for missing/extra columns
            if None in row or any(row.get(col) is None for col in REQUIRED_FIELDS):
                raise ValueError(f"line {line_no}: invalid row column count")

            try:
                title = row["title"].strip()
                if not title:
                    raise ValueError("title cannot be empty")
                importance = int(row["importance"])
                effort_h = float(row["effort_h"])
                deadline = date.fromisoformat(row["deadline"].strip())
                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
                tasks.append(task)
            except (ValueError, TypeError) as err:
                raise ValueError(f"line {line_no}: {err}") from err

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file.

    Format: JSON list containing dicts with title, importance, effort_h, and deadline (YYYY-MM-DD).
    Empty tasks list writes [].
    """
    serialized = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(serialized, f, ensure_ascii=False, indent=2)
