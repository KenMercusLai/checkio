import unittest
from ..simplification import simplify, Polynomial


class Tests(unittest.TestCase):

    def test_Polynomial(self):
        assert str(Polynomial([1]) + Polynomial([1])) == '2'
        assert str(Polynomial([3]) + Polynomial([0, 4]) +
                   Polynomial([-24]) + Polynomial([0, -2])) == '2*x-21'
        assert str(Polynomial([-1, 1]) * Polynomial([-1, 1])) == 'x**2-2*x+1'
        assert str(-Polynomial([-1, 1])) == '-1*x+1'
        assert str(-Polynomial([1])) == '-1'
        assert str(Polynomial([-2, 2]) * Polynomial([2, 2])) == '4*x**2-4'
        assert str(Polynomial([-2, 1]) * Polynomial([2, 1])
                   * Polynomial([2, 1])) == 'x**3+2*x**2-4*x-8'
        assert str(Polynomial([2]) * Polynomial([3, 2]) -
                   Polynomial([0, 1]) + Polynomial([0, 0, 0, 0, 1])) == 'x**4+3*x+6'

    def test_Extra(self):
        assert simplify('(x-1)*(x-1)') == 'x**2-2*x+1'
        assert simplify('(x+3)*(x+3)') == 'x**2+6*x+9'
        assert simplify('(x+4)*x*3-x*x') == '2*x**2+12*x'
        assert simplify('x+x*x+x*x*x*x') == 'x**4+x**2+x'
        assert simplify('2*(2*x+3)-x+x*x*x*x') == 'x**4+3*x+6'
        assert simplify('3+4*x-24-2*x') == '2*x-21'
        assert simplify('(x+1)*x*(x+1)') == 'x**3+2*x**2+x'
        assert simplify('x*x*x*x*x+100-2') == 'x**5+98'
        assert simplify('(x-500)*(x+500)') == 'x**2-250000'
        assert simplify('(x-2)*(x+2)*(x+2)') == 'x**3+2*x**2-4*x-8'

    def test_Generated(self):
        assert simplify(
            '84-x+x*37*80+78-98+x-(x)+(23)*x+x-x+x+78-(x*32+61+x-10*x*x)-(59*x)-(x)-x*49+x+23*72+0+(x+x)+(x*(x))') == '11*x**2+2844*x+1737'
        assert simplify(
            '74-x-15+x+31*x+95*(x+88)*38-x-25-23+x*x+49+x-(47+x+28-43*x-x-39+x-x-83*62)') == 'x**2+3684*x+322850'
        assert simplify(
            '(x+13-(x*x*x)*x-(x)-x+19-x*10*(x*62)+x-x*0*(66)*83-93+x-(21*x+(85-77+x-x)))') == '-x**4-620*x**2-20*x-69'
        assert simplify(
            '79+15*7-x+x-x+48-65+x-38+x+46*x*x*(3)+0+(45)') == '138*x**2+x+174'
        assert simplify(
            '98*85*x*(x-x-(x*(x-41-(x)+3-31+(41)*54*13-x+(x))))') == '-239179290*x**2'
        assert simplify(
            '24*45*(23*42+73-x)-x-75-13-41*(47-49*(x*25*(x*(x-(x-48*16+55*97)+x-54))))') == '50225*x**3-232089725*x**2-1081*x+1120105'
        assert simplify(
            'x+x-x+x*x+x*x*x-x*x*x*(4*x+84*x*x-x*x*x-x-x)+x-x-x') == 'x**6-84*x**5-2*x**4+x**3+x**2'
        assert simplify('72*x*x-(x+x-x*x)+x*81') == '73*x**2+79*x'
        assert simplify(
            '11+(x)*(x*x)*x*(x+x*20-(15)*x-(40+(x)-(x*x*x+x+x)*x+47-(x)))') == 'x**8+2*x**6+6*x**5-87*x**4+11'

    def test_Basics(self):
        assert simplify('(x-1)*(x+1)') == 'x**2-1'
        assert simplify('(x+1)*(x+1)') == 'x**2+2*x+1'
        assert simplify('(x+3)*x*2-x*x') == 'x**2+6*x'
        assert simplify('x+x*x+x*x*x') == 'x**3+x**2+x'
        assert simplify('(2*x+3)*2-x+x*x*x*x') == 'x**4+3*x+6'
        assert simplify('x*x-(x-1)*(x+1)-1') == '0'
        assert simplify('5-5-x') == '-x'
        assert simplify('x*x*x-x*x*x-1') == '-1'
