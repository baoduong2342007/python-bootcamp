"""Integration test for the shared study planner pipeline (Week 2).

Verifies the integration scenario specified in Section 3.4 of plan (3).md:
- Date: 2026-10-26
- Sample tasks: 'DS exam' (6.0h, importance 5, deadline 2026-10-30)
                'Assignment' (1.5h, importance 4, deadline 2026-10-27)
- Budget: 2.0 hours
- Total effort: 7.5
- Prioritised order: Assignment, DS exam
- Allocation: Assignment (1.5h), DS exam (0.5h)
- Rendered output:
  Assignment: 1.5 h
  DS exam: 0.5 h
"""

from datetime import date
from pathlib import Path

import pytest

from shared.contract import Task
from shared.total_effort import total_effort


def test_pipeline_total_effort_on_sample_tasks() -> None:
    """Verify total_effort component calculates 7.5h for the sample tasks."""
    tasks = [
        Task("DS exam", 5, 6.0, date(2026, 10, 30)),
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
    ]
    assert total_effort(tasks) == 7.5


def test_full_pipeline_when_all_functions_merged() -> None:
    """End-to-end integration test calling all 5 shared team functions.

    Skips gracefully if the other 4 team functions have not yet been merged into this branch.
    """
    try:
        from shared.parse_csv import parse_csv
        from shared.prioritise import prioritise
        from shared.render import render

        from shared.allocate import allocate
    except ImportError as e:
        pytest.skip(f"Integration pipeline awaiting team functions: {e}")

    sample_csv = Path(__file__).resolve().parents[2] / "samples" / "tasks.csv"
    if not sample_csv.exists():
        pytest.skip("samples/tasks.csv not available in current branch")

    today = date(2026, 10, 26)
    budget = 2.0

    tasks = parse_csv(sample_csv)
    assert len(tasks) == 2

    # Step 1: Total effort
    assert total_effort(tasks) == 7.5

    # Step 2: Prioritise
    ordered = prioritise(tasks, today)
    assert [t.title for t in ordered] == ["Assignment", "DS exam"]

    # Step 3: Allocate
    blocks = allocate(ordered, budget)
    assert len(blocks) == 2
    assert blocks[0].task.title == "Assignment"
    assert blocks[0].hours == 1.5
    assert blocks[1].task.title == "DS exam"
    assert blocks[1].hours == 0.5

    # Step 4: Render
    rendered = render(blocks)
    assert rendered == "Assignment: 1.5 h\nDS exam: 0.5 h"


if __name__ == "__main__":
    pytest.main([__file__])
