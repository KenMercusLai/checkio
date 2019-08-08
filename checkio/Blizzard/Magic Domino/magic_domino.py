import operator as op
from functools import reduce
from itertools import chain, combinations, islice, permutations, product
from random import shuffle


flatten = lambda x: [j for i in x for j in i]


def dominos():
    return [(i, j) for i in range(7) for j in range(i, 7)]


def tile_combinations(tiles, size, number):
    return [i for i in combinations(tiles, size // 2) if sum(map(sum, i)) == number]


def combine_columns(columns, size, exception=set()):
    if size == 0:
        yield []
    for i, v in enumerate(columns):
        new_exception = set(v) | exception
        sub_columns = [
            item
            for item in columns[i + 1 :]
            if not any([tile in new_exception for tile in item])
        ]
        for j in combine_columns(sub_columns, size - 1, new_exception):
            ret = [v] + j
            yield ret


def row_sum_check(columns, number, size):
    for i in range(size):
        item_index, sub_item_index = i // 2, i % 2
        if sum([i[item_index][sub_item_index] for i in columns]) != number:
            return False
    return True


def diagonal_check(columns, number, size):
    diagonal_indexes = []
    reversed_diagonal_indexes = []
    for i in range(size):
        diagonal_indexes.append((i // 2, i % 2))
        reversed_diagonal_indexes.append(((size - 1 - i) // 2, (size - 1 - i) % 2))

    for i in permutations(columns):
        if (
            sum(
                [
                    value[diagonal_indexes[row][0]][diagonal_indexes[row][1]]
                    for row, value in enumerate(i)
                ]
            )
            == number
            and sum(
                [
                    value[reversed_diagonal_indexes[row][0]][
                        reversed_diagonal_indexes[row][1]
                    ]
                    for row, value in enumerate(i)
                ]
            )
            == number
        ):
            return i
    return False


def brute_force(domino, number, size):
    shuffled_cols = []
    for column in domino:
        element_list = []
        for element in column:
            element_list.append(list(set([element, element[::-1]])))

        # find out all possible permutations of a column
        col_possibilities = []
        for i in permutations(element_list, len(element_list)):
            col_possibilities.append(product(*i))
        col_possibilities = chain(*col_possibilities)
        shuffled_cols.append(col_possibilities)

    for i in product(*shuffled_cols):
        if row_sum_check(i, number, size):
            ret = diagonal_check(i, number, size)
            if ret:
                return ret


def magic_domino(size, number):
    domino_tiles = dominos()
    columns = tile_combinations(domino_tiles, size, number)
    for i in combine_columns(columns, size):
        ret = brute_force(i, number, size)
        if ret:
            return list(zip(*[flatten(j) for j in ret]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    import itertools

    def check_data(size, number, user_result):

        # check types
        def check_container_type(o):
            return any(map(lambda t: isinstance(o, t), (list, tuple)))

        def check_cell_type(i):
            return isinstance(i, int)

        if not (
            check_container_type(user_result)
            and all(map(check_container_type, user_result))
            and all(map(lambda row: all(map(check_cell_type, row)), user_result))
        ):
            raise Exception(
                "You should return a list/tuple of lists/tuples with integers."
            )

        # check sizes
        def check_size(o):
            return len(o) == size

        if not (check_size(user_result) and all(map(check_size, user_result))):
            raise Exception("Wrong size of answer.")

        # check is it a possible numbers (from 0 to 6 inclusive)
        if not all(
            map(lambda x: 0 <= x <= 6, itertools.chain.from_iterable(user_result))
        ):
            raise Exception("Wrong matrix integers (can't be domino tiles)")

        # check is it a magic square
        def seq_sum_check(seq):
            return sum(seq) == number

        diagonals_indexes = zip(
            *map(lambda i: ((i, i), (i, size - i - 1)), range(size))
        )

        def values_from_indexes(inds):
            return itertools.starmap(lambda x, y: user_result[y][x], inds)

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

    check_data(4, 5, magic_domino(4, 5))
