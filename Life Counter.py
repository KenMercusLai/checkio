from copy import deepcopy


def count_neighbours(grid, row, col):
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    grid = [[0] * (len(grid[0]) + 2)] \
        + [[0] + list(i) + [0] for i in grid] \
        + [[0] * (len(grid[0]) + 2)]
    return sum([grid[row + 1 + i[0]][col + 1 + i[1]] for i in neighbors])


def life_counter(state, tick_n):
    cache = {}
    while tick_n:
        # print tick_n
        state = [[0] * (len(state[0]) + 2)] \
            + [[0] + list(i) + [0] for i in state] \
            + [[0] * (len(state[0]) + 2)]

        # remove top and bottom empty lines
        while 1 and len(state) >= 2:
            if sum(state[0]) == 0 and sum(state[1]) == 0:
                state = state[1:]
            else:
                break
        while 1 and len(state) >= 2:
            if sum(state[-1]) == 0 and sum(state[-2]) == 0:
                state = state[:-1]
            else:
                break
        # remove left and right empty cols
        state = zip(*state[::])
        while 1 and len(state) >= 2:
            if sum(state[0]) == 0 and sum(state[1]) == 0:
                state = state[1:]
            else:
                break
        while 1 and len(state) >= 2:
            if sum(state[-1]) == 0 and sum(state[-2]) == 0:
                state = state[:-1]
            else:
                break
        state = zip(*state[::])
        # state = [list(i) for i in state]

        if str(state) not in cache:
            # calc new state
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
            cache[str(state)] = NewState

        # print state == cache[str(state)]
        # print state
        # print cache[str(state)]
        state = deepcopy(cache[str(state)])

        tick_n -= 1
    # print cache
    return sum([sum(i) for i in state])


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
    # print life_counter((
    #     (0, 1, 0, 0, 0, 0, 1, 0),
    #     (1, 0, 0, 0, 0, 0, 0, 1),
    #     (1, 1, 1, 0, 0, 1, 1, 1),), 999)
    # print life_counter((
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    #     (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    #     (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    #     (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0),
    #     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),), 20)
