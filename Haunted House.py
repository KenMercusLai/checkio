__author__ = 'KenMercusLai'

DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}
import heapq


def shortest_path(graph, start, end):
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


def checkio(house, stephan, ghost):
    if stephan == 1:
        return 'N'

    # calc where can be the next position direction for each position
    house_status = ['NEWS'] * 16
    for i in range(16):
        for j in house[i]:
            house_status[i] = house_status[i].replace(j, '')
    for i in range(4):
        house_status[i] = house_status[i].replace('N', '')
        house_status[-i - 1] = house_status[-i - 1].replace('S', '')
        house_status[3 + i * 4] = house_status[3 + i * 4].replace('E', '')
        house_status[i * 4] = house_status[i * 4].replace('W', '')

    if stephan == 16 and ghost == 1 and 'W' in house_status[-1]:
        return 'W'

    adj = {}
    for i, j in enumerate(house_status):
        adj[i + 1] = {}
        for k in j:
            adj[i + 1][i + 1 + DIRS[k]] = 1000
    for i in range(1, 17):
        _, path = shortest_path(adj, i, 1)
        for j in zip(path, path[1:]):
            adj[j[0]][j[1]] -= 10
    shared_destination = set(map(lambda x: stephan + DIRS[x],
                                 house_status[stephan - 1])) \
        & set(map(lambda x: ghost + DIRS[x],
                  house_status[ghost - 1]))
    for i in list(shared_destination):
        adj[stephan][i] = 9999
    metrics, path = shortest_path(adj, stephan, 1)
    if path[1] - path[0] == 4:
        return 'S'
    elif path[1] - path[0] == -4:
        return 'N'
    elif path[1] - path[0] == 1:
        return 'E'
    else:
        return 'W'


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for
    # auto-testing
    from random import choice

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction]
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    assert check_solution(checkio,
                          ["", "S", "S", "",
                           "E", "NW", "NS", "",
                           "E", "WS", "NS", "",
                           "", "N", "N", ""]), "1st example"
    assert check_solution(checkio,
                          ["", "", "", "",
                           "E", "ESW", "ESW", "W",
                           "E", "ENW", "ENW", "W",
                           "", "", "", ""]), "2nd example"
