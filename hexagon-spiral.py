__author__ = 'KenMercusLai'


def determine_level(number):
    if number == 1:
        return 0, 0
    level = 1
    start_number = 2
    while 1:
        if start_number <= number <= start_number + level * 6 - 1:
            return level, number - start_number
        start_number += level * 6
        level += 1


def convert_to_position(level, shift):
    if level == 0:
        return 0, 0
    position_map_of_numbers = []
    for i in range(level):
        position_map_of_numbers.append((-level + 1 + i, 1 + i))
    for i in range(1, level + 1):
        position_map_of_numbers.append((i, level))
    for i in range(level - 1, 0, -1):
        position_map_of_numbers.append((level, i))
    for i in range(level):
        position_map_of_numbers.append((level - i, 0 - i))
    for i in range(level):
        position_map_of_numbers.append((0 - i, -level))
    for i in range(level):
        position_map_of_numbers.append((-level, -level + i))
    position_map_of_numbers.append((-level, 0))
    return position_map_of_numbers[shift]


def calc_distance((x0, y0), (x1, y1)):
    return max(abs(y1 - y0), abs(x1 - x0), abs((x1 - y1)*-1 - (x0 - y0)*-1))


def hex_spiral(first, second):
    return calc_distance(*map(lambda x: convert_to_position(x[0], x[1]),
                              [determine_level(first), determine_level(second)]))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert hex_spiral(2, 9) == 1, "First"
    assert hex_spiral(9, 2) == 1, "Reverse First"
    assert hex_spiral(6, 19) == 2, "Second, short way"
    assert hex_spiral(5, 11) == 3, "Third"
    assert hex_spiral(13, 15) == 2, "Fourth, One row"
    assert hex_spiral(11, 17) == 4, "Fifth, One more test"

