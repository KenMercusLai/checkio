class T:
    def __init__(self, anything):
        pass

    def __lt__(self, otherthing):
        return True

    def __gt__(self, otherthing):
        return True

    def __ge__(self, otherthing):
        return True

    def __le__(self, otherthing):
        return True

    def __eq__(self, otherthing):
        return True

    def __ne__(self, otherthing):
        return True


def checkio(anything):
    """Try to return anything else :)."""
    return T(anything)


if __name__ == '__main__':  # pragma: no cover
    import re
    import math

    assert checkio({}) != [], 'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81, 'never'
    assert checkio(re) >= re, 'make'
    assert checkio(re) <= math, 'this'
    assert checkio(5) == ord, ':)'

    print('NO WAY :(')
