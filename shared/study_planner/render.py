from collections.abc import Sequence

from shared.contract import Block


def render(blocks: Sequence[Block]) -> str:
    """Render a sequence of allocated blocks into human-readable text.

    Format: <title>: <hours:g> h
    If blocks is empty, returns 'No tasks.'.
    """
    if not blocks:
        return "No tasks."
    lines = [f"{block.task.title}: {block.hours:g} h" for block in blocks]
    return "\n".join(lines)
