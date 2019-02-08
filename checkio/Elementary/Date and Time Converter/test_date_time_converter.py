import unittest

from date_time_converter import date_time


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": '01.01.2000 00:00',
                "answer": "1 January 2000 year 0 hours 0 minutes",
            },
            {
                "input": '09.05.1945 06:30',
                "answer": "9 May 1945 year 6 hours 30 minutes",
            },
        ],
        "Extra": [
            {
                "input": '20.11.1990 03:55',
                "answer": "20 November 1990 year 3 hours 55 minutes",
            },
            {
                "input": '09.07.1995 16:50',
                "answer": "9 July 1995 year 16 hours 50 minutes",
            },
            {
                "input": '11.04.1812 01:01',
                "answer": "11 April 1812 year 1 hour 1 minute",
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert date_time(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert date_time(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
