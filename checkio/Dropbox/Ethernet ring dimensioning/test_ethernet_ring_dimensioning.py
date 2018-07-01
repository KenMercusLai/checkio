import unittest

from ethernet_ring_dimensioning import (
    checkio, generate_path, segment_bandwidth,
)


def test_generate_path():
    assert generate_path('AEFCBG', 'A', 'B') == 'AGB'
    assert generate_path('AEFCBG', 'B', 'A') == 'AGB'
    assert generate_path('AEFCBG', 'C', 'A') == 'CBGA'
    assert generate_path('AEFCBG', 'A', 'C') == 'AEFC'
    assert generate_path('AEFCBG', 'E', 'C') == 'EFC'


def test_segment_bandwidth():
    assert segment_bandwidth('AEFCBG',
                             [("AC", 5), ("EC", 10), ("AB", 60)]) == {'AE': 5,
                                                                      'EF': 15,
                                                                      'FC': 15,
                                                                      'CB': 0,
                                                                      'BG': 60,
                                                                      'GA': 60}


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ["AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)],
                "answer": [2, 2, 1, 0, 0]
            },
            {
                "input": ["ABCDEFGH", ("AD", 4)],
                "answer": [0, 0, 3, 0, 0]
            },
            {
                "input": ["ABCDEFGH", ("AD", 4), ("EA", 41)],
                "answer": [4, 0, 3, 0, 0]
            }
        ],
        "Extra": [
            {
                "input": ["ADBC", ["AD", 1], ["DB", 9],
                          ["BC", 0.345], ["CA", 13]],
                "answer": [0, 1, 1, 2, 0]
            },
            {
                "input": ["ABCDEFGH", ["AD", 4], ["DA", 4]],
                "answer": [0, 0, 3, 0, 0]
            },
            {
                "input": ["ABCDEFGH", ["AE", 170], ["EA", 10000], ["HF", 1]],
                "answer": [410, 0, 0, 0, 0]
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input'][0], *i['input'][1:]) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input'][0], *i['input'][1:]) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
