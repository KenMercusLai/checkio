import unittest

from house_password import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": "ULFFunH8ni",
                "answer": True
            },
            {
                "input": "aaaaaaaaaaaaaaaaaaaaa",
                "answer": False
            },
            {
                "input": "aA1",
                "answer": False
            },
            {
                "input": "awzbdzkfz",
                "answer": False
            },
            {
                "input": "RCAGOSHTTS",
                "answer": False
            },
            {
                "input": "6691219721",
                "answer": False
            },
            {
                "input": "PVlppfwrT",
                "answer": False
            },
            {
                "input": "45ae5lkgz",
                "answer": False
            },
            {
                "input": "1cmuPF1Ycz",
                "answer": True
            },
            {
                "input": "Pv4HdnUNb",
                "answer": False
            },
            {
                "input": "jRNfXg6CdM15SLChALq",
                "answer": True
            },
            {
                "input": "HZeLrcRR3NU5KprAybp",
                "answer": True
            },
            {
                "input": "aaaaaaaaaa1A",
                "answer": True
            },
            {
                "input": "aaaaaaaaa1Za",
                "answer": True
            },
            {
                "input": "aaaaaaaaa9Aa",
                "answer": True
            },
            {
                "input": "AAAAAAAAA1zA",
                "answer": True
            },
        ],
        "Extra": [

            {
                "input": "1",
                "answer": False
            },

            {
                "input": "vcugdgywnlj",
                "answer": False
            },
            {
                "input": "abcdef",
                "answer": False
            },
            {
                "input": "ABCDEF",
                "answer": False
            },
            {
                "input": "HJKKJDSHJKHDKWJWDW",
                "answer": False
            },
            {
                "input": "123456",
                "answer": False
            },
            {
                "input": "123456789012",
                "answer": False
            },
            {
                "input": "fsDSkjSD",
                "answer": False
            },
            {
                "input": "fsDSkjSDDSJhjhjd",
                "answer": False
            },
            {
                "input": "gfh123",
                "answer": False
            },
            {
                "input": "erer798rew9rew9r7ew987rw",
                "answer": False
            },
            {
                "input": "DHJK8768D",
                "answer": False
            },
            {
                "input": "DHJK87DSKJHWW68D",
                "answer": False
            },
            {
                "input": "Fa11con77",
                "answer": False
            },
            {
                "input": "Fa11con77YES",
                "answer": True
            },
            {
                "input": "Fa11con777",
                "answer": True
            },
            {
                "input": "aaaaaaaaaaaaaaaaaaaaaaaaaa"
                         "SSSSSSSSSSSSSSSSSSSSSSSSS111111111111",
                "answer": True
            },

            {
                "input": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJ"
                         "KLMNOPQRSTUVWXYZ0123456789",
                "answer": True
            },
            {
                "input": "9876543210ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvut"
                         "srqponmlkjihgfedcba",
                "answer": True
            },
            {
                "input": "IAKxnvZokrsWP1S0NCfJq4pti9Q6c8gXmB2alzuwUVR"
                         "bD73OGE5HjMTFYLyhed",
                "answer": True
            },
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
