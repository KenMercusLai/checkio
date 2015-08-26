class Line(object):

    """Line class. mainly used for intersection check"""

    def __init__(self, point1, point2):
        """init line

        Args:
            point1 (Point): Description
            point2 (Point): Description
        """
        self.point1 = point1
        self.point2 = point2

    def intersect_with(self, another_line):
        """check another_line intersect with itself or not

        Args:
            another_line (Line): another line

        Returns:
            bool: return true when intersects
        """
        pass

    def __orientation(self, point1, point2, point3):
        """To find orientation of ordered triplet (p, q, r).

        Args:
            point1 (Point): p
            point2 (Point): q
            point3 (Point): r

        Returns:
            int: 0 --> p, q and r are colinear,
                 1 --> Clockwise
                 2 --> Counterclockwise
        """
        val = (point2.y - point1.y) * (point3.x - point2.x) - \
            (point2.x - point1.x) * (point3.y - point2.y)

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2


class Point(object):

    """class for point, mainly used in Line class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_inside(polygon, point):
    return True or False


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) == True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) == False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) == True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) == False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) == True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) == False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) == True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) == False, "Eighth"
