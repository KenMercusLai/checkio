import datetime
from collections import Counter


def most_frequent_days(year):
    # since the week repeats in the whole year, we only need to find out
    # incompleted weekdays in the beginning and the end of the year.

    # incompleted weekdays in the beginning
    week_list = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                 'Friday', 'Saturday', 'Sunday']
    weekdays = []
    for i in range(1, 8):
        weekday = datetime.datetime(year, 1, i).isoweekday()
        if weekday == 1:
            # no incompleted week in beginning
            break
        weekdays.append(weekday)

    # incompleted weekdays in the end
    for i in range(7):
        weekday = datetime.datetime(year, 12, 31 - i).isoweekday()
        if weekday == 7:
            # no incompleted week in beginning
            break
        weekdays.append(weekday)

    # the most common elements
    ret = []
    week_counter = Counter(weekdays).most_common()
    ret.append(week_counter[0][0])
    for i in week_counter[1:]:
        if i[1] == week_counter[0][1]:
            ret.append(i[0])
        else:
            break
    ret = sorted(ret)
    return [week_list[i] for i in ret]


if __name__ == '__main__':  # pragma: no cover
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
