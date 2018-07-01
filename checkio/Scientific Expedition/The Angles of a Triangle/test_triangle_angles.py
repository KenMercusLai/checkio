import unittest

from triangle_angles import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [4, 4, 4], "answer": [60, 60, 60], "explanation": ""},
            {"input": [3, 4, 5], "answer": [37, 53, 90], "explanation": ""},
            {"input": [2, 2, 5], "answer": [0, 0, 0], "explanation": ""},
            {"input": [5, 4, 3], "answer": [37, 53, 90], "explanation": ""},
            {"input": [10, 20, 30], "answer": [0, 0, 0], "explanation": ""},
            {"input": [11, 20, 30], "answer": [11, 20, 149], "explanation": ""},
            {"input": [100, 100, 100], "answer": [60, 60, 60], "explanation": ""},
            {"input": [15, 14, 19], "answer": [47, 51, 82], "explanation": ""},
            {"input": [7, 4, 8], "answer": [30, 61, 89], "explanation": ""}
        ],
        "Extra": [
            {"input": [1000, 1000, 1000], "answer": [60, 60, 60], "explanation": ""},
            {"input": [50, 40, 30], "answer": [37, 53, 90], "explanation": ""},
            {"input": [100, 100, 1000], "answer": [0, 0, 0], "explanation": ""},
            {"input": [2, 3, 4], "answer": [29, 47, 104], "explanation": ""},
            {"input": [80, 80, 60], "answer": [44, 68, 68], "explanation": ""},
            {"input": [4, 6, 10], "answer": [0, 0, 0], "explanation": ""},
            {"input": [8, 6, 10], "answer": [37, 53, 90], "explanation": ""},
            {"input": [395, 295, 295], "answer": [48, 48, 84], "explanation": ""},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
