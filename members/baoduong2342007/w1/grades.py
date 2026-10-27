def summary(scores: list[float]) -> dict[str , float] :
    """Return minimum, maximum, mean and median of nonempty scores."""
    if (len(scores) == 0) :
        raise ValueError('scores must not be empty')

    Min = scores[0]
    Max = scores[0]
    Mean = 0
    for x in scores :
        Min = min(Min , x)
        Max = max(Max , x)
        Mean += x
    Mean /= len(scores)
    Mean = round(Mean , 2)
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    if (n % 2 == 0) :
        Median = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2
    else :
        Median = (sorted_scores[n // 2])
    Median = round(Median , 2)
    return {'min' : Min , 'max' : Max , 'mean' : Mean , 'median' : Median}
