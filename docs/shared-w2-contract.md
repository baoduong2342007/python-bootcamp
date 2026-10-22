# Proposed Week 2 shared contract

All planner functions use `shared.contract.Task` and `shared.contract.Block`,
never a personal Task type. This PR is a proposal awaiting four teammate
approvals; no unanimous agreement is asserted yet.

`Task(title: str, importance: int, effort_h: float, deadline: date)` requires
importance in 1–5 and nonnegative effort. `Block(task: Task, hours: float)`
requires nonnegative hours. Invalid ranges raise `ValueError`.
NaN is outside the nonnegative range and raises the same error.

`Block(task, 0)` is intentionally valid for direct construction and rendering.
The constructor does not allocate time or enforce an allocation budget.
`allocate` has a stronger postcondition: every returned block has `hours > 0`,
so zero-effort tasks and nonpositive allocations produce no blocks.

| Owner | Interface | Behavior |
| --- | --- | --- |
| Dương | `parse_csv(path) -> list[Task]` | UTF-8 CSV, ordered tasks; invalid data reports its line; empty input returns `[]`; missing headers report line 1 |
| Huy | `prioritise(tasks, today) -> list[Task]` | Descending importance / max(1, days remaining), stable ties |
| Quyền | `allocate(tasks, hours) -> list[Block]` | Greedy input order, partial last task allowed; nonpositive budget returns `[]`; omit zero-effort tasks and nonpositive blocks |
| Minh | `render(blocks) -> str` | One `<title>: <hours:g> h` per line; empty returns `No tasks.` |
| Bảo | `total_effort(tasks) -> float` | Sum effort; empty returns `0.0` |

Sorting/allocation must preserve input lists and Task attributes. CSV headers
are `title,importance,effort_h,deadline`; dates use ISO format. Missing files
keep `FileNotFoundError`. Every function PR includes its own tests under
`tests/shared_w2/`. Merge function PRs only after this contract is approved
and merged. Minh's existing render branch has a compatible temporary copy;
update that branch after the shared contract merges.

## Scope and merge order

PR #35 proposes the shared types, their tests, this contract, and the CI step
that runs `tests/shared_w2/`. Planner implementations have separate reviews.
The earlier `total_effort` implementation and integration scaffold belong in
[PR #45](https://github.com/baoduong2342007/python-bootcamp/pull/45).
[Parser PR #36](https://github.com/baoduong2342007/python-bootcamp/pull/36)
was already merged into the contract branch before contract approval; its
implementation is removed from this proposal and restored in a separate
follow-up [PR #48](https://github.com/baoduong2342007/python-bootcamp/pull/48).
The original implementation commits remain in Git history.

During this follow-up, [Huy's PR #41](https://github.com/baoduong2342007/python-bootcamp/pull/41)
was merged into the contract branch at `03df6f2`. At Dương's request, its
`prioritise` implementation and eight tests remain included in PR #35. This
does not establish the remaining teammates' contract approval or completion
of the five-function integration.

After all four teammate approvals and passing CI, squash merge the contract
into `main`, following the team's normal PR workflow. Keep the contract branch
until stacked function PRs have been updated. Each function owner then updates
their branch from `main`, uses the canonical contract, retargets the PR to
`main`, checks that its diff contains only the intended function changes, and
obtains the assigned review and passing CI before merging.

The shared CI job also runs for PRs targeting `feat/w2-shared-contract` so
stacked function PRs can be tested while waiting. Passing contract unit tests
does not establish that the five-function integration is complete. Bảo adds
the integration test after the functions merge; a missing module or sample
must fail that final test rather than skip it. A skipped scaffold is not
evidence that the team integration gate passed.

For sample tasks, today `2026-10-26`, and a 2-hour budget: total effort is
7.5, order is Assignment then DS exam, blocks are 1.5 and 0.5 hours. Render:

```text
Assignment: 1.5 h
DS exam: 0.5 h
```

AI assistance: Codex supports writing this contract proposal and its tests,
checking compatibility with Minh's temporary contract, and Git/PR preparation.
The 2026-10-22 follow-up addresses review feedback, separates function work,
rejects NaN effort/hours, and adds shared CI coverage and regression tests.
AI-generated code and documentation are retained. Approval must come from
the actual teammates, not from this document.
