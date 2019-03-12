import unittest

from stick_sawing import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": 64, "answer": [15, 21, 28]},
            {"input": 371, "answer": [36, 45, 55, 66, 78, 91]},
            {"input": 225, "answer": [105, 120]},
            {"input": 882, "answer": []},
        ],
        "Extra": [
            {"input": 631, "answer": [190, 210, 231]},
            {"input": 130, "answer": [21, 28, 36, 45]},
            {"input": 216, "answer": [6, 10, 15, 21, 28, 36, 45, 55]},
            {"input": 219, "answer": [3, 6, 10, 15, 21, 28, 36, 45, 55]},
            {"input": 994, "answer": []},
            {"input": 454, "answer": [3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]},
            {"input": 136, "answer": [36, 45, 55]},
            {"input": 5, "answer": []},
            {"input": 10, "answer": [1, 3, 6]},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
