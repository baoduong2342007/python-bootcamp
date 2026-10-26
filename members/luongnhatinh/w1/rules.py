"""W1-3: Thesis eligibility module."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    return bool(credits >= 120 and gpa >= 2.0)


def missing(credits: int, gpa: float) -> list[str]:
    ans = []
    if can_register_thesis(credits, gpa):
        return ans
    if credits < 120:
        a = 120 - credits
        s = f"need {a} more credits"
        ans.append(s)
    if gpa < 2.0:
        ans.append("need GPA at least 2.0")
    return ans
