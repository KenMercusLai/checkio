import unittest

from completely_empty import completely_empty


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [], "answer": True},
            {"input": [[]], "answer": True},
            {"input": [[], []], "answer": True},
            {"input": [1], "answer": False},
            {"input": [[], [1]], "answer": False},
            {"input": [0], "answer": False},
            {"input": [''], "answer": True},
            {"input": [[], [{'': 'No WAY'}]], "answer": True},
            {"input": [iter(())], "answer": True},
            {"input": [(), (), ()], "answer": True},
        ],
        "Extra": [
            {"input": [[[[]]]], "answer": True},
            {"input": [[1], [1]], "answer": False},
            {"input": [None], "answer": False},
            {"input": [iter((1,))], "answer": False},
            {"input": [type('', (), {'__iter__': None})()], "answer": False},
            {"input": type('', (), {'__getitem__': ().__getitem__})(), "answer": True},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert completely_empty(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert completely_empty(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
