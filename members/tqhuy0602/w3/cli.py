"""Run a reproducible study plan using Huy's W2 loader and shared functions."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.tqhuy0602.w2.io_utils import load_tasks
from shared.contract import Task
from shared.study_planner import allocate, prioritise, render


def positive_hours(text: str) -> float:
    """Validate a finite positive CLI budget using argparse's exit-2 path."""
    try:
        hours = float(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            "hours must be a positive finite number"
        ) from exc
    if not math.isfinite(hours) or hours <= 0:
        raise argparse.ArgumentTypeError("hours must be a positive finite number")
    return hours


def build_parser() -> argparse.ArgumentParser:
    """Describe the personal CLI without reading files or the clock."""
    parser = argparse.ArgumentParser(description="Huy's W3 study planner")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--hours", type=positive_hours, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Print a partial plan; expected input/file errors go to stderr, exit 1."""
    args = build_parser().parse_args(argv)
    today = args.today if args.today is not None else date.today()
    try:
        personal_tasks = load_tasks(args.csv_path)
        # W2's personal and shared dataclasses are distinct types. Convert once
        # at the boundary; sorting/allocation stay in the existing shared code.
        tasks = []
        for task in personal_tasks:
            if not math.isfinite(task.effort_h) or task.effort_h < 0:
                raise ValueError("task effort must be finite and non-negative")
            tasks.append(
                Task(task.title, task.importance, task.effort_h, task.deadline)
            )
        print(render(allocate(prioritise(tasks, today), args.hours)))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
