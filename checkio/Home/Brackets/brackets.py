from functools import reduce
from typing import Iterable

BRACKETS = '{[()]}'


def check_brackets(stack: list, bracket: str) -> list:
    match bracket:
        case '}' if stack and stack[-1] == '{':
            stack.pop()
            return stack
        case ']' if stack and stack[-1] == '[':
            stack.pop()
            return stack
        case ')' if stack and stack[-1] == '(':
            stack.pop()
            return stack
    stack.append(bracket)
    return stack


def checkio(data):
    bracket_list = filter(lambda x: x in BRACKETS, data)
    reduced_brackets = list(reduce(check_brackets, bracket_list, []))
    if reduced_brackets:
        return False
    return True


# These "asserts" using only for self-checking
# and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
