# T3-04 — Trần Quốc Huy: shared planner E2E

Code/tests do **Trần Quốc Huy phụ trách**, **Codex hỗ trợ toàn bộ**: đề xuất/viết tests và docs,
chạy kiểm tra, review hỗ trợ và Git/PR. Không nhận implementation shared CLI là của Huy.

Issue [#55](https://github.com/baoduong2342007/python-bootcamp/issues/55), reviewer Quyền.
Dependency [#54](https://github.com/baoduong2342007/python-bootcamp/issues/54): Dương/Quyền bổ sung shared CLI,
error handling và shared InfeasiblePlan. Base main `d19f42d` chỉ có package shared.study_planner, chưa có __main__.py.
Branch `test/w3-e2e-tqhuy0602` và PR này là draft; chưa đủ điều kiện merge hoặc báo E2E pass.

## Các cases được chuẩn bị

16 cases gọi `sys.executable -m shared.study_planner` từ repo root, timeout 10s, capture hai streams,
fixed today 2026-10-26. Kiểm tra sample 1.5h + 0.5h đúng thứ tự, tổng giờ <= budget,
missing/empty/header-only/bad CSV/schema sai, giữ line context, --require-all thiếu/đủ giờ,
hours hữu hạn/dương, date và option sai. Tests không skip và không sửa expected để che dependency thiếu.

## Kết quả thực tế — 2026-10-25, Python 3.11.16/macOS

```text
python -m ruff check tests_team --select E,F,I,B,UP,BLE --line-length 120    passed
python -m ruff format --check tests_team                                  passed
python -m pytest -q tests_team --tb=no                                    16 failed, 0 skipped
```

Nguyên nhân chung đã xác minh: `python -m shared.study_planner` báo thiếu `shared.study_planner.__main__`.
Đây là kết quả fail thật của dependency chưa triển khai; không phải bằng chứng E2E đạt.

## Bàn giao

1. Dương/Quyền triển khai #54 theo contract BC-03/7.5 trong plan; giữ shared W2 functions.
2. Cập nhật branch này từ main khi dependency merge; chạy lại đủ 16 cases.
3. Chỉ xử lý thay đổi contract sau thảo luận; không đổi expected để né implementation bug.
4. Bảo nối `python -m pytest -q tests_team` vào CI nhóm; peer review/CI đạt rồi mới merge.

Bài W3 cá nhân của Huy ở [PR #56](https://github.com/baoduong2342007/python-bootcamp/pull/56), tách riêng khỏi dependency CLI nhóm.
