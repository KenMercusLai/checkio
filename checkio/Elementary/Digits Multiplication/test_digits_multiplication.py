import unittest

from digits_multiplication import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": 123405,
                "answer": 120
            },
            {
                "input": 999,
                "answer": 729
            },
            {
                "input": 1000,
                "answer": 1
            },
            {
                "input": 1111,
                "answer": 1
            },

        ],
        "Extra": [
            {
                "input": 999999,
                "answer": 531441
            },
            {
                "input": 1,
                "answer": 1
            },
            {
                "input": 9,
                "answer": 9,
            },
            {
                "input": 736635,
                "answer": 11340
            },
            {
                "input": 375251,
                "answer": 1050
            },
            {
                "input": 778241,
                "answer": 3136
            },
            {
                "input": 930154,
                "answer": 540
            },
            {
                "input": 306026,
                "answer": 216
            },
            {
                "input": 194325,
                "answer": 1080
            },
            {
                "input": 376087,
                "answer": 7056
            },
            {
                "input": 550643,
                "answer": 1800
            },
            {
                "input": 90160,
                "answer": 54
            },
            {
                "input": 232177,
                "answer": 588
            },
            {
                "input": 951216,
                "answer": 540
            },
            {
                "input": 273438,
                "answer": 4032
            },
            {
                "input": 256991,
                "answer": 4860
            },
            {
                "input": 542929,
                "answer": 6480
            },
            {
                "input": 399996,
                "answer": 118098
            },
            {
                "input": 929806,
                "answer": 7776
            },
            {
                "input": 638332,
                "answer": 2592
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
