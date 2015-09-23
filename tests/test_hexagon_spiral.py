import unittest
from ..hexagon_spiral import hex_spiral


class Tests(unittest.TestCase):

    def test_Basics(self):
        assert hex_spiral(2, 9) == 1
        assert hex_spiral(9, 2) == 1
        assert hex_spiral(6, 19) == 2
        assert hex_spiral(5, 11) == 3
        assert hex_spiral(13, 15) == 2
        assert hex_spiral(11, 17) == 4
        assert hex_spiral(6, 4) == 2
        assert hex_spiral(42, 13) == 5
        assert hex_spiral(66, 81) == 10
        assert hex_spiral(76, 65) == 10
        assert hex_spiral(84, 78) == 6
        assert hex_spiral(92, 62) == 1
        assert hex_spiral(100, 1) == 6
        assert hex_spiral(200, 202) == 2

    def test_Extra(self):
        assert hex_spiral(2, 8) == 1
        assert hex_spiral(9, 1) == 2
        assert hex_spiral(16, 19) == 3
        assert hex_spiral(55, 11) == 6
        assert hex_spiral(11, 15) == 4
        assert hex_spiral(21, 17) == 4
        assert hex_spiral(41, 13) == 6
        assert hex_spiral(77, 81) == 4
        assert hex_spiral(55, 65) == 8
        assert hex_spiral(92, 32) == 8
        assert hex_spiral(101, 1) == 6
        assert hex_spiral(300, 302) == 2
        assert hex_spiral(999, 998) == 1
        assert hex_spiral(84, 68) == 10
