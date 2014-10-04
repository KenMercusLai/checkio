from copy import deepcopy


def count_neighbours(grid, row, col):
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    grid = [[0] * (len(grid[0]) + 2)] \
        + [[0] + list(i) + [0] for i in grid] \
        + [[0] * (len(grid[0]) + 2)]
    # print grid
    return sum([grid[row + 1 + i[0]][col + 1 + i[1]] for i in neighbors])


def life_counter(state, tick_n):
    while tick_n:
        state = [[0] * (len(state[0]) + 2)] \
            + [[0] + list(i) + [0] for i in state] \
            + [[0] * (len(state[0]) + 2)]
        rows = len(state)
        cols = len(state[0])
        NewState = deepcopy(state)
        NewState = [list(i) for i in NewState]
        for i in range(rows):
            for j in range(cols):
                neighbors = count_neighbours(state, i, j)
                if state[i][j]:
                    if neighbors < 2:
                        NewState[i][j] = 0
                    elif neighbors in [2, 3]:
                        NewState[i][j] = 1
                    elif neighbors > 3:
                        NewState[i][j] = 0
                else:
                    if neighbors == 3:
                        NewState[i][j] = 1
        state = deepcopy(NewState)
        while 1:
            if sum(state[0]) == 0:
                state = state[1:]
            else:
                break
        while 1:
            if sum(state[-1]) == 0:
                state = state[:-1]
            else:
                break
        tick_n -= 1
    return sum([sum(i) for i in NewState])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100) == 16, "Stones"
