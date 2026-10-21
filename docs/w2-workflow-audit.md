# Week 2 workflow audit — Trần Quốc Huy

Snapshot: 2026-10-21, checked using GitHub CLI. This is a record of observed
metadata, not a claim that all submissions or Lab 2 are complete.

| Item | Observed result | Action |
| --- | --- | --- |
| Bootcamp milestone `PY-W2` | Exists, milestone 2, no due date | Reused; no duplicate created |
| Bootcamp labels `python-hw`, `w2`, `team-hw` | All exist | Reused for Huy's issues #37, #38 and #39 |
| Bootcamp PR template | `.github/PULL_REQUEST_TEMPLATE.md` exists | Reused, unchanged |
| Official W2 test/sample import | PR #29 open when work began | Dependency documented; original tests temporarily used unchanged for local verification |
| Shared contract | PR #35 awaiting required team approvals | Function PRs must wait before merge |
| W2 CI | Existing main workflow covers W1/Ruff | W2 expansion remains Quyền's task; W1 success is not W2 evidence |
| Deadline | No verified LMS date supplied; milestone due date is unset | Keep unset; Dương verifies the official date |
| Assistant board | `gh project list --owner baoduong2342007` reports missing `read:project` scope | Board existence/configuration not verified through this token; no duplicate project created |

The labels and milestone were already present before this work. Only Huy's
missing issues were created. The README now documents W2 official tests
without `--variant`, explicit cross-test filenames, package execution, Ruff,
and dependency/approval gates.

## Board work still requiring project access

Locate the existing Assistant board before creating one. Required states:
Todo → In progress → In review → Done; fields: Component and Size. Add the ten
Lab 2 issues #6–#15 and the remaining follow-up issues. Closed legacy issues
must retain any missing pre-merge approval evidence as a separate follow-up;
closing an issue alone does not establish every DoD condition.

Project access must first be available through a suitably scoped token or an
authenticated browser with the owner's project permissions. This audit does
not claim that the board was inspected, created or updated.

AI use: Codex inspected metadata, drafted the README/audit and prepared Git
and PR updates for owner Trần Quốc Huy. No personal study hours, teammate
consensus, board completion or LMS deadline were inferred.
