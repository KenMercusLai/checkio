import unittest

from earth_distances import distance


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ['51°28′48″N 0°0′0″E', '46°12′0″N, 6°9′0″E'],
                "answer": 739.227_134_742_523_7,
            },
            {
                "input": ['33°51′31″S, 151°12′51″E', '40°46′22″N 73°59′3″W'],
                "answer": 15990.168_098_597_984,
            },
            {
                "input": ['90°0′0″N 0°0′0″E', '90°0′0″S, 0°0′0″W'],
                "answer": 20015.086_796_020_572,
            },
        ],
        "Extra": [
            {
                "input": ['40°46′25″N 73°59′3″W', '40°46′22″N 73°59′5″W'],
                "answer": 0.103_802_232_708_710_39,
            },
            {
                "input": ['51°28′48″N 0°0′0″E', '51°28′48″S 180°0′0″W'],
                "answer": 20015.086_796_020_572,
            },
            {
                "input": ['51°28′48″N 0°0′0″E', '51°28′48″N 0°0′1″E'],
                "answer": 0.019_236_344_879_572_7,
            },
            {
                "input": ['51°28′48″N 0°0′0″E', '0°0′0″N 109°20′0″E'],
                "answer": 11330.620_213_642_82,
            },
            {
                "input": ['90°0′0″N 0°0′0″E', '11°21′0″N 142°12′0″E'],
                "answer": 8745.480_980_594_544,
            },
            {
                "input": ['90°0′0″S, 0°0′0″E', '25°0′0″N 71°0′0″W'],
                "answer": 12787.416_564_124_254,
            },
            {
                "input": ['48°27′0″N,34°59′0″E', '15°47′56″S 47°52′0″W'],
                "answer": 10801.622_299_208_242,
            },
            {
                "input": ['36°10′30″N 115°8′11″W', '35°18′27″S 149°7′27″E'],
                "answer": 12678.216_459_012_221,
            },
            {
                "input": ['35°41′22″N 139°41′30″E', '55°45′0″N 37°37′0″E'],
                "answer": 7478.605_880_642_18,
            },
            {
                "input": ['55°45′0″N 37°37′0″E', '35°41′22″N 139°41′30″E'],
                "answer": 7478.605_880_642_18,
            },
            {
                "input": ['35°18′27″S 149°7′27″E', '36°10′30″N 115°8′11″W'],
                "answer": 12678.216_459_012_221,
            },
            {
                "input": ['15°47′56″S 47°52′0″W', '48°27′0″N,34°59′0″E'],
                "answer": 10801.622_299_208_242,
            },
            {
                "input": ['25°0′0″N 71°0′0″W', '90°0′0″S, 0°0′0″E'],
                "answer": 12787.416_564_124_254,
            },
            {
                "input": ['11°21′0″N 142°12′0″E', '90°0′0″N 0°0′0″E'],
                "answer": 8745.480_980_594_544,
            },
            {
                "input": ['0°0′0″N 109°20′0″E', '51°28′48″N 0°0′0″E'],
                "answer": 11330.620_213_642_82,
            },
        ],
    }

    def almost_equal(self, checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert self.almost_equal(distance(*i['input']), i['answer'])

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert self.almost_equal(distance(*i['input']), i['answer'])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
