# AI use log

## 2026-10-20 — TV4 / luongnhatinh (Week 2)

- Minh implemented Week 2 exercises (W2-1 to W2-5) and shared team function `render(blocks)` in `python-bootcamp`:
  - W2-1 `models.py`: dataclass `Task` with range validation on `importance` (1–5) and `days_left(today)`.
  - W2-2 `io_utils.py`: `load_tasks` and `save_json` handling UTF-8, CSV structure validation, and specific line-number error reporting.
  - W2-3 `errors.py`: custom exception `InfeasiblePlan` and `check_feasible` verification.
  - W2-4 `tests_for_baoduong2342007.py`: 5 cross-tests for Dương (summary even, top_k zero/negative, missing single shortage, by_day duplicate courses, binary_search 1-element found/not found).
  - W2-5 `__main__.py` & `__init__.py`: runnable package via `python -m members.luongnhatinh.w2` loading samples via relative path.
  - T-W2 `shared/study_planner/render.py` & `shared/render.py`: `render(blocks)` formatting `<title>: <hours:g> h` and `"No tasks."` for empty input, accompanied by 5 unit tests in `tests/shared_w2/test_render.py`.
- AI assistance was used to verify edge cases, review Ruff rules and format annotations according to modern Python 3.11+ standards. All code and logic have been locally tested and verified.
- Verification results:
  - Official W2 tests: 3 passed (`python -m pytest -q tests/test_w2.py --member luongnhatinh`)
  - Cross-tests: 5 passed (`python -m pytest -q members/luongnhatinh/w2/tests_for_baoduong2342007.py`)
  - Package execution: clean run printing 2 tasks
  - Shared render tests: 5 passed (`python -m pytest -q tests/shared_w2/test_render.py`)
  - Ruff check: 0 errors (clean)
  - Regression W1: 5 passed
- Actual hours spent: ~2.5 hours.
## 2026-10-21 — TV5 / simble2k (Week 2)

