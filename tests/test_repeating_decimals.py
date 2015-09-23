import unittest
from ..repeating_decimals import convert


class Tests(unittest.TestCase):

    def test_Edge(self):
        assert convert(0, 1) == "0."
        assert convert(0, 1000) == "0."
        assert convert(1, 1) == "1."
        assert convert(1, 1000) == "0.001"
        assert convert(1000, 1) == "1000."
        assert convert(1, 999) == "0.(001)"
        assert convert(1, 776) == "0.001(288659793814432989690721649484536082474226804123711340206185567010309278350515463917525773195876)"

    def test_Basics(self):
        assert convert(1, 3) == "0.(3)"
        assert convert(5, 3) == "1.(6)"
        assert convert(3, 8) == "0.375"
        assert convert(7, 11) == "0.(63)"
        assert convert(29, 12) == "2.41(6)"
        assert convert(11, 7) == "1.(571428)"
        assert convert(23, 2) == "11.5"
        assert convert(2, 21) == "0.(095238)"
        assert convert(1, 17) == "0.(0588235294117647)"
        assert convert(58, 23) == "2.(5217391304347826086956)"
        assert convert(0, 117) == "0."
        assert convert(4, 2) == "2."

    def test_Extra(self):
        assert convert(2, 3) == "0.(6)"
        assert convert(5, 2) == "2.5"
        assert convert(6, 4) == "1.5"
        assert convert(20, 6) == "3.(3)"
        assert convert(11, 13) == "0.(846153)"
        assert convert(22, 13) == "1.(692307)"
        assert convert(18, 23) == "0.(7826086956521739130434)"
        assert convert(30, 23) == "1.(3043478260869565217391)"
        assert convert(10, 12) == "0.8(3)"
        assert convert(41, 12) == "3.41(6)"
        assert convert(408, 77) == "5.(298701)"
        assert convert(944, 547) == "1.(7257769652650822669104204753199268738574040219378427787934186471663619744058500914076782449)"
        assert convert(113, 927) == "0.(1218985976267529665587918015102481)"
