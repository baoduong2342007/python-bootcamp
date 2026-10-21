"""W2-2: ordered UTF-8 CSV loading and JSON serialization."""

import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

REQUIRED_FIELDS = {"title", "importance", "effort_h", "deadline"}


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks; report malformed headers/records with their CSV line number."""
    tasks = []
    with Path(path).open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source, strict=True)
        try:
            fields = reader.fieldnames
        except csv.Error as exc:
            raise ValueError(f"line 1: {exc}") from exc
        if fields is None:
            return []
        if not REQUIRED_FIELDS.issubset(fields):
            raise ValueError("line 1: required columns are title,importance,effort_h,deadline")
        try:
            for row in reader:
                try:
                    if None in row or any(row[field] is None for field in REQUIRED_FIELDS):
                        raise ValueError("record has the wrong number of fields")
                    task = Task(
                        title=row["title"],
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                except (ValueError, TypeError) as exc:
                    raise ValueError(f"line {reader.line_num}: {exc}") from exc
                tasks.append(task)
        except csv.Error as exc:
            raise ValueError(f"line {reader.line_num}: {exc}") from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Write all four fields in input order with ISO-formatted deadlines."""
    records = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    with Path(path).open("w", encoding="utf-8") as target:
        json.dump(records, target, ensure_ascii=False, indent=2)
        target.write("\n")