- Bảo (`simble2k`) implemented Week 2 exercises (W2-1 to W2-5) in `members/simble2k/w2/` (PR #44) and the shared T-W2 function `total_effort` in branch `feat/w2-total-effort` (PR #45).
- AI assistant (Antigravity) was used for planning the implementation per `plan (3).md`, structuring edge test cases (`test_edges.py`), drafting cross-tests for Huy (`tests_for_tqhuy0602.py`), writing review notes (`review-huy-week1.md`), and formatting Git follow-up documentation.
- AI-generated code and test suites in this session were reviewed, tested, and validated locally. Actual time spent: approximately 2.5 hours.
## 2026-10-22 — Shared contract PR #35 follow-up

- Codex inspected GitHub reviews and CI, separated planner implementations
  from the contract proposal while retaining their original commits, and
  prepared separate function PR updates. No teammate approval is inferred.
- Retained AI-assisted changes clarify zero-hour Block construction versus
  allocate's positive-output rule, reject NaN effort/hours, add regression
  tests, and run shared tests in CI, including PRs stacked on the contract.
- The new NaN cases failed before the validation fix. Contract tests and CI
  results are recorded in PR #35; a skipped integration scaffold is not
  recorded as a completed team integration test.
- PR #41 was merged into the contract branch during this session. Dương
  explicitly chose to retain that update; Codex preserved prioritise and
  verified the resulting 17 shared tests without inferring contract approval.
- Parser follow-up #48 was subsequently merged into the contract branch
  during this work. Codex preserved that update too and verified the resulting
  31 shared tests; neither early function merge establishes contract consensus.

## 2026-10-21 — Week 2 / TV3 (pqquyenn)

- Phan Quỳnh Quyền hoàn thành 5 module bài tập cá nhân Week 2 (`models.py`, `io_utils.py`, `errors.py`, `tests_for_simble2k.py`, `__main__.py`) và hàm nhóm `allocate(tasks, hours)`.
- AI (Google Antigravity) hỗ trợ:
  - Thiết kế cấu trúc các module W2 theo yêu cầu bài tập và quy ước nhóm trong `plan (3).md`.
  - Xây dựng bộ test biên `test_edges.py` cho các trường hợp ngoại lệ (importance bounds, line numbering trong CSV error, UTF-8 JSON roundtrip, InfeasiblePlan exception).
  - Soạn thảo 5 test functions kiểm thử chéo W2-4 cho bài tập Week 1 của Bảo (`simble2k`) trong `tests_for_simble2k.py`.
  - Soạn thảo nhận xét review cho Bảo (`review-simble2k-week1.md`) gồm Question, Suggestion, Praise.
  - Cập nhật tài liệu theo dõi tiến độ và kiểm thử cục bộ.
- Toàn bộ code và test đã được chạy kiểm thử cục bộ: 3 official tests passed, 12 edge tests passed, 5 cross-tests passed, package module chạy in 2 tasks, Ruff clean.

## 2026-10-21 — TV2 / tqhuy0602, Week 2

- Trần Quốc Huy is the owner of issue #37 and PR #40. Codex implemented the
  retained W2 model, CSV/JSON utilities, exception, cross-tests, personal edge
  tests and package entry point; assisted verification, progress documentation,
  and Git/GitHub preparation. These new implementations are AI-assisted and
  are not declared independently self-written by Huy.
- Local Python 3.14 verification: 3 official W2 tests, 24 personal edge cases,
  7 cross-test cases for Minh (6 functions), and 5 W1 regression tests passed;
  Ruff passed. Package execution prints the two sample tasks; imports are quiet.
- Official W2 files were temporarily overlaid unchanged from Minh's pending
  import PR #29. They are excluded from Huy's commits. A clean checkout still
  requires that import before the sample-based W2 commands can run.
- Human approval, W2 CI coverage and merge remain pending. Huy reported
  6 hours of actual W2 study/work in this chat on 2026-10-21; automated runtime
  is excluded. No past dates or study hours were manufactured.
- After Huy explicitly authorized posting, Codex submitted COMMENT reviews
  with Question/Suggestion/Praise on Minh's #31/#32 and contract #35. These
  submissions are not personal team-consensus approvals.

## 2026-10-21 — Duong / Week 2

- Codex supports implementation of the personal W2 modules, generation of boundary and cross-tests, verification, documentation, and Git/GitHub operations. AI-generated code and tests from this session are retained; no claim of prior independent authorship is made.
- Local Python 3.12: 3 official W2, 23 boundary cases, 6 cross-tests and 5 W1 tests passed; package printed both sample tasks. Ruff 0.17.1 passed. Official W2 fixtures came from Minh's pending PR #29 in a disposable verification snapshot.
- Peer review, CI, merge and self-reported hours remain pending. See members/baoduong2342007/week2-followup.md for commands and provenance.

## 2026-10-16 — Week1 follow-up

- Dương wrote the original five exercises and asked Codex for Git help. He
  specified that punctuation splits words (`hello,world` -> `hello`, `world`).
- Codex renamed/pushed the branch and assisted with follow-up code, tests, CI,
  and docs: tokenization for Huy, Quyền, and Bảo; a group regression test; and
  docstring/documentation updates. Dương's tokenizer already met the rule.
  Minh's assignment and the instructor tests were untouched.
- Local pytest passed: TV1–TV3, 5 official tests each; TV5, 4 official + 1
  extra; group test, 4 cases. Ruff was not run. Original authorship and these
  AI-assisted follow-up changes are recorded separately; no hours inferred.

## 2026-10-15 — TV3 / pqquyenn

- Phan Quỳnh Quyền xác nhận 5 bài tập cá nhân Week1 ban đầu được thực hiện
  độc lập và đã merge vào main qua PR #14 tại commit b400900. Thời gian thực
  tế tự làm bài: khoảng 2 giờ.
- AI (Google Antigravity) hỗ trợ phiên bổ sung theo tài liệu `need_to_fix.md`:
  triển khai workflow CI GitHub Actions (`.github/workflows/ci.yml`), viết
  tài liệu hướng dẫn môi trường và CI (`docs/ci-environment.md`), chạy kiểm
  thử xác thực 1.093 trường hợp in-place cho bài của Huy (TV2), và chuẩn bị
  bằng chứng theo dõi tại `members/pqquyenn/week1-followup.md`.
- Kết quả kiểm thử trên main `f6512d0`:
  - Quyền (TV3): 5 official tests passed, 0 skipped (`--member pqquyenn --variant 3`); Ruff clean.
  - Ma trận toàn nhóm: TV1 5 passed, TV2 5 passed, TV4 5 passed, TV5 4 passed (1 deselected) + 1 extra passed. Toàn bộ repository Ruff clean (`All checks passed!`).
  - Đã soạn thảo nhận xét review bổ sung (Question, Suggestion, Praise) cho các PR #10, #11 và #25 của Huy.

## 2026-10-15 — TV2 / tqhuy0602

- Trần Quốc Huy confirms that the five original Week1 exercise implementations
  were self-written; AI assisted the other operations in PR #10/#11. No
  AI-generated exercise code is declared retained by Huy. Actual Week1 time
  before this follow-up: 2 hours, confirmed by Huy in this session.
- Codex assisted this follow-up by inspecting PR #17/#19 at their exact heads,
  running official tests, Ruff and edge checks, drafting supplemental reviews,
  adding the reviewer table and TV5 workflow, and preparing Git/GitHub updates.
  No individual exercise Python code or instructor tests changed in this PR.
- Verification on main `07b39013b62145d4e035fe8e964c6637aa65c9be`: Huy 5 official
  tests passed, no skips; Ruff clean; 1,093 insertion-sort cases passed with
  in-place mutation and identical returned object. TV5: 4 official passed,
  1 deselected; 1 group extra passed; Ruff clean. Local Python version: 3.14.0.
- Dương's original PR #17: 5 official passed; Ruff reported PLC0206. Follow-up
  PR #19: 5 official passed; Ruff clean. Both PRs were already merged when
  reviewed; these are supplemental reviews, not approvals before merge.
- Commands, tested revisions, review links and follow-up links are recorded
  in [Huy's evidence](../members/tqhuy0602/week1-followup.md). This local
  verification does not establish Ubuntu/Python 3.12 CI success.

## 2026-10-14 — TV1 / baoduong2342007

- Dương confirms that the original five Week1 exercises were self-written and AI assistance was used for GitHub operations. Reported time: approximately 2 hours.
- Codex assisted with review, running checks, opening PR #17, and resolving/merging Huy's PRs #10/#11 at Dương's request. The conflict resolutions preserved team progress and both README verification guides; no individual Python code was changed in those merges.
- In the TV1 follow-up linked to issue #18, Codex changed the timetable loop from dictionary-key lookup to iteration over `b.values()` to resolve Ruff PLC0206. This AI-assisted code change is retained; W1-2 punctuation behavior remains unchanged.
- Verification after the follow-up change: TV1 official tests 5 passed, no skip; Ruff for TV1 passed; `git diff --check` passed. Local checks are not evidence of Ubuntu CI.
- The original exercise history has one combined commit. It was not rewritten to manufacture five exercise commits.
- Bao's PR #15 was read and tested with Codex assistance; the local review notes are in TV1's member folder. These notes are not a GitHub approval or a review performed before the original merge.

## 2026-10-14 — TV5 / simble2k

- Bảo confirms that the five Week 1 exercises (`grades.py`, `rules.py`, `text_tools.py`, `timetable.py`, `translate.py`) and the extra test suite (`tests/test_w1_extra.py`) were implemented independently. AI assistance was not used to generate or retain solution code (`AI use: None` for exercise logic). Actual time spent: approximately 2 hours.
- AI assistance was used for Git/GitHub workflow guidance, formatting verification with Ruff, and preparing progress documentation.
- Verification results: 4 official instructor tests passed, 1 deselected (`test_w1_4_translate`); 1 extra test passed (`tests/test_w1_extra.py`); Ruff check and format clean for `members/simble2k/w1` and `tests/test_w1_extra.py`.
- Progress tracking: linked to issue #16 and merged PR #15 in `PROGRESS.md`.
## 2026-10-14 — TV4 / luongnhatinh

- Minh confirms that the original five Week1 exercises were self-written with no AI assistance (as declared in PR #13: None). Recorded actual time: 3.5 hours.
- In the follow-up review based on `need_to_fix.md`:
  - AI assistance was used to check and resolve Ruff warnings: refactored dictionary value iteration in `members/luongnhatinh/w1/timetable.py` to eliminate `PLC0206`, formatted the import block in `members/luongnhatinh/w1/translate.py` to resolve `I001`, and fixed escaped Markdown characters in the PR #13 body.
  - Follow-up verification for TV4: 5 official tests passed with 0 skips (`--member luongnhatinh --variant 4`), Ruff clean (`All checks passed!`). TV4 personal follow-up PR #20 opened and requested Bao (@simble2k) to review.
  - AI assisted with drafting team documentation for function interfaces (TV1–TV4), logging the official test source revision `2c6edc79772984f6a6ca0c3664ad0a49c907e80a` and upstream audit, recording review notes for Quyên's PR #14, and preparing the team documentation PR.

## Week 3 — Trần Quốc Huy (2026-10-25)

Người phụ trách code: **Trần Quốc Huy (`tqhuy0602`)**. **Codex hỗ trợ toàn bộ**: đọc kế hoạch,
kiểm tra materials/remote, đề xuất và trực tiếp viết dates/stats/CLI/tests, bổ sung docstrings W2,
soạn tracking/PROGRESS/bản nháp nhận xét Python-C++, cấu hình workflow cá nhân và chuẩn bị Git/PR.
Code AI tạo được giữ lại. Huy cần xác nhận hiểu code/nhận xét và giờ thực tế; peer review chưa được tự động xác nhận.
Validation: 3 official W3 +40 additional, 5 W1,27 W2 và51 shared W2 tests passed trên Python3.11.16;
Ruff phần Huy đạt; Ruff 0.6.9 local có 6 legacy findings W1; CI 0.17.2 được kiểm tra riêng. Official test_w3.py giữ nguyên byte theo source commit
f30c605c6ff376ac448ddb00fa82ae36347e29a9. E2E là PR riêng chờ shared CLI, chưa coi dependency thiếu là tests passed.

CI follow-up: Codex added explicit check=False to Huy subprocess tests and a PLW1510 per-file
exception only for the unchanged official test_w3.py. No source/test-group rules are disabled.
PR56 requests pqquyenn review; latest CI is recorded on the PR.

## Trần Quốc Huy — Week 3 follow-up (2026-10-26)

Code/phần việc do **Trần Quốc Huy (`tqhuy0602`) phụ trách**; **Codex hỗ trợ toàn bộ**:
đọc issue/peer review, bổ sung hai subprocess tests cho số giờ thập phân, kiểm tra regression
và hashes materials, cập nhật tracking/docs/PR. Các tests do AI tạo được giữ lại.
Huy tự báo 7 giờ cá nhân ngày 2026-10-26; thời gian chạy AI không được cộng vào.
Minh đã approved PR56 tại 7cf44ea; không nhận approval đó là của Huy hoặc Codex.
E2E không được ghi là đạt khi dependency CLI #54 còn thiếu.
