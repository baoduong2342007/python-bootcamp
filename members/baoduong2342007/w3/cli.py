"""Dương's CLI, using his W2 loader and the shared planner functions."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.baoduong2342007.w2.io_utils import load_tasks
from shared.contract import Task
from shared.study_planner import allocate, prioritise, render


def positive_hours(value: str) -> float:
    """Require a positive finite budget."""
    try:
        hours = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a positive finite number") from exc
    if not math.isfinite(hours) or hours <= 0:
        raise argparse.ArgumentTypeError("hours must be a positive finite number")
    return hours


def iso_date(value: str) -> date:
    """Parse a calendar date for argparse."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("today must be an ISO date") from exc


def main(argv: list[str] | None = None) -> int:
    """Load personal W2 tasks, convert to shared types, and print a plan."""
    parser = argparse.ArgumentParser(description="Plan study time")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--hours", type=positive_hours, required=True)
    parser.add_argument("--today", type=iso_date, default=None)
    args = parser.parse_args(argv)
    try:
        personal_tasks = load_tasks(args.csv_path)
        tasks = [Task(t.title, t.importance, t.effort_h, t.deadline) for t in personal_tasks]
        if any(not math.isfinite(t.effort_h) for t in tasks):
            raise ValueError("task effort must be finite")
        print(render(allocate(prioritise(tasks, args.today or date.today()), args.hours)))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
