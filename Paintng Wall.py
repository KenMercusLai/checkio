from time import sleep


def Merge(covered, NewCover):
    # merge new into list
    NeedMerge = False
    for i in covered:
        if NewCover[1] < i[0] or i[1] < NewCover[0]:
            continue
        else:
            NeedMerge = True
            break
    if NeedMerge:
        covered.remove(i)
        covered.append([min(i[0], NewCover[0]), max(i[1], NewCover[1])])
    else:
        covered.append(NewCover)

    # internal merge
    if len(covered) > 1:
        NeedMerge = False
        for i in range(len(covered) - 1):
            for j in range(i + 1, len(covered)):
                if (covered[j][1] < covered[i][0]
                        or covered[i][1] < covered[j][0]):
                    continue
                else:
                    NeedMerge = True
                    break
            if NeedMerge:
                break
        if NeedMerge:
            temp = [min(covered[i][0], covered[j][0]),
                    max(covered[i][1], covered[j][1])]
            del covered[j]
            del covered[i]
            covered.append(temp)
    return covered


def checkio(required, operations):
    covered = []
    for i in operations:
        covered = Merge(covered, i)
        if sum([j[1] + 1 - j[0] for j in covered]) >= required:
            return operations.index(i) + 1
    return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
    assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
    assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
    assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
    assert checkio(
        21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
    assert checkio(
        1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
