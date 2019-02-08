def merge_members(group, member_a, member_b):
    first_member = second_member = None
    for i in group:
        if member_a in i:
            first_member = i
        if member_b in i:
            second_member = i
    if first_member and second_member:
        try:
            group.remove(first_member)
            group.remove(second_member)
        except ValueError:
            pass
        group.append(list(set(first_member + second_member)))
        return sorted(group, key=lambda x: len(x), reverse=True)
    else:
        return group


def is_family(tree):
    all_members = {j: {'father': None, 'son': []} for i in tree for j in i}
    member_group = [[i] for i in all_members.keys()]

    for relation in tree:
        # he is his father and son
        if len(set(relation)) == 1:
            return False
        # someone's father and son are the same person
        if relation[1] != all_members[relation[0]]['father']:
            all_members[relation[0]]['son'].append(relation[1])
        else:
            return False
        # someone has multiple father
        if all_members[relation[1]]['father'] is None:
            all_members[relation[1]]['father'] = relation[0]
        else:
            return False
        member_group = merge_members(member_group, relation[0], relation[1])

    if len(member_group) != 1:
        return False
    return True


if __name__ == "__main__":
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert is_family([['Logan', 'Mike']]) == True, 'One father, one son'
    assert is_family([['Logan', 'Mike'], ['Logan', 'Jack']]) == True, 'Two sons'
    assert (
        is_family([['Logan', 'Mike'], ['Logan', 'Jack'], ['Mike', 'Alexander']]) == True
    ), 'Grandfather'
    assert (
        is_family([['Logan', 'Mike'], ['Logan', 'Jack'], ['Mike', 'Logan']]) == False
    ), 'Can you be a father for your father?'
    assert (
        is_family([['Logan', 'Mike'], ['Logan', 'Jack'], ['Mike', 'Jack']]) == False
    ), 'Can you be a father for your brother?'
    assert (
        is_family([['Logan', 'William'], ['Logan', 'Jack'], ['Mike', 'Alexander']])
        == False
    ), 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")
