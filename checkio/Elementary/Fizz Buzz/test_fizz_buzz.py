import unittest

from fizz_buzz import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": 15, "answer": "Fizz Buzz"},
            {"input": 6, "answer": "Fizz"},
            {"input": 10, "answer": "Buzz"},
            {"input": 7, "answer": "7"},
        ],
        "Edge": [
            {"input": 1000, "answer": "Buzz"},
            {"input": 1, "answer": "1"},
            {"input": 990, "answer": "Fizz Buzz"},
        ],
        "Extra": [
            {"input": 45, "answer": "Fizz Buzz"},
            {"input": 46, "answer": "46"},
            {"input": 47, "answer": "47"},
            {"input": 48, "answer": "Fizz"},
            {"input": 49, "answer": "49"},
            {"input": 50, "answer": "Buzz"},
            {"input": 999, "answer": "Fizz"},
            {"input": 1000, "answer": "Buzz"},
            {"input": 989, "answer": "989"},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer'], i['input']

    def test_Edge(self):
        for i in self.TESTS['Edge']:
            assert checkio(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
