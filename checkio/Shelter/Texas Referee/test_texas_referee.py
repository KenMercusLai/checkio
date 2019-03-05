import unittest

from texas_referee import texas_referee


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": "Kh,Qh,Ah,9s,2c,Th,Jh", "answer": "Ah,Kh,Qh,Jh,Th"},
            {"input": "Qd,Ad,9d,8d,Td,Jd,7d", "answer": "Qd,Jd,Td,9d,8d"},
            {"input": "5c,7h,7d,9s,9c,8h,6d", "answer": "9c,8h,7h,6d,5c"},
            {"input": "Ts,2h,2d,3s,Td,3c,Th", "answer": "Th,Td,Ts,3c,3s"},
            {"input": "Jh,Js,9h,Jd,Th,8h,Td", "answer": "Jh,Jd,Js,Th,Td"},
            {"input": "Js,Td,8d,9s,7d,2d,4d", "answer": "Td,8d,7d,4d,2d"},
            {"input": "Ts,2h,Tc,3s,Td,3c,Th", "answer": "Th,Td,Tc,Ts,3c"},
            {"input": "Ks,9h,Th,Jh,Kd,Kh,8s", "answer": "Kh,Kd,Ks,Jh,Th"},
            {"input": "2s,3s,4s,5s,2d,7h,8h", "answer": "8h,7h,5s,2d,2s"},
            {"input": "2c,3s,4s,5s,7s,2d,7h", "answer": "7h,7s,5s,2d,2c"},
            {"input": "3h,4h,Th,6s,Ad,Jc,2h", "answer": "Ad,Jc,Th,6s,4h"},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert texas_referee(i['input']) == i['answer']
