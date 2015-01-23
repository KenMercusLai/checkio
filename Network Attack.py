from time import sleep


def capture(matrix):
    # build up tree based on matrix
    connected = []
    for i in range(len(matrix)):
        connected.append(
            [j for j in range(len(matrix)) if i != j and matrix[i][j] == 1])

    # simulate the timeline
    timer = -1
    currectAttack = {}
    attacked = []
    remained = range(1, len(matrix))
    currectAttack[0] = 1
    while remained or currectAttack:
        timer += 1
        for i in currectAttack:
            currectAttack[i] -= 1
            if currectAttack[i] == 0:
                attacked.append(i)
        for i in attacked:
            try:
                del currectAttack[i]
            except:
                pass
        for i in attacked:
            for j in connected[i]:
                if j in remained:
                    currectAttack[j] = matrix[j][j]
                    remained.remove(j)
    return timer


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
