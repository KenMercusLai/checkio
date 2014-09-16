from math import sqrt
from itertools import combinations


def TriangularNumber(n):
    return n * (n + 1) / 2


def IsConsecutive(NumberList, j):
    StartIndex = NumberList.index(j[0])
    EndIndex = NumberList.index(j[-1])
    if StartIndex + len(j) - 1 == EndIndex:
        return True
    else:
        return False


def checkio(number):
    n = sqrt(number * 2)
    NumberList = [TriangularNumber(i) for i in range(1, int(n) + 1)
                  if TriangularNumber(i) < number]
    length = len(NumberList)
    while length > 1:
        for i in range(len(NumberList) - length + 1):
            if sum(NumberList[i:i+length]) == number:
                return NumberList[i:i+length]
        length -= 1
    return []

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
