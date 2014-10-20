from itertools import permutations


def checkio(data):
    FlatedMatrix = sum(data, [])
    MagicNumber = sum(range(1, len(FlatedMatrix) + 1)) / len(data)
    # check for numbers left
    NumbersLeft = [i + 1 for i in range(len(data) * len(data[0]))
                   if i + 1 not in FlatedMatrix]

    # check answer
    for i in permutations(NumbersLeft, len(NumbersLeft)):
        # build new list
        counter = 0
        NewList = []
        for j in FlatedMatrix:
            if j != 0:
                NewList.append(j)
            else:
                NewList.append(i[counter])
                counter += 1
        NewList = [NewList[j:j + len(data[0])]
                   for j in range(0, len(FlatedMatrix), len(data[0]))]

        # check rows
        TestPassed = True
        for i in NewList:
            if sum(i) != MagicNumber:
                TestPassed = False
                break
        # check cols
        if TestPassed:
            NewList = zip(*NewList[::])
            for i in NewList:
                if sum(i) != MagicNumber:
                    TestPassed = False
                    break

        # check cross
        if TestPassed:
            NewList = zip(*NewList[::])
            Cross1 = []
            for j, k in enumerate(NewList):
                Cross1.append(k[j])
            Cross2 = []
            for j, k in enumerate(NewList):
                Cross2.append(k[len(k) - j - 1])
            if sum(Cross1) != MagicNumber or sum(Cross2) != MagicNumber:
                TestPassed = False

        if TestPassed:
            print NewList
            return NewList


if __name__ == '__main__':
    # This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        # check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
        # check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        # check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
        # check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True

    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
