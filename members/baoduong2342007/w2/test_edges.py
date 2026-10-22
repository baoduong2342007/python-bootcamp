"""Additional boundary tests, separate from the instructor suite."""

import json
from datetime import date

import pytest

from .errors import InfeasiblePlan, check_feasible
from .io_utils import load_tasks, save_json
from .models import Task

HEADER = "title,importance,effort_h,deadline\n"


@pytest.mark.parametrize("importance", [1, 5])
def test_importance_endpoints(importance):
    assert Task("a", importance, 1, date(2026, 10, 30)).importance == importance


@pytest.mark.parametrize("importance", [0, 6])
def test_invalid_importance(importance):
    with pytest.raises(ValueError):
        Task("a", importance, 1, date(2026, 10, 30))


@pytest.mark.parametrize(
    "today,expected",
    [(date(2026, 10, 26), 4), (date(2026, 10, 30), 0), (date(2026, 11, 1), 0)],
)
def test_days_left(today, expected):
    assert Task("a", 1, 1, date(2026, 10, 30)).days_left(today) == expected


@pytest.mark.parametrize("contents", ["", HEADER])
def test_empty_csv(tmp_path, contents):
    path = tmp_path / "tasks.csv"
    path.write_text(contents, encoding="utf-8")
    assert load_tasks(path) == []


@pytest.mark.parametrize(
    "row",
    [
        "a,6,1,2026-10-30",
        "a,x,1,2026-10-30",
        "a,1,x,2026-10-30",
        "a,1,1,2026-02-30",
        "a,1",
        "a,1,1,2026-10-30,extra",
    ],
)
def test_bad_row_reports_line(tmp_path, row):
    path = tmp_path / "tasks.csv"
    path.write_text(HEADER + "ok,1,1,2026-10-30\n" + row + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(path)


def test_missing_header_columns(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text("title,importance\na,1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_tasks(path)


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_tasks(tmp_path / "missing.csv")


def test_unicode_roundtrip_and_order(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        HEADER + '"Ôn tập, Python",5,1.5,2026-10-30\nB,1,2,2026-11-01\n',
        encoding="utf-8",
    )
    tasks = load_tasks(path)
    assert tasks == [
        Task("Ôn tập, Python", 5, 1.5, date(2026, 10, 30)),
        Task("B", 1, 2.0, date(2026, 11, 1)),
    ]
    output = tmp_path / "tasks.json"
    save_json(tasks, output)
    assert json.loads(output.read_text(encoding="utf-8")) == [
        {
            "title": "Ôn tập, Python",
            "importance": 5,
            "effort_h": 1.5,
            "deadline": "2026-10-30",
        },
        {"title": "B", "importance": 1, "effort_h": 2.0, "deadline": "2026-11-01"},
    ]


def test_empty_json(tmp_path):
    output = tmp_path / "empty.json"
    save_json([], output)
    assert json.loads(output.read_text(encoding="utf-8")) == []


@pytest.mark.parametrize("hours", [10, 12])
def test_feasible_boundary(hours):
    check_feasible([Task("a", 1, 10, date(2026, 10, 30))], hours)


def test_infeasible_attributes():
    with pytest.raises(InfeasiblePlan) as caught:
        check_feasible([Task("a", 1, 10, date(2026, 10, 30))], 2)
    assert caught.value.needed_h == 10
    assert caught.value.available_h == 2
    assert "10" in str(caught.value) and "2" in str(caught.value)


def test_empty_plan():
    check_feasible([], 0)
