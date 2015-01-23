from math import hypot, ceil, floor

import heapq


def shortestPath(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while True:
        (cost, v, path) = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                return cost, path
            for (next_item, c) in graph[v].iteritems():
                heapq.heappush(queue, (cost + c, next_item, path))
    return queue


def FindBats(bunker):
    BatPositions = []
    for y in range(len(bunker)):
        for x in range(len(bunker[y])):
            if bunker[y][x] not in ['W', '-']:
                BatPositions.append((x, y))
    return BatPositions


def CanSeeEachOther(StartPosition, EndPosition, bunker):
    x0, y0 = StartPosition
    x1, y1 = EndPosition
    if abs(x0 - x1) >= abs(y0 - y1):
        ystep = (y1 - y0) * 1.0 / abs(x1 - x0) / 10
        xstep = (x1 - x0) * 1.0 / abs(x1 - x0) / 10
    else:
        ystep = (y1 - y0) * 1.0 / abs(y1 - y0) / 10
        xstep = (x1 - x0) * 1.0 / abs(y1 - y0) / 10
    while x1 * 1.0 != round(x0, 1) or y1 * 1.0 != round(y0, 1):
        x0 += xstep
        y0 += ystep
        if (str(int(round(x0, 1) * 10))[-1] == '5'
            and ('W' in [bunker[int(round(y0, 0))][int(ceil(x0))],
                         bunker[int(round(y0, 0))][int(floor(x0))]])):
            break
        if (str(int(round(y0, 1) * 10))[-1] == '5'
            and ('W' in [bunker[int(ceil(y0))][int(round(x0))],
                         bunker[int(floor(y0))][int(round(x0))]])):
            break
        if bunker[int(round(y0, 0))][int(round(x0, 0))] == 'W':
            break
    if x1 * 1.0 == round(x0, 1) and y1 * 1.0 == round(y0, 1):
        return True
    else:
        return False


def BatsVisibility(BatPositions, bunker):
    Visibility = {}
    for i in range(len(BatPositions)):
        for j in range(i + 1, len(BatPositions)):
            if CanSeeEachOther(BatPositions[i], BatPositions[j], bunker):
                if i not in Visibility:
                    Visibility[i] = {}
                if j not in Visibility:
                    Visibility[j] = {}
                distance = hypot(BatPositions[i][0] - BatPositions[j][0],
                                 BatPositions[i][1] - BatPositions[j][1])
                Visibility[i][j] = distance
                Visibility[j][i] = distance
    return Visibility


def checkio(bunker):
    BatPositions = FindBats(bunker)
    Visibility = BatsVisibility(BatPositions, bunker)
    AlphaPosition = [(x, y)
                     for y in range(len(bunker))
                     for x in range(len(bunker[y]))
                     if bunker[y][x] == 'A'][0]
    return shortestPath(Visibility, BatPositions.index(AlphaPosition), 0)[0]

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([
        "B--",
        "---",
        "--A"]), 2.83), "1st example"
    assert almost_equal(checkio([
        "B-B",
        "BW-",
        "-BA"]), 4), "2nd example"
    assert almost_equal(checkio([
        "BWB--B",
        "-W-WW-",
        "B-BWAB"]), 12), "3rd example"
    assert almost_equal(checkio([
        "B---B-",
        "-WWW-B",
        "-WA--B",
        "-W-B--",
        "-WWW-B",
        "B-BWB-"]), 9.24), "4th example"
