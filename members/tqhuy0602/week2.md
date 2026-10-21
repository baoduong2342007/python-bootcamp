# Week 2 — Trần Quốc Huy

Owner: `tqhuy0602`. Personal issue [#37](https://github.com/baoduong2342007/python-bootcamp/issues/37),
draft PR [#40](https://github.com/baoduong2342007/python-bootcamp/pull/40).
Assigned reviewer: Bảo (`simble2k`). Actual human hours: not yet reported.

Run from the repo root in a Python 3.10+ environment with pytest and Ruff:

```bash
python -m pytest -q tests/test_w2.py --member tqhuy0602
python -m pytest -q members/tqhuy0602/w2
python -m pytest -q members/tqhuy0602/w2/tests_for_luongnhatinh.py
python -m members.tqhuy0602.w2
python -m ruff check members/tqhuy0602/w2
```

Local verification on Python 3.14: respectively 3 official tests, 24 personal
edge cases, and 7 Minh cross-test cases passed. The cross-test file has six
functions and must be passed explicitly to pytest. The package prints DS exam
and Assignment; importing it does not execute the program. Ruff and Huy's five
official W1 regression tests pass.

Dependency: official tests/samples import [#29](https://github.com/baoduong2342007/python-bootcamp/pull/29).
For local verification only, the three files below were copied byte-for-byte
from import commit `3e03093700afa5854176195ddeca3469c6caf3c6`; they are not in
Huy's commits, and no assertion was changed:

| File | SHA-256 |
| --- | --- |
| `tests/test_w2.py` | `b89788e5ad09821d2a8e8cd98d437d048cebd5bbf1a4b4a027d30c703f504fd0` |
| `samples/tasks.csv` | `d2a1c85d61259938e7f6dffc85b2330056281a4ea90b8e6891b1dc76e9245c68` |
| `samples/tasks_bad.csv` | `17a5a63fff1c5fa856d4024d2e295ddaf6d00476638680567e5982588376287d` |

## Remaining gates

- Import PR #29 must merge before sample-based W2 commands work on a clean checkout.
- Quyền's W2 CI expansion and Bảo's review/approval are pending.
- Huy's review of Minh, shared-contract consensus, and the shared prioritise PR
  are tracked separately; local tests do not establish personal consensus.
- No `py-w2-done` tag or overall team completion is claimed.

AI use: Codex implemented the retained W2 code/tests and assisted checks,
documentation and Git operations. Huy is the assigned owner; human review and
actual human study time are not inferred from this automation.
