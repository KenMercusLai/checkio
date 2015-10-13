from copy import deepcopy
import operator
from collections import defaultdict
import heapq

DIRS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "NW": (-1, -1),
    "NE": (-1, 1),
    "SE": (1, 1),
    "SW": (1, -1),
    "": (0, 0),
}


def translate_move(original, new_position):
    if original == new_position:
        return ''
    if original[0] > new_position[0]:
        if original[1] > new_position[1]:
            return 'NW'
        elif original[1] == new_position[1]:
            return 'N'
        else:
            return 'NE'
    elif original[0] == new_position[0]:
        if original[1] > new_position[1]:
            return 'W'
        else:
            return 'E'
    else:
        if original[1] > new_position[1]:
            return 'SW'
        elif original[1] == new_position[1]:
            return 'S'
        else:
            return 'SE'


def position_of(character, yard):
    index = ''.join(yard).index(character)
    return index // len(yard[0]), index % len(yard[0])


def possible_move_of(y, x, yard):
    rows, cols = len(yard), len(yard[0])
    return [(y + i[0], x + i[1])
            for i in DIRS.values()
            if 0 <= y + i[0] <= rows - 1
            and 0 <= x + i[1] <= cols - 1
            and yard[y + i[0]][x + i[1]] not in ['X', 'I', 'S']]


def get_adjencies(y, x, yard):
    result = set()
    open_position = set()
    closed_position = set()
    I = position_of('I', yard)
    for i in possible_move_of(I[0], I[1], yard):
        closed_position.add(i)
    S = position_of('S', yard)
    for i in possible_move_of(S[0], S[1], yard):
        closed_position.add(i)
    if (y, x) not in closed_position:
        open_position.add((y, x))
    while open_position:
        next_position = open_position.pop()
        result.add(next_position)
        closed_position.add(next_position)
        for i in possible_move_of(next_position[0], next_position[1], yard):
            if i not in closed_position:
                open_position.add(i)
    return result


def chicken_space(yard):
    C = position_of('C', yard)
    adjencies = get_adjencies(C[0], C[1], yard)
    I = position_of('I', yard)
    for i in possible_move_of(I[0], I[1], yard):
        try:
            adjencies.remove(i)
        except KeyError:
            pass
    S = position_of('S', yard)
    for i in possible_move_of(S[0], S[1], yard):
        try:
            adjencies.remove(i)
        except KeyError:
            pass
    return adjencies


def is_support(yard):
    yard_string = ''.join(yard)
    return yard_string.index('I') > yard_string.index('S')


def build_topology(yard):
    result = defaultdict(dict)
    for y in range(len(yard)):
        for x in range(len(yard[0])):
            for i in DIRS.values():
                if 0 <= y + i[0] <= len(yard) - 1 and 0 <= x + i[1] <= len(yard[0]) - 1:
                    if yard[y + i[0]][x + i[1]] in ['C', '.']:
                        result[(y, x)][(y + i[0], x + i[1])] = 1
                        result[(y + i[0], x + i[1])][(y, x)] = 1
    return result


def shortest_path(graph, start, end):
    queue = [(0, start, [])]
    seen = set()
    while True:
        (cost, v, path) = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == end:
                break
            for (next_item, c) in graph[v].items():
                heapq.heappush(queue, (cost + c, next_item, path))
    return path


def hunt(yard):
    topology = build_topology(yard)
    for i in yard:
        print(i)

    if is_support(yard):
        catcher_move = shortest_path(topology,
                                     position_of('I', yard),
                                     position_of('C', yard))
        support_move = shortest_path(topology,
                                     position_of('S', yard),
                                     position_of('C', yard))
        if catcher_move[1] == support_move[1]:
            temp_topology = deepcopy(topology)
            del temp_topology[catcher_move[1]]
            support_move = shortest_path(temp_topology,
                                         position_of('S', yard),
                                         position_of('C', yard))
            result = translate_move(position_of('I', yard), catcher_move[1])
        else:
            result = translate_move(position_of('I', yard), catcher_move[1])
    else:
        catcher_move = shortest_path(topology,
                                     position_of('S', yard),
                                     position_of('C', yard))
        support_move = shortest_path(topology,
                                     position_of('I', yard), 
                                     position_of('C', yard))
        if catcher_move[1] == support_move[1]:
            temp_topology = deepcopy(topology)
            for k, v in temp_topology.items():
                try:
                    del v[catcher_move[1]]
                except KeyError:
                    pass
                temp_topology[k] = v
            try:
                support_move = shortest_path(
                    temp_topology, position_of('I', yard), position_of('C', yard))
                result = translate_move(position_of('I', yard), support_move[1])
            except IndexError:
                result = ''
        else:
            result = translate_move(position_of('I', yard), support_move[1])
    print(result)
    print()
    return result


