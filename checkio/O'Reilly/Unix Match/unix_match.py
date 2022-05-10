from itertools import pairwise
from re import search, match
from typing import Tuple


def translate_brackets(pattern: str, pair: Tuple[int, int]) -> Tuple[int, str]:
    if pair[1] - pair[0] == 1:
        return pair[0], ''
    else:
        sub_pattern = pattern[pair[0]:pair[1] + 1]
        if sub_pattern.startswith('[!'):
            return pair[0], '[^' + pattern[pair[0] + 1:pair[1]].replace('.', r'\.').replace('*', r'\*').replace('?',
                                                                                                                r'\?') + ']'
        else:
            return pair[0], '[' + pattern[pair[0] + 1:pair[1]].replace('.', r'\.').replace('*', r'\*').replace('?',
                                                                                                               r'\?') + ']'


def translate_non_pattern(pattern: str, pair: Tuple[int, int]) -> Tuple[int, str]:
    return pair[0], pattern[pair[0]:pair[1]].replace('.', '\.').replace('*', '.*').replace('?', '.').replace('[', '\[').replace(']', '\]')


def find_matching_left_bracket(string: str, right_bracket_index: int, stop_index: int) -> (int, int):
    for i in range(right_bracket_index, stop_index - 1, -1):
        if string[i] == '[':
            return i, right_bracket_index


def find_non_brackets(pattern: str, brackets: Tuple[Tuple[int, int]]) -> Tuple[Tuple[int, int]]:
    non_brackets = [(0, len(pattern))] * (len(brackets) + 1)
    if len(brackets) == 0:
        return non_brackets
    for i in range(len(non_brackets)):
        if i == 0:
            non_brackets[i] = (non_brackets[i][0], brackets[i][0])
        elif i == len(non_brackets) - 1:
            non_brackets[i] = (brackets[i - 1][1]+1, non_brackets[i][1])
        else:
            non_brackets[i] = (brackets[i - 1][1] + 1, brackets[i][0])
    return tuple([i for i in non_brackets if i[0] < i[1]])


def find_brackets(pattern: str) -> Tuple[Tuple[int, int]]:
    right_brackets = [k for k, v in enumerate(pattern) if v == ']']
    brackets_index_pairs = tuple(filter(lambda x: x, map(lambda x: find_matching_left_bracket(pattern, x[1], x[0]),
                                                         pairwise([0] + right_brackets))))
    print(right_brackets)
    print(brackets_index_pairs)
    return brackets_index_pairs


def translate_pattern(pattern: str) -> str:
    brackets_index_pairs = find_brackets(pattern)
    brackets = list(map(lambda x: translate_brackets(pattern, x), brackets_index_pairs))
    non_brackets_index_pair = find_non_brackets(pattern, brackets_index_pairs)
    print(non_brackets_index_pair)
    non_brackets = list(map(lambda x: translate_non_pattern(pattern, x), non_brackets_index_pair))
    return ''.join(map(lambda x: x[1], sorted(non_brackets + brackets)))


def unix_match(filename: str, pattern: str) -> bool:
    translated_pattern = translate_pattern(pattern)
    print(filename)
    print(pattern)
    print(translated_pattern)
    a = match(translated_pattern, filename)
    print(a)
    return '[]' not in pattern and bool(search(translated_pattern, filename))

if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
