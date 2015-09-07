import unittest
from .. import building_base


class Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Str(self):
        assert (str(building_base.Building(1, 1, 2, 2))
                == 'Building(1, 1, 2, 2, 10)')
        assert (str(building_base.Building(0.2, 1, 2, 2.2, 3.5))
                == 'Building(0.2, 1, 2, 2.2, 3.5)')

    def test_Corners(self):
        assert (building_base.Building(1, 1, 2, 2).corners()
                == {"south-west": [1, 1], "north-west": [3, 1], "north-east": [3, 3],
                    "south-east": [1, 3]})
        assert (building_base.Building(100.5, 0.5, 24.3, 12.2, 3).corners()
                == {"north-east": [112.7, 24.8], "north-west": [112.7, 0.5],
                    "south-west": [100.5, 0.5], "south-east": [100.5, 24.8]})

    def test_Area_Volume(self):
        assert building_base.Building(1, 1, 2, 2, 100).area() == 4
        assert (building_base.Building(100, 100, 135.5, 2000.1).area()
                == 271013.55)
        assert building_base.Building(1, 1, 2, 2, 100).volume() == 400
        assert (building_base.Building(100, 100, 135.5, 2000.1).volume()
                == 2710135.5)
