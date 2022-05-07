from collections import defaultdict, deque
from functools import reduce
from itertools import product
from operator import mul
from typing import List, Dict, Iterable

INDEX_MAPPING = [(0, 7, 63, 56), (1, 15, 62, 48), (2, 23, 61, 40), (3, 31, 60, 32), (4, 39, 59, 24), (5, 47, 58, 16),
                 (6, 55, 57, 8), (7, 63, 56, 0), (8, 6, 55, 57), (9, 14, 54, 49), (10, 22, 53, 41), (11, 30, 52, 33),
                 (12, 38, 51, 25), (13, 46, 50, 17), (14, 54, 49, 9), (15, 62, 48, 1), (16, 5, 47, 58),
                 (17, 13, 46, 50), (18, 21, 45, 42), (19, 29, 44, 34), (20, 37, 43, 26), (21, 45, 42, 18),
                 (22, 53, 41, 10), (23, 61, 40, 2), (24, 4, 39, 59), (25, 12, 38, 51), (26, 20, 37, 43),
                 (27, 28, 36, 35), (28, 36, 35, 27), (29, 44, 34, 19), (30, 52, 33, 11), (31, 60, 32, 3),
                 (32, 3, 31, 60), (33, 11, 30, 52), (34, 19, 29, 44), (35, 27, 28, 36), (36, 35, 27, 28),
                 (37, 43, 26, 20), (38, 51, 25, 12), (39, 59, 24, 4), (40, 2, 23, 61), (41, 10, 22, 53),
                 (42, 18, 21, 45), (43, 26, 20, 37), (44, 34, 19, 29), (45, 42, 18, 21), (46, 50, 17, 13),
                 (47, 58, 16, 5), (48, 1, 15, 62), (49, 9, 14, 54), (50, 17, 13, 46), (51, 25, 12, 38),
                 (52, 33, 11, 30), (53, 41, 10, 22), (54, 49, 9, 14), (55, 57, 8, 6), (56, 0, 7, 63), (57, 8, 6, 55),
                 (58, 16, 5, 47), (59, 24, 4, 39), (60, 32, 3, 31), (61, 40, 2, 23), (62, 48, 1, 15), (63, 56, 0, 7)]


def convert_to_matrix(text: str) -> List[str]:
    return [text[i * 8:i * 8 + 8] for i in range(8)]


def find_candidates(positions_of_lookfor_text, lookfor):
    combinations = [positions_of_lookfor_text[i] for i in lookfor]
    return combinations


def remove_impossibilities(possibilities: List[List[int]], allowed_indexes: Iterable[int]) -> List[List[int]]:
    for k, v in enumerate(possibilities):
        possibilities[k] = [i for i in v if i in allowed_indexes]
    for i in range(1, len(possibilities)):
        possibilities[i] = list(filter(lambda x: possibilities[i - 1][0] < x, possibilities[i]))
    for i in range(len(possibilities) - 2, -1, -1):
        possibilities[i] = list(filter(lambda x: x < possibilities[i + 1][-1], possibilities[i]))
    return possibilities


def find_possible_positions(text: str, lookfor: str, allowed_indexes: Iterable[int] = range(64)) -> List[List[int]]:
    positions_of_lookfor_text = mapping_text_position(text, lookfor)
    possible_combinations = find_candidates(positions_of_lookfor_text, lookfor)
    return remove_impossibilities(possible_combinations, allowed_indexes)


def mapping_text_position(text: str, lookfor: str) -> Dict:
    ret = defaultdict(list)
    [ret[v].append(i) for i, v in enumerate(text) if v in lookfor]
    return ret


def get_decrypted_text(grille: List[int], cryptogram: str) -> str:
    return ''.join([cryptogram[i] for i in grille])


def punch_holes(grille: List[int]) -> str:
    ret = ['.'] * 64
    for i in grille:
        ret[i] = 'X'
    return ''.join(ret)


def calc_combination_number(possibles):
    return reduce(mul, (map(lambda x: len(x), possibles)))


def pick_easiest(remained_0, remained_1, remained_2, remained_3) -> int:
    combinations = list(map(calc_combination_number, [remained_0, remained_1, remained_2, remained_3]))
    rotated = combinations.index(min(combinations))
    return rotated


def rotate(grille: List[int], times: int) -> List[int]:
    return sorted([INDEX_MAPPING[i][times] for i in grille])


def get_rotate_back(grille, rotated):
    new_index = []
    for i in grille:
        indexes = deque(INDEX_MAPPING[i])
        indexes.rotate(rotated)
        new_index.append(indexes[0])
    return sorted(new_index)


def all_rotations(grille, rotated):
    original = get_rotate_back(grille, rotated)
    return [original, rotate(original, 1), rotate(original, 2), rotate(original, 3)]


def find_result(plaintext, cryptogram, grille_combinations, rotated):
    combinations_to_test = product(*grille_combinations)
    for i in combinations_to_test:
        rotations = all_rotations(i, rotated)
        if ''.join(list(map(lambda x: get_decrypted_text(x, cryptogram), rotations))) == plaintext:
            return rotations[0]


def find_allowed_indexes(candidates):
    """find possible indexes and rotate for the next iteration"""
    indexes = list(set(j for i in candidates for j in i))
    return [INDEX_MAPPING[i][1] for i in indexes]


def find_grille(plaintext: str, cryptogram: str) -> List[str]:
    candidates_0 = find_possible_positions(cryptogram, plaintext[:16])
    candidates_1 = find_possible_positions(cryptogram, plaintext[16:32], find_allowed_indexes(candidates_0))
    candidates_2 = find_possible_positions(cryptogram, plaintext[32:48], find_allowed_indexes(candidates_1))
    candidates_3 = find_possible_positions(cryptogram, plaintext[48:], find_allowed_indexes(candidates_2))
    possible_grille_combinations = [candidates_0, candidates_1, candidates_2, candidates_3]
    rotated = pick_easiest(*possible_grille_combinations)
    grille_combinations = possible_grille_combinations[rotated]
    grille = find_result(plaintext, cryptogram, grille_combinations, rotated)
    return convert_to_matrix(punch_holes(grille))


if __name__ == "__main__":
    print("Example:")
    print(find_grille("quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
                      "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves", ))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_grille("quickbrownfoxjumpsoverthelazydogandjackdawslovesmysphinxofquartz",
                       "quicpsovkbroerthwnfoelazxjumydogmyspandjhinxackdofquawslartzoves", ) == ["XXXX....", "XXXX....",
                                                                                                 "XXXX....", "XXXX....",
                                                                                                 "........", "........",
                                                                                                 "........",
                                                                                                 "........", ]

    assert find_grille("weareallfromxanthcubesaidquicklyjustvisitingphazewewontbeforlong",
                       "wejhewucuaeswtbrveeoisantsalilbifdteifrqunooigrmplxcakhonnlagtyz", ) == ["X...X...", ".X.....X",
                                                                                                 "..X...X.", "...X.X..",
                                                                                                 "X.....X.", "...X...X",
                                                                                                 "..X.X...",
                                                                                                 ".X...X..", ]

    assert find_grille("theideaofcognitivebiasinpsychologyworksinananalogouswayacognitiv",
                       "tgovgeubyhsiawseiinorkdepaswoasifcyncyaanaognconaginihlttoiivloo", ) == ["X.......", ".X.....X",
                                                                                                 "X.....XX", ".X..X...",
                                                                                                 "XX......", "..XXX...",
                                                                                                 "..X....X",
                                                                                                 "...X....", ]

    print("Coding complete? Click 'Check' to earn cool rewards!")
