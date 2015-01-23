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
