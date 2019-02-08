import unittest

from making_change import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [8, [1, 3, 5]], "answer": 2},
            {"input": [12, [1, 4, 5]], "answer": 3},
        ],
        "Extra": [
            {"input": [1, [3, 4, 5]], "answer": None},
            {"input": [4, [3, 5]], "answer": None},
            {"input": [123_456, [1, 6, 7, 456, 678]], "answer": 187},
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
