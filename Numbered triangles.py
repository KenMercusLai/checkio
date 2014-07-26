import itertools


def checkio(chips):
    # generate all possible status for each chip
    print '--------------'
    chipPlaces = []
    for i in chips:
        chipPlaces.append([ij for ij in itertools.permutations(i)])
    # permutations for chips
    possiblePlaces = []
    for j in itertools.permutations(chipPlaces):
        possiblePlaces += [i for i in itertools.product(*j)]
    # extract all valid solutions
    validSolutions = [i for i in possiblePlaces
                      if (i[0][2] == i[1][0]
                          and i[1][2] == i[2][0]
                          and i[2][2] == i[3][0]
                          and i[3][2] == i[4][0]
                          and i[4][2] == i[5][0]
                          and i[5][2] == i[0][0])]
    # print validSolutions
    if validSolutions:
        # sum each solution
        # print [(map(lambda x: x[1], i)) for i in validSolutions]
        sumOfSolutions = [sum(map(lambda x: x[1], i)) for i in validSolutions]
        # print sumOfSolutions
        return max(sumOfSolutions)
    else:
        return 0

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"
