import unittest

from the_fastest_horse import fastest_horse


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": [['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']],
                "answer": 3
            },
            {
                "input": [['1:10', '1:15', '1:20'], ['1:05', '1:10', '1:15'], ['2:59', '2:59', '2:59']],
                "answer": 1
            }
        ],
        "Extra": [
            {
                "input": [['4:44', '4:11', '4:18'], ['3:10', '3:01', '3:14'], ['2:20', '2:23', '2:15']],
                "answer": 2
            },
            {
                "input": [
                    ['1:55', '1:50', '1:45', '1:40', '1:35'],
                    ['2:55', '2:50', '2:45', '2:40', '2:35'],
                    ['3:55', '3:50', '3:45', '3:40', '3:35'],
                    ['4:55', '4:50', '4:45', '4:40', '4:35'],
                    ['3:55', '3:50', '3:45', '3:40', '3:35'],
                    ['2:35', '2:40', '2:45', '2:50', '2:55']
                ],
                "answer": 5
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert fastest_horse(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert fastest_horse(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
