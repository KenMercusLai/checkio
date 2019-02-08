import unittest

from number_base import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": ["AF", 16], "answer": 175},
            {"input": ["101", 2], "answer": 5},
            {"input": ["101", 5], "answer": 26},
            {"input": ["Z", 36], "answer": 35},
            {"input": ["AB", 10], "answer": -1},
        ],
        "Extra": [
            {"input": ['F0', 16], "answer": 240},
            {"input": ['1111111111', 2], "answer": 1023},
            {"input": ['255', 7], "answer": 138},
            {"input": ['IDDQD', 30], "answer": 14_943_493},
            {"input": ['1000', 10], "answer": 1000},
            {"input": ['ASD', 15], "answer": -1},
            {"input": ['222', 3], "answer": 26},
            {"input": ['XYZ', 36], "answer": 44027},
            {"input": ['909', 9], "answer": -1},
            {"input": ['1234567890', 11], "answer": 2_853_116_695},
            {"input": ['5A6E', 10], "answer": -1},
            {"input": ['1000000', 31], "answer": 887_503_681},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input'][0], i['input'][1]) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input'][0], i['input'][1]) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
