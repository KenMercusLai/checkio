import unittest

from cipher_map import recall_password


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [
                    [
                        "X...",
                        "..X.",
                        "X..X",
                        "...."
                    ],
                    [
                        "itdf",
                        "gdce",
                        "aton",
                        "qrdi"
                    ]
                ],
                "answer": "icantforgetiddqd"
            },
            {
                "input": [
                    [
                        "....",
                        "X..X",
                        ".X..",
                        "...X"
                    ],
                    [
                        "xhwc",
                        "rsqx",
                        "xqzz",
                        "fyzr"
                    ]
                ],
                "answer": "rxqrwsfzxqxzhczy"
            },

        ],
        "Edge": [
            {
                "input": [
                    [
                        "X...",
                        ".X..",
                        "..X.",
                        "...X",
                    ],
                    [
                        "aaaa",
                        "aaaa",
                        "aaaa",
                        "aaaa"
                    ]
                ],
                "answer": "aaaaaaaaaaaaaaaa"
            },
            {
                "input": [
                    [
                        "X..X",
                        "....",
                        "....",
                        "X..X",
                    ],
                    [
                        "abcd",
                        "efgh",
                        "ijkl",
                        "mnop"
                    ]
                ],
                "answer": "admpadmpadmpadmp"
            },
            {
                "input": [
                    [
                        "....",
                        ".XX.",
                        ".XX.",
                        "....",
                    ],
                    [
                        "abcd",
                        "efgh",
                        "ijkl",
                        "mnop"
                    ]
                ],
                "answer": "fgjkfgjkfgjkfgjk"
            },
        ],
        "Extra": [
            {
                "input": [
                    [
                        "X...",
                        ".X..",
                        "..X.",
                        "...X"
                    ],
                    [
                        "azbx",
                        "azbx",
                        "azbx",
                        "azbx"
                    ]
                ],
                "answer": "azbxxbzaazbxxbza"
            },
            {
                "input": [
                    [
                        "XXXX",
                        "....",
                        "....",
                        "....",
                    ],
                    [
                        "call",
                        "rsqi",
                        "epzn",
                        "yeee"
                    ]
                ],
                "answer": "calllineyeeecrey"
            },
            {
                "input": [
                    [
                        "X...",
                        "X...",
                        "X...",
                        "X...",
                    ],
                    [
                        "call",
                        "rsqi",
                        "epzn",
                        "yeee"
                    ]
                ],
                "answer": "creycalllineyeee"
            },
            {
                "input": [
                    [
                        "X...",
                        "..X.",
                        ".X..",
                        "...X",
                    ],
                    [
                        "name",
                        "goto",
                        "line",
                        "nope"
                    ]
                ],
                "answer": "ntieeonnntieeonn"
            },
            {
                "input": [
                    [
                        "XX..",
                        "....",
                        "....",
                        "..XX",
                    ],
                    [
                        "cree",
                        "band",
                        "test",
                        "yepp"
                    ]
                ],
                "answer": "crppedtycrppedty"
            },
            {
                "input": [
                    [
                        "....",
                        "X..X",
                        "X..X",
                        "....",
                    ],
                    [
                        "cree",
                        "band",
                        "test",
                        "yepp"
                    ]
                ],
                "answer": "bdttreepbdttreep"
            },

            {
                "input": [
                    [
                        "...X",
                        "..X.",
                        "..X.",
                        "...X",
                    ],
                    [
                        "aazz",
                        "aazz",
                        "aazz",
                        "aazz"
                    ]
                ],
                "answer": "zzzzazazaaaaazaz"
            },



        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert recall_password(i['input'][0], i['input'][1]) == i['answer']

    def test_Edge(self):
        for i in self.TESTS['Edge']:
            assert recall_password(i['input'][0], i['input'][1]) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert recall_password(i['input'][0], i['input'][1]) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
