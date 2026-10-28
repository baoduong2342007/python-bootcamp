"""Unit tests for analyse in log_stats.py."""

from members.simble2k.w3.log_stats import analyse


def test_empty_pairs():
    res = analyse([])
    assert res == {"counts": {}, "p95": {}, "slowest": None}


def test_single_sample():
    res = analyse([("health", 150)])
    assert res["counts"]["health"] == 1
    assert res["p95"]["health"] == 150
    assert res["slowest"] == "health"


def test_official_baseline():
    pairs = [("fee", 100), ("fee", 300), ("fee", 200), ("rag", 900), ("rag", 1100)]
    res = analyse(pairs)
    assert res["counts"]["fee"] == 3
    assert res["counts"]["rag"] == 2
    assert res["p95"]["fee"] == 300
    assert res["p95"]["rag"] == 1100
    assert res["slowest"] == "rag"


def test_nearest_rank_twenty_samples():
    # 20 samples from 1 to 20: rank = ceil(0.95 * 20) - 1 = 19 - 1 = 18 -> value 19
    pairs = [("route_a", i) for i in range(1, 21)]
    res = analyse(pairs)
    assert res["counts"]["route_a"] == 20
    assert res["p95"]["route_a"] == 19
    assert res["slowest"] == "route_a"


def test_tie_breaking_picks_first_occurring_route():
    # route_x and route_y both have p95 = 500
    # route_x appears before route_y in the data
    pairs = [
        ("route_x", 100),
        ("route_x", 500),
        ("route_y", 200),
        ("route_y", 500),
    ]
    res = analyse(pairs)
    assert res["p95"]["route_x"] == 500
    assert res["p95"]["route_y"] == 500
    assert res["slowest"] == "route_x"

    # Reverse appearance order: route_y appears before route_x
    pairs_rev = [
        ("route_y", 200),
        ("route_y", 500),
        ("route_x", 100),
        ("route_x", 500),
    ]
    res_rev = analyse(pairs_rev)
    assert res_rev["slowest"] == "route_y"


def test_input_immutability_and_unsorted():
    original = [("beta", 400), ("alpha", 300), ("beta", 100), ("alpha", 200)]
    copy_original = list(original)

    res = analyse(original)
    # Check that input was not modified in-place
    assert original == copy_original

    # Alpha: [200, 300], n=2 -> ceil(0.95*2)-1 = 1 -> 300
    # Beta: [100, 400], n=2 -> ceil(0.95*2)-1 = 1 -> 400
    assert res["counts"]["alpha"] == 2
    assert res["counts"]["beta"] == 2
    assert res["p95"]["alpha"] == 300
    assert res["p95"]["beta"] == 400
    assert res["slowest"] == "beta"
