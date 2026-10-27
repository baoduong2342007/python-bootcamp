"""Date parsing utility for dynamic deadline handling."""

from datetime import date, timedelta
import re

WEEKDAYS: dict[str, int] = {
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
_ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_due(text: str, today: date) -> date:
    """Parse a flexible due date specification relative to a reference date.

    Supports:
    - ISO format dates: 'YYYY-MM-DD'
    - 'tomorrow': exactly 1 day after today
    - 'in N days' / 'in N day': N days after today (N non-negative integer)
    - Weekday name (e.g. 'Monday', 'Fri'): the upcoming occurrence strictly after today;
      if the given weekday matches today's weekday, returns that day in the following week.

    Args:
        text: The string representation of the due date.
        today: Reference date for relative calculations.

    Returns:
        The resolved calendar date.

    Raises:
        ValueError: If text cannot be parsed into a valid date or is empty.
    """
    if not isinstance(text, str):
        raise ValueError(
            f"Expected string for date specification, got {type(text).__name__}"
        )

    raw = text.strip()
    if not raw:
        raise ValueError("Due date text cannot be empty or whitespace only")

    # 1. ISO format 'YYYY-MM-DD'
    if _ISO_DATE_PATTERN.match(raw):
        try:
            return date.fromisoformat(raw)
        except ValueError as err:
            raise ValueError(f"Invalid ISO date '{raw}': {err}") from err

    lowered = raw.lower()

    # 2. 'tomorrow'
    if lowered == "tomorrow":
        return today + timedelta(days=1)

    # 3. 'in N days' / 'in N day'
    match = _IN_DAYS_PATTERN.match(lowered)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    # 4. Weekday name (strictly in the future)
    if lowered in WEEKDAYS:
        target_weekday = WEEKDAYS[lowered]
        delta = (target_weekday - today.weekday()) % 7
        if delta == 0:
            delta = 7
        return today + timedelta(days=delta)

    raise ValueError(f"Unrecognized date format: '{text}'")
