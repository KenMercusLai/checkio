def check_connection(network, first, second):
    # parse given connections to groups
    connection_groups = []
    all_people = []
    for i in network:
        x, y = i.split('-')
        all_people += [x, y]
        # check if x/y in a group, add them to the group
        # or create a new group
        existed = False
        for j in connection_groups:
            if x in j or y in j:
                j += [x, y]
                existed = True
        if not existed:
            connection_groups.append([x, y])

    # remove dup items in groups
    connection_groups = [set(i) for i in connection_groups]
    all_people = set(all_people)

    # i don't think this merge codes are good, but it works at least
    # in case there may be shared items between groups, we have to merge them
    for i in all_people:
        # get indexes of groups that shares people
        # generate a reversed index to avoid issue when removing item from list
        index_list = [j for j in range(len(connection_groups) - 1, -1, -1)
                      if i in connection_groups[j]]

        if len(index_list) > 1:
            temp = []
            for j in index_list:
                temp += list(connection_groups[j])
                del connection_groups[j]
            connection_groups.append(set(temp))

    # if first & second are in the same group, return True
    for i in connection_groups:
        if first in i and second in i:
            return True
    return False


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
