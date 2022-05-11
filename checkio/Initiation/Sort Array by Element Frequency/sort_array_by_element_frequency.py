from itertools import groupby
from typing import Iterable


def frequency_sort(items: Iterable):
    element_frequency = {i[0]: (len(list(i[1])), items.index(i[0])) for i in groupby(sorted(items))}
    ret = sorted(items, key=lambda x: str(element_frequency[x][0]) + '_' + str(len(items) - element_frequency[x][1]),
                 reverse=True)
    return ret


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
