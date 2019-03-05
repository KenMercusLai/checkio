import math  # noqa
import re  # noqa
import unittest

from solution_for_anything import checkio  # noqa


class Tests(unittest.TestCase):
    TESTS = {
        "1. Basics": [
            {"input": "checkio({1, 2, 3}) == {1, 2, 3}"},
            {"input": "checkio({}) != []"},
            {"input": "checkio('Hello') < 'World'"},
            {"input": "checkio(80) > 81"},
            {"input": "checkio(re) >= re"},
            {"input": "checkio(re) <= math"},
            {"input": "checkio(5) == ord"},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['1. Basics']:
            assert eval(i['input']), i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
