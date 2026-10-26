from datetime import date

import pytest

from members.luongnhatinh.w3.dates import parse_due

TODAY = date(2026, 10, 6)  # Tuesday


def test_parse_iso_date():
    assert parse_due("2026-10-30", TODAY) == date(2026, 10, 30)
    assert parse_due("2024-02-29", TODAY) == date(2024, 2, 29)  # leap year


def test_parse_tomorrow():
    assert parse_due("tomorrow", TODAY) == date(2026, 10, 7)
    assert parse_due("TOMORROW", TODAY) == date(2026, 10, 7)


def test_parse_in_n_days():
    assert parse_due("in 3 days", TODAY) == date(2026, 10, 9)
    assert parse_due("in 1 day", TODAY) == date(2026, 10, 7)
    assert parse_due("in 0 days", TODAY) == date(2026, 10, 6)


def test_parse_weekdays():
    # TODAY is Tuesday (weekday 1)
    assert parse_due("Fri", TODAY) == date(2026, 10, 9)
    assert parse_due("friday", TODAY) == date(2026, 10, 9)
    assert parse_due("Wed", TODAY) == date(2026, 10, 7)
    assert parse_due("Mon", TODAY) == date(2026, 10, 12)
    # Same weekday strictly advances by 7 days
    assert parse_due("Tue", TODAY) == date(2026, 10, 13)
    assert parse_due("Tuesday", TODAY) == date(2026, 10, 13)


def test_parse_invalid_raises_value_error():
    with pytest.raises(ValueError):
        parse_due("someday", TODAY)
    with pytest.raises(ValueError):
        parse_due("", TODAY)
    with pytest.raises(ValueError):
        parse_due("2026-02-31", TODAY)
    with pytest.raises(ValueError):
        parse_due("next year", TODAY)
