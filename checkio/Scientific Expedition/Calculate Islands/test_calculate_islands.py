import unittest

from calculate_islands import checkio, merge


def test_merge():
    assert merge([(1, 1)], [(1, 2)]) == [(1, 1), (1, 2)]
    assert merge([(1, 1), (1, 2)], [(2, 2)]) == [(1, 1), (1, 2), (2, 2)]
    assert merge([(0, 0), (0, 1)], [(1, 1), (1, 2), (2, 2)]) == [
        (0, 0),
        (0, 1),
        (1, 1),
        (1, 2),
        (2, 2),
    ]


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                ],
                "answer": [1, 3],
                "explanation": [[1, 3, 1], [3, 1.5, 2.5]],
            },
            {
                "input": [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                ],
                "answer": [5],
                "explanation": [[5, 2.5, 2.5]],
            },
            {
                "input": [
                    [0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                "answer": [2, 3, 3, 4],
                "explanation": [[2, 1.5, 0], [3, 1, 4], [3, 3, 3], [4, 5, 2.5]],
            },
            {
                "input": [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                ],
                "answer": [24],
                "explanation": [[24, 0.5, 2]],
            },
            {
                "input": [
                    [1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 0, 1],
                    [1, 0, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1],
                ],
                "answer": [4, 20],
                "explanation": [[4, 2.5, 2.5], [20, 0, 2.5]],
            },
            {
                "input": [
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                ],
                "answer": [5, 6, 7],
                "explanation": [[5, 2, 1], [6, 2.5, 3], [7, 3, 5]],
            },
            {
                "input": [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 1, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1, 0],
                ],
                "answer": [2, 5, 8],
                "explanation": [[2, 5.5, 1], [5, 6, 4], [8, 1, 2]],
            },
            {
                "input": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                "answer": [1],
                "explanation": [[1, 1, 1]],
            },
            {
                "input": [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
                "answer": [16],
                "explanation": [[16, 1.5, 1.5]],
            },
        ],
        "Extra": [
            {
                "input": [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 0, 0],
                    [1, 1, 0, 0, 0],
                ],
                "answer": [3, 4],
                "explanation": [[3, 1.5, 2.5], [4, 3.5, 0.5]],
            },
            {
                "input": [
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0],
                ],
                "answer": [6],
                "explanation": [[6, 2.5, 2.5]],
            },
            {
                "input": [
                    [0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                ],
                "answer": [2, 3, 3, 3],
                "explanation": [[2, 1.5, 0], [3, 1, 4], [3, 3, 3], [3, 5, 3]],
            },
            {
                "input": [
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 1],
                ],
                "answer": [23],
                "explanation": [[23, 0.5, 2]],
            },
            {
                "input": [
                    [1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 0, 1],
                    [1, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1],
                ],
                "answer": [3, 20],
                "explanation": [[3, 2.5, 2.5], [20, 0, 2.5]],
            },
            {
                "input": [
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                ],
                "answer": [4, 6, 7],
                "explanation": [[4, 1.5, 1], [6, 2.5, 3], [7, 3, 5]],
            },
            {
                "input": [
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0],
                    [0, 1, 0, 1, 1, 1],
                    [0, 0, 0, 0, 1, 0],
                ],
                "answer": [2, 5, 7],
                "explanation": [[2, 5.5, 1], [5, 6, 4], [7, 1, 2]],
            },
            {
                "input": [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
                "answer": [1],
                "explanation": [[1, 0, 1]],
            },
            {
                "input": [
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                ],
                "answer": [20],
                "explanation": [[20, 2, 1.5]],
            },
            {
                "input": [
                    [1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1],
                ],
                "answer": [1, 1, 1, 1, 16],
                "explanation": [[1, 0, 0], [1, 8, 0], [1, 0, 8], [1, 8, 8], [16, 2, 4]],
            },
            {
                "input": [[1], [1], [1], [1], [1], [1], [1], [1], [1]],
                "answer": [9],
                "explanation": [[9, 4, 0]],
            },
            {
                "input": [[1, 1, 1, 1, 0, 1, 1, 1, 1]],
                "answer": [4, 4],
                "explanation": [[4, 0, 1.5], [4, 0, 6.5]],
            },
            {
                "input": [
                    [1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1],
                ],
                "answer": [17],
                "explanation": [[17, 4, 4]],
            },
            {"input": [[1]], "answer": [1], "explanation": [[1, 0, 0]]},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
