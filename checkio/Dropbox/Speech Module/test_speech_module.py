import unittest

from speech_module import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": 1, "answer": "one"},
            {"input": 2, "answer": "two"},
            {"input": 3, "answer": "three"},
            {"input": 4, "answer": "four"},
            {"input": 5, "answer": "five"},
            {"input": 6, "answer": "six"},
            {"input": 9, "answer": "nine"},
            {"input": 10, "answer": "ten"},
            {"input": 11, "answer": "eleven"},
            {"input": 12, "answer": "twelve"},
            {"input": 13, "answer": "thirteen"},
            {"input": 14, "answer": "fourteen"},
            {"input": 15, "answer": "fifteen"},
            {"input": 16, "answer": "sixteen"},
            {"input": 17, "answer": "seventeen"},
            {"input": 18, "answer": "eighteen"},
            {"input": 19, "answer": "nineteen"},
            {"input": 999, "answer": "nine hundred ninety nine"},
            {"input": 784, "answer": "seven hundred eighty four"},
            {"input": 777, "answer": "seven hundred seventy seven"},
            {"input": 88, "answer": "eighty eight"},
            {"input": 44, "answer": "forty four"},
            {"input": 20, "answer": "twenty"},
            {"input": 30, "answer": "thirty"},
            {"input": 40, "answer": "forty"},
            {"input": 50, "answer": "fifty"},
            {"input": 80, "answer": "eighty"},
            {"input": 90, "answer": "ninety"},
            {"input": 100, "answer": "one hundred"},
            {"input": 200, "answer": "two hundred"},
            {"input": 300, "answer": "three hundred"},
            {"input": 600, "answer": "six hundred"},
            {"input": 700, "answer": "seven hundred"},
            {"input": 900, "answer": "nine hundred"},
            {"input": 21, "answer": "twenty one"},
            {"input": 312, "answer": "three hundred twelve"},
            {"input": 302, "answer": "three hundred two"},
            {"input": 509, "answer": "five hundred nine"},
            {"input": 753, "answer": "seven hundred fifty three"},
            {"input": 940, "answer": "nine hundred forty"},
            {"input": 999, "answer": "nine hundred ninety nine"},
        ],
        "Extra": [
            {"input": 98, "answer": "ninety eight"},
            {"input": 55, "answer": "fifty five"},
            {"input": 23, "answer": "twenty three"},
            {"input": 100, "answer": "one hundred"},
            {"input": 761, "answer": "seven hundred sixty one"},
            {"input": 637, "answer": "six hundred thirty seven"},
            {"input": 856, "answer": "eight hundred fifty six"},
            {"input": 742, "answer": "seven hundred forty two"},
            {"input": 592, "answer": "five hundred ninety two"},
            {"input": 269, "answer": "two hundred sixty nine"},
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
