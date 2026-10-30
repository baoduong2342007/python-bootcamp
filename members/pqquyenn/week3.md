# Week 3 — Phan Quỳnh Quyền (`pqquyenn`)

Personal Issue: [#51](https://github.com/baoduong2342007/python-bootcamp/issues/51)  
Branch: `py/w3-pqquyenn`  
Assigned Reviewer: Lương Nhật Minh (`luongnhatinh`)

---

## 1. Implemented Components

- **W3-1 (`dates.py`)**:
  - `parse_due(text, today) -> date`: Handles ISO `YYYY-MM-DD`, `tomorrow`, `in N days`, and weekday names (abbreviated `Mon`..`Sun` and full names).
  - Next occurrence convention: Weekdays strictly resolve to future dates (`days_ahead > 0`); matching the same weekday targets +7 days.
  - Case-insensitive and whitespace-stripped keywords.
  - Invalid formats, empty strings, and nonexistent calendar dates cleanly raise `ValueError`.
- **W3-2 (`log_stats.py`)**:
  - `analyse(pairs) -> dict`: Computes request counts per route, 95th percentile latency using the nearest-rank method (`ceil(0.95 * n) - 1`), and identifies the slowest route.
  - Tie-breaking: In case of equal maximum p95 latencies, the route encountered first in the input stream is chosen.
  - Empty input returns `{"counts": {}, "p95": {}, "slowest": None}` without mutating input lists.
- **W3-3 (`cli.py`)**:
  - Command-line interface built with `argparse` taking `csv_path`, `--hours`, and optional `--today`.
  - Converts personal `members.pqquyenn.w2.models.Task` to `shared.contract.Task` at the boundary.
  - Reuses shared `prioritise`, `allocate`, and `render`.
  - Rejects non-positive or non-finite hours (`nan`, `inf`) with exit code 2.
  - Handles missing files and bad CSV files gracefully with clear `stderr` messages and exit code 1.
- **W3-4 (Clean code & type annotations)**:
  - Full type annotations and PEP 257 docstrings across W1–W3.
  - Resolved legacy Ruff `B905` in `w1/translate.py` and `UP015` in `w2/io_utils.py`.
  - Ruff check and format clean across all files.

---

## 2. Python vs C++ Observations (Three Reflections)

1. **Quản lý phân vị và Sắp xếp (Immutable Sorting vs In-place `std::sort` / `std::nth_element`):**
   Trong Python (`log_stats.py`), việc tính toán p95 qua phương pháp nearest-rank sử dụng hàm dựng sẵn `sorted()` tự động trả về một danh sách mới được cấp phát độc lập, bảo đảm tính bất biến (immutability) cho mảng dữ liệu gốc và tránh các side-effect không mong muốn giữa các hàm phân tích. Ngược lại trong C++, thuật toán chuẩn `std::sort` hoặc giải thuật phân vị tối ưu $O(n)$ `std::nth_element` đều thay đổi trực tiếp vùng nhớ tại chỗ (in-place) trên `std::vector`; do đó lập trình viên C++ cần chủ động tạo bản sao `std::vector` nếu muốn duy trì dữ liệu log ban đầu.

2. **Xử lý Chuỗi và Lịch biểu Thời gian (High-level Date Abstraction vs `std::chrono`):**
   Trong `dates.py`, module chuẩn `datetime` và `re` của Python cung cấp abstraction mức cao, cho phép parse linh hoạt các biểu thức ngày phong phú ("tomorrow", "in N days", và weekday wrap-around qua modulo 7) chỉ trong vài chục dòng mã, đồng thời tự động kiểm tra tính hợp lệ của năm nhuận (như 2024-02-29 so với 2026-02-29). Ở C++20, dù thư viện `<chrono>` đã cung cấp `std::chrono::year_month_day` và `std::chrono::sys_days`, việc kiểm tra hợp lệ ngày tháng vẫn phải gọi thủ công qua `.ok()` trước khi chuyển đổi sang time point, và việc parse chuỗi động linh hoạt đòi hỏi lượng mã boilerplate lớn hơn đáng kể.

3. **Mô hình Dữ liệu và Ranh giới Chuyển đổi (Data Transfer Objects & Boundary Conversion):**
   Trong `cli.py`, việc tích hợp giữa model cá nhân `members.pqquyenn.w2.models.Task` và model dùng chung `shared.contract.Task` yêu cầu một bước chuyển đổi (boundary mapping) tường minh để đảm bảo an toàn hợp đồng giữa các tuần. Trong Python, dù hai `@dataclass` có tên thuộc tính giống nhau, chúng vẫn là hai kiểu dữ liệu độc lập tại runtime; trong khi ở C++, các struct có memory layout tương đương có thể được tái sử dụng hoặc chuyển đổi ngay tại thời điểm biên dịch (compile-time) thông qua type alias, conversion operator hoặc template mà không phát sinh phụ phí cấp phát lại đối tượng trong bộ nhớ.

---

## 3. Verification Commands & Results

Run from the repository root:
```bash
python -m pytest -q tests/test_w3.py --member pqquyenn
python -m pytest -q members/pqquyenn/w3/tests
python -m members.pqquyenn.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
python -m pytest -q tests/test_w1.py --member pqquyenn --variant 3
python -m pytest -q tests/test_w2.py members/pqquyenn/w2 --member pqquyenn
python -m pytest -q tests/shared_w2
python -m pytest -q tests_team/test_study_planner_cli.py
python -m ruff check members/pqquyenn --select E,F,I,B,UP,BLE --line-length 120
python -m ruff format --check members/pqquyenn/w3
```

### Local Test Output:
- Official W3 tests: **3 passed, 0 skips**.
- Quyền additional W3 tests: **17 passed** (`test_dates.py`: 6, `test_log_stats.py`: 6, `test_cli.py`: 5).
- Quyền W1 regression (variant 3): **5 passed**.
- Quyền W2 regression: **15 passed**.
- Shared W2 regression: **51 passed**.
- Shared CLI E2E tests: **16 passed**.
- Ruff checks & format: **All checks passed!**

---

## 4. AI Use Disclosure

Developed with assistance from Google Antigravity / Gemini assistant for scaffolding regex patterns in `dates.py`, nearest-rank index logic, boundary edge test fixtures, and documentation. All logic, typing, and tests were verified locally.
