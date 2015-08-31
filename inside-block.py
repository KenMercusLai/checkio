class Line(object):

    """Line class. mainly used for intersection check

    Attributes:
        point1 (Point): Description
        point2 (Point): Description
    """

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

        # Find the four orientations needed for general and special cases
        o1 = self.orientation(self.point1, self.point2, another_line.point1)
        o2 = self.orientation(self.point1, self.point2, another_line.point2)
        o3 = self.orientation(another_line.point1, another_line.point2,
                              self.point1)
        o4 = self.orientation(another_line.point1, another_line.point2,
                              self.point2)

        # General case
        if o1 != o2 and o3 != o4:
            return True

        # Special Cases
        # p1, q1 and p2 are colinear and p2 lies on segment p1q1
        if o1 == 0 and self.on_segment(self.point1, another_line.point1, self.point2):
            return True

        # p1, q1 and p2 are colinear and q2 lies on segment p1q1
        if o2 == 0 and self.on_segment(self.point1, another_line.point2, self.point2):
            return True

        # p2, q2 and p1 are colinear and p1 lies on segment p2q2
        if o3 == 0 and self.on_segment(another_line.point1, self.point1, another_line.point2):
            return True

        # p2, q2 and q1 are colinear and q1 lies on segment p2q2
        if o4 == 0 and self.on_segment(another_line.point1, self.point2, another_line.point2):
            return True

        # Doesn't fall in any of the above cases
        return False

    def on_segment(self, point1, point2, point3):
        """Given three colinear points p, q, r, the function checks if
           point q lies on line segment 'pr'

        Args:
            point1 (Point): p
            point2 (Point): q
            point3 (Point): r

        Returns:
            bool: true when they are on segment
        """

        if (point2.x <= max(point1.x, point3.x)
                and point2.x >= min(point1.x, point3.x)
                and point2.y <= max(point1.y, point3.y)
                and point2.y >= min(point1.y, point3.y)):
            return True
        else:
            return False

    def orientation(self, point1, point2, point3):
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

    def double_length(self):
        """double the length of current line from point1 to point2

        Returns:
            tuple: new end point coordinations
        """
        return (self.point1.x + 2 * (self.point2.x - self.point1.x),
                self.point1.y + 2 * (self.point2.y - self.point1.y))


class Point(object):

    """class for point, mainly used in Line class"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_inside(polygon, point):
    line2 = Line(Point(point[0], point[1]), Point(100, point[1]))
    intersections = 0
    point_pairs = [
        i for i in zip(polygon, polygon[1:])] + [(polygon[-1], polygon[0])]
    while point_pairs:
        # we draw polygon reversely
        i = point_pairs.pop()
        q1 = Point(i[0][0], i[0][1])
        p1 = Point(i[1][0], i[1][1])
        line1 = Line(p1, q1)
        if line1.intersect_with(line2):
            # double the length when find a intersection
            if point_pairs:
                point_pairs[-1] = (point_pairs[-1][0],
                                   line1.double_length())
            if line1.orientation(p1, Point(*point), q1) == 0:
                return line1.on_segment(p1, Point(*point), q1)
            intersections += 1
    if intersections % 2:
        return True
    else:
        return False


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
