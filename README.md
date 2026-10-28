# Python Bootcamp - Team03

This repository contains Team03's Python exercises for **CSC10014 - Computational Thinking**, covering Weeks 1, 2, and 3. The team builds on its C++ background to learn Python while practicing collaboration with Git and GitHub.

## Topics

| Week | Topics |
| --- | --- |
| W1 | Syntax, data types, conditionals, loops, functions, strings, and basic data structures |
| W2 | Modules, file handling, CSV/JSON, exceptions, classes, dataclasses, and pytest |
| W3 | The standard library, type hints, argparse, Ruff, and study planner integration |

## Team Members

| Member | Name | GitHub / Personal Folder |
| --- | --- | --- |
| 1 | Trương Quang Bảo Dương | [baoduong2342007](https://github.com/baoduong2342007) |
| 2 | Trần Quốc Huy | [tqhuy0602](https://github.com/tqhuy0602) |
| 3 | Phan Quỳnh Quyền | [pqquyenn](https://github.com/pqquyenn) |
| 4 | Lương Nhật Minh | [luongnhatinh](https://github.com/luongnhatinh) |
| 5 | Phạm Quốc Bảo | [simble2k](https://github.com/simble2k) |

## Repository Structure

```text
python-boostcamp/
├── README.md
├── PROGRESS.md              # Progress by member and week
├── .gitignore
├── .github/                # Issue templates and CI
├── members/                # Individual exercises
│   ├── baoduong2342007/
│   ├── tqhuy0602/
│   ├── pqquyenn/
│   ├── luongnhatinh/
│   └── simble2k/
├── shared/                 # Shared team exercises
├── tests/                  # Tests
└── docs/                   # Documentation and AI use records
```

Each member's folder contains `w1/`, `w2/`, and `w3/`. Individual exercises belong in their author's folder; team work belongs in the relevant shared folders.

## Workflow

Each member works on a separate branch, opens a pull request, and receives a review before merging. Record progress, test results, and issue/PR links in [PROGRESS.md](PROGRESS.md). Disclose AI assistance in [docs/ai-use-log.md](docs/ai-use-log.md).

See the short [Git workflow guide](docs/git-workflow.md) and [GitHub labels/milestones setup](docs/github-setup.md). Issue forms and a PR template are in `.github/`.

**Current status:** Week1 exercises and CI are in the repository. GitHub Actions runs the official tests for all five members on `main`; follow-up fixes and review evidence are tracked in `PROGRESS.md`.

### Week 1 Function Interfaces (TV1–TV4)

The Week 1 exercises require implementing the following functions in each member's `w1/` directory:

1. **W1-1: Grade Summary (`grades.py`)**
   - `summary(scores: list[float]) -> dict[str, float]`
   - Returns a dictionary with keys: `"min"`, `"max"`, `"mean"`, and `"median"` (rounded to 2 decimal places).
   - Raises `ValueError` if `scores` is empty.

2. **W1-2: Word Counter (`text_tools.py`)**
   - `word_count(text: str) -> dict[str, int]`: Counts word occurrences case-insensitively, treating punctuation (`.,!?;:`) as word separators. For example, `"hello,world"` contains `hello` and `world`.
   - `top_k(text: str, k: int) -> list[tuple[str, int]]`: Returns top `k` most frequent words sorted by count descending, then word ascending. Returns empty list if `k <= 0` or text has no words.

The instructor test files remain unchanged. The team punctuation regression check is separate: `python -m pytest -q tests/test_w1_tokenization.py`.

3. **W1-3: Thesis Eligibility (`rules.py`)**
   - `can_register_thesis(credits: int, gpa: float) -> bool`: Returns `True` if `credits >= 120` and `gpa >= 2.0`.
   - `missing(credits: int, gpa: float) -> list[str]`: Returns a list of human-readable requirement shortages (e.g., `"need X more credits"`, `"need GPA at least 2.0"`).

4. **W1-4: C++ to Python Translation (`translate.py`)**
   - Each member implements their assigned variant and includes a docstring comparing C++ vs. Python differences (memory management, dynamic typing, syntax/idiom):
     - **TV1 (`baoduong2342007`, Variant 1):** `binary_search(a: list[int], key: int) -> int`
     - **TV2 (`tqhuy0602`, Variant 2):** `insertion_sort(arr: list[int]) -> list[int]` (in-place modification, returns the same list)
     - **TV3 (`pqquyenn`, Variant 3):** `transpose(matrix: list[list[int]]) -> list[list[int]]`
     - **TV4 (`luongnhatinh`, Variant 4):** `primes_up_to(n: int) -> list[int]` (Sieve of Eratosthenes)

5. **W1-5: Group Timetable (`timetable.py`)**
   - `by_day(entries: list[tuple[str, str]]) -> dict[str, list[str]]`
   - Takes a list of `(course_code, weekday)` pairs and returns a dictionary mapping each day to an alphabetically sorted list of courses.

### Verification for Members 1–4 (TV1–TV4)

Run Week 1 checks from the repository root in an environment with `pytest` and `ruff` installed:

```bash
# Member 1 - Dương (Variant 1)
python -m pytest -q tests/test_w1.py --member baoduong2342007 --variant 1
python -m ruff check members/baoduong2342007

# Member 2 - Huy (Variant 2)
python -m pytest -q tests/test_w1.py --member tqhuy0602 --variant 2
python -m ruff check members/tqhuy0602

# Member 3 - Quyền (Variant 3)
python -m pytest -q tests/test_w1.py --member pqquyenn --variant 3
python -m ruff check members/pqquyenn

# Member 4 - Minh (Variant 4)
python -m pytest -q tests/test_w1.py --member luongnhatinh --variant 4
python -m ruff check members/luongnhatinh
```

Expected result: **5 passed** and clean Ruff checks for each member.

> [!WARNING]
> **Warning on skipped tests:** Always pass the correct `--member <username>` and `--variant <1-4>` arguments. If `--member` is omitted or invalid, `pytest` will skip individual tests by design in `tests/conftest.py`. Skipped tests do **not** count as passing.

### Verification for Member 5 (simble2k)

Run Week 1 checks from the repository root in an environment with pytest and Ruff installed:

```bash
# Run 4 official instructor tests (deselecting instructor variant 1-4)
python -m pytest -q tests/test_w1.py -k "not test_w1_4" --member simble2k

# Run 1 extra test for Member 5's unique_preserve_order (group-written test)
python -m pytest -q tests/test_w1_extra.py --member simble2k

# Linter and formatting check
python -m ruff check members/simble2k/w1 tests/test_w1_extra.py
python -m ruff format --check members/simble2k/w1 tests/test_w1_extra.py
```

Expected result: 4 official passed, 1 deselected; 1 extra test passed (`4 official + 1 extra`).

## Week 2: Run and Verify

Run commands from the repository root. Use the Python 3.12 environment from
[the environment guide](docs/ci-environment.md), with pytest and Ruff installed.

**Prerequisites:** the official W2 tests and sample files are being imported in
[#29](https://github.com/baoduong2342007/python-bootcamp/pull/29). The commands
below require that import plus your personal W2 package to be available in the
checkout. Missing files or skipped tests mean **W2 Pending**, not a passing submission.

For Huy, use:

```bash
# Three instructor tests for W2-1 to W2-3; W2 does not use --variant
python -m pytest -q tests/test_w2.py --member tqhuy0602

# Additional personal boundary tests
python -m pytest -q members/tqhuy0602/w2

# W2-4 cross-tests must be named explicitly: tests_for_*.py is not auto-discovered
python -m pytest -q members/tqhuy0602/w2/tests_for_luongnhatinh.py

# W2-5: read samples/tasks.csv using the package's __file__-relative path
python -m members.tqhuy0602.w2
python -m ruff check members/tqhuy0602/w2
```

For another member, replace the username and use that member's assigned
cross-test target:

| Author | Cross-test file in their `w2/` folder | Reviewer |
| --- | --- | --- |
| `baoduong2342007` | `tests_for_pqquyenn.py` | `luongnhatinh` |
| `tqhuy0602` | `tests_for_luongnhatinh.py` | `simble2k` |
| `pqquyenn` | `tests_for_simble2k.py` | `baoduong2342007` |
| `luongnhatinh` | `tests_for_baoduong2342007.py` | `tqhuy0602` |
| `simble2k` | `tests_for_tqhuy0602.py` | `pqquyenn` |

Each submission needs three official tests passing without skips, at least
five cross-test functions, successful package execution and clean Ruff checks.
Keep instructor assertions unchanged. Additional edge tests supplement the
official tests. A green W1 job alone does not establish W2 coverage; Quyền owns
the W2 CI expansion, and its status must be checked separately.

### Shared Week 2 planner

The proposed shared types and interfaces are in contract PR
[#35](https://github.com/baoduong2342007/python-bootcamp/pull/35).
All five functions use `shared.contract.Task` and `Block`, preserve input data,
and carry their own tests under `tests/shared_w2/`. Function PRs wait for the
contract to receive the required four teammate approvals and merge. Do not
substitute a personal Task class or claim agreement from a written proposal.

After the relevant functions/tests are available:

```bash
python -m pytest -q tests/shared_w2/
python -m ruff check shared/ tests/shared_w2/
```

Record actual commands/results, PR links and your real human study hours in
[PROGRESS.md](PROGRESS.md). Keep missing inputs, approvals or unimplemented
functions Pending. Dương creates `py-w2-done` only after all five submissions,
the approved contract, shared functions, integration and CI pass the team gates.
The verified metadata and open access/deadline items are recorded in
[Huy's W2 workflow audit](docs/w2-workflow-audit.md).

## Week 3: Run and Verify

Run commands from the repository root. Use Python 3.12 with pytest and Ruff installed.

For member Bảo (`simble2k`):

```bash
# Three instructor tests for W3-1 to W3-3 (Dates, Stats, CLI)
python -m pytest -q tests/test_w3.py --member simble2k

# Comprehensive personal unit tests for W3
python -m pytest -q members/simble2k/w3/tests

# Run personal CLI
python -m members.simble2k.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26

# Linter and formatting check
python -m ruff check members/simble2k/w3 tests/test_w3.py
python -m ruff format --check members/simble2k/w3
```

For other members, replace `--member simble2k` with the corresponding folder name under `members/`.

## Course Materials & Tests Source

The exercises follow Chapter 18 of **Git & GitHub for Team Projects**. Instructor materials and reference tests are available in [CSC10014 public materials](https://github.com/CSC10014-at-fit-hcmus/public_materials).

- **Official tests source revision:** commit [`2c6edc79772984f6a6ca0c3664ad0a49c907e80a`](https://github.com/CSC10014-at-fit-hcmus/public_materials/commit/2c6edc79772984f6a6ca0c3664ad0a49c907e80a) ("Tests for python-bootcamp (W1-W3)").
- **Week 2 materials import:** Week 2 test suite (`tests/test_w2.py`) and sample files (`samples/tasks.csv`, `samples/tasks_bad.csv`) were imported verbatim from [CSC10014 public materials](https://github.com/CSC10014-at-fit-hcmus/public_materials/tree/main/python-bootcamp) at revision [`4c1b2d075253fa282d8d8bf616616654a88db253`](https://github.com/CSC10014-at-fit-hcmus/public_materials/commit/4c1b2d075253fa282d8d8bf616616654a88db253) ("Added materials for W02") by Minh (`luongnhatinh`). The official test assertions and sample data retain their exact original hash.
- **Upstream check:** Upstream commits up to `4c1b2d0` ("Added materials for W02") have been audited; `tests/conftest.py` is identical to upstream, and no changes or updates to Week 1 tests have been made by the instructors. The official test files (`tests/conftest.py`, `tests/test_w1.py`, and `tests/test_w2.py`) retain their exact original hash.
