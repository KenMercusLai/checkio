import heapq
from collections import defaultdict
from itertools import permutations


def translate_route(path):
    result = []
    for i in zip(path, path[1:]):
        if i[0][0] < i[1][0]:
            result.append('D')
        elif i[0][0] > i[1][0]:
            result.append('U')
        elif i[0][1] < i[1][1]:
            result.append('R')
        else:
            result.append('L')
    return ''.join(result)


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
    return translate_route(path)


def build_topology(field_map):
    result = defaultdict(dict)
    cols = len(field_map[0])
    rows = len(field_map)

    for y in range(rows - 1):
        for x in range(cols - 1):
            if field_map[y][x] != 'W':
                if field_map[y + 1][x] != 'W':
                    result[(y, x)][(y + 1, x)] = 1
                    result[(y + 1, x)][(y, x)] = 1
                if field_map[y][x + 1] != 'W':
                    result[(y, x)][(y, x + 1)] = 1
                    result[(y, x + 1)][(y, x)] = 1
    # last col
    for y in range(rows - 1):
        if field_map[y][cols - 1] != 'W':
            if field_map[y + 1][cols - 1] != 'W':
                result[(y, cols - 1)][(y + 1, cols - 1)] = 1
                result[(y + 1, cols - 1)][(y, cols - 1)] = 1
    # last row
    for x in range(cols - 1):
        if field_map[rows - 1][x] != 'W':
            if field_map[rows - 1][x] != 'W':
                result[(rows - 1, x)][(rows - 1, x + 1)] = 1
                result[(rows - 1, x + 1)][(rows - 1, x)] = 1
    return result


def find_spots(target, field_map):
    target_index = [i for i, v in enumerate(''.join(field_map)) if v == target]
    return [(i // len(field_map[0]), i % len(field_map[0])) for i in target_index]


def checkio(field_map):
    start_point = find_spots('S', field_map)[0]
    end_point = find_spots('E', field_map)[0]
    boxes = find_spots('B', field_map)
    graph = build_topology(field_map)

    direct_route = shortest_path(graph, start_point, end_point)
    unpack_routes = {}
    for i in permutations(boxes, 2):
        unpack_routes[i] = [
            shortest_path(graph, start_point, i[0]),
            'B' + shortest_path(graph, i[0], i[1]) + 'B',
            shortest_path(graph, i[1], end_point),
        ]
    unpack_routes_metric = [
        len(i[0]) * 2 + len(i[1]) + len(i[2]) * 2
        for i in sorted(unpack_routes.values())
    ]
    if len(direct_route) * 2 < min(unpack_routes_metric):
        route = direct_route
    else:
        index = unpack_routes_metric.index(min(unpack_routes_metric))
        route = ''.join(sorted(unpack_routes.values())[index])
    return route


if __name__ == '__main__':  # pragma: no cover
    print("Example:")
    print(checkio(["S...", "....", "B.WB", "..WE"]))

    # This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0), "B": (0, 0)}

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1]
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
