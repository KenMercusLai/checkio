import unittest

from friendly_number import friendly_number


class Tests(unittest.TestCase):
    TESTS = {
        "1. Base": [
            {
                "input": [102, {}],
                "answer": '102'
            },
            {
                "input": [12341234, {'decimals': 1}],
                "answer": '12.3M'
            },
            {
                "input": [12000000, {'decimals': 3}],
                "answer": '12.000M'
            },
            {
                "input": [102, {'decimals': 2}],
                "answer": '102.00'
            },
            {
                "input": [10240, {}],
                "answer": '10k'
            },
            {
                "input": [1024000000, {'base': 1024, 'suffix': 'iB'}],
                "answer": '976MiB'
            },
            {
                "input": [-150, {'base': 100, "powers": ['', 'd', 'D']}],
                "answer": '-1d'
            },
            {
                "input": [-155, {'base': 100, "decimals": 1, "powers": ['', 'd', 'D']}],
                "answer": '-1.6d'
            },
            {
                "input": [255000000000, {"powers": ['', 'k', 'M']}],
                "answer": '255000M'
            },
        ],
        "2. Edges": [
            {
                "input": [1, {}],
                "answer": '1'
            },
            {
                "input": [0, {'decimals': 3, 'suffix': "th"}],
                "answer": '0.000th'
            },
            {
                "input": [10 ** 24, {}],
                "answer": '1Y',
                "explanation": "10**24"
            },
            {
                "input": [10 ** 32, {}],
                "answer": '100000000Y',
                "explanation": "10**32"
            },
            {
                "input": [4294967297, {'base': 2, 'powers': ["p" + str(n) for n in range(32)]}],
                "answer": '2p31'
            },
            {
                "input": [1, {'decimals': 15}],
                "answer": '1.000000000000000'
            },
        ],
        "3. Extra": [
            {
                "input": [42, {'base': 10, 'powers': ["u", "d"]}],
                "answer": '4d'
            },
            {
                "input": [42, {'powers': ["u", "d"], "suffix": "-n"}],
                "answer": '42u-n'
            },
            {
                "input": [19821904, {}],
                "answer": '19M'
            },
            {
                "input": [4000000001, {"base": 1024, "decimals": 1}],
                "answer": '3.7G'
            },
            {
                "input": [9000, {"suffix": "iB"}],
                "answer": '9kiB'
            },
        ]
    }

    def test_Base(self):
        for i in self.TESTS['1. Base']:
            [number, parameters] = i['input']
            assert friendly_number(number, **parameters) == i['answer'], i['input']

    def test_Edges(self):
        for i in self.TESTS['2. Edges']:
            [number, parameters] = i['input']
            assert friendly_number(number, **parameters) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['3. Extra']:
            [number, parameters] = i['input']
            assert friendly_number(number, **parameters) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
