import unittest

from ceasar_cipher import to_encrypt


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ("a b c", 3),
                "answer": 'd e f'
            },
            {
                "input": ("a b c", -3),
                "answer": 'x y z'
            }
        ],
        "Extra": [
            {
                "input": ("simple text", 16),
                "answer": "iycfbu junj"
            },
            {
                "input": ("important text", 10),
                "answer": "swzybdkxd dohd",
            },
            {
                "input": ("state secret", -13),
                "answer": "fgngr frperg",
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert to_encrypt(i['input'][0], i['input'][1]) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert to_encrypt(i['input'][0], i['input'][1]) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
