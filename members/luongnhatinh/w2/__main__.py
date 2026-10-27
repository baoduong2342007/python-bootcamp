from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    # Resolve repository root from members/luongnhatinh/w2/__main__.py (3 parents up)
    repo_root = Path(__file__).resolve().parents[3]
    samples_path = repo_root / "samples" / "tasks.csv"

    tasks = load_tasks(samples_path)
    for task in tasks:
        print(
            f"Task: {task.title} | Importance: {task.importance} | Effort: {task.effort_h}h | Deadline: {task.deadline}"
        )


if __name__ == "__main__":
    main()
