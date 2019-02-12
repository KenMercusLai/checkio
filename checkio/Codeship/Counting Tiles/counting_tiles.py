from math import ceil, hypot


def getMaxAndMinDistances(radius):
    radius = int(ceil(radius))
    distances = []
    for row in range(radius):
        for col in range(radius):
            temp = [
                hypot(row - radius, col - radius),
                hypot(row - radius, radius - col - 1),
                hypot(radius - row - 1, radius - col),
                hypot(radius - row - 1, radius - col - 1),
            ]
            distances.append((min(temp), max(temp)))
    return distances


def checkio(radius):
    distances = getMaxAndMinDistances(radius)
    solid = len(list(filter(lambda x: x[1] < radius, distances)))
    partial = len(list(filter(lambda x: x[1] > radius > x[0], distances)))
    """count tiles"""
    return [solid * 4, partial * 4]


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
