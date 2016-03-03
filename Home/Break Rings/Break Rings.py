from itertools import groupby, chain
from collections import Counter


def ring_to_destroy(rings):
    """
    find out which element connects with the least connection element
    :param rings:
    :return: element to destroy
    """
    least_connected = Counter(chain(*[i for i in rings if len(i) > 1])) \
        .most_common()[-1][0]
    return [j for i in rings if least_connected in i for j in i if j != least_connected][0]


def has_connection(rings):
    return any([1 for i in rings if len(i) > 1])


def remove_duplicates(rings):
    return list(set(map(tuple, rings)))


def destroy_ring(rings, ring):
    ret = []
    for i in rings:
        ret.append({j for j in i if j != ring})
    return tuple([k for k, v in groupby(sorted(remove_duplicates(ret))) if len(k) > 1])


def break_rings(rings):
    ring_counter = 0
    while has_connection(rings):
        rings = destroy_ring(rings, ring_to_destroy(rings))
        ring_counter += 1
    return ring_counter


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert break_rings(
        ({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(
        ({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 5}, {3, 6})) == 2, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {
        4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
