def checkio(array):
    if array:
        return sum(array[::2]) * array[-1]
    return 0


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__': # pragma: no cover
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
