from functools import lru_cache, cmp_to_key
from itertools import product, starmap
from math import log
from operator import mul

PRIME_FACTORS = (2, 3, 5)


class Factors:
    def __init__(self, factor):
        self.factor = factor
        self.current = 1

    def pop(self, value: int) -> int | None:
        if value == self.current:
            ret = self.current
            self.current *= self.factor
            return ret


@lru_cache
def is_ugly(n: int) -> bool:
    if n == 1:
        return True
    for prime in PRIME_FACTORS:
        while n % prime == 0:
            n //= prime
    return n == 1


def find_ugly_number(n: int, ugly_numbers=[1], queue=[1], confirmed_to=1) -> int:
    if len(ugly_numbers[:ugly_numbers.index(confirmed_to) + 1]) >= n:
        return ugly_numbers[n - 1]
    new_numbers = list(starmap(mul, product(PRIME_FACTORS, queue)))
    return find_ugly_number(n, sorted(set(ugly_numbers + new_numbers)), new_numbers, min(new_numbers))


def find_ugly_number2(n: int, current_number=1) -> int:
    counter = 0
    while counter < n:
        if is_ugly(current_number):
            counter += 1
            current_number += 1
        else:
            current_number += 1
    return current_number - 1


def find_ugly_number3(n: int) -> int:
    permutations = product(range(n), set([0] + list(range(n * 2 // 3))), set([0] + list(range(n * 2 // 5))))
    numbers = sorted([2 ** i[0] * 3 ** i[1] * 5 ** i[2] for i in permutations])
    return numbers


def find_ugly_number4(n: int) -> int:
    factor_list = [Factors(i) for i in [2, 3, 5, 6, 10, 15, 30]]
    for i in range(n):
        value_to_pick = min([i.current for i in factor_list])
        [i.pop(value_to_pick) for i in factor_list]
        print(value_to_pick)


def compare_tuples(a, b):
    return (a[0] - b[0]) * log(2) + (a[1] - b[1]) * log(3) + (a[2] - b[2]) * log(5)


def find_ugly_number5(n: int) -> int:
    known_ugly_numbers = []
    candidates = [(0, 0, 0)]
    for _ in range(n):
        next_to_add = candidates[0]
        del candidates[0]
        known_ugly_numbers.append(next_to_add)
        new_candidate2 = (next_to_add[0] + 1, next_to_add[1], next_to_add[2])
        new_candidate3 = (next_to_add[0], next_to_add[1] + 1, next_to_add[2])
        new_candidate5 = (next_to_add[0], next_to_add[1], next_to_add[2] + 1)
        for i in [new_candidate2, new_candidate3, new_candidate5]:
            if i not in candidates and i not in known_ugly_numbers:
                candidates.append(i)
        candidates = sorted(candidates, key=cmp_to_key(compare_tuples))
    return 2 ** known_ugly_numbers[-1][0] * 3 ** known_ugly_numbers[-1][1] * 5 ** known_ugly_numbers[-1][2]


def ugly_number(n: int) -> int:
    return find_ugly_number5(n)


if __name__ == "__main__":
    print("Example:")
    print(ugly_number(4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ugly_number(4) == 4
    assert ugly_number(6) == 6
    assert ugly_number(11) == 15
    print("Ugly Numbers coding complete? Click 'Check' to earn cool rewards!")