if __name__ == "__main__":  # pragma: no cover
    # These checker is using only for your local testing
    # It's run function in the same environment, but in the grading it will be
    # in various
    from random import choice
    from re import sub
    from math import hypot

    def random_chicken(_, possible):
        return choice(possible)

    def distance_chicken(func):
        def run_chicken(yard, possible):
            enemies = [find_position(yard, str(i + 1)) for i in range(N)]
            best = "", find_position(yard, "C")
            best_dist = 0 if func == max else float("inf")
            for d, (x, y) in possible:
                min_dist = min(hypot(x - ex, y - ey) for ex, ey in enemies)
                if func(min_dist, best_dist) == min_dist:
                    best = d, (x, y)
                    best_dist = min_dist
                elif min_dist == best_dist:
                    best = choice([(d, (x, y)), best])
                print(best, best_dist)
            return best

        return run_chicken

    CHICKEN_ALGORITHM = {
        "random": random_chicken,
        "run_away": distance_chicken(max),
        "hunter": distance_chicken(min)
    }

    ERROR_TYPE = "Your function must return a direction as a string."
    ERROR_FENCE = "A hobbit struck in the fence."
    ERROR_TREE = "A hobbit struck in an obstacle."
    ERROR_HOBBITS = "The Hobbits struck each other."
    ERROR_TIRED = "The Hobbits are tired."

    N = 2

    MAX_STEP = 100

    def find_position(yard, symb):
        for i, row in enumerate(yard):
            for j, ch in enumerate(row):
                if ch == symb:
                    return i, j
        return None, None

    def find_free(yard, position):
        x, y = position
        result = [("", position)]
        for k, (dx, dy) in DIRS.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(yard) and 0 <= ny < len(yard[0]) and yard[nx][ny] == ".":
                result.append((k, (nx, ny)))
        return result

    def prepare_yard(yard, numb):
        return tuple(sub("\d", "S", row.replace(str(numb), "I")) for row in yard)

    def checker(func, yard, chicken_algorithm="random"):
        for _ in range(MAX_STEP):
            individual_yards = [prepare_yard(yard, i + 1) for i in range(N)]
            results = [func(y) for y in individual_yards]
            if any(not isinstance(r, str) or r not in DIRS.keys() for r in results):
                print(ERROR_TYPE)
                return False
            chicken = find_position(yard, "C")
            possibles = find_free(yard, chicken)
            chicken_action, new_chicken = CHICKEN_ALGORITHM[
                chicken_algorithm](yard, possibles)
            positions = [find_position(yard, str(i + 1)) for i in range(N)]
            new_positions = []
            for i, (x, y) in enumerate(positions):
                nx, ny = x + DIRS[results[i]][0], y + DIRS[results[i]][1]
                if not (0 <= nx < len(yard) and 0 <= ny < len(yard[0])):
                    print(ERROR_FENCE)
                    return False
                if yard[nx][ny] == "X":
                    print(ERROR_TREE)
                    return False
                new_positions.append((nx, ny))
            if len(set(new_positions)) != len(new_positions):
                print(ERROR_HOBBITS)
                return False

            if any(new_chicken == pos for pos in new_positions):
                print("Gratz!")
                return True

            # update yard
            temp_yard = [[ch if ch in ".X" else "." for ch in row]
                         for row in yard]
            for i, (x, y) in enumerate(new_positions):
                temp_yard[x][y] = str(i + 1)
            temp_yard[new_chicken[0]][new_chicken[1]] = "C"
            yard = tuple("".join(row) for row in temp_yard)
        print(ERROR_TIRED)
        return False

    assert checker(hunt, ("......",
                          ".1.XX.",
                          "...CX.",
                          ".XX.X.",
                          "...2..",
                          "......"), "random"), "Example 1"
    assert checker(hunt, ("......",
                          ".1.XX.",
                          "...CX.",
                          ".XX.X.",
                          "...2..",
                          "......"), "run_away"), "Example 1"
    assert checker(hunt, ("......",
                          ".1.XX.",
                          "...CX.",
                          ".XX.X.",
                          "...2..",
                          "......"), "hunter"), "Example 1"

    assert checker(hunt, ("1.........",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.XCX.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".X.X.X.X.X",
                          ".........2"), "run_away"), "Tunnels"
    assert checker(hunt, ("1X.X.X.X2",
                          "X.X.X.X.X",
                          ".X.X.X.X.",
                          "X.X.X.X.X",
                          ".X.X.X.X.",
                          "X.X.X.X.X",
                          ".X.XCX.X.",
                          "X.X.X.X.X")), "ChessBoard"
    assert checker(hunt, ("...2...",
                          ".......",
                          ".......",
                          "...C...",
                          ".......",
                          ".......",
                          "...1...")), "Clear Random"
