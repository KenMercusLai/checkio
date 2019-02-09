import unittest

from bats_bunker import checkio, numbers, path_coordinates


def almost_equal(checked, correct, significant_digits=2):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ["B--", "---", "--A"],
                "answer": 2.83,
                "explanation": [[0, 0, 0], [2, 2, 2.83]],
            },
            {
                "input": ["B-B", "BW-", "-BA"],
                "answer": 4,
                "explanation": [[0, 0, 0], [0, 2, 2], [2, 2, 4]],
            },
            {
                "input": ["BWB--B", "-W-WW-", "B-BWAB"],
                "answer": 12,
                "explanation": [
                    [0, 0, 0],
                    [2, 0, 2],
                    [2, 2, 4],
                    [0, 2, 6],
                    [0, 5, 9],
                    [2, 5, 11],
                    [2, 4, 12],
                ],
            },
            {
                "input": ["B---B-", "-WWW-B", "-WA--B", "-W-B--", "-WWW-B", "B-BWB-"],
                "answer": 9.24,
                "explanation": [[0, 0, 0], [0, 4, 4], [2, 5, 6.24], [2, 2, 9.24]],
            },
        ],
        "Extra": [
            {
                "input": ["BW-", "--A", "B--"],
                "answer": 4.24,
                "explanation": [[0, 0, 0], [2, 0, 2], [1, 2, 4.24]],
            },
            {"input": ["A--", "---", "---"], "answer": 0, "explanation": []},
            {
                "input": ["B-B-B", "-WWW-", "BWA-B", "-WWW-", "B-B-B"],
                "answer": 8,
                "explanation": [[0, 0, 0], [0, 4, 4], [2, 4, 6], [2, 2, 8]],
            },
            {
                "input": ["BWA-B-", "-W----", "-WW-B-", "-W---B", "--B---", "B-B---"],
                "answer": 12.83,
                "explanation": [[0, 0, 0], [5, 0, 5], [2, 4, 10.07], [0, 2, 12.83]],
            },
            {
                "input": [
                    "B-B--B-",
                    "-W-W-W-",
                    "--B---B",
                    "BW-W-W-",
                    "----A--",
                    "BW-W-W-",
                    "-B--B-B",
                ],
                "answer": 16,
                "explanation": [
                    [0, 0, 0],
                    [0, 2, 2],
                    [2, 2, 4],
                    [2, 6, 8],
                    [6, 6, 12],
                    [6, 4, 14],
                    [4, 4, 16],
                ],
            },
            {
                "input": ["BBBBB", "BBBBB", "BBBBB", "BBBBB", "BBBBA"],
                "answer": 5.66,
                "explanation": [[0, 0, 0], [4, 4, 5.66]],
            },
            {
                "input": ["B-----", "-BBB--", "-WWBW-", "-----A", "B-W-B-"],
                "answer": 7.81,
                "explanation": [
                    [0, 0, 0],
                    [1, 3, 3.16],
                    [2, 3, 4.16],
                    [4, 4, 6.40],
                    [3, 5, 7.81],
                ],
            },
        ],
    }

    def test_numbers(self):
        assert list(numbers(0, 5)) == [0, 1, 2, 3, 4, 5]
        assert list(numbers(5, 0)) == [0, -1, -2, -3, -4, -5]
        assert list(numbers(-5, -10)) == [0, -1, -2, -3, -4, -5]
        assert list(numbers(-10, -5)) == [0, 1, 2, 3, 4, 5]

    def test_path_coordinates(self):
        assert set(path_coordinates((0, 0), (1, 1))) == set(
            [(0, 0), (0, 1), (1, 0), (1, 1)]
        )
        assert set(path_coordinates((2, 2), (0, 0))) == set(
            [(2, 2), (2, 1), (1, 2), (1, 1), (1, 0), (0, 1), (0, 0)]
        )
        assert set(path_coordinates((0, 0), (0, 2))) == set([(0, 0), (0, 1), (0, 2)])
        assert set(path_coordinates((0, 0), (1, 2))) == set(
            [(0, 0), (0, 1), (1, 1), (1, 2)]
        )

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert almost_equal(checkio(i['input']), i['answer'])

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert almost_equal(checkio(i['input']), i['answer'])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
