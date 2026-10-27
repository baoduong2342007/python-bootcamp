from members.luongnhatinh.w3.log_stats import analyse


def test_analyse_empty():
    res = analyse([])
    assert res == {"counts": {}, "p95": {}, "slowest": None}


def test_analyse_single_item():
    res = analyse([("fee", 150)])
    assert res["counts"] == {"fee": 1}
    assert res["p95"] == {"fee": 150}
    assert res["slowest"] == "fee"


def test_analyse_standard_pairs():
    pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    res = analyse(pairs)
    assert res["counts"] == {"fee": 3, "rag": 2}
    assert res["p95"]["fee"] == 300
    assert res["p95"]["rag"] == 1100
    assert res["slowest"] == "rag"


def test_analyse_nearest_rank_twenty_items():
    # 20 items: 1 to 20. ceil(0.95 * 20) - 1 = 19 - 1 = 18th index (0-based) -> value 19
    pairs = [("api", i) for i in range(1, 21)]
    res = analyse(pairs)
    assert res["p95"]["api"] == 19


def test_analyse_tie_breaking():
    # Two routes with same p95 latency: first encountered route wins
    pairs = [("routeA", 500), ("routeB", 500)]
    res = analyse(pairs)
    assert res["slowest"] == "routeA"

    pairs_reversed = [("routeB", 500), ("routeA", 500)]
    res_reversed = analyse(pairs_reversed)
    assert res_reversed["slowest"] == "routeB"


def test_analyse_does_not_mutate_input():
    original = [("fee", 300), ("fee", 100)]
    copied = list(original)
    analyse(original)
    assert original == copied
