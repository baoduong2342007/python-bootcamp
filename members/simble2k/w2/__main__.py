"""Runnable entry point for simble2k Week 2 package."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    sample_path = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    if not sample_path.exists():
        print(f"Sample file not found at {sample_path}")
        return
    tasks = load_tasks(sample_path)
    for t in tasks:
        print(f"{t.title} (importance={t.importance}, effort={t.effort_h}h, deadline={t.deadline})")


if __name__ == "__main__":
    main()
