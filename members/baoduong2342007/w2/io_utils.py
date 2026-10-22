"""Read CSV tasks and write their JSON representation."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks = []
    with open(path, encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        required = {"title", "importance", "effort_h", "deadline"}
        if reader.fieldnames is None:
            return []
        if not required.issubset(reader.fieldnames):
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
            except (TypeError, ValueError) as error:
                raise ValueError(f"line {reader.line_num}: {error}") from error
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    rows = [dict(asdict(task), deadline=task.deadline.isoformat()) for task in tasks]
    with open(path, "w", encoding="utf-8") as destination:
        json.dump(rows, destination, ensure_ascii=False, indent=2)
