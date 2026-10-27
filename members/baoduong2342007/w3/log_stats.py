"""Summarise request counts and nearest-rank latency percentiles."""

import math
from collections import Counter, defaultdict
from collections.abc import Iterable


def analyse(pairs: Iterable[tuple[str, float]]) -> dict:
    """Return counts, per-route p95, and the first route with maximal p95."""
    grouped: dict[str, list[float]] = defaultdict(list)
    for route, latency in pairs:
        grouped[route].append(latency)
    counts = dict(Counter({route: len(values) for route, values in grouped.items()}))
    p95 = {route: sorted(values)[math.ceil(0.95 * len(values)) - 1] for route, values in grouped.items()}
    return {"counts": counts, "p95": p95, "slowest": max(p95, key=p95.get) if p95 else None}
