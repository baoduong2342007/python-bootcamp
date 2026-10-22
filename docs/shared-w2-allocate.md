# Quyền's shared allocate function

Import with `from shared.allocate import allocate` or `from shared.study_planner import allocate`.
This function greedily allocates available study hours across a sequence of `shared.contract.Task` objects, returning a list of `shared.contract.Block` objects.

## Behavior & Invariants

- Returns `[]` if available hours $\le 0$ or if the task sequence is empty.
- Traverses tasks in the received order without reordering or mutating them.
- Allocates up to `task.effort_h` per task, allowing partial allocation of the last feasible task.
- Tasks with `effort_h <= 0` do not produce a block.
- Never creates blocks with 0 or negative hours.
- Total allocated hours never exceeds the available budget.
- Does not import from any personal member folder.

## Verification

- `python -m pytest -q tests/shared_w2/test_allocate.py` (all tests passed)
- `python -m pytest -q tests/shared_w2` (all shared tests passed)
- `python -m ruff check shared/ tests/shared_w2/` (All checks passed!)

## AI assistance

Trợ lý AI Antigravity hỗ trợ triển khai hàm `allocate`, xây dựng bộ unit tests, kiểm tra định dạng Ruff và soạn thảo tài liệu theo đúng kế hoạch nhóm `plan (3).md`.
