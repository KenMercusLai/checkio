import unittest

from counting_tiles import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": 2, "answer": [4, 12]},
            {"input": 3, "answer": [16, 20]},
            {"input": 2.1, "answer": [4, 20]},
            {"input": 2.5, "answer": [12, 20]},
            {"input": 1, "answer": [0, 4]},
            {"input": 4, "answer": [32, 28]},
            {"input": 0.5, "answer": [0, 4]},
            {"input": 3.5, "answer": [24, 28]},
            {"input": 3.8, "answer": [32, 28]},
        ],
        "Extra": [
            {"input": 1.1, "answer": [0, 12]},
            {"input": 2.2, "answer": [4, 20]},
            {"input": 3.3, "answer": [24, 28]},
            {"input": 0.9, "answer": [0, 4]},
            {"input": 2.7, "answer": [12, 20]},
            {"input": 3.4, "answer": [24, 28]},
            {"input": 0.1, "answer": [0, 4]},
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
