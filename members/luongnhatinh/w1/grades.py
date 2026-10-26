"""W1-1: Grade summary module."""


def summary(scores: list[float]):
    if not scores:
        raise ValueError("scores list cannot be empty")
    ans = {}
    s = 0
    ans["min"] = min(scores)
    ans["max"] = max(scores)
    for x in scores:
        s += x
    ans["mean"] = round(s / len(scores), 2)
    tmp = sorted(scores)
    n_scores = len(scores)
    if n_scores % 2 == 0:
        ans["median"] = round((tmp[n_scores // 2 - 1] + tmp[n_scores // 2]) / 2, 2)
    else:
        ans["median"] = round(tmp[n_scores // 2], 2)
    return ans
