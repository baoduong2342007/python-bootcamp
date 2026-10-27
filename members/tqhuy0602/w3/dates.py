"""Parse task deadlines using an explicit reference date."""

import re
from datetime import date, timedelta

WEEKDAYS = (
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
)


def parse_due(text: str, today: date) -> date:
    """Parse ISO, tomorrow, in N days, or the next named weekday.

    Keywords are case-insensitive with surrounding whitespace ignored. Both
    full weekday names and three-letter abbreviations are accepted. The same
    weekday always means next week, never today. Unsupported/overflowing dates
    raise ValueError, and the system clock is never read.
    """
    value = text.strip().lower()
    try:
        if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
            return date.fromisoformat(value)
        if value == "tomorrow":
            return today + timedelta(days=1)
        relative = re.fullmatch(r"in ([0-9]+) days?", value)
        if relative:
            return today + timedelta(days=int(relative.group(1)))
        for index, weekday in enumerate(WEEKDAYS):
            if value in (weekday, weekday[:3]):
                return today + timedelta(days=(index - today.weekday()) % 7 or 7)
    except (ValueError, OverflowError) as exc:
        raise ValueError("Invalid or out-of-range due date") from exc
    raise ValueError("Expected YYYY-MM-DD, tomorrow, in N days, or a weekday")
