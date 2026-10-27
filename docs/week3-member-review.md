# Week 3 member review snapshot — 2026-10-27

This is a local review snapshot of the named PR heads, not approval or a merge.
GitHub may change afterward. Codex performed the checks for Dương.

- Huy: [PR56](https://github.com/baoduong2342007/python-boostcamp/pull/56)
  open at `bc1035c`; instructor plus additional W3 tests: 45 passed locally.
  GitHub reports W3 Python 3.10/3.12 success. Actual peer approval remains to be checked.
- Minh: [PR58](https://github.com/baoduong2342007/python-boostcamp/pull/58)
  open at `1c9e4ec`; instructor plus additional W3 tests: 18 passed locally and
  GitHub reports W3 Python 3.10/3.12 success. Two input cases need attention:
  `--hours nan` exits 0 and allocates 7.5 hours, and a CSV row with effort -1
  reaches shared Task validation outside the error handler and prints a traceback.
  Add finite-hours validation and handle invalid model conversion with tests.
- Huy's shared E2E [PR57](https://github.com/baoduong2342007/python-boostcamp/pull/57)
  is draft at `b6031bc`, dependent on the shared CLI. Its 16 existing tests passed
  locally when run against Dương's separate CLI branch `feat/w3-shared-planner`
  commit `88baffb`; this is not a merged dependency or PR57 CI run.
- No W3 PR for Quyền or Bảo appeared in the GitHub pull request list at this check;
  this is not evidence that they have done no work outside the repository.
- Shared core classroom contributions are documented in the assistant repository's
  `docs/submissions/week3.md`; Huy's H1 PR21 and Bảo's rule-ID PR17 are merged,
  but each member's H1 report, review and three actual improvements require separate
  verification. Existing H3 files alone do not confirm personal reading.

Release tags require the plan's peer review, CI, fresh-clone checks and all member
contributions. The existing assistant tag points to an earlier commit; neither
release is represented as complete by this snapshot.
