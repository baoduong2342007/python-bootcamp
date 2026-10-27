# Week 3 — Lương Nhật Minh (`luongnhatinh`)

Personal Issue: [#52](https://github.com/baoduong2342007/python-bootcamp/issues/52)  
Branch: `py/w3-luongnhatinh`  
Assigned Reviewer: Bảo (`simble2k`)

---

## 1. Implemented Components

- **W3-1 (`dates.py`)**:
  - `parse_due(text, today) -> date`: Handles ISO `YYYY-MM-DD`, `tomorrow`, `in N days`, and weekday names (e.g. `Fri`, `Tue`).
  - Next occurrence convention: Weekdays strictly resolve to future dates (`days_ahead > 0`); matching the same weekday targets +7 days.
  - Invalid formats or date overflows cleanly raise `ValueError`.
- **W3-2 (`log_stats.py`)**:
  - `analyse(pairs) -> dict`: Computes request counts per route, 95th percentile latency using the nearest-rank method (`ceil(0.95 * n) - 1`), and identifies the slowest route.
  - Tie-breaking: In case of equal maximum p95 latencies, the route encountered first in the input wins.
  - Empty input returns `{"counts": {}, "p95": {}, "slowest": None}` without mutating input lists.
- **W3-3 (`cli.py`)**:
  - Command-line interface built with `argparse` reading a tasks CSV, `--hours`, and `--today`.
  - Converts personal `members.luongnhatinh.w2.models.Task` to `shared.contract.Task` at the boundary.
  - Reuses shared `prioritise`, `allocate`, and `render`.
  - Handles missing files, invalid dates, and non-positive hours gracefully with informative `stderr` messages and non-zero exit codes.
- **W3-4 (Clean code & type annotations)**:
  - Full type annotations and PEP 257 docstrings for all functions in W1–W3.
  - Ruff lint clean across all rules (E, F, I, B, UP, BLE).

---

## 2. Python vs C++ Observations (Three Reflections)

1. **Date Arithmetic vs `std::chrono`**:
   Python's `datetime.date` and `timedelta` automatically manage calendar transitions and raise `OverflowError` if dates exceed the valid year range (1..9999). In C++20 `std::chrono`, calendar types such as `year_month_day` do not validate boundaries implicitly; developers must manually invoke `.ok()` before converting to time points (`sys_days`).
2. **Immutable vs In-Place Sorting**:
   In Python, `sorted(iterable)` allocates and returns a new list, ensuring that calculating percentiles in `log_stats.py` does not mutate caller data. In C++, `std::sort` mutates the range in-place; achieving identical isolation requires an explicit copy (`std::vector<int> copy = vec; std::sort(copy.begin(), copy.end());`).
3. **Data Transfer Objects and Typing**:
   In Python, separate `@dataclass` types (`personal Task` vs `shared Task`) are structurally distinct; runtime boundary conversion guarantees contract safety. Python type annotations serve as static hints, whereas C++ enforces strict static typing at compile time, eliminating runtime type conversions between layout-equivalent structs if templated or aliased.

---

## 3. Verification Commands & Results

Run from the repository root:
```bash
python -m pytest -q tests/test_w3.py --member luongnhatinh
python -m pytest -q members/luongnhatinh/w3/tests
python -m pytest -q tests/test_w1.py --member luongnhatinh --variant 4
python -m pytest -q tests/test_w2.py members/luongnhatinh/w2 --member luongnhatinh
python -m pytest -q tests/shared_w2
python -m ruff check members/luongnhatinh --select E,F,I,B,UP,BLE --line-length 120
python -m ruff format --check members/luongnhatinh/w3
```

### Local Test Output:
- Official W3 tests: **3 passed, 0 skips**.
- Minh additional W3 tests: **13 passed**.
- Minh W1 regression: **5 passed**.
- Minh W2 regression: **27 passed**.
- Shared W2 regression: **51 passed**.
- Ruff checks: **All checks passed!**

---

## 4. AI Use Disclosure

AI coding assistant (Antigravity AI) was utilized for scaffolding regex patterns in `dates.py`, nearest-rank index calculations, and boundary test fixtures. All generated code was manually inspected, type-checked, and verified against edge cases.

### Review fixes — 2026-10-27

At Dương's request, Codex fixed the W3 CLI to reject non-finite hour budgets
and to report invalid shared-task effort (negative or non-finite) without a
traceback. Codex added subprocess regression tests. Minh should review and
confirm these changes; this entry does not claim that he authored the fixes.
