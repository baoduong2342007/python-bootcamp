def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether credits and GPA meet thesis requirements."""
    return ((credits >= 120) and (gpa >= 2.0))

def missing(credits: int, gpa: float) -> list[str] :
    """Explain unmet thesis requirements."""
    x = []
    if not can_register_thesis(credits, gpa):
        if (credits < 120) :
            y = 'need ' + str(120 - credits) + ' more credits'
            x.append(y)

        if (gpa < 2.0) :
            y = 'need GPA at least 2.0'
            x.append(y)
    return x

