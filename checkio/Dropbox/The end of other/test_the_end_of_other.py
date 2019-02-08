import unittest

from the_end_of_other import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ["hello", "lo", "he"],
                "answer": True,
                "explanation": ["hel", "lo"],
            },
            {
                "input": ["hello", "la", "hellow", "cow"],
                "answer": False,
                "explanation": None,
            },
            {
                "input": ["walk", "duckwalk"],
                "answer": True,
                "explanation": ["duck", "walk"],
            },
            {"input": ["one"], "answer": False, "explanation": None},
            {"input": ["helicopter", "li", "he"], "answer": False, "explanation": None},
        ],
        "Extra": [
            {
                "input": ["a", "the", "wall", "world", "nine"],
                "answer": False,
                "explanation": None,
            },
            {
                "input": ['longest', 'aa', 'a'],
                "answer": True,
                "explanation": ["a", "a"],
            },
            {
                "input": [
                    'jsakhfakljsdfhsakjdfhljkasdhfkasdjhfjklasdhfkasdhfalksjdhejkyrieucbciuwaeiuwhewkqjiorfuvnfjhbkehraa',
                    'aarhekbhjfnvufroijqkwehwuieawuicbcueirykjehdjsklafhdsakfhdsalkjfhjdsakfhdsakjlhfdjkashfdsjlkafhkasj',
                ],
                "answer": False,
                "explanation": None,
            },
            {
                "input": ["abc", "cba", "ba", "a", "c"],
                "answer": True,
                "explanation": ["cba", "ba"],
            },
            {
                "input": ["chupacabra", "megachupacabra", "gigachupacabra"],
                "answer": True,
                "explanation": ["mega", "chupacabra"],
            },
            {
                "input": ["giga", "mega", "woltz", "kilo"],
                "answer": False,
                "explanation": None,
            },
            {
                "input": [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                    "ten",
                ],
                "answer": False,
                "explanation": None,
            },
            {
                "input": [
                    "one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                    "ten",
                    "pacsix",
                ],
                "answer": True,
                "explanation": ["pac", "six"],
            },
            {
                "input": [
                    'a',
                    'b',
                    'c',
                    'd',
                    'e',
                    'f',
                    'g',
                    'h',
                    'i',
                    'j',
                    'k',
                    'l',
                    'm',
                    'n',
                    'o',
                    'p',
                    'q',
                    'r',
                    's',
                    't',
                    'u',
                    'v',
                    'w',
                    'x',
                    'y',
                    'z',
                ],
                "answer": False,
                "explanation": None,
            },
            {
                "input": ["check", "io", "checkio"],
                "answer": True,
                "explanation": ["check", "io"],
            },
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
