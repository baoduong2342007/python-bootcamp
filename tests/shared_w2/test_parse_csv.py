"""Shared CSV contract tests; no dependency on personal implementations."""

from datetime import date

import pytest

from shared.contract import Task
from shared.parse_csv import parse_csv

HEADER = "title,importance,effort_h,deadline\n"


def test_shared_type_values_order_and_unicode(tmp_path):
    path = tmp_path / "tasks.csv"
    path.write_text(
        HEADER + '"Ôn tập, Python",5,6,2026-10-30\nAssignment,4,1.5,2026-10-27\n',
        encoding="utf-8",
    )
    tasks = parse_csv(path)
    assert all(type(task) is Task for task in tasks)
    assert tasks == [
        Task("Ôn tập, Python", 5, 6.0, date(2026, 10, 30)),
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
    ]


@pytest.mark.parametrize("contents", ["", HEADER])
def test_empty_input(tmp_path, contents):
    path = tmp_path / "empty.csv"
    path.write_text(contents, encoding="utf-8")
    assert parse_csv(path) == []


@pytest.mark.parametrize(
    "row",
    [
        "a,0,1,2026-10-30",
        "a,6,1,2026-10-30",
        "a,x,1,2026-10-30",
        "a,1,x,2026-10-30",
        "a,1,-1,2026-10-30",
        "a,1,1,2026-02-30",
        "a,1",
        "a,1,1,2026-10-30,extra",
    ],
)
def test_invalid_row_reports_line(tmp_path, row):
    path = tmp_path / "bad.csv"
    path.write_text(HEADER + "ok,1,1,2026-10-30\n" + row + "\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 3"):
        parse_csv(path)


def test_missing_column_reports_header(tmp_path):
    path = tmp_path / "bad-header.csv"
    path.write_text("title,importance\na,1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        parse_csv(path)


def test_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        parse_csv(tmp_path / "absent.csv")


def test_zero_effort_is_valid(tmp_path):
    path = tmp_path / "zero.csv"
    path.write_text(HEADER + "a,1,0,2026-10-30\n", encoding="utf-8")
    assert parse_csv(path)[0].effort_h == 0
