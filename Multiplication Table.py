from operator import and_, or_, xor


def CreateTable(first, second):
    rows = len(first) + 1
    cols = len(second) + 1
    table = []
    for i in range(rows):
        if i == 0:
            table.append([''] + map(int, list(second)))
        else:
            table.append([int(first[i - 1])] + [''] * (cols - 1))
    return table


def Bit(first, second, operator):
    BitTable = CreateTable(first, second)
    for row in range(1, len(first) + 1):
        for col in range(1, len(second) + 1):
            BitTable[row][col] = operator(BitTable[0][col], BitTable[row][0])
    return sum([int(''.join(map(str, BitTable[i][1:])), 2)
                for i in range(1, len(BitTable))])


def checkio(first, second):
    return sum([Bit(bin(first)[2:], bin(second)[2:], and_),
                Bit(bin(first)[2:], bin(second)[2:], or_),
                Bit(bin(first)[2:], bin(second)[2:], xor)])

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
