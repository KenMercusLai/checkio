import unittest

from safe_coasts import finish_map


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": (
                    'D..XX.....',
                    '...X......',
                    '.......X..',
                    '.......X..',
                    '...X...X..',
                    '...XXXXX..',
                    'X.........',
                    '..X.......',
                    '..........',
                    'D...X....D',
                ),
                "answer": [
                    'DDSXXSDDDD',
                    'DDSXSSSSSD',
                    'DDSSSSSXSD',
                    'DDSSSSSXSD',
                    'DDSXSSSXSD',
                    'SSSXXXXXSD',
                    'XSSSSSSSSD',
                    'SSXSDDDDDD',
                    'DSSSSSDDDD',
                    'DDDSXSDDDD',
                ],
            },
            {
                "input": (
                    '........',
                    '........',
                    'X.X..X.X',
                    '........',
                    '...D....',
                    '........',
                    'X.X..X.X',
                    '........',
                    '........',
                ),
                "answer": [
                    'SSSSSSSS',
                    'SSSSSSSS',
                    'XSXSSXSX',
                    'SSSSSSSS',
                    'DDDDDDDD',
                    'SSSSSSSS',
                    'XSXSSXSX',
                    'SSSSSSSS',
                    'SSSSSSSS',
                ],
            },
            {
                "input": ('.....', '.....', '..D..', '.....', '.....'),
                "answer": ['DDDDD', 'DDDDD', 'DDDDD', 'DDDDD', 'DDDDD'],
            },
            {
                "input": ('D...D', '.....', '..X..', '.....', 'D...D'),
                "answer": ['DDDDD', 'DSSSD', 'DSXSD', 'DSSSD', 'DDDDD'],
            },
            {
                "input": (
                    'XXXXXXX',
                    'X.....X',
                    'X..D..X',
                    'X.DDD.X',
                    'X..D..X',
                    'X.....X',
                    'XXXXXXX',
                ),
                "answer": [
                    'XXXXXXX',
                    'XSSSSSX',
                    'XSDDDSX',
                    'XSDDDSX',
                    'XSDDDSX',
                    'XSSSSSX',
                    'XXXXXXX',
                ],
            },
        ],
        "Extra": [
            {"input": ('...', '.D.', '...'), "answer": ['DDD', 'DDD', 'DDD']},
            {
                "input": (
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '..........',
                    '.........D',
                ),
                "answer": [
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                    'DDDDDDDDDD',
                ],
            },
            {
                "input": (
                    'D.XXXXXXXX',
                    '..XXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXX..',
                    'XXXXXXXX.D',
                ),
                "answer": [
                    'DSXXXXXXXX',
                    'SSXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXXX',
                    'XXXXXXXXSS',
                    'XXXXXXXXSD',
                ],
            },
            {
                "input": ('DDD', 'DDD', 'D.D', 'DDD', 'DDD'),
                "answer": ['DDD', 'DDD', 'DDD', 'DDD', 'DDD'],
            },
            {
                "input": (
                    '..........',
                    '.D.......X',
                    '..........',
                    '..........',
                    '......X...',
                    '..........',
                    '..........',
                    '...X......',
                    '..........',
                    '..........',
                    'X.........',
                ),
                "answer": [
                    'DDDDDDDDSS',
                    'DDDDDDDDSX',
                    'DDDDDDDDSS',
                    'DDDDDSSSSS',
                    'DDDDDSXSSS',
                    'DDDDDSSSSS',
                    'DDSSSSSSSS',
                    'DDSXSSSSSS',
                    'DDSSSSSSSS',
                    'SSSSSSSSSS',
                    'XSSSSSSSSS',
                ],
            },
            {
                "input": (
                    'D.........',
                    '..........',
                    '..XXXXXX..',
                    '..X....X..',
                    '..X....X..',
                    '..X.......',
                    '..X.......',
                    '..XXX.....',
                    '.........X',
                    '..........',
                    '......X...',
                ),
                "answer": [
                    'DDDDDDDDDD',
                    'DSSSSSSSSD',
                    'DSXXXXXXSD',
                    'DSXSSSSXSD',
                    'DSXSSSSXSD',
                    'DSXSSSSSSD',
                    'DSXSSSDDDD',
                    'DSXXXSDDSS',
                    'DSSSSSDDSX',
                    'DDDDDSSSSS',
                    'DDDDDSXSSS',
                ],
            },
            {
                "input": (
                    '.X....X..',
                    '....X....',
                    '.........',
                    '.........',
                    '.........',
                    '.X.D..X..',
                    '.......XX',
                ),
                "answer": [
                    'SXSSSSXSD',
                    'SSSSXSSSD',
                    'DDDSSSDDD',
                    'DDDDDDDDD',
                    'SSSDDSSSD',
                    'SXSDDSXSS',
                    'SSSDDSSXX',
                ],
            },
            {
                "input": (
                    '...D...',
                    '.......',
                    'X......',
                    '.......',
                    '.......',
                    'XXXX...',
                    'X.....D',
                ),
                "answer": [
                    'DDDDDDD',
                    'SSDDDDD',
                    'XSDDDDD',
                    'SSDDDDD',
                    'SSSSSDD',
                    'XXXXSDD',
                    'XSSSSDD',
                ],
            },
            {
                "input": (
                    'D..X...X',
                    '.D...X..',
                    '.....X..',
                    '.X...XX.',
                    '...X....',
                    '..XX..X.',
                    'X.......',
                    '........',
                ),
                "answer": [
                    'DDSXSSSX',
                    'DDSSSXSS',
                    'SSSSSXSS',
                    'SXSSSXXS',
                    'SSSXSSSS',
                    'SSXXSSXS',
                    'XSSSSSSS',
                    'SSSSSSSS',
                ],
            },
            {
                "input": (
                    '.X.....X.X',
                    '....X.XX..',
                    'X.....X...',
                    'X..X...X.X',
                    '....XX.X..',
                    'D...X.....',
                    'DD...X.XX.',
                    '....X..X.X',
                    '.XX.......',
                ),
                "answer": [
                    'SXSSSSSXSX',
                    'SSSSXSXXSS',
                    'XSSSSSXSSS',
                    'XSSXSSSXSX',
                    'SSSSXXSXSS',
                    'DDDSXSSSSS',
                    'DDDSSXSXXS',
                    'SSSSXSSXSX',
                    'SXXSSSSSSS',
                ],
            },
            {
                "input": (
                    '.......XX.',
                    'XX..X...X.',
                    '........X.',
                    '.......X..',
                    '......X.X.',
                    '...XX....X',
                    '...XX.X.X.',
                    'X....X....',
                    '..D....D.X',
                ),
                "answer": [
                    'SSSSSSSXXS',
                    'XXSSXSSSXS',
                    'SSSSSSSSXS',
                    'SSSSSSSXSS',
                    'SSSSSSXSXS',
                    'SSSXXSSSSX',
                    'SSSXXSXSXS',
                    'XSSSSXSSSS',
                    'SSDDSSSDSX',
                ],
            },
            {
                "input": (
                    'X........X',
                    '...X.XXXX.',
                    'X.......X.',
                    '....X.....',
                    '.XXX......',
                    '......XX..',
                    '.X...X....',
                    '..XX.....D',
                ),
                "answer": [
                    'XSSSSSSSSX',
                    'SSSXSXXXXS',
                    'XSSSSSSSXS',
                    'SSSSXSSSSS',
                    'SXXXSSSSSD',
                    'SSSSSSXXSD',
                    'SXSSSXSSSD',
                    'SSXXSSSDDD',
                ],
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert finish_map(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert finish_map(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
