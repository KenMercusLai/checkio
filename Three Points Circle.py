import math


def get_circle_center_and_radius(x1, y1, x2, y2, x3, y3):
    # http://okwave.jp/qa/q7112206.html
    d = 2.0 * ((y1 - y3) * (x1 - x2) - (y1 - y2) * (x1 - x3))
    x = ((y1 - y3) * (y1 ** 2 - y2 ** 2 + x1 ** 2 - x2 ** 2) - (y1 - y2)
         * (y1 ** 2 - y3 ** 2 + x1 ** 2 - x3 ** 2)) / d
    y = ((x1 - x3) * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2) - (x1 - x2)
         * (x1 ** 2 - x3 ** 2 + y1 ** 2 - y3 ** 2)) / -d
    r = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    return (x, y), r


def checkio(data):
    (x1, y1), (x2, y2), (x3, y3) = eval(data)
    (x0, y0), r = get_circle_center_and_radius(x1, y1, x2, y2, x3, y3)
    return "(x-{:g})^2+(y-{:g})^2={:g}^2".format(round(x0, 2),
                                                 round(y0, 2),
                                                 round(r, 2))

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
