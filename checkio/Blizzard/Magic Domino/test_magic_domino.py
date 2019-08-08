import itertools
import random
import unittest

import pytest

from magic_domino import magic_domino


class Tests(unittest.TestCase):
    extra_tests_count = 3

    TESTS = {"Basics": [], "Extra": []}

    def setUp(self):
        for n in range(5, 20):
            self.TESTS["Basics"].append({"input": (4, n), "answer": (4, n)})

        for n in random.sample(range(13, 24), self.extra_tests_count):
            self.TESTS["Extra"].append({"input": (6, n), "answer": (6, n)})

    def check_data(self, size, number, user_result):
        # check types
        check_container_type = lambda o: any(
            map(lambda t: isinstance(o, t), (list, tuple))
        )
        check_cell_type = lambda i: isinstance(i, int)
        if not (
            check_container_type(user_result)
            and all(map(check_container_type, user_result))
            and all(map(lambda row: all(map(check_cell_type, row)), user_result))
        ):
            raise Exception(
                "You should return a list/tuple of lists/tuples with integers."
            )

        # check sizes
        check_size = lambda o: len(o) == size
        if not (check_size(user_result) and all(map(check_size, user_result))):
            raise Exception("Wrong size of answer.")

        # check is it a possible numbers (from 0 to 6 inclusive)
        if not all(
            map(lambda x: 0 <= x <= 6, itertools.chain.from_iterable(user_result))
        ):
            raise Exception("Wrong matrix integers (can't be domino tiles)")

        # check is it a magic square
        seq_sum_check = lambda seq: sum(seq) == number
        diagonals_indexes = zip(
            *map(lambda i: ((i, i), (i, size - i - 1)), range(size))
        )
        values_from_indexes = lambda inds: itertools.starmap(
            lambda x, y: user_result[y][x], inds
        )
        if not (
            all(map(seq_sum_check, user_result))
            and all(map(seq_sum_check, zip(*user_result)))  # rows
            and all(  # columns
                map(seq_sum_check, map(values_from_indexes, diagonals_indexes))
            )
        ):  # diagonals
            raise Exception("It's not a magic square.")

        # check is it domino square
        tiles = set()
        for x, y in itertools.product(range(size), range(0, size, 2)):
            tile = tuple(sorted((user_result[y][x], user_result[y + 1][x])))
            if tile in tiles:
                raise Exception("It's not a domino magic square.")
            tiles.add(tile)

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            self.check_data(i['answer'][0], i['answer'][1], magic_domino(*i['input']))

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            self.check_data(i['answer'][0], i['answer'][1], magic_domino(*i['input']))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
