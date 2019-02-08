import unittest

from easy_unpack import easy_unpack


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [1, 2, 3, 4, 5, 6, 7, 9], "answer": (1, 3, 7)},
            {"input": [1, 1, 1, 1], "answer": (1, 1, 1)},
            {"input": [6, 3, 7], "answer": (6, 7, 3)},
        ],
        "Extra": [
            {"input": [30, 40, 100], "answer": (30, 100, 40)},
            {"input": [5, 5, 5, 5, 5, 5], "answer": (5, 5, 5)},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert easy_unpack(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert easy_unpack(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
