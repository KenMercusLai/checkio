import unittest

from most_numbers import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [1, 2, 3],
                "answer": 2,
                "explanation": "3-1=2"
            },
            {
                "input": [5, -5],
                "answer": 10,
                "explanation": "5-(-5)=10"
            },
            {
                "input": [10.2, -2.2, 0, 1.1, 0.5],
                "answer": 12.4,
                "explanation": "10.2-(-2.2)=12.4"
            },
            {
                "input": [],
                "answer": 0,
                "explanation": "Empty"
            },
        ],
        "Extra": [
            {"input": [-99.9, 99.9],
             "answer": 199.8,
             "explanation": "99.9-(-99.9)"},
            {"input": [1, 1],
             "answer": 0,
             "explanation": "1-1"},
            {"input": [0, 0, 0, 0],
             "answer": 0,
             "explanation": "0-0"},
            {"input": [36.0, -26.0, -7.5, 0.9, 0.53, -6.6, -71.0, 0.53, -48.0,
                       57.0, 69.0, 0.063, -4.7, 0.01, 9.2],
             "answer": 140.0,
             "explanation": "69.0-(-71.0)"},
            {"input": [-0.035, 0.0, -0.1, 83.0, 0.28, 60.0],
             "answer": 83.1,
             "explanation": "83.0-(-0.1)"},

            {"input": [0.02, 0.93, 0.066, -94.0, -0.91, -21.0, -7.2, -0.018,
                       26.0],
             "answer": 120.0,
             "explanation": "26.0-(-94.0)"},

            {"input": [89.0, 0.014, 2.9, -1.2, 5.8],
             "answer": 90.2,
             "explanation": "89.0-(-1.2)"},

            {"input": [-69.0, 0.0, 0.0, -0.051, -0.021, -0.81],
             "answer": 69.0,
             "explanation": "0.0-(-69.0)"},

            {"input": [-0.07],
             "answer": 0.0,
             "explanation": "-0.07-(-0.07)"},

            {"input": [0.074, 0.12, -0.4, 4.0, -1.7, 3.0, -5.1, 0.57, -54.0,
                       -41.0, -5.2, -5.6, 3.8, 0.054, -35.0, -5.0, -0.005,
                       0.034],
             "answer": 58.0,
             "explanation": "4.0-(-54.0)"},

            {"input": [29.0, 0.47, -4.5, -6.7, -0.051, -0.82, -0.074, -4.0,
                       -0.015, -0.015, -8.0, -0.43],
             "answer": 37.0,
             "explanation": "29.0-(-8.0)"},

            {"input": [-0.036, -0.11, -0.55, -64.0],
             "answer": 63.964,
             "explanation": "-0.036-(-64.0)"},

            {"input": [-0.092, -0.079, -0.31, -0.87, -28.0, -6.2, -0.097, -5.8,
                       -0.025, -28.0, -4.7, -2.9, -8.0, -0.093, -13.0, -73.0],
             "answer": 72.975,
             "explanation": "-0.025-(-73.0)"},

            {"input": [-0.015, 7.6],
             "answer": 7.615,
             "explanation": "7.6-(-0.015)"},

            {"input": [-46.0, 0.19, -0.08, -4.0, 4.4, 0.071, -0.029, -0.034,
                       28.0, 0.043, -97.0],
             "answer": 125.0,
             "explanation": "28.0-(-97.0)"},

            {"input": [32.0, -0.07, -0.056, -6.4, 0.084],
             "answer": 38.4,
             "explanation": "32.0-(-6.4)"},

            {"input": [0.017, 0.015, 0.69, 0.78],
             "answer": 0.765,
             "explanation": "0.78-0.015"},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
