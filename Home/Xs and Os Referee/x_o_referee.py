def checkio(game_result):
    check_lines = []

    # generate lines need to check
    for row in range(3):
        line = []
        for col in range(3):
            line.append((row, col))
        check_lines.append(line)
    for col in range(3):
        line = []
        for row in range(3):
            line.append((row, col))
        check_lines.append(line)
    check_lines.append([(0, 0), (1, 1), (2, 2)])
    check_lines.append([(0, 2), (1, 1), (2, 0)])

    for i in check_lines:
        a, b, c = i
        if (game_result[a[0]][a[1]] != '.' and 
            game_result[a[0]][a[1]] == game_result[b[0]][b[1]] == game_result[c[0]][c[1]]):
            return game_result[a[0]][a[1]]
    return "D"

if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
