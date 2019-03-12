import unittest

from hidden_word import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [
                    """DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""",
                    "ten",
                ],
                "answer": [2, 14, 2, 16],
            },
            {
                "input": [
                    """He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""",
                    "noir",
                ],
                "answer": [4, 16, 7, 16],
            },
        ],
        "Extra": [
            {
                "input": [
                    """Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.""",
                    "them",
                ],
                "answer": [4, 4, 4, 7],
            },
            {
                "input": [
                    """Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.""",
                    "stog",
                ],
                "answer": [1, 19, 4, 19],
            },
            {
                "input": [
                    """One, two! One, two! And through and through
The vorpal blade went snicker-snack!
He left it dead, and with its head
He went galumphing back.""",
                    "back",
                ],
                "answer": [4, 17, 4, 20],
            },
            {
                "input": [
                    """And hast thou slain the Jabberwock?
Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!'
He chortled in his joy.
'Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.'""",
                    "tomy",
                ],
                "answer": [2, 5, 2, 8],
            },
            {
                "input": [
                    """Humpty Dumpty sat on a wall:
Humpty Dumpty had a great fall.
All the King's horses and all the King's men
Couldn't put Humpty Dumpty in his place again.""",
                    "oast",
                ],
                "answer": [1, 16, 4, 16],
            },
            {
                "input": [
                    """Hi all!
And all goodbye!
Of course goodbye.
or not""",
                    "haoo",
                ],
                "answer": [1, 1, 4, 1],
            },
            {
                "input": [
                    """xa
xb
x""",
                    "ab",
                ],
                "answer": [1, 2, 2, 2],
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(*i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(*i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
