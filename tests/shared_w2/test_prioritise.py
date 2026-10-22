"""Priority formula, stability, shared types, and input preservation."""

from copy import deepcopy
from datetime import date, timedelta

from shared.contract import Task
from shared.prioritise import prioritise

TODAY = date(2026, 10, 26)


def test_sample_order():
    exam = Task("DS exam", 5, 6, date(2026, 10, 30))
    assignment = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    assert prioritise([exam, assignment], TODAY) == [assignment, exam]


def test_due_and_overdue_use_one_day():
    future = Task("future", 5, 1, TODAY + timedelta(days=2))
    due = Task("due", 3, 1, TODAY)
    overdue = Task("overdue", 4, 1, TODAY - timedelta(days=10))
    assert prioritise([future, due, overdue], TODAY) == [overdue, due, future]


def test_equal_scores_keep_input_order():
    first = Task("first", 4, 1, TODAY + timedelta(days=2))
    second = Task("second", 2, 10, TODAY + timedelta(days=1))
    third = Task("third", 2, 0, TODAY)
    assert prioritise([second, first, third], TODAY) == [second, first, third]
    assert prioritise([third, first, second], TODAY) == [third, first, second]


def test_input_list_and_tasks_are_unchanged():
    low = Task("low", 1, 5, TODAY + timedelta(days=3))
    high = Task("high", 5, 0, TODAY)
    tasks = [low, high]
    snapshot = deepcopy(tasks)
    result = prioritise(tasks, TODAY)
    assert tasks == snapshot
    assert tasks[0] is low and tasks[1] is high
    assert result is not tasks
    assert result[0] is high and result[1] is low


def test_empty_returns_new_empty_list():
    tasks = []
    result = prioritise(tasks, TODAY)
    assert result == [] and result is not tasks


def test_single_task_and_sequence_input():
    task = Task("single", 3, 1, TODAY)
    assert prioritise((task,), TODAY) == [task]


def test_duplicate_task_references_are_preserved():
    task = Task("duplicate", 2, 1, TODAY)
    result = prioritise([task, task], TODAY)
    assert len(result) == 2
    assert result[0] is task and result[1] is task


def test_supplied_today_changes_ranking():
    early = Task("early", 2, 1, TODAY)
    later = Task("later", 5, 1, TODAY + timedelta(days=3))
    assert prioritise([early, later], TODAY) == [early, later]
    assert prioritise([early, later], TODAY + timedelta(days=3)) == [later, early]
