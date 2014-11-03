import datetime
import itertools


def FilterURL(URL):
    URL = URL.replace('http://', '')
    URL = URL.replace('https://', '')
    return '.'.join(URL.split('/')[0].split('.')[-2:])


def ConvertDateTime(DateTimeString):
    return datetime.datetime(*[int(ii) for ii in DateTimeString.split('-')])


def SplitList(L):
    SplitIndex = []
    for i, j in enumerate(zip(L, L[1:])):
        if (j[1][0] - j[0][0]).total_seconds() > 1800:
            SplitIndex.append(i)
    SplitIndex = [-1] + SplitIndex + [len(L) - 1]
    result = []
    for i in zip(SplitIndex, SplitIndex[1:]):
        result.append(L[i[0] + 1:i[1] + 1])
    return result


def checkio(log_text):
    lines = sorted([i.lower().split(';;') for i in log_text.splitlines()],
                   key=lambda x: x[1])
    lines = map(lambda x: [ConvertDateTime(x[0]), x[1], FilterURL(x[2])],
                lines)

    # groupby username
    temp1 = []
    for UserName, Items in [(j, list(k))
                            for j, k in itertools.groupby(lines,
                                                          lambda x: x[1])]:
        temp1.append(Items)

    # groupby url
    temp2 = []
    for i in temp1:
        i = sorted(i, key=lambda x: x[2])
        for j in [list(k) for _, k in itertools.groupby(i, lambda x: x[2])]:
            temp2.append(j)

    # split by time
    temp3 = []
    for i in temp2:
        temp3 += SplitList(i)

    result = []
    for i in temp3:
        result.append([i[0][1],
                       i[0][2],
                       int((i[-1][0] - i[0][0]).total_seconds() + 1),
                       len(i)])
    result = sorted(result, key=lambda x: (x[0], x[1], x[2], x[3]))

    return '\n'.join([';;'.join(map(str, i)) for i in result])

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert (checkio(
        """2013-01-01-01-00-00;;Name;;http://checkio.org/task
2013-01-01-01-02-00;;name;;http://checkio.org/task2
2013-01-01-01-31-00;;Name;;https://admin.checkio.org
2013-01-01-03-00-00;;Name;;http://www.checkio.org/profile
2013-01-01-03-00-01;;Name;;http://example.com
2013-02-03-04-00-00;;user2;;http://checkio.org/task
2013-01-01-03-11-00;;Name;;http://checkio.org/task""")
        ==
        """name;;checkio.org;;661;;2
name;;checkio.org;;1861;;3
name;;example.com;;1;;1
user2;;checkio.org;;1;;1"""), "Example"
