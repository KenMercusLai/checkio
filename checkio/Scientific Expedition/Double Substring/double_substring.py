from collections import defaultdict
from itertools import groupby


def find_repeated_chars(line):
    repeated_chars = [k for k, g in groupby(sorted(line)) if len(list(g)) > 1]
    indexes = defaultdict(list)
    for index, char in enumerate(line):
        if char in repeated_chars:
            indexes[char].append(index)
    return indexes


def non_overlapping_range(repeated_indexes, line):
    ret = []
    for i, v in enumerate(repeated_indexes[:-1]):
        for j in repeated_indexes[i + 1:]:
            max_repeated_len = min(j - i, len(line) - j)
            for k in range(max_repeated_len):
                ret.append((v, j, k + 1))
    return ret


def double_substring(line):
    indexes = find_repeated_chars(line)
    max_len = 0
    for i in indexes:
        sub_strings = non_overlapping_range(indexes[i], line)
        for start, end, length in sub_strings:
            if length <= max_len:
                continue
            if line[start:start + length] == line[end:end + length]:
                max_len = length
    return max_len


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
