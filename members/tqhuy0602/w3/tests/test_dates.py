"""Deadline boundaries beyond the instructor's examples."""

from datetime import date

import pytest

from members.tqhuy0602.w3.dates import parse_due


@pytest.mark.parametrize(
    ("text", "today", "expected"),
    [
        ("tomorrow", date(2026, 12, 31), date(2027, 1, 1)),
        ("in 3 days", date(2026, 10, 30), date(2026, 11, 2)),
        ("tomorrow", date(2028, 2, 28), date(2028, 2, 29)),
        ("2028-02-29", date(2026, 1, 1), date(2028, 2, 29)),
        (" Tue ", date(2026, 10, 6), date(2026, 10, 13)),
        ("FRIDAY", date(2026, 10, 6), date(2026, 10, 9)),
        ("in 0 days", date(2026, 10, 6), date(2026, 10, 6)),
        ("in 1 day", date(2026, 10, 6), date(2026, 10, 7)),
    ],
)
def test_due_boundaries(text, today, expected):
    assert parse_due(text, today) == expected


@pytest.mark.parametrize(
    "text", ["", "someday", "2026-02-29", "2026-13-01", "20261030", "in -1 days"]
)
def test_invalid_due(text):
    with pytest.raises(ValueError):
        parse_due(text, date(2026, 10, 6))


@pytest.mark.parametrize("text", ["tomorrow", "Fri", "in 999999999999999999999 days"])
def test_out_of_range_due(text):
    with pytest.raises(ValueError):
        parse_due(text, date.max)
