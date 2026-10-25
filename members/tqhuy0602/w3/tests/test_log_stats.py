"""Percentile, input ownership and deterministic tie rules."""

import pytest

from members.tqhuy0602.w3.log_stats import analyse


def test_empty_stats():
    assert analyse([]) == {"counts": {}, "p95": {}, "slowest": None}


def test_single_observation():
    assert analyse([("fee", 100)]) == {
        "counts": {"fee": 1},
        "p95": {"fee": 100},
        "slowest": "fee",
    }


def test_twenty_observations_nearest_rank_and_no_mutation():
    pairs = [("fee", value) for value in range(20, 0, -1)]
    original = pairs.copy()
    assert analyse(pairs)["p95"] == {"fee": 19}
    assert pairs == original


def test_ties_keep_first_route_and_iterable_input_is_supported():
    stats = analyse(iter([("office", 10), ("fee", 10), ("office", 1), ("rule", 9)]))
    assert stats == {
        "counts": {"office": 2, "fee": 1, "rule": 1},
        "p95": {"office": 10, "fee": 10, "rule": 9},
        "slowest": "office",
    }


@pytest.mark.parametrize("latency", [-1, float("nan"), float("inf"), float("-inf")])
def test_invalid_latencies(latency):
    with pytest.raises(ValueError, match="finite and non-negative"):
        analyse([("fee", latency)])
