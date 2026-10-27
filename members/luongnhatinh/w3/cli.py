"""Command-line interface for the study planner."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.luongnhatinh.w2.io_utils import load_tasks
from shared.allocate import allocate
from shared.contract import Task as SharedTask
from shared.prioritise import prioritise
from shared.render import render


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="members.luongnhatinh.w3.cli",
        description="Plan and allocate study hours from a CSV task list.",
    )
    parser.add_argument("csv_path", type=str, help="Path to the tasks CSV file.")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Total budget of study hours to allocate (must be positive).",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Anchor date for priority computation in YYYY-MM-DD format (defaults to current date).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not math.isfinite(args.hours) or args.hours <= 0:
        sys.stderr.write("Error: --hours must be greater than zero and finite.\n")
        return 1

    if args.today is not None:
        try:
            today_date = date.fromisoformat(args.today)
        except ValueError as exc:
            sys.stderr.write(f"Error: Invalid date format for --today: {exc}\n")
            return 1
    else:
        today_date = date.today()

    csv_file = Path(args.csv_path)
    try:
        personal_tasks = load_tasks(csv_file)
    except (FileNotFoundError, ValueError, OSError) as exc:
        sys.stderr.write(f"Error loading CSV file: {exc}\n")
        return 1

    # Convert personal tasks at the shared contract boundary, reporting bad input.
    try:
        shared_tasks = []
        for task in personal_tasks:
            if not math.isfinite(task.effort_h):
                raise ValueError(f"effort for {task.title!r} must be finite")
            shared_tasks.append(
                SharedTask(
                    title=task.title,
                    importance=task.importance,
                    effort_h=task.effort_h,
                    deadline=task.deadline,
                )
            )
    except ValueError as exc:
        sys.stderr.write(f"Error loading CSV file: {exc}\n")
        return 1

    prioritised = prioritise(shared_tasks, today_date)
    allocated_blocks = allocate(prioritised, args.hours)
    output_text = render(allocated_blocks)

    sys.stdout.write(output_text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
