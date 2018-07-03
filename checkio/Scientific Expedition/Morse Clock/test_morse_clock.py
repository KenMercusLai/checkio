import unittest

from morse_clock import checkio, to_binary


def test_to_binary():
    assert to_binary('0') == '0000'
    assert to_binary('1') == '0001'
    assert to_binary('2') == '0010'
    assert to_binary('3') == '0011'
    assert to_binary('4') == '0100'
    assert to_binary('5') == '0101'
    assert to_binary('6') == '0110'
    assert to_binary('7') == '0111'
    assert to_binary('8') == '1000'
    assert to_binary('9') == '1001'

    assert to_binary('0', 1) == '0'
    assert to_binary('1', 1) == '1'
    assert to_binary('2', 2) == '10'
    assert to_binary('3', 2) == '11'
    assert to_binary('4', 3) == '100'
    assert to_binary('5', 3) == '101'
    assert to_binary('6', 3) == '110'
    assert to_binary('7', 3) == '111'
    assert to_binary('8', 4) == '1000'
    assert to_binary('9', 4) == '1001'


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": "10:37:49",
                "answer": ".- .... : .-- .--- : -.. -..-",
                "explanation": "103749"
            },
            {
                "input": "21:34:56",
                "answer": "-. ...- : .-- .-.. : -.- .--.",
                "explanation": "213456"
            },
            {
                "input": "00:1:02",
                "answer": ".. .... : ... ...- : ... ..-.",
                "explanation": "000102"
            },
            {
                "input": "23:59:59",
                "answer": "-. ..-- : -.- -..- : -.- -..-",
                "explanation": "235959"
            },
            {
                "input": "0:10:2",
                "answer": ".. .... : ..- .... : ... ..-.",
                "explanation": "001002"
            }
        ],
        "Extra": [
            {
                "input": "17:0:28",
                "answer": ".- .--- : ... .... : .-. -...",
                "explanation": "170028"
            },
            {
                "input": "7:41:37",
                "answer": ".. .--- : -.. ...- : .-- .---",
                "explanation": "074137"
            },
            {
                "input": "4:25:13",
                "answer": ".. .-.. : .-. .-.- : ..- ..--",
                "explanation": "042513"
            },
            {
                "input": "15:18:8",
                "answer": ".- .-.- : ..- -... : ... -...",
                "explanation": "151808"
            },
            {
                "input": "2:32:41",
                "answer": ".. ..-. : .-- ..-. : -.. ...-",
                "explanation": "023241"
            },
            {
                "input": "9:44:31",
                "answer": ".. -..- : -.. .-.. : .-- ...-",
                "explanation": "094431"
            },
            {
                "input": "3:8:2",
                "answer": ".. ..-- : ... -... : ... ..-.",
                "explanation": "030802"
            },
            {
                "input": "5:1:9",
                "answer": ".. .-.- : ... ...- : ... -..-",
                "explanation": "050109"
            },
            {
                "input": "09:02:08",
                "answer": ".. -..- : ... ..-. : ... -...",
                "explanation": "090208"
            },
            {
                "input": "13:5:3",
                "answer": ".- ..-- : ... .-.- : ... ..--",
                "explanation": "130503"
            }
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert checkio(i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert checkio(i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
