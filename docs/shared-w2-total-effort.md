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
- `python -m pytest -q tests/shared_w2/` (15 passed, no skips, including 9 contract cases)
- `python -m ruff check shared/ tests/shared_w2/` (All checks passed!)

The implementation and its six tests are retained from commit `ad85ecd`.
They were removed from contract PR #35 to keep contract consensus separate
from function review, then restored here without rewriting the original
history. The earlier integration scaffold remains in that history; it is
excluded from this PR because the final five-function integration test belongs
after the other functions merge. No skipped scaffold counts as passing it.

AI assistance: Antigravity/Codex assisted in implementing `total_effort`,
generating edge tests and the earlier integration scaffold, verifying Ruff
styling, preparing documentation, and separating this function from PR #35.
Retained code and docs are disclosed per course policy; no new independent
authorship or teammate approval is asserted.
