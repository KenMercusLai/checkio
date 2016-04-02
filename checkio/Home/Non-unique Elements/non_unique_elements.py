from collections import Counter


def checkio(data):
    """
    Don't remove this function.
    It's need for check your solution
    """
    for i in [x for x, y in Counter(data).items() if y == 1]:
        data.remove(i)
    return data


# for self-testing
if __name__ == "__main__":  # pragma: no cover
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
