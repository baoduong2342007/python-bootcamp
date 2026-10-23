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

PR #41 was merged into the shared contract branch on 2026-10-22 at `03df6f2`,
and subsequently merged into `main` via contract PR #35 (`9624c2e`). All 8 prioritise
tests pass, fulfilling all acceptance criteria of issue #38. The assigned reviewer
for the original function PR was Bảo (`simble2k`).

AI use: Codex implemented the retained prioritise code and tests and assisted
verification, documentation and Git/PR preparation for owner Trần Quốc Huy.
Antigravity updated the completion and closeout status on main.
