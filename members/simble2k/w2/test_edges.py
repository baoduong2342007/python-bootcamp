"""Comprehensive boundary and edge tests for simble2k Week 2 modules."""

import json
from datetime import date
from pathlib import Path

import pytest

from members.simble2k.w2.errors import InfeasiblePlan, check_feasible
from members.simble2k.w2.io_utils import load_tasks, save_json
from members.simble2k.w2.models import Task


# --- W2-1 Task boundary tests ---
def test_task_valid_importance():
    t1 = Task("Task 1", 1, 2.0, date(2026, 12, 1))
    assert t1.importance == 1
    t5 = Task("Task 5", 5, 0.0, date(2026, 12, 1))
    assert t5.importance == 5


@pytest.mark.parametrize("invalid_importance", [0, -1, 6, 10])
def test_task_invalid_importance(invalid_importance):
    with pytest.raises(ValueError, match="importance must be between 1 and 5"):
        Task("Bad", invalid_importance, 1.0, date(2026, 12, 1))


def test_task_nan_effort():
    with pytest.raises(ValueError, match="effort_h must be non-negative"):
        Task("NaN Effort", 3, float("nan"), date(2026, 12, 1))


def test_task_negative_effort():
    with pytest.raises(ValueError, match="effort_h must be non-negative"):
        Task("Negative", 3, -1.5, date(2026, 12, 1))


def test_task_days_left():
    today = date(2026, 10, 20)
    # Future deadline
    t_future = Task("Future", 3, 2.0, date(2026, 10, 25))
    assert t_future.days_left(today) == 5

    # Due today -> returns 0
    t_today = Task("Today", 3, 2.0, date(2026, 10, 20))
    assert t_today.days_left(today) == 0

    # Overdue yesterday -> returns 0
    t_past = Task("Past", 3, 2.0, date(2026, 10, 19))
    assert t_past.days_left(today) == 0

    # Overdue far in past -> returns 0
    t_far_past = Task("Far Past", 3, 2.0, date(2025, 1, 1))
    assert t_far_past.days_left(today) == 0


# --- W2-2 CSV and JSON edge tests ---
def test_load_tasks_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        load_tasks(Path("non_existent_file_xyz.csv"))


def test_load_tasks_empty_file(tmp_path):
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("", encoding="utf-8")
    assert load_tasks(empty_csv) == []


def test_load_tasks_header_only(tmp_path):
    header_csv = tmp_path / "header_only.csv"
    header_csv.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    assert load_tasks(header_csv) == []


def test_load_tasks_missing_header_columns(tmp_path):
    bad_header = tmp_path / "bad_header.csv"
    bad_header.write_text("title,importance,deadline\nTask1,3,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_tasks(bad_header)


def test_load_tasks_invalid_row_reports_line(tmp_path):
    bad_row = tmp_path / "bad_row.csv"
    content = (
        "title,importance,effort_h,deadline\n"
        "Valid Task 1,3,2.5,2026-10-30\n"
        "Invalid Importance,not_an_int,1.0,2026-10-30\n"
    )
    bad_row.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(bad_row)


def test_save_json_empty_list(tmp_path):
    out = tmp_path / "empty.json"
    save_json([], out)
    assert json.loads(out.read_text(encoding="utf-8")) == []


def test_save_json_roundtrip_utf8(tmp_path):
    tasks = [
        Task("Bài tập tiếng Việt", 4, 3.5, date(2026, 11, 15)),
        Task("Ôn tập ĐSTT", 5, 4.0, date(2026, 11, 20)),
    ]
    out = tmp_path / "tasks.json"
    save_json(tasks, out)

    data = json.loads(out.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert data[0]["title"] == "Bài tập tiếng Việt"
    assert data[0]["deadline"] == "2026-11-15"
    assert data[1]["title"] == "Ôn tập ĐSTT"
    assert data[1]["effort_h"] == 4.0


# --- W2-3 InfeasiblePlan and check_feasible tests ---
def test_check_feasible_exact_budget():
    tasks = [
        Task("T1", 3, 4.0, date(2026, 11, 1)),
        Task("T2", 3, 6.0, date(2026, 11, 2)),
    ]
    # Total effort is exactly 10.0; budget is 10.0 -> must not raise
    check_feasible(tasks, 10.0)


def test_check_feasible_more_budget():
    tasks = [Task("T1", 3, 5.0, date(2026, 11, 1))]
    check_feasible(tasks, 10.0)


def test_check_feasible_empty_budget_zero():
    check_feasible([], 0.0)


def test_check_feasible_insufficient_budget():
    tasks = [
        Task("T1", 3, 4.5, date(2026, 11, 1)),
        Task("T2", 3, 5.5, date(2026, 11, 2)),
    ]
    with pytest.raises(InfeasiblePlan) as exc_info:
        check_feasible(tasks, 5.0)

    err = exc_info.value
    assert err.needed_h == 10.0
    assert err.available_h == 5.0
    assert "10" in str(err)
    assert "5" in str(err)


if __name__ == "__main__":
    pytest.main([__file__])
