import unittest

from days_between import days_diff


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": ((1982, 4, 19), (1982, 4, 22)), "answer": 3},
            {"input": ((2014, 1, 1), (2014, 8, 27)), "answer": 238},
            {"input": ((2014, 8, 27), (2014, 1, 1)), "answer": 238},
        ],
        "Extra": [
            {"input": ((1, 1, 1), (9999, 12, 31)), "answer": 3_652_058},
            {"input": ((9999, 12, 31), (1, 1, 1)), "answer": 3_652_058},
            {"input": ((1970, 1, 1), (2000, 1, 1)), "answer": 10957},
            {"input": ((2014, 2, 28), (2014, 2, 28)), "answer": 0},
            {"input": ((2012, 2, 29), (2014, 2, 28)), "answer": 730},
            {"input": ((7015, 1, 11), (8992, 2, 21)), "answer": 722_126},
            {"input": ((7410, 4, 9), (9884, 3, 16)), "answer": 903_587},
            {"input": ((4139, 10, 30), (4923, 12, 23)), "answer": 286_404},
            {"input": ((1622, 10, 4), (3555, 10, 12)), "answer": 706_021},
            {"input": ((5871, 8, 23), (6155, 6, 14)), "answer": 103_659},
            {"input": ((4632, 11, 18), (8077, 10, 26)), "answer": 1_258_238},
            {"input": ((696, 5, 7), (9241, 6, 27)), "answer": 3_121_048},
            {"input": ((6051, 1, 23), (4129, 8, 9)), "answer": 701_798},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert days_diff(i['input'][0], i['input'][1]) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert days_diff(i['input'][0], i['input'][1]) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
