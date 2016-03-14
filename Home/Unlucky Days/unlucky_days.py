import datetime

def checkio(year):
    counter = 0
    for i in range(1, 13):
        date = datetime.datetime(year, i, 13)
        if datetime.date.weekday(date) == 4:
            counter += 1
    return counter

if __name__ == '__main__': # pragma: no cover
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"

