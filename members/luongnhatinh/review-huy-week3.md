# Review notes for Huy's Week 3 PR #56

Prepared by Minh (`luongnhatinh`) on 2026-10-26.  
PR: [py-w3: tqhuy0602 (#56)](https://github.com/baoduong2342007/python-bootcamp/pull/56)  
Review Status: **Approved**

---

## 1. Validation Run Locally (Python 3.11)
- `python -m pytest -q tests/test_w3.py members/tqhuy0602/w3/tests --member tqhuy0602`: **43 passed in 3.93s, 0 skips**.
- `python -m pytest -q tests/test_w1.py --member tqhuy0602 --variant 2`: **5 passed**.
- `python -m pytest -q tests/test_w2.py members/tqhuy0602/w2 --member tqhuy0602`: **27 passed**.
- `python -m pytest -q tests/shared_w2`: **51 passed**.
- Ruff checks: `python -m ruff check members/tqhuy0602 --select E,F,I,B,UP,BLE --line-length 120`: **All checks passed!**
- Ruff format check: `python -m ruff format --check members/tqhuy0602/w3`: **7 files already formatted**.

---

## 2. Feedback (Question, Suggestion, Praise — QSP Pattern)

### Praise
- Clean implementation of nearest-rank p95 and tie-breaking in `log_stats.py`, strictly avoiding mutation of the input list.
- Comprehensive test coverage with 40 additional unit and boundary tests covering weekday offsets, leap day boundaries, and CLI error handling.
- Correctly imported official `tests/test_w3.py` byte-for-byte from public materials and exempted PLW1510 cleanly via `ruff.toml` without altering the instructor file.

### Question
- In `dates.py`, `parse_due` wraps `OverflowError` into `ValueError`. Did you test edge cases near year 9999 or negative date deltas?
- For `cli.py`, does the boundary conversion between personal `Task` and shared `Task` preserve float precision when handling non-integer effort hours?

### Suggestion
- Once shared CLI task #54 lands, rebase PR #57 (E2E tests) to unblock the final team integration.
- Remember to record your actual self-reported hours in `PROGRESS.md` before tagging `py-w3-done`.
