import unittest
from boolean_algebra import boolean


class Tests(unittest.TestCase):
    TESTS = {
        "Basic": [
            {
                "input": [0, 0, 'conjunction'],
                "answer": 0,
            },
            {
                "input": [0, 1, 'conjunction'],
                "answer": 0,
            },
            {
                "input": [1, 0, 'conjunction'],
                "answer": 0,
            },
            {
                "input": [1, 1, 'conjunction'],
                "answer": 1,
            },
            {
                "input": [0, 0, 'disjunction'],
                "answer": 0,
            },
            {
                "input": [0, 1, 'disjunction'],
                "answer": 1,
            },
            {
                "input": [1, 0, 'disjunction'],
                "answer": 1,
            },
            {
                "input": [1, 1, 'disjunction'],
                "answer": 1,
            },
        ],
        "Extra": [

            {
                "input": [0, 0, 'implication'],
                "answer": 1,
            },
            {
                "input": [0, 1, 'implication'],
                "answer": 1,
            },
            {
                "input": [1, 0, 'implication'],
                "answer": 0,
            },
            {
                "input": [1, 1, 'implication'],
                "answer": 1,
            },
            {
                "input": [0, 0, 'exclusive'],
                "answer": 0,
            },
            {
                "input": [0, 1, 'exclusive'],
                "answer": 1,
            },
            {
                "input": [1, 0, 'exclusive'],
                "answer": 1,
            },
            {
                "input": [1, 1, 'exclusive'],
                "answer": 0,
            },
            {
                "input": [0, 0, 'equivalence'],
                "answer": 1,
            },
            {
                "input": [0, 1, 'equivalence'],
                "answer": 0,
            },
            {
                "input": [1, 0, 'equivalence'],
                "answer": 0,
            },
            {
                "input": [1, 1, 'equivalence'],
                "answer": 1,
            },
        ]
    }

    def test_Basic(self):
        for i in self.TESTS['Basic']:
            assert boolean(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert boolean(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
