COLORS = ['blue', 'green', 'red', 'white', 'yellow']
PETS = ['cat', 'bird', 'dog', 'fish', 'horse']
BEVERAGES = ['beer', 'coffee', 'milk', 'tea', 'water']
CIGARETTES = ['Rothmans', 'Dunhill', 'Pall Mall', 'Winfield', 'Marlboro']
NATIONALITY = ['Brit', 'Dane', 'German', 'Norwegian', 'Swede']
NUMBERS = ['1', '2', '3', '4', '5']
QUESTIONS = ["number", "color", "nationality", "beverage", "cigarettes", "pet"]


from copy import deepcopy


def generate_empty_slots():
    """generate a dict contains 6 keys

    Returns:
        dict: dict contains 6 lists
    """
    return {'colors':      ['', '', '', '', ''],
            'pets':        ['', '', '', '', ''],
            'beverages':   ['', '', '', '', ''],
            'cigarettes':  ['', '', '', '', ''],
            'nationality': ['', '', '', '', ''],
            'numbers':     ['', '', '', '', '']}


def category_of(element):
    """find the category of the element

    Args:
        element (str): one of the given clue

    Returns:
        str: category name
    """
    if element in COLORS:
        return 'colors'
    if element in PETS:
        return 'pets'
    if element in BEVERAGES:
        return 'beverages'
    if element in CIGARETTES:
        return 'cigarettes'
    if element in NATIONALITY:
        return 'nationality'
    return 'numbers'


def fill_last_one(slots):
    """fill the empty if there is only one element left in a category

    Args:
        slots (dict): the game slots for answers

    Returns:
        dict: updated slots
    """
    tempslots = deepcopy(slots)
    for key, items in tempslots.items():
        if sum([1 for i in items if i]) == 4:
            last_element = list(
                set(globals()[key.upper()]).difference(set(items)))[0]
            slots[key] = [i if i else last_element for i in items]
    return slots


def find_empty_col(slots):
    """find empty col in slots

    Args:
        slots (dict): slots for answer

    Returns:
        int: available col for insert
             6 --> no available col 
             others --> col index
    """
    index = 0
    for i in list(zip(*list(slots.values())[::])):
        if sum([1 for j in list(i) if j]) == 0:
            return index
        index += 1
    return 6


def answer(relations, question):
    empty_slots = generate_empty_slots()
    # for an unknown reason, I have to go through relations from first to last
    # to build slots correctly, or the slots will conflicts
    # hope anyone can tell me why the order influences the final answer???
    relations = list(reversed(list(relations)))
    last_available_index = 0
    while relations:
        relation = relations.pop().split('-')
        item_list_of_first_element = empty_slots[category_of(relation[0])]
        item_list_of_second_element = empty_slots[category_of(relation[1])]
        # update respective index element in the category when find existed
        # element, or add simply add them into categories respectively

        # if two elements exist, align them
        if (relation[0] in item_list_of_first_element
                and relation[1] in item_list_of_second_element):
            index1 = item_list_of_first_element.index(relation[0])
            index2 = item_list_of_second_element.index(relation[1])
            for i in empty_slots:
                if i != category_of(relation[0]) and empty_slots[i][index2] != '':
                    empty_slots[i][index1], empty_slots[i][index2] = empty_slots[
                        i][index2], empty_slots[i][index1]
        # if we only find one in slots, add another one into it
        elif relation[0] in item_list_of_first_element:
            index = item_list_of_first_element.index(relation[0])
            item_list_of_second_element[index] = relation[1]
        elif relation[1] in item_list_of_second_element:
            index = item_list_of_second_element.index(relation[1])
            item_list_of_first_element[index] = relation[0]
        # in case we cannot find both of them, we see if there is an empty
        # column to insert the relation
        else:
            if last_available_index < 5:
                item_list_of_first_element[last_available_index] = relation[0]
                item_list_of_second_element[last_available_index] = relation[1]
            else:
                relations.insert(0, '-'.join(relation))
        # if we have 4 known elements in a category, we can simply fill the 5th
        # one
        empty_slots = fill_last_one(empty_slots)
        last_available_index = find_empty_col(empty_slots)

    question_element, question_category = question.split('-')
    index = empty_slots[category_of(question_element)].index(question_element)
    return empty_slots[question_category + 's'][index]


if __name__ == '__main__':
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'fish-color') == 'green'  # What is the color of the house where the Fish lives?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'tea-number') == '2'  # What is the number of the house where tea is favorite beverage?
    assert answer(('Norwegian-Dunhill', 'Marlboro-blue', 'Brit-3',
                   'German-coffee', 'beer-white', 'cat-water',
                   'horse-2', 'milk-3', '4-Rothmans',
                   'dog-Swede', 'Norwegian-1', 'horse-Marlboro',
                   'bird-Brit', '4-green', 'Winfield-beer',
                   'Dane-blue', '5-dog', 'blue-horse',
                   'yellow-cat', 'Winfield-Swede', 'tea-Marlboro'),
                  'Norwegian-beverage') == 'water'  # What is the favorite beverage of the Norwegian man?
