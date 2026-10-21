"""CSV/JSON contract boundaries and error reporting."""

import json
from datetime import date

import pytest

from .io_utils import load_tasks, save_json
from .models import Task

HEADER = "title,importance,effort_h,deadline\n"


@pytest.mark.parametrize("contents", ["", HEADER])
def test_empty_csv(contents, tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_text(contents, encoding="utf-8")
    assert load_tasks(source) == []


def test_missing_header_reports_line_one(tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_text("title,importance\nexam,3\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_tasks(source)


@pytest.mark.parametrize(
    "bad_row",
    [
        "bad,no,1,2026-10-30",
        "bad,0,1,2026-10-30",
        "bad,3,no,2026-10-30",
        "bad,3,1,2026-02-30",
        "bad,3,1",
        "bad,3,1,2026-10-30,extra",
    ],
)
def test_bad_record_reports_line_three(bad_row, tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_text(HEADER + "ok,3,1,2026-10-30\n" + bad_row + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(source)


def test_order_types_quoted_unicode_title_and_json(tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_text(
        HEADER + '"Đề án, tuần 2",5,1.5,2026-10-30\nAssignment,4,6,2026-10-27\n',
        encoding="utf-8",
    )
    tasks = load_tasks(str(source))
    assert tasks == [
        Task("Đề án, tuần 2", 5, 1.5, date(2026, 10, 30)),
        Task("Assignment", 4, 6.0, date(2026, 10, 27)),
    ]
    assert isinstance(tasks[0].importance, int)
    assert isinstance(tasks[0].effort_h, float)
    output = tmp_path / "plan.json"
    save_json(tasks, str(output))
    assert json.loads(output.read_text(encoding="utf-8")) == [
        {"title": "Đề án, tuần 2", "importance": 5, "effort_h": 1.5, "deadline": "2026-10-30"},
        {"title": "Assignment", "importance": 4, "effort_h": 6.0, "deadline": "2026-10-27"},
    ]


def test_missing_file_is_not_wrapped(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_tasks(tmp_path / "missing.csv")


def test_save_empty_list(tmp_path):
    output = tmp_path / "empty.json"
    save_json([], output)
    assert json.loads(output.read_text(encoding="utf-8")) == []
