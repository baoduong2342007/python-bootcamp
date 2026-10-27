"""Router log performance analysis and p95 latency calculation."""

from collections import defaultdict
import math
from typing import Any


def analyse(pairs: list[tuple[str, int]]) -> dict[str, Any]:
    """Analyse request logs to compute request counts, p95 latencies, and identify the slowest route.

    Percentile calculation uses the nearest-rank method:
        index = ceil(0.95 * n) - 1
    on a sorted list of latencies.

    If multiple routes tie for the highest p95 latency, the route that appeared
    first in the input data is selected as the slowest.

    Args:
        pairs: List of (route_name, latency_ms) tuples.

    Returns:
        Dict with keys:
            - 'counts': dict mapping route name to total request count.
            - 'p95': dict mapping route name to its 95th percentile latency.
            - 'slowest': route name with the highest p95, or None if input is empty.
    """
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}

    order: list[str] = []
    by_route: dict[str, list[int]] = defaultdict(list)

    for route, latency in pairs:
        if route not in by_route:
            order.append(route)
        by_route[route].append(latency)

    counts: dict[str, int] = {}
    p95: dict[str, int] = {}

    for route in order:
        latencies = sorted(by_route[route])
        n = len(latencies)
        rank = math.ceil(0.95 * n) - 1
        counts[route] = n
        p95[route] = latencies[rank]

    # Find the slowest route with tie-breaking based on first occurrence
    highest_p95 = -1
    slowest_route: str | None = None

    for route in order:
        route_p95 = p95[route]
        if route_p95 > highest_p95:
            highest_p95 = route_p95
            slowest_route = route

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest_route,
    }
