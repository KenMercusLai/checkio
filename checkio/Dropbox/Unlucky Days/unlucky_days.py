import datetime


def checkio(year):
    return sum([1 for i in range(1, 13)
                if datetime.datetime(year, i, 13).weekday() == 4])


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
