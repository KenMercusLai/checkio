def shear_45_ccw(array, m):
    ret = []
    for i in range(len(array)):
        ret.append([None] * 20)
        for j in range(len(array[i])):
            ret[i][int(i + m * j)] = array[i][j]
    return ret


def generateSlice(data):
    for aLine in data:
        for i in range(len(aLine) - 3):
            yield aLine[i : i + 4]


def isSequence(data):
    if (
        (data[0] == data[1])
        and (data[1] == data[2])
        and (data[2] == data[3])
        and (type(data[0]) == int)
    ):
        return True


def checkio(data):
    # original
    for i in generateSlice(data):
        if isSequence(i):
            return True

    # rotate 90
    dataR90 = zip(*data)
    for i in generateSlice(dataR90):
        if isSequence(i):
            return True

    # clockwise 45
    dataR45 = shear_45_ccw(data, -1)
    dataR45 = zip(*dataR45)
    for i in generateSlice(dataR45):
        if isSequence(i):
            return True

    # anti-clockwise 45
    dataAR45 = shear_45_ccw(data, 1)
    dataAR45 = zip(*dataAR45)
    for i in generateSlice(dataAR45):
        if isSequence(i):
            return True
    return False


# These "asserts" using only for self-checking
# and not necessary for auto-testing
if __name__ == '__main__':
    assert (
        checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
    ), "Vertical"
    assert (
        checkio([[7, 1, 4, 1], [1, 2, 5, 2], [3, 4, 1, 3], [1, 1, 8, 1]]) == False
    ), "Nothing here"
    assert (
        checkio(
            [
                [2, 1, 1, 6, 1],
                [1, 3, 2, 1, 1],
                [4, 1, 1, 3, 1],
                [5, 5, 5, 5, 5],
                [1, 1, 3, 1, 1],
            ]
        )
        == True
    ), "Long Horizontal"
    assert (
        checkio(
            [
                [7, 1, 1, 8, 1, 1],
                [1, 1, 7, 3, 1, 5],
                [2, 3, 1, 2, 5, 1],
                [1, 1, 1, 5, 1, 4],
                [4, 6, 5, 1, 3, 1],
                [1, 1, 9, 1, 2, 1],
            ]
        )
        == True
    ), "Diagonal"
