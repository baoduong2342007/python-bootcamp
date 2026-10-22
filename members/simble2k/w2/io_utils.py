"""I/O utilities for reading CSV and writing JSON tasks."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from CSV file, reporting line numbers on format errors."""
    path = Path(path)
    tasks: list[Task] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            return []
        required = {"title", "importance", "effort_h", "deadline"}
        if not required.issubset(set(reader.fieldnames)):
            raise ValueError("line 1: missing required CSV columns")
        for row in reader:
            try:
                if None in row:
                    raise ValueError("too many CSV fields")
                tasks.append(
                    Task(
                        title=row["title"],
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except Exception as exc:
                raise ValueError(f"line {reader.line_num}: invalid data ({exc})") from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file with ISO date formatting."""
    path = Path(path)
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
