"""Date parsing module for due dates relative to an anchor date."""

import re
from datetime import date, timedelta

_WEEKDAYS: dict[str, int] = {
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

_IN_DAYS_PATTERN = re.compile(r"^in\s+(\d+)\s+days?$", re.IGNORECASE)


def parse_due(text: str, today: date) -> date:
    """Parse relative and ISO-formatted due date expressions.

    Supported expressions:
    - ISO format dates: 'YYYY-MM-DD'
    - 'tomorrow' -> anchor date + 1 day
    - 'in N day(s)' -> anchor date + N days
    - Weekday abbreviations or full names ('Fri', 'Tuesday', etc.) -> next occurrence
      strictly in the future (matching the current weekday shifts to next week).

    Args:
        text: String describing the due date.
        today: Reference anchor date.

    Returns:
        The resolved calendar date.

    Raises:
        TypeError: If text is not a string or today is not a date.
        ValueError: If text is empty, contains unrecognized format, or represents
            an invalid date (e.g. 2026-02-29 in a non-leap year).
    """
    if not isinstance(text, str):
        raise TypeError("Due date expression must be a string")
    if not isinstance(today, date):
        raise TypeError("Anchor date must be a date instance")

    cleaned = text.strip()
    if not cleaned:
        raise ValueError("Due date expression cannot be empty")

    lower = cleaned.lower()

    if lower == "tomorrow":
        return today + timedelta(days=1)

    in_days_match = _IN_DAYS_PATTERN.match(lower)
    if in_days_match:
        days_offset = int(in_days_match.group(1))
        return today + timedelta(days=days_offset)

    if lower in _WEEKDAYS:
        target_wd = _WEEKDAYS[lower]
        days_ahead = (target_wd - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    try:
        return date.fromisoformat(cleaned)
    except ValueError as exc:
        raise ValueError(f"Unrecognized or invalid due date format: {text!r}") from exc
