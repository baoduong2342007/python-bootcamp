"""W2-4: regression checks for Quyen's Week 1 exercises."""

from members.pqquyenn.w1 import grades, rules, text_tools, timetable, translate


def test_summary_even_number_of_scores():
    assert grades.summary([9, 2, 4, 5]) == {
        "min": 2, "max": 9, "mean": 5.0, "median": 4.5,
    }


def test_top_k_nonpositive_limit():
    assert text_tools.top_k("cat cat dog", 0) == []
    assert text_tools.top_k("cat cat dog", -2) == []


def test_missing_only_gpa():
    assert rules.missing(120, 1.9) == ["need GPA at least 2.0"]


def test_missing_only_one_credit():
    assert rules.missing(119, 2.0) == ["need 1 more credits"]


def test_by_day_preserves_duplicates():
    entries = [("CS2", "Mon"), ("CS1", "Mon"), ("CS2", "Mon")]
    assert timetable.by_day(entries) == {"Mon": ["CS1", "CS2", "CS2"]}
    assert entries == [("CS2", "Mon"), ("CS1", "Mon"), ("CS2", "Mon")]


def test_transpose_empty_rows():
    matrix = [[], []]
    assert translate.transpose(matrix) == []
    assert matrix == [[], []]
