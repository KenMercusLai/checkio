def mirror(state):
    return [[j for j in i[::-1]] for i in state]


def clockwise_rotate(state):
    return [list(i) for i in zip(*state[::-1])]


def counterclockwise_rotate(state):
    return mirror(clockwise_rotate(mirror(state)))


def remove_zeros(line):
    return [i for i in line if i != 0]


def adding(line):
    first_element = line[0:1]
    second_element = line[1:2]
    rest_line = line[2:]
    if first_element and first_element == second_element:
        return [first_element[0] * 2], rest_line
    else:
        return first_element, second_element + rest_line


def recursive_adding(line):
    new_line, rest_line = adding(line)
    if rest_line:
        return new_line + recursive_adding(rest_line)
    return new_line


def padding_zeros(line):
    return line + [0] * (4 - len(line))


def move_left(state):
    non_zero_state = map(remove_zeros, state)
    added_state = map(recursive_adding, non_zero_state)
    return list(map(padding_zeros, added_state))


def flatten_list(state):
    return [item for sublist in state for item in sublist]


def add_new_element(state):
    flat_list = flatten_list(state)
    try:
        reversed_flat_list = list(reversed(flat_list))
        first_zero = reversed_flat_list.index(0)
        reversed_flat_list[first_zero] = 2
        new_flat_list = list(reversed(reversed_flat_list))
        return [new_flat_list[i : i + 4] for i in range(0, len(new_flat_list), 4)]
    except ValueError:
        return state


def move2048(state, move):
    if move == 'left':
        new_state = move_left(state)
    elif move == 'right':
        new_state = mirror(move_left(mirror(state)))
    elif move == 'up':
        new_state = clockwise_rotate(move_left(counterclockwise_rotate(state)))
    else:
        new_state = counterclockwise_rotate(move_left(clockwise_rotate(state)))
    if new_state == state:
        return [
            ['G', 'A', 'M', 'E'],
            ['O', 'V', 'E', 'R'],
            ['G', 'A', 'M', 'E'],
            ['O', 'V', 'E', 'R'],
        ]
    elif 2048 in flatten_list(new_state):
        return [
            ['U', 'W', 'I', 'N'],
            ['U', 'W', 'I', 'N'],
            ['U', 'W', 'I', 'N'],
            ['U', 'W', 'I', 'N'],
        ]
    return add_new_element(new_state)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert move2048([[0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 0, 0]], 'up') == [
        [0, 4, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2],
    ], "Start. Move Up!"
    assert move2048(
        [[4, 0, 0, 0], [0, 4, 0, 0], [0, 0, 0, 0], [0, 0, 8, 8]], 'right'
    ) == [[0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 2, 16]], "Simple right"
    assert move2048(
        [[2, 0, 2, 2], [0, 4, 4, 4], [8, 8, 8, 16], [0, 0, 0, 0]], 'right'
    ) == [[0, 0, 2, 4], [0, 0, 4, 8], [0, 8, 16, 16], [0, 0, 0, 2]], "Three merging"
    assert move2048(
        [[256, 0, 256, 4], [16, 8, 8, 0], [32, 32, 32, 32], [4, 4, 2, 2]], 'right'
    ) == [[0, 0, 512, 4], [0, 0, 16, 16], [0, 0, 64, 64], [0, 2, 8, 4]], "All right"
    assert move2048(
        [[4, 4, 0, 0], [0, 4, 1024, 0], [0, 256, 0, 256], [0, 1024, 1024, 8]], 'down'
    ) == [
        ['U', 'W', 'I', 'N'],
        ['U', 'W', 'I', 'N'],
        ['U', 'W', 'I', 'N'],
        ['U', 'W', 'I', 'N'],
    ], "We are the champions!"
    assert move2048(
        [[2, 4, 8, 16], [32, 64, 128, 256], [512, 1024, 2, 4], [8, 16, 32, 64]], 'left'
    ) == [
        ['G', 'A', 'M', 'E'],
        ['O', 'V', 'E', 'R'],
        ['G', 'A', 'M', 'E'],
        ['O', 'V', 'E', 'R'],
    ], "Nobody moves!"
