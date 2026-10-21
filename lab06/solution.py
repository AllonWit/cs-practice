def count_items(values: list) -> dist:
    counts = {}
    for word in values:
        counts[word] = count.get(word , 0) + 1
    return counts

def unique_sorted(values: list) -> list:
    unique = sorted(set(values))
    return unique