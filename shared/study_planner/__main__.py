"""Command-line interface for the shared Week 2 study planner."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from shared.parse_csv import parse_csv
from shared.study_planner import allocate, prioritise, render, total_effort


class InfeasiblePlan(Exception):
    """A complete plan requires more hours than available."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(f"Plan needs {needed_h:g} h; only {available_h:g} h available")


def positive_hours(value: str) -> float:
    """Parse a finite, positive time budget for argparse."""
    try:
        hours = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("hours must be a positive finite number") from exc
    if not math.isfinite(hours) or hours <= 0:
        raise argparse.ArgumentTypeError("hours must be a positive finite number")
    return hours


def iso_date(value: str) -> date:
    """Parse an ISO date for argparse."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("today must be an ISO date (YYYY-MM-DD)") from exc


def main(argv: list[str] | None = None) -> int:
    """Load and render a partial plan, or require all tasks when requested."""
    parser = argparse.ArgumentParser(description="Plan study time from a task CSV")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--hours", type=positive_hours, required=True)
    parser.add_argument("--today", type=iso_date, default=None)
    parser.add_argument("--require-all", action="store_true")
    args = parser.parse_args(argv)
    try:
        tasks = parse_csv(args.csv_path)
        needed = total_effort(tasks)
        if not math.isfinite(needed):
            raise ValueError("task effort must be finite")
        if args.require_all and needed > args.hours:
            raise InfeasiblePlan(needed, args.hours)
        print(render(allocate(prioritise(tasks, args.today or date.today()), args.hours)))
    except (OSError, UnicodeError, ValueError, InfeasiblePlan) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
