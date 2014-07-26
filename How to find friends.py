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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") is True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") is True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") is False, "I don't know any scouts."
