# Dương's shared CSV parser

Import with `from shared.parse_csv import parse_csv`. This function returns
`shared.contract.Task`, preserves input order, uses UTF-8 and reports invalid
data with the CSV line number. The shared contract also rejects negative
and NaN effort. Empty files/header-only files return `[]`; missing files retain
`FileNotFoundError`. No personal module is imported.

This branch depends on `feat/w2-shared-contract`; its PR initially targets
that branch to isolate the parser diff. Merge the contract after all four
teammates approve, then retarget this parser PR to `main` and update it before
merge. Minh is the assigned reviewer. Do not merge until approval and checks.

This follow-up retains the parser and tests from PR #36, which was already
merged into the contract branch before contract consensus. PR #35 now
excludes function implementations; this separate PR restores the parser for
the correct merge order. Original commits and the earlier review remain in
history; they do not establish approval of this updated PR.

Verification: `python -m pytest -q tests/shared_w2/` (23 passed, no skips:
14 parser cases plus 9 contract cases), whole-repository Ruff passed.
The fixtures here are independent test data; official samples remain in
Minh's PR #29. Team integration and release tag remain pending.

AI assistance: Codex supports parser implementation, test generation,
verification, documentation and Git/PR preparation. The generated parser,
tests and documentation are retained and disclosed.
