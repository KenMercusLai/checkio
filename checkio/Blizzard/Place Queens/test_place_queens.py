import unittest
from itertools import combinations

from place_queens import COLS, ROWS, THREATS, place_queens


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ["b2", "c4", "d6", "e8"],
                "answer": [["b2", "c4", "d6", "e8"], True],
                "show": '{"b2", "c4", "d6", "e8"}',
            },
            {
                "input": ["b2", "c4", "d6", "e8", "a7", "g5"],
                "answer": [["b2", "c4", "d6", "e8", "a7", "g5"], False],
                "show": '{"b2", "c4", "d6", "e8", "a7", "g5"}',
            },
        ],
        "Extra": [
            {
                "input": ["a5", "b7", "c1", "e2", "f8", "g6", "h3"],
                "answer": [["a5", "b7", "c1", "e2", "f8", "g6", "h3"], True],
                "show": '{"a5", "b7", "c1", "e2", "f8", "g6", "h3"}',
            },
            {
                "input": ["a1", "h8"],
                "answer": [["a1", "h8"], False],
                "show": '{"a1", "h8"}',
            },
            {"input": ["d5"], "answer": [["d5"], True], "show": '{"d5"}'},
            {
                "input": ["b2", "f7"],
                "answer": [["b2", "f7"], True],
                "show": '{"b2", "f7"}',
            },
            {
                "input": ["b3", "d4", "f5"],
                "answer": [["b3", "d4", "f5"], False],
                "show": '{"b3", "d4", "f5"}',
            },
            {
                "input": ["b3", "d2", "f5"],
                "answer": [["b3", "d2", "f5"], True],
                "show": '{"b3", "d2", "f5"}',
            },
            {
                "input": ["a4", "g8", "h2", "e1", "f6"],
                "answer": [["a4", "g8", "h2", "e1", "f6"], True],
                "show": '{"a4", "g8", "h2", "e1", "f6"}',
            },
            {
                "input": ["c3", "d3", "e3", "f3"],
                "answer": [["c3", "d3", "e3", "f3"], False],
                "show": '{"c3", "d3", "e3", "f3"}',
            },
            {
                "input": ["d5", "d7", "e1"],
                "answer": [["d5", "d7", "e1"], False],
                "show": '{"d5", "d7", "e1"}',
            },
        ],
    }

    def check_coordinate(self, coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(self, func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(
            isinstance(c, str) and len(c) == 2 and self.check_coordinate(c)
            for c in user_set
        ):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert self.checker(place_queens, i['input'], i['answer'][1])

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert self.checker(place_queens, i['input'], i['answer'][1])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
