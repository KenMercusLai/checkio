import unittest

from sun_angle import sun_angle


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": '07:00', "answer": 15},
            {"input": '12:15', "answer": 93.75},
        ],
        "Extra": [
            {"input": '12:30', "answer": 97.5},
            {"input": '05:55', "answer": "I don't see the sun!"},
            {"input": "18:01", "answer": "I don't see the sun!"},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert sun_angle(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert sun_angle(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
