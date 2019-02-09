import heapq
from collections import defaultdict
from itertools import combinations
from math import floor, hypot


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
            for (next_item, c) in graph[v].items():
                heapq.heappush(queue, (cost + c, next_item, path))
    return queue


def find_entities(bunker, entity):
    positions = []
    for y in range(len(bunker)):
        for x in range(len(bunker[y])):
            if bunker[y][x] == entity:
                positions.append((x, y))
    return positions


def numbers(x, y):
    if x <= y:
        return range(0, y - x + 1)
    else:
        return range(0, y - x - 1, -1)


def get_slope(position_1, position_2):
    return (position_2[1] - position_1[1]) / (position_2[0] - position_1[0])


def path_coordinates(position_1, position_2):
    path = []
    if position_2[0] == position_1[0]:
        # vertical
        for i in numbers(position_1[1], position_2[1]):
            path.append((position_1[0], position_1[1] + i))
    elif position_2[1] == position_1[1]:
        # horizontal
        for i in numbers(position_1[0], position_2[0]):
            path.append((position_1[0] + i, position_1[1]))
    else:
        slope = get_slope(position_1, position_2)
        if abs(slope) == 1:
            # diagnal
            for i in numbers(position_1[0], position_2[0]):
                path.append((position_1[0] + i, round(position_1[1] + i * slope)))
                # this is an edge case that the bat will hit the corner of a wall
                if len(path) > 1 and get_slope(path[-2], path[-1]) in [1, -1]:
                    path = [
                        (path[-2][0], path[-1][1]),
                        (path[-1][0], path[-2][1]),
                    ] + path
        else:
            # get the minimal step
            steps_per_cell = int(max(abs(slope), abs(1 / slope)))
            x_steps = abs(position_2[0] - position_1[0]) * steps_per_cell
            y_steps = abs(position_2[1] - position_1[1]) * steps_per_cell
            steps = max(x_steps, y_steps) * 2
            x_progress = (position_2[0] - position_1[0]) / steps
            y_progress = (position_2[1] - position_1[1]) / steps
            for i in range(steps + 1):
                new_x = position_1[0] + i * x_progress
                new_y = position_1[1] + i * y_progress
                path.append((round(new_x), round(new_y)))
                # hit the conner
                if new_x - int(new_x) == 0.5 and new_y - int(new_y) == 0.5:
                    path.append((round(new_x - 0.1), round(new_y - 0.1)))
                    path.append((round(new_x - 0.1), round(new_y + 0.1)))
                    path.append((round(new_x + 0.1), round(new_y - 0.1)))
                    path.append((round(new_x + 0.1), round(new_y + 0.1)))
    return list(set(path))


def bats_visibility(BatPositions, bunker):
    walls = find_entities(bunker, 'W')
    visibility = defaultdict(dict)
    for i, j in combinations(BatPositions, 2):
        path = path_coordinates(i, j)
        if not set(path).intersection(set(walls)):
            distance = hypot(i[0] - j[0], i[1] - j[1])
            visibility[i][j] = distance
            visibility[j][i] = distance
    return visibility


def checkio(bunker):
    bats = find_entities(bunker, 'B')
    alpha = find_entities(bunker, 'A')
    all_bats = bats + alpha
    visibility = bats_visibility(all_bats, bunker)
    return shortestPath(visibility, alpha[0], (0, 0))[0]


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':

    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(["B--", "---", "--A"]), 2.83), "1st example"
    assert almost_equal(checkio(["B-B", "BW-", "-BA"]), 4), "2nd example"
    assert almost_equal(checkio(["BWB--B", "-W-WW-", "B-BWAB"]), 12), "3rd example"
    assert almost_equal(
        checkio(["B---B-", "-WWW-B", "-WA--B", "-W-B--", "-WWW-B", "B-BWB-"]), 9.24
    ), "4th example"
