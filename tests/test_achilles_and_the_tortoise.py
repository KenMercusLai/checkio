import unittest
from ..achilles_and_the_tortoise import chase


def almost_equal(checked, correct, significant_digits):
    precision = 0.1 ** significant_digits
    return correct - precision < checked < correct + precision


class Tests(unittest.TestCase):

    def test_Basics(self):
        assert almost_equal(chase(6, 3, 2), 4.0, 8)
        assert almost_equal(chase(10, 1, 10), 11.111111111, 8)

    def test_Extra(self):
        assert almost_equal(chase(213, 202, 37), 716.454545455, 8)
        assert almost_equal(chase(330, 150, 57), 104.5, 8)
        assert almost_equal(chase(26, 13, 59), 118.0, 8)
        assert almost_equal(chase(106, 101, 16), 339.2, 8)
        assert almost_equal(chase(15, 13, 56), 420.0, 8)

    def test_Edge(self):
        assert almost_equal(chase(2, 1, 1), 2.0, 8)
        assert almost_equal(chase(342, 1, 60), 60.175953079, 8)
        assert almost_equal(chase(342, 341, 1), 342.0, 8)
        assert almost_equal(chase(342, 341, 60), 20520.0, 8)
