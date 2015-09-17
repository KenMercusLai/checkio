from itertools import combinations
from copy import deepcopy

POSSIBLE_ELEMENTS = 'ATCG'

CACHE = {}


def findfirst(sequence, start_index, target):
    key = sequence + str(start_index) + target
    if key in CACHE:
        return CACHE[key]
    for i in range(start_index, len(sequence)):
        if sequence[i] == target:
            CACHE[key] = [i]
            return CACHE[key]
    return []


def longest_match(first, second):
    results = set([])

    open_set = set([])
    longest_matches = 2
    for target in POSSIBLE_ELEMENTS:
        index_of_first = findfirst(first, 0, target)
        index_of_second = findfirst(second, 0, target)

        for j in index_of_first:
            for k in index_of_second:
                open_set.add((tuple([j]), tuple([k])))

    length_of_first = len(first)
    length_of_second = len(second)
    while open_set:
        # get one from open_set which reached farthest
        current = sorted(open_set, key=lambda x: -x[0][-1])[0]
        current_length = len(current[0])
        open_set.remove(current)
        if longest_matches > current_length + (length_of_first - 1 - current[0][-1]) \
                or longest_matches > current_length + (length_of_second - 1 - current[1][-1]):
            continue

        for target in POSSIBLE_ELEMENTS:
            key = first + str(current[0][-1] + 1) + target
            if key in CACHE:
                index_of_first = CACHE[key]
            else:
                index_of_first = findfirst(first, current[0][-1] + 1, target)

            key = second + str(current[1][-1] + 1) + target
            if key in CACHE:
                index_of_second = CACHE[key]
            else:
                index_of_second = findfirst(second, current[1][-1] + 1, target)

            if (not index_of_first) or (not index_of_second):
                if current_length >= longest_matches:
                    results.add(current)
                    longest_matches = current_length
            else:
                i_first = index_of_first[0]
                i_second = index_of_second[0]
                if longest_matches > current_length  + length_of_first - i_first \
                        or longest_matches > current_length + length_of_second - i_second:
                    pass
                else:
                    combination = (tuple(list(current[0]) + [i_first]),
                                   tuple(list(current[1]) + [i_second]))
                    open_set.add(combination)
    results = [i for i in results if len(i[0]) == longest_matches]
    return results


def common(first, second):
    results = longest_match(first, second)

    # translate indexes into chars
    sequences = []
    if results:
        for i in results:
            sequences.append(''.join([first[j] for j in i[0]]))
        return ','.join(sorted(list(set(sequences))))
    else:
        return ""


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
