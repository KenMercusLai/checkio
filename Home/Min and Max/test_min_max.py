import unittest
from min_max import min, max


class Tests(unittest.TestCase):
    TESTS = {
        "1. Basics": [
            {'input': "max(3, 2)",
             'answer': 3},
            {'input': "min(3, 2)",
             'answer': 2},
            {'input': "max([1, 2, 0, 3, 4])",
             'answer': 4},
            {'input': "min('hello')",
             'answer': "e"},
            {'input': "max(2.2, 5.6, 5.9, key=int)",
             'answer': 5.6},
            {'input': "min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1])",
             'answer': [9, 0]}
        ],
        "Extra": [
            {'input': "max([0])",
             'answer': 0},
            {'input': "min((9,))",
             'answer': 9},
            {'input': "max(range(6))",
             'answer': 5},
            {'input': "min(abs(i) for i in range(-10, 10))",
             'answer': 0},
            {'input': "max(x + 5 for x in range(6))",
             'answer': 10},
            {'input': 'max(filter(str.isalpha,"@v$e56r5CY{]"))',
             'answer': 'v'},
            {'input': "min({1, 2, 3, 4, -10})",
             'answer': -10},
            {'input': "max(set('djsaljldsklfjzx'))",
             'answer': "z"},
            {'input': "min(set('djsaljldsklfjzx'))",
             'answer': "a"},
            {'input': "max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1])",
             'answer': [7]},
            {'input': "min([1, 2, 3], [5, 6], [7], [0, 0, 0, 10], key=sum)",
             'answer': [1, 2, 3]},
            {'input': "max(True, False, -1, key=lambda x: not x)",
             'answer': False},
            {'input': "min(True, False, -1)",
             'answer': -1},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['1. Basics']:
            assert eval(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert eval(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
