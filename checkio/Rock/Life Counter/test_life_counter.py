import unittest

from life_counter import life_counter


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [
                    (
                        (0, 1, 0, 0, 0, 0, 0),
                        (0, 0, 1, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1),
                        (0, 0, 0, 0, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0),
                    ),
                    4,
                ],
                "answer": 15,
                "explanation": (0, 7, 0, 6),
            },
            {
                "input": [
                    (
                        (0, 1, 0, 0, 0, 0, 0),
                        (0, 0, 1, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1),
                        (0, 0, 0, 0, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0),
                    ),
                    15,
                ],
                "answer": 14,
                "explanation": (0, 7, -3, 6),
            },
            {
                "input": [((0, 1, 0), (0, 0, 1), (1, 1, 1)), 50],
                "answer": 5,
                "explanation": (0, 15, 0, 14),
            },
            {
                "input": [
                    (
                        (1, 1, 0, 1, 1),
                        (1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0),
                        (1, 1, 0, 1, 1),
                        (1, 1, 0, 1, 1),
                    ),
                    100,
                ],
                "answer": 16,
                "explanation": (0, 4, 0, 4),
            },
        ],
        "Extra": [
            {
                "input": [
                    (
                        (0, 0, 0, 0, 0, 0, 1, 0),
                        (1, 1, 0, 0, 0, 0, 0, 0),
                        (0, 1, 0, 0, 0, 1, 1, 1),
                    ),
                    129,
                ],
                "answer": 2,
                "explanation": (-4, 18, -6, 11),
            },
            {
                "input": [
                    (
                        (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                        (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                        (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                        (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
                        (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                        (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                        (1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0),
                    ),
                    100,
                ],
                "answer": 56,
                "explanation": (-1, 13, -1, 13),
            },
            {
                "input": [
                    (
                        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                        (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1),
                        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
                        (0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0),
                    ),
                    42,
                ],
                "answer": 36,
                "explanation": (-12, 10, -1, 16),
            },
            {
                "input": [
                    (
                        (0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1),
                        (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                    ),
                    100,
                ],
                "answer": 33,
                "explanation": (-9, 15, -5, 22),
            },
            {
                "input": [((0, 1, 0), (0, 0, 1), (1, 1, 1)), 999],
                "answer": 5,
                "explanation": None,
            },
            {
                "input": [
                    (
                        (0, 1, 0, 0, 0, 0, 1, 0),
                        (1, 0, 0, 0, 0, 0, 0, 1),
                        (1, 1, 1, 0, 0, 1, 1, 1),
                    ),
                    999,
                ],
                "answer": 10,
                "explanation": None,
            },
            {
                "input": [
                    (
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                        (0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1),
                    ),
                    100,
                ],
                "answer": 52,
                "explanation": (-18, 20, -5, 20),
            },
            {
                "input": [
                    (
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                    ),
                    10,
                ],
                "answer": 22,
                "explanation": (0, 17, 0, 16),
            },
            {
                "input": [
                    (
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                    ),
                    20,
                ],
                "answer": 0,
                "explanation": (0, 17, 0, 16),
            },
            {
                "input": [
                    (
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 1, 1, 1),
                        (0, 0, 0, 0, 0, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0),
                        (0, 0, 0, 0, 0, 0, 0, 0),
                        (1, 1, 1, 0, 0, 0, 0, 0),
                        (0, 0, 0, 0, 0, 1, 1, 1),
                        (0, 0, 0, 0, 0, 1, 0, 0),
                        (0, 0, 0, 0, 0, 0, 1, 0),
                        (1, 1, 1, 0, 0, 0, 0, 0),
                    ),
                    100,
                ],
                "answer": 3,
                "explanation": (-1, 10, -2, 7),
            },
            {
                "input": [
                    [
                        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                        [0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                        [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                        [1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                        [1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
                        [0, 1, 1, 0, 0, 1, 0, 1, 1, 1],
                        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                        [0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                        [0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
                    ],
                    50,
                ],
                "answer": 74,
                "explanation": (-6, 13, -5, 24),
            },
            {
                "input": [
                    [
                        [1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
                        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                        [0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
                        [0, 1, 1, 1, 0, 1, 1, 1, 0, 0],
                        [1, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                        [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
                        [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 1, 0, 1, 0, 1, 1],
                    ],
                    50,
                ],
                "answer": 79,
                "explanation": (-5, 17, -14, 16),
            },
            {
                "input": [
                    [
                        [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
                        [1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                        [1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                    ],
                    50,
                ],
                "answer": 81,
                "explanation": (-9, 15, -4, 24),
            },
            {
                "input": [
                    [
                        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                        [1, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                        [0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
                        [0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                        [1, 1, 0, 0, 0, 1, 1, 1, 1, 0],
                    ],
                    50,
                ],
                "answer": 18,
                "explanation": (-3, 16, -5, 13),
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert life_counter(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert life_counter(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()