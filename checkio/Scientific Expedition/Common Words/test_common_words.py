import unittest

from common_words import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": ["hello,world", "hello,earth"], "answer": "hello"},
            {"input": ["one,two,three", "four,five,six"], "answer": ""},
            {
                "input": ["one,two,three", "four,five,one,two,six,three"],
                "answer": "one,three,two",
            },
        ],
        "Extra": [
            {
                "input": [
                    "soccer,final,guitar,club,hammer",
                    "foraging,mediocre,frog,send,cleaning,guardian,thudding,soccer,water",
                ],
                "answer": "soccer",
            },
            {
                "input": [
                    "final,fun,xylophone,teacher,zebra,sausage,pencil,chair",
                    "banana,mediocre,softly,final,teacher,violently,moon",
                ],
                "answer": "final,teacher",
            },
            {
                "input": [
                    "uncle,musical,website,pencil,zebra,ink,hammer,teacher",
                    "hammer,literature,penguin,two,musical,computer,school,fun,network,pencil",
                ],
                "answer": "hammer,musical,pencil",
            },
            {
                "input": [
                    "mega,cloud,two,website,final",
                    "window,penguin,literature,network,fun,cloud,final,sausage",
                ],
                "answer": "cloud,final",
            },
            {
                "input": [
                    "final,pencil,school,dog,two,banana,moon,zebra,literature,ink",
                    "banana,sausage,window,uncle,ink,mediocre,cords,moon,network,fun",
                ],
                "answer": "banana,ink,moon",
            },
            {
                "input": ["penguin,home,zebra,computer", "penguin,home,zebra,computer"],
                "answer": "computer,home,penguin,zebra",
            },
            {"input": ["blubber,hammer", "hammer"], "answer": "hammer"},
            {
                "input": [
                    "website,violently,cords,walking,xylophone,final",
                    "blubber,sausage,computer,softly,penguin,moon",
                ],
                "answer": "",
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
