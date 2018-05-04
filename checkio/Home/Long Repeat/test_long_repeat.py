import unittest

from long_repeat import long_repeat


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": "sdsffffse",
                "answer": 4
            },
            {
                "input": "ddvvrwwwrggg",
                "answer": 3
            }
        ],
        "Extra": [
            {
                "input": "",
                "answer": 0
            }, {
                "input": "abababaab",
                "answer": 2
            }, {
                "input": "abababa",
                "answer": 1
            }, {
                "input": "aa",
                "answer": 2
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert long_repeat(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert long_repeat(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
