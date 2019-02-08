import unittest

from double_substring import (
    double_substring,
    find_repeated_chars,
    non_overlapping_range,
)


def test_find_repeated_chars():
    assert find_repeated_chars('aaabbbcc') == {
        'a': [0, 1, 2],
        'b': [3, 4, 5],
        'c': [6, 7],
    }

    assert find_repeated_chars('ababcbac') == {
        'a': [0, 2, 6],
        'b': [1, 3, 5],
        'c': [4, 7],
    }

    assert find_repeated_chars('aaaa') == {'a': [0, 1, 2, 3]}

    assert find_repeated_chars('abc') == {}


def test_non_overlapping_range():
    assert non_overlapping_range([0, 1, 2], 'aaabbbcc') == [
        (0, 1, 1),
        (0, 2, 1),
        (0, 2, 2),
        (1, 2, 1),
    ]

    assert non_overlapping_range([0, 2, 6], 'ababcbac') == [
        (0, 2, 1),
        (0, 2, 2),
        (0, 6, 1),
        (0, 6, 2),
        (2, 6, 1),
        (2, 6, 2),
    ]

    assert non_overlapping_range([0, 1, 2, 3], 'aaaa') == [
        (0, 1, 1),
        (0, 2, 1),
        (0, 2, 2),
        (0, 3, 1),
        (1, 2, 1),
        (1, 3, 1),
        (2, 3, 1),
    ]


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": "aaaa", "answer": 2},
            {"input": "abc", "answer": 0},
            {"input": "aghtfghkofgh", "answer": 3},
        ],
        "Extra": [
            {"input": "", "answer": 0},
            {"input": "abababaab", "answer": 3},
            {"input": "arefhjaref!!", "answer": 4},
            {"input": "aa", "answer": 1},
            {"input": "aaaaa", "answer": 2},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert double_substring(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert double_substring(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
