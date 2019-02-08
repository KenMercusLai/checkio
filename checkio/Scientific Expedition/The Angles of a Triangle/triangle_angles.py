from math import acos, degrees


def checkio(a, b, c):
    if a + b > c and b - a < c:
        first_angle = round(
            degrees(acos((b ** 2 + c ** 2 - a ** 2) * 1.0 / (2 * b * c)))
        )
        second_angle = round(
            degrees(acos((a ** 2 + c ** 2 - b ** 2) * 1.0 / (2 * a * c)))
        )
        result = [first_angle, second_angle, 180 - first_angle - second_angle]
        return list(map(int, sorted(result)))
    else:
        return [0, 0, 0]


# These "asserts" using only for self-checking
# and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
