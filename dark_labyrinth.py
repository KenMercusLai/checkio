import heapq
from copy import deepcopy
from collections import defaultdict

MAZE = [['?' for i in range(29)]  for i in range(14)] \
    + [['?' if i != 14 else 'P'  for i in range(29)]] \
    + [['?' for i in range(29)] for i in range(14)]
REACHED_POSITIONS = []


def update_maze(visible):
    visible_player_x = ''.join(visible).index('P') % len(visible[0])
    visible_player_y = ''.join(visible).index('P') // len(visible[0])
    maze_player_x = ''.join([''.join(i) for i in MAZE]).index('P') % len(MAZE)
    maze_player_y = ''.join([''.join(i) for i in MAZE]).index('P') // len(MAZE)
    start_line_num = maze_player_y - visible_player_y
    start_shift_num = maze_player_x - visible_player_x

    for line in range(len(visible)):
        for shift in range(len(visible[0])):
            if MAZE[line + start_line_num][shift + start_shift_num] in ['O', '?']:
                MAZE[line + start_line_num][shift +
                                            start_shift_num] = visible[line][shift]


def build_connections():
    result = defaultdict(dict)
    for y in range(len(MAZE)):
        for x in range(len(MAZE[0])):
            if MAZE[y][x] in ['P', '.']:
                if MAZE[y - 1][x] in ['P', '.', '?', 'E']:
                    result[(y, x)][(y - 1, x)] = 1
                    result[(y - 1, x)][(y, x)] = 1
                if MAZE[y + 1][x] in ['P', '.', '?', 'E']:
                    result[(y, x)][(y + 1, x)] = 1
                    result[(y + 1, x)][(y, x)] = 1
                if MAZE[y][x - 1] in ['P', '.', '?', 'E']:
                    result[(y, x)][(y, x - 1)] = 1
                    result[(y, x - 1)][(y, x)] = 1
                if MAZE[y][x + 1] in ['P', '.', '?', 'E']:
                    result[(y, x)][(y, x + 1)] = 1
                    result[(y, x + 1)][(y, x)] = 1
    return result


def find_destination(connections):
    maze_player_x = ''.join([''.join(i)
                             for i in MAZE]).index('P') % len(MAZE)
    maze_player_y = ''.join([''.join(i)
                             for i in MAZE]).index('P') // len(MAZE)
    REACHED_POSITIONS.append((maze_player_y, maze_player_x))
    # 'E' in MAZE
    converted_maze = ''.join([''.join(i) for i in MAZE])
    if 'E' in converted_maze:
        exit_x = converted_maze.index('E') % len(MAZE)
        exit_y = converted_maze.index('E') // len(MAZE)
        return (exit_y, exit_x)

    # goto the unknown with most neighbors
    unknowns = [(i[0], i[1], len(connections[i]))
                for i in sorted(connections) if MAZE[i[0]][i[1]] == '?']
    if unknowns:
        next_destination = (
            sorted(unknowns, key=lambda x: x[2], reverse=True))[0]
        return next_destination[0], next_destination[1]


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
            for (next_item, c) in graph[v].items():
                heapq.heappush(queue, (cost + c, next_item, path))
    return queue


def refrest_maze():
    for y in range(len(MAZE)):
        for x in range(len(MAZE[0])):
            MAZE[y][x] = '?'
            if y == x == 14:
                MAZE[y][x] = 'P'
    for i in range(len(REACHED_POSITIONS)):
        REACHED_POSITIONS.pop()


def find_path(visible):
    update_maze(visible)
    connections = build_connections()
    destionation = find_destination(connections)

    maze_player_x = ''.join([''.join(i) for i in MAZE]).index('P') % len(MAZE)
    maze_player_y = ''.join([''.join(i) for i in MAZE]).index('P') // len(MAZE)
    next_location = shortest_path(connections,
                                  (maze_player_y, maze_player_x),
                                  destionation)[1][1]

    if MAZE[next_location[0]][next_location[1]] != 'E':
        MAZE[maze_player_y][maze_player_x] = '.'
        MAZE[next_location[0]][next_location[1]] = 'P'
    else:
        refrest_maze()

    if next_location[0] != maze_player_y:
        if next_location[0] > maze_player_y:
            return 'S'
        else:
            return 'N'
    else:
        if next_location[1] > maze_player_x:
            return 'E'
        else:
            return 'W'


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    PLAYER = "P"
    WALL = "X"
    UNKNOWN = "?"
    EXIT = "E"
    EMPTY = "."
    MAX_STEP = 250

    def clear_zone(zone):
        return [row for row in zone if not all(el == UNKNOWN for el in row)]

    def get_visible(maze, player):
        grid = [["?" for _ in range(len(row))] for row in maze]
        grid[player[0]][player[1]] = PLAYER
        for direction, diff in DIR.items():
            r, c = player
            while maze[r][c] != WALL:
                r, c = r + diff[0], c + diff[1]
                grid[r][c] = maze[r][c]
                if direction in "NS":
                    grid[r + DIR["W"][0]][c + DIR["W"][1]
                                          ] = maze[r + DIR["W"][0]][c + DIR["W"][1]]
                    grid[r + DIR["E"][0]][c + DIR["E"][1]
                                          ] = maze[r + DIR["E"][0]][c + DIR["E"][1]]
                else:
                    grid[r + DIR["S"][0]][c + DIR["S"][1]
                                          ] = maze[r + DIR["S"][0]][c + DIR["S"][1]]
                    grid[r + DIR["N"][0]][c + DIR["N"][1]
                                          ] = maze[r + DIR["N"][0]][c + DIR["N"][1]]
        grid = clear_zone(list(zip(*clear_zone(grid))))
        return tuple("".join(trow) for trow in zip(*grid))

    def initial(maze, player):
        return maze, get_visible(maze, player)

    def checker(func, player, maze):
        step = 0
        while True:
            result = func(get_visible(maze, player))
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False

            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your flashlight is off. Bye bye.")
                    return False
                r, c = player[0] + DIR[act][0], player[1] + DIR[act][1]
                if maze[r][c] == WALL:
                    print("BAM! You in the wall at {}, {}.".format(r, c))
                    return False
                elif maze[r][c] == EXIT:
                    print("GRATZ!")
                    return True
                else:
                    player = r, c
                    step += 1

    assert checker(find_path, (1, 1), [
        "XXXXXXX",
        "X.....X",
        "X.X.X.X",
        "X.....X",
        "X.X.X.X",
        "X.X.E.X",
        "XXXXXXX",
    ]), "Simple"
    assert checker(find_path, (1, 4), [
        "XXXXXXXXXX",
        "X....X...X",
        "X.XXXX.X.X",
        "X....X.X.X",
        "X.XXXX.X.X",
        "X.X....X.X",
        "X.XXEX.X.X",
        "X.XXXXXX.X",
        "X........X",
        "XXXXXXXXXX",
    ]), "First"
    assert checker(find_path, (10, 10), [
        "XXXXXXXXXXXX",
        "XX...X.....X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "X..X.X.X.X.X",
        "X.XX.X.X.X.X",
        "X..X.X.X.X.X",
        "XX.X.X.X.X.X",
        "XE.X.....X.X",
        "XXXXXXXXXXXX",
    ]), "Up down"
