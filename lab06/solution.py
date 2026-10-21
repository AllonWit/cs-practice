def count_items(values: list) -> dict:
    counts = {}
    for word in values:
        counts[word] = counts.get(word , 0) + 1
    return counts


def unique_sorted(values: list) -> list:
    unique = sorted(set(values))
    return unique


def common(first, second: list) -> list:
    return sorted(set(first) & set(second))


def only_in_first(first, second: list) -> list:
    return sorted(set(first) - set(second))