import unittest

from humpty_dumpty import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "1. Basics": [
            {"input": [4, 2], "answer": [8.38, 21.48], "explanation": [8.38, 21.48]},
            {"input": [2, 2], "answer": [4.19, 12.57], "explanation": [4.19, 12.57]},
            {"input": [2, 4], "answer": [16.76, 34.69], "explanation": [16.76, 34.69]},
        ],
        "2. Extra": [
            {"input": [1, 3], "answer": [4.71, 17.07], "explanation": [4.71, 17.07]},
            {
                "input": [10, 10],
                "answer": [523.6, 314.16],
                "explanation": [523.6, 314.16],
            },
            {"input": [10, 1], "answer": [5.24, 24.79], "explanation": [5.24, 24.79]},
            {
                "input": [82, 19],
                "answer": [15499.57, 3930.55],
                "explanation": [15499.57, 3930.55],
            },
            {"input": [2, 3], "answer": [9.42, 22.25], "explanation": [9.42, 22.25]},
        ],
        "3. Edge": [
            {"input": [1, 1], "answer": [0.52, 3.14], "explanation": [0.52, 3.14]},
            {"input": [1, 99], "answer": [5131.79, 15403.68], "explanation": None},
            {"input": [99, 1], "answer": [51.84, 244.29], "explanation": None},
            {
                "input": [99, 99],
                "answer": [508_047.37, 30790.75],
                "explanation": [508_047.37, 30790.75],
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['1. Basics']:
            assert checkio(*i['input']) == i['answer']

    def test_Edge(self):
        for i in self.TESTS['3. Edge']:
            assert checkio(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['2. Extra']:
            assert checkio(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
