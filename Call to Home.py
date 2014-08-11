from math import ceil


def total_cost(calls):
    totalMins = 0
    basePrice = 1
    totalCost = 0
    dayCost = {}
    for i in calls:
        # calc how many mins for each day
        day, _, seconds = i.split()
        seconds = int(seconds)
        mins = ceil(seconds * 1.0 / 60)
        if day in dayCost:
            dayCost[day] += mins
        else:
            dayCost[day] = mins
    totalCost = [dayCost[i] if dayCost[i] <=
                 100 else 100 + (dayCost[i] - 100) * 2 for i in dayCost]
    return sum(totalCost)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
