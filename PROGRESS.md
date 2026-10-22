# Python Bootcamp Progress

Replace Pending with actual results only. Record actual hours, not allocation estimates. Bao owns completion of this table; each member updates their own row.

| Member | Week | Issue | PR | Reviewer | Tests | Hours |
| --- | --- | --- | --- | --- | --- | --- |
| Member 1 - Duong (baoduong2342007) | w1 | [#18](https://github.com/baoduong2342007/python-bootcamp/issues/18) | [#17](https://github.com/baoduong2342007/python-bootcamp/pull/17) and [#19](https://github.com/baoduong2342007/python-bootcamp/pull/19) merged; Huy posted supplemental reviews after merge | Member 2 - Huy | 5 official passed (`--member baoduong2342007 --variant 1`); Ruff clean in follow-up | ~2h (self-reported) |
| Member 2 - Huy (tqhuy0602) | w1 | [#2](https://github.com/baoduong2342007/python-bootcamp/issues/2); [#3](https://github.com/baoduong2342007/python-bootcamp/issues/3); [#24](https://github.com/baoduong2342007/python-bootcamp/issues/24) | [#10](https://github.com/baoduong2342007/python-bootcamp/pull/10), [#11](https://github.com/baoduong2342007/python-bootcamp/pull/11), [#25](https://github.com/baoduong2342007/python-bootcamp/pull/25) merged; no Quyền review recorded | Member 3 - Quyen (`pqquyenn`) | 5 official passed, no skips; Ruff clean; 1,093 insertion-sort cases passed; punctuation follow-up merged in #27 | 2h (Huy confirmed 2026-10-15; before this follow-up) |
| Member 3 - Quyen (pqquyenn) | w1 | Issue not found | [#14](https://github.com/baoduong2342007/python-bootcamp/pull/14) and [#26](https://github.com/baoduong2342007/python-bootcamp/pull/26) merged; no Minh review recorded | Member 4 - Minh (`luongnhatinh`) | 5 official passed, no skips; Ruff clean; punctuation follow-up merged in #27; [evidence](members/pqquyenn/week1-followup.md) | ~2h (self-reported) |
| Member 4 - Minh (luongnhatinh) | w1 | [#12](https://github.com/baoduong2342007/python-bootcamp/issues/12) | [#13](https://github.com/baoduong2342007/python-bootcamp/pull/13), [#20](https://github.com/baoduong2342007/python-bootcamp/pull/20), [#22](https://github.com/baoduong2342007/python-bootcamp/pull/22) merged; W1-2 correction is on branch `py-w1-done` | Member 5 - Bao | 5 official passed, no skips; tokenization regression includes Minh and passes locally; Ruff not rerun for this branch | 3.5h (self-reported) |
| Member 5 - Bao (simble2k) | w1 | [#16](https://github.com/baoduong2342007/python-bootcamp/issues/16) | [#15](https://github.com/baoduong2342007/python-bootcamp/pull/15) and [#21](https://github.com/baoduong2342007/python-bootcamp/pull/21) merged; no Dương review recorded | Member 1 - Duong | 4 official passed, 1 deselected + 1 extra passed; punctuation follow-up merged in #27 | 2h (self-reported) |

Once passing, Member 5 records `4 official + 1 extra`. Do not describe the additional test as an instructor test.

## Week 2

| Member | Week | Issue | PR | Reviewer | Tests | Hours |
| --- | --- | --- | --- | --- | --- | --- |
| Trần Quốc Huy (`tqhuy0602`) | w2 | [#37](https://github.com/baoduong2342007/python-bootcamp/issues/37) | [#40](https://github.com/baoduong2342007/python-bootcamp/pull/40), draft; not merged | Bảo (`simble2k`), pending | Local Python 3.14: 3 official + 24 own edge + 7 Minh cross-tests passed; package runs; Ruff clean. Tests/samples temporarily overlaid from pending #29. W2 CI and peer approval pending. | 6h (Huy self-reported in this session on 2026-10-21; excludes automated runtime) |

## Week 1 closeout snapshot (2026-10-16)

- Group follow-up PR [#27](https://github.com/baoduong2342007/python-bootcamp/pull/27) is merged into `main` at `8eaa7e2`.
- Main CI run [38889875835](https://github.com/baoduong2342007/python-bootcamp/actions/runs/38889875835) passed Ruff, the tokenization regression, and all five member jobs on Python 3.12.
- A fresh clone at that SHA passed the instructor tests on Python 3.13.14: TV1–TV4 each 5 passed; TV5 4 passed, 1 deselected, plus 1 extra passed; tokenization regression 4 passed. The instructor test files were unchanged.
- The Python 3.13.14 clone check is supplemental local evidence; the green CI run is the Python 3.12 verification.
- The GitHub branch `py-w1-done` includes the submission record and Minh's W1-2 correction. Its tests pass locally; no pull request has been opened, so this branch has not run through GitHub Actions or merged to `main`.
- The existing main CI run [38889875835](https://github.com/baoduong2342007/python-bootcamp/actions/runs/38889875835) passed Ruff and all five member jobs at `8eaa7e2`. Review approvals were waived by Dương, and the GitHub issue audit did not find a personal Week 1 issue for Quyền; this record does not claim those as completed.
- The Week 1 completion tag has not been pushed. No separate Moodle upload is specified for the between-session Week 1 homework.

## Week 2 personal progress

| Member | Week | Issue | PR | Reviewer | Tests | Hours |
| --- | --- | --- | --- | --- | --- | --- |
| Duong (baoduong2342007) | w2 | [#33](https://github.com/baoduong2342007/python-bootcamp/issues/33) | [#34](https://github.com/baoduong2342007/python-bootcamp/pull/34) draft; review/merge pending | Minh (luongnhatinh) | Local: 3 official + 23 boundary + 6 cross-tests passed; package OK using pending #29 fixtures; W1 5 passed; Ruff clean | Pending actual self-report |

