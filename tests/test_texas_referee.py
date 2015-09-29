import unittest
from ..texas_referee import texas_referee


class Tests(unittest.TestCase):

    def test_Basics(self):
        assert texas_referee('Kh,Qh,Ah,9s,2c,Th,Jh') == 'Ah,Kh,Qh,Jh,Th'
        assert texas_referee('Qd,Ad,9d,8d,Td,Jd,7d') == 'Qd,Jd,Td,9d,8d'
        assert texas_referee('5c,7h,7d,9s,9c,8h,6d') == '9c,8h,7h,6d,5c'
        assert texas_referee('Ts,2h,2d,3s,Td,3c,Th') == 'Th,Td,Ts,3c,3s'
        assert texas_referee('Jh,Js,9h,Jd,Th,8h,Td') == 'Jh,Jd,Js,Th,Td'
        assert texas_referee('Js,Td,8d,9s,7d,2d,4d') == 'Td,8d,7d,4d,2d'
        assert texas_referee('Ts,2h,Tc,3s,Td,3c,Th') == 'Th,Td,Tc,Ts,3c'
        assert texas_referee('Ks,9h,Th,Jh,Kd,Kh,8s') == 'Kh,Kd,Ks,Jh,Th'
        assert texas_referee('2s,3s,4s,5s,2d,7h,8h') == '8h,7h,5s,2d,2s'
        assert texas_referee('2c,3s,4s,5s,7s,2d,7h') == '7h,7s,5s,2d,2c'
        assert texas_referee('3h,4h,Th,6s,Ad,Jc,2h') == 'Ad,Jc,Th,6s,4h'
