import random
import unittest
from ..forgetful_prisoner import find_path

TESTS = {
    "1. Simple": {
        "maze": [
            "XXXXXXXXXXXX",
            "X..........X",
            "X.XXXXXXXX.X",
            "X.X......X.X",
            "X.X......X.X",
            "X.X......X.X",
            "X.X......X.X",
            "X.X......X.X",
            "X.X......X.X",
            "X.XXXXXXXX.X",
            "X.........EX",
            "XXXXXXXXXXXX"
        ],
        "player": [1, 1]
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
    "3. Left Rule": {
        "maze": [
            "XXXXXXXXXXXX",
            "X..........X",
            "X.XXXXXXXX.X",
            "X.X......X.X",
            "X.X.XX.X.X.X",
            "X.X......X.X",
            "X.X......X.X",
            "X.X..E...X.X",
            "X.X......X.X",
            "X.XXXX.XXX.X",
            "X..........X",
            "XXXXXXXXXXXX",
        ],
        "player": [1, 7]
    },
    "4. Vinc Maze": {
        "maze": [
            "XXXXXXXXXXXX",
            "X..........X",
            "X.XXXX...X.X",
            "X...X....X.X",
            "XXX..X.....X",
            "X.X..X...X.X",
            "X.X..X.E.X.X",
            "X.X..X...X.X",
            "X....X.....X",
            "X.XXXXXXXX.X",
            "X..........X",
            "XXXXXXXXXXXX",
        ],
        "player": [8, 4]
    },
}
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))
ALL_DIRECT = ((-1, -1), (-1, 0), (-1, 1), (0, 1),
              (1, 1), (1, 0), (1, -1), (0, -1))
DIR = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
WALL = "X"
EXIT = "E"
EMPTY = "."
MAX_STEP = 300


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

        for i in range(4, 7):
            name = "{}. Random".format(i)
            maze = generateMaze(12)
            x = y = 0
            while maze[x][y] == "X":
                x, y = random.randint(1, 10), random.randint(1, 10)
            player = x, y
            row_edges = [1, 5] if x // 6 else [6, 10]
            col_edges = [1, 5] if y // 6 else [6, 10]
            x = y = 0
            while maze[x][y] == "X":
                x, y = random.randint(*row_edges), random.randint(*col_edges)
            maze[x][y] = "E"
            TESTS[name] = {
                "maze": tuple("".join(row) for row in maze), "player": player}

    def get_visible(self, maze, player):
        result = {}
        for direction, (dr, dc) in DIR.items():
            cr, cc = player
            distance = -1
            while maze[cr][cc] != WALL:
                cr += dr
                cc += dc
                distance += 1
            result[direction] = distance
        return result

    def checker(self, func, player, maze):
        step = 0
        memory = 0
        while True:
            result, memory = func(self.get_visible(maze, player), memory)
            if not isinstance(result, str) or any(ch not in DIR.keys() for ch in result):
                print("The function should return a string with directions.")
                return False
            if not isinstance(memory, int) or memory < 0 or memory >= 2 ** 100:
                print(
                    "The memory number should be an integer from 0 to 2**100.")
                return False
            for act in result:
                if step >= MAX_STEP:
                    print("You are tired and your scanner is off. Bye bye.")
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
                            TESTS['1. Simple']['player'],
                            TESTS['1. Simple']['maze'])

    def test_Second(self):
        assert self.checker(find_path,
                            TESTS['2. Second']['player'],
                            TESTS['2. Second']['maze'])

    def test_LeftRule(self):
        assert self.checker(find_path,
                            TESTS['3. Left Rule']['player'],
                            TESTS['3. Left Rule']['maze'])

    def test_VincMaze(self):
        assert self.checker(find_path,
                            TESTS['4. Vinc Maze']['player'],
                            TESTS['4. Vinc Maze']['maze'])

    def test_Random(self):
        for i in TESTS:
            if 'Random' in i:
                assert self.checker(find_path,
                                    TESTS[i]['player'],
                                    TESTS[i]['maze'])
