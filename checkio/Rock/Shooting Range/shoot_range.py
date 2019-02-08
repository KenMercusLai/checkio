__author__ = 'KenMercusLai'
from math import atan2, degrees, radians, sin, sqrt


def angle_of_two_points(p1, p2):
    return degrees(atan2(p2[1] - p1[1], p2[0] - p1[0]))


def shot(wall1, wall2, shot_point, later_point):
    # calc 3 angles
    angle1 = angle_of_two_points(wall1, wall2) - angle_of_two_points(wall1, shot_point)
    angle2 = angle_of_two_points(later_point, shot_point) - angle_of_two_points(
        wall1, shot_point
    )
    if (angle1 > 0 and angle2 > 0) or (angle1 < 0 and angle2 < 0):
        return -1
    angle1 = abs(angle1)
    angle2 = abs(angle2)
    if angle1 > 180:
        angle1 = abs(180 - angle1)
    if angle2 > 180:
        angle2 = abs(180 - angle2)
    angle3 = 180 - angle1 - angle2

    line3 = sqrt((wall1[0] - shot_point[0]) ** 2 + (wall1[1] - shot_point[1]) ** 2)
    line2 = line3 / sin(radians(angle3)) * sin(radians(angle2))
    wall = sqrt((wall1[0] - wall2[0]) ** 2 + (wall1[1] - wall2[1]) ** 2)
    if line2 == wall or line2 == 0:
        return 0
    elif line2 > wall or line2 < 0:
        return -1
    else:
        return 100 - int(round(abs(wall / 2 - line2) / (wall / 2) * 100))


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    # and not necessary for auto-testing
    assert shot((2, 2), (5, 7), (11, 2), (8, 3)) == 100, "1st case"
    assert shot((2, 2), (5, 7), (11, 2), (7, 2)) == 0, "2nd case"
    assert shot((2, 2), (5, 7), (11, 2), (8, 4)) == 29, "3th case"
    assert shot((2, 2), (5, 7), (11, 2), (9, 5)) == -1, "4th case"
    assert shot((2, 2), (5, 7), (11, 2), (10.5, 3)) == -1, "4th case again"
