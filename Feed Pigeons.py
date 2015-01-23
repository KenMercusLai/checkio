def checkio(number):
    pigeon_queue = []
    new_pigeon = 1
    while number:
        pigeon_queue += [0] * new_pigeon
        for i in range(len(pigeon_queue)):
            pigeon_queue[i] += 1
            number -= 1
            if number == 0:
                break
        new_pigeon += 1
    return len(filter(lambda x: x, pigeon_queue))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
    print checkio(3)
