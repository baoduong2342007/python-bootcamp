import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    tasks: list[Task] = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return []

        clean_header = [col.strip() for col in header]
        expected_cols = ["title", "importance", "effort_h", "deadline"]
        if clean_header != expected_cols:
            raise ValueError("Missing or invalid required CSV columns at line 1")

        for line_no, row in enumerate(reader, start=2):
            if not row or all(c.strip() == "" for c in row):
                continue
            if len(row) != 4:
                raise ValueError(f"Invalid column count at line {line_no}")

            title = row[0].strip()
            try:
                importance = int(row[1].strip())
                effort_h = float(row[2].strip())
                deadline = date.fromisoformat(row[3].strip())
                task = Task(title=title, importance=importance, effort_h=effort_h, deadline=deadline)
            except Exception as exc:
                raise ValueError(f"Invalid task data at line {line_no}: {exc}") from exc

            tasks.append(task)

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    file_path = Path(path)
    payload = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(file_path, mode="w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
