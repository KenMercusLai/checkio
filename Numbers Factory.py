import itertools
from copy import deepcopy


def makeFactors(number):
    result = []
    if number < 10:
        result.append([number])
    else:
        for i in range(2, 10):
            if number % i == 0:
                result.append(sorted([i, number / i]))
    # remove duplicates
    result = [i for i, j in itertools.groupby(result)]
    return result


def checkio(data):
    result = []
    result = makeFactors(data)

    while any([j > 9 for i in result for j in i]):
        for i in result:
            if any([j > 9 for j in i]):
                result.remove(i)
                fractors = deepcopy(i)
                for j in fractors:
                    if j > 9:
                        fractors.remove(j)
                        for fractor in makeFactors(j):
                            result.append(sorted(fractors + fractor))
    # remove duplicates
    result = [i for i, j in itertools.groupby(result)]
    if result:
        return min([int(''.join(map(str, i))) for i in result])
    return 0
# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    # assert checkio(560) == 2578
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"
