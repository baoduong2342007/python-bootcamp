# Week 2 — Dương (`baoduong2342007`)

Personal issue: [#33](https://github.com/baoduong2342007/python-bootcamp/issues/33).
Branch: `py/w2-baoduong2342007`. Assigned reviewer: Minh (`luongnhatinh`).

## Implemented and checked locally — 2026-10-21

- W2-1: dataclass, importance bounds, nonnegative days remaining.
- W2-2: ordered CSV loading, line-numbered errors, UTF-8 JSON with ISO dates.
- W2-3: feasibility exception preserves required and available hours.
- W2-4: six test functions for Quyền's W1, including empty matrix rows.
- W2-5: relative imports, guarded entry point and sample path derived from `__file__`.

Verification used Python 3.12 and a disposable copy of this branch with the
unchanged instructor tests/samples from Minh's pending import branch at
`3e03093700afa5854176195ddeca3469c6caf3c6` (PR #29). The imported files are not
duplicated in this personal PR. Merge #29 before treating the package command
as runnable on the combined repository.

From the verification copy's root:

```bash
python -m pytest -q tests/test_w2.py --member baoduong2342007
python -m pytest -q members/baoduong2342007/w2/test_edges.py
python -m pytest -q members/baoduong2342007/w2/tests_for_pqquyenn.py
python -m members.baoduong2342007.w2
python -m pytest -q tests/test_w1.py --member baoduong2342007 --variant 1
python -m ruff check members/baoduong2342007/w2
```

Results: 3 official W2 + 23 boundary cases + 6 cross-tests passed, no skips;
the package printed `DS exam` and `Assignment`; 5 official W1 passed. Ruff
0.17.1 passed and `git diff --check` passed. These are local results; CI and
peer approval remain separate gates. No hours were inferred.

## AI assistance

Codex hỗ trợ triển khai các module W2, tạo tests, chạy kiểm tra, chuẩn bị
tài liệu và thao tác Git/GitHub. Mã và tests do AI tạo trong phiên này được
giữ lại và khai báo tại đây; không khẳng định bài này đã được tự viết trước
phiên hỗ trợ. Dương cần đọc, hiểu và trao đổi với reviewer trước khi merge.
