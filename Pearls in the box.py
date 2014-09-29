from itertools import combinations_with_replacement
from fractions import Fraction


def CreatePosibilityDict(pearls):
    PosibleCombinations = list(combinations_with_replacement([0, 1], pearls))
    result = {}
    for i in PosibleCombinations:
        if i not in result:
            result[i] = {}
        for j in PosibleCombinations:
            if j not in result:
                result[j] = {}
            if i == j:
                continue
            else:
                if sum([1 for k0, k1 in enumerate(i) if j[k0] != k1]) == 1:
                    if sum(i) > sum(j):
                        result[i][j] = Fraction(sum(i), pearls)
                    else:
                        result[i][j] = 1 - Fraction(sum(i), pearls)
    return result


def checkio(marbles, step):
    PosibilityDict = CreatePosibilityDict(len(marbles))
    CurrentStatus = [(tuple(sorted([1 if i == 'b' else 0
                                    for i in list(marbles)])), 1)]
    NextStatus = []
    for counter in range(step - 1):
        for i in CurrentStatus:
            for j in PosibilityDict[i[0]]:
                NextStatus.append((j, i[1] * PosibilityDict[i[0]][j]))
        CurrentStatus = NextStatus
        NextStatus = []
    result = []
    for i in CurrentStatus:
        for j in PosibilityDict[i[0]]:
            if sum(i[0]) < sum(j):
                result.append(i[1]*PosibilityDict[i[0]][j])
    return round(float(sum(result)), 2)

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    # assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"
