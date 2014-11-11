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
    CodeStream = [[], [], []]
    for i in text:
        CodeStream[0].append(0)
        CodeStream[1].append(0)
        CodeStream[2].append(0)
        if i.lower() in LETTERS:
            ConvertedCode = deepcopy(LETTERS_NUMBERS[LETTERS.index(i.lower())])
            if i not in LETTERS:
                ConvertedCode[0] = CAPITAL_FORMAT[0] + [0] + ConvertedCode[0]
                ConvertedCode[1] = CAPITAL_FORMAT[1] + [0] + ConvertedCode[1]
                ConvertedCode[2] = CAPITAL_FORMAT[2] + [0] + ConvertedCode[2]
        elif i in NUMBERS:
            ConvertedCode = deepcopy(LETTERS_NUMBERS[NUMBERS.index(i)])
            ConvertedCode[0] = NUMBER_FORMAT[0] + [0] + ConvertedCode[0]
            ConvertedCode[1] = NUMBER_FORMAT[1] + [0] + ConvertedCode[1]
            ConvertedCode[2] = NUMBER_FORMAT[2] + [0] + ConvertedCode[2]
        elif i in PUNCTUATION:
            ConvertedCode = deepcopy(PUNCTUATION[i])
        else:
            ConvertedCode = deepcopy(WHITESPACE)
        CodeStream[0] = CodeStream[0] + ConvertedCode[0]
        CodeStream[1] = CodeStream[1] + ConvertedCode[1]
        CodeStream[2] = CodeStream[2] + ConvertedCode[2]
        del ConvertedCode
    for i in range(3):
        CodeStream[i] = CodeStream[i][1:]

    # cut stream into 10 symbles long each line
    if len(CodeStream[0]) > 29:
        CodeStack = []
        while len(CodeStream[0]) > 29:
            CodeStack.append(CodeStream[0][:29])
            CodeStack.append(CodeStream[1][:29])
            CodeStack.append(CodeStream[2][:29])
            CodeStream[0] = CodeStream[0][30:]
            CodeStream[1] = CodeStream[1][30:]
            CodeStream[2] = CodeStream[2][30:]

        CodeStack.append(CodeStream[0][:29])
        CodeStack.append(CodeStream[1][:29])
        CodeStack.append(CodeStream[2][:29])
        CodeStream = []
        for i in range(len(CodeStack) / 3):
            CodeStream.append([0 for k in range(29)])
            CodeStream.append([0 if k+1 > len(CodeStack[i * 3]) else CodeStack[i * 3][k] for k in range(29)])
            CodeStream.append([0 if k+1 > len(CodeStack[i * 3+1]) else CodeStack[i * 3+1][k] for k in range(29)])
            CodeStream.append([0 if k+1 > len(CodeStack[i * 3+2]) else CodeStack[i * 3+2][k] for k in range(29)])
        return CodeStream[1:]
    return CodeStream


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
