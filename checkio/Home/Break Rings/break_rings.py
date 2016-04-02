from itertools import combinations


def break_rings(rings):
    elements = set([j for i in rings for j in i])
    for i in range(1, len(rings) - 1):
        for j in combinations(elements, i):
            if not [k for k in rings if not set(k).intersection(j)]:
                return len(j)

if __name__ == "__main__":  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4},
                        {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3},
                        {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2},
                        {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4},
                        {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
