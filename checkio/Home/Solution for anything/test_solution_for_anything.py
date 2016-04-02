import unittest

from solution_for_anything import checkio  # noqa


class Tests(unittest.TestCase):
    TESTS = {
        "1. Basics": [
            {
                "input": "checkio({}) != []"
            },
            {
                "input": "checkio('Hello') < 'World'"
            },
            {
                "input": "checkio(80) > 81"
            },
            {
                "input": "checkio(5) == ord"
            },
            {
                "input": 'checkio({1, 2, 3}) == {1, 2, 3}'
            }
        ],
        "2. Module": [
            {
                "input": "checkio(re) >= re"
            },
            {
                "input": "checkio(re) <= math"
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['1. Basics']:
            assert eval(i['input']), i['input']

    def test_Extra(self):
        import re  # noqa
        import math  # noqa
        for i in self.TESTS['2. Module']:
            assert eval(i['input']), i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
