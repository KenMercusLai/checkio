import unittest

from the_longest_palindromic import longest_palindromic


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": "abc", "answer": "a"},
            {"input": "abacada", "answer": "aba"},
            {"input": "artrartrt", "answer": "rtrartr"},
            {"input": "aaaaa", "answer": "aaaaa"},
        ],
        "Extra": [
            {"input": "so sad das-li", "answer": "sad das"},
            {"input": " a b c", "answer": " a "},
            {"input": "1", "answer": "1"},
            {
                "input": "123abcba",
                "answer": "abcba",
                "explanation": "At the end of text",
            },
            {
                "input": "abcba123abcdcba",
                "answer": "abcdcba",
                "explanation": "Two palindromes in text",
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert longest_palindromic(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert longest_palindromic(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
