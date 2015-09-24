import random
import unittest
from ..dark_labyrinth import find_path

TESTS = {
    "0. Simple": {
        "maze": [
            "XXXXXXX",
            "X.....X",
            "X.X.X.X",
            "X.....X",
            "X.X.X.X",
            "X.X.E.X",
            "XXXXXXX",
        ],
        "player": [1, 1]
    },
    "1. One": {
        "maze": [
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
        ],
        "player": [1, 4]
    },
    "2. Second": {
        "maze": [
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
        ],
        "player": [10, 10]
    },
    "3. Big": {
        "maze": [
            "XXXXXXXXXXXXXXX",
            "XXX...........X",
            "X...XXXXXXXXX.X",
            "X.X.X.......X.X",
            "X.X.X.X.X.X.X.X",
            "X.X.X.X.X.X.X.X",
            "X.....XXXXX...X",
            "X.X.X.......X.X",
            "X.X.XXXX.X.XX.X",
            "X.X.X..X.X.X..X",
            "X...XX.X.XXXX.X",
            "X.X..X.X....X.X",
            "X.XXXX.XXXXXX.X",
            "X........XE...X",
            "XXXXXXXXXXXXXXX",
        ],
        "player": [2, 2]
    },
    "4. Left Rule": {
        "maze": [
            "XXXXXXXXXXXXXXX",
            "X.............X",
            "X.XXXXXXXXXXX.X",
            "X.X.........X.X",
            "X.X.XXX.XXX.X.X",
            "X.X.X.....X.X.X",
            "X.X.X.XXX.X.X.X",
            "X.X.X.XEX.X.X.X",
            "X.X.X.X.X.X.X.X",
            "X.X.X.....X.X.X",
            "X.X.XXXXXXX.X.X",
            "X.X.........X.X",
            "X.XXXXX.XXXXX.X",
            "X.............X",
            "XXXXXXXXXXXXXXX",
        ],
        "player": [1, 7]
    }
}
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
ALL_DIRECT = (
    (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
PLAYER = "P"
WALL = "X"
UNKNOWN = "?"
EXIT = "E"
EMPTY = "."
MAX_STEP = 250


class Tests(unittest.TestCase):

    def setUp(self):
        def neighbours(coor, maze, direct=DIRECTIONS):
            x, y = coor
            N = len(maze)
            res = []
            for d in direct:
                nx = x + d[0]
                ny = y + d[1]
                if 0 < nx < N - 1 and 0 < ny < N - 1:
                    res.append((nx, ny))
            return res

        def carve(coor, maze):
            maze[coor[0]][coor[1]] = "."

        def isOpen(coor, maze):
            return maze[coor[0]][coor[1]] == "."

        def generateMaze(N):
            maze = [["X"] * N for _ in range(N)]
            start = (1, 1)
            exit = (N - 2, N - 2)
            queue = [start]
            good_neighs = []
            while queue or good_neighs:
                if good_neighs:
                    current = random.choice(good_neighs)
                    queue.append(current)
                else:
                    current = queue[-1]
                carve(current, maze)
                neighs = [
                    n for n in neighbours(current, maze) if not isOpen(n, maze)]
                good_neighs = []
                for n in neighs:
                    new_neighs = neighbours(n, maze, ALL_DIRECT)
                    all_current_neighs = neighbours(current, maze)
                    for cn in all_current_neighs:
                        if cn in new_neighs:
                            new_neighs.remove(cn)
                    if len([1 for x, y in new_neighs if maze[x][y] == "."]) <= 1:
                        good_neighs.append(n)
                if not good_neighs:
                    queue.remove(current)
            return maze

        for i in range(5, 8):
            name = "{}. Random".format(i)
            maze = generateMaze(15)
            x = y = 0
            while maze[x][y] == "X":
                x, y = random.randint(1, 13), random.randint(1, 13)
            player = x, y
            row_edges = [1, 7] if x // 8 else [8, 13]
            col_edges = [1, 7] if y // 8 else [8, 13]
            x = y = 0
            while maze[x][y] == "X":
                x, y = random.randint(*row_edges), random.randint(*col_edges)
            maze[x][y] = "E"
            TESTS[name] = {"maze": tuple("".join(row) for row in maze),
                           "player": player}

    def clear_zone(self, zone):
        return [row for row in zone if not all(el == UNKNOWN for el in row)]

    def get_visible(self, maze, player):
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
        grid = self.clear_zone(list(zip(*self.clear_zone(grid))))
        return tuple("".join(trow) for trow in zip(*grid))

    def initial(self, maze, player):
        return maze, self.get_visible(maze, player)

    def checker(self, func, player, maze):
        step = 0
        while True:
            result = func(self.get_visible(maze, player))
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

    def test_Simple(self):
        assert self.checker(find_path,
                            TESTS['0. Simple']['player'],
                            TESTS['0. Simple']['maze'])

    def test_One(self):
        assert self.checker(find_path,
                            TESTS['1. One']['player'],
                            TESTS['1. One']['maze'])

    def test_Second(self):
        assert self.checker(find_path,
                            TESTS['2. Second']['player'],
                            TESTS['2. Second']['maze'])

    def test_Big(self):
        assert self.checker(find_path,
                            TESTS['3. Big']['player'],
                            TESTS['3. Big']['maze'])

    def test_LeftRule(self):
        assert self.checker(find_path,
                            TESTS['4. Left Rule']['player'],
                            TESTS['4. Left Rule']['maze'])

    def test_Random(self):
        for i in TESTS:
            if 'Random' in i:
                assert self.checker(find_path,
                                    TESTS[i]['player'],
                                    TESTS[i]['maze'])
