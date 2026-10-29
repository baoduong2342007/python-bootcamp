"""Module translating matrix transposition from C++ to Python.

Difference between C++ and Python:
In C++, a 2D matrix is typically represented as `std::vector<std::vector<int>>`.
Transposing it requires manually declaring nested loops with explicit indices,
allocating the destination matrix dimensions beforehand, and managing bounds.
In Python, matrix transposition can be expressed concisely and idiomatically
using list comprehension or argument unpacking with `zip(*matrix)`. Python
handles dynamic typing, row/column allocations, and garbage collection
automatically without manual memory management.
"""


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a 2D rectangular matrix without mutating the input.

    In C++, transposing a matrix requires nested `for` loops, resizing the
    result vector of vectors to [cols][rows], and copying elements by index.
    In Python, this is accomplished pythonically using `zip(*matrix)` or nested
    comprehensions, creating a new matrix cleanly without modifying the input.

    Returns an empty list if matrix is empty or has zero columns.
    """
    if not matrix or not matrix[0]:
        return []
    return [list(col) for col in zip(*matrix, strict=False)]
