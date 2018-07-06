from itertools import combinations


def merge(island1, island2):
    for i in island1:
        for j in island2:
            if (abs(i[0] - j[0]) <= 1 and abs(i[1] - j[1]) <= 1):
                return island1 + island2
    return [island1, island2]


def checkio(data):
    lands = []
    for i, v in enumerate(data):
        for col, value in enumerate(v):
            if value == 1:
                lands.append([(i, col)])
    merged = True
    while merged:
        merged = False
        for i, j in combinations(lands, 2):
            ret = merge(i, j)
            if ret != [i, j]:
                lands.remove(i)
                lands.remove(j)
                lands.append(ret)
                merged = True
                break
    lands = [len(i) for i in lands]
    return sorted(lands)


# These "asserts" using only for self-checking
# and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
