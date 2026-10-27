# Python vs C++ Comparison (W3-4 Reflection)

1. **Kiểu dữ liệu và Structuring (Dynamic vs Static typing):**
   Trong Python, việc xử lý dữ liệu cặp `(route, latency)` và trả về cấu trúc phân cấp đa dạng (`dict` chứa `dict` và giá trị `None`) ở hàm `analyse` rất tự nhiên và nhanh gọn mà không cần khai báo lớp struct hay variant phức tạp; tuy nhiên C++ với `std::unordered_map` và static typing giúp bắt lỗi kiểu ngay tại thời điểm biên dịch (compile-time) thay vì dựa vào bộ test runtime.

2. **Quản lý bộ nhớ và Slicing / Sorting:**
   Khi tính toán phân vị `p95`, Python hỗ trợ sort và indexing trực tiếp rất ngắn gọn, nhưng cần chú ý tạo bản sao (shallow copy / comprehension) để tránh mutate mảng dữ liệu gốc; trong khi C++ yêu cầu quản lý bộ nhớ thông qua `std::vector` với passing by const reference hoặc `std::span` để tối ưu hóa hiệu năng và tránh copy overhead không cần thiết.

3. **Xử lý chuỗi và Thời gian (Date & Regex handling):**
   Module chuẩn `datetime` và `re` của Python cung cấp abstraction mức cao giúp việc parse linh hoạt các định dạng ngày ("tomorrow", "in N days", weekday) chỉ trong vài chục dòng code; còn trong C++, việc tương tự đòi hỏi cấu hình regex và thư viện `<chrono>` (C++20) với cú pháp khắt khe và tốn nhiều boilerplate hơn đáng kể.
