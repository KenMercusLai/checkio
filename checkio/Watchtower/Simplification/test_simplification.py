import unittest

from simplification import simplify


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {"input": "(x-1)*(x+1)", "answer": "x**2-1"},
            {"input": "(x+1)*(x+1)", "answer": "x**2+2*x+1"},
            {"input": "(x+3)*x*2-x*x", "answer": "x**2+6*x"},
            {"input": "x+x*x+x*x*x", "answer": "x**3+x**2+x"},
            {"input": "(2*x+3)*2-x+x*x*x*x", "answer": "x**4+3*x+6"},
            {"input": "x*x-(x-1)*(x+1)-1", "answer": "0"},
            {"input": "5-5-x", "answer": "-x"},
            {"input": "x*x*x-x*x*x-1", "answer": "-1"},
        ],
        "Extra": [
            {"input": "(x-1)*(x-1)", "answer": "x**2-2*x+1"},
            {"input": "(x+3)*(x+3)", "answer": "x**2+6*x+9"},
            {"input": "(x+4)*x*3-x*x", "answer": "2*x**2+12*x"},
            {"input": "x+x*x+x*x*x*x", "answer": "x**4+x**2+x"},
            {"input": "2*(2*x+3)-x+x*x*x*x", "answer": "x**4+3*x+6"},
            {"input": "3+4*x-24-2*x", "answer": "2*x-21"},
            {"input": "(x+1)*x*(x+1)", "answer": "x**3+2*x**2+x"},
            {"input": "x*x*x*x*x+100-2", "answer": "x**5+98"},
            {"input": "(x-500)*(x+500)", "answer": "x**2-250000"},
            {"input": "(x-2)*(x+2)*(x+2)", "answer": "x**3+2*x**2-4*x-8"},
        ],
        "Generated": [
            {
                "input": "84-x+x*37*80+78-98+x-(x)+(23)*x+x-x+x+78-(x*32+61+x-10*x*x)-(59*x)-(x)-x*49+x+23*72+0+(x+x)+(x*(x))",
                "answer": "11*x**2+2844*x+1737",
            },
            {
                "input": "74-x-15+x+31*x+95*(x+88)*38-x-25-23+x*x+49+x-(47+x+28-43*x-x-39+x-x-83*62)",
                "answer": "x**2+3684*x+322850",
            },
            {
                "input": "(x+13-(x*x*x)*x-(x)-x+19-x*10*(x*62)+x-x*0*(66)*83-93+x-(21*x+(85-77+x-x)))",
                "answer": "-x**4-620*x**2-20*x-69",
            },
            {
                "input": "79+15*7-x+x-x+48-65+x-38+x+46*x*x*(3)+0+(45)",
                "answer": "138*x**2+x+174",
            },
            {
                "input": "98*85*x*(x-x-(x*(x-41-(x)+3-31+(41)*54*13-x+(x))))",
                "answer": "-239179290*x**2",
            },
            {
                "input": "24*45*(23*42+73-x)-x-75-13-41*(47-49*(x*25*(x*(x-(x-48*16+55*97)+x-54))))",
                "answer": "50225*x**3-232089725*x**2-1081*x+1120105",
            },
            {
                "input": "x+x-x+x*x+x*x*x-x*x*x*(4*x+84*x*x-x*x*x-x-x)+x-x-x",
                "answer": "x**6-84*x**5-2*x**4+x**3+x**2",
            },
            {"input": "72*x*x-(x+x-x*x)+x*81", "answer": "73*x**2+79*x"},
            {
                "input": "11+(x)*(x*x)*x*(x+x*20-(15)*x-(40+(x)-(x*x*x+x+x)*x+47-(x)))",
                "answer": "x**8+2*x**6+6*x**5-87*x**4+11",
            },
        ],
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert simplify(i['input']) == i['answer']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert simplify(i['input']) == i['answer']

    def test_Generated(self):
        for i in self.TESTS['Generated']:
            assert simplify(i['input']) == i['answer']
