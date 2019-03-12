from itertools import combinations


def GroupDots(values):
    values = [list(eval(i)) for i in values]
    Changed = True
    while Changed:
        Changed = False
        for i in combinations(values, 2):
            if [j for j in i[0] if j in i[1]]:
                noDups = []
                [noDups.append(k) for k in i[0] + i[1] if not noDups.count(k)]
                values.remove(i[0])
                values.remove(i[1])
                values.append(noDups)
                Changed = True
                break
    return values


def checkio(cakes):
    LinesDict = {}
    for i in combinations(cakes, 2):
        if i[0][0] == i[1][0]:
            LinesDict[str(i)] = float('inf')
        else:
            if i[0][0] < i[1][0]:
                LinesDict[str(i)] = (i[1][1] - i[0][1]) / (i[1][0] - i[0][0])
            else:
                LinesDict[str(i)] = (i[0][1] - i[1][1]) / (i[0][0] - i[1][0])

    SlopesDict = {}
    for key, value in sorted(LinesDict.items()):
        if value not in SlopesDict:
            SlopesDict[value] = []
        SlopesDict[value].append(key)
    keys_to_del = [i for i in SlopesDict if len(SlopesDict[i]) < 3]
    for i in keys_to_del:
        del SlopesDict[i]

    for key, value in SlopesDict.items():
        SlopesDict[key] = [i for i in GroupDots(value) if len(i) > 2]
    return sum([len(SlopesDict[i]) for i in SlopesDict])


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert (
        checkio(
            [
                [2, 2],
                [2, 5],
                [2, 8],
                [5, 2],
                [7, 2],
                [8, 2],
                [9, 2],
                [4, 5],
                [4, 8],
                [7, 5],
                [5, 8],
                [9, 8],
            ]
        )
        == 6
    )
