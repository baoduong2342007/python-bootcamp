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
| Assistant board | [Lab 2 board](https://github.com/users/tqhuy0602/projects/2), owned by Huy, private | Created after project access was authorized and authenticated; 13 issue cards and Kanban view configured |

The labels and milestone were already present before this work. Only Huy's
missing issues were created. The README now documents W2 official tests
without `--variant`, explicit cross-test filenames, package execution, Ruff,
and dependency/approval gates.

## Board verification after authentication

Initially the CLI lacked `read:project`, and the in-app browser was signed out.
Huy explicitly authorized adding the `project` scope and completed GitHub's
device authentication. The repo had no linked project; Dương's visible project
was unrelated and not writable by Huy. A new Lab 2 board was created under Huy.

The board has Todo → In progress → In review → Done, Component and Size fields,
and a Gate note for historical approval gaps and current dependencies. It
contains all ten Lab 2 issues #6–#15 plus follow-ups #24, #26 and #28. Work in
progress is limited by the stated policy to two cards per person. Closed legacy
issues with remaining review/consensus gates are tracked In review instead of
being treated as fully complete; the original GitHub issue state is unchanged.

After Huy explicitly authorized the four invitations, `baoduong2342007`,
`pqquyenn`, `luongnhatinh` and `simble2k` were granted WRITER access. The board
stays private. GitHub rejects a direct repository link because project and
repository owners differ, so use the board URL above; no repository link is claimed.

AI use: Codex inspected metadata, drafted the README/audit and prepared Git
and PR updates for owner Trần Quốc Huy. No personal study hours, teammate
consensus or LMS deadline were inferred. Board setup and the authorized
collaborator roles were checked against the GitHub API.
