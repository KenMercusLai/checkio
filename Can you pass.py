from copy import deepcopy


def check_connection(network, first, second):
    # create non duplicates individuals
    allPeople = []
    for i in network:
        allPeople += i.split('-')
    tempAllPeople = [[i] for i in set(allPeople)]

    # create connections
    allPeople = None
    while tempAllPeople != allPeople:
        allPeople = deepcopy(tempAllPeople)
        for i in network:
            person1, person2 = i.split('-')
            group1 = filter(lambda x: person1 in x, tempAllPeople)
            group2 = filter(lambda x: person2 in x, tempAllPeople)
            group1, group2 = group1[0], group2[0]
            if group1 != group2:
                tempAllPeople.remove(group1)
                tempAllPeople.remove(group2)
                tempAllPeople.append(group1 + group2)
    # determine first and second are in same group or not
    group1 = filter(lambda x: first in x, tempAllPeople)
    group2 = filter(lambda x: second in x, tempAllPeople)
    if group1 == group2:
        return True
    return False


def buildNetwork(matrix):
    network = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            try:
                if matrix[row][col] == matrix[row][col + 1]:
                    network.append('(%d, %d)-(%d, %d)' %
                                   (row, col, row, col + 1))
            except:
                pass
            try:
                if matrix[row][col] == matrix[row + 1][col]:
                    network.append('(%d, %d)-(%d, %d)' %
                                   (row, col, row + 1, col))
            except:
                pass
    return network


def can_pass(matrix, first, second):
    if first == second:
        return False
    network = buildNetwork(matrix)
    return check_connection(network, str(first), str(second))


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
