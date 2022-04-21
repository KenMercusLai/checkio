from functools import reduce, lru_cache
from operator import add
from typing import List, Tuple


def is_even(x: int) -> bool:
    return x % 2 == 0


@lru_cache
def mountain_cover(top: Tuple[int, int]) -> List[Tuple[int, int]]:
    match top:
        case (_, 1):
            return [top]
        case (x, y) if is_even(x) != is_even(y):
            return [(x, y)]
        case _:
            return list(set([top] + mountain_cover((top[0] - 1, top[1] - 1)) + mountain_cover(
                (top[0], top[1] - 1)) + mountain_cover((top[0] + 1, top[1] - 1))))


def mountain_scape(tops: List) -> int:
    ret = (set(reduce(add, map(mountain_cover, map(tuple, tops)))))
    return len(ret)


if __name__ == '__main__':
    print("Example:")
    print(mountain_scape([(1, 1), (4, 2), (7, 3)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mountain_scape([(1, 1), (4, 2), (7, 3)]) == 13
    assert mountain_scape([(0, 2), (5, 3), (7, 5)]) == 29
    assert mountain_scape([(1, 3), (5, 3), (5, 5), (8, 4)]) == 37
    print("Coding complete? Click 'Check' to earn cool rewards!")
