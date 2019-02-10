from math import acos, degrees, hypot


def CalcAngle(P1, P2):
    if P2[0] < P1[0]:
        return 360 - degrees(
            acos((P2[1] - P1[1]) * 1.0 / hypot(P2[0] - P1[0], P2[1] - P1[1]))
        )
    return round(
        degrees(acos((P2[1] - P1[1]) * 1.0 / hypot(P2[0] - P1[0], P2[1] - P1[1]))), 0
    )


def CalcDistance(P1, P2):
    return hypot(P1[0] - P2[0], P1[1] - P2[1])


def checkio(data):
    """list[list[int, int],] -> list[int,].

    Find the convex hull.
    """
    SortedData = sorted(data, key=lambda x: (x[0], x[1]))
    SortedData += [SortedData[0]]
    PointList = []
    CurrentAngle = 0
    CurrentPoint = SortedData[0]
    while 1:
        PointList.append(CurrentPoint)
        SortedData.remove(CurrentPoint)
        AngleList = [
            CalcAngle(CurrentPoint, i) if i != CurrentPoint else 999 for i in SortedData
        ]
        MinAngle = min([i for i in AngleList if i >= CurrentAngle])
        NextPoint = [j for k, j in enumerate(SortedData) if AngleList[k] == MinAngle]

        # more than one point with same angle
        if len(NextPoint) != 1:
            DistanceList = [CalcDistance(i, CurrentPoint) for i in NextPoint]
            NextPoint = [
                j
                for i, j in enumerate(NextPoint)
                if DistanceList[i] == min(DistanceList)
            ]
        NextPoint = NextPoint[0]
        if PointList[0] == NextPoint:
            break
        else:
            CurrentAngle = min([i for i in AngleList if i >= CurrentAngle])
            CurrentPoint = NextPoint
    return list(map(lambda x: data.index(x), PointList))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio([[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]) == [
        4,
        5,
        6,
        0,
        1,
        2,
        3,
    ], "First example"
    assert checkio([[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]) == [
        1,
        0,
        6,
        3,
        5,
        2,
    ], "Second example"
