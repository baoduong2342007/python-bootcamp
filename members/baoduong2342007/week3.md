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
f30c605c6ff376ac448ddb00fa82ae36347e29a9. Dương must review and explain the work;
peer review, PR/issue links, actual hours, three self-written Python/C++ comparison
lines, and merge remain pending. This file does not assert those actions happened.
