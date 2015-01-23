def FilterState(state):
    FilteredState = []
    for i in state:
        FilteredState.append(filter(lambda x: x != 0, i))
    return FilteredState


def move2048(state, move):
    if move in ['left', 'right']:
        FilteredState = FilterState(state)
    else:
        FilteredState = FilterState(zip(*state[::]))
        for i in range(len(FilteredState)):
            FilteredState[i] = list(FilteredState[i])
    ResultState = []
    if move in ['up', 'left']:
        for i in FilteredState:
            if len(i) == 1:
                ResultState.append(i)
            else:
                index = 0
                temp = []
                while index <= len(i) - 1:
                    if len(i[index:]) == 1:
                        temp += i[index:]
                        index += 1
                    elif i[index] == i[index + 1]:
                        temp.append(i[index] + i[index + 1])
                        index += 2
                    else:
                        temp.append(i[index])
                        index += 1
                ResultState.append(temp)
        for i in range(len(ResultState)):
            ResultState[i] += [0] * (4 - len(ResultState[i]))
    elif move in ['right', 'down']:
        for i in FilteredState:
            if len(i) == 1:
                ResultState.append(i)
            else:
                index = len(i) - 1
                temp = []
                while index > -1:
                    if len(i[:index + 1]) == 1:
                        temp = i[:index + 1] + temp
                        index -= 1
                    elif i[index] == i[index - 1]:
                        temp.insert(0, i[index] + i[index - 1])
                        index -= 2
                    else:
                        temp.insert(0, i[index])
                        index -= 1
                ResultState.append(temp)
        for i in range(len(ResultState)):
            ResultState[i] = [0] * (4 - len(ResultState[i])) + ResultState[i]

    # rotate back
    if move in ['up', 'down']:
        ResultState = zip(*ResultState[::])
        for i in range(len(ResultState)):
            ResultState[i] = list(ResultState[i])

    if 2048 in reduce(lambda x, y: x + y, ResultState):
        return [['U', 'W', 'I', 'N'],
                ['U', 'W', 'I', 'N'],
                ['U', 'W', 'I', 'N'],
                ['U', 'W', 'I', 'N']]
    elif 0 not in reduce(lambda x, y: x + y, ResultState):
        return [['G', 'A', 'M', 'E'],
                ['O', 'V', 'E', 'R'],
                ['G', 'A', 'M', 'E'],
                ['O', 'V', 'E', 'R']]
    else:
        # add 2 in last 0
        be_quit = False
        for i in range(len(ResultState) - 1, -1, -1):
            for j in range(len(ResultState[i]) - 1, -1, -1):
                if ResultState[i][j] == 0:
                    ResultState[i][j] = 2
                    be_quit = True
                    break
            if be_quit:
                break
        return ResultState


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert move2048([[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 2, 0, 0]], 'up') == [[0, 4, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 2]], "Start. Move Up!"
    assert move2048([[4, 0, 0, 0],
                     [0, 4, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 8, 8]], 'right') == [[0, 0, 0, 4],
                                                 [0, 0, 0, 4],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 2, 16]], "Simple right"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'right') == [[0, 0, 2, 4],
                                                 [0, 0, 4, 8],
                                                 [0, 8, 16, 16],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[256, 0, 256, 4],
                     [16, 8, 8, 0],
                     [32, 32, 32, 32],
                     [4, 4, 2, 2]], 'right') == [[0, 0, 512, 4],
                                                 [0, 0, 16, 16],
                                                 [0, 0, 64, 64],
                                                 [0, 2, 8, 4]], "All right"
    assert move2048([[4, 4, 0, 0],
                     [0, 4, 1024, 0],
                     [0, 256, 0, 256],
                     [0, 1024, 1024, 8]], 'down') == [['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']], "We are the champions!"
    assert move2048([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2, 4],
                     [8, 16, 32, 64]], 'left') == [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']], "Nobody moves!"
