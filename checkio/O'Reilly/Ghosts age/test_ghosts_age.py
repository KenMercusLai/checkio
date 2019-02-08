import unittest

from ghosts_age import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": 9999, "answer": 1},
            {"input": 9997, "answer": 2},
            {"input": 9994, "answer": 3},
            {"input": 9995, "answer": 4},
            {"input": 9990, "answer": 5},
        ],
        "Extra": [
            {"input": 3703, "answer": 4665},
            {"input": 6736, "answer": 3516},
            {"input": 8997, "answer": 1594},
            {"input": 3387, "answer": 4349},
            {"input": 7198, "answer": 3978},
            {"input": 9598, "answer": 596},
            {"input": 9797, "answer": 183},
            {"input": 9173, "answer": 782},
            {"input": 7858, "answer": 2053},
            {"input": 8616, "answer": 1213},
            {"input": 3251, "answer": 4213},
            {"input": 3563, "answer": 4525},
            {"input": 6250, "answer": 3030},
            {"input": 9549, "answer": 547},
            {"input": 6839, "answer": 3619},
            {"input": 4035, "answer": 4997},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
