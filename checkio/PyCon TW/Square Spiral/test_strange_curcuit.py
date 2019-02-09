import unittest

from strange_curcuit import find_distance


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [1, 9], "answer": 2},
            {"input": [9, 1], "answer": 2},
            {"input": [10, 25], "answer": 1},
            {"input": [5, 9], "answer": 4},
            {"input": [26, 31], "answer": 5},
            {"input": [50, 16], "answer": 10},
        ],
        "Edge": [
            {"input": [1, 2], "answer": 1},
            {"input": [99, 1], "answer": 8},
            {"input": [999, 1], "answer": 26},
            {"input": [998, 999], "answer": 1},
            {"input": [73, 91], "answer": 18},
            {"input": [100, 82], "answer": 18},
            {"input": [900, 961], "answer": 59},
            {"input": [86, 69], "answer": 9},
        ],
        "Extra": [
            {"input": [2, 18], "answer": 4},
            {"input": [777, 555], "answer": 18},
            {"input": [100, 10], "answer": 12},
            {"input": [69, 96], "answer": 9},
            {"input": [521, 2], "answer": 13},
            {"input": [81, 65], "answer": 16},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert find_distance(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert find_distance(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
