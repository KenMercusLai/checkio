from copy import deepcopy

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '1234567890'


def convert(code):
    bin_code = bin(code)[2:].zfill(6)[::-1]
    return [[int(bin_code[j + i * 3]) for i in range(2)] for j in range(3)]


LETTERS_NUMBERS = list(map(convert,
                           [1, 3, 9, 25, 17, 11, 27, 19, 10, 26,
                            5, 7, 13, 29, 21, 15, 31, 23, 14, 30,
                            37, 39, 62, 45, 61, 53, 47, 63, 55, 46, 26]))
CAPITAL_FORMAT = convert(32)
NUMBER_FORMAT = convert(60)
PUNCTUATION = {",": convert(2), "-": convert(18), "?": convert(38),
               "!": convert(22), ".": convert(50), "_": convert(36)}
WHITESPACE = convert(0)


def braille_page(text):
    code_stream = [[], [], []]
    for i in text:
        code_stream[0].append(0)
        code_stream[1].append(0)
        code_stream[2].append(0)
        if i.lower() in LETTERS:
            converted_code = deepcopy(LETTERS_NUMBERS[LETTERS.index(i.lower())])
            if i not in LETTERS:
                converted_code[0] = CAPITAL_FORMAT[0] + [0] + converted_code[0]
                converted_code[1] = CAPITAL_FORMAT[1] + [0] + converted_code[1]
                converted_code[2] = CAPITAL_FORMAT[2] + [0] + converted_code[2]
        elif i in NUMBERS:
            converted_code = deepcopy(LETTERS_NUMBERS[NUMBERS.index(i)])
            converted_code[0] = NUMBER_FORMAT[0] + [0] + converted_code[0]
            converted_code[1] = NUMBER_FORMAT[1] + [0] + converted_code[1]
            converted_code[2] = NUMBER_FORMAT[2] + [0] + converted_code[2]
        elif i in PUNCTUATION:
            converted_code = deepcopy(PUNCTUATION[i])
        else:
            converted_code = deepcopy(WHITESPACE)
        code_stream[0] = code_stream[0] + converted_code[0]
        code_stream[1] = code_stream[1] + converted_code[1]
        code_stream[2] = code_stream[2] + converted_code[2]
        del converted_code
    for i in range(3):
        code_stream[i] = code_stream[i][1:]

    # cut stream into 10 symbles long each line
    if len(code_stream[0]) > 29:
        code_stack = []
        while len(code_stream[0]) > 29:
            code_stack.append(code_stream[0][:29])
            code_stack.append(code_stream[1][:29])
            code_stack.append(code_stream[2][:29])
            code_stream[0] = code_stream[0][30:]
            code_stream[1] = code_stream[1][30:]
            code_stream[2] = code_stream[2][30:]

        code_stack.append(code_stream[0][:29])
        code_stack.append(code_stream[1][:29])
        code_stack.append(code_stream[2][:29])
        code_stream = []
        for i in range(len(code_stack) / 3):
            code_stream.append([0 for k in range(29)])
            code_stream.append([0 if k + 1 > len(code_stack[i * 3]) else code_stack[i * 3][k] for k in range(29)])
            code_stream.append(
                [0 if k + 1 > len(code_stack[i * 3 + 1]) else code_stack[i * 3 + 1][k] for k in range(29)])
            code_stream.append(
                [0 if k + 1 > len(code_stack[i * 3 + 2]) else code_stack[i * 3 + 2][k] for k in range(29)])
        return code_stream[1:]
    return code_stream


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def checker(func, text, answer):
        result = func(text)
        return answer == tuple(tuple(row) for row in result)

    assert checker(braille_page, u"hello 1st World!", (
        (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1),
        (1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0))
    ), "Example"
    assert checker(braille_page, u"42", (
        (0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0),
        (0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0),
        (1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0))), "42"
    assert checker(braille_page, u"CODE", (
        (0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1),
        (0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0))
    ), "CODE"
