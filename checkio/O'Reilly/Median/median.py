def checkio(data):
    data = sorted(data)
    index = len(data) / 2
    if index == int(index):
        index = int(index)
        return (data[index] + data[index - 1]) / 2
    else:
        return data[int(index)]


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':  # pragma: no cover
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1_000_000))) == 499_999.5, "Long."
    print("The local tests are done.")
