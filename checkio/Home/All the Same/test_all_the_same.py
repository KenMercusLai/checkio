import unittest

from all_the_same import all_the_same


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [1, 1, 1],
                "answer": True
            },
            {
                "input": [1, 2, 1],
                "answer": False
            },
            {
                "input": [],
                "answer": True,
                "explanation": "All elements in empty list are equal"
            },
            {
                "input": [1],
                "answer": True,
                "explanation": "List contains only one element."
            }
        ],
        "Extra": [
            {
                "input": [1, 'a', 1],
                "answer": False
            },
            {
                "input": [600000],
                "answer": True
            },
            {
                "input": [10000, 99999],
                "answer": False
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert all_the_same(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert all_the_same(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
