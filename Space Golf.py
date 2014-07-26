from itertools import permutations


def golf(h):
    distances = []
    for i in [i for i in permutations(h)]:
        tempDistance = (i[0][0] ** 2 + i[0][1] ** 2) ** 0.5
        for j in range(len(i) - 1):
            tempDistance += ((i[j][0] - i[j + 1][0]) **
                             2 + (i[j][1] - i[j + 1][1]) ** 2) ** 0.5
        distances.append(tempDistance)
    return round(min(distances), 2)

print golf({(2, 2), (2, 8), (8, 8), (5, 5), (8, 2)})
