import unittest

from achilles_and_the_tortoise import chase


def almost_equal(checked, correct, significant_digits):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [6, 3, 2], "answer": 4.0},
            {"input": [10, 1, 10], "answer": 11.111_111_111},
        ],
        "Edge": [
            {"input": [2, 1, 1], "answer": 2.0},
            {"input": [342, 1, 60], "answer": 60.175_953_079},
            {"input": [342, 341, 1], "answer": 342.0},
            {"input": [342, 341, 60], "answer": 20520.0},
        ],
        "Extra": [
            {"input": [213, 202, 37], "answer": 716.454_545_455},
            {"input": [330, 150, 57], "answer": 104.5},
            {"input": [26, 13, 59], "answer": 118.0},
            {"input": [106, 101, 16], "answer": 339.2},
            {"input": [15, 13, 56], "answer": 420.0},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert almost_equal(chase(*i['input']), i['answer'], 8)

    def test_Edge(self):
        for i in self.TESTS['Edge']:
            assert almost_equal(chase(*i['input']), i['answer'], 8)

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert almost_equal(chase(*i['input']), i['answer'], 8)
