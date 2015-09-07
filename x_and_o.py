from copy import deepcopy
from functools import reduce

unitlists = [[(i, j) for j in range(3)] for i in range(3)] + \
    [[(j, i) for j in range(3)] for i in range(3)] + \
    [[(j, j) for j in range(3)]] + \
    [[(j, 2 - j) for j in range(3)]]


def remove_units(grid, mark_to_remove):
    grid = list(grid)
    result = deepcopy(unitlists)
    for i in range(3):
        for j in range(3):
            if grid[i][j] == mark_to_remove:
                result = [k for k in result if (i, j) not in k]
    return result

def most_valuable_cell(remained_unit_lists, grid, your_mark):
    result = {}
    for i in unitlists:
        for j in i:
            result[j] = 0
    # possible connection cell
    for i in remained_unit_lists:
        for j in i:
            result[j] += 1
    # defence cell
    grid = list(grid)
    for i in range(3):
        for j in range(3):
            if grid[i][j] in ['X', 'O'] and grid[i][j] != your_mark:
                for k in unitlists:
                    if (i, j) in k:
                        for kk in k:
                            if kk in result.keys():
                                result[kk] += 1
    for i in unitlists:
        score = reduce(lambda x, y: x*y, [4 if grid[j[0]][j[1]] not in [your_mark, '.'] else 1 for j in i ])
        for j in i:
            if j in result.keys():
                result[j] += score
    # offence cell
    for i in remained_unit_lists:
        score = sum([1 for j in i if grid[j[0]][j[1]] == your_mark])
        if score == 2:
            for j in i:
                if j in result.keys():
                    result[j] += 100
    return sorted(result.items(), key=lambda x: x[1], reverse=True)

def x_and_o(grid, your_mark):
    if your_mark == 'X':
        remained_units = remove_units(grid, 'O')
    else:
        remained_units = remove_units(grid, 'X')
    cell_list = most_valuable_cell(remained_units, grid, your_mark)
    for i in cell_list:
        if list(grid)[i[0][0]][i[0][1]] == '.':
            return i[0]
    for i in range(3):
        for j in range(3):
            if list(grid)[i][j] == '.':
                return i, j


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    from random import choice

    def random_bot(grid, mark):
        empties = [(x, y) for x in range(3)
                   for y in range(3) if grid[x][y] == "."]
        return choice(empties) if empties else (None, None)

    def referee(field):
        lines = (["".join(row) for row in field] + ["".join(row) for row in zip(*field)] +
                 [''.join(row) for row in zip(*[(r[i], r[2 - i]) for i, r in enumerate(field)])])
        if "X" * 3 in lines:
            return "X"
        elif "O" * 3 in lines:
            return "O"
        elif not "." in "".join(lines):
            return "D"
        else:
            return "."

    def check_game(user_func, user_mark, bot_mark, bot_algorithm=random_bot):
        grid = [["."] * 3 for _ in range(3)]
        if bot_mark == "X":
            x, y = bot_algorithm(grid, bot_mark)
            grid[x][y] = "X"
        while True:
            user_result = user_func(tuple("".join(row)
                                          for row in grid), user_mark)
            if (not isinstance(user_result, (tuple, list)) or len(user_result) != 2 or
                    not all(isinstance(u, int) and 0 <= u < 3 for u in user_result)):
                print(
                    "The result must be a list/tuple of two integers from 0 to 2.")
                return False

            if grid[user_result[0]][user_result[1]] != ".":
                print("You tried to mark the filled cell.")
                return False
            grid[user_result[0]][user_result[1]] = user_mark
            game_result = referee(grid)

            if game_result == "D" or game_result == user_mark:
                return True
            bot_move = bot_algorithm(grid, bot_mark)
            grid[bot_move[0]][bot_move[1]] = bot_mark
            game_result = referee(grid)
            if game_result == bot_mark:
                print("Lost :-(")
                return False
            elif game_result == "D":
                return True

    assert check_game(x_and_o, "X", "O"), "Random X"
    assert check_game(x_and_o, "O", "X"), "Random O"
