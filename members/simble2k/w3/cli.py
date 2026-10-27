"""Command-line interface for the study planner (personal Week 3 exercise)."""

import argparse
from datetime import date
from pathlib import Path
import sys

from members.simble2k.w2.io_utils import load_tasks
from shared.contract import Task as SharedTask
from shared.study_planner import allocate, prioritise, render


def build_parser() -> argparse.ArgumentParser:
    """Construct command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="study-planner",
        description="Prioritise and allocate study blocks from a task list CSV file.",
    )
    parser.add_argument(
        "csv_path",
        type=Path,
        help="Path to tasks CSV file.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Total available study hours.",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Reference date in ISO format YYYY-MM-DD (defaults to today).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns exit code 0 on success, 1 on error, 2 on bad arguments."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.hours < 0:
        print("Error: --hours must be non-negative.", file=sys.stderr)
        return 2

    if args.today:
        try:
            today = date.fromisoformat(args.today)
        except ValueError as exc:
            print(
                f"Error: Invalid --today date format '{args.today}': {exc}",
                file=sys.stderr,
            )
            return 2
    else:
        today = date.today()

    try:
        if not args.csv_path.exists():
            print(
                f"Error: Tasks file '{args.csv_path}' does not exist.", file=sys.stderr
            )
            return 1

        personal_tasks = load_tasks(args.csv_path)

        # Bridge boundary: Convert personal models to shared contract Tasks
        shared_tasks = [
            SharedTask(
                title=t.title,
                importance=t.importance,
                effort_h=t.effort_h,
                deadline=t.deadline,
            )
            for t in personal_tasks
        ]

        prioritised = prioritise(shared_tasks, today)
        blocks = allocate(prioritised, args.hours)
        output = render(blocks)
        print(output)
        return 0

    except Exception as exc:
        print(f"Error processing plan: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
