import unittest

from most_frequent import most_frequent


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": ['a', 'b', 'c', 'a', 'b', 'a'], "answer": 'a'},
            {"input": ['a', 'a', 'bi', 'bi', 'bi'], "answer": 'bi'},
        ],
        "Extra": [
            {"input": ['a'], "answer": 'a'},
            {"input": ['a', 'a'], "answer": 'a'},
            {"input": ['a', 'a', 'z'], "answer": 'a'},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert most_frequent(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert most_frequent(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
