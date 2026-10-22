# Supplemental review notes for Bảo's Week 1 PR #15 / #21

Prepared by Quyền (`pqquyenn`) for teammate Bảo (`simble2k`) on 2026-10-21. Target PRs: [#15](https://github.com/baoduong2342007/python-bootcamp/pull/15), [#21](https://github.com/baoduong2342007/python-bootcamp/pull/21).

## Validation performed

- Ran instructor tests: `python -m pytest -q tests/test_w1.py --member simble2k -k "not test_w1_4"`: 4 passed.
- Ran extra test: `python -m pytest -q tests/test_w1_extra.py --member simble2k`: 1 passed.
- Ran cross-tests written by Quyền in `members/pqquyenn/w2/tests_for_simble2k.py`: 5 passed.
- Ran Ruff linter: `python -m ruff check members/simble2k/w1`: all checks passed cleanly.
- Verified uniqueness, preservation of first occurrences, and input non-mutation for `unique_preserve_order`.

## Question

In `translate.py`, the `unique_preserve_order` function takes `items: list[int]` and maintains an internal `seen: set[int] = set()` to perform $O(1)$ membership checks. Did you consider how the behavior or type annotations would adapt if the input contained arbitrary hashable items (`Sequence[T]`), or did you intentionally constrain it to `list[int]` to directly mirror the C++ `std::vector<int>` specification?

## Suggestion

In `timetable.py`, `by_day` groups courses by day using `grouped.setdefault(day, []).append(course)`. While `setdefault` is standard and concise, using `collections.defaultdict(list)` could make the grouping idiom slightly cleaner and avoid creating a new empty list instance on every lookup in larger data loops.

## Praise

1. `unique_preserve_order` in `translate.py` contains a remarkably thorough and insightful docstring explaining the differences between C++ container management (`std::vector` + `std::unordered_set`, `const` references) and Python's dynamic object model and garbage collection.
2. The implementation of `unique_preserve_order` guarantees immutability of the caller's input list and correctly retains original order of first appearances without modification.
3. `top_k` in `text_tools.py` handles word ranking elegantly with multi-key sorting `(-item[1], item[0])`, properly resolving frequency ties in alphabetical order and returning `[]` when $k \le 0$.
4. All five modules adhere strictly to PEP 8 standards and pass Ruff linting with zero issues.
