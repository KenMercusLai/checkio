import unittest
from ..express_delivery import checkio

ACTIONS = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
    "B": (0, 0)
}


def check_solution(func, max_time, field):
    max_row, max_col = len(field), len(field[0])
    s_row, s_col = 0, 0
    total_time = 0
    hold_box = True
    route = func(field[:])
    for step in route:
        if step not in ACTIONS:
            print("Unknown action {0}".format(step))
            return False
        if step == "B":
            if hold_box:
                if field[s_row][s_col] == "B":
                    hold_box = False
                    total_time += 1
                    continue
                else:
                    print("Stephan broke the cargo")
                    return False
            else:
                if field[s_row][s_col] == "B":
                    hold_box = True
                total_time += 1
                continue
        n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
        total_time += 2 if hold_box else 1
        if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
            print("We've lost Stephan.")
            return False
        if field[n_row][n_col] == "W":
            print("Stephan fell in water.")
            return False
        s_row, s_col = n_row, n_col
        if field[s_row][s_col] == "E" and hold_box:
            if total_time <= max_time:
                return True
            else:
                print("You can deliver the cargo faster.")
                return False
    print("The cargo is not delivered")
    return False


class Tests(unittest.TestCase):

    def test_1_Basics(self):
        assert check_solution(checkio, 12, ['S...',
                                            '....',
                                            'B.WB',
                                            '..WE'])
        assert check_solution(checkio, 11, ['S...',
                                            '....',
                                            'B..B',
                                            '..WE'])

    def test_2_Extra(self):
        assert check_solution(checkio, 20, ['S.W...',
                                            '..WB..',
                                            '..WW..',
                                            '....B.',
                                            '....W.',
                                            '..B.BE'])
        assert check_solution(checkio, 18, ['SBW...',
                                            '.WWB..',
                                            '..WW..',
                                            '......',
                                            '...WW.',
                                            '..BWBE'])
        assert check_solution(checkio, 29, ['S..BW.',
                                            '.WWWWW',
                                            '.W....',
                                            '.W.W.B',
                                            '.W.W..',
                                            '...W.E'])

    def test_3_Weird(self):
        assert check_solution(checkio, 11, ['SB....BE'])
        assert check_solution(checkio, 16, ['S...BB..E'])
        assert check_solution(checkio, 13, ['SBBBBB',
                                            'BBBBBB',
                                            'BBBBBB',
                                            'BBBBBB',
                                            'BBBBBE'])
        assert check_solution(checkio, 22, ['S.......',
                                            '........',
                                            '..B.....',
                                            '.....B..',
                                            '........',
                                            '.......E'])
        assert check_solution(checkio, 35, ['SW.B.W.',
                                            '.W.W.W.',
                                            '.W.W.W.',
                                            '.W.W.WB',
                                            '.W.W.W.',
                                            '.B.W..E'])

    def test_4_Big(self):
        assert check_solution(checkio, 38, ['S..BW....',
                                            '...W.....',
                                            '..W......',
                                            '.........',
                                            '.WWWWWWW.',
                                            '..WB.....',
                                            '..W....B.',
                                            '..WWW.WWW',
                                            '....W...E'])
        assert check_solution(checkio, 56, ['S........',
                                            '.WWW.WWW.',
                                            '.W.B...W.',
                                            '.WWWWWWW.',
                                            '.W..B..W.',
                                            '.W.WWW.WW',
                                            '.W...W.WB',
                                            '.WWW.W.W.',
                                            '.....W..E'])
