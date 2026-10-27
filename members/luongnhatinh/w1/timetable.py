"""W1-5: Group the timetable by day module."""


def by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]:
    result = {}
    for course, day in entries:
        result.setdefault(day, []).append(course)
    for courses in result.values():
        courses.sort()
    return result
