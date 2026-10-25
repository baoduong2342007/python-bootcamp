"""Compute route counts and nearest-rank latency percentiles."""

from collections import Counter, defaultdict
from collections.abc import Iterable
from math import isfinite
from typing import TypedDict


class LogStats(TypedDict):
    """Per-route counts/p95, and the first route with the largest p95."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: Iterable[tuple[str, float]]) -> LogStats:
    """Group nonnegative finite latencies without mutating input.

    Use nearest-rank p95, ceil(0.95*n)-1; ties for slowest retain the first
    encountered route. Empty input returns empty mappings and slowest=None.
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = defaultdict(list)
    for route, latency in pairs:
        if not isfinite(latency) or latency < 0:
            raise ValueError("latency must be finite and non-negative")
        counts[route] += 1
        latencies[route].append(latency)
    # Integer arithmetic gives ceil(95*n/100), including exact boundaries.
    p95 = {
        route: sorted(values)[(95 * len(values) + 99) // 100 - 1]
        for route, values in latencies.items()
    }
    return {
        "counts": dict(counts),
        "p95": p95,
        "slowest": max(p95, key=p95.get) if p95 else None,
    }
