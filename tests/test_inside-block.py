import unittest
from .. import inside_block


class Tests(unittest.TestCase):

    def test_basics(self):
        assert inside_block.is_inside([[1, 1], [1, 3], [3, 3], [3, 1]],
                                      [2, 2]) == True
        assert inside_block.is_inside([[1, 1], [1, 3], [3, 3], [3, 1]],
                                      [4, 2]) == False
        assert inside_block.is_inside([[1, 1], [4, 1], [2, 3]],
                                      [3, 2]) == True
        assert inside_block.is_inside([[1, 1], [4, 1], [1, 3]],
                                      [3, 3]) == False
        assert inside_block.is_inside([[2, 1], [4, 1], [5, 3], [3, 4], [1, 3]],
                                      [4, 3]) == True
        assert inside_block.is_inside([[2, 1], [4, 1], [3, 2], [3, 4], [1, 3]],
                                      [4, 3]) == False
        assert inside_block.is_inside([[1, 1], [3, 2], [5, 1], [4, 3], [5, 5], [3, 4], [1, 5], [2, 3]],
                                      [3, 3]) == True
        assert inside_block.is_inside([[1, 1], [1, 5], [5, 5], [5, 4], [2, 4], [2, 2], [5, 2], [5, 1]],
                                      [4, 3]) == False

    def test_extra(self):
        assert inside_block.is_inside([[3, 4], [4, 2], [2, 1], [1, 3]],
                                      [2, 2]) == True
        assert inside_block.is_inside([[5, 1], [4, 4], [2, 4], [1, 1]],
                                      [3, 5]) == False
        assert inside_block.is_inside([[2, 5], [2, 2], [5, 2], [1, 1]],
                                      [3, 3]) == False
        assert inside_block.is_inside([[1, 1], [1, 3], [3, 3], [3, 1]],
                                      [1, 1]) == True
        assert inside_block.is_inside([[1, 1], [1, 3], [3, 3], [3, 1]],
                                      [3, 2]) == True
        assert inside_block.is_inside([[1, 1], [2, 6], [3, 1]],
                                      [2, 2]) == True
        assert inside_block.is_inside([[1, 1], [1, 3], [2, 4], [4, 4], [4, 3], [2, 1]],
                                      [2, 3]) == True
        assert inside_block.is_inside([[1, 1], [1, 3], [2, 4], [4, 4], [4, 3], [2, 1]],
                                      [3, 1]) == False
        assert inside_block.is_inside([[1, 1], [2, 3], [1, 3], [3, 4], [5, 3], [4, 3], [3, 1]],
                                      [2, 2]) == True
        assert inside_block.is_inside([[1, 1], [2, 3], [1, 3], [3, 4], [5, 3], [4, 3], [3, 1]],
                                      [1, 2]) == False
        assert inside_block.is_inside([[1, 1], [2, 4], [5, 4], [4, 1], [3, 1], [4, 3], [3, 3], [2, 1]],
                                      [2, 2]) == True
        assert inside_block.is_inside([[1, 1], [2, 4], [5, 4], [4, 1], [3, 1], [4, 3], [3, 3], [2, 1]],
                                      [3, 2]) == False
        assert inside_block.is_inside([[4, 2], [2, 4], [0, 3], [2, 3], [3, 2], [3, 0]],
                                      [3, 3]) == True
        assert inside_block.is_inside([[0, 0], [1, 1], [0, 2], [1, 3], [0, 4], [2, 4], [2, 0]],
                                      [1, 2]) == True
        assert inside_block.is_inside([[0, 0], [0, 4], [2, 4], [1, 3], [2, 2], [1, 1], [2, 0]],
                                      [1, 2]) == True
        assert inside_block.is_inside([[0, 0], [1, 1], [2, 0], [3, 1], [4, 0], [4, 2], [0, 2]],
                                      [2, 1]) == True
        assert inside_block.is_inside([[0, 0], [4, 0], [4, 2], [3, 1], [2, 2], [1, 1], [0, 2]],
                                      [2, 1]) == True
        assert inside_block.is_inside([[1, 1], [2, 3], [1, 3], [2, 5], [1, 5], [3, 8], [5, 5], [4, 5], [5, 3], [4, 3],
                                       [5, 1], [3, 3]],
                                      [3, 7]) == True
        assert inside_block.is_inside([[1, 1], [2, 3], [1, 3], [2, 5], [1, 5], [3, 8], [5, 5], [4, 5], [5, 3], [4, 3],
                                       [5, 1], [3, 3]],
                                      [3, 2]) == False
        assert inside_block.is_inside([[5, 1], [1, 5], [5, 9], [9, 5], [5, 5]],
                                      [5, 5]) == True
        assert inside_block.is_inside([[5, 1], [1, 5], [5, 9], [9, 5], [5, 5]],
                                      [6, 4]) == False
