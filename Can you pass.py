from copy import deepcopy


def check_connection(network, first, second):
    # create non duplicates individuals
    all_people = []
    for i in network:
        all_people += i.split('-')
    temp_all_people = [[i] for i in set(all_people)]

    # create connections
    all_people = None
    while temp_all_people != all_people:
        all_people = deepcopy(temp_all_people)
        for i in network:
            person1, person2 = i.split('-')
            group1 = filter(lambda x: person1 in x, temp_all_people)
            group2 = filter(lambda x: person2 in x, temp_all_people)
            group1, group2 = group1[0], group2[0]
            if group1 != group2:
                temp_all_people.remove(group1)
                temp_all_people.remove(group2)
                temp_all_people.append(group1 + group2)
    # determine first and second are in same group or not
    group1 = filter(lambda x: first in x, temp_all_people)
    group2 = filter(lambda x: second in x, temp_all_people)
    if group1 == group2:
        return True
    return False


def build_network(matrix):
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
    network = build_network(matrix)
    return check_connection(network, str(first), str(second))


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) is True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) is False, 'First example'
