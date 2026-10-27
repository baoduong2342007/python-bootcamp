# Dương — Week 3 working notes

The W3 implementation uses the W2 CSV loader and converts tasks into the shared
planner model at the boundary. `parse_due` accepts ISO dates, tomorrow, `in N days`,
and the next occurrence of a three-letter weekday; surrounding whitespace and
letter case are ignored. `analyse` uses nearest-rank p95, preserves the first route
on ties, and returns empty mappings/None for no input.

Run from the repository root:

```sh
python -m pytest -q tests/test_w3.py --member baoduong2342007
python -m pytest -q members/baoduong2342007/w3/tests
python -m members.baoduong2342007.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
```

Codex generated the implementation, tests and W1/W2 annotations and lint fixes at
Dương's request. The official test file is copied from public_materials commit
f30c605c6ff376ac448ddb00fa82ae36347e29a9. The work was merged in [PR #60](https://github.com/baoduong2342007/python-bootcamp/pull/60),
linked to [issue #49](https://github.com/baoduong2342007/python-bootcamp/issues/49).
Dương must review and explain the work; peer review, actual hours and three
self-written Python/C++ comparison lines remain pending. No personal actions are
inferred by this note.


## Verification on main, 2026-10-27

At main commit `6dff1c1`, Codex ran the official W3 tests and personal W3
boundary tests: 6 passed; W1/W2 and W2 edge regression: 31 passed; shared
planner E2E: 16 passed. Ruff 0.17.3 passed across the repository. These are
local Python 3.12 results, not a fresh-clone or peer-review claim.

Possible points for Dương to consider and write in his own words: Python's
`datetime` handles calendar arithmetic; `sorted` creates a new list whereas
C++ `std::sort` modifies a range; Python type hints do not enforce runtime
validation as C++ static types do. These suggestions are AI-generated, not
self-written reflection.
