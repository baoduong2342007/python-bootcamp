# Week 3 — Trần Quốc Huy (`tqhuy0602`)

Code/phần việc do **Trần Quốc Huy phụ trách**; **Codex hỗ trợ toàn bộ**: đề xuất và trực tiếp viết/chỉnh
code/tests/docs, review hỗ trợ, chạy kiểm tra, đối chiếu materials và chuẩn bị tracking/Git/PR.
Code do AI tạo được giữ lại. Huy cần đọc/giải thích code và xác nhận nhận xét cá nhân trước khi nộp.

## Phạm vi

Issue [#50](https://github.com/baoduong2342007/python-bootcamp/issues/50), reviewer `pqquyenn`.
Branch `py/w3-tqhuy0602`, base main `d19f42d`. W2 được xem là hoàn thành; chỉ thêm docstrings thiếu,
không viết lại loader/model hay thuật toán shared.

- `w3/dates.py`: ISO, tomorrow, in N days, next weekday. Hôm nay truyền tường minh; cùng weekday sang tuần sau.
- `w3/log_stats.py`: Counter counts, p95 nearest rank, slowest theo p95; hòa giữ route gặp trước; empty -> maps rỗng/None; không mutate input.
- `w3/cli.py`: argparse CSV/--hours/--today; gọi `w2.io_utils.load_tasks`, đổi fields từ personal Task sang shared Task tại boundary, rồi gọi shared prioritise/allocate/render. Kiểm tra effort hữu hạn/không âm tại boundary; không sửa W2 validation.
- Public exercise functions W1–W3 có type hints/docstrings; bổ sung docstrings còn thiếu ở W2.

Các quy ước nhóm ngoài official tests: strip/case-insensitive keywords, weekday đầy đủ, `in 0 days`,
nearest-rank/ties/empty và finite/nonnegative latencies. Các quy ước này có tests riêng.
Materials mới nhất vẫn là commit `f30c605c6ff376ac448ddb00fa82ae36347e29a9`.
Official `test_w3.py` được thêm nguyên byte để chạy bài; conftest và samples có sẵn được kiểm tra không đổi.
Hash và source ở [w3/materials.json](w3/materials.json). Bảo vẫn phụ trách gate materials/CI cho cả nhóm.

## Kết quả thực tế — 2026-10-25, macOS / Python 3.11.16

```text
python -m pytest -q tests/test_w3.py --member tqhuy0602          3 passed, 0 skipped
python -m pytest -q members/tqhuy0602/w3/tests                 40 passed
python -m pytest -q tests/test_w1.py --member tqhuy0602 --variant 2    5 passed
python -m pytest -q tests/test_w2.py members/tqhuy0602/w2 --member tqhuy0602    27 passed
python -m pytest -q tests/shared_w2                           51 passed
python -m ruff check members/tqhuy0602 --select E,F,I,B,UP,BLE --line-length 120    passed
python -m ruff format --check members/tqhuy0602/w3             passed
```

CLI demo đã chạy:

```text
python -m members.tqhuy0602.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
Assignment: 1.5 h
DS exam: 0.5 h
```

Workflow `.github/workflows/w3-tqhuy0602.yml` chạy official/additional tests có --member,
W1/W2/shared regression và Ruff riêng phần Huy trên Python 3.10/3.12.
Workflow CI toàn nhóm vẫn là phần Bảo. Ruff toàn repo hiện báo 6 lỗi có sẵn ở W1 của Dương/Minh;
không sửa source cá nhân của người khác. Đây là kết quả local của Ruff 0.6.9, không phải nguyên nhân fail CI 0.17.2.

## Ba nhận xét Python/C++ — bản nháp để Huy xác nhận

1. Python `date + timedelta` có kiểm tra biên ngày; `parse_due` chuyển cả OverflowError thành ValueError theo public contract. Khi viết C++ cần chọn kiểu lịch/ngày và xử lý lỗi biên tương ứng.
2. `sorted(values)` tạo list mới, nên thống kê p95 không thay input; `std::sort` trong C++ sắp xếp trực tiếp range, cần copy nếu muốn cùng contract.
3. Personal Task và shared Task là hai dataclass khác nhau; CLI chuyển từng field rõ ở boundary. Type hints Python không tự thay thế runtime validation; C++ cũng cần kiểm tra miền effort/budget khi parse dữ liệu ngoài.

## Tracking và việc còn chờ

- [Tracking W3](../../docs/w3-tracking.md) chứa issues 5 người, vòng reviewer và dependency CLI/E2E.
- E2E shared của Huy có issue #55 và branch/PR riêng, chờ #54 cung cấp `shared.study_planner.__main__` và shared InfeasiblePlan.
- Chưa có W3 PR của Dương để Huy review. Core PR16 đã merge với peer approval của Bảo; không nhận review đó là của Huy.
- PR cá nhân cần peer review/CI/merge. Giờ làm cá nhân chưa được Huy cung cấp; không suy ra từ thời gian chạy AI.
- Các commits trong phiên này đều ngày 2026-10-25; không giả lập lịch làm nhiều ngày hoặc sửa timestamps.

## CI follow-up

[PR56](https://github.com/baoduong2342007/python-bootcamp/pull/56) đã yêu cầu Quyền review.
Member CI Python 3.10/3.12 đã đạt ở [run40205079053](https://github.com/baoduong2342007/python-bootcamp/actions/runs/40205079053).
Base CI dùng Ruff 0.17.2, báo PLW1510 ở subprocess của test Huy và 2 calls trong official test_w3.py.
Đã thêm check=False vào test Huy vì tests tự kiểm tra exit code; ruff.toml chỉ miễn PLW1510
cho tests/test_w3.py để giữ nguyên file giảng viên. Không miễn rule cho source hoặc tests nhóm.
Kết quả 6 lỗi W1 local trước đó thuộc Ruff 0.6.9; không dùng kết quả đó để giải thích log CI 0.17.2.
Xem live PR cho CI của commit mới nhất.

Một lần full local rerun sau sửa subprocess đạt 42 passed và 1 timeout 10s ở invalid-date (stderr đã có argparse error); chạy lại riêng case đó đạt 1 passed trong 0.49s. CI 3.10/3.12 của commit mới là gate kiểm tra đầy đủ tiếp theo; không xóa ghi nhận lần timeout này.

Final verified CI: overall [run40206335449](https://github.com/baoduong2342007/python-bootcamp/actions/runs/40206335449)
and Huy matrix [run40206335489](https://github.com/baoduong2342007/python-bootcamp/actions/runs/40206335489)
succeeded at 23ad463 (Python3.10/3.12). Both matrix jobs run all43 W3 cases plus own/shared regressions.
The main-only push job is intentionally skipped on pull requests; no official W3 test is skipped in the member jobs.
PR56 remains open with pqquyenn review requested.
