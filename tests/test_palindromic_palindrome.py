import unittest
from ..palindromic_palindrome import checkio

class Tests(unittest.TestCase):

    def test_Code(self):
        code = open('palindromic_palindrome.py').read()
        if '#' in code:
            assert False
        assert code == code[::-1]


    def test_Extra(self):
        assert checkio("asd dsa") == True
        assert checkio("0000000000") == True
        assert checkio("master retsm") == False

    def test_Basics(self):
        assert checkio("asd") == False
        assert checkio("palindrome") == False
        assert checkio("ssssssss") == True
        assert checkio("qwertytrewq") == True
        assert checkio("123456") == False
        assert checkio("hello1olleh") == True
