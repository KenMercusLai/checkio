from math import ceil, hypot


def getMaxAndMinDistances(radius):
    radius = int(ceil(radius))
    distances = []
    for row in range(radius):
        for col in range(radius):
            temp = []
            temp.append(hypot(row - radius, col - radius))
            temp.append(hypot(row - radius, radius - col - 1))
            temp.append(hypot(radius - row - 1, radius - col))
            temp.append(hypot(radius - row - 1, radius - col - 1))
            distances.append((min(temp), max(temp)))
    return distances


def checkio(radius):
    distances = getMaxAndMinDistances(radius)
    solid = len(filter(lambda x: x[1] < radius, distances))
    partial = len(filter(lambda x: x[1] > radius and x[0] < radius, distances))
    """count tiles"""
    return [solid * 4, partial * 4]

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
