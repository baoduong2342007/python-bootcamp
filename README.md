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

## Course Materials & Tests Source

The exercises follow Chapter 18 of **Git & GitHub for Team Projects**. Instructor materials and reference tests are available in [CSC10014 public materials](https://github.com/CSC10014-at-fit-hcmus/public_materials).

- **Official tests source revision:** commit [`2c6edc79772984f6a6ca0c3664ad0a49c907e80a`](https://github.com/CSC10014-at-fit-hcmus/public_materials/commit/2c6edc79772984f6a6ca0c3664ad0a49c907e80a) ("Tests for python-bootcamp (W1-W3)").
- **Week 2 materials import:** Week 2 test suite (`tests/test_w2.py`) and sample files (`samples/tasks.csv`, `samples/tasks_bad.csv`) were imported verbatim from [CSC10014 public materials](https://github.com/CSC10014-at-fit-hcmus/public_materials/tree/main/python-bootcamp) at revision [`4c1b2d075253fa282d8d8bf616616654a88db253`](https://github.com/CSC10014-at-fit-hcmus/public_materials/commit/4c1b2d075253fa282d8d8bf616616654a88db253) ("Added materials for W02") by Minh (`luongnhatinh`). The official test assertions and sample data retain their exact original hash.
- **Upstream check:** Upstream commits up to `4c1b2d0` ("Added materials for W02") have been audited; `tests/conftest.py` is identical to upstream, and no changes or updates to Week 1 tests have been made by the instructors. The official test files (`tests/conftest.py`, `tests/test_w1.py`, and `tests/test_w2.py`) retain their exact original hash.
