import unittest

from building_base import Building


class Tests(unittest.TestCase):
    TESTS = {
        "1. Init": [
            {"input": (1, 1, 2, 2)},
            {"input": (1, 1, 2, 2, 10)},
            {"input": (0.54345, 1.12313, 2.0 / 6, 3.3 * 5, 1.0 / 2)},
        ],
        "2. Str": [
            {"input": (1, 1, 2, 2), "answer": "Building(1, 1, 2, 2, 10)"},
            {"input": (0.2, 1, 2, 2.2, 3.5), "answer": "Building(0.2, 1, 2, 2.2, 3.5)"},
        ],
        "3. Corners": [
            {
                "input": (1, 1, 2, 2),
                "answer": {
                    "south-west": [1, 1],
                    "north-west": [3, 1],
                    "north-east": [3, 3],
                    "south-east": [1, 3],
                },
            },
            {
                "input": (100.5, 0.5, 24.3, 12.2, 3),
                "answer": {
                    "north-east": [112.7, 24.8],
                    "north-west": [112.7, 0.5],
                    "south-west": [100.5, 0.5],
                    "south-east": [100.5, 24.8],
                },
            },
        ],
        "4. Area": [
            {"input": (1, 1, 2, 2, 100), "answer": 4},
            {"input": (100, 100, 135.5, 2000.1), "answer": 271_013.55},
        ],
        "5. Volume": [
            {"input": (1, 1, 2, 2, 100), "answer": 400},
            {"input": (100, 100, 135.5, 2000.1), "answer": 2_710_135.5},
        ],
    }

    def test_Init(self):
        for i in self.TESTS['1. Init']:
            assert Building(*i['input'])

    def test_Str(self):
        for i in self.TESTS['2. Str']:
            assert str(Building(*i['input'])) == i['answer']

    def test_Corners(self):
        for i in self.TESTS['3. Corners']:
            assert Building(*i['input']).corners() == i['answer']

    def test_Area(self):
        for i in self.TESTS['4. Area']:
            assert Building(*i['input']).area() == i['answer']

    def test_Volume(self):
        for i in self.TESTS['5. Volume']:
            assert Building(*i['input']).volume() == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
