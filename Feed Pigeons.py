def checkio(number):
    pigeonQueue = []
    newPigeon = 1
    while number:
        pigeonQueue += [0] * newPigeon
        for i in range(len(pigeonQueue)):
            pigeonQueue[i] += 1
            number -= 1
            if number == 0:
                break
        newPigeon += 1
    print pigeonQueue
    return len(filter(lambda x: x, pigeonQueue))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    print checkio(3)
