"""Parse common due-date expressions relative to a supplied date."""

import re
from datetime import date, timedelta

_WEEKDAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, tomorrow, in N days, or the next named weekday."""
    value = text.strip().lower()
    if value == "tomorrow":
        return today + timedelta(days=1)
    match = re.fullmatch(r"in (\d+) days?", value)
    if match:
        return today + timedelta(days=int(match.group(1)))
    if value in _WEEKDAYS:
        days = (_WEEKDAYS.index(value) - today.weekday()) % 7 or 7
        return today + timedelta(days=days)
    return date.fromisoformat(value)
