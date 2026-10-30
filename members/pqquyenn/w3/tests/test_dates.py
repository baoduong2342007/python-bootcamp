"""Unit tests for parse_due in members/pqquyenn/w3/dates.py."""

from datetime import date

import pytest

from members.pqquyenn.w3.dates import parse_due


def test_official_baseline():
    """Verify official baseline assertions for parse_due."""
    today = date(2026, 10, 6)  # Tuesday
    assert parse_due("2026-10-30", today) == date(2026, 10, 30)
    assert parse_due("tomorrow", today) == date(2026, 10, 7)
    assert parse_due("in 3 days", today) == date(2026, 10, 9)
    assert parse_due("Fri", today) == date(2026, 10, 9)
    assert parse_due("Tue", today) == date(2026, 10, 13)
    with pytest.raises(ValueError):
        parse_due("someday", today)


def test_iso_dates_and_leap_years():
    """Verify ISO format parsing including leap year edge cases."""
    anchor = date(2026, 1, 15)
    assert parse_due("2026-12-25", anchor) == date(2026, 12, 25)
    assert parse_due("2024-02-29", date(2024, 1, 1)) == date(2024, 2, 29)

    # 2026 is not a leap year
    with pytest.raises(ValueError):
        parse_due("2026-02-29", anchor)

    # Out of range month/day
    with pytest.raises(ValueError):
        parse_due("2026-13-01", anchor)
    with pytest.raises(ValueError):
        parse_due("2026-04-31", anchor)


def test_tomorrow_transitions():
    """Verify tomorrow handles month and year rollovers."""
    assert parse_due("tomorrow", date(2026, 10, 31)) == date(2026, 11, 1)
    assert parse_due("  ToMoRRoW  ", date(2026, 12, 31)) == date(2027, 1, 1)


def test_in_n_days_variations():
    """Verify in N days with singular/plural, whitespace, and 0 days."""
    anchor = date(2026, 10, 6)
    assert parse_due("in 1 day", anchor) == date(2026, 10, 7)
    assert parse_due("in 5 days", anchor) == date(2026, 10, 11)
    assert parse_due("  IN   14   DAYS  ", anchor) == date(2026, 10, 20)
    assert parse_due("in 0 days", anchor) == date(2026, 10, 6)


def test_weekday_calculations():
    """Verify weekday matching strictly returns next occurrences."""
    # 2026-10-06 is Tuesday (weekday 1)
    today = date(2026, 10, 6)

    assert parse_due("Wed", today) == date(2026, 10, 7)
    assert parse_due("Wednesday", today) == date(2026, 10, 7)
    assert parse_due("Thu", today) == date(2026, 10, 8)
    assert parse_due("Friday", today) == date(2026, 10, 9)
    assert parse_due("Sat", today) == date(2026, 10, 10)
    assert parse_due("Sunday", today) == date(2026, 10, 11)
    assert parse_due("Mon", today) == date(2026, 10, 12)

    # Same weekday as today must jump to next week (+7 days)
    assert parse_due("Tue", today) == date(2026, 10, 13)
    assert parse_due("tuesday", today) == date(2026, 10, 13)


def test_invalid_date_inputs():
    """Verify invalid formats, types, and empty values raise appropriate errors."""
    today = date(2026, 10, 6)

    with pytest.raises(ValueError):
        parse_due("", today)
    with pytest.raises(ValueError):
        parse_due("   ", today)
    with pytest.raises(ValueError):
        parse_due("next week", today)
    with pytest.raises(ValueError):
        parse_due("2026/10/06", today)

    with pytest.raises(TypeError):
        parse_due(None, today)  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        parse_due(12345, today)  # type: ignore[arg-type]
