"""Unit tests for analyse in members/pqquyenn/w3/log_stats.py."""

from members.pqquyenn.w3.log_stats import analyse


def test_empty_pairs():
    """Verify analyse returns empty dictionaries and None on empty input."""
    res = analyse([])
    assert res == {"counts": {}, "p95": {}, "slowest": None}


def test_single_sample():
    """Verify single route sample analysis."""
    res = analyse([("auth", 120)])
    assert res["counts"] == {"auth": 1}
    assert res["p95"] == {"auth": 120}
    assert res["slowest"] == "auth"


def test_official_baseline():
    """Verify official baseline assertions for analyse."""
    pairs = [("fee", 100), ("fee", 300), ("rag", 900), ("rag", 1100), ("fee", 200)]
    res = analyse(pairs)
    assert res["counts"] == {"fee": 3, "rag": 2}
    assert res["slowest"] == "rag"
    assert res["p95"]["fee"] == 300
    assert res["p95"]["rag"] == 1100


def test_nearest_rank_twenty_samples():
    """Verify nearest-rank calculation with n=20 yields rank 18 (value 19)."""
    # ceil(0.95 * 20) - 1 = 19 - 1 = 18 -> 19
    pairs = [("query", i) for i in range(1, 21)]
    res = analyse(pairs)
    assert res["counts"]["query"] == 20
    assert res["p95"]["query"] == 19
    assert res["slowest"] == "query"


def test_tie_breaking_picks_first_occurring_route():
    """Verify ties in maximal p95 resolve to the first encountered route."""
    pairs = [
        ("route_a", 250),
        ("route_a", 500),
        ("route_b", 300),
        ("route_b", 500),
    ]
    res = analyse(pairs)
    assert res["p95"]["route_a"] == 500
    assert res["p95"]["route_b"] == 500
    assert res["slowest"] == "route_a"

    # Reversed order in input
    pairs_rev = [
        ("route_b", 300),
        ("route_b", 500),
        ("route_a", 250),
        ("route_a", 500),
    ]
    res_rev = analyse(pairs_rev)
    assert res_rev["slowest"] == "route_b"


def test_input_immutability_and_unsorted():
    """Verify that inputs are not mutated and unsorted values sort properly."""
    original = [("beta", 450), ("alpha", 150), ("beta", 100), ("alpha", 350)]
    copy_input = list(original)

    res = analyse(original)
    assert original == copy_input

    # alpha sorted: [150, 350], n=2 -> rank = ceil(0.95*2)-1 = 1 -> 350
    # beta sorted: [100, 450], n=2 -> rank = 1 -> 450
    assert res["counts"]["alpha"] == 2
    assert res["counts"]["beta"] == 2
    assert res["p95"]["alpha"] == 350
    assert res["p95"]["beta"] == 450
    assert res["slowest"] == "beta"
