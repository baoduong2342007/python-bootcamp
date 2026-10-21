# Proposed Week 2 shared contract

All planner functions use `shared.contract.Task` and `shared.contract.Block`,
never a personal Task type. This PR is a proposal awaiting four teammate
approvals; no unanimous agreement is asserted yet.

`Task(title: str, importance: int, effort_h: float, deadline: date)` requires
importance in 1–5 and nonnegative effort. `Block(task: Task, hours: float)`
requires nonnegative hours. Invalid ranges raise `ValueError`.

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

For sample tasks, today `2026-10-26`, and a 2-hour budget: total effort is
7.5, order is Assignment then DS exam, blocks are 1.5 and 0.5 hours. Render:

```text
Assignment: 1.5 h
DS exam: 0.5 h
```

AI assistance: Codex supports writing this contract proposal and its tests,
checking compatibility with Minh's temporary contract, and Git/PR preparation.
AI-generated code and documentation are retained. Approval must come from
the actual teammates, not from this document.
