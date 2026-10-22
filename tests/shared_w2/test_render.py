from datetime import date

import pytest

from shared.contract import Block, Task
from shared.render import render


def test_render_empty_blocks():
    """Empty block sequence must return 'No tasks.'."""
    assert render([]) == "No tasks."
    assert render(()) == "No tasks."


def test_render_single_block():
    """Single block formatted as '<title>: <hours:g> h'."""
    task = Task("DS exam", 5, 6.0, date(2026, 10, 30))
    block = Block(task=task, hours=2.0)
    assert render([block]) == "DS exam: 2 h"


def test_render_multiple_blocks_matching_plan_example():
    """Multiple blocks formatted matching section 3.4 example."""
    b1 = Block(task=Task("Assignment", 4, 1.5, date(2026, 10, 27)), hours=1.5)
    b2 = Block(task=Task("DS exam", 5, 6.0, date(2026, 10, 30)), hours=0.5)

    expected = "Assignment: 1.5 h\nDS exam: 0.5 h"
    assert render([b1, b2]) == expected


def test_render_fractional_hours():
    """Verify various fractional hour representations with :g format."""
    b1 = Block(task=Task("Lab review", 3, 0.75, date(2026, 10, 28)), hours=0.75)
    b2 = Block(task=Task("Coding", 4, 1.0, date(2026, 10, 29)), hours=1.0)
    assert render([b1, b2]) == "Lab review: 0.75 h\nCoding: 1 h"


def test_render_does_not_mutate_input():
    """Render should not mutate the input sequence or block objects."""
    task = Task("Review", 3, 2.0, date(2026, 10, 28))
    block = Block(task=task, hours=2.0)
    blocks = [block]

    result = render(blocks)
    assert result == "Review: 2 h"
    assert len(blocks) == 1
    assert block.hours == 2.0
    assert task.effort_h == 2.0


if __name__ == "__main__":
    pytest.main([__file__])
