import unittest

from repeating_decimals import convert


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": [1, 3], "answer": "0.(3)"},
            {"input": [5, 3], "answer": "1.(6)"},
            {"input": [3, 8], "answer": "0.375"},
            {"input": [7, 11], "answer": "0.(63)"},
            {"input": [29, 12], "answer": "2.41(6)"},
            {"input": [11, 7], "answer": "1.(571428)"},
            {"input": [23, 2], "answer": "11.5"},
            {"input": [2, 21], "answer": "0.(095238)"},
            {"input": [1, 17], "answer": "0.(0588235294117647)"},
            {"input": [58, 23], "answer": "2.(5217391304347826086956)"},
            {"input": [0, 117], "answer": "0."},
            {"input": [4, 2], "answer": "2."},
        ],
        "Edge": [
            {"input": [0, 1], "answer": "0."},
            {"input": [0, 1000], "answer": "0."},
            {"input": [1, 1], "answer": "1."},
            {"input": [1, 1000], "answer": "0.001"},
            {"input": [1000, 1], "answer": "1000."},
            {"input": [1, 999], "answer": "0.(001)"},
            {
                "input": [1, 776],
                "answer": "0.001(288659793814432989690721649484536082474226804123711340206185567010309278350515463917525773195876)",
            },
        ],
        "Extra": [
            {"input": [2, 3], "answer": "0.(6)"},
            {"input": [5, 2], "answer": "2.5"},
            {"input": [6, 4], "answer": "1.5"},
            {"input": [20, 6], "answer": "3.(3)"},
            {"input": [11, 13], "answer": "0.(846153)"},
            {"input": [22, 13], "answer": "1.(692307)"},
            {"input": [18, 23], "answer": "0.(7826086956521739130434)"},
            {"input": [30, 23], "answer": "1.(3043478260869565217391)"},
            {"input": [10, 12], "answer": "0.8(3)"},
            {"input": [41, 12], "answer": "3.41(6)"},
            {"input": (408, 77), "answer": "5.(298701)"},
            {
                "input": (944, 547),
                "answer": "1.(7257769652650822669104204753199268738574040219378427787934186471663619744058500914076782449)",
            },
            {"input": (113, 927), "answer": "0.(1218985976267529665587918015102481)"},
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert convert(*i['input']) == i['answer']

    def test_Edge(self):
        for i in self.TESTS['Edge']:
            assert convert(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert convert(*i['input']) == i['answer']
