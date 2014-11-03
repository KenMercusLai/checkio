from math import hypot
from random import randint, choice
PossiblePositions = [(i, j) for i in range(10) for j in range(10)]


def checkio(steps):
    global PossiblePositions
    # first move random
    if len(steps) == 1:
        PossiblePositions = [(i, j) for i in range(10) for j in range(10)]
        while 1:
            row = randint(0, 9)
            col = randint(0, 9)
            if [row, col] != steps[0][:2]:
                PossiblePositions.remove((steps[0][0], steps[0][1]))
                return [row, col]

    DistanceMap1 = {}
    for i in PossiblePositions:
        DistanceMap1[i] = hypot(i[0] - steps[-1][0], i[1] - steps[-1][1])
    DistanceMap2 = {}
    for i in PossiblePositions:
        DistanceMap2[i] = hypot(i[0] - steps[-2][0], i[1] - steps[-2][1])
    if steps[-1][-1] == 1:
        PossiblePositions = [i for i in PossiblePositions
                             if DistanceMap1[i] < DistanceMap2[i]]
    elif steps[-1][-1] == -1:
        PossiblePositions = [i for i in PossiblePositions
                             if DistanceMap1[i] > DistanceMap2[i]]
    else:
        PossiblePositions = [i for i in PossiblePositions
                             if DistanceMap1[i] == DistanceMap2[i]]
    return choice(PossiblePositions)


if __name__ == '__main__':
    # This part is using only for self-checking and not necessary for
    # auto-testing
    MAX_STEP = 12

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(
                prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
            distance = hypot(row - goal[0], col - goal[1])
            alteration = 0 if prev_distance == distance else (
                1 if prev_distance > distance else -1)
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
