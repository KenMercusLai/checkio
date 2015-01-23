from math import pi, asin, atanh, sqrt


def volume(height, width):
    a = width / 2.0
    c = height / 2.0
    return round(pi * 4.0 / 3 * a * a * c, 2)


def surface_area(height, width):
    a = width / 2.0
    c = height / 2.0
    if c == a:
        return round(4 * pi * a * a, 2)
    if c < a:
        e2 = 1 - c * c / a / a
        return round(2 * pi * a * a * (1 + (1 - e2) / sqrt(e2) * atanh(sqrt(e2))), 2)
    else:
        e2 = 1 - a * a / c / c
        return round(2 * pi * a * a * (1 + c / a / sqrt(e2) * asin(sqrt(e2))),
                     2)


def checkio(height, width):
    return [volume(height, width), surface_area(height, width)]

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
