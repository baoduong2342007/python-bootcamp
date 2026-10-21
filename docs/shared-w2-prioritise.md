# Huy's shared prioritise function

Use `from shared.prioritise import prioritise` with `shared.contract.Task`.
The implementation is in `shared/study_planner/prioritise.py`.

`prioritise(tasks, today)` returns a new list sorted by descending
`importance / max(1, (deadline - today).days)`. Due and overdue tasks use a
denominator of one; ties retain the original order. Task objects are preserved
by identity, including repeated references, and neither task fields nor input
ordering are mutated. `today` is explicit, so results are reproducible.

The fixed sample at `2026-10-26` ranks Assignment (4 / 1) above DS exam (5 / 4).

```bash
python -m pytest -q tests/shared_w2/test_prioritise.py
python -m ruff check shared/prioritise.py shared/study_planner/prioritise.py tests/shared_w2/test_prioritise.py
```

This branch is stacked on shared contract PR #35. Its PR targets the contract
branch to isolate Huy's changes; merge the contract only after the required
team approvals, then retarget this PR to `main`. Assigned reviewer: Bảo
(`simble2k`). No contract consensus or human approval is claimed by this file.

AI use: Codex implemented the retained prioritise code and tests and assisted
verification, documentation and Git/PR preparation for owner Trần Quốc Huy.
