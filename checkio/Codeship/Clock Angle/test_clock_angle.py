import unittest

from clock_angle import clock_angle


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": "02:30", "answer": 105.0},
            {"input": "18:00", "answer": 180.0},
            {"input": "12:01", "answer": 5.5},
            {"input": "00:00", "answer": 0.0},
            {"input": "01:43", "answer": 153.5},
            {"input": "01:42", "answer": 159.0},
            {"input": "13:42", "answer": 159.0},
            {"input": "23:59", "answer": 5.5},
        ],
        "Extra": [
            {"input": "05:40", "answer": 70.0},
            {"input": "05:16", "answer": 62.0},
            {"input": "20:37", "answer": 36.5},
            {"input": "00:23", "answer": 126.5},
            {"input": "23:47", "answer": 71.5},
            {"input": "07:01", "answer": 155.5},
            {"input": "13:50", "answer": 115.0},
            {"input": "19:27", "answer": 61.5},
            {"input": "04:03", "answer": 103.5},
            {"input": "14:55", "answer": 117.5},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert clock_angle(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert clock_angle(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
