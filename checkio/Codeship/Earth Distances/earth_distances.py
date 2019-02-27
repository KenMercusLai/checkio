import re
from math import acos, cos, pi, radians, sin


R = 6371


def extract_position(position_str):
    items = re.search('(\d+)\D(\d+)\D(\d+)\D(\w)', position_str).groups()
    if 'W' in position_str or 'S' in position_str:
        return radians(
            -(int(items[0]) * 3600 + int(items[1]) * 60 + int(items[2])) / 3600.0
        )
    return radians((int(items[0]) * 3600 + int(items[1]) * 60 + int(items[2])) / 3600.0)


def distance(first, second):
    if len(first.split()) == 2:
        first = first.split()
    else:
        first = first.split(',')
    if len(second.split()) == 2:
        second = second.split()
    else:
        second = second.split(',')
    first_latitude, first_longitude, second_latitude, second_longitude = map(
        extract_position, first + second
    )
    direct_distance = sin(first_latitude) * sin(second_latitude) + cos(
        first_latitude
    ) * cos(second_latitude) * cos(first_longitude - second_longitude)
    if acos(direct_distance) == 0:
        return pi * R
    return round(R * acos(direct_distance), 1)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2
    ), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1
    ), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2
    ), "Opera Night"
    distance(u"48°27′0″N,34°59′0″E", u"15°47′56″S 47°52′0″W")
