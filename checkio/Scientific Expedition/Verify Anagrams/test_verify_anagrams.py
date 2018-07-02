import unittest

from verify_anagrams import verify_anagrams


class Tests(unittest.TestCase):
    TESTS = {
        "0. Basics": [
            {
                "input": ["Programming", "Gram Ring Mop"],
                "answer": True,
                "common": "programming"
            },
            {
                "input": ["Hello", "Ole Oh"],
                "answer": False,
                "common": "helo"
            },

            {
                "input": ["Kyoto", "Tokyo"],
                "answer": True,
                "common": "kyoto"
            }

        ],
        "1. Extra": [
            {
                "input": ["Hamlet", "Amleth"],
                "answer": True,
                "common": "hamlet"
            },
            {
                "input": ["Kings Lead Hat", "Talking Heads"],
                "answer": True,
                "common": "kingsleadhat"
            },
            {
                "input": ["Hello", "Hell"],
                "answer": False,
                "common": "hel"
            },

            {
                "input": ["abcdefghijklmnopqrstuvwxyz", "Cwm fjord bank glyphs vext quiz"],
                "answer": True,
                "common": "abcdefghijklmnopqrstuvwxyz"
            },
            {
                "input": ["Listen", "Silent"],
                "answer": True,
                "common": "listen"
            },
            {
                "input": ["A telephone girl", "Repeating allo"],
                "answer": False,
                "common": "atelepongirl"
            },
            {
                "input": ["Waitress", "The stew Sir"],
                "answer": False,
                "common": "witress"
            },
            {
                "input": ["The Morse Code", "There Come Dots"],
                "answer": False,
                "common": "themorsecode"
            },

        ],
        "2. Edge": [
            {
                "input": ["a", "a"],
                "answer": True,
                "common": "a"
            },
            {
                "input": ["x", "X"],
                "answer": True,
                "common": "x"
            },
            {
                "input": ["A O X", "x o a"],
                "answer": True,
                "common": "aox"
            },
            {
                "input": ["  Hi  all  ", "all hi"],
                "answer": True,
                "common": "hiall"
            },
            {
                "input": ["a", "z"],
                "answer": False,
                "common": ""
            },
            {
                "input": ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU",
                          'UTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'],
                "answer": True,
                "common": "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu"
            },
            {
                "input": ["bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU",
                          'TSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'],
                "answer": False,
                "common": "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst"
            },
            {
                "input": ["aaaaaaaaabbb", "ba"],
                "answer": False,
                "common": "ab"
            },
            {
                "input": ["a", "abcd"],
                "answer": False,
                "common": "a"
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['0. Basics']:
            assert verify_anagrams(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['1. Extra']:
            assert verify_anagrams(*i['input']) == i['answer'], i['input']

    def test_Edge(self):
        for i in self.TESTS['2. Edge']:
            assert verify_anagrams(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
