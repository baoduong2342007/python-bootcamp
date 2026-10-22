"""CSV input for the shared planner, using the team's Task type."""

import csv
from datetime import date
from pathlib import Path

from .contract import Task


def parse_csv(path: str | Path) -> list[Task]:
    tasks = []
    with open(path, encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None:
            return []
        required = {"title", "importance", "effort_h", "deadline"}
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
