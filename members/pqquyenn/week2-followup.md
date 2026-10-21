# Week 2 — Quyền (`pqquyenn`)

Personal branch: `py/w2-pqquyenn`.
Assigned reviewer: Dương (`baoduong2342007`).
Reviewee for cross-tests and review: Bảo (`simble2k`).
Shared function: `allocate(tasks, hours)` on branch `feat/w2-allocate-pqquyenn`.

## Implemented and checked locally — 2026-10-21

- **W2-1** (`models.py`): dataclass `Task` with `title: str`, `importance: int`, `effort_h: float`, `deadline: date`. Validates importance in range 1–5 (raises `ValueError` otherwise) and non-negative effort. Implements `days_left(today: date) -> int` returning difference in days, bounded at minimum 0 (due today and overdue tasks return 0).
- **W2-2** (`io_utils.py`):
  - `load_tasks(path)` reads UTF-8 CSV via `csv.DictReader`, preserves task order, checks required header columns `title,importance,effort_h,deadline` (raises `ValueError` with `"line 1"` on missing columns), and raises `ValueError` with line number (e.g. `"line 3"`) on corrupted or invalid rows. Empty or header-only files return `[]`.
  - `save_json(tasks, path)` serializes tasks to clean UTF-8 JSON list with ISO formatted dates (`YYYY-MM-DD`).
- **W2-3** (`errors.py`): defines `InfeasiblePlan(Exception)` holding `needed_h` and `available_h` with descriptive string representation. `check_feasible(tasks, available_h)` sums effort and raises `InfeasiblePlan` strictly when `needed_h > available_h`.
- **W2-4** (`tests_for_simble2k.py`): 5 cross-test functions for Member 5 - Bảo (`simble2k`)'s Week 1 solutions:
  1. `test_summary_even_length`: even-length score lists, verifying min, max, mean, and median.
  2. `test_top_k_non_positive_k`: non-positive $k \le 0$ returning `[]`.
  3. `test_missing_single_shortage`: single shortage cases (credits only, GPA only, both).
  4. `test_by_day_preserves_duplicate_courses`: preserves duplicate course occurrences on the same day in sorted order.
  5. `test_unique_preserve_order_contract`: verifies first occurrence preservation and input non-mutation for `unique_preserve_order`.
- **W2-5** (`__main__.py` & `__init__.py`): clean package imports using relative imports, entry point deriving sample path relative to `__file__`, and no execution side effects when imported.
- **Edge tests** (`test_edges.py`): 12 comprehensive unit tests covering boundary importance (1, 5, 0, 6, -1), non-negative and NaN effort, date calculations, corrupted CSV formats, unicode roundtrip in JSON, and feasibility checks.

## Local verification commands

```bash
# Official Week 2 tests (tested against pending PR #29 samples/tests)
python -m pytest -q tests/test_w2.py --member pqquyenn

# Edge tests and cross-tests
python -m pytest -q members/pqquyenn/w2/test_edges.py
python -m pytest -q members/pqquyenn/w2/tests_for_simble2k.py

# Package run
python -m members.pqquyenn.w2

# Week 1 regression
python -m pytest -q tests/test_w1.py --member pqquyenn --variant 3

# Ruff linting
python -m ruff check members/pqquyenn/w2
```

Results: All tests passed with 0 failures, 0 skips, and clean Ruff output.

## AI assistance

Trợ lý AI Antigravity đã hỗ trợ triển khai cấu trúc mã tuần 2 cho `pqquyenn`, viết bộ test biên (edge tests), kiểm thử chéo W2-4 cho `simble2k`, cập nhật cấu hình CI W2 và tài liệu theo kế hoạch nhóm `plan (3).md`. Toàn bộ mã nguồn đã được chạy kiểm tra thực tế trên môi trường máy cá nhân.
