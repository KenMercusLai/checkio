import unittest

from hexagon_spiral import hex_spiral


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [2, 9], "answer": 1, "explanation": 2},
            {"input": [9, 2], "answer": 1, "explanation": 2},
            {"input": [6, 19], "answer": 2, "explanation": 7},
            {"input": [5, 11], "answer": 3, "explanation": 1},
            {"input": [13, 15], "answer": 2, "explanation": 14},
            {"input": [11, 17], "answer": 4, "explanation": 1},
            {"input": [6, 4], "answer": 2, "explanation": 1},
            {"input": [42, 13], "answer": 5, "explanation": 4},
            {"input": [66, 81], "answer": 10, "explanation": 1},
            {"input": [76, 65], "answer": 10, "explanation": 7},
            {"input": [84, 78], "answer": 6, "explanation": 15},
            {"input": [92, 62], "answer": 1, "explanation": 0},
            {"input": [100, 1], "answer": 6, "explanation": 0},
            {"input": [200, 202], "answer": 2, "explanation": 0},
        ],
        "Extra": [
            {"input": [2, 8], "answer": 1, "explanation": 0},
            {"input": [9, 1], "answer": 2, "explanation": 2},
            {"input": [16, 19], "answer": 3, "explanation": 7},
            {"input": [55, 11], "answer": 6, "explanation": 17},
            {"input": [11, 15], "answer": 4, "explanation": 1},
            {"input": [21, 17], "answer": 4, "explanation": 6},
            {"input": [41, 13], "answer": 6, "explanation": 1},
            {"input": [77, 81], "answer": 4, "explanation": 79},
            {"input": [55, 65], "answer": 8, "explanation": 32},
            {"input": [92, 32], "answer": 8, "explanation": 0},
            {"input": [101, 1], "answer": 6, "explanation": 0},
            {"input": [300, 302], "answer": 2, "explanation": 0},
            {"input": [999, 998], "answer": 1, "explanation": 0},
            {"input": [84, 68], "answer": 10, "explanation": 37},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert hex_spiral(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert hex_spiral(*i['input']) == i['answer']
