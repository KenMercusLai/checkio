# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re
from math import pi, cos, sin, radians, acos
R = 6371


def ExtractPosition(PositionStr):
    items = re.search('(\d+)\D(\d+)\D(\d+)\D(\w)', PositionStr).groups()
    if 'W' in PositionStr or 'S' in PositionStr:
        return radians(-(int(items[0]) * 3600
                         + int(items[1]) * 60 + int(items[2])) / 3600.0)
    return radians((int(items[0]) * 3600 + int(items[1]) * 60
                    + int(items[2])) / 3600.0)


def distance(first, second):
    if len(first.split()) == 2:
        first = first.split()
    else:
        first = first.split(',')
    if len(second.split()) == 2:
        second = second.split()
    else:
        second = second.split(',')
    FirstLatitude, FirstLongitude, SecondLatitude, SecondLongitude = map(
        ExtractPosition, first + second)
    DirectDistance = sin(FirstLatitude) * sin(SecondLatitude) + cos(FirstLatitude) * \
        cos(SecondLatitude) * cos(FirstLongitude - SecondLongitude)
    if acos(DirectDistance) == 0:
        return pi * R
    return round(R * acos(DirectDistance), 1)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
    distance(u"48°27′0″N,34°59′0″E", u"15°47′56″S 47°52′0″W")
