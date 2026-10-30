"""Performance analysis module for computing route request counts and p95 latencies."""

import math
from collections import defaultdict
from collections.abc import Iterable
from typing import Any


def analyse(pairs: Iterable[tuple[str, float | int]]) -> dict[str, Any]:
    """Compute request counts, p95 latencies per route, and the slowest route.

    Percentile calculation follows the nearest-rank convention:
        rank = ceil(0.95 * n) - 1
    applied to an independently sorted list of latencies for each route.

    Tie-breaking: If multiple routes tie for the maximum p95 latency,
    the route that appeared first in the input stream is selected.

    Empty input handling: If pairs is empty, returns empty mappings for
    'counts' and 'p95', and None for 'slowest'.

    Args:
        pairs: Iterable of (route_name, latency) pairs.

    Returns:
        Dict with keys:
            - 'counts': dict mapping route name to integer request count.
            - 'p95': dict mapping route name to its 95th percentile latency.
            - 'slowest': route name with the highest p95 latency, or None.
    """
    if pairs is None:
        return {"counts": {}, "p95": {}, "slowest": None}

    order: list[str] = []
    by_route: dict[str, list[float | int]] = defaultdict(list)

    for route, latency in pairs:
        if route not in by_route:
            order.append(route)
        by_route[route].append(latency)

    if not order:
        return {"counts": {}, "p95": {}, "slowest": None}

    counts: dict[str, int] = {}
    p95: dict[str, float | int] = {}

    for route in order:
        latencies = sorted(by_route[route])
        n = len(latencies)
        rank = math.ceil(0.95 * n) - 1
        counts[route] = n
        p95[route] = latencies[rank]

    max_p95: float | int = -float("inf")
    slowest_route: str | None = None

    for route in order:
        val = p95[route]
        if val > max_p95:
            max_p95 = val
            slowest_route = route

    return {
        "counts": counts,
        "p95": p95,
        "slowest": slowest_route,
    }
