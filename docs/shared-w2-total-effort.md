# Bảo's shared total_effort calculator

Import with `from shared.total_effort import total_effort` or `from shared.study_planner import total_effort`.
This function computes the sum of `effort_h` for a given sequence of `shared.contract.Task` objects.
It returns `0.0` (as a float) for an empty task sequence, preserves input sequences and task objects
without mutation, and does not import from any personal member folder.

This branch depends on `feat/w2-shared-contract`; its PR targets that branch to isolate the `total_effort` diff.
Merge the contract after team consensus, then retarget this PR to `main` before merge.
Quyền (`pqquyenn`) is the assigned reviewer.

Verification:
- `python -m pytest -q tests/shared_w2/test_total_effort.py` (6 passed)
- `python -m ruff check shared/ tests/shared_w2/` (All checks passed!)

AI assistance: Antigravity/Codex assisted in implementing `total_effort`, generating edge tests and integration test scaffolding, verifying Ruff styling, and preparing documentation. All generated code and docs are retained and disclosed per course policy.
