import unittest

from the_best_number_ever import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [],
                "answer": 0
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert isinstance(checkio(), (int, float, complex))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
