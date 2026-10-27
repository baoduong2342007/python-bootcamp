"""W1-2: Word counter module."""


def word_count(text: str) -> dict[str, int]:
    """Count lowercase words, preserving digits and Unicode characters."""
    punctuation = ".,!?;:"
    translation = str.maketrans(punctuation, " " * len(punctuation))
    words = text.lower().translate(translation).split()

    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the top k words by count, breaking ties alphabetically."""
    if k <= 0:
        return []

    ranked_words = sorted(
        word_count(text).items(), key=lambda item: (-item[1], item[0])
    )
    return ranked_words[:k]
