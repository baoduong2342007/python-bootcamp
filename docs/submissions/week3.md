# Week 3 submission evidence — work in progress

This is an evidence index, not a declaration that Week 3 is complete. Recheck links, reviews, CI and commit IDs before submission or creating `py-w3-done`.

- Repository: https://github.com/baoduong2342007/python-bootcamp
- Assistant repository index: https://github.com/baoduong2342007/assistant_core_lab/blob/main/docs/submissions/week3.md
- Individual tracking: [Week 3 tracking](../w3-tracking.md) and [PROGRESS](../../PROGRESS.md). Some historical entries may be stale; use live issue and PR links below for status.

| Member | W3 issue | PR / status at verification |
| --- | --- | --- |
| Dương | [#49](https://github.com/baoduong2342007/python-bootcamp/issues/49) | [#60](https://github.com/baoduong2342007/python-bootcamp/pull/60) merged; peer review and personal evidence still pending per issue |
| Huy | [#50](https://github.com/baoduong2342007/python-bootcamp/issues/50) | [#56](https://github.com/baoduong2342007/python-bootcamp/pull/56) merged; consult PR for review and CI |
| Quyền | [#51](https://github.com/baoduong2342007/python-bootcamp/issues/51) | [#63](https://github.com/baoduong2342007/python-bootcamp/pull/63) open; review and merge pending |
| Minh | [#52](https://github.com/baoduong2342007/python-bootcamp/issues/52) | Check issue and repository for final PR and review evidence |
| Bảo | [#53](https://github.com/baoduong2342007/python-bootcamp/issues/53) | [#62](https://github.com/baoduong2342007/python-bootcamp/pull/62) merged; consult PR for review and CI |

Shared planner: [#54](https://github.com/baoduong2342007/python-bootcamp/issues/54) is open; implementation [#59](https://github.com/baoduong2342007/python-bootcamp/pull/59), E2E [#57](https://github.com/baoduong2342007/python-bootcamp/pull/57), and E2E CI [#61](https://github.com/baoduong2342007/python-bootcamp/pull/61) merged. Confirm outstanding review and ownership evidence in #54.

## Fresh checkout observation — 2026-10-30

Codex cloned the GitHub default branch on Windows and tested commit `aa9f845dbe2fd21b0fb6214750a6ee9082c4b234` with an existing system Python 3.13 and pytest installation. This is a fresh checkout, **not** a clean environment or the required independent teammate fresh-clone sign-off.

- `py -3.13 -m pytest -q tests_team`: 16 passed.
- `py -3.13 -m pytest -q tests/test_w3.py --member <username>`: 3 passed each for `baoduong2342007`, `tqhuy0602`, `luongnhatinh`, and `simble2k`.
- The same command for `pqquyenn`: 3 failed because the W3 modules are not on main. PR #63 contains them and remains open.

Separately, the PR #63 head `b9ad33bc51c5d70ad9c97b8fa7bfbb014b64be3f` was tested by Codex from an extracted snapshot with the existing Python 3.13 environment: official tests 3 passed; `members/pqquyenn/w3/tests` 17 passed; sample CLI printed Assignment 1.5 h then DS exam 0.5 h. This is not evidence that the code was merged.

Before release, obtain the missing owner and peer evidence, merge accepted changes, repeat all five official tests and individual/shared regressions in a clean independent clone at the final commit, link the relevant CI run, and record the result without inventing hours or approvals.
