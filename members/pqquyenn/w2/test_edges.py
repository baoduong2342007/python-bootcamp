"""Edge case and unit tests for pqquyenn's Week 2 implementation."""

import json
from datetime import date
from pathlib import Path

import pytest

from members.pqquyenn.w2.errors import InfeasiblePlan, check_feasible
from members.pqquyenn.w2.io_utils import load_tasks, save_json
from members.pqquyenn.w2.models import Task

# --- Models Tests ---


def test_task_valid_boundaries():
    t1 = Task(title="Boundary low", importance=1, effort_h=0.0, deadline=date(2026, 12, 1))
    assert t1.importance == 1
    assert t1.effort_h == 0.0

    t5 = Task(title="Boundary high", importance=5, effort_h=10.5, deadline=date(2026, 12, 31))
    assert t5.importance == 5
    assert t5.effort_h == 10.5


def test_task_invalid_importance():
    with pytest.raises(ValueError, match="importance"):
        Task(title="Zero", importance=0, effort_h=1.0, deadline=date(2026, 12, 1))

    with pytest.raises(ValueError, match="importance"):
        Task(title="Six", importance=6, effort_h=1.0, deadline=date(2026, 12, 1))

    with pytest.raises(ValueError, match="importance"):
        Task(title="Negative", importance=-2, effort_h=1.0, deadline=date(2026, 12, 1))


def test_task_invalid_effort():
    with pytest.raises(ValueError, match="effort_h"):
        Task(title="Negative effort", importance=3, effort_h=-0.5, deadline=date(2026, 12, 1))

    with pytest.raises(ValueError, match="effort_h"):
        Task(title="NaN effort", importance=3, effort_h=float("nan"), deadline=date(2026, 12, 1))


def test_task_days_left():
    t = Task(title="Project", importance=4, effort_h=3.0, deadline=date(2026, 10, 30))
    # Future
    assert t.days_left(date(2026, 10, 25)) == 5
    # Same day
    assert t.days_left(date(2026, 10, 30)) == 0
    # Overdue
    assert t.days_left(date(2026, 11, 5)) == 0


# --- IO Utils Tests ---


def test_load_tasks_empty_and_header_only(tmp_path: Path):
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("", encoding="utf-8")
    assert load_tasks(empty_csv) == []

    header_csv = tmp_path / "header_only.csv"
    header_csv.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    assert load_tasks(header_csv) == []


def test_load_tasks_missing_header_columns(tmp_path: Path):
    bad_header = tmp_path / "bad_header.csv"
    bad_header.write_text("title,importance,deadline\nTask 1,3,2026-10-30\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_tasks(bad_header)


def test_load_tasks_corrupted_row(tmp_path: Path):
    corrupted = tmp_path / "corrupted.csv"
    corrupted.write_text(
        "title,importance,effort_h,deadline\n"
        "Task 1,3,2.0,2026-10-30\n"
        "Task 2,invalid_importance,1.5,2026-10-31\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(corrupted)


def test_load_tasks_invalid_date(tmp_path: Path):
    bad_date = tmp_path / "bad_date.csv"
    bad_date.write_text(
        "title,importance,effort_h,deadline\n"
        "Task 1,3,2.0,30-10-2026\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="line 2"):
        load_tasks(bad_date)


def test_load_tasks_non_existent():
    with pytest.raises(FileNotFoundError):
        load_tasks(Path("non_existent_file.csv"))


def test_save_json_roundtrip_with_unicode(tmp_path: Path):
    tasks = [
        Task(title="Lập trình Python", importance=5, effort_h=3.5, deadline=date(2026, 11, 15)),
        Task(title="Đọc tài liệu C++", importance=2, effort_h=1.0, deadline=date(2026, 11, 20)),
    ]
    out_file = tmp_path / "tasks.json"
    save_json(tasks, out_file)

    loaded_raw = json.loads(out_file.read_text(encoding="utf-8"))
    assert len(loaded_raw) == 2
    assert loaded_raw[0]["title"] == "Lập trình Python"
    assert loaded_raw[0]["importance"] == 5
    assert loaded_raw[0]["effort_h"] == 3.5
    assert loaded_raw[0]["deadline"] == "2026-11-15"
    assert loaded_raw[1]["title"] == "Đọc tài liệu C++"


def test_save_json_empty_list(tmp_path: Path):
    out_file = tmp_path / "empty.json"
    save_json([], out_file)
    assert json.loads(out_file.read_text(encoding="utf-8")) == []


# --- Errors Tests ---


def test_check_feasible():
    tasks = [
        Task("T1", 3, 2.5, date(2026, 10, 30)),
        Task("T2", 4, 3.5, date(2026, 10, 30)),
    ]  # total needed = 6.0

    # Sufficient time
    check_feasible(tasks, 6.0)
    check_feasible(tasks, 10.0)

    # Empty tasks with 0 hours
    check_feasible([], 0.0)

    # Insufficient time
    with pytest.raises(InfeasiblePlan) as exc_info:
        check_feasible(tasks, 5.0)

    exc = exc_info.value
    assert exc.needed_h == 6.0
    assert exc.available_h == 5.0
    assert "6" in str(exc)
    assert "5" in str(exc)
