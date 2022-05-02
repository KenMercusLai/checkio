from collections import defaultdict
from itertools import product
from typing import List, Dict, Tuple


def clockwise_rotate_90(grille: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    return list(map(lambda x: (-x[1] + 7, x[0]), grille))


def rotate_90(grille: List[int]) -> List[int]:
    return convert_to_index(clockwise_rotate_90(convert_to_coordinates(grille)))


def rotate_180(grille: List[int]) -> List[int]:
    return convert_to_index(clockwise_rotate_90(clockwise_rotate_90(convert_to_coordinates(grille))))


def rotate_270(grille: List[int]) -> List[int]:
    return convert_to_index(
        clockwise_rotate_90(clockwise_rotate_90(clockwise_rotate_90(convert_to_coordinates(grille)))))


def convert_to_index(coordinates: List[Tuple[int, int]]) -> List[int]:
    return sorted([i[1] * 8 + i[0] for i in coordinates])


def convert_to_coordinates(indexes: List[int]) -> List[Tuple[int, int]]:
    """ coordinates are in (col, row) """
    return [(i % 8, i // 8) for i in indexes]


def convert_to_matrix(text: str) -> List[str]:
    return [text[i * 8:i * 8 + 8] for i in range(8)]


def is_list_increasing(l: List[int]) -> bool:
    return all(l[i] < l[i + 1] for i in range(len(l) - 1))


def find_candidates(positions_of_lookfor_text, lookfor):
    combinations = [positions_of_lookfor_text[i] for i in lookfor]
    print(combinations)
    for i in range(1, len(combinations)):
        combinations[i] = list(filter(lambda x: combinations[i-1][0]<x, combinations[i]))
    print(combinations)
    for i in range(len(combinations) - 2, -1, -1):
        combinations[i] = list(filter(lambda x: x < combinations[i + 1][-1], combinations[i]))
    print(combinations)
    return combinations


def look_for_grille(text: str, lookfor: str) -> List[Tuple[int]]:
    positions_of_lookfor_text = mapping_text_position(text, lookfor)
    print(positions_of_lookfor_text)
    possible_combinations = find_candidates(positions_of_lookfor_text, lookfor)
    print(possible_combinations)
    candidates = product(*possible_combinations)
    return list(filter(is_list_increasing, candidates))


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


def find_grille(plaintext: str, cryptogram: str) -> List[str]:
    grille_candidates = look_for_grille(cryptogram, plaintext[:16])
    # print(grille_candidates)
    for i in grille_candidates:
        # print(i)
        if get_decrypted_text(rotate_90(i), cryptogram) == plaintext[16:32] and get_decrypted_text(rotate_180(i),
                                                                                                   cryptogram) == plaintext[
                                                                                                                  32:48] and get_decrypted_text(
            rotate_270(i), cryptogram) == plaintext[48:]:
            return convert_to_matrix(punch_holes(i))


if __name__ == "__main__":
    print("Example:")
    print(find_grille("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb","ababaaaababbbbbaaaaaaaaaaabaaaaaaabbaaabaabaaaaaaaaaaaaababaabaa"))
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
