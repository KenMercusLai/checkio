import unittest
from math import hypot

from colder_warmer import checkio


MAX_STEP = 12


def check_solution(func, goal, start):
    prev_steps = [start]
    for step in range(MAX_STEP):
        row, col = func([s[:] for s in prev_steps])
        if [row, col] == goal:
            return True
        if 10 <= row or 0 > row or 10 <= col or 0 > col:
            print("You gave wrong coordinates.")
            return False
        prev_distance = hypot(prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
        distance = hypot(row - goal[0], col - goal[1])
        alteration = (
            0 if prev_distance == distance else (1 if prev_distance > distance else -1)
        )
        prev_steps.append([row, col, alteration])
    print("Too many steps")
    return False


class Tests(unittest.TestCase):
    TESTS = {
        "1st": {"input": [[5, 5, 0]], "goal": [7, 7]},
        "2nd": {"input": [[0, 0, 0]], "goal": [5, 6]},
        "3rd": {"input": [[0, 0, 0]], "goal": [9, 9]},
        "4th": {"input": [[7, 7, 0]], "goal": [2, 4]},
        "5th": {"input": [[0, 9, 0]], "goal": [9, 0]},
    }

    def test_Basics(self):
        for i in self.TESTS:
            assert check_solution(
                checkio, self.TESTS[i]['goal'], self.TESTS[i]['input'][0]
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
