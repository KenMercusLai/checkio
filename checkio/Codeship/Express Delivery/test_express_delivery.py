import unittest

from express_delivery import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "1. Basics": [
            {
                "input": ["S...", "....", "B.WB", "..WE"],
                "answer": (["S...", "....", "B.WB", "..WE"], 12),
                "explanation": "LLLDDD",
            },
            {
                "input": ["S...", "....", "B..B", "..WE"],
                "answer": (["S...", "....", "B..B", "..WE"], 11),
                "explanation": "DDBLLLBD",
            },
        ],
        "2. Extra": [
            {
                "input": ["S.W...", "..WB..", "..WW..", "....B.", "....W.", "..B.BE"],
                "answer": (
                    ["S.W...", "..WB..", "..WW..", "....B.", "....W.", "..B.BE"],
                    20,
                ),
                "explanation": "",
            },
            {
                "input": ["SBW...", ".WWB..", "..WW..", "......", "...WW.", "..BWBE"],
                "answer": (
                    ["SBW...", ".WWB..", "..WW..", "......", "...WW.", "..BWBE"],
                    18,
                ),
            },
            {
                "input": ["S..BW.", ".WWWWW", ".W....", ".W.W.B", ".W.W..", "...W.E"],
                "answer": (
                    ["S..BW.", ".WWWWW", ".W....", ".W.W.B", ".W.W..", "...W.E"],
                    29,
                ),
            },
        ],
        "3. Weird": [
            {"input": ["SB....BE"], "answer": (["SB....BE"], 11)},
            {"input": ["S...BB..E"], "answer": (["S...BB..E"], 16)},
            {
                "input": ["SBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBE"],
                "answer": (["SBBBBB", "BBBBBB", "BBBBBB", "BBBBBB", "BBBBBE"], 13),
            },
            {
                "input": [
                    "S.......",
                    "........",
                    "..B.....",
                    ".....B..",
                    "........",
                    ".......E",
                ],
                "answer": (
                    [
                        "S.......",
                        "........",
                        "..B.....",
                        ".....B..",
                        "........",
                        ".......E",
                    ],
                    22,
                ),
            },
            {
                "input": [
                    "SW.B.W.",
                    ".W.W.W.",
                    ".W.W.W.",
                    ".W.W.WB",
                    ".W.W.W.",
                    ".B.W..E",
                ],
                "answer": (
                    ["SW.B.W.", ".W.W.W.", ".W.W.W.", ".W.W.WB", ".W.W.W.", ".B.W..E"],
                    35,
                ),
            },
        ],
        "4. Big": [
            {
                "input": [
                    "S..BW....",
                    "...W.....",
                    "..W......",
                    ".........",
                    ".WWWWWWW.",
                    "..WB.....",
                    "..W....B.",
                    "..WWW.WWW",
                    "....W...E",
                ],
                "answer": (
                    [
                        "S..BW....",
                        "...W.....",
                        "..W......",
                        ".........",
                        ".WWWWWWW.",
                        "..WB.....",
                        "..W....B.",
                        "..WWW.WWW",
                        "....W...E",
                    ],
                    38,
                ),
            },
            {
                "input": [
                    "S........",
                    ".WWW.WWW.",
                    ".W.B...W.",
                    ".WWWWWWW.",
                    ".W..B..W.",
                    ".W.WWW.WW",
                    ".W...W.WB",
                    ".WWW.W.W.",
                    ".....W..E",
                ],
                "answer": (
                    [
                        "S........",
                        ".WWW.WWW.",
                        ".W.B...W.",
                        ".WWWWWWW.",
                        ".W..B..W.",
                        ".W.WWW.WW",
                        ".W...W.WB",
                        ".WWW.W.W.",
                        ".....W..E",
                    ],
                    56,
                ),
            },
        ],
    }

    def check_solution(self, func, max_time, field):
        ACTIONS = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0), "B": (0, 0)}
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

    def test_Basics(self):
        for i in self.TESTS['1. Basics']:
            assert self.check_solution(checkio, i['answer'][1], i['answer'][0])

    def test_Extra(self):
        for i in self.TESTS['2. Extra']:
            assert self.check_solution(checkio, i['answer'][1], i['answer'][0])

    def test_Weird(self):
        for i in self.TESTS['3. Weird']:
            assert self.check_solution(checkio, i['answer'][1], i['answer'][0])

    def test_Big(self):
        for i in self.TESTS['4. Big']:
            assert self.check_solution(checkio, i['answer'][1], i['answer'][0])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
