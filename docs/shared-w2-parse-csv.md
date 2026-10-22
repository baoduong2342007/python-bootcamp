# Dương's shared CSV parser

Import with `from shared.parse_csv import parse_csv`. This function returns
`shared.contract.Task`, preserves input order, uses UTF-8 and reports invalid
data with the CSV line number. The shared contract also rejects negative
and NaN effort. Empty files/header-only files return `[]`; missing files retain
`FileNotFoundError`. No personal module is imported.

PR #48 initially targeted `feat/w2-shared-contract` to isolate the parser
diff. It was then merged into that branch on 2026-10-22 at `29c9020`, before
contract consensus. The parser is now included in PR #35, which still requires
all four teammate approvals and passing CI before reaching `main`. Minh is
the assigned parser reviewer; merging into the contract branch does not
establish the remaining contract approvals.

This follow-up retains the parser and tests from PR #36, which was already
merged into the contract branch before contract consensus. PR #35's scope
correction separated the parser for independent review; the subsequent merge
of #48 brought it back into the proposal. Original commits and the earlier
review remain in history; they do not establish renewed contract approval.

Verification: `python -m pytest -q tests/shared_w2/` (23 passed, no skips:
14 parser cases plus 9 contract cases), whole-repository Ruff passed.
The fixtures here are independent test data; official samples remain in
Minh's PR #29. Team integration and release tag remain pending.

AI assistance: Codex supports parser implementation, test generation,
verification, documentation and Git/PR preparation. The generated parser,
tests and documentation are retained and disclosed.
