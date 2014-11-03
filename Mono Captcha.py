FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def SplitImage(image):
    result = []
    i = 0
    while 1:
        temp = [j[i * 4:(i + 1) * 4 + 1] for j in image]
        if len(reduce(lambda x, y: x + y, temp)) < 25:
            break
        else:
            result.append(temp)
            i += 1
    return result


def checkio(image):
    FontNumbers = [1 if i == 'X' else 0 for i in list(FONT)]
    FontNumbers = [FontNumbers[i * (len(FONT) / 5): (i + 1) * len(FONT) / 5]
                   for i in range(5)]
    FontNumbers = SplitImage(FontNumbers)
    FontNumbers = [FontNumbers[-1]] + FontNumbers[:-1]

    ImageNumbers = SplitImage(image)
    result = []
    for i in ImageNumbers:
        for j in range(len(FontNumbers)):
            NumberDotStream = reduce(lambda x, y: x + y, i)
            FontDotStream = reduce(lambda x, y: x + y, FontNumbers[j])
            if sum([1 for k0, k1 in enumerate(NumberDotStream)
                    if FontDotStream[k0] != k1]) <= 1:
                result.append(str(j))
                break
    return int(''.join(result))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
