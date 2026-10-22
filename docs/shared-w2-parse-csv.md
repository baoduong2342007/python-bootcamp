# Dương's shared CSV parser

Import with `from shared.parse_csv import parse_csv`. This function returns
`shared.contract.Task`, preserves input order, uses UTF-8 and reports invalid
data with the CSV line number. The shared contract also rejects negative
effort. Empty files/header-only files return `[]`; missing files retain
`FileNotFoundError`. No personal module is imported.

This branch depends on `feat/w2-shared-contract`; its PR initially targets
that branch to isolate the parser diff. Merge the contract after all four
teammates approve, then retarget this parser PR to `main` and update it before
merge. Minh is the assigned reviewer. Do not merge until approval and checks.

Verification: `python -m pytest -q tests/shared_w2/` (20 passed), Ruff passed.
The fixtures here are independent test data; official samples remain in
Minh's PR #29. Team integration and release tag remain pending.

AI assistance: Codex supports parser implementation, test generation,
verification, documentation and Git/PR preparation. The generated parser,
tests and documentation are retained and disclosed.
