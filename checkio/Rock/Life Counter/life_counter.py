from collections import defaultdict


def count_neighbours(state, row, col):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum([1 for i in neighbors if (row + i[0], col + i[1]) in state])


def cell_changes(state):
    changes = defaultdict(int)
    if not state:
        return changes
    coordinates = state.keys()
    min_row = min(map(lambda x: x[0], coordinates))
    max_row = max(map(lambda x: x[0], coordinates))
    min_col = min(map(lambda x: x[1], coordinates))
    max_col = max(map(lambda x: x[1], coordinates))
    for i in range(min_row - 1, max_row + 2):
        for j in range(min_col - 1, max_col + 2):
            neighbors = count_neighbours(state, i, j)
            if (i, j) in state and neighbors not in [2, 3]:
                changes[(i, j)] = 0
            elif (i, j) not in state and neighbors == 3:
                changes[(i, j)] = 1
    return changes


def translate_state(state):
    translated_state = defaultdict(int)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 1:
                translated_state[(i, j)] = 1
    return translated_state


def life_counter(state, tick_n):
    new_state = translate_state(state)
    for _ in range(tick_n):
        changes = cell_changes(new_state)
        for i in changes:
            if changes[i] == 0:
                try:
                    del new_state[i]
                except KeyError:
                    pass
            else:
                new_state[i] = 1
    return sum(new_state.values())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert (
        life_counter(
            (
                (0, 1, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0, 0),
            ),
            4,
        )
        == 15
    ), "Example"
    assert (
        life_counter(
            (
                (0, 1, 0, 0, 0, 0, 0),
                (0, 0, 1, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 1, 1),
                (0, 0, 0, 0, 0, 0, 0),
                (1, 1, 1, 0, 0, 0, 0),
            ),
            15,
        )
        == 14
    ), "Little later"
    assert life_counter(((0, 1, 0), (0, 0, 1), (1, 1, 1)), 50) == 5, "Glider"
    assert (
        life_counter(
            (
                (1, 1, 0, 1, 1),
                (1, 1, 0, 1, 1),
                (0, 0, 0, 0, 0),
                (1, 1, 0, 1, 1),
                (1, 1, 0, 1, 1),
            ),
            100,
        )
        == 16
    ), "Stones"
