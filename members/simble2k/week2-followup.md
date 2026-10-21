# Week 2 — Bảo (`simble2k`)

Personal issue: [#43](https://github.com/baoduong2342007/python-bootcamp/issues/43).
Personal PR: [#44](https://github.com/baoduong2342007/python-bootcamp/pull/44).
Team function PR: [#45](https://github.com/baoduong2342007/python-bootcamp/pull/45).
Shared function branch: `feat/w2-total-effort`.
Assigned reviewer for personal PR: Quyền (`pqquyenn`).
Reviewee for cross-tests and review: Huy (`tqhuy0602`).

## Implemented and checked locally — 2026-10-21

- **W2-1** (`models.py`): dataclass `Task`, importance validation (1..5), non-negative effort, `days_left(today)` with 0 minimum (past due and due today return 0).
- **W2-2** (`io_utils.py`): `load_tasks` reads UTF-8 CSV with `csv.DictReader`, preserves row order, checks required header columns (raises `ValueError` on line 1 if missing), and reports accurate 1-indexed line numbers on invalid rows (such as line 3 on `tasks_bad.csv`). `save_json` exports list of tasks to UTF-8 JSON with ISO formatted deadlines.
- **W2-3** (`errors.py`): `InfeasiblePlan` custom exception retaining `needed_h` and `available_h`, with human-readable message. `check_feasible` raises exception strictly when `needed_h > available_h`.
- **W2-4** (`tests_for_tqhuy0602.py`): 5 thorough unit tests for Huy's Week 1 exercises covering even-element score summary, non-positive k top words, single requirement shortages, duplicate course grouping in timetable, and in-place insertion sorting with duplicate elements.
- **W2-5** (`__main__.py` & `__init__.py`): clean package imports using relative paths, entry point resolving sample path relative to `__file__`, and no execution side effects when imported.
- **Edge tests** (`test_edges.py`): 12 comprehensive test functions covering all boundary conditions, non-existent files, empty files, and roundtrip JSON integrity.

## Local verification commands

```bash
# Official Week 2 tests
python -m pytest -q tests/test_w2.py --member simble2k

# Edge and cross tests
python -m pytest -q members/simble2k/w2/test_edges.py
python -m pytest -q members/simble2k/w2/tests_for_tqhuy0602.py

# Package run
python -m members.simble2k.w2

# Week 1 regression
python -m pytest -q tests/test_w1.py --member simble2k -k "not test_w1_4"
python -m pytest -q tests/test_w1_extra.py --member simble2k

# Ruff linting
python -m ruff check members/simble2k/w2
```

Results: All tests passed with 0 failures, 0 skips, and clean Ruff output.

## AI assistance

AI assistant (Antigravity/Codex) was utilized to structure the Week 2 modules according to the shared team plan, write edge test suites, run local validation, and format Git documentation. All code was reviewed and validated locally.
