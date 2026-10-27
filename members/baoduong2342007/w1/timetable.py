def by_day(a : list[tuple[str , str]]) -> dict[str , list[str]] :
    """Group and sort courses by day, retaining duplicates."""
    b = {}
    for course , day in a :
        b.setdefault(day, []).append(course)
    for courses in b.values():
        courses.sort()
    return b
