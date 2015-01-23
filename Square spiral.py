def get_position(number):
    circle = 1
    while True:
        if number <= circle * circle:
            circle = (circle - 1) / 2
            break
        circle += 2
    # on left
    if (circle * 2 + 1) ** 2 - circle * 2 <= number <= (circle * 2 + 1) ** 2:
        return -circle, number - (circle * 2 + 1) ** 2 + circle
    # on bottom
    elif (circle * 2 + 1) ** 2 - circle * 4 <= number <= (circle * 2 + 1) ** 2 - circle * 2:
        return (circle * 2 + 1) ** 2 - circle * 2 - number - circle, -circle
    # on right
    elif (circle * 2 + 1) ** 2 - circle * 6 <= number <= (circle * 2 + 1) ** 2 - circle * 4:
        return circle, (circle * 2 + 1) ** 2 - circle * 4 - number - circle
    else:
        return number - ((circle * 2 + 1) ** 2 - circle * 6) + circle, circle


def find_distance(first, second):
    a = get_position(first)
    b = get_position(second)
    return sum(map(lambda x: abs(x[0] - x[1]), zip(a, b)))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"
