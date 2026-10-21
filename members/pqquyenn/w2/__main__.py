"""Runnable package entry point for members.pqquyenn.w2."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    """Load sample tasks and display them."""
    sample_csv = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    if not sample_csv.exists():
        print(f"Sample file not found at: {sample_csv}")
        return
    tasks = load_tasks(sample_csv)
    for task in tasks:
        print(f"{task.title} (importance: {task.importance}, effort: {task.effort_h:g}h, deadline: {task.deadline})")


if __name__ == "__main__":
    main()
