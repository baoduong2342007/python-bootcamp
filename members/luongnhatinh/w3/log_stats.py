"""Log statistics analysis utilities."""

import math
from collections import Counter


def analyse(pairs: list[tuple[str, int]]) -> dict:
    """Analyze route latencies and compute counts, p95 latencies, and identify the slowest route.

    Percentile calculation:
        Uses the nearest-rank method: index = ceil(0.95 * n) - 1 on sorted latencies.

    Tie-breaking:
        In case of equal maximum p95 values, the route encountered earliest in pairs wins.

    Returns:
        A dict with:
        - 'counts': dict[str, int]
        - 'p95': dict[str, int]
        - 'slowest': str | None
    """
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    # Track route counts and collect latencies per route without mutating input
    counts_counter: Counter[str] = Counter()
    latencies_by_route: dict[str, list[int]] = {}
    first_seen: list[str] = []

    for route, latency in pairs:
        counts_counter[route] += 1
        if route not in latencies_by_route:
            latencies_by_route[route] = []
            first_seen.append(route)
        latencies_by_route[route].append(latency)

    p95_by_route: dict[str, int] = {}
    for route in first_seen:
        sorted_vals = sorted(latencies_by_route[route])
        n = len(sorted_vals)
        rank_idx = math.ceil(0.95 * n) - 1
        p95_by_route[route] = sorted_vals[rank_idx]

    # Find slowest route (largest p95 latency, first-seen breaks ties)
    slowest_route: str | None = None
    max_p95 = -1
    for route in first_seen:
        val = p95_by_route[route]
        if val > max_p95:
            max_p95 = val
            slowest_route = route

    return {
        "counts": dict(counts_counter),
        "p95": p95_by_route,
        "slowest": slowest_route,
    }
