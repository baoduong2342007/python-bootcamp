"""Unit tests for parse_due in dates.py."""

from datetime import date
import pytest

from members.simble2k.w3.dates import parse_due


def test_iso_dates_standard():
    today = date(2026, 10, 6)
    assert parse_due("2026-10-30", today) == date(2026, 10, 30)
    assert parse_due("2027-01-01", today) == date(2027, 1, 1)


def test_iso_dates_leap_year():
    today = date(2024, 1, 1)
    # 2024 is leap year, 2024-02-29 is valid
    assert parse_due("2024-02-29", today) == date(2024, 2, 29)
    # 2026 is not leap year, 2026-02-29 must raise ValueError
    with pytest.raises(ValueError):
        parse_due("2026-02-29", today)


def test_tomorrow():
    today = date(2026, 10, 6)
    assert parse_due("tomorrow", today) == date(2026, 10, 7)
    assert parse_due("  ToMoRRoW  ", today) == date(2026, 10, 7)

    # End of month transition
    today_eom = date(2026, 10, 31)
    assert parse_due("tomorrow", today_eom) == date(2026, 11, 1)

    # End of year transition
    today_eoy = date(2026, 12, 31)
    assert parse_due("tomorrow", today_eoy) == date(2027, 1, 1)


def test_in_n_days():
    today = date(2026, 10, 6)
    assert parse_due("in 3 days", today) == date(2026, 10, 9)
    assert parse_due("in 1 day", today) == date(2026, 10, 7)
    assert parse_due("IN 10 DAYS", today) == date(2026, 10, 16)
    assert parse_due("in 0 days", today) == date(2026, 10, 6)


def test_weekdays_upcoming():
    # 2026-10-06 is Tuesday (weekday 1)
    today = date(2026, 10, 6)

    # Upcoming Wednesday (weekday 2)
    assert parse_due("Wed", today) == date(2026, 10, 7)
    assert parse_due("Wednesday", today) == date(2026, 10, 7)

    # Upcoming Friday (weekday 4)
    assert parse_due("Fri", today) == date(2026, 10, 9)
    assert parse_due("friday", today) == date(2026, 10, 9)

    # Upcoming Sunday (weekday 6)
    assert parse_due("Sun", today) == date(2026, 10, 11)

    # Upcoming Monday (weekday 0) -> next week
    assert parse_due("Mon", today) == date(2026, 10, 12)


def test_weekdays_same_as_today_shifts_to_next_week():
    # 2026-10-06 is Tuesday. Tuesday should return Tuesday of NEXT week (+7 days)
    today = date(2026, 10, 6)
    assert parse_due("Tue", today) == date(2026, 10, 13)
    assert parse_due("tuesday", today) == date(2026, 10, 13)

    # Test Friday with today being Friday
    today_fri = date(2026, 10, 9)
    assert parse_due("Fri", today_fri) == date(2026, 10, 16)


def test_invalid_date_inputs():
    today = date(2026, 10, 6)

    with pytest.raises(ValueError, match="Unrecognized date format"):
        parse_due("someday", today)

    with pytest.raises(ValueError, match="Unrecognized date format"):
        parse_due("next week", today)

    with pytest.raises(ValueError, match="cannot be empty"):
        parse_due("", today)

    with pytest.raises(ValueError, match="cannot be empty"):
        parse_due("   ", today)

    with pytest.raises(ValueError, match="Expected string"):
        parse_due(12345, today)  # type: ignore

    with pytest.raises(ValueError, match="Invalid ISO date"):
        parse_due("2026-13-45", today)
