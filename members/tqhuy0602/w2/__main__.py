"""W2-5: run from the repository root with python -m members.tqhuy0602.w2."""

from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    sample = Path(__file__).resolve().parents[3] / "samples" / "tasks.csv"
    for task in load_tasks(sample):
        print(task)


if __name__ == "__main__":
    main()
