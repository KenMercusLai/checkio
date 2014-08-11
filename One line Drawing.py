import itertools


def CanBeChained(segment):
    # print segment
    stack = []
    if len(segment) == 1:
        x11, y11, x12, y12 = segment[0]
        stack.append((x11, y11))
        stack.append((x12, y12))
    for i in zip(segment, segment[1:]):
        # print i, stack
        if not len(stack):
            x11, y11, x12, y12 = i[0]
            x21, y21, x22, y22 = i[1]
            if (x11, y11) == (x21, y21) or (x11, y11) == (x22, y22):
                stack.append((x12, y12))
                stack.append((x11, y11))
            elif (x12, y12) == (x21, y21) or (x12, y12) == (x22, y22):
                stack.append((x11, y11))
                stack.append((x12, y12))
            else:
                break
        else:
            lastx, lasty = stack[-1]
            # print lastx, lasty
            x21, y21, x22, y22 = i[0]
            if (lastx, lasty) == (x21, y21):
                stack.append((x22, y22))
            elif (lastx, lasty) == (x22, y22):
                stack.append((x21, y21))
            else:
                break
    # print stack
    if stack and len(segment) != 1:
        lastx, lasty = stack[-1]
        x21, y21, x22, y22 = i[1]
        if (lastx, lasty) == (x21, y21):
            stack.append((x22, y22))
        elif (lastx, lasty) == (x22, y22):
            stack.append((x21, y21))
    # print stack
    # print '--------------'
    return stack


def CanBeDrawInOneLine(segments):
    points = []
    for i in segments:
        points.append((i[0], i[1]))
        points.append((i[2], i[3]))
    pointCount = [(i, len([k for k in j]))
                  for i, j in itertools.groupby(sorted(points))]
    OddPoints = filter(lambda x: x[1] % 2 != 0, pointCount)
    return OddPoints


def draw(segments):
    OddPoints = CanBeDrawInOneLine(segments)
    # 0 or 2 odd points, else cannot be drawn by one line
    if len(OddPoints) in [2, 0]:
        if len(segments) != 1:
            if len(OddPoints) == 0:
                startLine = list(segments)[0]
                segments.remove(startLine)
                x, y, _, _ = startLine
                for i in segments:
                    if (x, y) in [(i[0], i[1]), (i[2], i[3])]:
                        endLine = i
                        break
                segments.remove(endLine)
                aaa = 0
                print len(segments)
                for i in itertools.permutations(segments):
                    print aaa, '\r',
                    aaa += 1
                    ret = CanBeChained([startLine] + list(i) + [endLine])
                    if len(ret) == len(segments) + 3:
                        return ret
            else:
                x, y = OddPoints[0][0]
                for i in segments:
                    if (x, y) in [(i[0], i[1]), (i[2], i[3])]:
                        startLine = i
                        break
                segments.remove(i)
                x, y = OddPoints[1][0]
                for i in segments:
                    if (x, y) in [(i[0], i[1]), (i[2], i[3])]:
                        endLine = i
                        break
                segments.remove(i)
                for i in itertools.permutations(segments):
                    ret = CanBeChained([startLine] + list(i) + [endLine])
                    if len(ret) == len(segments) + 3:
                        return ret
        else:
            for i in itertools.permutations(segments):
                ret = CanBeChained(i)
                if len(ret) == len(segments) + 1:
                    return ret
    return []


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def checker(func, in_data, is_possible=True):
        user_result = func(in_data)
        if not is_possible:
            if user_result:
                print("How did you draw this?")
                return False
            else:
                return True
        if len(user_result) < 2:
            print("More points please.")
            return False
        data = list(in_data)
        for i in range(len(user_result) - 1):
            f, s = user_result[i], user_result[i + 1]
            if (f + s) in data:
                data.remove(f + s)
            elif (s + f) in data:
                data.remove(s + f)
            else:
                print("The wrong segment {}.".format(f + s))
                return False
        if data:
            print("You forgot about {}.".format(data[0]))
            return False
        return True

    # assert checker(draw,
    #                {(1, 2, 1, 5), (1, 2, 7, 2),
    #                 (1, 5, 4, 7), (4, 7, 7, 5)}), "Example 1"
    # assert checker(draw,
    #                {(1, 2, 1, 5), (1, 2, 7, 2), (1, 5, 4, 7),
    #                 (4, 7, 7, 5), (7, 5, 7, 2), (1, 5, 7, 2),
    #                 (7, 5, 1, 2)}, False), "Example 2"
    # assert checker(draw,
    #                {(1, 2, 1, 5), (1, 2, 7, 2),
    #                 (1, 5, 4, 7), (4, 7, 7, 5),
    #                 (7, 5, 7, 2), (1, 5, 7, 2),
    #                 (7, 5, 1, 2), (1, 5, 7, 5)}), "Example 3"
    # edge 3
    print draw({(8, 4, 8, 6), (4, 8, 6, 2), (6, 8, 8, 6), (4, 8, 8, 6),
                (2, 6, 4, 2), (6, 2, 8, 4), (6, 8, 6, 2), (2, 6, 6, 2),
                (2, 4, 8, 4), (6, 8, 8, 4), (4, 2, 6, 2), (4, 2, 8, 6),
                (2, 4, 2, 6), (4, 2, 6, 8), (4, 2, 4, 8), (2, 4, 6, 2),
                (2, 4, 4, 8), (4, 8, 6, 8), (6, 2, 8, 6), (4, 8, 8, 4),
                (2, 6, 8, 6), (2, 6, 6, 8), (2, 4, 4, 2), (4, 2, 8, 4),
                (2, 4, 6, 8), (2, 6, 4, 8), (2, 6, 8, 4), (2, 4, 8, 6)})
    # edge 4
    print draw({(4, 2, 6, 8), (2, 4, 6, 2), (4, 8, 6, 2), (2, 4, 6, 8),
                (6, 8, 6, 2), (6, 2, 8, 4), (4, 2, 8, 4), (2, 6, 4, 8),
                (2, 6, 6, 8), (2, 6, 4, 2), (4, 2, 4, 8), (2, 4, 4, 8),
                (4, 8, 6, 8), (2, 4, 4, 2), (2, 4, 8, 4), (6, 8, 8, 4),
                (2, 6, 6, 2), (2, 6, 8, 4), (4, 2, 6, 2), (4, 8, 8, 4),
                (2, 4, 2, 6)})
