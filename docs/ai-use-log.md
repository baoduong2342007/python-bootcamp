# AI use log

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
