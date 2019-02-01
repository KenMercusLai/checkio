from copy import deepcopy
from itertools import combinations


COLS = "abcdefgh"
ROWS = "12345678"
THREATS = {c + r: set(
    [c + ROWS[k] for k in range(8)]
    + [COLS[k] + r for k in range(8)]
    + [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8]
    + [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
    for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}


def checkAvailablePosition(board, placed):
    tempBoard = deepcopy(board)
    for i in placed:
        if i not in tempBoard:
            tempBoard = []
            break
        threats = sorted(THREATS[i])
        tempBoard = [j for j in tempBoard if j not in threats]
    return tempBoard


def place_queens(placed):
    board = [c + r for c in COLS for r in ROWS]
    availablePositions = checkAvailablePosition(board, placed)
    # print availablePositions
    remainedQueens = 8 - len(placed)
    queenPositionCombinations = [
        i for i in combinations(availablePositions, remainedQueens)]
    # print len(queenPositionCombinations)
    for position in queenPositionCombinations:
        colIndicators = set([i[0] for i in position] + [i[0] for i in placed])
        if len(colIndicators) < 8:
            continue
        rowIndicators = set([i[1] for i in position] + [i[1] for i in placed])
        if len(rowIndicators) < 8:
            continue
        i = list(position)
        tempPositions = deepcopy(availablePositions)
        while True:
            if len(i) == 1 and i[0] not in tempPositions:
                break
            queen = i.pop()
            tempPositions = checkAvailablePosition(
                tempPositions, [queen])
            if not tempPositions:
                break
        # i is empty means all queen can be positioned
        if not i:
            return set(list(placed) + list(position))
    return set({})


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    assert checker(
        place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"
