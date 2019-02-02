import unittest

from shoot_range import shot


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ((2, 2), (5, 7), (11, 2), (8, 3)),
                "answer": 100,
                "explanation": [3.5, 4.5]
            },
            {
                "input": ((2, 2), (5, 7), (11, 2), (7, 2)),
                "answer": 0,
                "explanation": [2.0, 2.0]
            },
            {
                "input": ((2, 2), (5, 7), (11, 2), (8, 4)),
                "answer": 29,
                "explanation": [4.571428571428571, 6.285714285714286]
            },
            {
                "input": ((2, 2), (5, 7), (11, 2), (9, 5)),
                "answer": -1,
                "explanation": [6.2631578947368425, 9.105263157894736]
            },
            {
                "input": ((2, 2), (5, 7), (11, 2), (10.5, 3)),
                "answer": -1,
                "explanation": [6.909090909090909, 10.181818181818182]
            },
        ],
        "Extra": [
            {
                "input": ((2, 2), (5, 7), (8, 3), (11, 2)),
                "answer": -1,
                "explanation": [14, 1]
            },
            {
                "input": ((1, 1), (99, 99), (99, 1), (41, 39)),
                "answer": 79,
                "explanation": [39.791666666666664, 39.791666666666664]
            },
            {
                "input": ((10, 10), (10, 90), (50, 90), (50, 50)),
                "answer": -1,
                "explanation": None
            },
            {
                "input": ((10, 10), (10, 90), (50, 60), (70, 60)),
                "answer": -1,
                "explanation": None
            },
            {
                "input": ((10, 10), (10, 90), (70, 60), (50, 60)),
                "answer": 75,
                "explanation": [10.0, 60.0]
            },
            {
                "input": ((2, 2), (10, 2), (5, 10), (5, 5)),
                "answer": 75,
                "explanation": [5.0, 2.0]
            },
            {
                "input": ((2, 2), (10, 2), (5, 10), (3, 5)),
                "answer": -1,
                "explanation": [1.8, 2.0]
            },
            {
                "input": ((2, 2), (10, 2), (5, 10), (4, 5)),
                "answer": 35,
                "explanation": [3.4, 2.0]
            },
            {
                "input": ((2, 10), (10, 2), (10, 10), (3, 10)),
                "answer": 0,
                "explanation": [2.0, 10.0]
            },
            {
                "input": ((2, 10), (10, 2), (10, 10), (10, 4)),
                "answer": 0,
                "explanation": [10.0, 2.0]
            },
            {
                "input": ((2, 10), (10, 2), (10, 10), (3, 10.1)),
                "answer": -1,
                "explanation": [1.8840579710144931, 10.115942028985506]
            },
            {
                "input": ((2, 10), (10, 2), (10, 10), (3, 9.9)),
                "answer": 3,
                "explanation": [2.1126760563380276, 9.887323943661972]
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert shot(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert shot(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
