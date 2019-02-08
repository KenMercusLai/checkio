import unittest

from unlucky_days import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": 1634, "answer": 2},
            {"input": 2873, "answer": 2},
            {"input": 1586, "answer": 1},
            {"input": 2689, "answer": 2},
            {"input": 2819, "answer": 2},
            {"input": 2792, "answer": 2},
            {"input": 2723, "answer": 2},
            {"input": 1909, "answer": 1},
            {"input": 1812, "answer": 2},
            {"input": 1618, "answer": 2},
            {"input": 2132, "answer": 1},
            {"input": 2065, "answer": 3},
            {"input": 1594, "answer": 1},
            {"input": 2473, "answer": 2},
            {"input": 1797, "answer": 2},
            {"input": 2956, "answer": 2},
            {"input": 2478, "answer": 1},
            {"input": 2580, "answer": 1},
            {"input": 2662, "answer": 1},
            {"input": 2719, "answer": 1},
            {"input": 1880, "answer": 2},
            {"input": 2919, "answer": 2},
            {"input": 1927, "answer": 1},
            {"input": 2298, "answer": 1},
            {"input": 2255, "answer": 2},
            {"input": 2326, "answer": 1},
            {"input": 2886, "answer": 2},
            {"input": 2833, "answer": 1},
            {"input": 2837, "answer": 3},
            {"input": 2995, "answer": 3},
            {"input": 2824, "answer": 2},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
