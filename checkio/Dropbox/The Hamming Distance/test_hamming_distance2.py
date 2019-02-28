import unittest

from hamming_distance2 import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [117, 17], "answer": 3},
            {"input": [1, 2], "answer": 2},
            {"input": [16, 15], "answer": 5},
            {"input": [255, 1], "answer": 7},
            {"input": [16, 16], "answer": 0},
            {"input": [204, 157], "answer": 3},
            {"input": [31, 51], "answer": 3},
            {"input": [84, 198], "answer": 3},
            {"input": [57, 39], "answer": 4},
            {"input": [140, 160], "answer": 3},
            {"input": [16, 128], "answer": 2},
            {"input": [2, 255], "answer": 7},
            {"input": [100, 200], "answer": 4},
            {"input": [255, 1], "answer": 7},
        ],
        "Extra": [
            {"input": [1, 999_999], "answer": 11},
            {"input": [999_999, 1], "answer": 11},
            {"input": [1, 524_287], "answer": 18},
            {"input": [524_288, 524_287], "answer": 20},
            {"input": [100_000, 50], "answer": 7},
            {"input": [193_521, 872_992], "answer": 11},
            {"input": [249_994, 104_391], "answer": 9},
            {"input": [679_972, 710_253], "answer": 8},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
