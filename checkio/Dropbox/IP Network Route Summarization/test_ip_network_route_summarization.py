import unittest

from ip_network_route_summarization import checkio


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": ["172.16.12.0", "172.16.13.0",
                          "172.16.14.0", "172.16.15.0"],
                "answer": "172.16.12.0/22"
            },
            {
                "input": ["172.16.12.0", "172.16.13.0", "172.155.43.9"],
                "answer": '172.0.0.0/8'
            },
            {
                "input": ["172.16.12.0", "172.16.13.0",
                          "172.155.43.9", "146.11.2.2"],
                "answer":'128.0.0.0/2'
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
