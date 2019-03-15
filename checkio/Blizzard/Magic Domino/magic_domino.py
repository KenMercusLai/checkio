from itertools import product, permutations, combinations, islice
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def number_combinations(size, number):
    return [i for i in product(*[list(range(7))] * size) if sum(i) == number]


def vertical_combination(combination):
    columns = {}
    for i in combination:
        dominos = [tuple(sorted(i[j:j + 2])) for j in range(0, len(i), 2)]
        if len(dominos) == len((set(dominos))):
            columns[i] = dominos
    return columns


def has_duplicate_tiles(status, columns):
    tiles = []
    for i in status:
        tiles += columns[i]
    return len(tiles) != len(set(tiles))


def max_tile_duplicate(status, columns):
    for i in range(2, len(status) + 1):
        if has_duplicate_tiles(status[:i], columns):
            return i
    return 0


def brute_force(size, number, columns):
    total_column_combinations = len(columns)
    domino_combinations = combinations(columns.keys(), size)
    for i in domino_combinations:
        duplications = max_tile_duplicate(i, columns)
        if duplications:
            # skip
            skip_combinations = ncr(total_column_combinations-duplications, size-duplications)-1
            islice(domino_combinations, skip_combinations)
            continue
        # row check
        row_sums = list(map(sum, list(zip(*i))))
        if not (len(set(row_sums)) == 1 and row_sums[0] == number):
            continue
        # diangal check
        for diagnal_check in permutations(i):
            diagnal1 = [diagnal_check[j][j] for j in range(size)]
            diagnal2 = [diagnal_check[j][size - j - 1] for j in range(size)]
            if (sum(diagnal1) == sum(diagnal2) == number):
                return diagnal_check


def magic_domino(size, number):
    valid_number_combinations = number_combinations(size, number)
    columns = vertical_combination(valid_number_combinations)
    return list(zip(*brute_force(size, number, columns)))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    import itertools

    def check_data(size, number, user_result):

        # check types
        check_container_type = lambda o: any(map(lambda t: isinstance(o, t), (list, tuple)))
        check_cell_type = lambda i: isinstance(i, int)
        if not (check_container_type(user_result) and
                all(map(check_container_type, user_result)) and
                all(map(lambda row: all(map(check_cell_type, row)), user_result))):
            raise Exception("You should return a list/tuple of lists/tuples with integers.")

        # check sizes
        check_size = lambda o: len(o) == size
        if not (check_size(user_result) and all(map(check_size, user_result))):
            raise Exception("Wrong size of answer.")

        # check is it a possible numbers (from 0 to 6 inclusive)
        if not all(map(lambda x: 0 <= x <= 6, itertools.chain.from_iterable(user_result))):
            raise Exception("Wrong matrix integers (can't be domino tiles)")

        # check is it a magic square
        seq_sum_check = lambda seq: sum(seq) == number
        diagonals_indexes = zip(*map(lambda i: ((i, i), (i, size - i - 1)), range(size)))
        values_from_indexes = lambda inds: itertools.starmap(lambda x, y: user_result[y][x], inds)
        if not (all(map(seq_sum_check, user_result)) and  # rows
                all(map(seq_sum_check, zip(*user_result))) and  # columns
                all(map(seq_sum_check, map(values_from_indexes, diagonals_indexes)))):  # diagonals
            raise Exception("It's not a magic square.")

        # check is it domino square
        tiles = set()
        for x, y in itertools.product(range(size), range(0, size, 2)):
            tile = tuple(sorted((user_result[y][x], user_result[y + 1][x])))
            if tile in tiles:
                raise Exception("It's not a domino magic square.")
            tiles.add(tile)

    check_data(4, 5, magic_domino(4, 5))
