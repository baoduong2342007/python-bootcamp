"""Deadline date parsing utilities."""

import re
from datetime import date, timedelta

WEEKDAYS = {
    "mon": 0,
    "monday": 0,
    "tue": 1,
    "tuesday": 1,
    "wed": 2,
    "wednesday": 2,
    "thu": 3,
    "thursday": 3,
    "fri": 4,
    "friday": 4,
    "sat": 5,
    "saturday": 5,
    "sun": 6,
    "sunday": 6,
}


def parse_due(text: str, today: date) -> date:
    """Parse human-readable deadline strings into concrete date objects.

    Supported formats:
    - ISO date: 'YYYY-MM-DD' (e.g. '2026-10-30')
    - 'tomorrow' -> today + 1 day
    - 'in N days' -> today + N days (N >= 0)
    - Weekday name (e.g. 'Fri', 'Tue') -> next occurrence after today (same weekday advances 7 days)

    Raises:
        ValueError: If text cannot be parsed or represents an invalid date.
    """
    clean_text = text.strip()
    if not clean_text:
        raise ValueError("Empty date string cannot be parsed.")

    # 1. ISO date: YYYY-MM-DD
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", clean_text):
        try:
            return date.fromisoformat(clean_text)
        except ValueError as exc:
            raise ValueError(f"Invalid ISO date: {clean_text}") from exc

    lower = clean_text.lower()

    # 2. 'tomorrow'
    if lower == "tomorrow":
        try:
            return today + timedelta(days=1)
        except OverflowError as exc:
            raise ValueError(f"Date overflow for 'tomorrow' from {today}") from exc

    # 3. 'in N days'
    in_days_match = re.fullmatch(r"in\s+(\d+)\s+days?", lower)
    if in_days_match:
        days_n = int(in_days_match.group(1))
        try:
            return today + timedelta(days=days_n)
        except OverflowError as exc:
            raise ValueError(
                f"Date overflow for 'in {days_n} days' from {today}"
            ) from exc

    # 4. Weekday names
    if lower in WEEKDAYS:
        target_wd = WEEKDAYS[lower]
        days_ahead = (target_wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        try:
            return today + timedelta(days=days_ahead)
        except OverflowError as exc:
            raise ValueError(
                f"Date overflow for weekday '{clean_text}' from {today}"
            ) from exc

    raise ValueError(f"Unrecognized date format: '{clean_text}'")
