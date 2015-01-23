def max_steps(numbers):
    if len(numbers) == 1:
        return numbers[0]
    elif len(numbers) == 0:
        return 0
    return numbers[-1] + max(max_steps(numbers[:-1]), max_steps(numbers[:-2]))


def checkio(numbers):
    return max_steps(numbers + [0])

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio(
        [-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')
