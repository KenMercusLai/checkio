def line_formulate(point_one, point_two):
    """
    return a,b,c of ax+by+c=0
    """
    # if it's parallel with x axis or y axis
    if point_one[1] == point_two[1]:
        return (0, 1, -point_one[1])
    elif point_one[0] == point_two[0]:
        return (1, 0, -point_one[0])
    else:
        # calc the a, b, c
        a = (point_two[1] - point_one[1]) * 1.0 / (point_two[0] - point_one[0])
        c = (point_one[0] * point_two[1] - point_two[0]
             * point_one[1]) * 1.0 / (point_one[0] - point_two[0])
        return (a, -1, c)


def midperpandicular(line, point):
    # perpendicular of the line in ax+by+c=0
    if line[0] == 0:
        new_a = 1
        new_b = 0
        new_c = -(new_a * point[0] + new_b * point[1])
    elif line[1] == 0:
        new_a = 0
        new_b = 1
        new_c = -(new_a * point[0] + new_b * point[1])
    else:
        new_a = -1.0 / line[0]
        new_b = line[1]
        new_c = -(new_a * point[0] + new_b * point[1])
    return (new_a, new_b, new_c)


def intersection(line_one, line_two):

    if line_one[1] > 0:
        line_one = map(lambda x: -x, line_one)
    if line_two[1] > 0:
        line_two = map(lambda x: -x, line_two)
    print line_one, line_two
    # x+c=0
    if line_one[1] == 0:
        return (-line_one[2], line_two[0] * -line_one[2] + line_two[2])
    elif line_two[1] == 0:
        return (-line_two[2], line_one[0] * -line_two[2] + line_one[2])
    # y+c=0
    elif line_one[0] == 0:
        return ((line_one[2] * line_two[1] + line_two[2]) * 1.0 / -line_two[0], -line_one[2])
    elif line_two[0] == 0:
        return ((line_two[2] * line_one[1] + line_one[2]) * 1.0 / -line_one[0], -line_two[2])
    else:
    # ax+by+c=0
        return ((line_two[2] - line_one[2]) * 1.0 / (line_one[0] - line_two[0]),
                line_one[0] * ((line_two[2] - line_one[2]) * 1.0 / (line_one[0] - line_two[0])) + line_one[2])


def checkio(data):
    points = [int(i)
              for i in data.replace('(', '').replace(')', '').split(',')]
    point_one = points[0:2]
    point_two = points[2:4]
    point_three = points[4:6]

    line_one = line_formulate(point_one, point_two)
    middle_point_of_line_one = (
        (point_one[0] + point_two[0]) * 1.0 / 2, (point_one[1] + point_two[1]) * 1.0 / 2)
    midperpandicular_one = midperpandicular(line_one, middle_point_of_line_one)

    line_two = line_formulate(point_two, point_three)
    middle_point_of_line_two = (
        (point_two[0] + point_three[0]) * 1.0 / 2, (point_two[1] + point_three[1]) * 1.0 / 2)
    midperpandicular_two = midperpandicular(line_two, middle_point_of_line_two)

    intersection_point = intersection(
        midperpandicular_one, midperpandicular_two)
    r = round(((point_one[0] - intersection_point[0]) ** 2 +
               (point_one[1] - intersection_point[1]) ** 2) ** 0.5, 2)

    # replace this for solution
    return "(x-{:g})^2+(y-{:g})^2={:g}^2".format(round(intersection_point[0], 2),
                                                 round(intersection_point[1], 2), r)

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
